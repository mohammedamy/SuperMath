"""Extended SVG diagram library for KAUST Mathematics Competition (KMC) bank expansion & study lessons.

Every helper delegates to kmc_diagrams.wrap_svg(), guaranteeing strict XML validity,
crisp vector scaling on both screen (Light/Dark) and A4 paper, and authentic KMC TikZ styling.
"""
import math
from kmc_diagrams import (
    BLUE,
    DARK,
    GREEN,
    GRID,
    MUTED,
    ORANGE,
    RED,
    SHADE,
    SHADE_ALT,
    STROKE,
    WATER,
    _dim_h,
    _dim_v,
    _esc,
    _nlabel,
    _vdot,
    _vlabel,
    wrap_svg,
)


# 1. Visual Fraction Grid (cols x rows, first `shaded` cells shaded in lilac/sky)
def svg_fraction_grid(cols: int = 5, rows: int = 4, shaded: int = 7, highlight_extra: int = 0) -> str:
    cw = min(40, 240 // max(cols, 1))
    ch = min(34, 140 // max(rows, 1))
    gw, gh = cols * cw, rows * ch
    x0, y0 = (300 - gw) / 2, (175 - gh) / 2
    parts = []
    idx = 0
    for r in range(rows):
        for c in range(cols):
            fill = "#ffffff"
            if idx < shaded:
                fill = SHADE
            elif idx < shaded + highlight_extra:
                fill = WATER
            parts.append(
                f'<rect x="{x0 + c*cw:.1f}" y="{y0 + r*ch:.1f}" width="{cw:.1f}" height="{ch:.1f}" '
                f'fill="{fill}" stroke="{STROKE}" stroke-width="1.5"/>'
            )
            idx += 1
    return wrap_svg("".join(parts), w=300, h=175, disp_w=360)


# 2. Two-Jar Juice Transfer Diagram
def svg_two_jars(lbl_a: str, frac_a: float, lbl_b: str, frac_b: float, arrow_txt: str = "") -> str:
    parts = []
    for i, (lbl, fr, fill_c) in enumerate([(lbl_a, frac_a, WATER), (lbl_b, frac_b, SHADE)]):
        jx = 52 + i * 148
        jy, jw, jh = 34, 68, 112
        wh = max(0.0, min(1.0, fr)) * (jh - 8)
        parts.append(
            f'<rect x="{jx}" y="{jy + jh - wh:.1f}" width="{jw}" height="{wh:.1f}" rx="4" fill="{fill_c}"/>'
            f'<path d="M {jx} {jy} L {jx} {jy+jh-6} Q {jx} {jy+jh} {jx+6} {jy+jh} L {jx+jw-6} {jy+jh} '
            f'Q {jx+jw} {jy+jh} {jx+jw} {jy+jh-6} L {jx+jw} {jy}" fill="none" stroke="{STROKE}" stroke-width="2.2"/>'
        )
        for tick in (0.25, 0.5, 0.75):
            ty = jy + jh - tick * (jh - 8)
            parts.append(f'<line x1="{jx}" y1="{ty:.1f}" x2="{jx+10}" y2="{ty:.1f}" stroke="{MUTED}" stroke-width="1.2"/>')
        parts.append(_nlabel(jx + jw / 2, jy + jh + 20, lbl, size=12))
    if arrow_txt:
        parts.append(
            f'<path d="M 132 76 Q 160 54 188 76" fill="none" stroke="{ORANGE}" stroke-width="2"/>'
            f'<polygon points="188,76 180,71 182,80" fill="{ORANGE}"/>'
            + _nlabel(160, 56, arrow_txt, size=12, color=ORANGE)
        )
    return wrap_svg("".join(parts), w=320, h=180, disp_w=380)


# 3. 2-Set Venn Diagram
def svg_venn_2(lbl_a: str, lbl_b: str, val_only_a: str, val_both: str, val_only_b: str, val_out: str = "") -> str:
    parts = [
        f'<rect x="16" y="14" width="288" height="156" rx="8" fill="#f8fafc" stroke="{MUTED}" stroke-width="1.3"/>',
        f'<circle cx="126" cy="95" r="54" fill="{WATER}" fill-opacity="0.65" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<circle cx="194" cy="95" r="54" fill="{SHADE}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="1.8"/>',
        _nlabel(100, 34, lbl_a, size=12, color=BLUE),
        _nlabel(220, 34, lbl_b, size=12, color=STROKE),
        _nlabel(96, 100, val_only_a, size=14),
        _nlabel(160, 100, val_both, size=14, color=RED),
        _nlabel(224, 100, val_only_b, size=14),
    ]
    if val_out:
        parts.append(_nlabel(276, 156, val_out, size=12, color=MUTED))
    return wrap_svg("".join(parts), w=320, h=184, disp_w=380)


# 4. 3-Set Venn Diagram
def svg_venn_3(la: str, lb: str, lc: str, vals: dict) -> str:
    # vals keys: a, b, c, ab, bc, ac, abc
    parts = [
        f'<circle cx="132" cy="78" r="48" fill="{WATER}" fill-opacity="0.52" stroke="{BLUE}" stroke-width="1.7"/>',
        f'<circle cx="188" cy="78" r="48" fill="{SHADE}" fill-opacity="0.52" stroke="{STROKE}" stroke-width="1.7"/>',
        f'<circle cx="160" cy="124" r="48" fill="#fde68a" fill-opacity="0.45" stroke="{ORANGE}" stroke-width="1.7"/>',
        _nlabel(92, 34, la, size=12, color=BLUE),
        _nlabel(228, 34, lb, size=12, color=STROKE),
        _nlabel(160, 184, lc, size=12, color=ORANGE),
        _nlabel(108, 68, vals.get("a", ""), size=12),
        _nlabel(212, 68, vals.get("b", ""), size=12),
        _nlabel(160, 148, vals.get("c", ""), size=12),
        _nlabel(160, 62, vals.get("ab", ""), size=12),
        _nlabel(133, 108, vals.get("ac", ""), size=12),
        _nlabel(187, 108, vals.get("bc", ""), size=12),
        _nlabel(160, 93, vals.get("abc", ""), size=13, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=196, disp_w=380)


# 5. Digital 24-Hour Clock Display
def svg_digital_clock(time_str: str = "12:21", sub_lbl: str = "24-hour display") -> str:
    parts = [
        f'<rect x="52" y="34" width="216" height="92" rx="14" fill="#0f172a" stroke="{STROKE}" stroke-width="2.5"/>',
        f'<rect x="64" y="46" width="192" height="68" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.4"/>',
        f'<text x="160" y="93" font-family="ui-monospace, Menlo, monospace" font-size="38" font-weight="800" '
        f'letter-spacing="4" fill="#38bdf8" text-anchor="middle">{_esc(time_str)}</text>',
        _nlabel(160, 148, sub_lbl, size=12, color=MUTED),
    ]
    return wrap_svg("".join(parts), w=320, h=166, disp_w=350)


# 6. Analog Clock Face with Hands at hour h (0..11) and minute m (0..59)
def svg_analog_clock(h: int = 4, m: int = 30, angle_lbl: str = "?") -> str:
    cx, cy, r = 150, 95, 72
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{STROKE}" stroke-width="2.2"/>']
    for k in range(1, 13):
        ang = math.radians(k * 30 - 90)
        tx, ty = cx + (r - 15) * math.cos(ang), cy + (r - 15) * math.sin(ang) + 4
        mx1, my1 = cx + (r - 5) * math.cos(ang), cy + (r - 5) * math.sin(ang)
        mx2, my2 = cx + r * math.cos(ang), cy + r * math.sin(ang)
        parts.append(f'<line x1="{mx1:.1f}" y1="{my1:.1f}" x2="{mx2:.1f}" y2="{my2:.1f}" stroke="{MUTED}" stroke-width="1.4"/>')
        parts.append(_nlabel(tx, ty, str(k), size=11))
    ang_m = ((m * 6) - 90) % 360
    ang_h = (((h % 12) * 30 + m * 0.5) - 90) % 360
    rm, rh = math.radians(ang_m), math.radians(ang_h)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 54*math.cos(rm):.1f}" y2="{cy + 54*math.sin(rm):.1f}" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round"/>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 38*math.cos(rh):.1f}" y2="{cy + 38*math.sin(rh):.1f}" stroke="{RED}" stroke-width="3.2" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.8" fill="{DARK}"/>')
    if angle_lbl:
        parts.append(_nlabel(258, 98, f"θ = {angle_lbl}", size=13, color=ORANGE))
    return wrap_svg("".join(parts), w=310, h=190, disp_w=360)


# 7. Dot Growth Pattern (L-shape or Cross for Step 1, 2, 3)
def svg_dot_pattern(mode: str = "L") -> str:
    parts = []
    for step in (1, 2, 3):
        bx = 26 + (step - 1) * 102
        by = 128
        coords = []
        if mode == "L":
            # Corner + `step` dots up + `step` dots right -> 2*step + 1
            coords.append((0, 0))
            for k in range(1, step + 1):
                coords.append((0, -k))
                coords.append((k, 0))
            for dx, dy in coords:
                parts.append(f'<circle cx="{bx + 18 + dx*16}" cy="{by + dy*16}" r="5" fill="{STROKE}"/>')
        else:
            # Cross: center + `step` in 4 directions -> 4*step + 1
            cx, cy = bx + 38, 86
            coords.append((0, 0))
            for k in range(1, step + 1):
                coords.extend([(k, 0), (-k, 0), (0, k), (0, -k)])
            for dx, dy in coords:
                parts.append(f'<circle cx="{cx + dx*11}" cy="{cy + dy*11}" r="3.8" fill="{BLUE}"/>')
        parts.append(_nlabel(bx + 38, 162, f"({step})", size=12, color=MUTED))
    return wrap_svg("".join(parts), w=326, h=180, disp_w=390)


# 8. Two-Step Function Machine Pipeline
def svg_function_machine(in_lbl: str, op1: str, op2: str, out_lbl: str) -> str:
    parts = [
        _nlabel(34, 92, in_lbl, size=15, color=BLUE),
        f'<line x1="56" y1="88" x2="86" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="86,88 79,83 79,93" fill="{DARK}"/>',
        f'<rect x="88" y="60" width="76" height="56" rx="10" fill="{WATER}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(126, 93, op1, size=14),
        f'<line x1="164" y1="88" x2="194" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="194,88 187,83 187,93" fill="{DARK}"/>',
        f'<rect x="196" y="60" width="76" height="56" rx="10" fill="{SHADE}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(234, 93, op2, size=14),
        f'<line x1="272" y1="88" x2="300" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="300,88 293,83 293,93" fill="{DARK}"/>',
        _nlabel(322, 92, out_lbl, size=15, color=RED),
    ]
    return wrap_svg("".join(parts), w=352, h=164, disp_w=400)


# 9. 3-Row Additive Number Pyramid
def svg_number_pyramid(top: str, mid_l: str, mid_r: str, bot_l: str, bot_m: str, bot_r: str) -> str:
    bw, bh = 66, 36
    boxes = [
        (137, 26, top, SHADE),
        (104, 70, mid_l, WATER), (170, 70, mid_r, WATER),
        (71, 114, bot_l, "#ffffff"), (137, 114, bot_m, "#ffffff"), (203, 114, bot_r, "#ffffff"),
    ]
    parts = []
    for x, y, txt, fc in boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="6" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(x + bw / 2, y + 23, txt, size=14))
    return wrap_svg("".join(parts), w=340, h=174, disp_w=380)


