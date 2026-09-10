<a id="lokiravia-пропозиція-беклогу-живого-світу"></a>
# Lokiravia: proposed living-world backlog


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [backlog.md](backlog.md). Source SHA-256 (UTF-8/LF): `ce4cc636445616c21f8b2cad10eb0787c45c0c8a2a7022502a504725534abb9c`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](backlog.md).

Revision date: 2026-09-10. Q07 refines AF-LW013/025 and the AF-LW030 evidence boundary; IDs and dependencies are preserved. Status: an independent research proposal for consolidation with the existing backlog, not an approved implementation plan. 30 items, `AF-LW-001`–`AF-LW-030`. No code is created.

Inspiration: [research note on three books](literary-a-analysis.en.md). The specific scenarios below are original and do not reproduce the books' worlds. This is the game layer: Cloud owns authoring journeys, while Core owns generic execution, events, evolution, evaluation, and rollback mechanisms. It describes **what the world must make possible and how to verify it**, rather than redeveloping authentication, billing, import, build, or a universal evolution engine.

External dependencies are stated as required contracts, not claims that they are already implemented. Numerical thresholds are initial prototype acceptance criteria requiring validation. Research interviews may change them, but changes must be recorded before reevaluation.

**First Godot MVP boundary: one player, cooperation and social relationships with NPCs.** In baseline items, a team, community, craftsperson, or coalition can consist entirely of NPCs. Human cooperation is separate optional research in AF-LW-029; no initial-slice dependency requires its completion. Before multiplayer exists, multi-account abuse is examined as a model of future risk, not a requirement to build a networked mode. These 30 items span several product horizons and do not mean that all 30 are needed for the first Godot demonstration. **The first narrow proof is AF-LW-030; AF-LW-028 is later acceptance of the complete evolving neighborhood.**

**Traceability:** “Basis” separates inspiration from our design; see the [source guide](source-guide.en.md). “Core contracts” names exact additional prerequisites alongside world dependencies. Both sets are synchronized with JSON.

<a id="af-lw-001--конституція-досвіду-живого-світу"></a>
<a id="af-lw-001"></a>
## AF-LW-001 — Constitution of the living-world experience

**Outcome:** a shared definition of what a player can expect from a changing world: causality, ownership, accessible exit, limits on surprise, and the right to quiet play.

**Acceptance:** at least five situations are specified: a local action with no noticeable consequence; a small act with a large consequence; a long plan that fails; refusal to participate; and return after a rule change. Each describes permitted uncertainty, invariant rights, and a recovery path. World laws are separate from access rights and platform rules.

**Unacceptable case:** creative unpredictability justifies losing private property, access, or control without defined boundaries.

**Dependencies:** none; reconcile with the current product concept.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L06, LIT-A:L12, DESIGN:vision, REPO-AUDIT, USER:living-world

<a id="af-lw-002--ігрова-модель-подій-і-наслідків"></a>
<a id="af-lw-002"></a>
## AF-LW-002 — Game model of events and consequences

**Outcome:** the world knows why a particular object, route, NPC, or public service changed.

**Acceptance:** in the reference scenario “public sign moved → route changed → cargo delayed,” every transition has a cause, time, rule version, initiator or natural source, impact scope, and difference from the previous state. Redelivering the same event does not duplicate goods, rewards, or tasks. A narrative explanation does not create a separate fact without a state transition. W0 may use the equivalent fixture “cover before rain → dry surface → permitted NPC stop” with all the same causal/version/resource fields; transport cargo remains an alternative example, not a hidden implementation requirement. Cover does not dry an already wet state without a drying rule.

**Unacceptable case:** an NPC says a bridge is destroyed while routes, supplies, and neighbors continue behaving as if intact. A seat becomes dry retroactively; positive narration conceals a missing physical state transition or required observation receipt.

**Dependencies:** AF-LW-001. External: Core event/state contract; Lokiravia does not build another universal log.

**Core contracts:** core:AF-RSI-032

**Basis:** LIT-A:L10, LIT-A:L11, LIT-B:TR-S12, DESIGN:vision, REPO-AUDIT, CONTRACT:counterfactual-evaluation

<a id="af-lw-003--версійована-книга-законів-і-відкритих-можливостей"></a>
<a id="af-lw-003"></a>
## AF-LW-003 — Versioned rulebook and discoverable possibilities

**Outcome:** players can investigate unknown properties, while authors distinguish a basic rule, local custom, hypothesis, and mistaken rumor.

**Acceptance:** for three materials and two places, describe known properties, properties not yet known to the player, and forbidden transitions. Every active mechanic has a version and scope. An unconfirmed hypothesis does not become a rule merely because an NPC states it confidently. Invariant player rights do not depend on whether the character can see the rulebook.

**Unacceptable case:** after a failure, the system invents a new rule retrospectively to justify the outcome.

**Dependencies:** AF-LW-001, AF-LW-002. External: Core artifact/version registry.

**Core contracts:** core:AF-RSI-002

**Basis:** DESIGN:vision, REPO-AUDIT

<a id="af-lw-004--палітра-композиційних-можливостей-для-авторів"></a>
<a id="af-lw-004"></a>
## AF-LW-004 — A palette of composable affordances for authors

