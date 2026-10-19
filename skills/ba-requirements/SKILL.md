---
name: ba-requirements
description: "Write and review implementable requirements, rules, scenarios, and acceptance criteria. Use when an agreed need must become clear behavior and quality expectations."
---
# Requirements and acceptance

## Establish the boundary
Identify the intended outcome, actors, relevant systems/processes, and the next user of the specification. Choose a representation that fits the work: a concise rule, scenario, table, story, or model. Do not require every representation for every request.

## Specify the behavior
1. Assign a stable identifier and link the item to its source and intended outcome.
2. State who or what acts, under which conditions, the expected behavior, and the resulting state. Include important failure paths, permissions, and boundary cases.
3. Separate policy/business rules from interface choices. Identify external dependencies and assumptions instead of silently making them requirements.
4. Specify relevant quality expectations with workload, population, operating conditions, and a way to assess them. Ask for missing thresholds rather than inventing committed targets.
5. Write observable acceptance examples. Given/When/Then is useful for behavior; other forms are fine when clearer. Include at least one consequential exception where it exists.
6. Review wording for ambiguity, contradictions, feasibility concerns, and enough detail for the next step. Then separately check whether the requested behavior supports the intended outcome.

## Distinguish review states
Clear wording does not establish business value. Business value does not establish stakeholder authorization. Track quality review, outcome rationale, and approval separately. Record actual decisions and who made them; draft recommendations remain drafts.

## Deliver
Use [the requirement card](templates/requirement-card.md). For larger sets, include a compact coverage table connecting outcomes, requirement IDs, acceptance examples, and open issues. Keep the set coherent rather than duplicating the same rule across documents.

## Review
Could two implementers reasonably interpret the behavior differently? Could a tester determine whether the agreed behavior occurred? Does satisfying the item plausibly help the intended stakeholder? Surface unresolved answers with a recommended owner.

## Handoff
Return the artifact, sources used, assumptions, open decisions, recommendation, and next useful role. Use only available tools and authorized actions. Do not delegate recursively unless that authority was explicitly provided. Unavailable access limits evidence; it does not justify inventing it.