# 10. Motion Timeline (Opposite Meet or Same-Direction Chase)
def svg_motion_timeline(left_lbl: str, right_lbl: str, dist_lbl: str, v1_lbl: str, v2_lbl: str, meet: bool = True) -> str:
    parts = [
        f'<line x1="44" y1="98" x2="296" y2="98" stroke="{STROKE}" stroke-width="2.4"/>',
        _vdot(44, 98, 4), _vdot(296, 98, 4),
        _nlabel(44, 122, left_lbl, size=13),
        _nlabel(296, 122, right_lbl, size=13),
        _dim_h(44, 296, 142, dist_lbl, above=False),
        f'<line x1="48" y1="68" x2="118" y2="68" stroke="{BLUE}" stroke-width="2.4"/>',
        f'<polygon points="118,68 109,63 109,73" fill="{BLUE}"/>',
        _nlabel(83, 56, v1_lbl, size=12, color=BLUE),
    ]
    if meet:
        parts.extend([
            f'<line x1="292" y1="68" x2="222" y2="68" stroke="{RED}" stroke-width="2.4"/>',
            f'<polygon points="222,68 231,63 231,73" fill="{RED}"/>',
            _nlabel(257, 56, v2_lbl, size=12, color=RED),
        ])
    else:
        parts.extend([
            _vdot(154, 98, 4),
            f'<line x1="158" y1="68" x2="224" y2="68" stroke="{RED}" stroke-width="2.4"/>',
            f'<polygon points="224,68 215,63 215,73" fill="{RED}"/>',
            _nlabel(191, 56, v2_lbl, size=12, color=RED),
        ])
    return wrap_svg("".join(parts), w=340, h=176, disp_w=400)


