"""Polished SVG diagram engine modeled after official KAUST Mathematics Competition (KMC) past papers.

Visual hallmarks matched from official KMC 2025-2026 booklets & G6-7 sample papers:
- Clean white card container with subtle slate border (#cbd5e1), dark KMC plum/charcoal geometry strokes (#231942 / #111827)
- Soft KMC lilac/orchid polygon shading (#d8bfe6), pale sky-blue water/sector accents (#bae6fd), crisp neutral grids (#cbd5e1)
- Open white vertex circles (TikZ style) with italic serif math labels (A, B, C, D, P, Q)
- Dimension offset arrows, right-angle markers, trigonometric angle arcs, isometric 3D cubes, balance scales, spinners, number strips, cube nets, bar charts, and bilingual travel-time map graphs.
"""
import math
import xml.etree.ElementTree as ET

STROKE = "#231942"
DARK = "#111827"
SHADE = "#d8bfe6"
SHADE_ALT = "#c7d2fe"
WATER = "#cfe8ff"
GRID = "#cbd5e1"
MUTED = "#64748b"
ORANGE = "#ea580c"
GREEN = "#16a34a"
BLUE = "#2563eb"
RED = "#dc2626"


def wrap_svg(body: str, w: int = 320, h: int = 200, disp_w: int = 420,
             title: str = "KMC competition diagram / رسم مسابقة كاوست للرياضيات") -> str:
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{title}" '
        f'style="display:block;max-width:100%;width:{disp_w}px;max-height:280px;'
        f'margin:14px auto;background:#ffffff;border-radius:10px;border:1px solid #cbd5e1">'
        f'<title>{title}</title>{body}</svg>'
    )
    # Guarantee every generated diagram is strictly valid XML.
    ET.fromstring(svg)
    return svg


def _esc(text) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _vdot(x: float, y: float, r: float = 2.8) -> str:
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#ffffff" stroke="{DARK}" stroke-width="1.5"/>'


def _vlabel(x: float, y: float, text: str, size: int = 15, anchor: str = "middle") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Georgia, \'Times New Roman\', serif" '
        f'font-style="italic" font-size="{size}" font-weight="600" fill="{DARK}" '
        f'text-anchor="{anchor}">{_esc(text)}</text>'
    )


def _nlabel(x: float, y: float, text: str, size: int = 13, color: str = DARK,
            anchor: str = "middle", bold: bool = True) -> str:
    fw = "700" if bold else "500"
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter, system-ui, sans-serif" '
        f'font-size="{size}" font-weight="{fw}" fill="{color}" '
        f'text-anchor="{anchor}">{_esc(text)}</text>'
    )


def _dim_h(x1: float, x2: float, y: float, label: str, above: bool = False) -> str:
    ty = y - 7 if above else y + 15
    return (
        f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        f'<line x1="{x1:.1f}" y1="{y-4:.1f}" x2="{x1:.1f}" y2="{y+4:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        f'<line x1="{x2:.1f}" y1="{y-4:.1f}" x2="{x2:.1f}" y2="{y+4:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        + _nlabel((x1 + x2) / 2, ty, label, size=13, color=DARK)
    )


def _dim_v(x: float, y1: float, y2: float, label: str, right: bool = True) -> str:
    tx = x + 10 if right else x - 10
    anchor = "start" if right else "end"
    return (
        f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        f'<line x1="{x-4:.1f}" y1="{y1:.1f}" x2="{x+4:.1f}" y2="{y1:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        f'<line x1="{x-4:.1f}" y1="{y2:.1f}" x2="{x+4:.1f}" y2="{y2:.1f}" stroke="{MUTED}" stroke-width="1.3"/>'
        + _nlabel(tx, (y1 + y2) / 2 + 4, label, size=13, color=DARK, anchor=anchor)
    )


# 1. Matchstick adjacent squares: (1), (2), (3)
def svg_matchstick_squares(counts=(1, 2, 3)) -> str:
    u = 28
    parts = []
    cur_x = 26
    for idx, k in enumerate(counts, 1):
        y0 = 32
        for i in range(k):
            x = cur_x + i * u
            parts.append(
                f'<rect x="{x}" y="{y0}" width="{u}" height="{u}" fill="#faf5ff" '
                f'stroke="{STROKE}" stroke-width="2.4" stroke-linejoin="round"/>'
            )
        for i in range(k + 1):
            for dy in (0, u):
                parts.append(f'<circle cx="{cur_x + i*u}" cy="{y0 + dy}" r="2.3" fill="{ORANGE}"/>')
        parts.append(_nlabel(cur_x + (k * u) / 2, y0 + u + 22, f"({idx})", size=13, bold=False))
        cur_x += k * u + 26
    w = max(cur_x + 6, 260)
    return wrap_svg("".join(parts), w=w, h=96, disp_w=400)


# 2. Matchstick triangle row: (1), (2), (3)
def svg_matchstick_triangles(counts=(1, 2, 3)) -> str:
    s = 30
    ht = s * math.sqrt(3) / 2
    parts = []
    cur_x = 24
    y_bot = 64
    for idx, n_tri in enumerate(counts, 1):
        # n_tri triangles in a zig-zag strip (up, down, up, ...)
        verts = []
        for t in range(n_tri):
            x0 = cur_x + t * (s / 2)
            if t % 2 == 0:
                pts = [(x0, y_bot), (x0 + s, y_bot), (x0 + s / 2, y_bot - ht)]
            else:
                pts = [(x0, y_bot - ht), (x0 + s, y_bot - ht), (x0 + s / 2, y_bot)]
            pstr = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            parts.append(f'<polygon points="{pstr}" fill="#faf5ff" stroke="{STROKE}" stroke-width="2.2"/>')
            verts.extend(pts)
        seen = set()
        for vx, vy in verts:
            key = (round(vx, 1), round(vy, 1))
            if key not in seen:
                seen.add(key)
                parts.append(f'<circle cx="{vx:.1f}" cy="{vy:.1f}" r="2.2" fill="{ORANGE}"/>')
        span = (n_tri + 1) * (s / 2)
        parts.append(_nlabel(cur_x + span / 2, y_bot + 22, f"({idx})", size=13, bold=False))
        cur_x += span + 28
    w = int(max(cur_x + 10, 260))
    return wrap_svg("".join(parts), w=w, h=100, disp_w=400)


# 3. Shaded triangle inside rectangle (base = bottom, apex on top edge)
def svg_shaded_triangle_in_rect(L, W, apex_frac: float = 0.62, unit: str = "cm") -> str:
    rx, ry = 55, 26
    rw = 180
    rh = max(84, min(125, int(rw * (W / max(L, 1)))))
    ax = rx + rw * apex_frac
    lbl_l = f"{L} {unit}".strip()
    lbl_w = f"{W} {unit}".strip()
    body = (
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>'
        f'<polygon points="{rx},{ry+rh} {rx+rw},{ry+rh} {ax:.1f},{ry}" fill="{SHADE}" fill-opacity="0.85" '
        f'stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>'
        f'<rect x="{rx}" y="{ry+rh-10}" width="10" height="10" fill="none" stroke="{STROKE}" stroke-width="1.3"/>'
        + _vdot(rx, ry + rh) + _vdot(rx + rw, ry + rh) + _vdot(ax, ry)
        + _dim_h(rx, rx + rw, ry + rh + 14, lbl_l, above=False)
        + _dim_v(rx + rw + 14, ry, ry + rh, lbl_w, right=True)
    )
    return wrap_svg(body, w=320, h=ry + rh + 42)