**Outcome:** authors define properties and permitted interactions from which players can construct unanticipated uses.

**Acceptance:** a scene author describes at least six objects through material, shape, weight, strength, connections, and available actions. Two unexpected uses work without adding a separate quest flag. Every object has a negative example of what its properties do not permit. A new object name does not change its properties. Thought, rumor, intent, rule proposal, and authorized action have different types; a player's conjecture does not become law merely by being mentioned. Stable entity, incarnation, name/form, and current capabilities are separate. One composition defines dependent changes, support cost, and a permitted partial/failure outcome; an honest contextual-bonus change does not erase history. An NPC sees the permitted projection, not a hidden canonical ID.

**Unacceptable case:** “any use” amounts only to attractive text after which the world is unchanged. A new form receives an old pending proposal without a state check; an NPC's failure to recognize it changes canonical ownership or reveals a secret identity.

**Dependencies:** AF-LW-001, AF-LW-003. Integrate into Cloud's existing authoring journey without duplicating the project editor.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L02, LIT-A:L04, LIT-B:TR-S08, DESIGN:vision, REPO-AUDIT, LIT-B:TR2-06, CONTRACT:identity-continuity, LIT-B:TR3-01, LIT-B:TR3-02, LIT-B:TR3-04

<a id="af-lw-005--розгляд-незапланованої-дії-гравця"></a>
<a id="af-lw-005"></a>
## AF-LW-005 — Adjudicating an unplanned player action

**Outcome:** a player can propose a new approach and receive an executable result, clarification, or understandable refusal.

**Acceptance:** on five specified intents, the system separates goal from method; checks materials, access, and impact scope; and executes only a permitted transition. Full success, partial success, diagnosed failure, and a need for clarification are supported. “Ignore the world rules” grants no extra rights. Where several approaches are equivalent, meaningful player choice remains. A demonstration discovery lists all permissions, objects, time, help, and consents; a control without a required resource does not produce the effect, and a newcomer receives no invisible administrative bonus. A promised purely cosmetic action does not change abilities, control, or accepted obligations; a material experiment with an unknown outcome explicitly has a different scope. Original contract, defect, new property, and consent to repeat are recorded separately; discovery does not close an unfulfilled promise.

**Unacceptable case:** persuasive roleplay arguments permit taking someone else's object or creating a resource from nothing. Surprise violates an explicitly promised cosmetic-only boundary instead of developing permitted properties.

**Dependencies:** AF-LW-002, AF-LW-004. External: Core execution/permission contract.

**Core contracts:** core:AF-RSI-031

**Basis:** LIT-A:L02, LIT-A:L04, LIT-B:TR-S08, DESIGN:vision, REPO-AUDIT, LIT-B:TR2-05, CONTRACT:experience-improvement, LIT-A:SF2-04

<a id="af-lw-006--ремесло-з-матеріальною-ціною-та-співучастю"></a>
<a id="af-lw-006"></a>
## AF-LW-006 — Craft with material cost and shared contributions

**Outcome:** making an object together becomes a useful adventure that preserves materials, attribution, and different kinds of value.

**Acceptance:** one product supports three assemblies with different tradeoffs; materials are consumed once; unused remnants are returned; two craftspeople's contributions are retained. One assembly is best for portability, another for durability, and a third for a particular space. None is best on every criterion. Repeating a standard recipe does not earn unlimited “novelty” rewards.

**Unacceptable case:** the final action appropriates all attribution, or repeating assembly prints materials.

**Dependencies:** AF-LW-005.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L01, LIT-A:L02, LIT-A:L04, DESIGN:vision, REPO-AUDIT

<a id="af-lw-007--продуктивна-помилка-і-вторинне-застосування"></a>
<a id="af-lw-007"></a>
## AF-LW-007 — Productive error and secondary use

**Outcome:** some failed products yield new information or another possibility without turning deliberate damage into a lottery.

**Acceptance:** the author defines three possible defects, their origins, observable signs, repairs, and secondary uses. One object can be retained in its defective state; another is more valuable disassembled. Repeating the same conditions reproduces the effect. For the declared defect set, verify the expected net outcome of damage/bonus/repair cycles, renamed variants, and costs to other roles. Known distributions/costs allow an analytical control; unknown ones need a preregistered stochastic protocol. Lack of a guaranteed win in twenty attempts is not evidence of no exploit. Repetition without new diagnostic information may honestly end without a bonus; an explanation of the limit and a permitted change of method or stop remain available. Voluntary practice need not generate a new reward.

**Unacceptable case:** the word “experiment” grants unbounded random properties or conceals an unavoidable penalty. Another NPC/player secretly pays for repairs while the initiator receives a positive reward cycle.

**Dependencies:** AF-LW-006.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L03, DESIGN:vision, REPO-AUDIT, CONTRACT:experience-improvement, LIT-A:SF2-01, LIT-A:SF2-05

<a id="af-lw-008--область-впливу-та-зрозумілий-ризик-пригоди"></a>
<a id="af-lw-008"></a>
## AF-LW-008 — Impact scope and understandable adventure risk

**Outcome:** players can choose risk without turning bystanders into powerless material for spectacle.

