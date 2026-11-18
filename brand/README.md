# Brand

The icons, wordmarks, lockups and badges of the organisation and its projects.
A project has one colour, which its icon, its wordmark and its badges use.

| Project | Colour on dark | Colour on light |
| --- | --- | --- |
| Aiviarium | `#3FCF8E` | `#12875A` |
| Rookery | `#F2B33D` | `#9A6200` |
| Parrot | `#FF6369` | `#D1343B` |
| Crow | `#8F8FFA` | `#4A4AC8` |
| Hatchery | `#E879F9` | `#A21CAF` |

## What is here

| Folder | Holds |
| --- | --- |
| `icons/` | Each icon in full detail, reduced for 24 to 48 px (`-icon`) and for 16 px (`-16`), each for dark and light (`-light`) backgrounds and in one colour (`-mono`) |
| `wordmarks/` | Each name as outlines, for dark and light backgrounds and in one colour |
| `lockups/` | Icon and wordmark together, side by side, stacked, and at text size (`-text`) with the reduced icon |
| `fonts/` | Bricolage Grotesque, the typeface of the wordmarks, with its license |

## A name as an image

GitHub shows a README in its own typeface. Where a project's name should look
like its wordmark, use the lockup at text size. This one follows the reader's
theme and links to the repository:

```html
<a href="https://github.com/aiviarium/hatchery"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/aiviarium/.github/main/brand/lockups/lockup-hatchery-text.svg">
  <img src="https://raw.githubusercontent.com/aiviarium/.github/main/brand/lockups/lockup-hatchery-text-light.svg" alt="Hatchery" height="34">
</picture></a>
```

Use a height of 34 for a name in running text and 56 for the heading of a page.

## Badges

Badges come from [aiviarium/badges](https://github.com/aiviarium/badges). It draws a badge with the project's icon and colour, and takes the label and value from any shields.io badge:

```markdown
![Release](https://aiviarium-badges.helight.workers.dev/hatchery/github/v/release/aiviarium/hatchery)
![State](https://aiviarium-badges.helight.workers.dev/hatchery/badge/state-in%20development-x)
```

`/hatchery` alone gives the name, and `/hatchery?facet` gives it as the wordmark. The README of that repository lists the rest.
