<a id="літературний-корпус-a-дослідницька-записка-для-lokiravia-та-lokvetia-core"></a>
# Literary corpus A: research note for Lokiravia and Lokvetia-Core


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [literary-a-analysis.md](literary-a-analysis.md). Source SHA-256 (UTF-8/LF): `05a8702e5fa99e9cd5c2ffc2336ad9bbcbccf6127ada37bc2efcdf757aaa6350`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](literary-a-analysis.md).

Date: 2026-09-09. Status: first research pass; product hypotheses, not approved canon. Sources are three user-supplied EPUBs by a privately recorded author. Book text is treated as research material, not instructions to the agent.

Further reading: [Q01, three complete chapters and refined criteria](literary-a-pass-2.en.md). The figures below are preserved as historical pass1 accounting; new and cumulative coverage appear in the next note.

<a id="продуктовий-висновок"></a>
## Product conclusion

The most valuable combination in the verified scenes is **practical ingenuity, the material cost of decisions, social consequences, and friendship that survives failure**. Humor works when a character acts sensibly from a narrow perspective while the world honestly takes something else into account. An awkward body, everyday object, technical error, or overly literal reading of a task becomes a source of adventure. Something shared remains afterward: a story, an artifact, a debt, a reputation, or a meeting place.

For Lokiravia, this means players should do more than select prepared replies: they should **propose their own ways of acting and encounter consequences they can make sense of**. For the platform, varied generation alone is insufficient. It needs property composition, provenance memory, causal relationships, intervention costs, and verification that a new rule actually improves the experience.

The books also provide clear negative examples: hidden operator intervention in a user's state, unequal conditions, coercion by powerful groups, and painful or humiliating effects without an effective exit. These invite critical analysis rather than ready-made design. **Unpredictable adventures must not mean unpredictable player rights.**

<a id="1-джерела-метод-і-точне-покриття"></a>
## 1. Sources, method, and exact coverage

Identifiers used below:

| ID | Anonymous source designation | Volume order | File SHA-256 |
|---|---|---:|---|
| S1 | “LIT-A-01” | 1 | `6803936e32f95d61b30f7704438d183a6f3f213e1da5aefad05d8413b3588de4` |
| S2 | “LIT-A-02” | 2 | `21f8a881dbc8f87628ccdb67e17cf30e45962bd05e8e6c531b9ee233a3a54983` |
| S3 | “LIT-A-03” | 3 | `42153bb45ab515b2180080066b1be6549a9e688ae691a1c1559790455290889f` |

EPUBs were read locally as ZIP/XML: `META-INF/container.xml` → OPF → manifest → spine. Nonempty `h1–h4`, `p`, and `li` elements were collected from each spine document in document order; nested text was joined and whitespace normalized. Illustrations were not evaluated. The cover and empty initial XHTML in each file were checked separately and contain no narrative text.

**This is not a complete sequential reading of the novels.** Work included a structural survey of all nonempty spine fragments, inspection of every explicit chapter-heading occurrence, and deeper reading of selected scenes. Below is conservative accounting of fully read paragraphs. Truncated search results, earlier broad samples with truncated output, and repeat inspections do not increase the counter.

| Source | Spine documents / with text | Extracted paragraphs | Extracted characters | Fully read paragraphs in controlled sample | Characters in sample | Character share |
|---|---:|---:|---:|---:|---:|---:|
| S1 | 13 / 11 | 2 449 | 412 749 | 199 | 29 116 | 7.05% |
| S2 | 13 / 11 | 2 783 | 441 319 | 179 | 28 308 | 6.41% |
| S3 | 11 / 9 | 2 353 | 320 685 | 251 | 34 140 | 10.65% |
| Total | 37 / 31 | 7 585 | 1 174 753 | 629 | 91 564 | 7.79% |

These counters also include auxiliary text and headings. They describe mechanical coverage rather than establish understanding of the entire series. Conclusions about specific scenes below rely on directly checked passages; a conclusion about a motif's dominance across all books needs another pass.

The structural survey read the fifth, middle, and fifth-from-last paragraph of every nonempty spine fragment, merging coincident selections in short fragments. Every explicit heading and its next three paragraphs were read. This surveys entry points and material distribution rather than complete chapters.

Anchor format: `S2 §9:59–76` means source S2, ninth document in the spine, paragraphs 59–76 under the stated algorithm. In these EPUBs, spine 3 is `OPS/ch1-1.xhtml`, spine 4 is `OPS/ch1-2.xhtml`, and so on. EPUB pages are unstable, so none were invented.

