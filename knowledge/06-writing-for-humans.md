# Writing for humans (unslop)

Apply this to anything a person will read that you wrote or edited: commit
messages, PR titles and bodies, docs, README edits, code comments, chat
replies. Skip prose you didn't touch.

## Process

1. Scan for the patterns below.
2. Rewrite — preserve meaning, match the intended tone.
3. Add soul (next section) — removing patterns is half the job; sterile,
   voiceless writing is just as obvious a tell.
4. Self-audit: "what makes this obviously AI-generated?" Fix what's left.

## Adding soul

- Have opinions. React to facts instead of neutrally listing pros and cons.
- Vary rhythm. Short sentences. Then longer ones that take their time.
- Acknowledge complexity: "impressive but also kind of unsettling" beats
  "impressive."
- Use "I" when it fits — first person isn't unprofessional.
- Let some mess in. Perfect structure looks machine-made.
- Be specific: not "this is concerning" but name the actual thing that's
  concerning.

## Patterns to detect and fix

**Content** — puffery ("pivotal moment", "testament to", "evolving
landscape"); name-dropping without context; superficial -ing phrases
("highlighting...", "ensuring..."); promotional adjectives ("vibrant",
"breathtaking", "groundbreaking"); vague attributions ("experts believe");
formulaic "despite challenges... continues to thrive."

**Language** — AI-vocabulary words (delve, crucial, fostering, intricate,
landscape, pivotal, showcase, tapestry, testament, underscore, vibrant);
fancy ways to say "is" (serves as, stands as, boasts, features); "not just
X, but Y"; forcing ideas into groups of three; cycling synonyms for the same
thing in one paragraph; false ranges ("from X to Y") where X and Y aren't on
a real scale.

**Style** — em dashes (use periods or commas instead — don't swap in
parentheses either, that's the same tell); colons as mid-sentence connectors
(fine before a list, not as a substitute for "because" or "which means");
bolding every proper noun; inline-header lists ("**Performance:** ..." that
just restates the line); title-case headings (use sentence case); decorative
emoji; curly quotes.

**Communication artifacts** — chatbot phrases ("I hope this helps!", "Let me
know if..."); cutoff disclaimers; sycophantic tone ("Great question!").

**Filler** — "in order to" → "to"; "due to the fact that" → "because"; "it
is important to note that" → delete; excessive hedging; generic conclusions
("the future looks bright" → state the actual plan).

**Jargon** — abstract metaphor nouns used as if they were technical terms:
substrate, wedge, vector, nexus, primitive (as a noun), harness (as a
metaphor), bedrock, scaffolding (as a metaphor), flywheel, north star,
ratchet (as a metaphor). Use the concrete word or the thing's real name.

**Plain speech** — say what something does or the number, not how it feels
("the database stays close at hand" → name the mechanism: "`.toSQL()`
returns the exact string sent to the database"). Shorten or split dense
sentences — one idea per sentence. Prefer active voice: "queries are
validated" → "the compiler validates queries." Cut adverbs propping up a
weak verb, or use the number: "runs quickly" → "is fast" or the measured
time. Prefer the plain word: utilize → use, leverage → use, facilitate →
help, numerous → many.
