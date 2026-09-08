// Action: orchestrates the live word-count UI. Owns wiring the DOM to the
// service, not the tokenizing mechanics.

import { tokenize } from "../service/word_count.js";

function updateCount() {
  const input = document.getElementById("input");
  const count = document.getElementById("count");
  const words = tokenize(input.value);
  count.textContent = `${words.length} words`;
}

document.getElementById("input").addEventListener("input", updateCount);
updateCount();