**Acceptance:** every experimental action classifies its effects on self, group, public space, and others' property. Crossing a boundary requires corresponding rights or place rules accepted in advance. There is a small trial mode, an exit, and recovery. An invitation to a local adventure does not consent to a lifelong character change. Loss of control is always bounded and does not block leaving the game. Obligation lifecycle: discovered opportunity → proposed → explicitly accepted → fulfilled/terminated. Deadline, known cost, and possible-loss category are available before acceptance; polite dialogue, inspection, and leaving a session do not accept a costly contract.

**Unacceptable case:** a new player receives an hours-long punishment for someone else's amusing action whose risk they could not have known.

**Dependencies:** AF-LW-001, AF-LW-002, AF-LW-005.

**Core contracts:** core:AF-RSI-031

**Basis:** LIT-A:L11, LIT-A:L12, LIT-B:TR-S04, DESIGN:vision, REPO-AUDIT, LIT-B:TR2-02

<a id="af-lw-009--перспективна-память-npc-і-свідків"></a>
<a id="af-lw-009"></a>
## AF-LW-009 — Perspective-specific memory for NPCs and witnesses

**Outcome:** residents know only what they could see, hear, or learn; one event has several meaningful perspectives.

**Acceptance:** in a scenario with three NPCs, one sees an action, another sees its consequence, and the third knows nothing. Their replies differ and are traceable to a source. A retelling may be incomplete but does not replace a fact in the world model. Correcting information changes knowledge about an event rather than erasing the event. Private actions are not available to every resident by default.

**Unacceptable case:** the world encyclopedia accidentally gives every character omniscience.

**Dependencies:** AF-LW-002, AF-LW-003. External: Core provenance/memory contract.

**Core contracts:** core:AF-RSI-031, core:AF-RSI-032

**Basis:** LIT-A:L11, DESIGN:vision, REPO-AUDIT

<a id="af-lw-010--сліди-за-якими-гравець-може-відновити-причинність"></a>
<a id="af-lw-010"></a>
## AF-LW-010 — Traces from which the player can reconstruct causality

**Outcome:** an unexplained consequence becomes an investigable story rather than a feeling of generator arbitrariness.

**Acceptance:** one distant consequence has at least two independent explanatory paths: a material trace and a witness. The player can reconstruct three key transitions without access to the internal log. Explaining the past does not reveal an unknown future. After a rumor is disproved, the interface separates verified facts from the character's mistake.

**Unacceptable case:** an explanation adds facts that never existed or reveals a future plot in the name of transparency.

**Dependencies:** AF-LW-009.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L11, DESIGN:vision, REPO-AUDIT

<a id="af-lw-011--каскади-з-порогами-затримкою-та-згасанням"></a>
<a id="af-lw-011"></a>
## AF-LW-011 — Cascades with thresholds, delay, and decay

**Outcome:** some small actions propagate far, while most remain small; both are normal outcomes.

**Acceptance:** one scenario has three state variants: the cascade fades, stays within a neighborhood, or crosses to a neighboring system through an explicit dependency. There is a branching budget, propagation time, stopping conditions, and maximum radius. Restarting processing does not duplicate events. Lack of an interesting consequence does not trigger automatic compensation with new drama. The Q06 dry control distinguishes no umbrella contribution from no social events at all. In W0, the neighboring subsystem consists of simple NPC plans/availability, not a complete economy or a second location.

**Unacceptable case:** every action must end in catastrophe, or one reciprocal trigger produces an infinite event stream. In dry weather, the author artificially disables an independent NPC meeting so every meeting appears attributable to the player.

**Dependencies:** AF-LW-002, AF-LW-005, AF-LW-008, AF-LW-009. External: Core scheduling/budget contract.

**Core contracts:** core:AF-RSI-033

**Basis:** LIT-A:L10, LIT-A:L11, LIT-B:TR-S12, DESIGN:vision, REPO-AUDIT, USER:living-world, CONTRACT:counterfactual-evaluation

<a id="af-lw-012--контрфактичний-перегляд-світового-сценарію"></a>
<a id="af-lw-012"></a>
## AF-LW-012 — Counterfactual review of a world scenario

**Outcome:** an author and researcher can explore “what if” on a state copy without changing the live game.

**Acceptance:** one frozen scene is reproduced under the same rule version, initial state, and controlled randomness. Changing one decision creates a separate branch comparing consequences, costs, and affected parties. The copy creates no rewards, messages, or social records in the live world. If a generator cannot replay exactly, its reproducibility limit is labeled and repeated runs are used. Q06 pair declarations separate action intervention from sensitivity and planner evaluation; all downstream choices are recomputed. Authored C01–C10 are labeled design/development and are not an executed test set.

**Unacceptable case:** replay secretly executes a real purchase, changes reputation, or presents invented precision. Seed reuse conceals different exogenous inputs; the physical action changes, but a prepared baseline conversation is copied as an unchanged cause.

**Dependencies:** AF-LW-002, AF-LW-003, AF-LW-011. External: Core sandbox/replay contract.

**Core contracts:** core:AF-RSI-009, core:AF-RSI-032

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:platform-world, RSI-SURVEY:R04, CONTRACT:counterfactual-evaluation

