// Reusable text-processing mechanics. No knowledge of *why* it's called,
// and no DOM access — this is the service layer, ported from
// sample-feature/service/text_service.py so the same bug class is visible
// in a live UI instead of only a CLI.

export function tokenize(text) {
  return text.trim().split(/\s+/).filter(Boolean);
}