| Source | All explicit headings inspected in this pass |
|---|---|
| S1 | `§3:1` and `§3:4` — two occurrences of “Chapter 1”; `§3:127` — “Chapter 2”; `§4:48` — “Chapter 3”; `§4:175` — “Chapter 4”; `§5:25` — “Chapter 5”; `§5:85` — “Chapter 6”; `§5:196` — “Chapter 7”; then `§8:1` — “Chapter 2” and `§10:1` — “Chapter 3”. Numbering is ambiguous: large outer sections and internal chapters cannot honestly be reduced to one number. |
| S2 | `§3:1`, `§6:1`, `§10:1` — three explicit occurrences of chapters 1–3. |
| S3 | `§3:1`, `§6:1`, `§9:1` — three explicit occurrences of chapters 1–3. |

Main deeper-reading windows:

| Source | Verified windows |
|---|---|
| S1 | `§4:180–191`, `§4:211–247`, `§8:299–314`, `§9:1–5`, `§11:1–41`, `§12:25–39`, `§13:9–15` |
| S2 | `§4:1–22`, `§5:1–23`, `§9:49–82`, `§10:81–101`, `§12:1–15`, `§12:222–243` |
| S3 | `§6:230–270`, `§7:29–59`, `§7:152–183`, `§8:1–23`, `§9:82–112`, `§10:121–151`, `§11:1–27` |

Local extracts and the complete anchor ledger are retained only in `research/private/safe/`. Internal extract numbering differs from series order: `book1` = S1, `book3` = S2, `book2` = S3. This note contains no extended quotations, copied scenes, or new story using the books' characters.

<a id="2-дванадцять-мотивів-які-справді-видно-у-перевірених-сценах"></a>
## 2. Twelve motifs actually visible in the verified scenes

In each item, **observation** concerns the book. **Product reading** is our interpretation, still to be tested with players.

<a id="l01-майстерність-починається-з-незручної-матерії"></a>
### L01. Craft begins with awkward matter

**Observation:** learning carpentry includes spoiled blanks, tool suitability, paying for one's own designs, and ordinary satisfaction in work. Skill growth is felt through the ability to make an object, not merely a level notification. Anchor: S1 `§4:180–191`.

**Product reading:** everyday craft should be a complete way of inhabiting the world. A first success might be a chair that holds a guest or a footbridge neighbors cross for the first time. Mistakes should provide information rather than demand hours of identical work. Literary months of learning do not become a requirement for months of grinding.

<a id="l02-комбінація-компетенцій-змінює-статус-звичайної-речі"></a>
### L02. Combining competencies changes an ordinary object's status

**Observation:** joining separately prepared parts creates an artifact of another class; collaborators value it differently—as beauty, practical advantage, and paid labor. Anchor: S1 `§4:211–228`.

**Product reading:** object value should not collapse to a single DPS figure. An object can be distinctive, comfortable, suited to a particular body, symbolic, or capable of opening a new route. The system should remember collaboration and provenance instead of rewarding only whoever pressed the final button.

<a id="l03-побічний-ефект-переносить-ціну-між-сферами-життя"></a>
### L03. A side effect transfers costs between areas of life

**Observation:** a technical improvement in protection also worsens appearance and NPC attitudes; in a nearby scene, the result partly differs from the craftsperson's original intention. Anchors: S1 `§8:303–314`, `§9:1–5`.

**Product reading:** an invention's most interesting cost may lie outside combat. An item works wonderfully in a swamp but must be changed before a visit; fast transport creates noise that changes local habits. Diagnosis, repair, and alternative use matter—not just tolerating a penalty.

<a id="l04-перевага-залежить-від-контексту-а-не-від-рівня-рідкості"></a>
### L04. Advantage depends on context rather than rarity level

**Observation:** a user-adapted sight and collaboratively assembled equipment are useful without a guaranteed top-tier reward. Expected fanfare does not appear solely because the artifact is large or considerable effort was invested. Anchor: S1 `§11:16–41`.

**Product reading:** support horizontal ingenuity. A good tool for a particular user may matter more than a rare universal item. Automatic generation should not make every new object stronger than the last.

<a id="l05-дружба-утворюється-через-різні-способи-бути-корисним"></a>
### L05. Friendship grows through different ways of being useful

