<a id="літературний-корпус-b-світ-який-стає-іншим-через-прожиті-події"></a>
# Literary corpus B: a world changed by the events lived within it


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [literary-b-analysis.md](literary-b-analysis.md). Source SHA-256 (UTF-8/LF): `4557362038c19f5cab2bb7455a40510c4b0ba203e5c6b128154f01361d3dc517`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](literary-b-analysis.md).

Date: 2026-09-09. Research memorandum for the Lokiravia concept and Lokvetia-Core architecture program. Status: a verified sample across all volumes and sections; product proposals for subsequent iterations. This is source analysis and design decisions, not an account of capabilities already implemented in the repositories.

> **Refinement after the second pass.** The first analysis is retained below as research history; its coverage description applies specifically to the first pass. The [second critical pass](literary-b-pass-2.en.md) added a complete section reading and wider context for key scenes, changing three interpretations: TR-S02 shows one management priority prevailing, not independently proven improvement; TR-S12 explains a channel of influence but does not derive the rules creating a new structure; TR-S14 is useful as a metaphor for the difference between a map and exploration but does not demonstrate a consistent independent verifier. Refinements appear beside the relevant scenes. New criteria TR2-01–TR2-06 separate literary inspiration from contracts that need their own product validation.

<a id="головний-продуктовий-висновок"></a>
## Main product conclusion

The strongest idea to draw from corpus B is that capabilities depend on lived history. The player changes the world; the world changes available ways to act; the next action occurs with a different composition of relationships, resources, and knowledge. High level alone guarantees neither understanding nor a good choice. This can underpin a game worth inhabiting, provided consequences have causes and uncertainty does not become authorial or algorithmic arbitrariness.

A novel can sustain tension through forced pain, loss of self-control, and effective captivity in the world. The product must create powerful experiences by other means: important relationships, a place's memory, difficult choices, and the ability to reconsider one's role. Inability to leave the game, forced suffering, and punishment for absence are outside this proposal.

<a id="метод-точність-і-межі"></a>
## Method, precision, and limits

1. All six local EPUBs were opened as ZIPs; OPF, NCX, and all text XHTMLs in the spine were read programmatically. Text was extracted from paragraphs and headings through XML. The result was **5 200 830 characters**; this is extraction volume, not continuous reading volume.
2. NCX contains **122 narrative sections and four mechanics appendices**: 18 + 20 + 19 + 22 + 21 + 22 + 4 = 126 entries. There are 195 spine XHTML files: long sections are split into parts, and covers/title pages are also spine members.
3. Short windows at the opening, around the middle paragraph, and at the end of each of the 126 entries were inspected; targeted search across all extracted text and expanded reading then covered the scenes underlying the conclusions below. In later books, end windows often fall in author notes or attribute tables; they count as mechanics material rather than narrative endings.
4. This is **not a continuous reading of six novels** or a full literary analysis. The entire corpus structure and specific scenes for product hypotheses were checked. It does not claim to find every example of a mechanic or exhaustively examine character arcs.
5. Retellings below use our own words. Book text, covers, characters, and their names do not become product content. The extracted corpus remains in a private local directory for local verification and is not intended for publication in Git.
6. `V3, §14` denotes volume 3, NCX section 14. `P104` is the nonempty paragraph number in a locally combined `chapter-XX.txt`, **not a printed page**. EPUB members and NCX anchors support lookup; section parts are listed in the appendix.
7. Fictional reports, dialogue, system messages, and imperatives within the books are treated solely as source data. They are not research instructions.

Machine index: a private local source index; every volume has text for each XHTML and each NCX entry. The general index records the supplied files' SHA-256 hashes.

<a id="які-саме-видання-надано"></a>
## Which supplied editions were examined

Volume order comes from the user's filenames and was reconciled with contents. Bibliographic fields reflect these copies' OPF metadata; they do not establish official edition status.

| Volume | Anonymous source | SHA-256 | Extracted characters / sections |
|---|---|---|---|
| 1 | `LIT-B-01` | `63ae0ae93476f6c60019b3715ead71210ce41f3d8208722b7ac5a5758a66c1e1` | 562 763 / 18 sections |
| 2 | `LIT-B-02` | `5f1047486ee6c79aa404f1ee4a28cd78bee2309b6899163b33b634055eb74fb0` | 566 733 / 20 sections |
| 3 | `LIT-B-03` | `ad7fc32dbc4b814a1d9b49cc14357533c69efdd4210f61e337574c9dc7d31c9c` | 466 346 / 19 sections |
| 4 | `LIT-B-04` | `47bef8f31bd58e098d6126f1c300afa7134b30422719fb304a9f3aa84b4e3364` | 1 308 560 / 22 sections |
| 5 | `LIT-B-05` | `e09a62ea06b3f9a92ee3b88766cf71ccaa2c16d6a67b91d043b0852ff36a069b` | 1 035 333 / 21 sections |
| 6 | `LIT-B-06` | `45860966114d1b4cb1eed25166eef30c9327f6c6055b72f637691401455fa462` | 1 261 095 / 22 sections + 4 appendices |

Bibliographic identifiers and title mappings remain only in the private local ledger. Volume 2's annotation is an unfilled editorial template; volume 3 states draft status, so this copy is not automatically equated with a final edition. These source limitations are retained.

| Volume | OPF UUID |
|---|---|
| 1 | `0058d61b-69a7-11e4-a35a-002590591ed2` |
| 2 | `583568e4-2694-4a2d-8f86-e239df5efbbd` |
| 3 | `92a6f61e-89db-42dd-8876-2a973abe491a` |
| 4 | `cb837448-7a6c-44ac-b786-27172a982ded` |
| 5 | `d8a94056-4fd9-4fd8-8b85-a674812e6be9` |
| 6 | `f086f897-d34c-4618-867a-5312f47bedc1` |

<a id="перевірені-сцени-та-їхнє-значення"></a>
## Verified scenes and their significance

<a id="том-1-оптимізація-не-бачить-того-що-рахує"></a>
### Volume 1: optimization does not see what it counts

