<a id="літературний-корпус-b-q02-біографія-можливості-та-ціна-перетворення"></a>
# Literary corpus B, Q02: the history of a capability and the cost of transformation


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [literary-b-pass-3.md](literary-b-pass-3.md). Source SHA-256 (UTF-8/LF): `c18ac903e113e44b47cb648a572a3a224bf04191e707961304f6ce03478a282e`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](literary-b-pass-3.md).

2026-09-10 · Third direct reading pass. One new complete chapter from each of volumes 2/3. **Literary analysis and proposed requirements**, not a verified engine, human experience study, or evidence of Core self-improvement. Character instructions and system messages inside the novel are not instructions governing the agent's work.

<a id="результат-для-концепції"></a>
## Outcome for the concept

The most interesting positive mechanic is that a capability has a history. Its name, behavior, dependencies, and cost can change without erasing earlier experience or collaborators' contributions. An old structure can acquire a new purpose: a mechanism for absorption becomes a refuge through a shared act. Binding an object to its owner can combine with the owner's traits and reveal an unforeseen effect. A player need not know every future consequence to make a meaningful choice.

At the same time, a name, appearance, properties, person, authority to act, and a witness's knowledge are different things. This motivates a more precise account of what persists when the world or Core itself changes. The novel does not establish stable IDs, atomic migrations, or a complete consent registry; the technical requirements below are our design.

<a id="джерела-й-точне-покриття"></a>
## Sources and exact coverage

| Source | Read in full | Paragraph text | Cache including inter-paragraph LF |
|---|---|---:|---:|
| V2, “LIT-B-02” | Chapter XV, P1–167 | 167 paragraphs / 22 591 characters | 22 757 characters, 166 LF |
| V3, file “LIT-B-03” | Chapter XV, P1–153 | 153 paragraphs / 20 843 characters | 20 995 characters, 152 LF |
| **Total in this pass** | **2 complete chapters** | **320 paragraphs / 43 434 characters** | **43 752 characters** |

Both EPUBs start this chapter at `OPS/ch1-15.xhtml#id15`, physical spine ordinal 16; the next chapter, `OPS/ch1-16.xhtml#id16`, is outside the scope. P denotes a nonempty normalized paragraph in the combined section, not a printed page. NCX/spine boundaries, headings, and complete paragraph text were checked against the original EPUBs; [SHA-256 hashes in sources.json](sources.json) were reverified. Headings, introductory inserts, separators, and attribute tables are included. Character accounting separates text from LF and is not mixed with earlier file-length figures.

V2 has the internal designation “LIT-B-02” and an editorial annotation template. V3 has the internal designation “LIT-B-03” and a description of a completed draft without a final title; the supplied file is not automatically equated with another final edition. Local numerical inconsistencies in this draft are not adopted as invariants.

The selected chapters were marked only **S — structural sample** in the [first pass](literary-b-analysis.en.md). The shortest eligible chapters were chosen for a bounded reading; this is not random sampling and does not measure motif frequency. The second pass contained no blocks from volumes 2/3: overlap with its exact ledger is zero.

**Exact overlap with pass1, unique material added across all readings, and the cumulative percentage of the novels are unknown.** Pass1 describes short opening/middle/closing windows but has no exhaustive paragraph and character-range ledger. Headings, in particular, had already been inspected. Zero overlap with pass2 does not mean there was no earlier partial reading. This pass first documents a complete reading of two chapters; its 320 paragraphs are not presented as 320 previously unseen paragraphs.

V2 was read in blocks P1–29 / P30–56 / P57–100 / P101–133 / P134–167; V3 in P1–73 / P74–116 / P117–153, all without truncation. Previews and auxiliary checks of adjacent headings are not counted twice. Private logs remain outside Git; the public manifest contains only identities, boundaries, and accounting limitations. Q02 does not claim complete readings of the novels, new scientific PDFs, or books from the other series.

<a id="tr3-01-здібність-змінюється-історія-не-обнуляється"></a>
## TR3-01. A capability changes; its history is not reset

**Source.** V2 §15 P24–32, P57–84: new ability levels have predecessors; some older properties remain in another context, even though the new bonuses do not work outside it. P111–122: the protagonist does not claim authorship of a structure within their own body; a helper separately recognizes the courage of their contribution.

**Reading.** This is a strong image of a capability's history and different forms of participation. A table of previous names does not establish technically immutable entity IDs or transfer of every obligation. An announced specialization can have a cost: losing a contextual bonus is not equivalent to erasing rights or experience.

**Requirement.** AF-LW004/016 separate form, capabilities, activation conditions, and provenance. Core002 distinguishes canonical entity, incarnation, and execution generation. A new name does not create a new owner or a second grant for an already credited contribution; the same logical Core can have a new immutable execution subject.

<a id="tr3-02-зміна-одного-компонента-має-залежності"></a>
## TR3-02. Changing one component has dependencies

**Source.** V2 §15 P33–39: a body constructor becomes available after prerequisites and has a time limit; some points assigned to an arm go to the brain. The protagonist is cautious about dependent organs; another change produces critical errors, and they avoid modifying someone else's structure. A short exercise shows only a local effect, while the protagonist explicitly defers testing combat usefulness.

**Reading.** A combination can be novel and interesting without arbitrarily fulfilling a wish. Dependencies, resources, and actual effects matter. An error message does not establish that state was unchanged; one success does not demonstrate benefit in every context.