# 4. Corner-inscribed shaded triangle inside rectangle L x W
def svg_inscribed_corner_triangle_in_rect(L: int, W: int, cut_top: int, cut_right: int) -> str:
    rx, ry = 48, 32
    rw, rh = 190, 120
    # Vertices: bottom-left (0,rh), a point on top at cut_top/L from left, and a point on right edge at cut_right/W from bottom
    px = rx + rw * (cut_top / L)
    py = ry
    qx = rx + rw
    qy = ry + rh * (1 - cut_right / W)
    bx, by = rx, ry + rh
    body = (
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>'
        f'<polygon points="{bx},{by} {px:.1f},{py} {qx},{qy:.1f}" fill="{SHADE}" fill-opacity="0.85" '
        f'stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>'
        + _nlabel((rx + px) / 2, ry - 8, str(cut_top), 12)
        + _nlabel((px + rx + rw) / 2, ry - 8, str(L - cut_top), 12)
        + _nlabel(rx + rw + 14, (ry + qy) / 2 + 4, str(W - cut_right), 12)
        + _nlabel(rx + rw + 14, (qy + ry + rh) / 2 + 4, str(cut_right), 12)
        + _nlabel(rx - 14, ry + rh / 2 + 4, str(W), 12)
        + _nlabel(rx + rw / 2, ry + rh + 18, str(L), 12)
        + _vdot(bx, by) + _vdot(px, py) + _vdot(qx, qy)
    )
    return wrap_svg(body, w=305, h=182)