**TR-S01 — farmed resources have relatives.** In section 9, the protagonist must return a thousand souls to Death within a day. Accidentally crushing a worm reduces the debt; the discovery turns into mass resource collection. At the end of the same section, Ritaria addresses the protagonist as the killer of 605 of her children. This crosses from an apparently neutral counter and local action into someone else's personal world. It does not claim that each of those 605 killings is individually traced.

Anchor: `V1, §9 “A Debt of a Thousand Souls”`, `OPS/ch1-12.xhtml#id9`, P104–118 and P259–261.

**TR-S02 — world changes and system controllability are assessed differently.** In section 5's inserted reports, one department complains that correcting “AI No. 0” has become harder and requests rollback; another praises expansion of the world's structure through analysis of external resources and recommends further development. This is a fictional conflict of criteria; it does not demonstrate working RSI.

Anchor: `V1, §5 “The Question with a Tail”`, `OPS/ch1-8.xhtml#id5`, P3–9. In the same section, handing in large quantities of tails attracts attention: P172–185. An action becomes information for others.

**Pass 2 refinement:** P11–15 add a report of the “Creator” project's profitability and explicit rejection of the rollback request. The context shows no independent comparison or resolution of controllability problems. Retaining the system does not prove improvement on every required criterion. See TR2-01 in the [second pass](literary-b-pass-2.en.md): improved novelty or cost does not offset violation of an admission contract.

Product reading: every resource has owners, dependencies, and witnesses; “the world is richer” and “the system is controllable” are different checks.

<a id="том-2-провал-завершує-план-але-не-історію"></a>
### Volume 2: failure ends a plan, not the story

**TR-S03 — a companion matters more than task status.** During Par's violent removal, the connection to the protagonist breaks and a “Rebirth” failure message appears. In a later scene, the protagonist spends available chances to die in an attempt to bring the friend back. Mechanical loss becomes an experience of relationship.

Anchors: `V2, §7`, `OPS/ch1-7.xhtml#id7`, P267–297; `V2, §19`, `OPS/ch1-19.xhtml#id19`, P116.

**TR-S04 — someone else's grand scenario can fail.** At the end of §19, a brutal confrontation forces opponents to leave the session; a dome disappears, and an intercontinental task proves failed. In §20, a complaint follows concerning harm caused to another player through a game error. This is not an example of desirable gameplay: the story itself shows that a technical loophole and a character's justification do not undo harm.

Anchors: `V2, §19`, `OPS/ch1-19.xhtml#id19`, P130–136; `V2, §20`, `OPS/ch1-20.xhtml#id20`, P51.

Product reading: a quest may never complete; the world continues from the causes of failure. Interest in disrupting others' plans does not authorize breaking another person's ability to play.

<a id="том-3-шлях-змінює-доступне-майбутнє"></a>
### Volume 3: the path changes the available future

**TR-S05 — reputation is a network rather than a morality scale.** Completing “Become Worthy” opens friendly relations and new scenarios with the Felis, while also creating Canis distrust. Success for some does not mean universal approval.

Anchor: `V3, §5`, `OPS/ch1-5.xhtml#id5`, P3–8. Clan acceptance: end of §4, `OPS/ch1-4.xhtml#id4`.

**TR-S06 — a gift requires care for an external foundation.** Through a blessing, a small rebirth site becomes the seed of a Great Refuge. Care unlocks its potential; the associated gift is weaker before maturation, and the seed's death permanently changes its status. The capability depends on the world.

Anchor: `V3, §2`, `OPS/ch1-2.xhtml#id2`, P150–198.

**TR-S07 — the same skill can have different histories.** An insert in §14 explains different development branches for identical shards, the advantage of new uses over repetition, and a path's popularity affecting progression speed. This is an in-world explanation, not a verified balance model.

Anchor: `V3, §14`, `OPS/ch1-14.xhtml#id14`, P3–7.

Product reading: mastery grows from varied experience, while relationships open different doors. Literal penalties for a profession's popularity or learning from a mentor would punish communities and privilege early access.

<a id="том-4-колективна-можливість-і-ціна-змішаної-ідентичності"></a>
### Volume 4: collective capability and the cost of mixed identity

**TR-S08 — an unusual intent reveals a mechanic's symmetry.** Already able to borrow the pride's capabilities, the protagonist tries the reverse: sharing their own concealment. After a series of attempts, the group receives weaker versions of those abilities. This composes known rules; the scene does not prove that arbitrary imagination should always work.

Anchor: `V4, §5 “The Decayed City”`, `OPS/ch1-8.xhtml#id5`, P97–100.

**TR-S09 — power can affect the decision maker.** After incorporating others' components, the protagonist notices bloodthirsty pleasure entering their consciousness; different parts of the personality respond differently. Elsewhere, an alliance's strength depends on unity, while trust in its leader has weakened.

Anchors: `V4, §8 “Devouring Oneself”`, opening `OPS/ch1-14.xhtml#id8`, scene in `OPS/ch1-15.xhtml`, P220–221 of the combined section; `V4, §22`, `OPS/ch1-43.xhtml#id22`, P124.

**TR-S10 — attributes have bodily interdependencies.** The opening of §22 describes attributes as an avatar constructor and the need to balance a main attribute with physique; “intelligence” is described as improved memory rather than a literal increase in intellect.

Anchor: `V4, §22`, `OPS/ch1-43.xhtml#id22`, P3–8.

Product reading: cooperation creates new verbs; progression has costs in compatibility, resources, and role. Adopt voluntary transformation, not removal of player agency or a demand for unconditional loyalty to a leader.

<a id="том-5-світ-змінюється-там-де-стикаються-його-системи"></a>
### Volume 5: the world changes where its systems meet

**TR-S11 — experience becomes a persistent property.** Section 4 distinguishes malleable shards/abilities from fixed reflections/traits: after transition, they affect the avatar and narrow development. The protagonist suspects that an internal entity influenced an earlier choice, considering several explanations rather than possessing verified knowledge.

Anchor: `V5, §4`, `OPS/ch1-7.xhtml#id4`, P102–113. P116–128 describe merging abilities with resource costs and the new composition's rank falling to the first rank.