# 11. Fencepost / Tree Spacing Diagram
def svg_fenceposts(gap_lbl: str = "d", total_lbl: str = "L") -> str:
    xs = [44, 98, 152, 248, 302]
    parts = [f'<line x1="34" y1="108" x2="312" y2="108" stroke="{MUTED}" stroke-width="2"/>']
    for x in xs:
        parts.append(f'<rect x="{x-4}" y="64" width="8" height="44" rx="2" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.6"/>')
    parts.append(_nlabel(200, 92, "· · ·", size=18, color=MUTED))
    parts.append(_dim_h(44, 98, 46, gap_lbl, above=True))
    parts.append(_dim_h(44, 302, 134, total_lbl, above=False))
    return wrap_svg("".join(parts), w=346, h=172, disp_w=390)


# 12. Folded Paper Corner Angle Diagram
def svg_paper_fold(ang_lbl: str = "α", ask_lbl: str = "x") -> str:
    parts = [
        f'<rect x="46" y="38" width="218" height="118" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<polyline points="184,38 264,38 264,116" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="5,4"/>',
        f'<polygon points="184,38 264,116 174,108" fill="{SHADE}" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="184" y1="38" x2="264" y2="116" stroke="{RED}" stroke-width="2"/>',
        _nlabel(214, 58, ang_lbl, size=13, color=RED),
        _nlabel(155, 58, ask_lbl, size=13, color=BLUE),
    ]
    return wrap_svg("".join(parts), w=316, h=182, disp_w=380)