# 5. Subdivided apex triangle for counting triangles (KMC G6-7 Q8 style)
def svg_subdivided_apex_triangle(n_base_parts: int = 3, n_levels: int = 2) -> str:
    ax, ay = 150, 22
    bx, by = 54, 156
    cx, cy = 246, 156
    parts = [f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#faf5ff" stroke="{STROKE}" stroke-width="2"/>']
    # Interior rays from apex to base divisions
    for i in range(1, n_base_parts):
        t = i / n_base_parts
        px = bx + (cx - bx) * t
        parts.append(f'<line x1="{ax}" y1="{ay}" x2="{px:.1f}" y2="{by}" stroke="{STROKE}" stroke-width="1.7"/>')
    # Horizontal cross segments (levels from apex: 1..n_levels-1; base is n_levels)
    for lv in range(1, n_levels):
        f = lv / n_levels
        lx = ax + (bx - ax) * f
        rx = ax + (cx - ax) * f
        ly = ay + (by - ay) * f
        parts.append(f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{rx:.1f}" y2="{ly:.1f}" stroke="{STROKE}" stroke-width="1.7"/>')
    parts.append(_vdot(ax, ay))
    return wrap_svg("".join(parts), w=300, h=180)


# 6. Balance scales (KMC G6-7 Q10 style)
def svg_balance_scales(s1_circles: int, s1_squares: int, s2_squares: int, s2_triangles: int) -> str:
    parts = []
    def draw_beam(cx, y_beam, left_shapes, right_shapes):
        out = []
        # Beam & fulcrum
        out.append(f'<line x1="{cx-68}" y1="{y_beam}" x2="{cx+68}" y2="{y_beam}" stroke="{STROKE}" stroke-width="2.4"/>')
        out.append(f'<polygon points="{cx},{y_beam+1} {cx-12},{y_beam+24} {cx+12},{y_beam+24}" fill="#5b21b6" stroke="{STROKE}" stroke-width="1.5"/>')
        # Left shapes
        lx = cx - 60
        for kind in left_shapes:
            out.append(_draw_shape(kind, lx, y_beam - 1))
            lx += 16
        # Right shapes
        rx = cx + 60 - (len(right_shapes) - 1) * 16
        for kind in right_shapes:
            out.append(_draw_shape(kind, rx, y_beam - 1))
            rx += 16
        return "".join(out)

    def _draw_shape(kind, x, y_bottom):
        if kind == "C":
            return f'<circle cx="{x}" cy="{y_bottom-7}" r="6.5" fill="#fb923c" stroke="{STROKE}" stroke-width="1.5"/>'
        if kind == "S":
            return f'<rect x="{x-6.5}" y="{y_bottom-13.5}" width="13" height="13" fill="#4ade80" stroke="{STROKE}" stroke-width="1.5"/>'
        # Triangle
        return f'<polygon points="{x},{y_bottom-14} {x-7},{y_bottom-0.5} {x+7},{y_bottom-0.5}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.5"/>'

    parts.append(draw_beam(92, 66, ["C"] * s1_circles, ["S"] * s1_squares))
    parts.append(draw_beam(248, 66, ["S"] * s2_squares, ["T"] * s2_triangles))
    return wrap_svg("".join(parts), w=340, h=112, disp_w=430)


# 7. Polyomino of identical unit squares (cross, T, L, staircase, U, H)
def svg_polyomino(cells, caption: str = "") -> str:
    # cells: list of (col, row)
    min_c = min(c for c, _ in cells)
    max_c = max(c for c, _ in cells)
    min_r = min(r for _, r in cells)
    max_r = max(r for _, r in cells)
    cols = max_c - min_c + 1
    rows = max_r - min_r + 1
    u = min(34, max(22, 130 // max(cols, rows)))
    ox = (280 - cols * u) / 2
    oy = 22
    parts = []
    for c, r in cells:
        x = ox + (c - min_c) * u
        y = oy + (r - min_r) * u
        parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{u}" height="{u}" '
            f'fill="{SHADE}" fill-opacity="0.82" stroke="{STROKE}" stroke-width="2"/>'
        )
    h = int(oy + rows * u + (32 if caption else 20))
    if caption:
        parts.append(_nlabel(140, oy + rows * u + 20, caption, size=12, color=MUTED, bold=False))
    return wrap_svg("".join(parts), w=280, h=h, disp_w=360)


# 8. Spinner divided into exact fractional sectors (KMC G6-7 Q14 style)
def svg_spinner(sectors) -> str:
    # sectors = [(fraction_float, label_str), ...] summing to 1.0
    cx, cy, r = 140, 88, 62
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SHADE}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="2.2"/>']
    ang = -math.pi / 2  # start at 12 o'clock
    palette = ["#ede9fe", "#ddd6fe", "#c4b5fd", "#fae8ff", "#e0e7ff", "#dbeafe"]
    for idx, (frac, lbl) in enumerate(sectors):
        span = frac * 2 * math.pi
        a1, a2 = ang, ang + span
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if span > math.pi else 0
        col = palette[idx % len(palette)]
        parts.append(
            f'<path d="M {cx},{cy} L {x1:.2f},{y1:.2f} A {r},{r} 0 {large},1 {x2:.2f},{y2:.2f} Z" '
            f'fill="{col}" stroke="{STROKE}" stroke-width="1.8"/>'
        )
        mid = (a1 + a2) / 2
        lx, ly = cx + 0.62 * r * math.cos(mid), cy + 0.62 * r * math.sin(mid) + 5
        parts.append(_nlabel(lx, ly, str(lbl), size=14, color=DARK))
        ang = a2
    # Pointer arrow from center
    px, py = cx + 30 * math.cos(-0.45), cy + 30 * math.sin(-0.45)
    parts.append(f'<line x1="{cx-16}" y1="{cy+8}" x2="{px:.1f}" y2="{py:.1f}" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{DARK}"/>')
    parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.8" fill="{ORANGE}"/>')
    return wrap_svg("".join(parts), w=280, h=176, disp_w=350)


# 9. Isometric 3D painted n x n x n cube (KMC G6-7 Q16 style)
def svg_painted_cube_3d(n: int = 3) -> str:
    cx, cy = 140, 92
    R = 64
    dx = R * math.cos(math.radians(30))
    dy = R * math.sin(math.radians(30))
    # Basis vectors from center (front corner):
    # u_left = (-dx, -dy), u_right = (dx, -dy), u_down = (0, R)
    # Top corner = (cx, cy - 2*dy)
    def pt_top(i, j):
        # i in 0..n along front-left, j in 0..n along front-right, from back-top corner (cx, cy - R)
        tx, ty = cx, cy - R
        return (tx - (i / n) * dx + (j / n) * dx, ty + (i / n) * dy + (j / n) * dy)

    def pt_left(i, k):
        # i in 0..n from back-left to front, k in 0..n downward
        lx, ly = cx - dx, cy - dy
        return (lx + (i / n) * dx, ly + (i / n) * dy + (k / n) * R)

    def pt_right(j, k):
        # j in 0..n from front to back-right, k in 0..n downward
        rx, ry = cx, cy
        return (rx + (j / n) * dx, ry - (j / n) * dy + (k / n) * R)

    top_poly = [pt_top(0, 0), pt_top(0, n), pt_top(n, n), pt_top(n, 0)]
    left_poly = [pt_left(0, 0), pt_left(n, 0), pt_left(n, n), pt_left(0, n)]
    right_poly = [pt_right(0, 0), pt_right(n, 0), pt_right(n, n), pt_right(0, n)]

    def poly_s(pts, fill):
        s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        return f'<polygon points="{s}" fill="{fill}" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>'

    parts = [
        poly_s(top_poly, "#ede9fe"),
        poly_s(left_poly, "#d8bfe6"),
        poly_s(right_poly, "#c4b5fd"),
    ]
    for t in range(1, n):
        p1, p2 = pt_top(t, 0), pt_top(t, n)
        q1, q2 = pt_top(0, t), pt_top(n, t)
        parts.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')
        parts.append(f'<line x1="{q1[0]:.1f}" y1="{q1[1]:.1f}" x2="{q2[0]:.1f}" y2="{q2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')

        l1, l2 = pt_left(t, 0), pt_left(t, n)
        lh1, lh2 = pt_left(0, t), pt_left(n, t)
        parts.append(f'<line x1="{l1[0]:.1f}" y1="{l1[1]:.1f}" x2="{l2[0]:.1f}" y2="{l2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')
        parts.append(f'<line x1="{lh1[0]:.1f}" y1="{lh1[1]:.1f}" x2="{lh2[0]:.1f}" y2="{lh2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')

        r1, r2 = pt_right(t, 0), pt_right(t, n)
        rh1, rh2 = pt_right(0, t), pt_right(n, t)
        parts.append(f'<line x1="{r1[0]:.1f}" y1="{r1[1]:.1f}" x2="{r2[0]:.1f}" y2="{r2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')
        parts.append(f'<line x1="{rh1[0]:.1f}" y1="{rh1[1]:.1f}" x2="{rh2[0]:.1f}" y2="{rh2[1]:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')

    return wrap_svg("".join(parts), w=280, h=180, disp_w=340)


# 10. Equilateral triangle with three corner equilateral cuts (KMC G6-7 Q17 style)
def svg_equilateral_corner_cuts(big_label: str = "6 cm", cut_label: str = "x") -> str:
    s = 148
    h = s * math.sqrt(3) / 2
    ax, ay = 140, 20
    bx, by = 140 - s / 2, 20 + h
    cx, cy = 140 + s / 2, 20 + h
    f = 0.25  # visual corner fraction
    def lerp(p, q, t):
        return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
    A, B, C = (ax, ay), (bx, by), (cx, cy)
    hex_pts = [
        lerp(A, B, f), lerp(B, A, f),
        lerp(B, C, f), lerp(C, B, f),
        lerp(C, A, f), lerp(A, C, f),
    ]
    hstr = " ".join(f"{x:.1f},{y:.1f}" for x, y in hex_pts)
    body = (
        f'<polygon points="{ax},{ay} {bx:.1f},{by:.1f} {cx:.1f},{cy:.1f}" fill="#ffffff" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>'
        f'<polygon points="{hstr}" fill="{SHADE}" fill-opacity="0.85" stroke="{STROKE}" stroke-width="1.8" stroke-linejoin="round"/>'
        + _nlabel(140, by + 20, big_label, size=13)
        + _nlabel(ax + 24, ay + 22, cut_label, size=12, color=BLUE)
    )
    return wrap_svg(body, w=280, h=182, disp_w=350)


# 11. Square cut into 8 congruent triangles by diagonals & midlines (KMC G6-7 Q18 style)
def svg_square_eighths_shaded(shaded_indices, draw_horiz: bool = False) -> str:
    # Square centered at (140,90), half-side 62. 8 sectors clockwise from top-left-upper:
    # 0: top-left of top triangle, 1: top-right of top triangle,
    # 2: upper-right, 3: lower-right, 4: bottom-right, 5: bottom-left, 6: lower-left, 7: upper-left
    x0, y0, s = 78, 28, 124
    xm, ym = x0 + s / 2, y0 + s / 2
    x1, y1 = x0 + s, y0 + s
    tris = [
        [(x0, y0), (xm, y0), (xm, ym)],
        [(xm, y0), (x1, y0), (xm, ym)],
        [(x1, y0), (x1, ym), (xm, ym)],
        [(x1, ym), (x1, y1), (xm, ym)],
        [(x1, y1), (xm, y1), (xm, ym)],
        [(xm, y1), (x0, y1), (xm, ym)],
        [(x0, y1), (x0, ym), (xm, ym)],
        [(x0, ym), (x0, y0), (xm, ym)],
    ]
    parts = [f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>']
    for idx in shaded_indices:
        pstr = " ".join(f"{px:.1f},{py:.1f}" for px, py in tris[idx])
        parts.append(f'<polygon points="{pstr}" fill="{SHADE}" fill-opacity="0.88" stroke="none"/>')
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{x1}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{xm}" y1="{y0}" x2="{xm}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    if draw_horiz:
        parts.append(f'<line x1="{x0}" y1="{ym}" x2="{x1}" y2="{ym}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="none" stroke="{STROKE}" stroke-width="2.2"/>')
    return wrap_svg("".join(parts), w=280, h=180, disp_w=340)


# 12. Horizontal number strip [10 |   | ? |   | 130] (KMC G6-7 Q20 style)
def svg_number_strip(cells) -> str:
    # cells: list of strings, e.g. ["10", "", "?", "", "130"]
    n = len(cells)
    cw, ch = 50, 36
    total_w = n * cw
    w = max(300, total_w + 48)
    ox = (w - total_w) / 2
    oy = 24
    parts = []
    for i, val in enumerate(cells):
        x = ox + i * cw
        is_q = (val == "?")
        fill = "#ede9fe" if is_q else "#ffffff"
        parts.append(f'<rect x="{x:.1f}" y="{oy}" width="{cw}" height="{ch}" fill="{fill}" stroke="{STROKE}" stroke-width="2"/>')
        if val:
            col = "#5b21b6" if is_q else DARK
            parts.append(_nlabel(x + cw / 2, oy + 23, val, size=14, color=col))
    return wrap_svg("".join(parts), w=w, h=84, disp_w=400)


# 13. Number-line alternating jumps (KMC G6-7 Q21 style)
def svg_number_line_jumps(fwd: int, back: int, target: int) -> str:
    w, h = 340, 108
    x0, x1, y = 30, 310, 68
    parts = [
        f'<line x1="{x0-8}" y1="{y}" x2="{x1+10}" y2="{y}" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{x1+14},{y} {x1+6},{y-4} {x1+6},{y+4}" fill="{STROKE}"/>',
    ]
    # Show key ticks: 0, fwd-back, fwd, ..., target
    max_v = max(target, fwd + 2)
    def xpos(v):
        return x0 + (v / max_v) * (x1 - x0)

    key_vals = sorted({0, fwd - back, fwd, target})
    for v in key_vals:
        xv = xpos(v)
        parts.append(f'<line x1="{xv:.1f}" y1="{y-5}" x2="{xv:.1f}" y2="{y+5}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(xv, y + 20, str(v), size=12, color=RED if v == target else DARK))

    # Forward arc 0 -> fwd
    xf = xpos(fwd)
    xb = xpos(fwd - back)
    parts.append(f'<path d="M {x0:.1f},{y-4} Q {(x0+xf)/2:.1f},{y-42} {xf:.1f},{y-4}" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    parts.append(_nlabel((x0 + xf) / 2, y - 28, f"+{fwd}", size=12, color=BLUE))
    # Backward arc fwd -> fwd-back
    parts.append(f'<path d="M {xf:.1f},{y+4} Q {(xf+xb)/2:.1f},{y+30} {xb:.1f},{y+4}" fill="none" stroke="{ORANGE}" stroke-width="1.8" stroke-dasharray="3,2"/>')
    parts.append(_nlabel((xf + xb) / 2, y + 33, f"-{back}", size=11, color=ORANGE))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=420)


# 14. Column cryptarithm card (KMC G6-7 Q22 & Senior Q5 style)
def svg_column_cryptarithm(addends, total_str: str) -> str:
    # addends: list of strings of equal/padded length, total_str: string
    cols = max(max(len(a) for a in addends), len(total_str))
    cw, rh = 24, 24
    w = max(220, cols * cw + 90)
    h = (len(addends) + 1) * rh + 38
    ox = (w - cols * cw) / 2 + 8
    oy = 26
    parts = []
    for r_idx, row in enumerate(addends):
        padded = row.rjust(cols)
        y = oy + r_idx * rh
        if r_idx == len(addends) - 1:
            parts.append(_nlabel(ox - 18, y, "+", size=15, color=STROKE))
        for c_idx, ch in enumerate(padded):
            if ch != " ":
                col = "#7c3aed" if ch in ("★", "☆", "?", "□") else DARK
                parts.append(_nlabel(ox + c_idx * cw, y, ch, size=15, color=col))
    line_y = oy + (len(addends) - 1) * rh + 8
    parts.append(f'<line x1="{ox - 26:.1f}" y1="{line_y}" x2="{ox + (cols-0.4)*cw:.1f}" y2="{line_y}" stroke="{STROKE}" stroke-width="2"/>')
    padded_tot = total_str.rjust(cols)
    ty = line_y + 21
    for c_idx, ch in enumerate(padded_tot):
        if ch != " ":
            parts.append(_nlabel(ox + c_idx * cw, ty, ch, size=15, color=DARK))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=320)


# 15. Flattened 6-square cube net with face labels
def svg_cube_net(cells_with_labels) -> str:
    # cells_with_labels: list of (col, row, label)
    min_c = min(c for c, _, _ in cells_with_labels)
    max_c = max(c for c, _, _ in cells_with_labels)
    min_r = min(r for _, r, _ in cells_with_labels)
    max_r = max(r for _, r, _ in cells_with_labels)
    cols = max_c - min_c + 1
    rows = max_r - min_r + 1
    u = 38
    w = max(260, cols * u + 60)
    h = rows * u + 40
    ox = (w - cols * u) / 2
    oy = 20
    parts = []
    for c, r, lbl in cells_with_labels:
        x = ox + (c - min_c) * u
        y = oy + (r - min_r) * u
        fill = "#ede9fe" if lbl == "?" else "#faf5ff"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{u}" height="{u}" fill="{fill}" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(_nlabel(x + u / 2, y + u / 2 + 5, str(lbl), size=15, color="#5b21b6" if lbl == "?" else DARK))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=360)


# 16. Bar chart with optional '?' missing bar
def svg_bar_chart(bars, y_max: int = None) -> str:
    # bars: list of (x_label, numeric_val_for_height, display_val_str)
    vals = [v for _, v, _ in bars]
    max_v = y_max if y_max else max(max(vals), 1)
    n = len(bars)
    w, h = 320, 178
    x0, y0, x1, y1 = 44, 24, 298, 144
    parts = []
    # Horizontal gridlines
    for step in range(5):
        gy = y1 - (step / 4) * (y1 - y0)
        gv = round((step / 4) * max_v)
        parts.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="{GRID}" stroke-width="1"/>')
        parts.append(_nlabel(x0 - 8, gy + 4, str(gv), size=10, color=MUTED, anchor="end", bold=False))
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    bw = min(34, int((x1 - x0 - 20) / (n * 1.6)))
    gap = (x1 - x0 - n * bw) / (n + 1)
    for i, (xlbl, v, disp) in enumerate(bars):
        bx = x0 + gap + i * (bw + gap)
        bh = max(8, (v / max_v) * (y1 - y0 - 12))
        by = y1 - bh
        is_q = (disp == "?")
        fill = "#fb923c" if is_q else SHADE
        stroke_d = 'stroke-dasharray="4,2"' if is_q else ""
        parts.append(
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw}" height="{bh:.1f}" '
            f'fill="{fill}" fill-opacity="0.88" stroke="{STROKE}" stroke-width="1.7" {stroke_d}/>'
        )
        parts.append(_nlabel(bx + bw / 2, by - 6, disp, size=12, color=ORANGE if is_q else DARK))
        parts.append(_nlabel(bx + bw / 2, y1 + 17, xlbl, size=11, color=DARK, bold=False))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=400)


# 17. Glass water cups (exact KMC Junior Q5 page_j-008.png style!)
def svg_water_cups(levels=(1.0, 0.0, 0.0), labels=("1", "2", "3")) -> str:
    n = len(levels)
    w = 96 * n + 40
    h = 148
    parts = []
    for i, lv in enumerate(levels):
        cx = 68 + i * 92
        yt, yb = 30, 108
        rt, rb = 28, 21
        if lv > 0.01:
            wy = yb - lv * (yb - yt)
            wr = rb + lv * (rt - rb)
            parts.append(
                f'<path d="M {cx-wr:.1f},{wy:.1f} L {cx-rb},{yb} A {rb},6 0 0,0 {cx+rb},{yb} '
                f'L {cx+wr:.1f},{wy:.1f} Z" fill="{WATER}" stroke="none"/>'
            )
            parts.append(f'<ellipse cx="{cx}" cy="{wy:.1f}" rx="{wr:.1f}" ry="5" fill="#bae6fd" stroke="{BLUE}" stroke-width="1.2"/>')
        parts.append(f'<ellipse cx="{cx}" cy="{yt}" rx="{rt}" ry="6" fill="none" stroke="{DARK}" stroke-width="2"/>')
        parts.append(f'<line x1="{cx-rt}" y1="{yt}" x2="{cx-rb}" y2="{yb}" stroke="{DARK}" stroke-width="2"/>')
        parts.append(f'<line x1="{cx+rt}" y1="{yt}" x2="{cx+rb}" y2="{yb}" stroke="{DARK}" stroke-width="2"/>')
        parts.append(f'<path d="M {cx-rb},{yb} A {rb},5.5 0 0,0 {cx+rb},{yb}" fill="none" stroke="{DARK}" stroke-width="2"/>')
        parts.append(f'<path d="M {cx-rb},{yb} A {rb},5.5 0 0,1 {cx+rb},{yb}" fill="none" stroke="{DARK}" stroke-width="1.3" stroke-dasharray="3,3"/>')
        if labels and i < len(labels):
            parts.append(_nlabel(cx, yb + 24, labels[i], size=12, color=MUTED, bold=False))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=380)


