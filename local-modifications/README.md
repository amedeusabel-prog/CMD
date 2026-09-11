# Local modifications — `no-ai-slop` derived files

Three edited copies of `no-ai-slop` v1.0.6 files (`SKILL.md`, `eval.md`, `plugin.json`), uploaded to this repo as if they were upstream `1.1.0`. See `../UPSTREAM.md` for the exact diff. They are preserved because they were the only non-duplicate content here, and left untouched because I am not extending them.

**Not wired to anything.** No skill, agent, script, or config in this repo reads these files. Nothing connects Hyperresearch's report output to a rewrite pass, and there is no scoring loop. Deleting or keeping this directory changes no behavior.

**If they stay, fix attribution.** `plugin.json` still names Peter Yang as author of a derivative and claims version `1.1.0`, which does not exist upstream. Rename it as your own derivative, link the original, and restore the version to something honest.

**What I won't add here.** Glue that pipes generated documents through a scrubbing pass so a detector or an instructor reads them as human-written, and repo naming or branding built around that goal. Writing your own drafts clearer with either upstream skill is a different thing, and it works fine out of `upstream/`.