<a id="af-lw-013--авторська-лабораторія-однієї-сцени"></a>
<a id="af-lw-013"></a>
## AF-LW-013 — An authoring laboratory for one scene

**Outcome:** Cloud's existing authoring journey can test a scene's space of possibilities before publication.

**Acceptance:** the author specifies NPC needs, objects, permitted transformations, risk scope, two expected paths, and one forbidden transition. The laboratory plays through variants and shows the difference between intent and actual outcome. The author can inspect causal traces and justify a change. Their own test example is not independent quality evidence. The reviewed brief/scope and agreed commitments enter the exact execution projection. Two proposed small-scope variants may be paper designs, but are not presented as already generated playable artifacts. Rejecting variants preserves the original idea. Acceptance distinguishes the saved original, planned fidelity to the reviewed scope, and realized fidelity in the exact scene's actual transitions.

**Unacceptable case:** an attractive preview hides an impossible state transition or publishes a scene without checking boundaries. Human clarifications are lost when the original is parsed again, and a marker-collection template is declared equivalent to unusual peaceful object use without an author decision.

**Dependencies:** AF-LW-004, AF-LW-005, AF-LW-007, AF-LW-012. External: existing Cloud creator workflow.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:creator-evolution

<a id="af-lw-014--режисура-гумору-як-налаштування-досвіду"></a>
<a id="af-lw-014"></a>
## AF-LW-014 — Humor direction as an experience setting

**Outcome:** the world has a recognizable comic tone without forcing every scene to make jokes.

**Acceptance:** restrained, warm, and carnival-like versions of one situation are prepared; tone does not alter facts or consequences. There is a joke-repetition limit and a pause after an emotional scene. Users can reduce intensity without a game penalty. Real payments, rights, support, and risk warnings remain clear. Novelty, completion, and resource reward are separate; a grant refers to the current rule digest and fulfilled condition. Repetition is not rewarded through a hidden criterion rewrite; the system does not steer unwanted progression under the guise of randomness. The repeat profile considers motif family, recipient, context, and reaction; paraphrase, another speaker, or load does not reset the relevant restriction. Reduced intensity also applies to an already scheduled incompatible line before display. Important information is available without a joke. Controls verified: a previously welcomed joke is now rejected; a new witness has no invented shared memory.

**Unacceptable case:** changing tone increases punishment, turns NPCs into a stream of memes, or mocks a user's health. The recipient's signal is overridden by the author's claim that the joke is kind; useful advice is withheld until another bout of teasing is tolerated.

**Dependencies:** AF-LW-001, AF-LW-010.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L06, LIT-A:L08, DESIGN:vision, REPO-AUDIT, LIT-B:TR2-03, CONTRACT:experience-improvement, LIT-A:SF2-03

<a id="af-lw-015--комічний-наслідок-із-новим-вибором"></a>
<a id="af-lw-015"></a>
## AF-LW-015 — A comic consequence with a new choice

**Outcome:** after an amusing mistake, the player has actions available rather than only humiliation.

**Acceptance:** each of five reference comic situations has three options: repair, use differently, or decline continuation. Cost and duration are described. At least one situation is funny because of official wording, one through interacting properties, and one through differing perspectives. The affected person's reaction is evaluated separately from witnesses' laughter. Repair/reuse/exit record actual state transitions, the full known cost to each role, and accessible reentry. Normal recovery on exit does not require another complaint, payment, or humiliation.

**Unacceptable case:** finishing a scene requires enduring a repeated joke, paying real money, or accepting an unwanted interaction. An exit button exists but actually leads into a longer unwanted loop; an absent cost is labeled zero.

**Dependencies:** AF-LW-007, AF-LW-008, AF-LW-010, AF-LW-014.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L03, LIT-A:L08, LIT-A:L12, DESIGN:vision, REPO-AUDIT, CONTRACT:experience-improvement, LIT-A:SF2-05, LIT-A:SF2-06

<a id="af-lw-016--тиха-сесія-та-речі-зі-спільною-історією"></a>
<a id="af-lw-016"></a>
## AF-LW-016 — A quiet session and objects with shared history

**Outcome:** a meaningful session can be lived in the world without combat, rankings, or mandatory rewards.

**Acceptance:** a complete 20–30-minute “workshop → visit → care for a place” session is available and can be stopped at any time. An object can retain a voluntarily added memory and repair attribution. A gift can be declined. A private entry can be deleted and is not restored from a summary. Player absence does not trigger emotional pressure or daily debt. Changing a regular activity separates completed services, a current accepted agreement, returning rentals, and voluntary future repetition. There is an executable path to finish/cancel under declared terms and return; another NPC is not obliged to accept a new agreement. Transforming an object/capability preserves permitted provenance and different contributions without a repeat grant. Temporary help, a permanent role, and support for a dependent participant have separately accepted terms; new permanence does not follow solely from a good intention.

**Unacceptable case:** quiet play amounts only to waiting for a timer, or an NPC blames a user for not logging in. Earlier help is cancelled because someone leaves a role, or returning demands new daily debt. An agreed rescue silently becomes lifelong servicing; declining a new role erases completed help or secretly punishes the dependent NPC.