# 18. Subdivided 2x2 rectangle (perimeters or areas of 4 sub-rectangles)
def svg_subdivided_rect_2x2(tl: str, tr: str, bl: str, br: str) -> str:
    x0, y0 = 54, 24
    w1, w2 = 104, 88
    h1, h2 = 62, 74
    cells = [
        (x0, y0, w1, h1, tl),
        (x0 + w1, y0, w2, h1, tr),
        (x0, y0 + h1, w1, h2, bl),
        (x0 + w1, y0 + h1, w2, h2, br),
    ]
    parts = []
    for x, y, cw, ch, lbl in cells:
        is_q = ("?" in lbl)
        fill = SHADE if is_q else "#f8fafc"
        parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fill}" fill-opacity="0.82" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(_nlabel(x + cw / 2, y + ch / 2 + 5, lbl, size=14, color="#5b21b6" if is_q else DARK))
    return wrap_svg("".join(parts), w=300, h=184, disp_w=380)


# 19. Subdivided 3x3 rectangle (KMC Senior style)
def svg_subdivided_rect_3x3(grid_labels) -> str:
    # grid_labels: 3x3 list of strings
    x0, y0 = 46, 18
    ws = [68, 76, 64]
    hs = [44, 52, 46]
    parts = []
    cy = y0
    for r in range(3):
        cx = x0
        for c in range(3):
            lbl = grid_labels[r][c]
            is_q = ("?" in lbl)
            fill = SHADE if is_q else ("#f1f5f9" if lbl else "#ffffff")
            parts.append(f'<rect x="{cx}" y="{cy}" width="{ws[c]}" height="{hs[r]}" fill="{fill}" stroke="{STROKE}" stroke-width="1.8"/>')
            if lbl:
                parts.append(_nlabel(cx + ws[c] / 2, cy + hs[r] / 2 + 5, lbl, size=13, color="#5b21b6" if is_q else DARK))
            cx += ws[c]
        cy += hs[r]
    return wrap_svg("".join(parts), w=300, h=178, disp_w=380)


