<a id="місто-яке-винне-тобі-послугу"></a>
# The Town That Owes You a Favour


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [living-world-design.md](living-world-design.md). Source SHA-256 (UTF-8/LF): `ebc8081b5d201c444525cc20e99a6c89dac1867e57cc43abcfa7004aaf0a3c89`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](living-world-design.md).

An original scenario for Lokiravia. Revision: 2026-09-10, following the Q06 paper walkthrough. Status: product specification for discussion and paper prototyping; implementation and actual trial results do not yet exist. The target expanded experience is **30 minutes for one player working with NPC collaborators**. Human cooperative play belongs to a later stage and needs separate network-state and authority checks; it does not silently expand the first Godot MVP.

**W0-build boundary:** the first build may reduce the district to one bench, two NPCs—Ilka and Yaryna—rain, an umbrella, and a clamp. In this minimal version, the umbrella belongs to the player: a loan from an innkeeper is not added without the innkeeper herself and her contract. It is sufficient to demonstrate the physical relationship between cover and a dry place, one conditional NPC response, an outcome without a cascade, and local-state persistence. Six places, the municipal office, the thirty-minute composition, and **the full E01–E08 below are a later expanded scenario**, not hidden scope in the first build.

**Research refinement:** the [second pass through corpus B](literary-b-pass-2.en.md) showed that fictional surprise can depend on hidden obligations, protagonist privilege, and inconsistent reward descriptions. This scenario has its own verifiable rules for accepting agreements, rewards, and authority to change the world; they are set out below and are not considered proven by the literary analogy itself.

**Q06:** [ten paper scenarios](causal-scenarios.en.md) specify initial moisture, timing, NPC windows, refusal, alternative help, assembly progress, and a failed local plan. The [comparison protocol](counterfactual-evaluation.en.md) separates an authored trace from actual evidence of Core self-improvement.

<a id="обіцянка-досвіду"></a>
## The experience promise

You arrive in an unfamiliar town, lend an umbrella to a bench—and under certain conditions help a new public place come into being. The town may remember what you did, offer a favour in return, and later begin debating whether a place itself can promise anyone anything. In another run, the umbrella will simply keep two planks dry. Both outcomes are honest.

The aim is to create the feeling: “I saw a possibility nobody named for me; now something here is different.” We do not promise that every whim will rewrite the universe. We promise that real differences will arise from actions, other residents, and world state, and that their causes will not be invented retrospectively.

The literary basis is a set of principles from the [corpus B analysis](literary-b-analysis.en.md): external consequences of optimization, TR-S01; collective new capability, TR-S08; boundary interactions, TR-S12; and the distinction between a visible achievement and a real result, TR-S14. The town, characters, objects, jokes, and specific event below are new original proposals, without transferring the books' fictional details.

<a id="район-і-люди"></a>
## The district and its people

The district's working name is Good Intentions Lane. It has six places within a short walk: an inn, a municipal workshop, a tram stop with a bench, a favours office, a reading courtyard, and an abandoned kiosk. Residents already have activities that do not require the player to appear.

Ilka repairs municipal furniture. She needs a dry workspace, a clamp, and time before another job; she will not abandon her work merely because the player asks eloquently. Yaryna runs evening readings. She is looking for an accessible corner where paper stays dry, but has no authority to occupy someone else's premises. Registrar Panko checks accepted obligations against the town's capacity. He can recognize a service provided but does not create unlimited gifts.

The sign on his office door reads: “Gratitude accepted without an appointment. Complaints about gratitude: Thursdays.” The joke comes from an institution taking its unusual business seriously. Panko does not speak in nonstop witticisms: when a soaked Yaryna is trying to save her notes, he offers practical help.

The town is not one omniscient NPC. It “remembers” through people, records, and changed places. A municipal favour is a specific voluntary agreement, such as one day's use of the workshop. It is not a currency, investment, or infinite kindness counter. An unsolicited act does not automatically make another resident a debtor.

<a id="тридцять-хвилин-розгорнутого-сценарію"></a>
## Thirty minutes of the expanded scenario

