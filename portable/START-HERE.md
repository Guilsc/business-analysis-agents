# Use in a text-only assistant

Supply this instruction and the relevant files from `portable/roles/` through your host's supported file, instructions, or knowledge interface.

```text
Help me achieve this goal: [goal and context].
Use the supplied Business Analysis Agents role guides. Start with the
orchestrator for a multi-step request, or apply one relevant role directly.
Work within the supplied scope and available evidence. Keep observations,
interpretations, assumptions, recommendations, and decisions distinguishable.
If authorized delegation is available, use focused specialist briefs.
Otherwise apply roles sequentially and say that is what you did.
Return a useful artifact, evidence, unresolved questions, and next action.
```

Each portable role embeds its templates and local references. It does not embed other roles or the optional diagram-design skill. Supply those separately when needed. If a document cannot be retrieved, ask for the relevant content rather than claiming to have read it.

Tools, accounts, filesystem access, and separate agents come from the host. A path or command in a document does not create those capabilities. Without a renderer, diagram output can be source with visual verification pending.