# 13. Glued Unit Cube Stack (3D Isometric Columns)
def svg_cube_stack_3d(cols=(3, 2, 1)) -> str:
    # Draw isometric unit cubes side-by-side along x with heights cols[i]
    dx, dy, dz = 28, 14, 28
    parts = []
    x_start, y_base = 88, 142
    for i, h in enumerate(cols):
        for z in range(h):
            cx = x_start + i * dx
            cy = y_base + i * dy - z * dz
            # Top, Left, Right isometric faces
            top = f"{cx},{cy-dz} {cx+dx},{cy-dz-dy} {cx+2*dx},{cy-dz} {cx+dx},{cy-dz+dy}"
            left = f"{cx},{cy-dz} {cx+dx},{cy-dz+dy} {cx+dx},{cy+dy} {cx},{cy}"
            right = f"{cx+dx},{cy-dz+dy} {cx+2*dx},{cy-dz} {cx+2*dx},{cy} {cx+dx},{cy+dy}"
            parts.append(f'<polygon points="{top}" fill="#f3e8ff" stroke="{STROKE}" stroke-width="1.5"/>')
            parts.append(f'<polygon points="{left}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.5"/>')
            parts.append(f'<polygon points="{right}" fill="{SHADE_ALT}" stroke="{STROKE}" stroke-width="1.5"/>')
    return wrap_svg("".join(parts), w=310, h=190, disp_w=360)


# 14. 3x3 Magic Square Grid
def svg_magic_square_3x3(cells) -> str:
    # cells: 3x3 list of strings
    s = 44
    x0, y0 = 94, 24
    parts = []
    for r in range(3):
        for c in range(3):
            val = str(cells[r][c])
            fc = SHADE if "?" in val or val in ("x", "X") else ("#f0f9ff" if (r == 1 and c == 1) else "#ffffff")
            parts.append(
                f'<rect x="{x0 + c*s}" y="{y0 + r*s}" width="{s}" height="{s}" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>'
                + _nlabel(x0 + c*s + s/2, y0 + r*s + 27, val, size=15, color=(RED if "?" in val or val in ("x", "X") else DARK))
            )
    return wrap_svg("".join(parts), w=320, h=180, disp_w=340)