| Time | What the player experiences | What the prototype must demonstrate |
|---|---|---|
| 0–4 min | Receives a room at the inn, a map of a few doors, and a borrowed umbrella. The innkeeper asks for its return before departure, with no daily timer. | A calm place to return to and an object with properties; the game does not demand work for the right to begin. |
| 4–9 min | Meets Ilka and Yaryna and sees their difficulties with rain and a reading place. Can take an ordinary errand: bring a clamp from the workshop. | NPC intent is visible in behavior; the errand is one entry into the world, not a mandatory route. |
| 9–16 min | Explores the umbrella's coverage, the bench, the kiosk, and tram movements. Can shelter the bench, give the umbrella to a person, or stay beneath it themselves. | Freedom within verifiable properties; the same action produces the same physical effect. |
| 16–24 min | If conditions align, NPCs linger by the dry bench and agree on a temporary reading place. The player decides whether to remain involved. | Continuation depends on others' plans, resources, and consent; it is not imposed through rewards. |
| 24–30 min | Sees a local result, asks about its causes, agrees on another meeting, or returns home. | State persists; there is a truthful trace and a suitable place for the next visit. |

Creating a new ontology or reaching the “best ending” is not required within half an hour. Success in this expanded slice means one real change recognizable upon return, or a clear experience of why an idea did not develop further.

<a id="незвична-дія-та-її-точні-передумови"></a>
## The unusual action and its exact prerequisites

In control profile Q06-S0, the bench starts dry, installation takes t0–2, and rain begins at t3. The player can secure the umbrella above the bench with a wooden clamp. If the bench is already wet, the cover only prevents further wetting; W0 has no automatic drying, and E03 cannot silently turn wet=true into dry. Different timing needs its corresponding scenario profile. The clamp is returned after dismantling. The umbrella acquires one level of wear, which Ilka can later repair; installation costs the player two minutes. While the umbrella stands there, the player walks in the rain: wet clothes change sounds and everyday reactions, but do not take away movement rights, health, or the ability to finish the episode.

The authored model specifies in advance: coverage area, two available seating positions, precipitation level, wetting rate, bench occupancy, time of the next tram, NPC schedules, their needs, available materials, and current permissions. These numbers are prototype parameters for calibration, not a simulation of real meteorology. A language model cannot add a third dry seat, a stock of fabric, or Yaryna's consent in a sentence.

If coverage is sufficient and installed before wetting, the seats remain usable. Shared opportunity requires actual NPC availability intervals to overlap for the proposed action's duration, rather than two independent “in the neighborhood” booleans. Ilka waits for the tram only when she has at least six spare minutes; Yaryna chooses a dry place only when her own route takes her nearby. Their meeting makes conversation possible. A reading-corner proposal arises when Yaryna has the need, Ilka agrees to help, and permission for temporary use is available. Randomness may select a conversation topic from allowed options but cannot bypass those prerequisites.

<a id="наскрізний-слід-одного-можливого-результату"></a>
## An end-to-end trace of one possible result

The table describes one authored verification scenario. It is not a mandatory chain hardcoded into an “umbrella for the bench” quest.

| Event | Confirmed inputs | State change and visible trace |
|---|---|---|
| E01. Rain approaches | Profile record: initial bench dry, rain at t3; clouds/cues available to the player | Bench still dry; Yaryna keeps notes in a protected bag. A forecast does not create rain retroactively. |
| E02. Umbrella installed | Player has umbrella and clamp; place available; geometry valid | Object attached to support, wear +1; coverage appears over two seats. |
| E03. Rain starts; seats stay dry | Weather event t3; E02 completed beforehand; initially dry, sufficient coverage | Dry observation with actual cover; adjacent exposed stone becomes wet. This prevents a transition, rather than wet→dry or a reward for “genius.” |
| E04. Two people linger | E03; Ilka can still reach her job; Yaryna passes nearby; seats available | Both independently choose the bench for different reasons; dialogue does not imply they came for the player's quest. |
| E05. A shared proposal appears | E04; reading need; repair skill; voluntary consent | Yaryna asks to keep the cover until the evening reading; Ilka offers her own time. The player can refuse. |
| E06. Temporary corner opens | Player agrees; owner permits loan extension; place permission; reserved sign/box from Ilka's inventory and her accepted work slot | After the installation job completes, materials move from the workshop and specific resources are consumed/attached. Structure is temporary; no object is created through text. |
| E06a. Reading takes place | E06; participants present; accepted reading interval; actual start/end, permitted evidence of execution | ReadingCompleted records only the portion actually performed. A sign alone does not prove a reading occurred. |
| E07. Town accepts the service | E06a with independently checkable state/observer receipt; Yaryna's testimony labeled by provenance; Panko has authority and one available workshop day | A specific favour is offered to the player, who can accept or decline. Ilka's and Yaryna's contributions are also recorded. |
| E08. Player returns | Persisted E02–E07; time between sessions; storage agreement | Innkeeper keeps umbrella dry, Yaryna has left the next reading time; a short local account agrees with the log. |