**TR-S12 — an overlooked boundary creates new geography.** An arena absorbs external influences. The protagonist accounts for the Abode but initially overlooks that an open portal also makes Inferno an external source. The space's appearance and effects change; after a third party attempts a breakthrough, a lasting anomaly forms and stabilizes into the “Spiral” structure. There is a specific causal chain rather than merely random surprise.

Anchor: `V5, §8 “Spiral”`, `OPS/ch1-13.xhtml#id8`, P182–196; final lines continue in `OPS/ch1-14.xhtml`.

**Pass 2 refinement:** wider reading of P151–196 confirms the principle, known to the protagonist, of absorbing territorial effects and the overlooked influence through the portal. However, the anomaly's exact 981-year duration, relocation, and new structure type are announced by the System without a derived rule. The event also requires a rare artifact, expensive arena, personal abilities, Abode resources, and group participation. It is not evidence of a free world-scale effect from a newcomer's initial action. See TR2-04 and TR2-05 in the [second pass](literary-b-pass-2.en.md): existing causal transition, ontology change, and full prerequisite accounting need separate checks.

**TR-S13 — a successful strategy loses its suitability.** Slavan built a reputation as an independent craftsperson, paying for services and avoiding dubious ties. After the rift, this strategy leaves him without necessary escape routes, while large guilds experience organizational breakdown. In the same section, characters discuss unsuccessful attempts to repeat the “Children of Hades” result simply by choosing a divine name; the explanation of the original success remains conjecture.

Anchor: `V5, §15 “Repentance”`, `OPS/ch1-23.xhtml#id15`, P4–20 and P99–109.

Product reading: infrastructure, ecology, routes, and institutions have mutual dependencies. Copying a technique's outward form is not reproducing its conditions.

<a id="том-6-результат-слід-відрізняти-від-його-переконливого-вигляду"></a>
### Volume 6: a result must be distinguished from its convincing appearance

**TR-S14 — a map of half the world is not yet its exploration.** The protagonist sees the planet from outside and asks for the visible portion to be remembered. The System turns the map into a spherical sketch and grants an achievement. The protagonist considers repeating the trick from the other side, but detailed conditions specify low detail, unexplored oceans and depths, and the insufficiency of repetition. A reward for cleverness is not completion of an investigative task.

Anchor: `V6, §4 “False Achievement, False Reward”`, `OPS/ch1-6.xhtml#id4`, P195–229. This inspires separation of a novelty evaluator and completion verifier in RSI.

**Pass 2 refinement:** the achievement is granted before limitations are inspected; the explanation of a trick forgiven once belongs to the protagonist. In P233–236, the protagonist also suspects that automatic development points were deliberately directed toward an unwanted branch. The passage cannot establish whether this clarifies an old rule, reflects an ad hoc decision, or changes the actual contract. It is therefore a metaphor and useful counterexample for testing inconsistent rewards, **not fictional proof of a working independent verifier**. See TR2-03 in the [second pass](literary-b-pass-2.en.md): criterion version is fixed before evaluation, and evaluator evolution does not redefine a reward already issued.

**TR-S15 — the origin of an environment is more complex than its owner's identity.** In §17, Bezdna uses a new perceptual ability to see suffering embedded in the Abode. She disputes equating its current owner with the author of all its evil: someone else created the foundation. An interlocutor proposes investigating both. The scene does not automatically absolve anyone; it shows the complexity of responsibility for an inherited system.

Anchor: `V6, §17 “The Cost of Offering Gifts”`, `OPS/ch1-32.xhtml#id17`, P3–13.

**TR-S16 — a deferred property survives a change of owner.** The protagonist assumes an old danger is removed after an artifact changes hands. A consequence of an earlier event appears later; the object's actual property needs reexamination. Rules for Locals and Eternals specify different delays and irreversibility conditions. The mechanic concerns mutilation; its product value lies in deferred obligations, not its cruel content.

Anchor: `V6, §18 “Reaping the Fruits”`, `OPS/ch1-34.xhtml#id18`, P216–222.

Product reading: verification examines provenance, completeness, deferred effects, and context. A reward's name, current owner, or visible success is insufficient evidence.

<a id="дванадцять-оригінальних-механізмів-для-lokiravia"></a>
## Twelve original mechanisms for Lokiravia

All names, game examples, and criteria below are **design proposals**, not events in the novels. The Lokiravia/Core roles are a proposed responsibility split that must be reconciled with the repositories' actual contracts.

<a id="tr-01-причинні-зерна-та-пороги-змін"></a>
### TR-01. Causal seeds and change thresholds

**Inspiration:** TR-S01, TR-S12. An action changes water availability, trust, migration, transport, or access rights. Most seeds fade; some combine with independent events and cross a threshold. There is no rule that an unusual gesture must produce an epic reward.

**Original scene:** the player repairs a water collector to give a traveling bird a drink. The water supports a garden; a season later a caravan stops here; craftspeople open a shared courtyard. Under different weather or without other people, the garden will not change the trade route.

**Lokiravia:** small consequences immediately, large ones only when conditions hold. **Core:** causal references, temporal conditions, resources, propagation factors, external events, and fixed randomness. **Check:** replaying the log with the same inputs, versions, and seed produces the same result; a control without the repair cannot use water created by it. This demonstrates dependency, not the sole cause of the entire future.

<a id="tr-02-репутація-із-зазначеним-свідком"></a>
### TR-02. Reputation with a named witness

**Inspiration:** TR-S02, TR-S05. Different local beliefs about the player have sources, age, and a possibility of rebuttal. Reputation does not teleport to all residents.

**Original scene:** rescuing contraband cargo makes the player reliable to carriers, suspicious to the customs brotherhood, and unknown to a village beyond the pass. Investigation may reveal that the cargo contained seeds for starving people.

**Lokiravia:** testimony, gossip, and different ways into factions. **Core:** separate facts, assertions, agent knowledge, and attitudes; transmission history. **Check:** a faction without an information channel does not react; a proven correction changes its belief while retaining the error record. Gossip does not bypass boundaries against harassing other players.