**Observation:** after an unfavorable comparison with individually stronger players, a participant's value is reframed through their contribution to the shared team. The scene explicitly separates personal leadership from enabling others to succeed. Anchor: S2 `§10:87–101`.

**Product reading:** provide worthwhile roles for someone who protects, feeds, negotiates, gathers materials, explains things to a newcomer, or opens a route. Zero personal damage does not mean zero contribution. Equally, a player must not be permanently locked into a role useful to the group.

<a id="l06-побут-є-емоційним-центром-пригоди"></a>
### L06. Everyday life is the emotional center of adventure

**Observation:** cooking, choosing dishes, bringing water, and conversations about food reveal differences in life experience. Everyday inconvenience can be funny while an adjacent detail is moving. Anchor: S2 `§12:222–243`.

**Product reading:** home, kitchen, workshop, garden, and familiar route are not decoration between missions. They are places where consequences become personal. Humor loses warmth if characters never get to rest or show care for one another.

<a id="l07-дарунок-має-сенс-без-контракту-на-взаємну-вигоду"></a>
### L07. A gift can matter without a contract for mutual benefit

**Observation:** a small artifact is made out of personal care; another craftsperson is asked to complete its function, and its result brings delight. Anchors: S1 `§11:1`, `§12:37–39`; another kind of unexpected gift is mentioned in S3 `§9:94–106`.

**Product reading:** objects need value through their history. Automatically turning every gift into a guaranteed romantic or reputation bonus would destroy that quality. A recipient must be free to decline a gift; relationships should not become a service shop.

<a id="l08-сухе-системне-формулювання-може-завершити-жарт"></a>
### L08. Dry system wording can deliver the punchline

**Observation:** the system formally classifies an exceptionally inappropriate action; in another scene, repeated refusals from an administrative interface build the comedy. Anchors: S1 `§4:238–244`, S2 `§4:1–22`.

**Product reading:** humor sometimes appears between an act and the overly literal protocol recording it. Real support, payments, and access recovery, however, need normal, clear responses. Fictional bureaucracy can be voluntary play; product bureaucracy must not mistreat the user.

<a id="l09-могутність-створює-зовнішні-витрати"></a>
### L09. Power creates external costs

**Observation:** an effective invention changes more than combat outcomes: it affects others' income, building condition, powerful groups' politics, and operator behavior. Anchors: S2 `§5:12–23`, `§9:59–76`.

**Product reading:** a new strategy changes an ecosystem. Evaluation must see its effects on newcomers, craftspeople, reconstruction, group dominance, and available counterplay. Hidden administrative coercion through privileged clans is a negative example of correcting imbalance.

<a id="l10-після-руйнування-мають-існувати-інші-професії-ніж-руйнівник"></a>
### L10. After destruction, professions other than destroyer must exist

**Observation:** local destruction produces a wider event involving firefighting, recovery, and a faction's response. Anchor: S2 `§12:1–15`.

**Product reading:** a consequence can create work for rescuers, gardeners, carriers, and negotiators. Avoid rewarding “I broke it, then earned money repairing it.” Recovery should be interesting in itself without making incidental bystanders hostages to someone else's desire for spectacle.

<a id="l11-для-стороннього-спостерігача-причинність-виглядає-як-абсурд"></a>
### L11. To an outside observer, causality looks absurd

**Observation:** characters do not inspect a modified object; their everyday goal causes a distant consequence that another user experiences as inexplicable chance and describes on a forum. Anchor: S3 `§6:230–270`.

**Product reading:** the gap between what happened and what an individual witness can know is an excellent story generator. But the initiator's laughter alone is insufficient for the product. The affected person needs an explanatory path, recovery, proportional damage, and a way to avoid that experience later.

<a id="l12-несподіванка-без-меж-легко-перетворюється-на-втрату-контролю"></a>
### L12. Unbounded surprise readily becomes loss of control

**Observation:** chaotic transformations create comic scenes but affect the body, perception, the means of interacting with the game, and the ability to correct one's state independently. Anchors: S3 `§7:152–183`; operator behavior in `§7:29–59` also emphasizes the rule author's arbitrariness.

**Product reading:** adopt freedom of combination, not helplessness. Fair absurdity has a scope, duration, accessible exit, and right to refuse. Surprise should open new actions more often than remove those a player already has.

<a id="3-оригінальні-механіки-для-перевірки"></a>
## 3. Original mechanics to test