Decisions can branch after E05. In E06, the umbrella is not “given away” without its owner's consent; if the loan is not extended, residents seek another canopy or postpone the reading. Panko does not reward generated text about a reading—he verifies that it actually occurred. This directly applies TR-S14.

<a id="дві-альтернативи-та-відсутність-каскаду"></a>
## Two alternatives and the absence of a cascade

**Direct path:** the player brings the clamp and helps Ilka repair the kiosk door. This is more reliable, takes less time, and opens a dry room. It may become a reading place through another agreement. The unusual must not be the only route to an interesting story.

**Personal path:** the player lends Yaryna the umbrella. She saves her notes, continues her own route, and may introduce the player to the reading group later. The bench gets wet and the collective meeting does not happen; a relationship changes without creating a new place.

**No umbrella contribution or no shared continuation:** in dry weather, the bench is usable without cover; NPCs can meet independently of it. The Q06-C03 pair does not credit the umbrella with a necessary contribution to the same social outcome. If NPC windows do not overlap, or someone does not accept the proposal, the particular shared reading does not occur; physical benefit and other permissible events remain. An NPC may sincerely thank the player for the care, but is not obliged to. The player retrieves the object and carries on. The system does not insert a secret rare visitor solely to justify the player's time spent.

Refusal is also a complete choice: “Today I just want to take a walk.” Lodging remains available and the town attends to its own affairs. Independent conditions sustain unpredictability, rather than a guaranteed reward for unusual behavior.

<a id="малий-підготовлений-план-який-не-спрацював-у-w0"></a>
## A small prepared plan that fails in W0

Q06-C09 uses the same bench and two NPCs. The player inspects the place, installs cover during t0–2, prepares a spoken invitation, but plans to gather both at t8. Yaryna leaves at t7 under a preexisting schedule; she did not promise to wait until t8. The cover works, but the particular simultaneous-reading plan is not fulfilled. A visible clock and a reply about timing make the reason understandable.

This is failure of a particular chosen policy, not a demand to break every idea. If the player changes the time to t5 early enough and obtains consent, another plan can work. If late, they retain honest local benefit, a new invitation, or the right to leave; no failure jackpot is added.

<a id="довгий-добрий-план-який-не-спрацював"></a>
## A long, well-intentioned plan that fails

This is a seasonal example after W0-build, not an additional requirement for the first bench. Over two game weeks, the player and Yaryna prepare a regular evening reading group. They observe tram passengers, choose a time, print six posters, arrange two evenings of canopy use, and spend their own time on the program. Their hypothesis is that passengers waiting for a connection will become regular listeners. Nobody guarantees an audience.

Meanwhile, town craftspeople complete a footbridge. The repair order, resources, and completed stages existed in the season's initial state; a neighborhood notice was posted before preparations for the readings. This is other residents' independent project, not an event an administrator adds after judging the player's plan. Once the bridge opens, NPCs for whom walking becomes shorter change their routes under their normal rules. On the chosen evening, transfers no longer bring together the expected audience.

None of the expected visitors comes to the reading. Yaryna and the player may read together, move the notices, or abandon the idea. Posters have been used, the prepared material remains, but the goal of establishing a regular group is **not achieved**. No hidden rare reward turns the evening into a secret victory. Even careful preparation may have overlooked someone else's successful plan.

The log shows the old bridge order, its completion, changes to specific routes, and the absence of listeners. If the bridge is unfinished in the control run, NPCs cannot use it; that does not guarantee reading attendance, because other needs remain. Already accepted promises—for example, payment to Ilka for a canopy actually built—are fulfilled regardless of the broader plan's failure. Failure may yield a new research question, but the world is not obliged to compensate it with a special story.

<a id="як-виникає-й-завершується-зобовязання"></a>
## How an obligation begins and ends

The lifecycle separates **opportunity → proposal → accepted agreement → execution → fulfilled / terminated under its terms / unfulfilled**. Discovering a narrative opportunity is not accepting a task. A proposal specifies parties, subject, known cost, deadline or its determination method, fulfillment criterion, and how participation can end. If an unknown future effect is material, its category and boundary are visible, rather than a fabricated exact probability.