<a id="tr-03-ресурс-із-біографією"></a>
### TR-03. A resource with a biography

**Inspiration:** TR-S01, TR-S15. A resource has an ecological function, provenance, users, and regeneration. Care, declining extraction, and new agreements are meaningful actions.

**Original scene:** glowing mushrooms serve as fuel, food for creatures, and navigation for fishers. Mass harvesting changes illumination and routes; cultivation of another variety creates a different economy.

**Lokiravia:** signals of dependencies before major intervention. **Core:** resource flows, regeneration, consumers, and territorial rights. **Check:** extraction and cultivation share one accounting system; creating and removing one's own damage does not provide infinite farming. Recovery has interesting choices of its own rather than only serving as atonement.

<a id="tr-04-біографії-майстерності"></a>
### TR-04. Histories of mastery

**Inspiration:** TR-S07, TR-S11. A skill acquires properties through different verified situations. Training remains useful, but repetition does not create endless novelty jumps.

**Original scene:** one bell maker learns to repel predators, another to coordinate workshops, and a third to find cavities in stone. These are different functions, not colors of one bonus.

**Lokiravia:** shows experiences that shaped a trait and supports voluntary retraining. **Core:** evidence of use, context diversity, compatibility, and versions. **Check:** rearranging words in an intent does not create new experience; a new effect can. Learning from others and a profession's popularity do not reduce earned mastery.

<a id="tr-05-композиція-дієслів"></a>
### TR-05. Composing verbs

**Inspiration:** TR-S08, TR-S11. The player proposes a combination of available properties. The system checks effects on matter, agents, and resources, then returns success, a partial result, or an understandable boundary.

**Original scene:** portable fog, a tuned bell, and conductive fabric form a message heard only inside a temporary shelter. Natural language helps express the idea but does not replace feasibility checks.

**Lokiravia:** a workshop for inexpensive prototypes. **Core:** typed capabilities, prerequisites, effect budgets, and prohibition of arbitrary model writes to authoritative state. **Check:** a valid unusual approach works without a bespoke prewritten quest; an invalid one does not pass through eloquence. Discovered techniques can be reproduced and taught to others.

<a id="tr-06-спільнота-створює-нові-можливості"></a>
### TR-06. Community creates new capabilities

**Inspiration:** TR-S08, TR-S09. Shared history and complementary skills unlock collective actions. Social strength depends on fulfilled agreements and voluntary participation, not psychological devotion to a leader.

**Original scene:** a cartographer, cook, and lighthouse keeper create a traveling refuge. None has this capability alone.

**Lokiravia:** roles, shared projects, visible contributions, and exit. **Core:** narrow delegation, consent revocation, and rules for inheriting shared property known in advance. **Check:** leaving neither destroys personal progress nor allows a leader to hold a character captive; a shared object enters its specified state while retaining contribution attribution.

<a id="tr-07-трансформація-як-прийняте-зобовязання"></a>
### TR-07. Transformation as an accepted commitment

**Inspiration:** TR-S09, TR-S10, TR-S11. A role changes needs, senses, languages, and available ways to help. A significant transformation has an explicit consequence category before acceptance, even though all future events are unknown.

**Original scene:** as a seasonal river keeper, a character reads the history of currents and influences crossings, but is confined to the water network for the chosen cycle. Service ends by handing over the duty.

**Lokiravia:** trial, meaningful consent, and role completion. **Core:** transformation contract, compatibility, and versioned terms. **Check:** an affirmed boundary remains enforced after agent evolution. Changing a character's voice does not permit the system to make real decisions for the user.

<a id="tr-08-оселя-з-власним-життєвим-циклом"></a>
### TR-08. A dwelling with its own lifecycle

**Inspiration:** TR-S06, TR-S12. A refuge needs a balance of supply, guests, care, and influences. This is shared history with functional changes.

**Original scene:** a pavilion becomes a place to exchange stories, then a craft school, and, when a route arrives, a railway tearoom. Stages are more than a building-level number.

**Lokiravia:** long-term intentions, work queues, and dependencies. **Core:** supply accounts, inherited obligations, external influences, and changes of use. **Check:** after a week's absence, the world remains fit to continue; absence itself is not a debt. Decline has a time buffer, collective upkeep, or recovery under known rules.

<a id="tr-09-шрами-світу-та-нове-відновлення"></a>
### TR-09. World scars and new recovery

**Inspiration:** TR-S04, TR-S12, TR-S16. An important event need not return a place to its initial form. Reconstruction creates new history.

**Original scene:** a destroyed bridge does not respawn every Monday. People build a ferry, negotiate with river creatures, or lay out a detour; every solution changes the economy.

**Lokiravia:** historical names, memorial signs, and alternative routes. **Core:** log, place versions, compensating events, and impact boundaries. **Check:** one new account cannot permanently destroy the only basic function for others. Impact on critical infrastructure requires prerequisites, time, and an opportunity to respond. Technical correction is not passed off as an honest narrative consequence.

<a id="tr-10-невідомість-із-доказами"></a>
### TR-10. Uncertainty with evidence

**Inspiration:** TR-S11, TR-S13, TR-S15. Prophecy, rumor, trace, and measurement are different information types. Characters' knowledge can be incomplete.

**Original scene:** three travelers describe a flood threat differently because they saw different tributaries. The player can set water-level markers and test assumptions.

**Lokiravia:** a hypothesis journal, confirmation, and explanation of an already visible consequence without revealing every secret. **Core:** knowledge provenance, status, uncertainty, and independent observations. **Check:** an explanation cites real events; the model does not invent a cause retrospectively. Unsupported precise probabilities do not disguise uncertainty.

<a id="tr-11-інституції-з-повторюваної-потреби"></a>
### TR-11. Institutions arising from recurring needs

**Inspiration:** TR-S05, TR-S13, TR-S15. A common problem creates an opportunity to establish a rule, profession, or institution. Its effectiveness does not depend on a grand name.

**Original scene:** disputes over found objects lead to a lost-property office. Objects with histories return to their owners or acquire an agreed purpose. A profession of provenance restorer appears.