# 15. Street Grid Shortest Path (A at bottom-left to B at top-right, optional blocked node)
def svg_street_grid(cols: int = 4, rows: int = 3, blocked: tuple = None) -> str:
    cw = min(46, 210 // max(cols, 1))
    ch = min(38, 126 // max(rows, 1))
    gw, gh = cols * cw, rows * ch
    x0, y0 = (310 - gw) / 2, (184 - gh) / 2
    parts = []
    for r in range(rows + 1):
        y = y0 + r * ch
        parts.append(f'<line x1="{x0:.1f}" y1="{y:.1f}" x2="{x0+gw:.1f}" y2="{y:.1f}" stroke="{STROKE}" stroke-width="1.8"/>')
    for c in range(cols + 1):
        x = x0 + c * cw
        parts.append(f'<line x1="{x:.1f}" y1="{y0:.1f}" x2="{x:.1f}" y2="{y0+gh:.1f}" stroke="{STROKE}" stroke-width="1.8"/>')
    ax, ay = x0, y0 + gh
    bx, by = x0 + gw, y0
    parts.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="5" fill="{GREEN}"/>' + _vlabel(ax - 14, ay + 14, "A"))
    parts.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="5" fill="{BLUE}"/>' + _vlabel(bx + 14, by - 6, "B"))
    if blocked is not None:
        bc, br = blocked  # 0..cols from left, 0..rows from bottom
        px, py = x0 + bc * cw, y0 + (rows - br) * ch
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="#fee2e2" stroke="{RED}" stroke-width="2"/>')
        parts.append(_nlabel(px, py + 4, "×", size=14, color=RED))
    return wrap_svg("".join(parts), w=310, h=188, disp_w=370)


# 16. Labeled Pie Chart
def svg_pie_chart(slices) -> str:
    # slices: list of (fraction_0_to_1, label_str)
    cx, cy, r = 135, 95, 68
    colors = [WATER, SHADE, "#fde68a", "#bbf7d0", "#fecdd3"]
    parts = []
    ang0 = -90.0
    for i, (fr, lbl) in enumerate(slices):
        sweep = fr * 360.0
        ang1 = ang0 + sweep
        r0, r1 = math.radians(ang0), math.radians(ang1)
        x0, y0 = cx + r * math.cos(r0), cy + r * math.sin(r0)
        x1, y1 = cx + r * math.cos(r1), cy + r * math.sin(r1)
        large = 1 if sweep > 180 else 0
        col = colors[i % len(colors)]
        parts.append(
            f'<path d="M {cx} {cy} L {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z" '
            f'fill="{col}" stroke="{STROKE}" stroke-width="1.6"/>'
        )
        mid = math.radians((ang0 + ang1) / 2)
        lx, ly = cx + (r * 0.62) * math.cos(mid), cy + (r * 0.62) * math.sin(mid) + 4
        parts.append(_nlabel(lx, ly, lbl, size=11))
        ang0 = ang1
    return wrap_svg("".join(parts), w=280, h=190, disp_w=340)


# 17. Prime Factor Tree Diagram
def svg_factor_tree(root_lbl: str, left_lbl: str, right_lbl: str, rl_lbl: str, rr_lbl: str) -> str:
    nodes = [
        (160, 32, root_lbl, SHADE),
        (98, 92, left_lbl, WATER),
        (222, 92, right_lbl, "#ffffff"),
        (182, 152, rl_lbl, WATER),
        (262, 152, rr_lbl, WATER),
    ]
    edges = [(160, 32, 98, 92), (160, 32, 222, 92), (222, 92, 182, 152), (222, 92, 262, 152)]
    parts = [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{STROKE}" stroke-width="1.8"/>' for x1, y1, x2, y2 in edges]
    for x, y, lbl, fc in nodes:
        parts.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(x, y + 5, lbl, size=13))
    return wrap_svg("".join(parts), w=320, h=188, disp_w=360)


# 18. Binary Light-Bulb Panel (bits e.g. [1,0,1,1,0])
def svg_binary_bulbs(bits=(1, 0, 1, 1, 0), weights=(16, 8, 4, 2, 1)) -> str:
    n = len(bits)
    gap = 54
    x0 = 160 - (n - 1) * gap / 2
    parts = [f'<rect x="24" y="24" width="272" height="132" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.8"/>']
    for i, (b, w) in enumerate(zip(bits, weights)):
        cx = x0 + i * gap
        fc = "#fde047" if b else "#e2e8f0"
        sc = ORANGE if b else MUTED
        parts.append(f'<circle cx="{cx:.1f}" cy="74" r="17" fill="{fc}" stroke="{sc}" stroke-width="2"/>')
        parts.append(_nlabel(cx, 79, "ON" if b else "OFF", size=9, color=DARK))
        parts.append(_nlabel(cx, 122, str(w), size=13, color=STROKE))
    return wrap_svg("".join(parts), w=320, h=176, disp_w=380)


# 19. Geometric Square Completion / (a + b)^2 Partitioned Square
def svg_area_identity_square(a_lbl: str = "a", b_lbl: str = "b") -> str:
    x0, y0, sa, sb = 78, 22, 92, 50
    s = sa + sb
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{sa}" height="{sa}" fill="{WATER}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0+sa}" y="{y0}" width="{sb}" height="{sa}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0}" y="{y0+sa}" width="{sa}" height="{sb}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0+sa}" y="{y0+sa}" width="{sb}" height="{sb}" fill="#fde68a" stroke="{STROKE}" stroke-width="1.8"/>',
        _nlabel(x0 + sa / 2, y0 + sa / 2 + 5, f"{a_lbl}²", size=15),
        _nlabel(x0 + sa + sb / 2, y0 + sa / 2 + 5, f"{a_lbl}{b_lbl}", size=13),
        _nlabel(x0 + sa / 2, y0 + sa + sb / 2 + 5, f"{a_lbl}{b_lbl}", size=13),
        _nlabel(x0 + sa + sb / 2, y0 + sa + sb / 2 + 5, f"{b_lbl}²", size=13),
        _nlabel(x0 + sa / 2, y0 - 6, a_lbl, size=13, color=BLUE),
        _nlabel(x0 + sa + sb / 2, y0 - 6, b_lbl, size=13, color=ORANGE),
        _nlabel(x0 - 14, y0 + sa / 2 + 5, a_lbl, size=13, color=BLUE),
        _nlabel(x0 - 14, y0 + sa + sb / 2 + 5, b_lbl, size=13, color=ORANGE),
    ]
    return wrap_svg("".join(parts), w=300, h=188, disp_w=350)


