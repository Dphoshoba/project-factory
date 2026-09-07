# Build: service-layer architecture

**Two-layer separation:** actions orchestrate domain rules (the "why/when"),
while a service layer centralizes reusable operational mechanics (the
"how"). This prevents duplicated code, inconsistent behavior, and bugs fixed
in one path but not others.

## When to use it

- Multiple callers need the same low-level operation (sending email, calling
  an external API, running a command, parsing a file format).
- You're copy-pasting operational logic between action files.
- A bug fix in one workflow doesn't propagate to others doing the same
  thing.
- You're adding a feature that shares mechanics with an existing one.

Don't use it when the logic is truly domain-specific and has exactly one
caller — that's premature abstraction, not architecture.

## Core pattern

```
Orchestration layer (actions)          Service layer (shared mechanics)
├── owns business rules                ├── owns reusable operations
├── owns state transitions             ├── owns provider/SDK interactions
├── owns auth/ownership checks         ├── owns command execution details
├── owns failure classification        ├── owns health checks / readiness
├── owns retries / user-facing errors  └── returns structured results
└── calls service functions
```

Rule of thumb: "what this product flow means" stays in actions; "how to do
this operation reliably" moves to the service layer.

## Quick reference

| Design principle | Do | Don't |
|---|---|---|
| API shape | Composable capability functions | One giant "do everything" method |
| Inputs/outputs | Explicit params, structured returns | Hidden global state, reaching into the DB |
| Migration | Extract one block, replace one caller, verify, then migrate the rest | Refactor everything at once |
| Domain logic | Keep auth, policy, error classification in actions | Let the service mutate domain state directly |
| Extraction trigger | Logic repeated across 2+ callers | Logic used once (over-abstraction) |

## Designing service functions

Design as capability blocks, not monoliths — each caller picks what it
needs:

```
createManagedSandbox(...)
prepareRepo(...)
detectPackageManager(...)
installDependencies(...)
```

Each function should:

- Accept all required data as explicit parameters.
- Return structured outputs (e.g. `{ ready, previewUrl, proxyPort }`), not a
  bare boolean or a thrown exception as the only signal.
- Never reach into a database or other shared state directly.
- Make failure explicit — a structured result, not a swallowed error.

## Migration checklist

1. Write the flow in action code first, so the behavior is clear.
2. Mark the operational chunks that repeat across callers.
3. Extract only the repeated, non-domain chunks to the service layer.
4. Replace one caller, verify it still works, then migrate the rest.
5. Keep domain policy in actions: auth, status transitions, error
   classification.
6. Run the repo's verification (typecheck, lint, tests) and confirm every
   flow that used the old code still works.

## Anti-patterns

| Anti-pattern | Problem |
|---|---|
| God service | One huge function hides all control flow |
| Leaky service | Service mutates the database/domain state directly |
| Inconsistent API | Each function uses different argument styles and error semantics |
| Over-abstraction | Extracting logic that only one caller ever uses |

## Example

```
# service layer — shared mechanics, no knowledge of *why* it's called
def send_welcome_email(to: str, name: str) -> None:
    html = f"<h1>Welcome {name}</h1>"
    email_provider.send(to, "Welcome", html)

# action — owns WHEN to send (business rule)
if user.marketing_opt_in:
    send_welcome_email(to=user.email, name=user.name)

# a different action, same mechanic
send_welcome_email(to=invitee.email, name=invitee.name)
```

## Mental model

New feature → write it in an action first → do you see repeated ops? →
extract to a service. No repetition? → leave it in the action.

Your architecture in one sentence: actions orchestrate domain rules, the
service layer centralizes reusable operational mechanics behind a
composable, explicit-input API.