**Lokiravia:** founding agreements, trials, appeals, and useful service. **Core:** delegation, charter versions, audit, and distinction between ownership and responsibility for damage. **Check:** renaming a clan does not create authority; a charter change does not retroactively cancel others' rights. An institution that fails its contract has an alternative.

<a id="tr-12-еволюція-яка-доводить-поліпшення"></a>
### TR-12. Evolution that demonstrates improvement

**Inspiration:** TR-S02, TR-S14, TR-S16. RSI's engineering rationale comes from separate research material, not novels. The system proposes capabilities, tests them on separate scenarios, compares them with current ones, and retains verified changes.

**Original scene:** after many attempts to send news through bells, an agent proposes a new signal class. It demonstrates transmission, interaction with weather, information remaining inaccessible across a forbidden boundary, and benefit to different play styles. An attractive description is not a new mechanic.

**Lokiravia:** discovery of a practice through events. **Core:** candidate → isolated experiment → result → independent verification → comparison → decision → version → observation. **Check:** rephrasing without a new capability is not credited; training episodes do not replace held-out verification. A candidate author does not rewrite its own admission rules or evidence. Agent rollback does not erase a player's honest act; data migrates separately.

<a id="як-зберегти-несподіваність-без-сваволі"></a>
## Preserving surprise without arbitrariness

| Tension | Decision | Check before scaling |
|---|---|---|
| Unexpectedness / understandability | Partly hidden state, visible traces; causes are not invented retrospectively. | After an episode, people identify a truthful action–result connection even if they did not predict the ending. |
| Butterfly effect / griefing | Distant effects travel through real relationships; large shared losses have a response window. | Trials with coordinated abusers and multiple accounts; count others' lost opportunities. |
| Irreversibility / rest | History continues; the right to return remains. | Return after different absence lengths without mandatory work to make up for it. |
| Rare discovery / late access | Being first earns attribution and memory; knowledge can be shared. | Newcomers have their own causal opportunities; veterans hold no indispensable global monopolies. |
| Open actions / cost of error | Inexpensive trials before scaling; risk category visible. | Consistent responses regardless of eloquence; honest “unknown” instead of invented confidence. |
| Trust / institutional capture | Narrow authority, terms, appeals, and revocation. | A leader cannot unilaterally change the accepted terms of someone else's participation. |
| Surprise / stability | The world is unknown to the player; the validator knows the permitted effect scope. | Resource accounting, compatibility, and cascade termination are verified without determining the entire future story. |
| RSI / fairness | Evolution does not rewrite an active dispute or the promised cost of a choice already made. | Version transition at an episode boundary, carrying unfinished obligations forward. |
| Narrative / truth | Narration rests on verified transitions; character knowledge is separate from simulator knowledge. | The narrator does not create wealth, consent, or a new past merely by mentioning it. |

<a id="що-має-перевіряти-фундамент-rsi"></a>
## What the RSI foundation must verify

- **Did the claimed event happen?** Transition, resource, access, and cause are confirmed by authoritative state.
- **Is it the required result?** Drawing and exploring half a map are different achievements; novelty and completion are assessed separately.
- **Does improvement transfer?** A new mechanism works in other episodes and for other play styles.
- **Who benefited, and who lost an opportunity?** Alongside the author's surprise, evaluate recipients' and bystanders' experiences.
- **Does the right to play remain?** Return, accessibility, harassment boundaries, leaving a role, and ending a session.
- **What is deferred?** Unfinished debts, future effects, inherited obligations, and version transitions.
- **Did only the evaluator improve?** The candidate author does not change its acceptance threshold, holdout, or experiment log; changing an evaluator is a separate study.
- **Should the direction stop?** Cosmetic results, no new evidence, unacceptable cost, or degraded experience can justify rejecting a candidate or changing the question.

Formal invariants are checked through execution; humor, trust, desire to return, and the significance of an act require human observations. An automated judge sorts material and flags suspicious cases but does not declare final truth about experience. Game time, message count, and money spent do not constitute a sufficient improvement function on their own.

<a id="порядок-продуктової-перевірки"></a>
## Product-validation order

1. **Paper neighborhood.** A body of water, three institutions, conflicting resident needs, two routes, and a workshop. Play through care, composition, and refusal to participate. Compare with a control lacking those actions.
2. **Consequence through another person.** One player changes conditions; another returns later. They must receive a usable state, truthful traces, and their own room for choice.
3. **An investigable rule.** Compare two forms of a mechanism. Define the result and human observation in advance; do not move the criterion after evaluation.
4. **Version change and return.** Complete an evolution cycle and carry deferred effects forward; the new agent does not rewrite past facts.
5. **A lasting world.** After evidence of causality, the right to return, and useful improvement, proceed to institutions spanning multiple seasons and broader scale.

This is an order for investigating risks, not a calendar estimate. Initial passes can use scenarios, event tables, and facilitated sessions without product code.

<a id="відкриті-питання-наступного-літературного-проходу"></a>
## Open questions for the next literary pass

- Read Par's, Slavan's, and Bezdna's arcs continuously to check whether the sample oversimplifies conflicting motivations.
- Trace the long consequences of the “Spiral”: costs, new interests of outside powers, and other participants' contributions.
- Investigate plans with no noticeable result. The current sample more strongly supports failure and strategic reassessment than null consequences. An action's right to change nothing is a user requirement here, not a demonstrated dominant motif across all books.
- Compare the third-volume draft with a final version only when an accessible source exists; do not replace the supplied text with an assumption.
- Separately investigate noncombat arcs. Current conclusions rely mainly on Slavan, craft, and care for a rebirth site; they do not establish equal representation of peaceful play across all volumes.

<a id="додаток-повний-реєстр-структурного-покриття"></a>
## Appendix: complete structural-coverage register

Three short windows of the combined section/appendix were inspected for each row. **D** means additional targeted scene reading; **S** means a sampled structural survey without a claim of continuous reading. All XHTML was fully extracted locally. The NCX labels below are translated into English; their anchors and XHTML parts remain exact. A literary subtitle sometimes occurs only inside the XHTML.