# 20. Tank with Inlet (Fill) Pipe and Outlet (Drain) Pipe
def svg_pipe_tank(in_lbl: str = "+A", out_lbl: str = "−B") -> str:
    parts = [
        f'<rect x="96" y="72" width="128" height="74" fill="{WATER}" rx="4"/>',
        f'<path d="M 96 42 L 96 146 L 224 146 L 224 42" fill="none" stroke="{STROKE}" stroke-width="2.4"/>',
        # Inlet pipe top-left
        f'<path d="M 38 30 L 114 30 L 114 54" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>',
        _nlabel(68, 22, in_lbl, size=12, color=BLUE),
        # Outlet pipe bottom-right
        f'<path d="M 224 134 L 278 134 L 278 156" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>',
        _nlabel(262, 124, out_lbl, size=12, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=370)


# 21. Thales Circle: Diameter AB with Point C on Semicircle
def svg_thales_circle(ang_a_lbl: str = "34°", ask_lbl: str = "x") -> str:
    cx, cy, r = 160, 106, 74
    ax, ay = cx - r, cy
    bx, by = cx + r, cy
    ang = math.radians(-122)
    px, py = cx + r * math.cos(ang), cy + r * math.sin(ang)
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<polygon points="{ax},{ay} {bx},{by} {px:.1f},{py:.1f}" fill="{SHADE}" fill-opacity="0.55" stroke="{STROKE}" stroke-width="2"/>',
        _vdot(cx, cy, 3.2), _vlabel(cx, cy + 16, "O", 13),
        _vdot(ax, ay), _vlabel(ax - 13, ay + 5, "A"),
        _vdot(bx, by), _vlabel(bx + 13, by + 5, "B"),
        _vdot(px, py), _vlabel(px - 6, py - 10, "C"),
        _nlabel(ax + 34, ay - 8, ang_a_lbl, size=12, color=BLUE),
        _nlabel(bx - 32, by - 8, ask_lbl, size=12, color=RED),
    ]
    return wrap_svg("".join(parts), w=320, h=194, disp_w=370)


