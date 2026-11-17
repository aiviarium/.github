# Contributing

Thanks for wanting to help. This page says how a change gets from an idea to
`main` in the projects of this organisation. A repository with a
`CONTRIBUTING.md` of its own follows that one, which also says what the
project is trying to be. Coding agents should read the repository's
`AGENTS.md` as well.

## Before you write code

**Open an issue first.** This goes for features, for changes in behaviour and
for anything larger than an obvious fix. Say what you want to do and why. The
scope should be small enough to review in one sitting. Several small issues are
better than one large one.

Choose the form that fits:

| Form | For |
| --- | --- |
| Feature | Something the project can't do at all yet |
| Improvement | Something it does already, but could do more easily, faster or more clearly |
| Integration | An agent, tool, provider or service |

You don't have to wait for an answer before you start. Once the issue is
there, you can begin on the pull request straight away if you like. The order
is what matters, since the issue is where we find out whether the change
belongs in the project at all, and it's cheaper to find that out before the
work is done.

A few rules follow from that:

- A feature pull request with no issue behind it will be closed.
- Opening the pull request first and then filing an issue that summarises it
  doesn't count. The issue comes first.
- A first contribution always starts with an issue. Pull requests from
  accounts with no earlier issues or history in the project will be closed,
  however good the code is.

Typo fixes, broken links and small documentation corrections can go straight
to a pull request.

## How issues are handled

An issue's type, such as Bug, Feature or Improvement, says what kind it is.
Labels say the rest:

| Labels | Say |
| --- | --- |
| `area: …` | The part of the project it's about. Each repository has its own |
| `needs triage`, `needs info`, `accepted`, `blocked` | Where the issue stands |
| `duplicate`, `out of scope`, `plugin candidate` | Why it was closed |

A new issue starts with `needs triage`. When it belongs in the project, it gets
`accepted`, and a pull request is welcome from then on. An idea that would
work better as a plugin is closed with `plugin candidate`, and one that
doesn't fit what the project is with `out of scope`.

## Using language models

Using a model to help is fine, and welcome. Most of this code was written with
one. What we ask:

- **You review it.** Read every line of a change before you submit it, and be
  able to explain it. The maintainers review it as well, but that's the second
  review, and yours comes first.
- **Use a capable model.** Weak models produce code that looks right and
  isn't, and reviewing that costs more than writing it would have.
- **No unattended submissions.** Issues and pull requests opened by an agent
  with nobody reading them will be closed.
- **Prose passes the style rules.** Where a repository has rules for its
  documentation, they have to pass.

Issues and commit messages may be written with a model too. We'd ask you to
write the core of an issue yourself first, even if a model tidies it
afterwards. A short account in your own words tells us more than a formatted page.

## Making the change

Each repository's README or `AGENTS.md` says how to build it and run its
checks. A pull request is ready when:

- The repository's checks pass.
- Behaviour that changed has a test.
- Documentation is updated in the same pull request.
- Commits follow [Conventional Commits](https://www.conventionalcommits.org/),
  with a short subject that says what changed.
- The pull request links its issue and stays within it. Leave unrelated
  cleanups for a pull request of their own.

## Reporting bugs

Open an issue with what you ran, what you expected and what happened. The
version helps. Take addresses, tokens and passwords out before you paste
anything.

Don't report security problems in an issue. [SECURITY.md](SECURITY.md) says
where they go.

## Licence

Each repository states its licence. By contributing you agree that your
contribution is licensed the same way, with no further terms.