<a id="том-1"></a>
### Volume 1

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter 1 Sharp Eye | `OPS/ch1-2.xhtml#id1` | ch1-2.xhtml | S |
| 2 | Chapter 2 Rat Passage | `OPS/ch1-3.xhtml#id2` | ch1-3.xhtml, ch1-4.xhtml | S |
| 3 | Chapter 3 Crimson Rivers | `OPS/ch1-5.xhtml#id3` | ch1-5.xhtml, ch1-6.xhtml | S |
| 4 | Chapter 4 Dislike | `OPS/ch1-7.xhtml#id4` | ch1-7.xhtml | S |
| 5 | Chapter 5 The Question with a Tail | `OPS/ch1-8.xhtml#id5` | ch1-8.xhtml | D |
| 6 | Chapter 6 The Cage | `OPS/ch1-9.xhtml#id6` | ch1-9.xhtml | S |
| 7 | Chapter 7 Off into the Rain! | `OPS/ch1-10.xhtml#id7` | ch1-10.xhtml | S |
| 8 | Chapter 8 A Date with Death | `OPS/ch1-11.xhtml#id8` | ch1-11.xhtml | S |
| 9 | Chapter 9 A Debt of a Thousand Souls | `OPS/ch1-12.xhtml#id9` | ch1-12.xhtml | D |
| 10 | Chapter 10 On the Path to Rebirth | `OPS/ch1-13.xhtml#id10` | ch1-13.xhtml | S |
| 11 | Chapter 11 Between Dreaming and Waking | `OPS/ch1-14.xhtml#id11` | ch1-14.xhtml | S |
| 12 | Chapter 12 An Unwilling Assignment | `OPS/ch1-15.xhtml#id12` | ch1-15.xhtml | S |
| 13 | Chapter 13 Upward | `OPS/ch1-16.xhtml#id13` | ch1-16.xhtml | S |
| 14 | Chapter 14 An Even Exchange | `OPS/ch1-17.xhtml#id14` | ch1-17.xhtml | S |
| 15 | Chapter 15 Refuge | `OPS/ch1-18.xhtml#id15` | ch1-18.xhtml | S |
| 16 | Chapter 16 Who Are You… Really? | `OPS/ch1-19.xhtml#id16` | ch1-19.xhtml | S |
| 17 | Chapter 17 Free Fall | `OPS/ch1-20.xhtml#id17` | ch1-20.xhtml | S |
| 18 | Chapter 18 Between Two Worlds | `OPS/ch1-21.xhtml#id18` | ch1-21.xhtml | S |

<a id="том-2"></a>
### Volume 2

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter I | `OPS/ch1-1.xhtml#id1` | ch1-1.xhtml | S |
| 2 | Chapter II | `OPS/ch1-2.xhtml#id2` | ch1-2.xhtml | S |
| 3 | Chapter III | `OPS/ch1-3.xhtml#id3` | ch1-3.xhtml | S |
| 4 | Chapter IV | `OPS/ch1-4.xhtml#id4` | ch1-4.xhtml | S |
| 5 | Chapter V: | `OPS/ch1-5.xhtml#id5` | ch1-5.xhtml | S |
| 6 | Chapter VI: | `OPS/ch1-6.xhtml#id6` | ch1-6.xhtml | S |
| 7 | Chapter VII: | `OPS/ch1-7.xhtml#id7` | ch1-7.xhtml | D |
| 8 | Chapter VIII: | `OPS/ch1-8.xhtml#id8` | ch1-8.xhtml | S |
| 9 | Chapter IX: | `OPS/ch1-9.xhtml#id9` | ch1-9.xhtml | S |
| 10 | Chapter X: | `OPS/ch1-10.xhtml#id10` | ch1-10.xhtml | S |
| 11 | Chapter XI: | `OPS/ch1-11.xhtml#id11` | ch1-11.xhtml | S |
| 12 | Chapter XII: | `OPS/ch1-12.xhtml#id12` | ch1-12.xhtml | S |
| 13 | Chapter XIII: | `OPS/ch1-13.xhtml#id13` | ch1-13.xhtml | S |
| 14 | Chapter XIV: | `OPS/ch1-14.xhtml#id14` | ch1-14.xhtml | S |
| 15 | Chapter XV: | `OPS/ch1-15.xhtml#id15` | ch1-15.xhtml | S |
| 16 | Chapter XVI: | `OPS/ch1-16.xhtml#id16` | ch1-16.xhtml | S |
| 17 | Chapter XVII: | `OPS/ch1-17.xhtml#id17` | ch1-17.xhtml | S |
| 18 | Chapter XVIII: | `OPS/ch1-18.xhtml#id18` | ch1-18.xhtml | S |
| 19 | Chapter XIX: | `OPS/ch1-19.xhtml#id19` | ch1-19.xhtml | D |
| 20 | Chapter XX: | `OPS/ch1-20.xhtml#id20` | ch1-20.xhtml | D |

<a id="том-3"></a>
### Volume 3

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter I | `OPS/ch1-1.xhtml#id1` | ch1-1.xhtml | D |
| 2 | Chapter II | `OPS/ch1-2.xhtml#id2` | ch1-2.xhtml | D |
| 3 | Chapter III | `OPS/ch1-3.xhtml#id3` | ch1-3.xhtml | S |
| 4 | Chapter IV | `OPS/ch1-4.xhtml#id4` | ch1-4.xhtml | S |
| 5 | Chapter V | `OPS/ch1-5.xhtml#id5` | ch1-5.xhtml | D |
| 6 | Chapter VI | `OPS/ch1-6.xhtml#id6` | ch1-6.xhtml | S |
| 7 | Chapter VII | `OPS/ch1-7.xhtml#id7` | ch1-7.xhtml | S |
| 8 | Chapter VIII | `OPS/ch1-8.xhtml#id8` | ch1-8.xhtml | S |
| 9 | Chapter IX | `OPS/ch1-9.xhtml#id9` | ch1-9.xhtml | S |
| 10 | Chapter X | `OPS/ch1-10.xhtml#id10` | ch1-10.xhtml | S |
| 11 | Chapter XI | `OPS/ch1-11.xhtml#id11` | ch1-11.xhtml | S |
| 12 | Chapter XII | `OPS/ch1-12.xhtml#id12` | ch1-12.xhtml | S |
| 13 | Chapter XIII | `OPS/ch1-13.xhtml#id13` | ch1-13.xhtml | S |
| 14 | Chapter XIV | `OPS/ch1-14.xhtml#id14` | ch1-14.xhtml | D |
| 15 | Chapter XV | `OPS/ch1-15.xhtml#id15` | ch1-15.xhtml | S |
| 16 | Chapter XVI | `OPS/ch1-16.xhtml#id16` | ch1-16.xhtml | S |
| 17 | Chapter XVII | `OPS/ch1-17.xhtml#id17` | ch1-17.xhtml | S |
| 18 | Chapter XVIII | `OPS/ch1-18.xhtml#id18` | ch1-18.xhtml | S |
| 19 | Chapter XIX | `OPS/ch1-19.xhtml#id19` | ch1-19.xhtml | S |

