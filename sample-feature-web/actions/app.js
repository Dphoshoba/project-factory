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
