"""Draws the README's static artwork into ../../assets/ in the minimal dark theme (theme.py).

Usage: python draw_assets.py
Edit the CONTENT block below, then re-run. Anything marked TODO is a placeholder.
"""
import os

from theme import (BG, CYAN, LINE, LINE_STRONG, MARGIN, MONO, SANS, TEXT, TEXT_DIM, TEXT_SOFT, W, esc, glyph, hairline, heading,
                   logo, panel, split, svg)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets')

# ───────────────────────────── CONTENT ─────────────────────────────
NAME = 'Sashika Dinith'
KICKER = 'AI & Data Science Student'
TAGLINE = 'I teach machines to find patterns, then build smart systems that act on them.'
LOCATION = 'Sri Lanka'
SCHOOL = 'Robert Gordon University'
TYPED = 'model.fit(curiosity, epochs=∞)'          # the line that types itself in the hero

ABOUT = [  # (glyph, label, text)
    ('graduation-cap', 'Studying at RGU', 'BSc (Hons) Artificial Intelligence & Data Science'),
    ('flame', 'Currently', 'Building an ML model to predict student dropout'),
    ('brain-circuit', 'Interested in', 'AI engineering, data analytics & smart systems'),
    ('sparkles', 'Learning', 'Swift and iOS development, from the ground up'),
]

PROJECTS = [  # (file, name, meta line, status, description lines, tags, public)
    ('dropout-predictor', 'Student Dropout Predictor', 'Team research · 2026 – present', 'Ongoing',
     ['Uses machine learning to predict student dropout risk,', 'analysing key student-related features and reviewing',
      'the limits of existing prediction techniques.'],
     ['Machine Learning', 'Research', 'Team project'], False),
    ('zcheck', 'ZCheck', 'Individual project · 2026', 'Private',
     ['Estimates whether an A/L Z-score meets the university', 'admission cutoff for a district, stream, course and',
      'university in Sri Lanka, trained on UGC cutoff data.'],
     ['Machine Learning', 'UGC dataset', 'Sri Lanka'], False),
    ('agroleaf', 'AgroLeaf', 'Smart irrigation prototype · 2025', 'Private',
     ['Helps Sri Lankan farmers optimise irrigation with soil-', 'moisture sensors, water-level monitoring and weather',
      'insights, plus leak detection and crop scheduling.'],
     ['IoT', 'Sensors', 'Multilingual'], False),
    ('kubernetes-demo', 'kubernetes-demo', 'Public repo · 2026', '',
     ['An Express API on Node.js, containerised with Docker', '(Compose for local dev) and deployed to Kubernetes', 'with its own Deployment and Service.'],
     ['Node.js', 'Express', 'Docker', 'Kubernetes'], True),
]

STACK = [  # (group, [(icon key, label)])
    ('AI & Data', [('python', 'Python'), ('jupyter', 'Jupyter'), ('numpy', 'NumPy'), ('pandas', 'pandas'), ('scikitlearn', 'scikit-learn'),
                   ('tensorflow', 'TensorFlow'), ('pytorch', 'PyTorch')]),
    ('Web & Backend', [('javascript', 'JavaScript'), ('nodedotjs', 'Node.js'), ('express', 'Express'), ('postgresql', 'PostgreSQL')]),
    ('DevOps & Tools', [('docker', 'Docker'), ('kubernetes', 'Kubernetes'), ('git', 'Git'), ('github', 'GitHub'), ('npm', 'npm')]),
]

LINKS = [  # (file, label, icon key or None for the globe, live?)    the URLs are in README.md
    ('portfolio', 'Portfolio · soon', None, False),
    ('linkedin', 'LinkedIn', 'linkedin', True),
    ('email', 'Email', 'gmail', True),
    ('github', 'GitHub', 'github', True),
]
FOOTER = 'Thanks for stopping by. Always happy to talk AI, data and ideas.'
# ───────────────────────────────────────────────────────────────────