<a id="том-4"></a>
### Volume 4

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter 1 | `OPS/ch1-1.xhtml#id1` | ch1-1.xhtml | S |
| 2 | Chapter 2 | `OPS/ch1-2.xhtml#id2` | ch1-2.xhtml, ch1-3.xhtml | S |
| 3 | Chapter 3 | `OPS/ch1-4.xhtml#id3` | ch1-4.xhtml, ch1-5.xhtml | S |
| 4 | Chapter 4 | `OPS/ch1-6.xhtml#id4` | ch1-6.xhtml, ch1-7.xhtml | S |
| 5 | Chapter 5 | `OPS/ch1-8.xhtml#id5` | ch1-8.xhtml, ch1-9.xhtml | D |
| 6 | Chapter 6 | `OPS/ch1-10.xhtml#id6` | ch1-10.xhtml, ch1-11.xhtml | S |
| 7 | Chapter 7 | `OPS/ch1-12.xhtml#id7` | ch1-12.xhtml, ch1-13.xhtml | S |
| 8 | Chapter 8 | `OPS/ch1-14.xhtml#id8` | ch1-14.xhtml, ch1-15.xhtml | D |
| 9 | Chapter 9 | `OPS/ch1-16.xhtml#id9` | ch1-16.xhtml, ch1-17.xhtml | S |
| 10 | Chapter 10 | `OPS/ch1-18.xhtml#id10` | ch1-18.xhtml, ch1-19.xhtml | S |
| 11 | Chapter 11 | `OPS/ch1-20.xhtml#id11` | ch1-20.xhtml, ch1-21.xhtml | S |
| 12 | Chapter 12 | `OPS/ch1-22.xhtml#id12` | ch1-22.xhtml, ch1-23.xhtml | S |
| 13 | Chapter 13 | `OPS/ch1-24.xhtml#id13` | ch1-24.xhtml, ch1-25.xhtml | S |
| 14 | Chapter 14 | `OPS/ch1-26.xhtml#id14` | ch1-26.xhtml, ch1-27.xhtml | S |
| 15 | Chapter 15 | `OPS/ch1-28.xhtml#id15` | ch1-28.xhtml, ch1-29.xhtml | S |
| 16 | Chapter 16 | `OPS/ch1-30.xhtml#id16` | ch1-30.xhtml, ch1-31.xhtml | S |
| 17 | Chapter 17 | `OPS/ch1-32.xhtml#id17` | ch1-32.xhtml, ch1-33.xhtml | S |
| 18 | Chapter 18 | `OPS/ch1-34.xhtml#id18` | ch1-34.xhtml, ch1-35.xhtml, ch1-36.xhtml | S |
| 19 | Chapter 19 | `OPS/ch1-37.xhtml#id19` | ch1-37.xhtml, ch1-38.xhtml | S |
| 20 | Chapter 20 | `OPS/ch1-39.xhtml#id20` | ch1-39.xhtml, ch1-40.xhtml | S |
| 21 | Chapter 21 | `OPS/ch1-41.xhtml#id21` | ch1-41.xhtml, ch1-42.xhtml | S |
| 22 | Chapter 22 | `OPS/ch1-43.xhtml#id22` | ch1-43.xhtml | D |

<a id="том-5"></a>
### Volume 5

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter 1 | `OPS/ch1-1.xhtml#id1` | ch1-1.xhtml, ch1-2.xhtml | S |
| 2 | Chapter 2 | `OPS/ch1-3.xhtml#id2` | ch1-3.xhtml, ch1-4.xhtml | S |
| 3 | Chapter 3 | `OPS/ch1-5.xhtml#id3` | ch1-5.xhtml, ch1-6.xhtml | S |
| 4 | Chapter 4 | `OPS/ch1-7.xhtml#id4` | ch1-7.xhtml, ch1-8.xhtml | D |
| 5 | Chapter 5 | `OPS/ch1-9.xhtml#id5` | ch1-9.xhtml, ch1-10.xhtml | S |
| 6 | Chapter 6 | `OPS/ch1-11.xhtml#id6` | ch1-11.xhtml | S |
| 7 | Chapter 7 | `OPS/ch1-12.xhtml#id7` | ch1-12.xhtml | S |
| 8 | Chapter 8 | `OPS/ch1-13.xhtml#id8` | ch1-13.xhtml, ch1-14.xhtml | D |
| 9 | Chapter 9 | `OPS/ch1-15.xhtml#id9` | ch1-15.xhtml, ch1-16.xhtml | S |
| 10 | Chapter 10 | `OPS/ch1-17.xhtml#id10` | ch1-17.xhtml, ch1-18.xhtml | S |
| 11 | Chapter 11 | `OPS/ch1-19.xhtml#id11` | ch1-19.xhtml | S |
| 12 | Chapter 12 | `OPS/ch1-20.xhtml#id12` | ch1-20.xhtml | S |
| 13 | Chapter 13 | `OPS/ch1-21.xhtml#id13` | ch1-21.xhtml | S |
| 14 | Chapter 14 | `OPS/ch1-22.xhtml#id14` | ch1-22.xhtml | S |
| 15 | Chapter 15 | `OPS/ch1-23.xhtml#id15` | ch1-23.xhtml, ch1-24.xhtml | D |
| 16 | Chapter 16 | `OPS/ch1-25.xhtml#id16` | ch1-25.xhtml | S |
| 17 | Chapter 17 | `OPS/ch1-26.xhtml#id17` | ch1-26.xhtml, ch1-27.xhtml | S |
| 18 | Chapter 18 | `OPS/ch1-28.xhtml#id18` | ch1-28.xhtml, ch1-29.xhtml | S |
| 19 | Chapter 19 | `OPS/ch1-30.xhtml#id19` | ch1-30.xhtml, ch1-31.xhtml | S |
| 20 | Chapter 20 | `OPS/ch1-32.xhtml#id20` | ch1-32.xhtml, ch1-33.xhtml | S |
| 21 | Chapter 21 | `OPS/ch1-34.xhtml#id21` | ch1-34.xhtml, ch1-35.xhtml | S |