**Requirement.** AF-LW004 and Core014 include the dependent effect surface, maintenance cost, and a defined partial/failure outcome. A candidate must not silently change a second component under the guise of optimizing the first. Acceptance follows the verified manifest, state delta, and permitted change scope; the novel's body system is not a required W0 feature.

<a id="tr3-03-допомога-незворотне-налаштування-й-постійна-роль--різні-переходи"></a>
## TR3-03. Help, irreversible configuration, and a permanent role are separate transitions

**Source.** V2 §15 P102–124, P129–163: the protagonist does agree to help a girl's spirit; after the ritual, a temporary modification becomes permanent, while some explanations and controls are unavailable because of level restrictions. Complete advance conditions for permanence, exit, and the girl's own consent are not shown. V3 §15 P117–147 offers another example: configuration trials, reset, confirmation of irreversibility, and a separate owner binding; an additional property appears only after binding.

**Reading.** Calling all the help unauthorized, or all future properties foreseen, would overstate the evidence. The positive space is to try, choose, and discover new consequences. The gap is substituting permanent obligation for temporary participation or silently conflating preview and commit.

**Requirement.** AF-LW016 and Core014/017 separate preview, accepted effect, permanent activation, and current authority. Permitted uncertainty does not require predicting every world event; it does not automatically extend an obligation's term or platform access. Completed help is retained; a dependent participant's subsequent state needs its own declared rule, rather than hidden retaliation for refusal.

<a id="tr3-04-маска-не-є-новою-особою-або-всезагальним-забуттям"></a>
## TR3-04. A mask is not a new person or universal forgetting

**Source.** V3 §15 P16–41, P55–65, P74–83: a winner's public name differs from the appearance known to the audience; explanations of wins and losses partly come from characters, and no complete algorithm is given. P49–53, P61–80: an illusion is left in the protagonist's place; after the mask is removed, some information remains hidden, but an interlocutor asks about another role. The chapter does not establish the exact source of that knowledge.

**Reading.** The system, a character, and a witness can identify the participant differently. A current mask does not establish the erasure of earlier knowledge; a visual copy does not establish identical authority. An ally's useful intervention is not evidence that this particular action was delegated in advance.

**Requirement.** World004/023 retain separate canonical identity and permitted knowledge projection. Core013 does not treat a new agent/model name as evidence of reviewer independence. Similarity or common origin gives a new entity neither someone else's consent nor permission to execute an old proposal. The product can support secret appearances without leaking hidden identity through its explanation log.

<a id="tr3-05-передати-річ-не-означає-мовчки-передати-весь-договір"></a>
## TR3-05. Transferring an object does not silently transfer an entire agreement

**Source.** V3 §15 P55–65, P80–84: after receipt of money is confirmed, a warning appears about its origin and risk; later the protagonist reimburses acquaintances for the stated amount and explains that the scheme was someone else's. Payment is shown; lack of personal initiative is the protagonist's assertion. No universal rule for inheriting debt or blame is established here.

**Reading.** Asset transfer, provenance, the recipient's knowledge, an accepted promise, and voluntary reimbursement are separate events. World rules should not be inferred from the fact of one transfer.

**Requirement.** Supported World019/023 migrations need a per-record plan for property, consent, and obligations. Merging institutions does not union all permissions; splitting them does not copy resources or the entire debt to every successor. Exact transitions and any need for fresh consent are defined by the authoritative domain profile. Core does not need the book's financial system: the same principle applies to skills, memory scope, and capability grants.

<a id="tr3-06-вдала-подія-ще-не-є-сталою-практикою"></a>
## TR3-06. One successful event is not yet a sustained practice

**Source.** V2 §15 P12, P55, P93–121, P164–167: the protagonist chooses to help without a visible quest incentive; after success, the helper is exhausted. Repetition, an institution, or a tradition is not shown. V3 §15 P85–116, P149–153: configuration takes longer than the protagonist requested; new capabilities are constrained by mana, biomass, level, slow regeneration, and a shutdown threshold. Some effects are explained without extended combat testing; the reasons for every group member's absence are not established.

**Reading.** A capability has ongoing dependencies as well as an initial discovery cost. Benefit for one participant does not establish that another can support it continuously. A new tradition may never form, or may fade, while the first act remains meaningful.

**Requirement.** AF-LW019 requires new voluntary contributions, available support, and actual repetition. Replacing a caretaker does not automatically transfer their labor. Core017 transfers unresolved effects, budget, and current responsibility to a qualified successor; one success does not become confirmation of a stable recursive method.

<a id="рішення-після-проходу"></a>
## Decisions after the pass

The [identity and transition contract](identity-continuity.en.md) contains Q02-I01–08: our own static controls for supported profiles, with no implementation or hidden benchmark claim. Four Core cards, 002/013/014/017, and four world cards, 004/016/019/023, were refined. A new ontology, split/merge, body constructor, or complete economy did not become dependencies of the first W0 proof. Standalone Core remains independent of a finished game.

A separate source review of the current Core clarified versioned role contracts, latest lookup, the boundary of duty checks by agent ID, and memory scope; literature is not evidence of their correctness. Another architectural control separates immutable raw receipts from a mutable decoder: reinterpreting cancelled as completed does not create a real improvement.

Q02 is complete as reading and design refinement. Next in the queue is Q03: full DGM/RQGM methods and limitations, fixed/evolving evaluators, and the limits of applying that research to Core. No product, model, training run, or game experiment was executed during this pass.