The player can accept a clear agreement through ordinary dialogue or an appropriate action; every movement does not need a separate modal. Inspection, a polite “thank you,” a journal hypothesis, or closing a session, however, does not consent to expenditure or debt. A material change of terms returns as a new proposal instead of being applied to old consent.

In E05, Yaryna merely proposes leaving the cover in place. In the full scenario, E06 additionally needs the umbrella owner's permission; it is not inferred from the player holding the object. If someone refuses, the reading finds another route or does not happen. An NPC may leave on schedule, closing the opportunity, but the player's absence does not thereby become a new punishment. A temporary role does not become permanent through a hidden timer.

<a id="стабільний-контракт-винагороди"></a>
## A stable reward contract

A reward for verified service, a distinction for an unusual method, and a resident's warm reaction are different outcomes. E05 or E06 alone does not guarantee a municipal reward: if no such promise exists, the interface does not display one. E07 is Panko's voluntary offer in response to a verified reading; the player may accept or decline. If a favour was promised earlier, its terms are fixed on acceptance, before the result is evaluated.

The record retains rule version, criterion, fulfillment evidence, applied modifiers, exact outcome, and unfulfilled parts of the agreement. A new evaluator does not retroactively add an audience-size requirement or turn an issued workshop day into a different service. A personalized offer differs from fulfillment of a promise; it is not disguised as a random reward and does not alter character progression without the player's acceptance.

Control runs check identical decisions for identical evidence under the same version and relevant prerequisites. The narrator may remember a funny way of installing the umbrella, but an attractive description does not replace a dry bench, a reading actually held, or the owner's consent. A technical error receives a separate visible correction; Core evolution does not justify rewriting honestly earned history.

<a id="ux-гравця"></a>
## Player UX

Object inspection shows everyday properties: “covers a small area,” “can be secured,” “needs drying.” The bench offers “Try something,” alongside direct object manipulation. Players can describe intent in words; the system presents a short plan of actual actions and their cost before resources are spent. Unknown outcomes are labeled honestly, without percentages invented from nothing.

NPCs do not display lists of hidden numerical motives overhead. Ilka checks the clock, Yaryna protects her notes: the world gives cues through behavior. Important boundaries are available in ordinary language: “I won't reach my customer in time,” “We can't leave her property here without her permission.”

The journal has three separate entry types: “Observed,” “I think,” and “Agreed.” Asking “Why do people read here now?” shows the confirmed short chain E02 → E04 → E05 → E06 and residents' contributions. It does not reveal every future scenario. On return, the player sees zero to three confirmed relevant changes and only actual unfinished agreements, if any. After a quiet walk, it is valid to say there are no significant changes; the interface does not invent a debt to fill a card.

Humor arises from consequences. Panko may issue a document “On the Umbrella's Temporary Appointment as a Roof.” After its removal, the document becomes a memory, not grounds for claiming the roof still exists. Jokes do not target the player's refusal, mistake, or vulnerability.

<a id="повтор-який-можна-завершити"></a>
### Repetition that can end

After the umbrella is removed, Panko may joke once that the roof resigned voluntarily. This is a new context grounded in actual state. If the player asks to dispense with ceremony, Panko plainly explains the loan's status and available next actions; another NPC does not repeat the same teasing in different words. An old scheduled line checks the current setting before display. This is a proposed variant for author/human review, not a mandatory joke in W0.

The player can stop organizing readings: a completed meeting remains history, borrowed items are returned under the accepted agreement, and nobody automatically promised another meeting. Residents may propose continuing on their own or do something else. Changing activities does not erase earlier contributions. The [Q01 contract](experience-improvement.en.md) defines separate checks for repetition, exit/restore, costs to other roles, and missing human feedback.

<a id="ux-автора-світу-та-обмежена-агентність-npc"></a>
## World-author UX and bounded NPC agency

The author composes an episode from places, objects, needs, permissions, budgets, and permitted actions. They can inspect a causal map, remove E02 and compare outcomes, accelerate weather, change a schedule, and check for no continuation. A separate mode shows which facts a particular resident knows; the author does not confuse simulator knowledge with information available to an NPC.