# 20. Square + circular/semicircular shaded regions
def svg_square_circle_shaded(side_label: str, mode: str = "inscribed_outside") -> str:
    x0, y0, s = 82, 22, 120
    xm, ym = x0 + s / 2, y0 + s / 2
    r = s / 2
    parts = []
    if mode == "inscribed_outside":
        # Shaded corners outside inscribed circle
        parts.append(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="{SHADE}" fill-opacity="0.85" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<circle cx="{xm}" cy="{ym}" r="{r}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<circle cx="{xm}" cy="{ym}" r="2.5" fill="{DARK}"/>')
    elif mode == "quarter_minus_semi":
        # Quarter circle centered at bottom-left, minus semicircle on bottom side
        parts.append(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<path d="M {x0},{y0+s} L {x0},{y0} A {s},{s} 0 0,1 {x0+s},{y0+s} Z" fill="{SHADE}" fill-opacity="0.85" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<path d="M {x0},{y0+s} A {r},{r} 0 0,1 {x0+s},{y0+s} Z" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>')
    elif mode == "two_semis_outside":
        # Square minus two inward semicircles on left and right edges
        parts.append(f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="{SHADE}" fill-opacity="0.85" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<path d="M {x0},{y0} A {r},{r} 0 0,1 {x0},{y0+s} Z" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<path d="M {x0+s},{y0} A {r},{r} 0 0,0 {x0+s},{y0+s} Z" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>')
    else:  # stadium: rectangle + two outer semicircles
        rx, ry, rw, rh = 86, 42, 108, 84
        rr = rh / 2
        parts.append(
            f'<path d="M {rx},{ry} L {rx+rw},{ry} A {rr},{rr} 0 0,1 {rx+rw},{ry+rh} '
            f'L {rx},{ry+rh} A {rr},{rr} 0 0,1 {rx},{ry} Z" fill="{SHADE}" fill-opacity="0.8" stroke="{STROKE}" stroke-width="2"/>'
        )
        parts.append(f'<line x1="{rx}" y1="{ry}" x2="{rx}" y2="{ry+rh}" stroke="{STROKE}" stroke-width="1.3" stroke-dasharray="4,3"/>')
        parts.append(f'<line x1="{rx+rw}" y1="{ry}" x2="{rx+rw}" y2="{ry+rh}" stroke="{STROKE}" stroke-width="1.3" stroke-dasharray="4,3"/>')
        parts.append(_dim_h(rx, rx + rw, ry + rh + 16, side_label))
        return wrap_svg("".join(parts), w=280, h=172, disp_w=360)

    parts.append(_dim_h(x0, x0 + s, y0 + s + 16, side_label))
    return wrap_svg("".join(parts), w=284, h=182, disp_w=350)


# 21. Unit-grid lattice polygon (exact Pick's / bounding-box / Pythagorean perimeter)
def svg_grid_polygon(cols: int, rows: int, vertices, labels=None) -> str:
    # vertices in math grid coords (0..cols, 0..rows) where y=0 is bottom
    u = min(28, int(140 / max(cols, rows)))
    w = max(260, cols * u + 72)
    h = rows * u + 52
    ox = (w - cols * u) / 2
    oy = 24
    parts = []
    for i in range(cols + 1):
        gx = ox + i * u
        parts.append(f'<line x1="{gx:.1f}" y1="{oy}" x2="{gx:.1f}" y2="{oy + rows*u}" stroke="{GRID}" stroke-width="1.1"/>')
    for j in range(rows + 1):
        gy = oy + j * u
        parts.append(f'<line x1="{ox:.1f}" y1="{gy}" x2="{ox + cols*u:.1f}" y2="{gy}" stroke="{GRID}" stroke-width="1.1"/>')
    pts_svg = [(ox + vx * u, oy + (rows - vy) * u) for vx, vy in vertices]
    pstr = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts_svg)
    parts.append(f'<polygon points="{pstr}" fill="{SHADE}" fill-opacity="0.82" stroke="{STROKE}" stroke-width="2.2" stroke-linejoin="round"/>')
    cx = sum(px for px, _ in pts_svg) / len(pts_svg)
    cy = sum(py for _, py in pts_svg) / len(pts_svg)
    for idx, (px, py) in enumerate(pts_svg):
        parts.append(_vdot(px, py, 2.8))
        if labels and idx < len(labels):
            dx, dy = px - cx, py - cy
            nm = max(math.hypot(dx, dy), 1)
            lx, ly = px + 13 * dx / nm, py + 13 * dy / nm + 4
            parts.append(_vlabel(lx, ly, labels[idx], size=13))
    parts.append(_nlabel(ox + u / 2, oy + rows * u + 16, "1", size=10, color=MUTED, bold=False))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=370)


# 22. Regular polygon with diagonals/chords
def svg_regular_polygon(n: int = 5, chords=(), vertex_names=None) -> str:
    cx, cy, r = 140, 92, 64
    pts = []
    for k in range(n):
        ang = -math.pi / 2 + k * (2 * math.pi / n)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    pstr = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts = [f'<polygon points="{pstr}" fill="#faf5ff" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>']
    for i, j in chords:
        parts.append(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{BLUE}" stroke-width="1.8"/>')
    names = vertex_names or [chr(65 + k) for k in range(n)]
    for k, (px, py) in enumerate(pts):
        parts.append(_vdot(px, py))
        ang = -math.pi / 2 + k * (2 * math.pi / n)
        lx, ly = cx + (r + 15) * math.cos(ang), cy + (r + 15) * math.sin(ang) + 5
        parts.append(_vlabel(lx, ly, names[k], size=14))
    return wrap_svg("".join(parts), w=280, h=186, disp_w=350)


# 23. Square ABCD + Equilateral triangle BCE (inside or outside)
def svg_square_equilateral(inside: bool = True) -> str:
    # Square ABCD: A(80,146), B(180,146), C(180,46), D(80,46). Equilateral on base AB!
    x0, y0, s = 88, 42, 104
    A = (x0, y0 + s)
    B = (x0 + s, y0 + s)
    C = (x0 + s, y0)
    D = (x0, y0)
    ht = s * math.sqrt(3) / 2
    E = (x0 + s / 2, y0 + s - ht) if inside else (x0 + s / 2, y0 + s + ht * 0.72)
    h_svg = 180 if inside else 235
    if not inside:
        # shift upward so outward triangle fits cleanly
        dy = -34
        A, B, C, D, E = [(p[0], p[1] + dy) for p in (A, B, C, D, E)]
    parts = [
        f'<rect x="{D[0]}" y="{D[1]}" width="{s}" height="{s}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]:.1f},{B[1]:.1f} {E[0]:.1f},{E[1]:.1f}" fill="{SHADE}" fill-opacity="0.78" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        f'<line x1="{D[0]:.1f}" y1="{D[1]:.1f}" x2="{E[0]:.1f}" y2="{E[1]:.1f}" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<line x1="{C[0]:.1f}" y1="{C[1]:.1f}" x2="{E[0]:.1f}" y2="{E[1]:.1f}" stroke="{BLUE}" stroke-width="1.8"/>',
    ]
    for pt, nm, ox, oy in [(D, "D", -12, -4), (C, "C", 12, -4), (A, "A", -12, 14), (B, "B", 12, 14), (E, "E", 0, -10 if inside else 16)]:
        parts.append(_vdot(pt[0], pt[1]))
        parts.append(_vlabel(pt[0] + ox, pt[1] + oy, nm, size=14))
    return wrap_svg("".join(parts), w=280, h=h_svg, disp_w=350)


# 24. Congruent inner triangles inside isosceles triangle (exact KMC Senior page_s-032.png!)
def svg_congruent_inner_triangles(base_angle_deg: int = 37) -> str:
    A = (46, 152)
    C = (254, 152)
    B = (150, 32)
    P = (150, 92)
    Q = (192, 116)
    parts = [
        f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#ffffff" stroke="{DARK}" stroke-width="1.8" stroke-linejoin="round"/>',
        f'<polygon points="{A[0]},{A[1]} {P[0]},{P[1]} {Q[0]},{Q[1]}" fill="{SHADE}" fill-opacity="0.55" stroke="{DARK}" stroke-width="1.6"/>',
        f'<line x1="{B[0]}" y1="{B[1]}" x2="{P[0]}" y2="{P[1]}" stroke="{DARK}" stroke-width="1.6"/>',
        f'<line x1="{P[0]}" y1="{P[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{DARK}" stroke-width="1.6"/>',
        _nlabel(76, 146, f"{base_angle_deg}°", size=11, color=BLUE),
        _nlabel(224, 146, f"{base_angle_deg}°", size=11, color=BLUE),
    ]
    for pt, nm, ox, oy in [(A, "A", -11, 12), (C, "C", 11, 12), (B, "B", 0, -9), (P, "P", -11, 3), (Q, "Q", 4, 15)]:
        parts.append(_vdot(pt[0], pt[1]))
        parts.append(_vlabel(pt[0] + ox, pt[1] + oy, nm, size=14))
    return wrap_svg("".join(parts), w=300, h=180, disp_w=380)


# 25. Travel-time map network (exact KMC Junior Q12 page_j-011.png style, localized!)
def svg_travel_map(nodes, edges) -> str:
    # nodes: dict of key -> (x, y, label_str)
    # edges: list of (k1, k2, weight_int)
    w, h = 340, 226
    parts = []
    for k1, k2, wt in edges:
        x1, y1, _ = nodes[k1]
        x2, y2, _ = nodes[k2]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DARK}" stroke-width="1.6"/>')
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        parts.append(f'<rect x="{mx-10:.1f}" y="{my-8:.1f}" width="20" height="16" rx="3" fill="#ffffff"/>')
        parts.append(_nlabel(mx, my + 4, str(wt), size=11, color=DARK))
    for k, (x, y, lbl) in nodes.items():
        bw = max(58, len(lbl) * 6 + 18)
        bh = 24
        is_special = k in ("S", "T", "M")
        fill = "#ede9fe" if is_special else "#ffffff"
        parts.append(f'<rect x="{x - bw/2:.1f}" y="{y - bh/2:.1f}" width="{bw:.1f}" height="{bh}" rx="5" fill="{fill}" stroke="{DARK}" stroke-width="1.6"/>')
        parts.append(_nlabel(x, y + 4, lbl, size=11, color=DARK))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=430)


