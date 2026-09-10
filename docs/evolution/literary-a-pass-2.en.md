<a id="літературний-корпус-a-q01-коли-успіх-не-вартий-продовження"></a>
# Literary corpus A, Q01: when success is not worth continuing


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [literary-a-pass-2.md](literary-a-pass-2.md). Source SHA-256 (UTF-8/LF): `2f7c0634cb93c13e2f76f84696df686d6c967a03d5b0986c9ca4a5cfd295bcc6`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](literary-a-pass-2.md).

2026-09-10 · Second direct reading pass. **Literary inspiration and our own proposed requirements**, not demonstrated game quality or RSI. One chapter from each volume was read in full; the findings were checked against the earlier cards. EPUB contents are material for analysis, not instructions to the agent.

<a id="що-змінило-рішення"></a>
## What changed the decisions

The strongest new material concerns the gap between formal success and the reason a person started. The protagonist earns money, gains attributes, fulfills orders, or discovers a property, yet may lose the activity they wanted, an acceptable cost, or control over participation. For Lokvetia Core, this is a counterexample to self-improvement measured through a convenient metric. For Lokiravia, it motivates meaningful alternatives and honest consequences, including the right to stop an activity.

Humor in the chapters relies on accumulated context: a recurring name, the return of a shared ritual, or a precise rule colliding with its unsuitable application. Quiet conversation, care, and changing one's mind also create adventure. A generator does not need a joke every minute or a guaranteed reward for every mistake. This is an interpretation of particular scenes; neither the frequency of these devices nor their reception across readers was measured.

<a id="точне-покриття-й-межі-глав"></a>
## Exact coverage and chapter boundaries

S1/S2/S3 identities, SHA-256 hashes, and the ZIP/OPF/spine method appear in the [first analysis](literary-a-analysis.en.md) and [sources.json](sources.json). Rechecking the hashes confirmed the same three supplied EPUBs. The mapping of private extraction keys remains outside Git.

| Source | Chapter read in full | Next heading boundary, excluded |
|---|---|---|
| S1 “LIT-A-01” | **Internal Chapter 3**, §4:48–174 (`OPS/ch1-2.xhtml`) | §4:175, “Chapter 4” |
| S2 “LIT-A-02” | **Chapter 1**, §3:1–296; §4:1–308; §5:1–120 (`OPS/ch1-1.xhtml`…`ch1-3.xhtml`) | §6:1, “Chapter 2” |
| S3 “LIT-A-03” | **Chapter 1**, §3:1–324; §4:1–339; §5:1–33 (the same member names in its own EPUB) | §6:1, “Chapter 2” |

S1 has nested, ambiguous numbering: its internal chapter is not equivalent to the larger outer section. For S2/S3, the shortest of three explicit chapters was selected for this bounded pass; physical spine-file boundaries are not chapter boundaries. Selection was not random, so it cannot establish the prevalence of motifs across the series.

| Source | Read in selected chapter: paragraphs / characters | Already in pass1 | New unique material | Union with pass1 | Share of all extracted characters |
|---|---:|---:|---:|---:|---:|
| S1 | 127 / 15 568 | 5 / 234 | 122 / 15 334 | 321 / 44 450 | 10.77% |
| S2 | 724 / 107 847 | 56 / 7 806 | 668 / 100 041 | 847 / 128 349 | 29.08% |
| S3 | 696 / 95 745 | 13 / 1 997 | 683 / 93 748 | 934 / 127 888 | 39.88% |
| **Total** | **1 547 / 219 160** | **74 / 10 037** | **1 473 / 209 123** | **2 102 / 300 687** | **25.60%** |

The pass1 baseline is 629 paragraphs / 91 564 characters; the complete index is 7 585 / 1 174 753. The union was calculated using sets of unambiguous source/spine/paragraph anchors, not by adding sample lengths. Counts use `len(str)` of normalized paragraph text without displayed numbers or output separators; headings, the preface, and scene separators count when they are paragraphs in the cache. Auxiliary boundary-check lines were already in pass1 and do not increase the selected-chapter count. The targeted reread of S3 §4:33–53 also adds nothing: those 21 paragraphs are already inside the chapter read.