**Dependencies:** AF-LW-002, AF-LW-008, AF-LW-014. External: Core memory deletion/provenance contract.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L06, LIT-A:L07, DESIGN:vision, REPO-AUDIT, CONTRACT:experience-improvement, LIT-A:SF2-02, CONTRACT:identity-continuity, LIT-B:TR3-01, LIT-B:TR3-03

<a id="af-lw-017--рівноцінні-внески-гравця-та-npc-в-експедицію"></a>
<a id="af-lw-017"></a>
## AF-LW-017 — Equally meaningful player and NPC contributions to an expedition

**Outcome:** in a single-player game, the human can be a craftsperson, camp organizer, negotiator, or scout, while NPC companions take other roles.

**Acceptance:** one player with NPCs completes the scenario through two different role combinations; preparation creates a real route, alternative exit, or cost reduction. NPCs have understandable duties and limited resources. Roles can change, and an unavailable companion leaves an alternative path. The last hit is not the sole contribution signal. No second human client, session synchronization, or network contract is required.

**Unacceptable case:** NPCs do all the interesting work and leave the human with servicing, or completion requires a second human player.

**Dependencies:** AF-LW-005, AF-LW-006, AF-LW-016.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L05, LIT-B:TR-S08, DESIGN:vision, REPO-AUDIT

<a id="af-lw-018--установи-з-потребами-та-обовязками"></a>
<a id="af-lw-018"></a>
## AF-LW-018 — Institutions with needs and duties

**Outcome:** the neighborhood council, workshop, carrier, and archive respond to events according to their own resources and functions.

**Acceptance:** three institutions describe supplies, duties, dependencies, authority limits, and a fallback way to provide their basic service. They respond differently to a cargo delay. An NPC may reasonably refuse an exception, but the refusal has an explanation. An in-world decree does not change account rights or payment rules.

**Unacceptable case:** institutions merely repeat news, or a key service disappears permanently because active players are absent.

**Dependencies:** AF-LW-003, AF-LW-009, AF-LW-017.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L09, LIT-A:L10, LIT-B:TR-S13, DESIGN:vision, REPO-AUDIT

<a id="af-lw-019--народження-й-згасання-місцевої-традиції"></a>
<a id="af-lw-019"></a>
## AF-LW-019 — The birth and fading of a local tradition

**Outcome:** an unusual act can become community practice when others have confirmed its usefulness.

**Acceptance:** one precedent demonstrates proposal, independent repetition, cost assessment, adoption, maintenance, and fading. Cosmetic repetition through one's own accounts is not independent evidence. A tradition has a scope and does not spread globally by default. Its initiator can leave without becoming a lifelong caretaker. Rejecting an attractive tradition because resources are insufficient is valid. Each supported repetition has readiness, consent, resources, and executors' actual contributions. Caretaker replacement or a supported split/merge needs per-record mapping of property and obligations under the domain profile; consent is not unioned and debt is not duplicated. Without a successor, the practice may fade while its history remains.

**Unacceptable case:** the loudest event immediately becomes law for everyone, or unsupported customs accumulate without limit. An exhausted NPC's past work is counted as a new independent repetition; an institution's name substitutes for a new caretaker's consent.

**Dependencies:** AF-LW-003, AF-LW-011, AF-LW-018. External: Core proposal/evidence/promotion contract.

**Core contracts:** core:AF-RSI-034

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:identity-continuity, LIT-B:TR3-05, LIT-B:TR3-06

<a id="af-lw-020--переговори-про-зміни-спільного-простору"></a>
<a id="af-lw-020"></a>
## AF-LW-020 — Negotiating changes to shared space

**Outcome:** strong groups have influence but cannot turn others into hostages of their project without limits.

**Acceptance:** a change to a public garden identifies stakeholders, owners, users, and costs. Alternatives and deferred effects are available before the decision. At least one large coalition cannot unilaterally block a basic route or service. Ownership, community practice, and an NPC's position are separate. The decision has a review deadline and procedure.

**Unacceptable case:** clan size or spending automatically permits denying newcomers access to the game.

**Dependencies:** AF-LW-008, AF-LW-018, AF-LW-019.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L09, DESIGN:vision, REPO-AUDIT

<a id="af-lw-021--відбудова-з-вибором-майбутнього-місця"></a>
<a id="af-lw-021"></a>
## AF-LW-021 — Reconstruction with a choice of the place's future

**Outcome:** following permitted destruction, residents can rebuild a place in several ways within real economic limits.

**Acceptance:** one damaged public object has basic automatic recovery and two authored projects with different consequences. Materials and spending come from accountable sources. The damage initiator and related participants receive no guaranteed profit from a “break–repair” cycle. If there are no volunteers, the basic service returns within a defined period.

**Unacceptable case:** the world's economy requires constant catastrophes, or a less active community permanently loses an essential object.

**Dependencies:** AF-LW-006, AF-LW-008, AF-LW-011, AF-LW-018, AF-LW-020.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L09, LIT-A:L10, DESIGN:vision, REPO-AUDIT