# 26. Parallel lines zigzag angle puzzle
def svg_parallel_zigzag(ang_top: str, ang_mid: str, ang_bot: str) -> str:
    parts = [
        f'<line x1="34" y1="36" x2="266" y2="36" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="34" y1="150" x2="266" y2="150" stroke="{STROKE}" stroke-width="2"/>',
        # Parallel arrows
        f'<path d="M 235,32 L 243,36 L 235,40" fill="none" stroke="{STROKE}" stroke-width="1.6"/>',
        f'<path d="M 235,146 L 243,150 L 235,154" fill="none" stroke="{STROKE}" stroke-width="1.6"/>',
        # Zigzag: (95,36) -> (175,93) -> (105,150)
        f'<polyline points="95,36 178,93 105,150" fill="none" stroke="{BLUE}" stroke-width="2.2" stroke-linejoin="round"/>',
        _vdot(95, 36) + _vdot(178, 93) + _vdot(105, 150),
        _vlabel(42, 28, "L₁", 13) + _vlabel(42, 168, "L₂", 13),
        _nlabel(130, 52, ang_top, size=12, color=DARK),
        _nlabel(142, 97, ang_mid, size=13, color=ORANGE),
        _nlabel(138, 144, ang_bot, size=12, color=DARK),
    ]
    return wrap_svg("".join(parts), w=300, h=182, disp_w=380)


