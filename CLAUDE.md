# Working in this repository

Tiny Dungeon – One More Room: a portrait pixel-art roguelite auto-battler for YouTube Playables,
built with Phaser 3, TypeScript and Vite. `docs/ARCHITECTURE.md` describes the layers,
`docs/BALANCE.md` the balance model and simulation, `PROGRESS.md` the status.

Checks: `npm run typecheck`, `npm test`, `npm run build`, and `npm run package` (validates the
YouTube Playables bundle rules). Headless play-throughs: `node tools/smoke.mjs` and
`node tools/ui-smoke.mjs` (slow).

The CC0 source art and sound packs live in the asset library of
https://github.com/felixarvid2/test (`assets/`). `python3 tools/build_assets.py` finds them through
`TD_ASSET_LIBRARY` or a checkout of that repo next to this one. The built files in `public/assets`
are committed.

## Who does what

Work is split by model; the subagents live in `.claude/agents/`.

| Work | Who | Model |
|---|---|---|
| Finding files and symbols, reading code, answering "where/how" | `Explore` | Haiku |
| Simple mechanical edits that are already fully specified (renames, strings, data values, the same small change in many places) | `mechanic` | Haiku |
| Regular coding: implementing a specified feature or fix, tests, planned refactors | `implementer` | Sonnet |
| Running a project's checks (tests, build, lint) and reporting only the verdict and failures | `verifier` | Haiku |
| Docs from a short summary: READMEs, notes, commit and PR bodies | `scribe` | Haiku |
| Shipping: commit, push, PR (merge only after the user approves) | `shipper` | Haiku |
| Architecture, trade-offs, hard bugs with an unknown cause, risk review | the main session, or `architect` when the main session runs a smaller model | Opus |

- Delegate search and reading to `Explore` instead of reading many files yourself, and pass it the
  question, not a file list to dump.
- Hand `implementer` a clear spec (what, where, how to verify); hand `mechanic` the exact change.
  Run independent pieces in parallel.
- Keep decisions here: choosing an approach, reviewing what subagents return, and anything that
  spans several systems. Check their results (the diff and the verifier's verdict) before committing.
- Hand `verifier` the project to check; hand `scribe` the facts. `shipper` merges a pull request
  only when told that the user approved that merge.