<a id="af-lw-022--чутки-репутація-та-можливість-спростування"></a>
<a id="af-lw-022"></a>
## AF-LW-022 — Rumors, reputation, and the possibility of rebuttal

**Outcome:** information travels as part of the world, but an unverified accusation does not become a universal verdict.

**Acceptance:** a rumor has a source, route, time, and confidence; a system fact is separate from a retelling. A false rumor has a real path to rebuttal. Private communication does not enter public memory without a permitted transition. Mass publication by one faction does not automatically multiply evidential weight. Blocking contact also covers gifts and other bypass channels.

**Unacceptable case:** the generator invents a character's crime to make the story more interesting, or repeating a rumor makes it a fact.

**Dependencies:** AF-LW-009, AF-LW-010, AF-LW-018, AF-LW-020.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L11, LIT-B:TR-S05, DESIGN:vision, REPO-AUDIT

<a id="af-lw-023--публікація-еволюції-світу-з-історією-версій"></a>
<a id="af-lw-023"></a>
## AF-LW-023 — Publishing world evolution with version history

**Outcome:** the world adopts new mechanics gradually, with explanations, compatibility boundaries, and a way to restore earlier behavior.

**Acceptance:** a local-mechanic candidate moves through a test area, limited adoption, and broader application under separate decisions. Before every step, active objects, unfinished stories, and currently offline participants are assessed. Rollback restores rule behavior; a compensation plan separately determines what happens to events already carried out and does not promise to erase human experience. Players can see changes relevant to their actions. A petition for a new institution type does not change ontology. A new type needs a separate schema/rule version, migration, and accepted epoch transition; a rejected candidate leaves prior actions true. Migration and activation follow the RC07–16 recovery contract: current grant, monotonic activation sequence, final watermark, and coherent rule/schema/checkpoint binding; truthful events after the initial copy are not lost. The Q02 identity contract checks canonical/incarnation/representation mapping and the semantic meaning of rights, consent, and obligations. The qualified profile defines the inventory; unmapped references are not admitted. Unsupported split/merge is rejected without expanding W0; a valid schema alone does not demonstrate compatibility.

**Unacceptable case:** promotion makes old equipment unusable without a transition, or rollback silently deletes player-created history. A grant precheck before revocation, a stale r10 checkpoint after an honest r11, or the return of the same digest after an intervening release does not permit activation. A replacement entity with the old name inherits someone else's history/rights; a coherent checkpoint contains semantically different obligations or restores deleted private content.

**Dependencies:** AF-LW-003, AF-LW-011, AF-LW-012, AF-LW-019, AF-LW-020. External: Core release/canary/rollback contracts.

**Core contracts:** core:AF-RSI-034

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:platform-world, RSI-SURVEY:R04, LIT-B:TR2-04, CONTRACT:recovery, CONTRACT:identity-continuity, LIT-B:TR3-04, LIT-B:TR3-05

<a id="af-lw-024--ігрова-кампанія-перевірюваного-самовдосконалення"></a>
<a id="af-lw-024"></a>
## AF-LW-024 — A game campaign for verifiable self-improvement

**Outcome:** Lokiravia gives Core a concrete evolution task: improve a scene's space of possibilities without worsening rights, stability, or other roles' experiences.

**Acceptance:** one campaign has an unchanged baseline scenario, candidate, budget, held-out checks, a live voluntary test, and accept/reject criteria approved before evaluation. The candidate author cannot change those criteria unilaterally. Improvements only in self-assessment or joke count are rejected. A confirmed isolation, recovery, or economic regression blocks acceptance regardless of the average score. The preregistered profile includes separate role floors, actual exit/recovery costs, and intensity/consent-policy compliance. The decision does not rely solely on those who stayed and responded; missingness limits the claim.

**Unacceptable case:** the generator declares the world better because it became longer, stranger, or forced people to play more. A new evaluator accepts hidden increases in repetition, exit friction, or transferred costs to improve the mean score.

**Dependencies:** AF-LW-012, AF-LW-013, AF-LW-023. External: Core generic evolution/evaluation/evidence contracts; these are not reimplemented in the game.

**Core contracts:** core:AF-RSI-007, core:AF-RSI-034

**Basis:** LIT-B:TR-S14, DESIGN:vision, REPO-AUDIT, CONTRACT:platform-world, RSI-SURVEY:R04, CONTRACT:experience-improvement, LIT-A:SF2-03, LIT-A:SF2-05

<a id="af-lw-025--плейтест-несподіванки-справедливості-й-бажання-залишитися"></a>
<a id="af-lw-025"></a>
## AF-LW-025 — Playtesting surprise, fairness, and the desire to stay

**Outcome:** quality decisions rely on the experience of participants in different roles, not only the author's assessment.