# 27. Subdivided triangle with n equal segments on each side (exact KMC page_d-018.png!)
def svg_subdivided_triangle_grid(n: int = 4, shaded_coords=()) -> str:
    # Barycentric grid of n rows: row r (0 at top C to n at bottom AB)
    C = (150.0, 22.0)
    A = (46.0, 156.0)
    B = (254.0, 156.0)
    def pt(r, c):
        # r in 0..n from top C, c in 0..r from left to right
        if r == 0:
            return C
        y = C[1] + (r / n) * (A[1] - C[1])
        xl = C[0] + (r / n) * (A[0] - C[0])
        xr = C[0] + (r / n) * (B[0] - C[0])
        x = xl + (c / r) * (xr - xl)
        return (x, y)

    parts = [f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#ffffff" stroke="{DARK}" stroke-width="1.8"/>']
    # Draw all n^2 unit sub-triangles; shade those in shaded_coords = set of (r, c, 'U'|'D')
    shaded_set = set(shaded_coords)
    for r in range(1, n + 1):
        for c in range(r):
            # Upright triangle: (r-1, c), (r, c), (r, c+1)
            u_pts = [pt(r - 1, c), pt(r, c), pt(r, c + 1)]
            fill = "#c0c6cf" if (r, c, "U") in shaded_set else "#ffffff"
            pstr = " ".join(f"{x:.1f},{y:.1f}" for x, y in u_pts)
            parts.append(f'<polygon points="{pstr}" fill="{fill}" stroke="{DARK}" stroke-width="1.1" stroke-linejoin="round"/>')
        for c in range(r - 1):
            # Downward triangle: (r-1, c), (r-1, c+1), (r, c+1)
            d_pts = [pt(r - 1, c), pt(r - 1, c + 1), pt(r, c + 1)]
            fill = "#c0c6cf" if (r, c, "D") in shaded_set else "#ffffff"
            pstr = " ".join(f"{x:.1f},{y:.1f}" for x, y in d_pts)
            parts.append(f'<polygon points="{pstr}" fill="{fill}" stroke="{DARK}" stroke-width="1.1" stroke-linejoin="round"/>')
    parts.append(_vlabel(A[0] - 12, A[1] + 8, "A", 14))
    parts.append(_vlabel(B[0] + 12, B[1] + 8, "B", 14))
    parts.append(_vlabel(C[0], C[1] - 7, "C", 14))
    return wrap_svg("".join(parts), w=300, h=180, disp_w=380)


# 28. Overlapping two rectangles / squares
def svg_overlapping_rects(lbl1: str, lbl2: str, lbl_ov: str) -> str:
    parts = [
        f'<rect x="52" y="28" width="118" height="90" fill="#e0e7ff" fill-opacity="0.7" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="126" y="62" width="122" height="92" fill="#fae8ff" fill-opacity="0.7" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="126" y="62" width="44" height="56" fill="{SHADE}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(88, 72, lbl1, size=12, color=DARK),
        _nlabel(208, 114, lbl2, size=12, color=DARK),
        _nlabel(148, 94, lbl_ov, size=12, color="#5b21b6"),
    ]
    return wrap_svg("".join(parts), w=300, h=180, disp_w=370)


# 29. Right trapezoid circumscribed around a semicircle on its vertical leg
def svg_trapezoid_semicircle(top_b: str, bot_b: str) -> str:
    # Vertical leg AD on left from (78,28) to (78,148), radius = 60, center O(78,88)
    x0, y_top, y_bot = 78, 28, 148
    r = (y_bot - y_top) / 2  # 60
    ym = (y_top + y_bot) / 2
    w_top, w_bot = 52, 132
    parts = [
        f'<polygon points="{x0},{y_top} {x0+w_top},{y_top} {x0+w_bot},{y_bot} {x0},{y_bot}" fill="#faf5ff" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        f'<path d="M {x0},{y_top} A {r},{r} 0 0,1 {x0},{y_bot} Z" fill="{SHADE}" fill-opacity="0.82" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="{x0}" y="{y_top}" width="9" height="9" fill="none" stroke="{STROKE}" stroke-width="1.2"/>',
        f'<rect x="{x0}" y="{y_bot-9}" width="9" height="9" fill="none" stroke="{STROKE}" stroke-width="1.2"/>',
        f'<circle cx="{x0}" cy="{ym}" r="2.6" fill="{DARK}"/>',
        _nlabel(x0 + w_top / 2, y_top - 8, top_b, size=12),
        _nlabel(x0 + w_bot / 2, y_bot + 18, bot_b, size=12),
        _vlabel(x0 - 11, ym + 5, "O", 13),
    ]
    return wrap_svg("".join(parts), w=290, h=182, disp_w=360)


# 30. 3D Cuboid water tank / Cylinder with inscribed solid
def svg_water_tank_3d(L_lbl: str, W_lbl: str, H_lbl: str, water_frac: float = 0.6) -> str:
    x0, y0, w, h = 66, 48, 130, 92
    dx, dy = 40, -24
    wh = h * water_frac
    wy = y0 + h - wh
    parts = [
        # Water block
        f'<polygon points="{x0},{wy:.1f} {x0+w},{wy:.1f} {x0+w+dx},{wy+dy:.1f} {x0+dx},{wy+dy:.1f}" fill="#bae6fd" stroke="{BLUE}" stroke-width="1.3"/>',
        f'<rect x="{x0}" y="{wy:.1f}" width="{w}" height="{wh:.1f}" fill="{WATER}" fill-opacity="0.85" stroke="none"/>',
        f'<polygon points="{x0+w},{wy:.1f} {x0+w+dx},{wy+dy:.1f} {x0+w+dx},{y0+h+dy:.1f} {x0+w},{y0+h}" fill="#93c5fd" fill-opacity="0.7" stroke="none"/>',
        # Hidden back edges
        f'<line x1="{x0+dx}" y1="{y0+dy}" x2="{x0+dx}" y2="{y0+h+dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        f'<line x1="{x0}" y1="{y0+h}" x2="{x0+dx}" y2="{y0+h+dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        f'<line x1="{x0+dx}" y1="{y0+h+dy}" x2="{x0+w+dx}" y2="{y0+h+dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        # Outer wireframe
        f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{x0},{y0} {x0+dx},{y0+dy} {x0+w+dx},{y0+dy} {x0+w},{y0}" fill="none" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        f'<polygon points="{x0+w},{y0} {x0+w+dx},{y0+dy} {x0+w+dx},{y0+h+dy} {x0+w},{y0+h}" fill="none" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        _nlabel(x0 + w / 2, y0 + h + 18, L_lbl, size=12),
        _nlabel(x0 + w + dx / 2 + 16, y0 + h + dy / 2 + 10, W_lbl, size=12),
        _nlabel(x0 - 18, y0 + h / 2 + 4, H_lbl, size=12),
    ]
    return wrap_svg("".join(parts), w=296, h=180, disp_w=370)


# 31. Multiplicative / additive vertex-edge number triangle
def svg_number_triangle_puzzle(v_top: str, v_bl: str, v_br: str, e_left: str, e_right: str, e_bot: str) -> str:
    T = (145, 32)
    BL = (64, 146)
    BR = (226, 146)
    ML = ((T[0] + BL[0]) / 2, (T[1] + BL[1]) / 2)
    MR = ((T[0] + BR[0]) / 2, (T[1] + BR[1]) / 2)
    MB = ((BL[0] + BR[0]) / 2, (BL[1] + BR[1]) / 2)
    parts = [
        f'<polygon points="{T[0]},{T[1]} {BL[0]},{BL[1]} {BR[0]},{BR[1]}" fill="none" stroke="{STROKE}" stroke-width="2.2"/>'
    ]
    # Edge rectangles
    for (mx, my), lbl in [(ML, e_left), (MR, e_right), (MB, e_bot)]:
        is_q = (lbl == "?")
        parts.append(f'<rect x="{mx-18:.1f}" y="{my-13:.1f}" width="36" height="26" rx="5" fill="{SHADE if is_q else "#ffffff"}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(mx, my + 5, lbl, size=13, color="#5b21b6" if is_q else DARK))
    # Vertex circles
    for (vx, vy), lbl in [(T, v_top), (BL, v_bl), (BR, v_br)]:
        is_q = (lbl == "?")
        parts.append(f'<circle cx="{vx}" cy="{vy}" r="16" fill="{SHADE if is_q else "#faf5ff"}" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(_nlabel(vx, vy + 5, lbl, size=13, color="#5b21b6" if is_q else DARK))
    return wrap_svg("".join(parts), w=290, h=182, disp_w=360)


# 32. Coordinate rectangular spiral walk (exact KMC Senior spiral problem style!)
def svg_spiral_walk() -> str:
    cx, cy, u = 148, 94, 24
    def gp(x, y):
        return (cx + x * u, cy - y * u)

    parts = []
    for gx in range(-3, 4):
        x, _ = gp(gx, 0)
        parts.append(f'<line x1="{x}" y1="{cy-3*u}" x2="{x}" y2="{cy+3*u}" stroke="{GRID}" stroke-width="1"/>')
    for gy in range(-3, 4):
        _, y = gp(0, gy)
        parts.append(f'<line x1="{cx-3*u}" y1="{y}" x2="{cx+3*u}" y2="{y}" stroke="{GRID}" stroke-width="1"/>')
    parts.append(f'<line x1="{cx-3*u-10}" y1="{cy}" x2="{cx+3*u+12}" y2="{cy}" stroke="{MUTED}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{cx}" y1="{cy+3*u+8}" x2="{cx}" y2="{cy-3*u-12}" stroke="{MUTED}" stroke-width="1.5"/>')
    # Spiral path: (0,0)->(1,0)->(1,1)->(-1,1)->(-1,-1)->(2,-1)->(2,2)->(-2,2)
    path_pts = [(0, 0), (1, 0), (1, 1), (-1, 1), (-1, -1), (2, -1), (2, 2), (-2, 2)]
    for i in range(len(path_pts) - 1):
        p1, p2 = gp(*path_pts[i]), gp(*path_pts[i + 1])
        parts.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{ORANGE}" stroke-width="2.4" stroke-linecap="round"/>')
        parts.append(_vdot(p1[0], p1[1], 2.5))
    plast = gp(*path_pts[-1])
    parts.append(f'<circle cx="{plast[0]}" cy="{plast[1]}" r="3.5" fill="{ORANGE}"/>')
    parts.append(_nlabel(cx + 3 * u + 16, cy + 4, "x", size=12, color=DARK))
    parts.append(_nlabel(cx + 8, cy - 3 * u - 8, "y", size=12, color=DARK))
    parts.append(_nlabel(cx - 12, cy + 14, "(0,0)", size=10, color=DARK, bold=False))
    return wrap_svg("".join(parts), w=296, h=190, disp_w=360)


# 33. Rectilinear staircase / right-angle polygon perimeter (KMC G6-7 Practice Set 1 Q2 style!)
def svg_rectilinear_staircase(W_lbl: str, H_lbl: str, steps: int = 3) -> str:
    x0, y0, rw, rh = 62, 26, 168, 114
    pts = [(x0, y0 + rh), (x0 + rw, y0 + rh)]
    # climb steps from bottom-right (x0+rw, y0+rh) up-left to (x0, y0)
    dx = rw / steps
    dy = rh / steps
    cx, cy = x0 + rw, y0 + rh
    for _ in range(steps):
        cy -= dy
        pts.append((cx, cy))
        cx -= dx
        pts.append((cx, cy))
    pstr = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    body = (
        f'<polygon points="{pstr}" fill="{SHADE}" fill-opacity="0.8" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>'
        f'<rect x="{x0}" y="{y0+rh-10}" width="10" height="10" fill="none" stroke="{STROKE}" stroke-width="1.3"/>'
        + _dim_h(x0, x0 + rw, y0 + rh + 16, W_lbl)
        + _dim_v(x0 - 14, y0, y0 + rh, H_lbl, right=False)
    )
    return wrap_svg(body, w=300, h=180, disp_w=370)


# 34. Midpoints of sides of a square joined (KMC G6-7 Practice Set 1 Q3 style!)
def svg_midpoint_square_shaded(side_lbl: str, shade_inner: bool = True) -> str:
    x0, y0, s = 82, 22, 118
    xm, ym = x0 + s / 2, y0 + s / 2
    outer_fill = "#ffffff" if shade_inner else SHADE
    inner_fill = SHADE if shade_inner else "#ffffff"
    body = (
        f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="{outer_fill}" fill-opacity="0.85" stroke="{STROKE}" stroke-width="2"/>'
        f'<polygon points="{xm},{y0} {x0+s},{ym} {xm},{y0+s} {x0},{ym}" fill="{inner_fill}" fill-opacity="0.88" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>'
        + _vdot(xm, y0) + _vdot(x0 + s, ym) + _vdot(xm, y0 + s) + _vdot(x0, ym)
        + _dim_h(x0, x0 + s, y0 + s + 16, side_lbl)
    )
    return wrap_svg(body, w=284, h=180, disp_w=350)


# 35. Cube inscribed inside a circular cylinder (KMC Senior Category B Q5 style!)
def svg_cube_in_cylinder(side_lbl: str) -> str:
    cx, yt, yb = 145, 36, 138
    rx, ry = 66, 20
    # Top square vertices on top ellipse at 45, 135, 225, 315 degrees
    angs = [math.radians(a) for a in (35, 145, 215, 325)]
    top_pts = [(cx + rx * math.cos(a), yt + ry * math.sin(a)) for a in angs]
    bot_pts = [(cx + rx * math.cos(a), yb + ry * math.sin(a)) for a in angs]
    tp_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in top_pts)
    front_face = [top_pts[0], top_pts[1], bot_pts[1], bot_pts[0]]
    ff_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in front_face)
    parts = [
        # Cylinder back/base
        f'<path d="M {cx-rx},{yb} A {rx},{ry} 0 0,1 {cx+rx},{yb}" fill="none" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="3,3"/>',
        # Cube hidden vertical edges
        f'<line x1="{top_pts[2][0]:.1f}" y1="{top_pts[2][1]:.1f}" x2="{bot_pts[2][0]:.1f}" y2="{bot_pts[2][1]:.1f}" stroke="{BLUE}" stroke-width="1.3" stroke-dasharray="3,3"/>',
        f'<line x1="{top_pts[3][0]:.1f}" y1="{top_pts[3][1]:.1f}" x2="{bot_pts[3][0]:.1f}" y2="{bot_pts[3][1]:.1f}" stroke="{BLUE}" stroke-width="1.3" stroke-dasharray="3,3"/>',
        # Cube front shaded face & top face
        f'<polygon points="{ff_str}" fill="{SHADE}" fill-opacity="0.72" stroke="{STROKE}" stroke-width="1.8" stroke-linejoin="round"/>',
        f'<polygon points="{tp_str}" fill="#ede9fe" fill-opacity="0.88" stroke="{STROKE}" stroke-width="1.8" stroke-linejoin="round"/>',
        # Cylinder outer outline
        f'<ellipse cx="{cx}" cy="{yt}" rx="{rx}" ry="{ry}" fill="none" stroke="{DARK}" stroke-width="2"/>',
        f'<line x1="{cx-rx}" y1="{yt}" x2="{cx-rx}" y2="{yb}" stroke="{DARK}" stroke-width="2"/>',
        f'<line x1="{cx+rx}" y1="{yt}" x2="{cx+rx}" y2="{yb}" stroke="{DARK}" stroke-width="2"/>',
        f'<path d="M {cx-rx},{yb} A {rx},{ry} 0 0,0 {cx+rx},{yb}" fill="none" stroke="{DARK}" stroke-width="2"/>',
        _dim_v(cx + rx + 14, yt, yb, side_lbl, right=True),
    ]
    return wrap_svg("".join(parts), w=300, h=176, disp_w=370)


if __name__ == "__main__":
    # Self-test all 32 diagram builders
    tests = [
        svg_matchstick_squares(),
        svg_matchstick_triangles(),
        svg_shaded_triangle_in_rect(12, 8),
        svg_inscribed_corner_triangle_in_rect(10, 8, 4, 3),
        svg_subdivided_apex_triangle(4, 2),
        svg_balance_scales(3, 2, 1, 3),
        svg_polyomino([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], "5 identical squares"),
        svg_spinner([(0.5, "1"), (0.25, "2"), (0.125, "3"), (0.125, "4")]),
        svg_painted_cube_3d(3),
        svg_equilateral_corner_cuts("6 cm", "x"),
        svg_square_eighths_shaded([0, 6, 7]),
        svg_number_strip(["10", "", "?", "", "130"]),
        svg_number_line_jumps(5, 3, 20),
        svg_column_cryptarithm(["1★2", "1★3", "1★4"], "309"),
        svg_cube_net([(1, 0, "1"), (0, 1, "2"), (1, 1, "3"), (2, 1, "4"), (3, 1, "5"), (1, 2, "6")]),
        svg_bar_chart([("Mon", 12, "12"), ("Tue", 18, "18"), ("Wed", 15, "?"), ("Thu", 21, "21")]),
        svg_water_cups((1.0, 0.0, 0.0)),
        svg_subdivided_rect_2x2("P = 14", "P = 18", "P = 20", "P = ?"),
        svg_subdivided_rect_3x3([["12", "", "16"], ["", "20", ""], ["14", "", "?"]]),
        svg_square_circle_shaded("10 cm", "inscribed_outside"),
        svg_square_circle_shaded("8 cm", "quarter_minus_semi"),
        svg_square_circle_shaded("12 m", "stadium"),
        svg_grid_polygon(5, 4, [(0, 1), (3, 0), (5, 3), (1, 4)], ["A", "B", "C", "D"]),
        svg_regular_polygon(5, [(0, 2), (0, 3)]),
        svg_square_equilateral(inside=True),
        svg_square_equilateral(inside=False),
        svg_congruent_inner_triangles(37),
        svg_travel_map(
            {"S": (170, 200, "Home"), "A": (75, 135, "Park"), "M": (170, 115, "Bakery"), "B": (265, 135, "Mall"), "T": (170, 30, "School")},
            [("S", "A", 8), ("S", "M", 11), ("S", "B", 9), ("A", "M", 4), ("B", "M", 5), ("M", "T", 10), ("A", "T", 15)],
        ),
        svg_parallel_zigzag("38°", "?°", "47°"),
        svg_subdivided_triangle_grid(4, [(1, 0, "U"), (2, 0, "D"), (3, 1, "D"), (4, 0, "U"), (4, 3, "U")]),
        svg_overlapping_rects("Area 36", "Area 25", "9"),
        svg_trapezoid_semicircle("4", "9"),
        svg_water_tank_3d("20 cm", "15 cm", "12 cm", 0.6),
        svg_number_triangle_puzzle("?", "3", "4", "18", "24", "12"),
        svg_spiral_walk(),
    ]
    print(f"OK: {len(tests)} KMC SVG builders verified cleanly.")
