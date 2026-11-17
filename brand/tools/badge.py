#!/usr/bin/env python3
"""Draw a badge in a project's colour.

  badge.py PROJECT LABEL [VALUE] [--value-colour PROJECT] [-o FILE]

PROJECT is aiviarium, rookery, parrot, crow or hatchery. The badge shows the
project's icon and LABEL on a dark field and, when VALUE is given, VALUE on the
project's colour, or on the colour of the project --value-colour names. Text is drawn as outlines, so the badge looks the same
wherever it is shown. Needs fonttools and brotli.
"""
import argparse
import re
import sys
from functools import lru_cache
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

BRAND = Path(__file__).resolve().parents[1]

# The base colour of each project on a dark background.
COLOURS = {
    "aiviarium": "#3FCF8E",
    "rookery": "#F2B33D",
    "parrot": "#FF6369",
    "crow": "#8F8FFA",
    "hatchery": "#E879F9",
}
FIELD = "#18181B"  # behind the label
LINE = "#2A2A30"  # the outline, which keeps the badge visible on a dark page
LABEL = "#EDEDEF"
VALUE = "#0A0A0B"

HEIGHT = 22
RADIUS = 5
PAD = 7
ICON = 14
SIZE = 11.5
BASELINE = 15.2


@lru_cache(None)
def face(weight):
    font = TTFont(BRAND / "fonts" / "inter.woff2")
    return instantiateVariableFont(font, {"wght": weight})


def outline(text, weight, x, colour):
    """The text as one path starting at x, and the x where it ends."""
    font = face(weight)
    scale = SIZE / font["head"].unitsPerEm
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for char in text:
        name = cmap.get(ord(char), ".notdef")
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, BASELINE)))
        x += font["hmtx"][name][0] * scale
    return f'<path fill="{colour}" d="{pen.getCommands()}"/>', x


def icon(project):
    source = (BRAND / "icons" / f"{project}-icon.svg").read_text()
    body = source.split(">", 1)[1].rsplit("</svg>", 1)[0]
    box = re.search(r'viewBox="([^"]+)"', source).group(1)
    y = (HEIGHT - ICON) / 2
    return f'<svg x="{PAD - 1}" y="{y:g}" width="{ICON}" height="{ICON}" viewBox="{box}">{body}</svg>'


def badge(project, label, value=None, value_colour=None):
    colour = COLOURS[project]
    fill = COLOURS[value_colour or project]
    x = PAD - 1 + ICON + 5
    label_path, x = outline(label, 600 if value is None else 500, x, colour if value is None else LABEL)
    split = x + PAD
    parts = [f'<rect width="{split:.1f}" height="{HEIGHT}" fill="{FIELD}"/>', icon(project), label_path]
    width = split
    if value is not None:
        value_path, end = outline(value, 650, split + PAD, VALUE)
        width = end + PAD
        parts.insert(1, f'<rect x="{split:.1f}" width="{width - split:.1f}" height="{HEIGHT}" fill="{fill}"/>')
        parts.append(value_path)
    width = round(width + 0.49)
    title = label if value is None else f"{label}: {value}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}" '
        f'width="{width}" height="{HEIGHT}" viewBox="0 0 {width} {HEIGHT}">'
        f"<title>{title}</title>"
        f'<clipPath id="r"><rect width="{width}" height="{HEIGHT}" rx="{RADIUS}"/></clipPath>'
        f'<g clip-path="url(#r)">{"".join(parts)}</g>'
        f'<rect x=".5" y=".5" width="{width - 1}" height="{HEIGHT - 1}" rx="{RADIUS - .5}" fill="none" stroke="{LINE}"/>'
        "</svg>\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("project", choices=sorted(COLOURS))
    parser.add_argument("label")
    parser.add_argument("value", nargs="?")
    parser.add_argument("--value-colour", choices=sorted(COLOURS), metavar="PROJECT")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    svg = badge(args.project, args.label, args.value, args.value_colour)
    if args.output:
        args.output.write_text(svg)
    else:
        sys.stdout.write(svg)


if __name__ == "__main__":
    main()
