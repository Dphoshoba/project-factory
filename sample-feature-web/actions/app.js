// Action: orchestrates the live word-count UI. Owns wiring the DOM to the
// service, not the tokenizing mechanics.

import { tokenize } from "../service/word_count.js";

function updateCount() {
  const input = document.getElementById("input");
  const count = document.getElementById("count");
  const words = tokenize(input.value);
  const label = words.length === 1 ? "word" : "words";
  count.textContent = `${words.length} ${label}`;
}

document.getElementById("input").addEventListener("input", updateCount);
updateCount();

// Test-only: automation (e.g. the tier-3 evidence harness) needs reliable
// keyboard focus without pixel coordinates. Real visitors get standard
// browser behavior -- this only fires when explicitly requested via the URL,
// so screen readers aren't disrupted by an unexpected focus jump on load.
const params = new URLSearchParams(location.search);
if (params.get("autofocus") === "1") {
  document.getElementById("input").focus();

  // A repeated test run can leave earlier "Word Count" tabs open. A plain
  // title match is then ambiguous -- an OS-level actuator (or anything else
  // matching by window/tab title) can land on a stale tab instead of this
  // one. A unique per-run title removes that ambiguity entirely.
  const runId = params.get("runid");
  if (runId) {
    document.title = `Word Count [${runId}]`;
  }
}
