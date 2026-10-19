---
name: ba-change-impact
description: "Assess a proposed change across requirements, rules, interfaces, roles, tests, and rollout. Use for scope changes, dependency analysis, and decision tracking."
---
# Change impact and traceability

## Establish the baseline
Identify the proposed change, its reason, the current artifact versions, and who can decide. If there is no stable baseline, first describe what is known and which parts are still evolving.

## Follow consequences
1. Identify affected outcomes, requirements, rules, data, interfaces, users, operations, tests, and releases. Follow meaningful relationships rather than linking every artifact to every other one.
2. Distinguish direct effects from plausible downstream effects. Record the evidence or dependency behind each link.
3. Compare accepting, modifying, delaying, or declining the proposal. Explain impacts on value, effort, timing, risk, and other stakeholders.
4. Include transition needs: migration, training, communication, fallback, and temporary coexistence where applicable.
5. Recommend a disposition with uncertainty and questions for the decision owner. Do not change approval state without a recorded authorized decision.
6. After a decision, update the agreed artifacts and relationships within the authorized write scope. Preserve the prior rationale and version history.

## Traceability at useful depth
Choose links that answer coverage or change questions: a need motivates a requirement, a rule constrains behavior, a design implements it, and a check assesses fulfillment. Name the relationship and direction. Delete stale links only after assessing why they existed.

## Deliver
Return a change summary, affected-artifact list with versions, consequence assessment, recommended action, actual decision state, and update plan. Use [the change note](templates/change-note.md). Highlight unresolved approval or missing evidence rather than burying it in the impact narrative.

## Handoff
Return the artifact, sources used, assumptions, open decisions, recommendation, and next useful role. Use only available tools and authorized actions. Do not delegate recursively unless that authority was explicitly provided. Unavailable access limits evidence; it does not justify inventing it.