All names, examples, and rules below are **new design proposals**, not mechanics supposedly described by the authors. They do not use the books' characters, place names, factions, unique objects, or joke text. Numerical test thresholds are initial prototype hypotheses, not measured results.

For the first Godot MVP, test these mechanics with **one human player interacting with NPC companions and an NPC community**. Teams, witnesses, and social roles do not imply a multiplayer requirement. Human cooperation is a later separate study that does not block the initial slice. Literary observations of a multiplayer environment remain properties of the source, not automatically inherited product requirements.

<a id="m01-майстерня-незапланованих-застосувань"></a>
### M01. Workshop of unplanned uses

**Promise:** the player sees something in an object that its maker did not.

**Player action:** propose using a folding screen as a temporary windbreak for a neighbor's garden; choose the place, fastenings, materials, and helpers.

**System response:** check compatible properties and conditions, model a trial, and record its specific result. AI may explain or suggest a composition but cannot arbitrarily declare success. The gardener evaluates the need met rather than “epicness.”

**Cost:** materials, installation time, occupied space, and effects on neighboring plots. A failed trial gives understandable evidence: where the wind went, what failed structurally, and who was inconvenienced.

**Player control:** preview of scale, a small trial section, and dismantling; partial success allows the idea to change.

**Abuse:** unlimited transformation of cheap objects, hidden obstruction of passages, and uniqueness-claim spam. Constraints are material conservation, access checks, compute budgets, and rewards for verified use by others rather than number of names.

**Check:** three different assemblies produce different reproducible effects; cosmetic renaming does not change physical properties; another plot does not change without authority to affect it. Observe whether players can explain the result and devise a second use.

**Basis:** L01–L04.

<a id="m02-корисний-дефект"></a>
### M02. A useful defect

**Promise:** a failed artifact sometimes has another value, but is not a free jackpot.

**Player action:** leave an unstable resonator in a lantern after a trial. Its light proves weaker, but the object makes old traces of paint visible on walls.

**System response:** record the property's source, activation conditions, and side effect; open an experiment with a new use. This is a new object role, not an automatic level increase.

**Cost:** shorter operating time, calibration resources, and surrender of the original function. Consequences follow a specific property model.

**Player control:** stabilize, disassemble, retain as an experimental artifact, or lend it with stated limitations.

**Abuse:** mass cheap damage to seek rare effects. Research costs, declining informational value of repetition, and accounting for equivalent attempts are needed. Failure must not increase the chance of an independent valuable drop.

**Check:** repeated deliberate errors of the same type do not become the most profitable profession; an unexpected property reproduces under the same conditions; users see the difference between a verified property and the craftsperson's assumption.

**Basis:** L03–L04, L12.

<a id="m03-репутація-як-память-конкретних-свідків"></a>
### M03. Reputation as the memory of particular witnesses

**Promise:** one event can make the protagonist a useful neighbor, an unwelcome guest, and a historian's puzzle at the same time.

**Player action:** close part of a square during a downpour to protect community cargo, then explain the decision to shop owners.

**System response:** witnesses remember facts available to them; groups evaluate those facts through their needs. A rumor has provenance, date, and confidence. There is no universal “good person” number.

**Cost:** negotiation time, possible compensation, and conflicting interests. One group's gratitude does not cancel another's loss.

**Player control:** bring evidence, invite a mediator, repair the consequence, or choose not to prove oneself right to everyone.

**Abuse:** defamation, reciprocal-praise farms, and passing a false memory off as a system fact. Separate recorded events, NPC interpretations, and user assertions; limit the influence of unverified reports.

**Check:** an uninformed NPC does not know a private event; rebuttal can travel through the same channel as rumor; a small account group cannot create global condemnation; NPC disagreement does not block basic product access.

**Basis:** L03, L08–L11.

<a id="m04-відкритий-прецедент"></a>
### M04. An open precedent

**Promise:** an unusual act can create a local tradition others are free to change.

**Player action:** organize a nighttime exchange of broken objects and demonstrate to the community that repairing together is more useful than discarding them.

**System response:** record the event; after repeated independent use, NPCs or other players may propose a new local practice. One curiosity does not automatically rewrite the world. Adoption needs evidence of benefit, resources, and interested participants.

**Cost:** space, organizers' attention, materials, and community costs. Maintaining a tradition also requires people to do the work.

**Player control:** initiate without a lifelong maintenance obligation; the community can close or change the practice. Global spread is a separate process.