# 22. Isosceles Trapezoid with Dashed Altitudes
def svg_isosceles_trapezoid(top_lbl: str = "10", bot_lbl: str = "22", leg_lbl: str = "10", h_lbl: str = "h") -> str:
    parts = [
        f'<polygon points="104,44 216,44 264,138 56,138" fill="{SHADE}" fill-opacity="0.5" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<line x1="104" y1="44" x2="104" y2="138" stroke="{BLUE}" stroke-width="1.6" stroke-dasharray="5,4"/>',
        f'<line x1="216" y1="44" x2="216" y2="138" stroke="{BLUE}" stroke-width="1.6" stroke-dasharray="5,4"/>',
        f'<rect x="104" y="128" width="10" height="10" fill="none" stroke="{BLUE}" stroke-width="1.3"/>',
        _nlabel(160, 35, top_lbl, size=13),
        _nlabel(160, 158, bot_lbl, size=13),
        _nlabel(68, 88, leg_lbl, size=13),
        _nlabel(252, 88, leg_lbl, size=13),
        _nlabel(118, 95, h_lbl, size=13, color=BLUE),
    ]
    return wrap_svg("".join(parts), w=320, h=176, disp_w=380)


# 23. Power of a Point: Tangent PT and Secant PAB to Circle
def svg_power_of_point(pt_lbl: str = "PT", pa_lbl: str = "PA", ab_lbl: str = "AB") -> str:
    cx, cy, r = 206, 98, 60
    px, py = 48, 128
    # Tangent point T near top-left of circle, secant through A and B
    tx, ty = 176, 46
    ax, ay = 147, 108
    bx, by = 264, 83
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WATER}" fill-opacity="0.45" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="{px}" y1="{py}" x2="{tx}" y2="{ty}" stroke="{RED}" stroke-width="2.1"/>',
        f'<line x1="{px}" y1="{py}" x2="{bx}" y2="{by}" stroke="{BLUE}" stroke-width="2.1"/>',
        _vdot(px, py), _vlabel(px - 12, py + 5, "P"),
        _vdot(tx, ty), _vlabel(tx - 6, ty - 10, "T"),
        _vdot(ax, ay), _vlabel(ax - 4, ay + 18, "A"),
        _vdot(bx, by), _vlabel(bx + 12, by + 4, "B"),
        _nlabel(104, 78, pt_lbl, size=12, color=RED),
        _nlabel(102, 132, pa_lbl, size=12, color=BLUE),
        _nlabel(205, 112, ab_lbl, size=12, color=BLUE),
    ]
    return wrap_svg("".join(parts), w=316, h=182, disp_w=380)


# 24. Interior Angle Bisector AD in Triangle ABC
def svg_angle_bisector_tri(ab_lbl: str = "12", ac_lbl: str = "18", bd_lbl: str = "BD", dc_lbl: str = "DC") -> str:
    ax, ay = 142, 30
    bx, by = 54, 144
    cx, cy = 266, 144
    dx, dy = 138, 144
    parts = [
        f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<line x1="{ax}" y1="{ay}" x2="{dx}" y2="{dy}" stroke="{RED}" stroke-width="2" stroke-dasharray="5,3"/>',
        f'<path d="M 129 47 A 22 22 0 0 0 141 52" fill="none" stroke="{ORANGE}" stroke-width="1.8"/>',
        f'<path d="M 141 55 A 25 25 0 0 0 156 49" fill="none" stroke="{ORANGE}" stroke-width="1.8"/>',
        _vdot(ax, ay), _vlabel(ax, ay - 9, "A"),
        _vdot(bx, by), _vlabel(bx - 12, by + 4, "B"),
        _vdot(cx, cy), _vlabel(cx + 12, cy + 4, "C"),
        _vdot(dx, dy), _vlabel(dx, dy + 17, "D"),
        _nlabel(86, 84, ab_lbl, size=13),
        _nlabel(216, 84, ac_lbl, size=13),
        _nlabel(96, 160, bd_lbl, size=12, color=BLUE),
        _nlabel(202, 160, dc_lbl, size=12, color=BLUE),
    ]
    return wrap_svg("".join(parts), w=320, h=182, disp_w=380)