def write(name, text):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def network():
    """A small neural-net diagram for the hero: hairline links, one path lit in the accent."""
    layers = [(740, [100, 150, 200]), (835, [75, 125, 175, 225]), (930, [125, 175])]
    lit = [(740, 150), (835, 125), (930, 175)]
    out = []
    for (x1, ys1), (x2, ys2) in zip(layers, layers[1:]):
        out += [f'<path d="M{x1} {a} L{x2} {b}" stroke="{LINE}" stroke-width="1"/>' for a in ys1 for b in ys2]
    out.append(f'<path class="flow" d="M{lit[0][0]} {lit[0][1]} L{lit[1][0]} {lit[1][1]} L{lit[2][0]} {lit[2][1]}" fill="none" stroke="{CYAN}" stroke-width="1.5" stroke-dasharray="5 7"/>')
    for x, ys in layers:
        for y in ys:
            on = (x, y) in lit
            out.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{BG}" stroke="{CYAN if on else LINE_STRONG}" stroke-width="1.5"/>'
                       + (f'<circle cx="{x}" cy="{y}" r="2.5" fill="{CYAN}"/>' if on else ''))
    return ''.join(out)


def hero():
    H = 300
    x = 56
    tw = len(TYPED) * 8.45
    body = f'''<defs><clipPath id="typed"><rect class="reveal" x="{x + 20}" y="204" width="0" height="24"/></clipPath></defs>
{panel(W, H)}
<text x="{x}" y="74" font-family="{MONO}" font-size="12" font-weight="600" letter-spacing="2.2" fill="{CYAN}">{esc(KICKER.upper())}</text>
<text x="{x - 3}" y="140" font-family="{SANS}" font-size="60" font-weight="700" letter-spacing="-1.5" fill="{TEXT}">{esc(NAME)}</text>
<text x="{x}" y="176" font-family="{SANS}" font-size="17" fill="{TEXT_SOFT}">{esc(TAGLINE)}</text>
<text x="{x}" y="221" font-family="{MONO}" font-size="14" fill="{CYAN}">&gt;</text>
<g clip-path="url(#typed)"><text x="{x + 20}" y="221" font-family="{MONO}" font-size="14" fill="{TEXT}">{esc(TYPED)}</text></g>
<rect class="caret" x="{x + 20 + tw + 4:.0f}" y="208" width="8" height="16" fill="{CYAN}"/>
{glyph('map-pin', x, 249, 14, TEXT_DIM)}<text x="{x + 21}" y="261" font-family="{SANS}" font-size="13" fill="{TEXT_SOFT}">{esc(LOCATION)}</text>
{glyph('graduation-cap', x + 110, 249, 14, TEXT_DIM)}<text x="{x + 131}" y="261" font-family="{SANS}" font-size="13" fill="{TEXT_SOFT}">{esc(SCHOOL)}</text>
{network()}'''
    style = f'''
.reveal {{ animation: type 2.6s steps({len(TYPED)}, end) .3s forwards; }}
@keyframes type {{ to {{ width: {tw + 4:.0f}px; }} }}
.caret {{ animation: blink 1.1s steps(1) infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}
.flow {{ animation: flow 2.4s linear infinite; }} @keyframes flow {{ to {{ stroke-dashoffset: -24; }} }}
@media (prefers-reduced-motion: reduce) {{ .reveal {{ width: {tw + 4:.0f}px; }} }}
'''
    return svg(W, H, f'{NAME}: {KICKER} at {SCHOOL}, {LOCATION}. {TAGLINE}', body, style)