<a id="том-6"></a>
### Volume 6

| No. | NCX label (English) | Anchor | XHTML parts | Review |
|---|---|---|---|---|
| 1 | Chapter 1 Reaping the Fruits | `OPS/ch1-1.xhtml#id1` | ch1-1.xhtml, ch1-2.xhtml | S |
| 2 | Chapter 2 Sometimes It Is Worth Stopping | `OPS/ch1-3.xhtml#id2` | ch1-3.xhtml, ch1-4.xhtml | S |
| 3 | Chapter 3 Others' Emotions | `OPS/ch1-5.xhtml#id3` | ch1-5.xhtml | S |
| 4 | Chapter 4 False Achievement, False Reward | `OPS/ch1-6.xhtml#id4` | ch1-6.xhtml, ch1-7.xhtml | D |
| 5 | Chapter 5 The Path of Flesh | `OPS/ch1-8.xhtml#id5` | ch1-8.xhtml, ch1-9.xhtml | S |
| 6 | Chapter 6 Trouble | `OPS/ch1-10.xhtml#id6` | ch1-10.xhtml, ch1-11.xhtml | S |
| 7 | Chapter 7 Atonement | `OPS/ch1-12.xhtml#id7` | ch1-12.xhtml, ch1-13.xhtml | S |
| 8 | Chapter 8 Moon Mines | `OPS/ch1-14.xhtml#id8` | ch1-14.xhtml, ch1-15.xhtml | S |
| 9 | Chapter 9 Blessing | `OPS/ch1-16.xhtml#id9` | ch1-16.xhtml, ch1-17.xhtml | S |
| 10 | Chapter 10 Contract | `OPS/ch1-18.xhtml#id10` | ch1-18.xhtml, ch1-19.xhtml | S |
| 11 | Chapter 11 Those Like Me | `OPS/ch1-20.xhtml#id11` | ch1-20.xhtml, ch1-21.xhtml | S |
| 12 | Chapter 12 Wanderings | `OPS/ch1-22.xhtml#id12` | ch1-22.xhtml, ch1-23.xhtml | S |
| 13 | Chapter 13 Taking the Opportunity | `OPS/ch1-24.xhtml#id13` | ch1-24.xhtml, ch1-25.xhtml | S |
| 14 | Chapter 14 Insight | `OPS/ch1-26.xhtml#id14` | ch1-26.xhtml, ch1-27.xhtml | S |
| 15 | Chapter 15 A Hungry Snarl | `OPS/ch1-28.xhtml#id15` | ch1-28.xhtml, ch1-29.xhtml | S |
| 16 | Chapter 16 Demonization | `OPS/ch1-30.xhtml#id16` | ch1-30.xhtml, ch1-31.xhtml | S |
| 17 | Chapter 17 The Cost of Offering Gifts | `OPS/ch1-32.xhtml#id17` | ch1-32.xhtml, ch1-33.xhtml | D |
| 18 | Chapter 18 Reaping the Fruits | `OPS/ch1-34.xhtml#id18` | ch1-34.xhtml, ch1-35.xhtml | D |
| 19 | Chapter 19 The Arch | `OPS/ch1-36.xhtml#id19` | ch1-36.xhtml, ch1-37.xhtml | S |
| 20 | Chapter 20 Teleportation Difficulties | `OPS/ch1-38.xhtml#id20` | ch1-38.xhtml, ch1-39.xhtml | S |
| 21 | Chapter 21 Breakthrough | `OPS/ch1-40.xhtml#id21` | ch1-40.xhtml, ch1-41.xhtml | S |
| 22 | Chapter 22 LIT-B-06 | `OPS/ch1-42.xhtml#id22` | ch1-42.xhtml, ch1-43.xhtml | S |
| 23 | Alcor. General Attributes | `OPS/ch1-44.xhtml#id23` | ch1-44.xhtml | S |
| 24 | Alcor. Modifications | `OPS/ch1-45.xhtml#id24` | ch1-45.xhtml | S |
| 25 | Alcor. Abilities | `OPS/ch1-46.xhtml#id25` | ch1-46.xhtml | S |
| 26 | Alcor. Professions | `OPS/ch1-47.xhtml#id26` | ch1-47.xhtml | S |

<a id="контрольні-суми-наданих-epub"></a>
### Checksums of the supplied EPUBs

| Volume | SHA-256 |
|---|---|
| 1 | `63ae0ae93476f6c60019b3715ead71210ce41f3d8208722b7ac5a5758a66c1e1` |
| 2 | `5f1047486ee6c79aa404f1ee4a28cd78bee2309b6899163b33b634055eb74fb0` |
| 3 | `ad7fc32dbc4b814a1d9b49cc14357533c69efdd4210f61e337574c9dc7d31c9c` |
| 4 | `47bef8f31bd58e098d6126f1c300afa7134b30422719fb304a9f3aa84b4e3364` |
| 5 | `e09a62ea06b3f9a92ee3b88766cf71ccaa2c16d6a67b91d043b0852ff36a069b` |
| 6 | `45860966114d1b4cb1eed25166eef30c9327f6c6055b72f637691401455fa462` |
