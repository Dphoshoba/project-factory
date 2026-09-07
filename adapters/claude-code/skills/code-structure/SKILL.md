---
name: code-structure
description: Use when multiple workflows duplicate the same operational logic, when deciding what belongs in actions vs a shared service layer, or when adding a feature that shares mechanics with an existing one.
---

# Service layer architecture

Follow `knowledge/02-service-layer-architecture.md` at the root of this
factory. Summary: actions own the "why/when" (business rules, auth, state
transitions); a service layer owns the "how" (reusable operational
mechanics) behind explicit-input, structured-return functions. Extract to
the service layer only when logic repeats across two or more callers —
never for a single caller.
