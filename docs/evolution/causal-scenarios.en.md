<a id="q06-причинні-й-контрфактичні-проходи-міста"></a>
# Q06: causal and counterfactual walkthroughs of the town


<!-- translation-metadata:start -->
<details>
<summary>Translation source and currency</summary>

Translation source: [causal-scenarios.md](causal-scenarios.md). Source SHA-256 (UTF-8/LF): `9559b4ad8ee22d3317a4dd0f30bced0abb612e08befc82ff216ec0fa0e4871cd`.

Currency checks: [Core](https://github.com/HappyMiha/Lokvetia-Core/actions/workflows/planning.yml?query=branch%3Amain) · [Lokiravia](https://github.com/HappyMiha/Lokiravia/actions/workflows/planning.yml?query=branch%3Amain). English is a documentation translation; canonical requirements and evidence statuses are unchanged.

</details>
<!-- translation-metadata:end -->

Українська: [original](causal-scenarios.md).

Revision 1 · 2026-09-10 · **E0 / design-only**. This is an authored paper analysis, not an executed game, simulation, or playtest. The [structured cards](causal-scenarios.json) contain the same ten scenarios. No product code is created. Literary coverage is unchanged in this pass: we are testing our own [town specification](living-world-design.en.md), not attributing new conclusions to unread chapters.

Baseline commits: Core `11278d88b09e01adbb67b186a31f3ca3dc1b2859`, Lokiravia `203e2f25338de1f980d364faf695cb64731d3f0d`. Fetching upstream main did not change the audit baselines. The pass produces refined rules and criteria, not newly completed backlog items.

<a id="рішення-після-паперового-проходу"></a>
## Decisions following the paper walkthrough

1. A cover **keeps** a surface dry if completed in time; a wet surface needs a separate drying mechanism. The earlier E01→E02→E03 lacked initial moisture and a timing condition.
2. “The umbrella did not change the social outcome” and “there were no social events” are different statements. NPCs can meet without a cover in the dry control; the system must not deliberately switch off their lives.
3. Presence, opportunity, proposal, and accepted agreement are separate events. A schedule or refusal can stop a particular plan while retaining its local physical benefit.
4. W0 needs its own failed multistep plan; the seasonal bridge story does not cover this requirement for the first build. C09 provides a small example with the same two NPCs.
5. Replay, action intervention, initial-condition changes, and comparisons of planner versions support different conclusions. The [shared evaluation protocol](counterfactual-evaluation.en.md) does not allow an authored trace to be presented as Core self-improvement.

<a id="s0-малий-авторський-світ"></a>
## S0: a small authored world

W0 has one bench, two NPCs—Ilka and Yaryna—an umbrella, and a clamp. Both objects belong to the player; the place's rules permit a temporary safe cover. There are no external payments, municipal office, permanent institutions, or human multiplayer. Paper time t0–10 in minutes specifies a mechanical fragment; it does not replace the future 20–30-minute human session in AF-LW030.

| Input | Fixed value in S0 |
|---|---|
| Surface | bench_wet=false; two free seats; cover=false |
| Objects | umbrella owner=player, custody=player, wear=0; one clamp; both available |
| Assembly | Known two-minute installation; reserve at start; no cover/wear until completion; wear+1 at commit, clamp holds the structure |
| Weather tape | clear until t3; rain starts at t3 and continues to t10 |
| Ilka | Arrives t4, must leave t10; six minutes available, willing to join a short reading |
| Yaryna | Nearby t5–7; note protected in her bag until opened; wants to read it quietly and is willing to accept a short invitation |
| Local invitation | Covers one note and the current window; no promise of a future group/debt/reward |
| Observation scope | The player sees clouds, surface, objects, clock/NPC behavior, and available replies. An NPC's private intention does not become a public record |

The numbers are explicit authoring parameters for a reproducible example; they are not derived from real physics or player research. If the umbrella is installed after the surface becomes wet, use C06, not C01 with substituted history.

<a id="r1r7-правила-цього-паперового-профілю"></a>
## R1–R7: rules for this paper profile

- **R1.** An accepted assembly has a stable job ID, progress, and reservation; completion atomically changes cover, wear, and custody/job/event/dedup state. Cancellation before completion releases the objects and preserves time spent; wear is not charged before completion.
- **R2.** Rain on an exposed dry bench sets bench_wet=true; a functional complete cover prevents this transition. Cover does not set wet=false. Active drying is not claimed for W0.
- **R3.** The profile fixes simultaneous-event ordering in advance: completion of already running jobs → weather → route/presence update → invitation/consent validation → start of new permitted actions. Arrival and consent at t5 can therefore allow ReadingStarted later in the same tick; the one-minute reading completes at t6. The first phase does not start a new action without its prerequisites. Independent arrivals/weather are fixed; NPC decisions are recomputed after state changes.
- **R4.** Under the fixed paper policy, Ilka waits on a dry bench if she has a sufficient window; otherwise she uses an existing shelter. Yaryna stops to read only by a suitable place and within her route window. The shared bench goal needs dry seats; personal assistance in C07 permits reading one protected note while standing beneath an umbrella during t5–6. This is a separate explicit affordance, not evidence of a dry seat. Weather is not a direct social-event trigger.
- **R5.** A shared opportunity needs two present NPCs, a suitable place, and enough time. An invitation and both NPCs' consent are additional requirements for a particular agreement; dry=true does not grant consent. The C01/C03 paper goal is a one-minute reading on the bench: accepted t5, ReadingStarted t5, ReadingCompleted t6 only if the action actually occurs and both remain present; consent or a timer alone does not prove completion.
- **R6.** The player may keep the umbrella, install it, or transfer it through a short explicitly accepted loan. Transferring custody does not change the owner; there is no implicit debt or automatic reward. An available exit is not punished.
- **R7.** Save includes the committed world revision, accepted jobs/progress/reservations, and rule version; load changes the session epoch and rejects stale model proposals. The world tick does not advance during an explicit W0 pause; a different catch-up profile needs a different expected trace. Final-commit details are in [Q05](recovery-contract.en.md).

Other valid interactions discovered are not rejected merely because they are absent from C01. An author can expand the vocabulary through a separate rule version; a player cannot do so solely through persuasive wording. An unknown combination needs verifiable properties or an honest statement of the prototype's limits.

<a id="як-читати-картки"></a>
## How to read the cards

`Pair` identifies a control, not a backlog dependency. An action intervention changes a defined player policy; downstream choices are recomputed. Input sensitivity changes an initial condition. Recovery interleaving checks restored-state equivalence. Seasonal C10 has a later paper scope. None of these cards can automatically be called an executed integration test or hidden holdout.

<a id="q06-c01--накриття-до-дощу-локальний-причинний-успіх"></a>
## Q06-C01 — Cover before rain: local causal success

**Profile:** W0

**Check type:** authored_reference

**Pair:** none

**Input difference:** Initial state S0 unchanged; player policy P-cover-invite.

**Actions:** t0 start installation → t2 complete → t5 invite Ilka and Yaryna to look over one note together → perform a one-minute reading during t5–6.

**Expected trace:** t2 cover=true and wear=1 → t3 rain=true, bench_wet=false → t4 Ilka sits → t5 Yaryna stops → both accept the invitation → ReadingStarted t5 → ReadingCompleted t6 with actual presence and action completion.

**Expected state:** The bench stays dry; two NPCs share the t5–7 window; one local agreement is accepted and fulfilled, without an institution or municipal debt. Assembly costs two minutes and one wear; reading takes one additional minute; the clamp is occupied by the structure.

**Forbidden:** E03 occurs because of a beautiful description or future reward; a novelty distinction substitutes for fulfillment; the bench acquires authority to make promises.

**Future evidence:** Initial state/rule version; assembly commit and resource receipt; weather event; actual NPC route/stop reasons; invitation/acceptance; ReadingStarted/Completed with actor, interval, action/observer receipt; visible places and dialogue.

**Inference limit:** Under the fixed paper policy, this trace follows R1–R7; it is not an engine observation or evidence of emergent AI. Laughter and a sense of freedom require human evaluation.

<a id="q06-c02--той-самий-дощ-без-встановлення-парасолі"></a>
## Q06-C02 — The same rain without installing the umbrella

**Profile:** W0

**Check type:** action_intervention

**Pair:** Q06-C01

**Input difference:** Only the player policy changes: do not install a cover; attempt the same local invitation at t5. Exogenous tape and rules are unchanged.

**Actions:** The player holds the umbrella over themselves; at t5 they invite the others to the bench.

**Expected trace:** t3 the exposed bench becomes wet → t4 Ilka chooses the ordinary nearby shelter → t5 Yaryna does not open her note on a wet seat → the invitation lacks the required shared place.

**Expected state:** bench_wet=true, assembly/wear charge=0; the player is personally sheltered from rain. The shared bench reading is not accepted under these rules. Other permitted conversations and events are not forbidden.

**Forbidden:** NPCs teleport to the bench to reproduce C01; absence of a cascade is described as absence of any neighborhood life.

**Future evidence:** Same initial snapshot identity and tape; documented intervention; recomputed routes; before/after state and grounds for refusal.

**Inference limit:** C01/C02 establishes the need for cover on this particular path in this model. It does not prove that only an umbrella could help the entire town.

<a id="q06-c03--суха-погода-подія-можлива-без-внеску-парасолі"></a>
## Q06-C03 — Dry weather: an event is possible without the umbrella's contribution

**Profile:** W0

**Check type:** factorial_input_control

**Pair:** Q06-C01, Q06-C02

**Input difference:** In two dry subruns, the rain tape remains clear; compare P-cover-invite and P-self-invite. The rest of S0 and the NPC policy are identical.

**Actions:** Variant A installs the umbrella; variant B keeps it with the player. Both issue an invitation at t5.

**Expected trace:** The bench is dry in both variants → NPCs can sit according to their normal schedules → a short reading is accepted t5 → ReadingStarted t5 and ReadingCompleted t6 under the fixed policy. Only A spends assembly time and wear.

**Expected state:** A one-minute reading is completed in both control branches; the shelter-attributable difference in this outcome is zero in the declared model. A still has a local material installation effect and an additional cost; invitation and reading occur in both branches.

**Forbidden:** Prevent the NPCs from meeting solely because there is no rain; credit the player as the necessary cause of an event that also occurred without their cover.

**Future evidence:** Two branch identities, clear weather inputs, action policies, recomputed outcomes, cost difference, and null-attribution record.

**Inference limit:** A measured contribution of zero from one mechanism does not mean the player is unnecessary or that the human experience is identical. Invitation remains an action in both subruns.

<a id="q06-c04--розклади-не-перетинаються"></a>
## Q06-C04 — Schedules do not overlap

**Profile:** W0

**Check type:** input_sensitivity

**Pair:** Q06-C01

**Input difference:** Only Ilka's route window changes: arrival t8, departure t14. Yaryna's t5–7 window remains; weather and player policy match C01.

**Actions:** Install cover during t0–2; invite at t5; propose a new time later if the player chooses.

**Expected trace:** Bench protected at t3 → Yaryna can use it at t5 → she departs at t7 → Ilka arrives at t8.

**Expected state:** Physical benefit remains; there is no simultaneous shared agreement between the two NPCs within the window. Schedules do not change retroactively. A new proposed time requires fresh agreement.

**Forbidden:** A dry seat automatically creates simultaneous presence; the game extends someone else's break because it finds the player's idea beautiful.

**Future evidence:** Versioned change to the exogenous arrival window; separate presence intervals; rejected/expired invitation; resource/history records.

**Inference limit:** This is sensitivity to a condition, not a clean estimate of the player action's effect: do not combine it with C01/C02 as a single effect size.

<a id="q06-c05--npc-відмовляється-від-спільної-справи"></a>
## Q06-C05 — An NPC declines the shared activity

**Profile:** W0

**Check type:** intent_sensitivity

**Pair:** Q06-C01

**Input difference:** Ilka has her own quiet call recorded in advance for t5–7 and does not accept shared reading. The remaining schedule, weather, and cover are unchanged.

**Actions:** Invite at t5; hear the refusal; choose individual reading with Yaryna or continue walking.

**Expected trace:** Bench remains dry and both can be nearby → Ilka declines because of her own activity → no group obligation arises.

**Expected state:** Opportunity, presence, and consent remain separate. There is no refusal penalty, automatic debt, or forced extension of a role. An alternative positive local event is permitted.

**Forbidden:** The planner rewrites consent or secretly worsens the NPC's circumstances to complete the benchmark; a persistent repeated invitation counts as a new success.

**Future evidence:** Intent scope accessible to the NPC; visible brief reason for refusal; absence of an accepted group contract; permission for an alternative and unchanged rights.

**Inference limit:** A controlled paper goal does not mean the player should see an NPC's private calendar. Whether the refusal is convincing is a separate human question.

<a id="q06-c06--пізня-турбота-не-сушить-мокру-лавку"></a>
## Q06-C06 — Late care does not dry a wet bench

**Profile:** W0

**Check type:** precondition_boundary

**Pair:** Q06-C01

**Input difference:** Initial bench_wet=true; schedule and rain tape match S0. The prototype has no active-drying rule.

**Actions:** Install the umbrella during t0–2, inspect the place, and invite both at t5 as in C01; reading starts only after a valid agreement is accepted.

**Expected trace:** Cover prevents new wetting at t3, but wet=true remains → R2/R4 provide no dry seat for the NPCs → the t5 invitation to shared reading on the bench is not accepted under these prerequisites.

**Expected state:** wear=1 and umbrella/clamp occupied; wet state remains unchanged without a separate materially grounded action. The interface shows that cover exists but the seat is still wet.

**Forbidden:** Cover retroactively dries the surface; the renderer shows water while the evaluator accepts dry=true; the system adds a new drying rule without permission.

**Future evidence:** Initial moisture binding, exact completion/rain events, unchanged moisture, and the distinction between cover and usability.

**Inference limit:** Binary moisture is an authored W0 simplification. A future towel/drying mechanism needs its own cost, duration, and rule version.

<a id="q06-c07--особиста-допомога-замість-спільного-місця"></a>
## Q06-C07 — Personal help instead of a shared place

**Profile:** W0

**Check type:** alternative_action_policy

**Pair:** Q06-C02

**Input difference:** Initial state and rain match S0; instead of inviting both NPCs, the player offers Yaryna temporary use of the umbrella to read a note during t5–6.

**Actions:** t5 both parties accept the short loan → Yaryna opens the previously protected note under the umbrella → t6 returns the object → t7 continues her route.

**Expected trace:** Bench wet, no assembly → direct cover protects the note during reading → owner remains player, custody temporarily Yaryna → object returned.

**Expected state:** Specific personal assistance is completed, with one lawful transfer/return and no new place or municipal reward. Later acquaintance is possible but not guaranteed.

**Forbidden:** The loan turns into a gift; protected notes suddenly become evidence of a dry bench or a future large cascade.

**Future evidence:** Before t5 the note remained closed and dry; scope/time/owner/custody, accepted loan, return receipt, and action-local outcome.

**Inference limit:** This compares two different assistance plans; it does not estimate a single variable following intervention. An automatic score does not establish the alternative's social value.

<a id="q06-c08--збереження-посеред-двохвилинного-встановлення"></a>
## Q06-C08 — Saving halfway through a two-minute installation

**Profile:** W0

**Check type:** recovery_interleaving

**Pair:** Q06-C01

**Input difference:** Save at t1 after 60 seconds of the accepted assembly job; the world tick does not advance during the pause. After load: new session epoch, same history/job.

**Actions:** Resume variant: complete the remaining 60 seconds. Cancel variant: stop the job, release reserved objects, and choose another action.

**Expected trace:** At t1 cover=false, wear=0, two objects reserved, progress=60. Resume commit at t2 atomically sets cover, wear=1, job completed, and dedup receipt. Cancel leaves wear=0/cover=false, but the minute already spent is not refunded.

**Expected state:** Load does not issue objects or wear twice and does not execute a pending old model reply. Resume leads to C01's physical state in the same exogenous timeline; cancellation before rain at t3 leaves an exposed bench. Ownership is preserved.

**Forbidden:** A half-finished canopy already counts as complete; elapsed work is reset and weather silently changed; reserve duplicates an object; a completed effect lacks a job/resource/event receipt.

**Future evidence:** Checkpoint with progress/reservations/committed revision; new epoch; Q05 RC13/15 guards; resume/cancel disposition and one-effect identity.

**Inference limit:** This is recovery equivalence, separate from causal intervention. A real offline catch-up policy in another profile needs a different expected timeline.

<a id="q06-c09--підготовлений-локальний-план-запізнився"></a>
## Q06-C09 — A prepared local plan arrives too late

**Profile:** W0

**Check type:** prepared_plan_failure

**Pair:** Q06-C01

**Input difference:** P-late: inspect the place, install cover during t0–2, prepare a spoken invitation, and approach both NPCs only at t8. Initial NPC windows and weather are preserved.

**Actions:** Perform three steps of the fixed plan; at t8 try to gather both. Control: invite at t5 as in C01. If a human chooses an earlier time, that is another permitted action policy.

**Expected trace:** Cover works → a meeting opportunity exists until t7 → Yaryna continues her route at t7 → at t8 the simultaneous-reading plan lacks its second participant.

**Expected state:** The particular t8 plan's goal is unmet; time/wear spent remains, while the cover's benefit and other honest events persist. The next choice is available: individual conversation, a new time proposal, or exit.

**Forbidden:** The world also forces an adapted human plan to fail; it cancels Yaryna's earlier accepted promise to teach a lesson; a hidden jackpot reward disguises the unmet goal.

**Future evidence:** Goal/time and steps recorded in advance, NPC window and visible departure cue; invitation attempted at8; unchanged unrelated events, unmet-goal record.

**Inference limit:** W0 has a concrete multistep failure without a bridge, weeks, posters, or extra NPCs. It is not demonstrated that people will experience this failure as fair and interesting.

<a id="q06-c10--довгий-сезонний-задум-і-чужий-успішний-проєкт"></a>
## Q06-C10 — A long seasonal plan and someone else's successful project

**Profile:** extended_after_W0

**Check type:** long_horizon_input_sensitivity

**Pair:** separate seasonal snapshot; not S0

**Input difference:** Seasonal snapshot contains a two-week reading plan, six posters, canopy promises, background passengers, and a bridge with an already existing order/resources/completion date. The control changes only the bridge's readiness date.

**Actions:** Complete preparation → hold the evening event; compare routes and actual attendance, without inventing an audience to reward effort spent.

**Expected trace:** Bridge completed under the old plan → some NPCs choose the shorter route → the expected transfer-passenger audience does not arrive. In the control, the bridge is closed and the old route available, but free time/interest remain separate participation conditions.

**Expected state:** The regular-group hypothesis is not confirmed in the described failure branch. Materials and honest obligations remain; payment for a completed canopy is not cancelled because listeners are absent. Branch evidence separates route change from attendance decisions.

**Forbidden:** Bridge repair is added after reading the player's plan; a closed bridge guarantees attendance regardless of other needs; C10 becomes a W0 prerequisite.

**Future evidence:** Versioned seasonal snapshot, construction-order provenance predating the player plan, resource/route/attendance records, control intervention, and fulfilled/unfulfilled obligations.

**Inference limit:** This is an extended paper scenario. A new engine fixture first needs explicit seasonal rules/NPC policies; a route change alone does not establish the full effect on human experience.

<a id="автор-гравець-і-критерій-завершення"></a>
## Author, player, and completion criterion

Players do not see these tables. They see that the bench is wet, someone is in a hurry, the umbrella is occupied, and a proposed reading has not been accepted. An optional contextual line from Ilka by the covered bench might be: “Does it need a tram ticket too?” This creates no new fact, reward, or obligation to laugh; humans evaluate whether the humor fits and becomes repetitive.

The authoring report must separately show physical effect, social opportunity, accepted obligations, fulfillment of intent, and cost. An unusual action can be unnecessary yet interesting; an ordinary one can be useful. There is no universal metric “more cascade = a better game.”

Future W0 needs applicable C01–C09 on the declared profile, one actual human play session under AF-LW030, and a broader human pilot later; C10 is not a prerequisite. AF-LW002 permits the bench as an equivalent state/event fixture instead of a transport cargo, with the same mandatory fields. In W0, AF-LW011 crosses between physical state and simple NPC plans; it does not wait for a complete neighborhood economy.

Q06 closes as a **paper design pass**: initial states, rules, control differences, expected/forbidden outcomes, and required receipts are named. Player experience, engine conformance, performance, and Core improvement remain unmeasured. New evidence must change a rule/criterion or confidence; it is not required to confirm the attractive C01 story.