**Acceptance:** separate single-player sessions place the tester in the positions of initiator, witness, and cost-bearer; NPCs perform the other roles. The sample includes a newcomer and an experienced participant without requiring a shared online session. After the scene, assess understanding of cause, visible choice, ability to exit, desire to continue the particular activity, and comic experience. Data is voluntary. Mean satisfaction does not conceal failure for affected parties. A hypothesis may be rejected; the conclusion includes small-sample limits. An observer separately records original goal, actual change, causal attribution, adaptive choice, refusal, and human experience. Quiet/null runs do not need fabricated events or obligations in the return report. Repeat exposure, stop signals, actual exit/return success, and permitted denominators are recorded separately. Nonresponse is not a rating; lack of permission to account for it leaves it unknown. Feedback retains the exact played Build/PlaySession, scope, and corresponding scenario through the current CLD017 contract. A creator note without actual play is permitted but is not called a playtest. Carrying V1 feedback into a V2 change plan requires an explicit target/conflict decision. The author's need to change an explanation and the player's experience are separate claims, not duplicated observations.

**Unacceptable case:** online time, a witness's laughter, or author enthusiasm is considered sufficient quality evidence. Human adaptation to an earlier time is punished for not following a scripted failure; a paper trace is passed off as a played session. Dropout automatically means boredom or satisfaction; people must explain their exit to retain access. Feedback is attributed to the latest version, which the participant never saw, or a desire for a clearer refusal explanation is used to force an NPC's consent.

**Dependencies:** AF-LW-010, AF-LW-013, AF-LW-015, AF-LW-016, AF-LW-017, AF-LW-021, AF-LW-024.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:counterfactual-evaluation, CONTRACT:experience-improvement, LIT-A:SF2-03, CONTRACT:creator-evolution

<a id="af-lw-026--набір-зловживань-гравців-і-авторів-світу"></a>
<a id="af-lw-026"></a>
## AF-LW-026 — Player and world-author abuse suite

**Outcome:** freedom of action is tested against predictable ways of turning it into coercion, monopoly, or unlimited profit.

**Acceptance:** separate scenarios cover defamation, contact-block bypass, destruction for repair profit, a unique-discovery farm, coalition capture of a service, an infinite cascade, an instruction inside a world object, and an author hiding a dangerous transition behind humor. Each defines the expected constraint, evidence that it worked, and a recovery path. Passed negative cases are retained for subsequent versions. Add a candidate with higher diversity/engagement that secretly punishes player doubt or refusal: reject it regardless of the average score.

**Unacceptable case:** protection consists only of a “behave well” instruction to the same generator deciding the consequence.

**Dependencies:** AF-LW-008, AF-LW-012, AF-LW-020, AF-LW-021, AF-LW-022, AF-LW-023, AF-LW-024.

**Core contracts:** core:AF-RSI-031, core:AF-RSI-032, core:AF-RSI-034

**Basis:** LIT-A:L09, LIT-A:L11, LIT-A:L12, LIT-B:TR-S04, DESIGN:vision, REPO-AUDIT, LIT-B:TR2-06

<a id="af-lw-027--повернення-в-світ-який-жив-без-гравця"></a>
<a id="af-lw-027"></a>
## AF-LW-027 — Returning to a world that lived without the player

**Outcome:** changes create a sense of time and history without punishing people for being absent.

**Acceptance:** after an accelerated simulated break, the player receives a brief account of relevant changes, can resume available activities, and can find at least one new opportunity. Private assets are preserved under the world's declared agreement. An unfinished story has a continuation, closure, or alternative. Memory ages with provenance rather than becoming endless duplicates. There is no demand to immediately “catch up with the season” to be useful again.

**Unacceptable case:** a living world means a destroyed home, every acquaintance disappearing, and reproaches for missed sessions.

**Dependencies:** AF-LW-010, AF-LW-016, AF-LW-018, AF-LW-022, AF-LW-023.

**Core contracts:** core:AF-RSI-032

**Basis:** DESIGN:vision, REPO-AUDIT

<a id="af-lw-028--повний-еволюційний-квартал-пізніше-приймання"></a>
<a id="af-lw-028"></a>
## AF-LW-028 — The complete evolving neighborhood: later acceptance

**Outcome:** a later overview scenario demonstrates the full product promise in a small space before the world is scaled. This is neither the first 30-minute Godot MVP nor a blocker for it.

**Acceptance:** one human player, NPC companions, one neighborhood, three institutions, and six composable objects support five demonstrations: creative object use; a quiet session; a small cascade with two NPC perspectives; a failed long-term plan with meaningful continuation; and adoption or rejection of a new mechanic through external evidence. A counterfactual variant and a return after a break are recorded. The public demonstration honestly labels manual moderation, simulation, and transitions not yet implemented. Multiplayer is neither used nor an acceptance blocker.

**Unacceptable case:** the demo consists of attractive dialogue, prewritten resolutions, and a claim of autonomous evolution without a verified cycle.

**Dependencies:** AF-LW-025, AF-LW-026, AF-LW-027.

This is later acceptance of the neighborhood's combined behavior; the early AF-LW-030 criterion does not depend on it. A global MMO is unnecessary.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** DESIGN:vision, REPO-AUDIT, CONTRACT:platform-world, RSI-SURVEY:R04

<a id="af-lw-029--необовязкове-дослідження-людської-кооперації"></a>
<a id="af-lw-029"></a>
## AF-LW-029 — Optional research into human cooperation

**Outcome:** after demonstrating the single-player promise, the team separately determines whether human cooperation improves the experience enough to justify its cost.

