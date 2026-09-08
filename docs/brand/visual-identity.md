# Lokiravia visual identity

**Lokiravia** is the creative product formerly called AgentFactory Cloud. Its endorsement is **Lokiravia by Lokvetia**. Lokvetia is the family brand, and **Lokvetia Core** is the separate local AI agent orchestration product. Use the full relationship in introductions and the compact “by Lokvetia” line in the product lockup.

The identity gives game ideas a warm, welcoming workspace. Its geometric L shares the structure of the Lokvetia Core mark; an amber spark replaces Core's square. The spark represents a new idea, not AI execution, a completed build, or permission to publish.

## Canonical assets

| Asset | Repository path | Served path |
| --- | --- | --- |
| Mark and SVG favicon | [`src/agentfactory_cloud/static/brand-mark.svg`](../../src/agentfactory_cloud/static/brand-mark.svg) | `/static/brand-mark.svg` |
| Full wordmark | [`src/agentfactory_cloud/static/brand-wordmark.svg`](../../src/agentfactory_cloud/static/brand-wordmark.svg) | `/static/brand-wordmark.svg` |
| Application identity styles | [`src/agentfactory_cloud/static/brand.css`](../../src/agentfactory_cloud/static/brand.css) | `/static/brand.css` |

The mark has a `64 × 64` viewBox. The wordmark has a `360 × 80` viewBox and includes “Lokiravia” with “BY LOKVETIA.” The assets use native SVG geometry and local text, with no external font or image requests.

The [creator/operator prototype](../../prototypes/creator-operator/index.html) also works when its own directory is the web server root. It embeds the same mark as inline SVG and as a data-URL favicon; the required identity CSS is copied into its existing [style.css](../../prototypes/creator-operator/style.css). When canonical mark geometry or shared typography changes, update these embedded copies together. Keep the preview's sample-data notice visible.

## Color

| Role | Color | Use |
| --- | --- | --- |
| Violet ink | `#332746` | Main text |
| Violet | `#62418E` | Primary actions and links |
| Deep violet | `#513880` | Mark background and hover states |
| Amber spark | `#F2C675` | Spark inside the mark |
| Cream | `#F8F2E8` | L inside the mark |
| Warm paper | `#FAF7F1` | Application background |
| Light surface | `#FFFDF9` | Content cards and dialogs |
| Muted ink | `#6A6173` | Supporting copy |
| Border | `#E0D8E6` | Dividers and card outlines |
| Soft violet | `#F0EAF7` | Neutral pills and secondary accents |
| Focus | `#996115` | Keyboard focus outline |

Use violet ink and the darker violet for text on warm paper. Amber is a graphic accent, not body text on a light background. Status messages keep their existing meaning and use explicit words; brand decoration must not suggest that a game is ready or a decision has been approved.

## Typography and composition

Interface text uses `Segoe UI Variable Text`, then `Segoe UI`, then the system sans-serif. Main display headings use `Iowan Old Style`, `Palatino Linotype`, then Georgia/serif for a more editorial, imaginative tone. All fonts are local fallbacks. The standalone wordmark uses `Segoe UI` with an Arial/sans-serif fallback.

Keep the mark square and scale proportionally. Allow clear space of at least one quarter of the mark's width around a standalone mark. Use it at 24 CSS pixels or larger in normal content; the favicon may be smaller. Application headers currently use 38–42 pixels.

The standalone wordmark is intended for light backgrounds. Use it near its 360-pixel native width when the endorsement must remain readable. In narrow headers, use the mark beside live “Lokiravia” text and “by Lokvetia,” as the application does. On a dark presentation, put the complete wordmark on a light panel. Do not stretch, rotate, recolor, or add effects to the mark.

## Accessibility and implementation

A mark beside visible product text is decorative: use an empty image `alt`, or `aria-hidden="true"` for inline SVG. A standalone image needs an accessible name of “Lokiravia by Lokvetia.” Preserve visible focus outlines and reduced-motion support.

The application stylesheet is loaded after the existing page stylesheet and scoped with `brand-cloud`. Prototype-specific styles use `brand-prototype`. Presentation must preserve existing DOM IDs, hidden access controls, confirmation steps, and form attributes. Brand changes do not change the local workspace's privacy or execution behavior.

The product domain is `lokiravia.com`; the family domain is `lokvetia.com`. Domain links identify the brands and do not promise deployed services. These assets define the project's visual identity and make no claim of trademark registration. Compatibility and rollout details are in [the migration guide](migration.md).