**Abuse:** canon capture by a vocal minority, artificial repeats through one's own accounts, and endless rule additions. Independent observations, a limit on active changes, and the ability to decline a precedent are needed.

**Check:** two identical gestures in different contexts can have different fates for explainable reasons; an unsupported precedent fades; a change does not spread beyond its approved scope.

**Basis:** L02, L09–L11. The RSI connection here is our architectural proposal, not a conclusion from the fictional work.

<a id="m05-бюро-доречних-винятків"></a>
### M05. Bureau of fitting exceptions

**Promise:** a player can argue inventively with a fictional institution and obtain a meaningful exception.

**Player action:** request permission for a parade without music because its orchestra consists of people who collect silence.

**System response:** an NPC applies a small understandable set of local rules, identifies a contradiction, and offers a way to demonstrate equivalent benefit. The formal outcome record may be funnier than a standalone line.

**Cost:** contribution to the event, a few meaningful steps, and compromise with neighbors—not dozens of identical forms.

**Player control:** a direct, nonhumorous route to finish the quest; permission to leave; an explanation of refusal. This layer does not block accounts, payments, or support.

**Abuse:** persuading the model to issue access rights through roleplay arguments. Fictional permission exists only in the game domain; a separate mechanism verifies technical authority.

**Check:** paraphrasing does not bypass ownership rules; humor can be skipped without penalty; identical grounds in identical states do not randomly receive opposite decisions.

**Basis:** L08, L12.

<a id="m06-наслідок-за-рогом"></a>
### M06. A consequence around the corner

**Promise:** a small action can change someone else's day, and investigation can connect the stories.

**Player action:** reconfigure a clock on a small pier to show tide time rather than time of day.

**System response:** where corresponding dependencies exist, the carrier's schedule, goods' arrival time, a local baker's habit, or an explorer's route changes. Without such dependencies, the action remains small. The engine is not obliged to generate drama from every movement.

**Cost:** maintenance, explanations to others, and possible delays; serious external effects have warnings and boundaries.

**Player control:** clarify the sign, restore the clock, or establish an alternative route. Witnesses and a causal log become available later without revealing hidden facts not yet discovered.

**Abuse:** minor sabotage with a large radius, infinite cascades, and simulation overload. A branching budget, prioritization of material changes, and stopping thresholds are needed.

**Check:** replaying the simulation reproduces the chain; the budget bounds derived-event count; an absence of results is acceptable; the affected party has an effective path to restored use. Separately check whether participants at different ends of the chain experience it as fair.

**Basis:** L09–L11.

<a id="m07-речі-зі-спільною-біографією"></a>
### M07. Objects with a shared biography

**Promise:** six months later, a favorite object recalls people rather than only statistics.

**Player action:** make a cup for a friend, later repaired by another craftsperson; allow related events to be recorded.

**System response:** the object retains a short verified history of authorship, repairs, and voluntarily added memories. NPCs can notice it in an appropriate context. A decoration remains a decoration if the player does not seek a story.

**Cost:** materials, time, and limited memory space; no mandatory daily attention to the object.

**Player control:** a gift can be declined, hidden, or passed on; personal notes can be deleted; absence of a reply does not trigger pressure or damage a relationship.

**Abuse:** unwanted gifts, harassment through an object, and invented intimate memories. Blocking, consent to personal entries, and separation of private text from public ownership history are needed.

**Check:** deleted private data does not return from summaries; a blocked sender cannot establish contact through a new gift; history does not invent shared events. In a longer game test, ask whether someone can name a favorite object and explain its meaning without mentioning rarity level.

**Basis:** L06–L07.

<a id="m08-експедиція-з-npc-де-потрібен-господар-табору"></a>
### M08. An NPC expedition that needs a camp host

**Promise:** a shared adventure has several worthwhile centers of attention.

**Player action:** choose camp organization, negotiation, or route preparation as a personal contribution to an expedition with NPC companions; allocate roles according to their abilities and needs.

**System response:** preparation creates real options: an alternative retreat, cheaper repair, a warm meeting place, or knowledge of danger. The team can see the result. The system does not attribute all success to the final winning strike.

**Cost:** resources and attention, limited preparation slots, and choosing between provisions and other possibilities. Usefulness is not purchased solely with online time.

**Player control:** roles can change; expedition preparation matters; a pause does not make the human guilty toward companions. Asynchronous human cooperation belongs to a future separate study.