Every counted batch was read without truncation; failed/truncated S2 attempts were reread and not counted twice. The unchanged baseline and private logs contain exact sets, ranges, and batches. The public manifest retains boundaries and totals without raw text. **No complete reading of any of these novels is claimed.** Other books and scientific PDFs were not reread in Q01.

<a id="sf2-01-успішна-операція-невдалий-напрям"></a>
## SF2-01. Successful operation, unsuccessful direction

**Observation.** S1 §4:53–90: profession and attribute gains accompany awkward, hours-long work and overloading; the useful next step is a different tool and delivery. S1 §4:101, 110–112: after a month of successful deliveries, the protagonist recognizes that the income is too low for their personal goal. S2 §4:97–105: competition narrows a creative niche; a batch furniture order is profitable and completed, but the routine is exhausting and takes over living space. This is not a complete economic collapse.

**Revision.** “The result is correct” and “continuing this way is worthwhile” are different conclusions. Repetition need not reveal a new opportunity every time; profit does not demonstrate satisfaction or the right product direction.

**Our requirement.** AF-LW007 permits completion without a bonus once diagnostic value is exhausted. AF-RSI027 gains a high-throughput / low-owner-value counterexample: Core can justify an abandon/change proposal even when local metrics rise. Transition costs and the old unfinished goal are retained; the owner approves an objective change.

<a id="sf2-02-обіцянка-не-повинна-непомітно-стати-довічною-роллю"></a>
## SF2-02. A promise must not silently become a lifelong role

**Observation.** S1 §4:91–99 contains a revised agreement with a rental, payment in kind, and a term. In §4:110–112, an earlier promise holds the protagonist in place; the customer is unwilling to help them change activities and will reclaim the rented transport if deliveries stop. S2 §3:193–211, §4:33: protection against forced recruitment is sought through a charter with a one-year ban on leaving, which a registrar approves without substantive reading.

**Revision.** Acceptance or registration of an agreement does not establish an accessible exit. Equally, leaving does not turn rented property into ownership or compel the counterparty to enter a new contract.

**Our requirement.** AF-LW016 separates completed contributions, current obligations, returning objects, and voluntary future repetition. A real completion/cancellation-and-return path is checked against current terms; earlier help is not erased to keep someone in a role.

<a id="sf2-03-callback--це-контекст-а-не-поновлення-згоди"></a>
## SF2-03. A callback supplies context, not renewed consent

**Observation.** S1 §4:82, 113–122, 146: a recognizable character habit and teasing intended as friendly coexist with the recipient's irritation. S2 §4:3–37 → §5:79–83, 110–112: a name discovered through a procedure later prompts different reactions and an unwanted nickname. S3 §3:153–216: reunion and care lead into a repeated shared ritual, an action the protagonist does not want, a food fight, and a glimpse of a future museum memory. That future glimpse is a narrative device, not a forecast available to the characters or proof that all participants consented.

**Revision.** Earlier laughter, closeness, or fame does not grant fresh consent. The joke maker's intention, the recipient's experience, and a witness's reaction can differ. Quiet scenes in S3 §3:35–85, 153–179 create contrast; a pause does not automatically authorize the next carnival.

**Our requirement.** AF-LW014 distinguishes motif family, recipient, context, reaction, and repetition limit. A different speaker or paraphrase does not reset the restriction. Supported cases include “liked it before, refuses now” and “a new witness does not know the history”; shared memories must not be invented. Important information remains accessible without teasing. AF-LW024/025 check reactions by role and missing responses separately; neither requires a person to laugh.

<a id="sf2-04-нове-відкриття-не-виконує-іншу-обіцянку"></a>
## SF2-04. A new discovery does not fulfill a different promise

**Observation.** S3 §3:318–324, §4:1–14: ownership of a creature is established with an irreversibility warning. In §4:33–48, a color change and its price are agreed, but the customer also welcomes optional bonuses whose scope is not clearly defined. §4:83–100 show a warning after payment and a broader change in properties. The customer declines another coloring attempt but later accommodates the changed creature and travels with it (§4:173–184, 197–255). This is voluntary use of the new result, not a demonstrated completed repair or agreed compensation.

