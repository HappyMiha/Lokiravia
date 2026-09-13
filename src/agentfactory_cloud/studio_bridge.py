"""Opt-in connection from a creator's saved brief to Core on this same PC."""
from contextlib import asynccontextmanager
import os
from pathlib import Path
from urllib.parse import urlsplit

from fastapi import HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt


class Launch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    expected_revision: StrictInt = Field(ge=1)
    confirmed: StrictBool


def install_routes(app, store, *, workspace=None, core_url=None):
    configured = workspace or os.environ.get("LOKIRAVIA_CORE_WORKSPACE")
    root = Path(configured).expanduser().resolve() if configured else None
    url = (core_url or os.environ.get("LOKIRAVIA_CORE_URL", "http://127.0.0.1:8765")).rstrip("/")
    parsed = urlsplit(url)
    if (parsed.scheme not in {"http", "https"} or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
            or parsed.username or parsed.password or parsed.path or parsed.query or parsed.fragment):
        raise ValueError("The local Core bridge requires a loopback origin")
    runner = None
    if root:
        from agent_factory.studio_runner import StudioRunner
        runner = StudioRunner(root / ".agent-factory" / "state.db", root)
        prior = app.router.lifespan_context
        @asynccontextmanager
        async def lifespan(app):
            async with prior(app):
                try:
                    yield
                finally:
                    runner.close()
        app.router.lifespan_context = lifespan

    @app.get("/api/studio/connection")
    def connection():
        return {"configured": root is not None, "scope": "local_planning",
                "core_url": url if root else None}

    @app.post("/api/briefs/{ident}/studio", status_code=202)
    def launch(ident: str, request: Request, body: Launch):
        principal = request.state.local_principal
        if (principal is None or not {"write", "control"} <= principal.scopes
                or not ({"local", "*"} & principal.tenants)):
            raise HTTPException(403, "Studio execution access is required.")
        actor = principal.actor
        brief = store.get(ident, actor)
        if not body.confirmed:
            raise HTTPException(400, "Confirm starting local planning.")
        if body.expected_revision != brief["revision"]:
            raise HTTPException(409, "Reload the latest saved idea before starting.")
        if root is None:
            raise HTTPException(409, "Connect Core on this computer first.")
        from agent_factory.studio_start import create_local_game
        # The stable brief revision is the replay key. A lost HTTP response must
        # never produce another mission or another paid/model request.
        fields = brief.get("fields", {})
        title = fields.get("title", "").strip() or brief["original_text"][:100]
        idea = brief["original_text"]
        if any(str(value).strip() for value in fields.values()):
            idea += "\n\nSaved creator brief:\n" + "\n".join(
                f"{key}: {value}" for key, value in fields.items() if str(value).strip())
        try:
            result = create_local_game(root / ".agent-factory" / "state.db", root,
                                       actor=actor, command_id=f"lokiravia:{ident}:{brief['revision']}",
                                       title=title, idea=idea, runner=runner)
        except (KeyError, ValueError, OSError):
            raise HTTPException(409, "Qualify the local Core worker before starting.") from None
        return result | {"url": url + result["url"]}