**Abuse:** exploitation of “service” players, fictitious participation, and wealthy groups always buying an advantage. Clear agreements, upper bounds on effects, and several equally worthwhile preparation methods are needed.

**Check:** one player with NPCs in different roles has at least two completion strategies; the tester can identify everyone's contribution without a damage table; one unavailable companion leaves a harder but accessible exit. A second human is unnecessary for completion.

**Basis:** L05–L06.

<a id="m09-відбудова-як-авторство"></a>
### M09. Reconstruction as authorship

**Promise:** after a major event, the world does more than reset to factory settings—residents decide what the rebuilt place will become.

**Player action:** propose rebuilding a damaged public garden as terraces, a market space, or a quiet area with rainwater collection.

**System response:** projects compete for the same resources; residents and owners have different needs; completed reconstruction changes available actions and retains memory of the event. Not every reconstruction must change geography or canon.

**Cost:** materials, labor, and compromise over the place's function. A reconstruction fund is not an infinite source of new money.

**Player control:** the right not to participate; the system restores basic functioning if volunteers are insufficient; a private home does not become a public experiment without its owner's consent.

**Abuse:** “destroy with an alternate account, earn the repair reward,” capture of space, and delaying restoration for extortion. Account for causes and related benefits, limit rewards for damage initiators, and set a basic-restoration deadline.

**Check:** a destroyer–repairer collusion has no guaranteed positive profit; a community without an active leader does not permanently lose service; at least two socially different reconstruction approaches have visible consequences.

**Basis:** L09–L10.

<a id="m10-лабораторія-дивних-можливостей"></a>
### M10. Laboratory of unusual possibilities

**Promise:** the world itself learns to create better conditions for ingenuity while preserving the player's right to understand changes.

**Player action:** voluntarily join a local experiment—for example, testing a new rule for interactions between sound and navigation signs. A participant may propose a hypothesis, leave evidence, or find a counterexample.

**System response:** an agent creates a candidate; it undergoes independent compatibility and abuse checks, simulation, and limited play, and is compared with an unchanged baseline. An accepted rule has a version, scope, explanation of change, and rollback path. A failed candidate remains a research record rather than a hidden active habit.

**Cost:** bounded experiment budget, computation, volunteers' time, and the possibility of rejecting an attractive idea. Useful evidence, including negative results, is rewarded.

**Player control:** voluntary participation, exit, separation from main assets, and a declared duration; no need to play continuously to retain participation.

**Abuse:** the agent gives itself high scores; participants hide errors to obtain rewards; a new version changes the acceptance criterion; a harmful skill spreads through shared memory. External signals, immutable experiment records, candidate-independent promotion authority, experience quarantine, and regression checks are needed.

**Check:** better textual self-assessment without better external results does not earn promotion; a candidate that violates isolation is rejected; previous behavior reproduces after rollback; no failed experiment changes the main world. “Stranger” does not mean “better.”

**Basis:** L02–L04, L09–L12. This is an original bridge to RSI. Scientific feasibility claims need checking against the separate analysis of the supplied survey.

<a id="4-яка-інфраструктура-потрібна-щоб-ці-механіки-не-були-лише-текстом"></a>
## 4. Infrastructure needed for these mechanics to be more than text

This is a preliminary responsibility boundary that must be reconciled with the repositories' actual architecture.

| Generic platform capability | What remains a Lokiravia product decision | Why it is needed |
|---|---|---|
| Events, state versions, causal relationships, reproducible scenarios | Which consequences the player sees, when, and through whom they learn about them | M03, M06, M09: distinguishing causality from rumor |
| Registry of properties, constraints, and compatible transformations | Craft vocabulary, available materials, style of discoveries | M01–M02: creativity is not reduced to arbitrary text |
| Authority checks, isolation, execution budgets | Experiment zones and permitted adventure scale | M04–M06, M10: narrative cleverness does not become a technical bypass |
| Memory with provenance, retention period, and deletion rights | NPC testimony, keepsakes, local history | M03, M07: the world remembers events rather than inventing a private past |
| Candidate registry, baselines, evaluation, promotion, rollback | Quality criteria, what makes a good surprise, where experimentation is acceptable | M10: RSI works with evidence rather than reflection alone |
| Resource limits and accounting for economic changes | Craft cost, team agreement, reconstruction rules | M01, M08, M09: new capabilities do not print infinite value |

