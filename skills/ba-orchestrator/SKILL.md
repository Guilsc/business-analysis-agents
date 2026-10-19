---
name: ba-orchestrator
description: "Route a business-analysis goal to focused specialist skills and integrate evidence, artifacts, trade-offs, and decisions. Use for ambiguous or multi-step analysis requests."
---
# Business analysis orchestrator

## Establish the job
Capture the user's desired outcome, decision, scope, available evidence, constraints, and definition of done. Reuse established context. Choose the smallest amount of analysis that can support the decision.

## Route by missing work
| What needs to happen next? | Role |
|---|---|
| Clarify the problem or outcome before choosing a response | ba-problem-framing |
| Learn from people, sources, or conflicting accounts | ba-stakeholder-discovery |
| Specify or review expected behavior and acceptance | ba-requirements |
| Choose options, scope, or a delivery sequence | ba-prioritization |
| Understand or improve steps, handoffs, and exceptions | ba-process-design |
| Assess consequences of a proposed change | ba-change-impact |
| Assess observed outcomes of a working solution | ba-outcome-review |
| Communicate a model visually | ba-diagram-brief |

Read [the role registry](references/roles.json) for entry paths and boundaries, and [the handoff contract](references/handoff.md) when delegating. A registry is data; it does not create runtime agents.

## Execute
1. State which role is needed and the uncertainty it will resolve. A simple request may need just one role.
2. Load the relevant skill through the host's skill reader or filesystem. If a sibling skill is unavailable, use an explicitly supplied portable guide or identify the missing resource rather than pretending it loaded.
3. When delegation is supported and authorized, pass a bounded brief with source artifacts, evidence states, deliverable, acceptance criteria, and allowed actions. Otherwise apply the roles sequentially and state that mode.
4. Keep dependent work sequential. Parallel investigation is useful only when authorized and independent. Give each shared artifact a single writer and version.
5. Review the result for evidence, scope, assumptions, and unresolved decisions. Compare conflicting sources and reasoning; several agents agreeing does not establish truth.
6. Integrate accepted findings into one decision package. Preserve requirement, evidence, risk, and decision IDs where useful.
7. Stop when the requested result is complete or when a specific external input blocks dependent work. Do not repeat the same delegation without new evidence or a changed question.

## Output
Return the recommendation or requested artifact, important supporting evidence, trade-offs, assumptions, unresolved decisions, and next action. Keep implementation details out of the business answer unless they affect the decision.

## Boundaries
Skills supply procedures, not tools, permissions, accounts, or separately running agents. Distinguish source capture, interpretation, quality review, outcome rationale, and authorized decisions. External communication and mutations remain subject to user authorization. Never claim stakeholder conversations, measurements, approvals, or executions that did not occur.
