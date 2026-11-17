# .github

Defaults for every repository in the aiviarium organisation.

| Path | What it does |
| --- | --- |
| `profile/README.md` | The organisation's page on GitHub |
| `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` | Used by a repository that has no file of that name |
| `.github/ISSUE_TEMPLATE/` | The issue forms of a repository that has no `ISSUE_TEMPLATE` folder |
| `.github/PULL_REQUEST_TEMPLATE.md` | The same for pull requests |
| `.vale/`, `.vale.ini` | The prose rules every repository of the organisation uses, checked here by CI |
| `labels/` | The shared labels, the script that applies them and the ruleset for `main` |

A file in a repository replaces the one here. Issue forms are all or nothing: a
repository with any form of its own gets none of these.

## Issue types

The forms set an issue type. The organisation has Bug, Feature, Task,
Improvement, Integration, Documentation, Question and Tracking. Types are set
up under the organisation's settings.

## Labels

```sh
labels/sync.sh aiviarium/hatchery          # add and update the shared labels
labels/sync.sh aiviarium/hatchery --prune  # also drop GitHub's defaults that the types replace
```

`labels/labels.json` is the list. A repository adds its own `area: …` labels
beside them.

## Ruleset

`labels/ruleset-main.json` is the ruleset for the default branch. The branch
can't be deleted or force-pushed. Changes go through a pull request, and the
`ci` check has to pass.
Apply it to a repository with:

```sh
gh api -X POST repos/aiviarium/REPO/rulesets --input labels/ruleset-main.json
```