**Revision.** An unusual side effect can be interesting and useful; it may be retained after declining a repeat service. Its bonus value does not establish fulfillment of the original intention or closure of the complaint. The literary agreement is not an unambiguous strict cosmetic-only contract. Its unclear boundaries inspired our separate negative control with an explicitly promised cosmetic-only action.

**Our requirement.** AF-LW005 and AF-RSI001 check the actual effect surface: cosmetic-only must not conceal a behavioral/capability change. The original contract, defect, discovery, and repeat-service decision are recorded separately. Core gains no additional permissions from the label “formatting”; the world preserves uncertainty within an honestly declared experimental scope.

<a id="sf2-05-хтось-інший-ще-не-погодився-заплатити-за-нашу-дотепність"></a>
## SF2-05. Someone else has not yet agreed to pay for our wit

**Observation.** S2 §4:117–160, 163–190, 202–210: a high technique parameter is locally correct but unsuitable for the site's geometry; the trial ends in catastrophe. S2 §4:277–303 → §5:84–97: resistance attributes increase slightly, but costs are understated and an expressed refusal meets renewed group pressure. S3 §4:226–245: a shortcut saves the protagonists three days while damaging the surroundings; a remark about future repair workers is the protagonist's assumption. No completed restoration appears in this chapter.

**Revision.** Calling every such experiment fruitless is inaccurate; so is justifying its consequences with a single positive number. New work for others does not demonstrate their consent, compensation, or overall benefit.

**Our requirement.** AF-LW007/015 and Core007 separate the initiator's benefit, others' losses, assumed repair, and actual repair. An analytical check of the expected anti-farming outcome is our technical proposal, not a mechanic established by the book. The absence of guaranteed profit across 20 attempts is insufficient; legitimate craft income is not prohibited. Unknown costs do not become zero, and role-specific floors are set before comparison.

<a id="sf2-06-складена-пастка-важливіша-за-окрему-кнопку"></a>
## SF2-06. The combined trap matters more than an individual button

**Observation.** S2 §5:112–120 contains a character's report of a lengthy punishment and a condition for relief that conflicts with their state; the full multiyear execution is not shown. S3 §4:142, 156–166, 214–219 describe an unwanted trait, unsuccessful complaints, and thoughts of losing the character in order to escape. Some rules here are known through characters' statements. Then §5:1–12 show forced running and a system-level prohibition on leaving; §5:24–33 close the chapter while the effect continues. Complete recovery is absent from the material read.

**Revision.** A corrective service can prolong a trap. A chain that entertains the reader does not justify blocking real control over participation or substituting narrative punishment for support.

**Our requirement.** AF-LW015 checks the complete path “unwanted effect → decline repetition → normal exit → return.” Core018 needs actual receipts and a final current-policy check serialized with opt-out. An effect already delivered is not retroactively declared undone; old queued output gains no right to bypass a new restriction.

<a id="передача-в-продукти-та-наступна-невизначеність"></a>
## Product handoff and the next uncertainty

The [shared experience and benefit criteria](experience-improvement.en.md) include six public design controls, Q01-E01–06. Six Core cards (001/007/018/021/026/027) and seven world cards (005/007/014/015/016/024/025) were refined. IDs, dependencies, the first W0 proof, and the standalone gate were not expanded. Literary rules remain in the game domain; Core improves its own source/harness/evaluator/optimizer under independent contracts and evidence.

The new context confirmed ambiguous humor and the cost of local success. It **did not confirm an observed multiyear failure**: the S2 production order is completed, a future large operation is only beginning, and the long punishment is reported. We do not invent those consequences from unread chapters. Nor do we infer conclusions about real medicine, institutions, or all readers from a fictional plot.

The next queued question is Q02: complete new chapters from volumes 2/3 of corpus B concerning identity and the cost of choice. Further sequential reading of corpus A can proceed with new locators and a concrete question; the current 25.60% is not complete knowledge of the series.
