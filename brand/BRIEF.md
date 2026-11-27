# Brief for a new project's marks

This brief is for whoever draws the marks of a new project, by hand or with a drawing
agent. Hand it over whole. The files in this folder are the reference for every rule
below. Open them before drawing, and compare against them while drawing.

## Files of a project

A project has one name, one colour and one subject, and 18 files.

| Folder | Files |
| --- | --- |
| `icons/` | `<p>.svg`, `<p>-light.svg`, `<p>-mono.svg`, `<p>-icon.svg`, `<p>-icon-light.svg`, `<p>-icon-mono.svg`, `<p>-16.svg`, `<p>-16-light.svg`, `<p>-16-mono.svg` |
| `wordmarks/` | `<p>.svg`, `<p>-light.svg`, `<p>-mono.svg` |
| `lockups/` | `lockup-<p>.svg`, `lockup-<p>-light.svg`, `lockup-<p>-stacked.svg`, `lockup-<p>-stacked-light.svg`, `lockup-<p>-text.svg`, `lockup-<p>-text-light.svg` |

`<p>` is the name in lower case. A file without `-light` is for dark backgrounds. A `-mono`
file has one colour, `currentColor`. Add the project's row to the colour table in
`README.md`, and register it in [aiviarium/badges](https://github.com/aiviarium/badges) so its
badges draw.

## The colour

Each project has one hue that no other current project uses, as two tones. The tone on
dark is a light, saturated colour, and the tone on light is a darker shade that passes
4.5:1 on white. Pick a hue well away from the others in the table. Neighbours that differ
only a little in hue read as the same project at badge size.

The full icon uses four tones of the hue, plus a near-black eye with a near-white glint.
Derive the deep, shadow and highlight tones from the base the way the existing palettes
do. This table lists them, ordered deep, shadow, base, highlight.

| Project | On dark | On light |
| --- | --- | --- |
| Aiviarium | `#16573C` `#25875E` `#3FCF8E` `#A4EBCB` | `#09462F` `#0E6845` `#12875A` `#85D7B1` |
| Rookery | `#694B20` `#AD7B28` `#F2B33D` `#F9DA97` | `#483619` `#765018` `#9A6200` `#E6C079` |
| Crow | `#353564` `#5D5DB0` `#8F8FFA` `#C0C0FF` | `#29295F` `#383893` `#4A4AC8` `#A9A9F2` |
| Heron | `#204E68` `#327FA9` `#4FB6F2` `#A4DAFA` | `#123D55` `#125779` `#0B6FA8` `#8BC9EA` |
| Sparrow | `#495720` `#7B952E` `#B5D94C` `#DDEC9C` | `#34451A` `#486114` `#5B7A0E` `#BAD884` |

The eye is `#18181B` with a glint of `#EDEDEF` in both themes.

## The subject

Every mark is a bird or something of a bird's, such as its cage, its nest or its head.
Choose a subject that fits the name and has a silhouette unlike the others in the set.

- Draw the bird as a bird, with its real anatomy and proportions. Look at photographs of
  the species before drawing. The marks are stylised through flat shapes and few tones,
  never through geometric or abstract forms.
- Keep symbols of what the project does out of the bird. No brackets, arrows, digits,
  documents or circuit lines.
- A head or bust faces right, as Crow and Heron do. A whole bird in flight flies right.
- A bust ends in a broad base of breast and shoulder, so it stands on the bottom of the
  square instead of hanging from the top.

The traits that tell a species apart carry the mark. Get them right before anything else.
These came up while drawing the current set:

- A heron's head is a long, flat, low wedge whose crown runs straight into the bill. A
  round dome makes it a duck or a swan. The neck is thin under the head, widens toward
  the breast and folds into a sharp S. A smooth tube of even width reads as a swan, and a
  thread-thin neck reads as a seahorse.
- A sparrow is plump, with a large round head, a short thick beak and a short squared tail,
  and a long spiked tail turns it into a swallow. Keep the far wing hidden behind the body,
  because any part of it below the body reads as a dangling leg.
- A crest, a cap or an eye stripe follows the outline of the head exactly. A cap with a gap
  under it reads as a helmet.

## Sizes

| Tier | `viewBox` | Use | How it is drawn |
| --- | --- | --- | --- |
| Full | `0 0 128 128` | 64 px and up | All four tones and the eye. The subject fills the square with a margin of 6 to 10 units, and its visual weight is near the centre. |
| `-icon` | `0 0 48 48` | 24 to 48 px | The same bird with fewer shapes, in two or three tones, with the eye. Parts and gaps stay at least 2.5 units wide, so they hold at 24 px. |
| `-16` | `0 0 16 16` | 16 px, favicons | Pixel art. Only whole-pixel rectangles, written as runs like `M5 2h5v1H5Z`. The base colour and at most one highlight. |

Redraw each tier for its size instead of scaling the one above. At 16 px, build the bird
from its few defining traits. The heron at 16 px is a one-pixel bill across the top, a neck
two pixels wide and a block of breast. The sparrow is a round body block with a head, a
one-pixel beak and a wedge of wing above it.

The mono version of each tier is one path filled with `currentColor` and
`fill-rule="evenodd"`. The eye, the line between head and bill and the main feather lines
are cut out of it as further subpaths, as in `crow-mono.svg`. A mono icon without cuts is
a blob.

## The wordmark

The wordmark is the name set in Bricolage Grotesque (`fonts/bricolage-grotesque.woff2`) and
converted to outlines, one `<path>` per letter.

| Property | Value |
| --- | --- |
| Weight | 760 on the font's `wght` axis |
| Size | 100 units, so one font unit is 0.1 |
| Baseline | y 80 |
| `viewBox` | `0 0 <width> 105`, the width fitted to the word |
| Spacing | the font's own advance widths and kerning |

Many letters exist in a current wordmark already. Copy those outlines instead of
outlining them again, then outline only the letters that are missing, with the values
above, and check that they match their neighbours in weight and height.

Each letter in the coloured wordmarks has one facet, a straight cut rising from left to
right with a second tone above it. The cut starts at the letter's left edge at about 46%
of the letter's height from its top and rises at about 25 degrees, a slope of 0.4 to 0.6.
A letter that already exists keeps its cut. On dark, the letter is the base tone and the
facet the highlight tone. On light, the letter is the shadow tone and the facet the base
tone. The mono wordmark has no facets.

Keep `role="img"` and `aria-label="<Name>"` on the root `<svg>` of every wordmark and
lockup.

## The lockups

The lockups place the icon's `<svg>` and the wordmark's paths in one file. Nothing is
drawn new for them, so regenerate them whenever an icon or wordmark changes.

| Lockup | `viewBox` | Icon | Wordmark |
| --- | --- | --- | --- |
| Side by side | `0 0 <175 + wordmark width> 150` | the full icon at 150 by 150, at 0 0 | `translate(175 33)` |
| Stacked | `0 0 <wordmark width> 270` | the full icon at 150 by 150, centred: `x` is half of the width minus 150 | `translate(0 165)` |
| Text size (`-text`) | as side by side | the `-icon` tier at 150 by 150 | `translate(175 33)` |

The 33 puts the letters, rather than the wordmark's box, at the icon's centre, because the
box runs below the baseline.

## How to write the files

- Plain `<path>` elements, and `<ellipse>` or `<circle>` for an eye. Absolute coordinates,
  on whole or half units where it works.
- No strokes, gradients, filters, masks, clip paths, `<use>`, `<style>` or embedded images.
- A full icon stays around 2 KB. Size beyond that is usually shapes nobody can see.

## Check it before it's done

Render every file next to the existing ones and look at them together, on the dark and
the light background.

- Look at the full icons at 128 px and at 400 px, the `-icon` tier at 48 and 24 px, and the
  `-16` tier at its true 16 px, not only enlarged.
- Ask of each bird whether a stranger could tell the species, and whether it could be
  mistaken for another bird. Compare its proportions with a photograph.
- Look for shapes poking out of the silhouette, gaps between layers, an eye that touches
  the outline and tones out of order.
- Check that the new hue still reads as its own project next to the others in a lockup row.

When a drawing agent draws the marks, review its renders yourself, and send each round
back with concrete fixes in units and shapes, such as "deepen the head by 3 to 4 units
so the eye is inside it".