def about():
    y0, rh = 112, 64
    H = y0 + rh * 2 + 10
    cells = []
    for i, (g, label, text) in enumerate(ABOUT):
        x, y = MARGIN + (i % 2) * 470, y0 + (i // 2) * rh
        if i % 2 == 0:
            cells.append(hairline(MARGIN, W - MARGIN, y))
        cells.append(f'{glyph(g, x, y + 16, 14, CYAN)}'
                     f'<text x="{x + 22}" y="{y + 27}" font-family="{MONO}" font-size="11" font-weight="600" letter-spacing="1.4" fill="{TEXT_DIM}">{esc(label.upper())}</text>'
                     f'<text x="{x}" y="{y + 50}" font-family="{SANS}" font-size="16" font-weight="600" fill="{TEXT}">{esc(text)}</text>')
    body = f'{panel(W, H)}{heading("About", "who I am")}{"".join(cells)}'
    return svg(W, H, 'About me: ' + '; '.join(f'{l} {t}' for _, l, t in ABOUT), body)


def section_heading(title, kicker):
    H = 104
    return svg(W, H, title, f'{panel(W, H)}{heading(title, kicker)}')


def project(i, n, title, meta, status, lines, tags, public):
    """A project card. Public repos get an arrow (the card links to the repo); private ones a
    status pill (Ongoing / Private) and a lock instead."""
    cw, H = W / n, 238
    pw, ox = split(n, i)
    x, right = ox + 28, ox + pw - 28
    desc = ''.join(f'<text x="{x}" y="{112 + j * 22}" font-family="{SANS}" font-size="14" fill="{TEXT_SOFT}">{esc(l)}</text>' for j, l in enumerate(lines))
    if public:
        corner = f'<text x="{right}" y="50" font-family="{MONO}" font-size="16" fill="{CYAN}" text-anchor="end">↗</text>'
    else:
        pill_w = round(30 + len(status) * 7)
        live = status == 'Ongoing'
        corner = (f'<rect x="{right - pill_w + .5}" y="31.5" width="{pill_w - 1}" height="25" rx="12.5" fill="{CYAN if live else "#fff"}" '
                  f'fill-opacity="{.08 if live else .03}" stroke="{CYAN if live else LINE_STRONG}" stroke-opacity="{.5 if live else 1}"/>'
                  + (f'<circle class="live" cx="{right - pill_w + 14}" cy="44" r="3" fill="{CYAN}"/>' if live
                     else glyph('lock', right - pill_w + 9, 38, 11, TEXT_SOFT, 2))
                  + f'<text x="{right - pill_w + 23}" y="48.5" font-family="{MONO}" font-size="11.5" font-weight="600" fill="{CYAN if live else TEXT_SOFT}">{esc(status)}</text>')
    body = f'''{panel(pw, H, x=ox)}
<text x="{x}" y="50" font-family="{SANS}" font-size="20" font-weight="700" letter-spacing="-.2" fill="{TEXT}">{esc(title)}</text>{corner}
<text x="{x}" y="74" font-family="{MONO}" font-size="12" fill="{CYAN}">{esc(meta)}</text>
{desc}{hairline(x, right, 186)}
<text x="{x}" y="214" font-family="{MONO}" font-size="12" fill="{TEXT_DIM}">{esc("  ·  ".join(tags))}</text>'''
    style = '.live { animation: live 2s ease-in-out infinite; } @keyframes live { 50% { opacity: .25; } }'
    return svg(f'{cw:g}', H, f'{title} ({meta}{", " + status if status else ""}): {" ".join(lines)} {", ".join(tags)}.', body, style)


def stack():
    """The toolbox as loose tiles (no panel behind them): a centred title plate, then each group
    under a small label with dotted rules either side, its tiles centred in a row."""
    tw, th, gap = 112, 100, 12
    pw = 220
    px = (W - pw) / 2
    out = [panel(pw, 80, x=px),
           f'<text x="{W / 2}" y="31" font-family="{MONO}" font-size="11.5" font-weight="600" letter-spacing="2" fill="{CYAN}" text-anchor="middle">TECH STACK</text>'
           f'<text x="{W / 2}" y="61" font-family="{SANS}" font-size="24" font-weight="700" letter-spacing="-.3" fill="{TEXT}" text-anchor="middle">Toolbox</text>']
    y, n = 108, 0
    for group, items in STACK:
        cw = round(40 + len(group) * 7.2)
        cx = (W - cw) / 2
        out.append(f'<path d="M0 {y + 14} H{cx - 14:.0f} M{cx + cw + 14:.0f} {y + 14} H{W}" stroke="{LINE_STRONG}" stroke-width="1.5" stroke-dasharray="1 7" stroke-linecap="round"/>'
                   f'{panel(cw, 28, 14, x=cx, y=y)}<circle cx="{cx + 16:.1f}" cy="{y + 14}" r="3" fill="{CYAN}"/>'
                   f'<text x="{cx + 27:.1f}" y="{y + 18}" font-family="{MONO}" font-size="11.5" font-weight="600" letter-spacing=".4" fill="{TEXT_SOFT}">{esc(group)}</text>')
        y += 44
        x0 = (W - (len(items) * tw + (len(items) - 1) * gap)) / 2
        for i, (key, label) in enumerate(items):
            x = x0 + i * (tw + gap)
            out.append(f'''<g transform="translate({x:.1f} {y})">{panel(tw, th, 14)}
<rect x="8.5" y="8.5" width="{tw - 17}" height="56" rx="9" fill="#0f151c" stroke="{LINE}"/>
<g class="item" style="animation-delay:{-n * .37:.2f}s">{logo(key, tw / 2 - 14, 22, 28, TEXT)}</g>
<text x="{tw / 2}" y="86" font-family="{SANS}" font-size="12.5" font-weight="600" fill="{TEXT}" text-anchor="middle">{esc(label)}</text></g>''')
            n += 1
        y += th + 26
    H = y - 26
    style = '.item { animation: hover 3.6s ease-in-out infinite; } @keyframes hover { 50% { transform: translateY(-3px); } }'
    return svg(W, H, 'My toolbox. ' + ' '.join(f'{g}: {", ".join(l for _, l in it)}.' for g, it in STACK), ''.join(out), style)


def button(i, n, label, key, live=True):
    """A link button; one that isn't live yet is drawn dimmed, with a dashed border."""
    cw, H = W / n, 56
    pw, ox = split(n, i)
    content = 18 + 10 + len(label) * 8.3
    x = ox + (pw - content) / 2
    ink = TEXT if live else TEXT_DIM
    icon = logo(key, f'{x:.1f}', 19, 18, ink) if key else glyph('globe', f'{x:.1f}', 19, 18, ink)
    frame = panel(pw, H, 12, x=ox) if live else (
        f'<rect x="{ox + .5}" y=".5" width="{pw - 1}" height="{H - 1}" rx="12" fill="{BG}" stroke="{LINE_STRONG}" stroke-dasharray="4 4"/>')
    body = (f'{frame}{icon}'
            f'<text x="{x + 28:.1f}" y="33.5" font-family="{SANS}" font-size="15" font-weight="600" fill="{ink}">{esc(label)}</text>')
    return svg(f'{cw:g}', H, label, body)


def footer():
    H = 72
    body = (f'{panel(W, H)}<circle cx="{W / 2 - len(FOOTER) * 3.45 - 14:.0f}" cy="36" r="3" fill="{CYAN}"/>'
            f'<text x="{W / 2}" y="41" font-family="{SANS}" font-size="15" fill="{TEXT_SOFT}" text-anchor="middle">{esc(FOOTER)}</text>')
    return svg(W, H, FOOTER, body)


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith('.svg'):
            os.remove(os.path.join(OUT, f))
    write('hero.svg', hero())
    write('about.svg', about())
    write('projects.svg', section_heading('Projects', 'what I build'))
    for i, (f, *card) in enumerate(PROJECTS):
        write(f'project-{f}.svg', project(i % 2, 2, *card))     # two to a row
    write('stack.svg', stack())
    for i, (f, label, key, live) in enumerate(LINKS):
        write(f'btn-{f}.svg', button(i, len(LINKS), label, key, live))
    write('footer.svg', footer())
    print('wrote', len(os.listdir(OUT)), 'files to', os.path.abspath(OUT))


if __name__ == '__main__':
    main()