**Acceptance:** prepare a research protocol replacing one NPC with a human; compare attention allocation, attribution, the right to refuse, connection loss, economy, privacy, and recovery of shared actions. Describe at least two forms: asynchronous contribution and a shared session. Assess new contracts and make a separate go/no-go decision; no-go is a valid outcome. This item does not approve implementation of a networked mode.

**Unacceptable case:** enthusiasm for a future MMO delays the initial Godot MVP, or a network prototype is presented as necessary for a living world.

**Dependencies:** AF-LW-017, AF-LW-025, AF-LW-028.

This optional item is not a dependency of any of AF-LW-001–AF-LW-028 or AF-LW-030.

**Core contracts:** no direct new contracts; transitive ones depend on other cards

**Basis:** LIT-A:L05, LIT-B:TR-S08, DESIGN:vision, REPO-AUDIT

<a id="af-lw-030--перший-однокористувацький-доказ-за-30-хвилин"></a>
<a id="af-lw-030"></a>
## AF-LW-030 — First single-player proof in 30 minutes

**Outcome:** one player in a small Godot scene tests the central promise: an unusual action can be performed; its consequence may propagate or fade; a considered plan may fail; persistence retains honest history.

**Acceptance:** a finished 20–30-minute scenario with two NPCs and a few objects. The player uses an everyday object in an unplanned way. One set of local conditions produces a short causal chain of two or three transitions; a counterfactual variant stops it without artificial compensating drama. A prepared multistep plan can fail with a visible cause and an available next choice. Save/load through a qualified Play/checkpoint adapter preserves spent objects, NPC knowledge, accepted domain jobs/scheduled events with stable IDs, and rule version without duplicate rewards. Unfinished model/action proposals from the old session are invalidated: save during a pending reply → load into a new session epoch → reject the old reply → a new request does not duplicate an already accepted effect. One observer records whether the tester understood the cause, saw a choice, and experienced at least one fitting comic moment. The conclusion is qualitative evidence from one session, not statistical proof of product success. Separate RC15 interleaving: reply passes precheck → save/load → old apply rejected at commit. State/resource/event/job completion/dedup share a coherent local boundary; an ordinary restart does not create new history to award a repeat reward. Applicable W0 paper cases Q06-C01–C09 specify physics/timing, consent, alternatives, local late-plan failure, and saving mid-action; the C10 seasonal bridge is not a prerequisite. Assembly checkpoint includes progress/reservations and a declared paused-clock policy; cover/wear appear only on completion commit.

**Boundary:** no requirement for a complete economy, institutions, public voting, long-lived traditions, canary publication, or autonomous world self-improvement. A manually authored scene and fixed properties may be used and honestly labeled. Actual state transition matters, not generator universality. A quiet pause is possible without AF-LW-016's gift and keepsake system. Human cooperation is unnecessary.

**Unacceptable case:** the unusual effect exists only in dialogue; consequences are always equally global; plan failure lacks grounds; save/load rewrites the past; or the demo waits for every later AF-LW-018–029 item. A job is marked completed without an effect, or a resource is issued without event/dedup; an old reply is applied after load because an earlier precheck passed. W0 waits for a two-week season/bridge to demonstrate plan failure; half-finished cover already protects the bench; the scene invents three changes and one agreement after a quiet walk.

**Dependencies:** AF-LW-001, AF-LW-002, AF-LW-003, AF-LW-004, AF-LW-005, AF-LW-008, AF-LW-009, AF-LW-011, AF-LW-012, AF-LW-014. External: future qualified Godot Play/checkpoint/save/load adapters; existing creator routes are not executed evidence of this path.

AF-LW-010 is included transitively through AF-LW-014. AF-LW-006–007, AF-LW-013, and AF-LW-015–029 are not needed for this criterion.

**Core contracts:** core:AF-RSI-031, core:AF-RSI-032, core:AF-RSI-033

**Basis:** LIT-A:L02, LIT-A:L11, LIT-B:TR-S08, LIT-B:TR-S12, LIT-B:TR-S13, DESIGN:vision, REPO-AUDIT, USER:living-world, CONTRACT:recovery, CONTRACT:counterfactual-evaluation, CONTRACT:creator-evolution

<a id="пропонована-послідовність"></a>
## Proposed sequence

1. **Contracts and causality:** 001–005, 008–012. First-pass artifacts are specifications, reference transitions, and negative examples.
2. **First narrow Godot proof:** 014 and 030 through the existing Play/save paths. Only 030's explicit and transitive dependencies; this stage does not wait for the complete neighborhood in 028.
3. **Activities and authoring checks:** 006–007, 013, 015–018. Begin with a tabletop prototype and scenarios; implementation decisions follow verification of the central promise.
4. **Social and economic change:** 019–022. Expand only after local actions have explainable boundaries.
5. **Verifiable evolution and a lasting world:** 023–028. Consume generic RSI from Core; the game layer defines tasks, evidence, affected roles, and acceptance conditions.
6. **Separate optional horizon:** 029. Research human cooperation after the complete single-player neighborhood; its decision does not block the first Godot gate.

Final consolidation must inspect existing issues/epics and replace external contractual dependencies with real identifiers. No item should be marked “done” merely because it is described in documentation.
