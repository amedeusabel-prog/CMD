# CMD — vendored upstreams

This repository is not a project. Before 2026-09-11 it was a single `Add files via upload` commit of 49 files: **46 were byte-identical copies of two public MIT repositories**, and **3 were locally modified copies of files from one of them**. Nothing else was original. It is now deduplicated — the 45 pure copies are deleted, the real trees are vendored at pinned commits, and the 3 edits are quarantined with a diff record.

## Layout

```
CMD/
  README.md                     this file
  UPSTREAM.md                   provenance: tags, commit SHAs, what each file came from
  upstream/
    hyperresearch/              jordan-gibbs/hyperresearch @ v0.9.1 (183443a) — complete package
    no-ai-slop/                 petergyang/no-ai-slop @ main (000650b) — complete plugin
  local-modifications/
    no-ai-slop/                 SKILL.md, eval.md, plugin.json — edited copies, see below
```

## Using the vendored code

The loose `base.py` / `note.py` / `search.py` / `graph.py` / `output.py` / provider files that used to sit in this repo's root were excerpts of `hyperresearch/web/` and `hyperresearch/models/`. They imported `hyperresearch.core.config`, `hyperresearch.web.base`, and `hyperresearch.cli` — modules that were not in this repo — so they were inert. Against the vendored tree every internal import resolves:

```sh
pip install -e upstream/hyperresearch          # pulls pydantic, typer, Crawl4AI, pymupdf, httpx
python -m hyperresearch --help
```

`pydantic` and friends are declared in `upstream/hyperresearch/pyproject.toml`; they are the only reason a bare `python -c "import hyperresearch.models.search"` fails before install. The CLI workflow files (`ci.yml`, `publish.yml`) also lived in this repo's root, where GitHub Actions ignores them; the working copies are at `upstream/hyperresearch/.github/workflows/`.

## Licenses

Both vendored trees are MIT and stay intact, license texts included:

- `upstream/hyperresearch/LICENSE` — Copyright (c) 2026 Jordan Gibbs
- `upstream/no-ai-slop/LICENSE` — Copyright (c) 2026 Peter Yang

Neither project endorses this repo, and nothing here has been contributed upstream.

## Scope of what is here

`upstream/` is someone else's released software, mirrored so this repo stops being a broken skeleton. `local-modifications/` holds the only original content in the repo — an added "Statistical fingerprints to fix" section and its matching eval checklist, which do not exist in `no-ai-slop` v1.0.6 (grep it: zero hits for *perplexity*, *burstiness*, *fingerprint*, *detector* upstream). They are kept unedited and unwired: no script, skill, or agent here invokes them, and there is no chain from Hyperresearch's report output into them.

Two things I will not build on top of this: a rename or rebrand of the repo around evading AI detection, and any glue, prompt, or loop whose job is getting AI-written text past a detector or an instructor's assumption of human authorship. The writing-editing and research tooling above is usable as the authors shipped it. For the specific case of text that is graded as your own, the constraint is not the detector's score — it is whether the writing is honestly attributable to you.