# 25. Right Triangle with Inscribed Circle (Inradius r = (a + b - c)/2)
def svg_right_tri_incircle(a_lbl: str = "6", b_lbl: str = "8", c_lbl: str = "10", r_lbl: str = "r") -> str:
    # Right angle at C=(74,144), B=(242,144) (len 168), A=(74,28) (len 116) -> hyp ~204 -> r=(116+168-204)/2 = 40
    cx, cy = 74, 144
    bx, by = 242, 144
    ax, ay = 74, 28
    hyp = math.hypot(bx - ax, by - ay)
    r = (116 + 168 - hyp) / 2
    ix, iy = cx + r, cy - r
    parts = [
        f'<polygon points="{ax},{ay} {cx},{cy} {bx},{by}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1"/>',
        f'<rect x="{cx}" y="{cy-12}" width="12" height="12" fill="none" stroke="{STROKE}" stroke-width="1.4"/>',
        f'<circle cx="{ix:.1f}" cy="{iy:.1f}" r="{r:.1f}" fill="{SHADE}" fill-opacity="0.55" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{ix:.1f}" y2="{cy:.1f}" stroke="{RED}" stroke-width="1.8"/>',
        _vdot(ix, iy, 2.8),
        _nlabel(ix + 10, iy + r / 2 + 3, r_lbl, size=13, color=RED),
        _nlabel(56, 88, a_lbl, size=13),
        _nlabel(158, 163, b_lbl, size=13),
        _nlabel(172, 78, c_lbl, size=13),
    ]
    return wrap_svg("".join(parts), w=306, h=182, disp_w=370)


# 26. Coordinate Parabola & Horizontal Line / Roots
def svg_parabola_roots(r1_lbl: str = "r₁", r2_lbl: str = "r₂", v_lbl: str = "V") -> str:
    # Quadratic Bezier P0=(68,28), P1=(168,268), P2=(268,28) -> exact y(0.5)=148, y=120 at x=119.7 and x=216.3
    parts = [
        f'<line x1="36" y1="120" x2="284" y2="120" stroke="{MUTED}" stroke-width="1.6"/>',
        f'<line x1="84" y1="18" x2="84" y2="170" stroke="{MUTED}" stroke-width="1.6"/>',
        f'<path d="M 68 28 Q 168 268 268 28" fill="none" stroke="{BLUE}" stroke-width="2.4"/>',
        f'<line x1="168" y1="22" x2="168" y2="168" stroke="{ORANGE}" stroke-width="1.3" stroke-dasharray="4,4"/>',
        _vdot(119.7, 120, 3.4), _nlabel(112, 138, r1_lbl, size=12),
        _vdot(216.3, 120, 3.4), _nlabel(224, 138, r2_lbl, size=12),
        _vdot(168, 148, 3.4), _nlabel(186, 162, v_lbl, size=12, color=ORANGE),
    ]
    return wrap_svg("".join(parts), w=316, h=182, disp_w=370)


# 27. Coordinate Diamond Region |x| + |y| <= R and Round Table Seating
def svg_coord_diamond(r_lbl: str = "R") -> str:
    cx, cy, u = 160, 92, 62
    parts = [
        f'<line x1="56" y1="{cy}" x2="264" y2="{cy}" stroke="{MUTED}" stroke-width="1.5"/>',
        f'<line x1="{cx}" y1="16" x2="{cx}" y2="168" stroke="{MUTED}" stroke-width="1.5"/>',
        f'<polygon points="{cx},{cy-u} {cx+u},{cy} {cx},{cy+u} {cx-u},{cy}" fill="{SHADE}" fill-opacity="0.55" stroke="{STROKE}" stroke-width="2"/>',
        _vdot(cx + u, cy), _nlabel(cx + u + 16, cy + 15, f"({r_lbl},0)", size=11),
        _vdot(cx, cy - u), _nlabel(cx + 22, cy - u + 4, f"(0,{r_lbl})", size=11),
        _vdot(cx - u, cy), _vdot(cx, cy + u),
    ]
    return wrap_svg("".join(parts), w=320, h=184, disp_w=360)


def svg_round_table(n_seats: int = 6, highlight_adj: bool = True) -> str:
    cx, cy, rt, rs = 160, 94, 46, 66
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{rt}" fill="{WATER}" stroke="{STROKE}" stroke-width="2"/>']
    for i in range(n_seats):
        ang = math.radians(i * (360 / n_seats) - 90)
        sx, sy = cx + rs * math.cos(ang), cy + rs * math.sin(ang)
        col = SHADE if (highlight_adj and i in (0, 1)) else "#ffffff"
        sc = RED if (highlight_adj and i in (0, 1)) else STROKE
        parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="11" fill="{col}" stroke="{sc}" stroke-width="1.8"/>')
        parts.append(_nlabel(sx, sy + 4, str(i + 1), size=10))
    return wrap_svg("".join(parts), w=320, h=188, disp_w=350)

