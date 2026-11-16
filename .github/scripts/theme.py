"""Shared look for the profile README artwork (draw_assets.py) and the live stat
cards (stat_cards.py): flat near-black panels, hairline borders, quiet type, and
#00DFFF as the single accent. Plain SVG, almost no animation.

Everything is inlined (icons included): GitHub shows these files as images, and
an SVG loaded as an image can't fetch anything.
"""
import os
import re
from html import escape as esc

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, 'icons')

SANS = "'Inter', 'SF Pro Display', 'Segoe UI Variable Display', 'Segoe UI', system-ui, -apple-system, sans-serif"
MONO = "ui-monospace, 'SF Mono', 'Cascadia Mono', 'JetBrains Mono', Consolas, 'Liberation Mono', monospace"

BG = '#0a0e13'          # panel surface
LINE = '#1c2630'        # hairlines and borders
LINE_STRONG = '#2b3947'

CYAN = '#00DFFF'        # the only accent

TEXT = '#e6edf3'
TEXT_SOFT = '#8b98a5'
TEXT_DIM = '#566370'

W = 1000                # every full-width block is drawn 1000 wide
GAP = 12                # gap between blocks that sit side by side
MARGIN = 40             # inner margin of a full-width panel

REDUCED = '@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; } }'


def svg(w, h, label, body, style=''):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(label)}">\n<title>{esc(label)}</title>\n'
        f'<style>{style}\n{REDUCED}</style>\n{body}\n</svg>\n'
    )


def panel(w, h, rx=16, x=0, y=0):
    """A flat dark panel with a hairline border."""
    return f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="{BG}" stroke="{LINE}"/>'


def hairline(x1, x2, y):
    return f'<rect x="{x1}" y="{y}" width="{x2 - x1}" height="1" fill="{LINE}"/>'


def heading(text, kicker, x=MARGIN, y=46):
    """Section heading: a small mono kicker in the accent colour above the title."""
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="11.5" font-weight="600" letter-spacing="2" fill="{CYAN}">{esc(kicker.upper())}</text>'
            f'<text x="{x}" y="{y + 34}" font-family="{SANS}" font-size="26" font-weight="700" letter-spacing="-.3" fill="{TEXT}">{esc(text)}</text>')


def split(n, i, total=W, gap=GAP):
    """For n blocks shown side by side as n equal images: the width of each block and
    where block i starts inside its own image, so the gaps between blocks come out equal."""
    w = (total - gap * (n - 1)) / n
    return w, i * (w + gap) - i * total / n


def _read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def logo(key, x, y, size, color=TEXT_SOFT):
    """A single-colour tool logo (Simple Icons, icons/) at (x, y)."""
    src = _read(os.path.join(ICONS, f'{key}.svg'))
    inner = re.sub(r'^.*?<svg[^>]*>|</svg>\s*$', '', src, flags=re.S).replace('currentColor', color)
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}">{inner}</svg>'


def glyph(name, x, y, size, color, width=1.75):
    """A Lucide line icon (icons/ui/) in one colour."""
    src = _read(os.path.join(ICONS, 'ui', f'{name}.svg'))
    inner = re.sub(r'^.*?<svg[^>]*>|</svg>\s*$', '', src, flags=re.S)
    inner = inner.replace('currentColor', color).replace('stroke-width="2"', f'stroke-width="{width}"')
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24" overflow="visible">{inner}</svg>'