Each NPC has personal intentions, accessible objects, movement areas, authority to promise, a spending limit, and a condition for ending attempts. It chooses its next action from permitted options and can revise its plan after a new event. It does not rewrite authoritative facts, others' consent, ownership rules, or town budgets. A rejected intention leads to another attempt or an understandable refusal; an infinite inner monologue does not count as life.

The author's screen contains execution evidence, invariant violations, and explanatory uncertainty. The player's screen contains the town. Neither treats new text or an agent self-report as proof that an event occurred.

<a id="епохи-світ-може-змінювати-самі-категорії"></a>
## Epochs: the world can change its categories

In the first epoch, the bench is an object, a reading corner is a permitted kind of public place, and specific people are the parties to agreements. “The bench helped the town” is a metaphor. It grants the bench no automatic legal or agent authority.

After many independent communities develop, a new question may arise: can a place supported by different people retain obligations beyond each person's tenure? A later epoch may introduce **a shared place with stewardship** as a new category. It has representatives, an obligation limit, a defined community benefit, and residents' right to change its stewardship. These are new transfer and planning capabilities, not a renamed bench.

Such a transition is a separate product and architecture decision: a candidate defines semantics, migration of old records, authority checks, completion of existing loans, and a way for a particular world to decline. It undergoes isolated simulation and independent evaluation. An active episode remains on its accepted version. The player's first contribution stays in history but grants no monopoly over the new class of institutions.

In expanded E06, the initial scenario inventory must explicitly define one sign, one box, and Ilka's available time before the proposal; if anything is absent, the corner does not open. E06a verifies that a reading occurred independently of an NPC-written report. These details belong to the expanded district, not W0-build.

Renaming the corner or changing its caretaker does not automatically make it a new place or transfer all duties. For a supported transition, the author defines what remains the same, who accepts the next work, and where resources come from. A good earlier story can remain a memory after a practice ends. A resident may not recognize a modified object; that lack of knowledge does not change its owner. [Q02](identity-continuity.en.md) describes these distinctions without requiring a new transformation system in W0.

<a id="память-світу-й-технічне-відновлення"></a>
## World memory and technical recovery

An honest E06 remains history even if the next agent version behaves worse. Agent rollback changes future behavior without deleting the corner or agreement. If a fault wrongly creates ten umbrellas, the system restores correct state using the verified log, records a technical correction, and compensates dependent losses. It does not claim that an invented storm stole the umbrellas.

Q06-C08 defines assembly as an accepted job: before completion, cover=false/wear=0, objects reserved, progress saved. Resume continues remaining work; cancel releases reservations without refunding time spent; completion atomically creates effect/resource/job/dedup records. The world tick does not advance during a W0 pause. A pending model request is not a saved assembly job; the Q05 final-commit guard checks an old reply after load.

Deferred events retain parent causes, rule version, and already accepted obligations. New-epoch transitions have verified migrations. The profile must have a verified recovery method or explicitly enter paused/degraded state when no compatible permitted fallback exists; narrative irreversibility does not prohibit correcting technical errors.

<a id="межі-шкоди-й-наступні-перевірки"></a>
## Harm boundaries and the next checks

In the first slice, a single player cannot destroy the only lodging, close every exit, or make an essential NPC permanently unavailable. An obstacle can move a reading, alter trust, or change a route; the district has alternative ways to function. Repeatedly damaging and repairing one's own canopy does not generate new municipal favours. Third-party praise or fabricated text does not substitute for evidence of completed work.

Future human cooperative play adds rights to shared objects, simultaneous-action conflicts, duplication protection, partner exit, and confirmation of shared costs. Until those checks exist, single-player evidence is not presented as a ready MMO mechanic.

The first study consists of 12 facilitated single-player sessions with rainy, dry, and conflicting-schedule conditions. This is a proposed format, not a test already conducted. Acceptance conditions: every confirmed consequence has real prerequisites; control runs do not create cascades without the conditions; at least 8 of 12 participants can explain one real relationship; everyone can leave and return to a usable state. Surprise, laughter, and the desire to live in the district are collected through separate open questions; these measures are not collapsed into one automatic score.

An initial subject for Core self-improvement could be how to help NPCs find a permitted joint action without violating schedules or rights. Baseline and new planners are compared across different episodes, operating costs, errors, and people's experiences. The candidate does not edit its own exam. Improvement of Core itself is a separate verified result; changes to the town's history do not substitute for it.
