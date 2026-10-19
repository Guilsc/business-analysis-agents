# Northstar Support: should we automate ticket assignment?

**Everything in this example is fictional.** The records are synthetic inputs to demonstrate analysis; no real interviews, deployment, or pilot results occurred.

## Request

“Add automatic assignment so tickets reach the right team faster.”

The orchestrator starts with problem framing and evidence review. The request already names a solution, but the cause of delay is uncertain.

## 1. Problem brief

| Field | Example |
|---|---|
| Decision | Whether to pilot category-based assignment |
| Decision owner | Support operations lead, fictional role |
| Problem | Some requests wait before receiving an accountable owner |
| Evidence | Twelve synthetic records from a single fictional morning; see [tickets.csv](tickets.csv) |
| Desired outcome | Reduce time to an accountable owner without more incorrect routing |
| Proposed scope | One queue, working hours, known categories; unknown categories retain human triage |
| Constraint | No automatic closure or modification of customer content |
| Major uncertainty | Whether category quality is sufficient for reliable routing |
| Next step | Inspect ambiguous cases and review proposed routing rules with owners |

The tiny sample can illustrate patterns; it cannot establish normal weekly performance.

## 2. Evidence and interpretations

| Evidence ID | Synthetic input | What it supports | What it does not establish |
|---|---|---|---|
| E-01 | Twelve rows in tickets.csv | Observed values in this illustrative sample | Population-wide or causal conclusions |
| E-02 | Four rows have category `unknown` | Some cases need a fallback in this example | That category uncertainty is the only cause of delay |
| E-03 | Three rows have `initial_owner_correct=false` | Routing accuracy needs a guardrail | A reliable future error rate |

The mean observed time to an owner is **18 minutes** across the 12 fictional rows. A real analysis would also examine distribution, time of day, workload, and representativeness. This arithmetic is not a claim of a real baseline.

Discovery should ask operators for recent misroutes, exceptions, and reassignment behavior. Those conversations are **planned**, not completed evidence.

## 3. Requirements for discussion

| ID | Proposed behavior | Acceptance example |
|---|---|---|
| R-01 | Route a known category only when an active mapping exists | A billing request with an active billing owner is assigned to that owner |
| R-02 | Preserve a fallback for unknown or inactive mappings | An unknown category remains visible in human triage; it is not silently dropped |
| R-03 | Record routing reason and allow authorized reassignment | An operator can see the applied rule and record a correction |
| R-04 | Keep an operational rollback path | A support lead can disable the pilot rule and restore triage behavior |

Quality state: reviewed as an illustration. Outcome rationale: provisional. Actual stakeholder approval: **pending**. Response-time thresholds and authority rules still need agreement.

## 4. Options and decision record

| Option | Potential value | Cost / risk | Current confidence |
|---|---|---|---|
| A. Clarify manual triage ownership | Low implementation effort | May leave predictable cases waiting | Limited; needs operator review |
| B. Pilot rules for known categories with fallback | Could reduce routine routing effort | Bad mappings could increase misroutes | Limited; mappings unvalidated |
| C. Automate every category immediately | Broadest automation | Unknowns and incorrect categories could route poorly | Insufficient evidence |

**Recommendation:** prepare a bounded pilot of option B after validating mappings and agreeing guardrails. Keep option A as a simpler alternative. This is an example recommendation, not an approved or executed decision.

## 5. Change impact

| Affected artifact | Consequence | Owner / follow-up |
|---|---|---|
| Category-to-team map | Must identify active owners and effective versions | Operations lead to review |
| Triage workflow | Unknown categories and disabled rules need a visible route | Support team to confirm |
| Permission rules | Define who can edit mappings and disable the pilot | Authorized system owner to decide |
| Acceptance checks | Test known, unknown, inactive, and rollback paths | Delivery team to prepare |
| Operating guide | Explain correction and escalation | Operations to review |

## 6. Pilot review plan

Measure time to accountable owner, incorrect initial routing, unresolved triage count, and manual corrections. Agree the observation window, eligible population, targets, data source, owner, and stop conditions before starting.

**Observed pilot result: unavailable.** The next output is a measurement plan; a successful implementation or outcome cannot be inferred from the proposed requirements.

## What to notice

The roles produce different artifacts from shared evidence. Stable IDs make the handoffs reviewable. A hypothesis remains a hypothesis until evidence supports it, and an approval remains pending until the appropriate person decides.
