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
| `tools/` | `shield.sh` prints the badge settings of a project |

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

Badges come from [shields.io](https://shields.io), so they can show a release,
the state of CI or any other value it offers. A project's badge has its icon
on a dark label and the value on the project's colour. `tools/shield.sh`
prints the query string that does this:

```bash
brand/tools/shield.sh hatchery
```

Append what it prints to the address of a shields.io badge:

```markdown
![Release](https://img.shields.io/github/v/release/aiviarium/hatchery?style=flat&labelColor=18181B&color=E879F9&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OCA0OCI%2BPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEgLTEpIHNjYWxlKC4zOSkiIGZpbGw9IiNFODc5RjkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTU5IDEyIEM4MCA5IDEwMyA0OCAxMDUgNzUgQzEwNyA5OSA5MSAxMTQgNjggMTE2IEM0MyAxMTggMjQgMTA1IDIyIDgyIEMyMCA1NSAzOCAxNSA1OSAxMloiLz48cGF0aCBmaWxsPSIjNjczNTcxIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik03IDI5TDE1IDI0TDE5IDI1TDI0IDE5TDI4IDIxTDMyIDE1TDM5IDE2TDMzIDE5TDMwIDI1TDI1IDIzTDIwIDI5TDE1IDI3WiIvPjwvc3ZnPg%3D%3D)
![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-x?style=flat&labelColor=18181B&color=E879F9&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OCA0OCI%2BPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEgLTEpIHNjYWxlKC4zOSkiIGZpbGw9IiNFODc5RjkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTU5IDEyIEM4MCA5IDEwMyA0OCAxMDUgNzUgQzEwNyA5OSA5MSAxMTQgNjggMTE2IEM0MyAxMTggMjQgMTA1IDIyIDgyIEMyMCA1NSAzOCAxNSA1OSAxMloiLz48cGF0aCBmaWxsPSIjNjczNTcxIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik03IDI5TDE1IDI0TDE5IDI1TDI0IDE5TDI4IDIxTDMyIDE1TDM5IDE2TDMzIDE5TDMwIDI1TDI1IDIzTDIwIDI5TDE1IDI3WiIvPjwvc3ZnPg%3D%3D)
```

The icon is encoded in the address. Run the script again after a change to an
icon.