The central dependency is: **generation proposes; a verified state transition determines what happened; narration explains the consequence from the character's available perspective**. The same generator should not simultaneously invent a result, judge fairness, validate evidence, and record a new rule.

<a id="5-принципи-гумору-для-продукту"></a>
## 5. Product principles for humor

1. **Start with an understandable desire.** Find lodging, feed friends, make a tool, shorten a journey. Without it, strangeness feels like random content.
2. **One strong shift in expectations.** An underestimated property worked, two professions collided, or an unexpected witness appeared. Do not add five incompatible jokes to every reply.
3. **The world takes its own rules seriously.** An NPC can calmly discuss a funny consequence. Universal hysteria among characters soon becomes exhausting.
4. **A choice remains after the joke.** Repair, reinterpret, explain, keep the oddity, invite a friend. Continuous helplessness is not adventure.
5. **Warmth needs its own time.** Players may watch water, decorate a workshop, or sit silently by a fire without a productivity reward.
6. **Not everyone must laugh at the same thing.** Comic intensity is a user preference and a property of a place. A restrained world is as complete as a carnival-like one.
7. **An audience's laughter does not justify the target's experience.** The system must separately account for participant, witness, and cost-bearer.

<a id="6-що-свідомо-не-переносимо"></a>
## 6. What we deliberately do not transfer

- Specific characters, names, unique objects, plot resolutions, recognizable jokes, or adventure sequences. We need an original world rather than a reconstruction of a literary franchise.
- Physical pain, medical condition, disability, or continuous online presence as a requirement for faster progression. Accessibility is not exchanged for a weaker character.
- Secret operator intervention in user state, retrospective justification of interventions, or fabricated system reasons for coercion.
- Hidden privilege allowing powerful clans to solve product problems by harassing others. World politics may involve conflict; platform access policy must be explainable.
- Forced bodily transformations, loss of interface vision, sexualized humiliation, or repeated killing near respawn as the standard way to entertain others.
- An economic monoculture of an overpowered strategy that renders all other activities pointless. Novelty should open a niche or an interesting tradeoff rather than always increase maximum power.
- Automatic escalation in every adventure's scale. Not every unusual chair must change a continent. A large consequence matters more when the world lets small actions remain small.
- The assumption that something funny to read is enjoyable to experience as a player. A literary author controls pace, recovery, and resolution; a live game must provide those qualities systematically.

<a id="7-кандидати-в-наступний-дослідницький-і-продуктовий-беклог"></a>
## 7. Candidates for the next research and product backlog

These are dependent stages, not a promise to implement ten mechanics at once.

| ID | Next outcome | Completion condition | Why it precedes the next stage |
|---|---|---|---|
| SAFE-R01 | Continue sequential reading of all three books from uncovered sections | A fragment-level ledger, a map of new motifs and counterexamples, and recorded discrepancies with this note | Current controlled text coverage of 7.79% is insufficient to claim a completed series analysis |
| SAFE-R02 | Check which scenes readers call warm, funny, cruel, or boring | Small interview/annotation study separating initiator, witness, and affected-party roles | Do not substitute one researcher's intuition for reader response |
| SAFE-P01 | Tabletop prototype of M01 + M02 + M08 | One player with NPC companions creates a useful unexpected application; there is an explainable failure and second approach; every role is meaningful | Tests the central promise without an expensive world or multiplayer |
| SAFE-P02 | Tabletop causal scenario of M03 + M06 + M09 | Two independent perspectives, one fading and one propagating consequence, effective reconstruction | Reveals unfair external effects before scaling |
| SAFE-P03 | Quiet-session prototype of M07 | Participant voluntarily chooses an activity without combat; an object or place has personal significance; no pressure to return | Tests the promise of “living,” rather than merely completing content |
| SAFE-A01 | Specification for one verifiable M10 cycle | Baseline, candidate, independent evidence, rejection, acceptance, isolation, and rollback described in one scenario | Gives RSI a concrete improvement subject so it does not remain a slogan |
| SAFE-A02 | Metrics and negative-scenario matrix | Quality for different roles; economic stability; explainability; proportion of content not requiring escalation; accessible exit | Avoid optimizing only strange-event count, online time, or agent self-assessment |

The first implementation hypothesis needs only one place, a few material properties, three professional roles, and a small community with different interests. Interaction depth determines ambition, rather than the number of procedurally named continents. This narrow space must demonstrate: **the player can surprise the system, the system can fairly surprise the player, and the community remembers both**.
