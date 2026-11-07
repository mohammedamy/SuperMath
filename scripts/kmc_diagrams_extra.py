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
    max_op = max(len(str(op1)), len(str(op2)))
    if max_op > 16:
        op_sz = 11
        bw = min(172, int(round(max_op * 6.8 + 22)))
    elif max_op > 11:
        op_sz = 12
        bw = min(144, int(round(max_op * 7.4 + 22)))
    else:
        bw = max(78, min(114, max_op * 8 + 20))
        op_sz = 13 if bw >= 94 else 14
    in_pad = max(62, len(str(in_lbl)) * 8 + 22)
    out_pad = max(62, len(str(out_lbl)) * 8 + 22)
    x_a1_s = in_pad
    x_b1 = x_a1_s + 28
    x_a2_s = x_b1 + bw
    x_b2 = x_a2_s + 28
    x_a3_s = x_b2 + bw
    x_a3_e = x_a3_s + 28
    w = x_a3_e + out_pad
    parts = [
        _nlabel(x_a1_s / 2 + 4, 92, in_lbl, size=14, color=BLUE),
        f'<line x1="{x_a1_s}" y1="88" x2="{x_b1 - 2}" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="{x_b1 - 2},88 {x_b1 - 9},83 {x_b1 - 9},93" fill="{DARK}"/>',
        f'<rect x="{x_b1}" y="60" width="{bw}" height="56" rx="10" fill="{WATER}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(x_b1 + bw / 2, 93, op1, size=op_sz),
        f'<line x1="{x_a2_s}" y1="88" x2="{x_b2 - 2}" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="{x_b2 - 2},88 {x_b2 - 9},83 {x_b2 - 9},93" fill="{DARK}"/>',
        f'<rect x="{x_b2}" y="60" width="{bw}" height="56" rx="10" fill="{SHADE}" stroke="{STROKE}" stroke-width="2"/>',
        _nlabel(x_b2 + bw / 2, 93, op2, size=op_sz),
        f'<line x1="{x_a3_s}" y1="88" x2="{x_a3_e}" y2="88" stroke="{DARK}" stroke-width="2"/>',
        f'<polygon points="{x_a3_e},88 {x_a3_e - 7},83 {x_a3_e - 7},93" fill="{DARK}"/>',
        _nlabel(x_a3_e + out_pad / 2 - 4, 92, out_lbl, size=14, color=RED),
    ]
    return wrap_svg("".join(parts), w=w, h=164, disp_w=min(430, max(390, w)))


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
def svg_binary_bulbs(bits=(1, 0, 1, 1, 0), weights=(16, 8, 4, 2, 1), lang: str = "en") -> str:
    n = len(bits)
    gap = min(56, max(44, 260 // max(n, 1)))
    w_box = max(272, n * gap + 36)
    w_svg = w_box + 48
    x0 = w_svg / 2 - (n - 1) * gap / 2
    on_t = "مضاء" if lang == "ar" else "ON"
    off_t = "مطفأ" if lang == "ar" else "OFF"
    parts = [f'<rect x="24" y="24" width="{w_box}" height="132" rx="12" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.8"/>']
    for i, (b, w) in enumerate(zip(bits, weights)):
        cx = x0 + i * gap
        fc = "#fde047" if b else "#e2e8f0"
        sc = ORANGE if b else MUTED
        parts.append(f'<circle cx="{cx:.1f}" cy="74" r="18" fill="{fc}" stroke="{sc}" stroke-width="2"/>')
        parts.append(_nlabel(cx, 78, on_t if b else off_t, size=9, color=DARK))
        parts.append(_nlabel(cx, 124, str(w), size=13, color=STROKE))
    return wrap_svg("".join(parts), w=int(w_svg), h=176, disp_w=min(420, int(w_svg) + 50))


# 19. Geometric Square Completion / (a + b)^2 Partitioned Square
def svg_area_identity_square(a_lbl: str = "a", b_lbl: str = "b") -> str:
    def _sq(lbl: str) -> str:
        s = str(lbl).strip()
        if any(ch in s for ch in "+-−/²³ "):
            return f"({s})²"
        return f"{s}²"

    def _prod(la: str, lb: str) -> str:
        sa_s, sb_s = str(la).strip(), str(lb).strip()
        if (sa_s, sb_s) in {("x", "1/x"), ("1/x", "x"), ("x²", "1/x²"), ("1/x²", "x²")}:
            return "1"
        wa = f"({sa_s})" if any(ch in sa_s for ch in "+-−/ ") else sa_s
        wb = f"({sb_s})" if any(ch in sb_s for ch in "+-−/ ") else sb_s
        if len(sa_s) == 1 and sa_s.isalpha() and len(sb_s) == 1 and sb_s.isalpha():
            return f"{sa_s}{sb_s}"
        if sa_s.isdigit() and len(sb_s) == 1 and sb_s.isalpha():
            return f"{sa_s}{sb_s}"
        if sb_s.isdigit() and len(sa_s) == 1 and sa_s.isalpha():
            return f"{sb_s}{sa_s}"
        if wb.startswith("(") and len(wa) <= 2 and wa.isalpha():
            return f"{wa}{wb}"
        if wa.startswith("(") and len(wb) <= 2 and wb.isalpha():
            return f"{wa}{wb}"
        return f"{wa}·{wb}"

    sq_a = _sq(a_lbl)
    sq_b = _sq(b_lbl)
    pr_ab = _prod(a_lbl, b_lbl)
    x0, y0, sa, sb = 82, 24, 96, 68
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{sa}" height="{sa}" fill="{WATER}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0+sa}" y="{y0}" width="{sb}" height="{sa}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0}" y="{y0+sa}" width="{sa}" height="{sb}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{x0+sa}" y="{y0+sa}" width="{sb}" height="{sb}" fill="#fde68a" stroke="{STROKE}" stroke-width="1.8"/>',
        _nlabel(x0 + sa / 2, y0 + sa / 2 + 5, sq_a, size=14 if len(sq_a) <= 6 else 12),
        _nlabel(x0 + sa + sb / 2, y0 + sa / 2 + 5, pr_ab, size=13 if len(pr_ab) <= 5 else 11),
        _nlabel(x0 + sa / 2, y0 + sa + sb / 2 + 5, pr_ab, size=13 if len(pr_ab) <= 5 else 12),
        _nlabel(x0 + sa + sb / 2, y0 + sa + sb / 2 + 5, sq_b, size=13 if len(sq_b) <= 5 else 11),
        _nlabel(x0 + sa / 2, y0 - 7, a_lbl, size=13, color=BLUE),
        _nlabel(x0 + sa + sb / 2, y0 - 7, b_lbl, size=13, color=ORANGE),
        _nlabel(x0 - 8, y0 + sa / 2 + 5, a_lbl, size=13, color=BLUE, anchor="end"),
        _nlabel(x0 - 8, y0 + sa + sb / 2 + 5, b_lbl, size=13, color=ORANGE, anchor="end"),
    ]
    return wrap_svg("".join(parts), w=320, h=206, disp_w=360)


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



# 28. Digit / Place-Value Cards (Divisibility, Palindromes, Base-b, Digit Sums)
def svg_digit_cards(slots, badge_lbl: str = "", note_lbl: str = "") -> str:
    n = len(slots)
    max_ch = max((len(str(s)) for s in slots), default=1)
    cw = max(42, min(88, int(max_ch * 8.2 + 22)))
    gap = 8
    total_w = n * cw + (n - 1) * gap
    pad_w = max(len(str(badge_lbl)) * 7.6 + 44, len(str(note_lbl)) * 7.4 + 44, total_w + 48, 300)
    w = int(round(pad_w))
    h = 158 if (badge_lbl and note_lbl) else (142 if (badge_lbl or note_lbl) else 116)
    ox = (w - total_w) / 2
    oy = 46 if badge_lbl else 26
    parts = []
    if badge_lbl:
        bw = max(110, len(str(badge_lbl)) * 7.4 + 28)
        parts.append(f'<rect x="{(w - bw)/2:.1f}" y="12" width="{bw:.1f}" height="24" rx="12" fill="#ede9fe" stroke="{STROKE}" stroke-width="1.4"/>')
        parts.append(_nlabel(w / 2, 28, badge_lbl, size=11, color="#5b21b6"))
    for i, s in enumerate(slots):
        x = ox + i * (cw + gap)
        st = str(s)
        is_mys = any(ch in st for ch in ("?", "□", "★", "d", "A", "B", "x", "k")) and not st.isdigit()
        fc = SHADE if is_mys else "#f8fafc"
        sc = "#6d28d9" if is_mys else STROKE
        parts.append(f'<rect x="{x:.1f}" y="{oy}" width="{cw}" height="48" rx="8" fill="{fc}" stroke="{sc}" stroke-width="2"/>')
        fs = 15 if len(st) <= 3 else (13 if len(st) <= 6 else 11)
        parts.append(_nlabel(x + cw / 2, oy + 30, st, size=fs, color=("#5b21b6" if is_mys else DARK)))
    if note_lbl:
        parts.append(_nlabel(w / 2, oy + 72, note_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=min(430, max(350, w + 30)))


# 29. Proportional Bar / Tape Model (Fractions of Remainder, Percent Chains, Ratios, Bundles)
def svg_tape_bar_split(segments, total_lbl: str = "", sub_lbl: str = "") -> str:
    # segments: list of (weight_float, label_str)
    tot_wt = sum(max(0.08, float(wt)) for wt, _ in segments) or 1.0
    min_bar_w = max(256, sum(max(52, int(len(str(lbl)) * 7.5 + 18)) for _, lbl in segments))
    bar_w = min(380, min_bar_w)
    w = max(320, bar_w + 56, int(len(str(total_lbl)) * 7.5 + 60), int(len(str(sub_lbl)) * 7.5 + 60))
    x0 = (w - bar_w) / 2
    y0 = 48 if total_lbl else 28
    bh = 44
    h = y0 + bh + (44 if sub_lbl else 24)
    palette = [WATER, SHADE, "#fde68a", "#bbf7d0", "#fecdd3"]
    parts = []
    if total_lbl:
        parts.append(_dim_h(x0, x0 + bar_w, y0 - 10, total_lbl, above=True))
    # Compute widths respecting minimum label width
    raw_ws = [max(46.0, (max(0.08, float(wt)) / tot_wt) * bar_w, len(str(lbl)) * 7.0 + 14) for wt, lbl in segments]
    scale = bar_w / sum(raw_ws)
    ws = [rw * scale for rw in raw_ws]
    # Ensure bar_w is wide enough if scaling shrunk any label box
    needed_factor = max((len(str(lbl)) * 7.0 + 14) / max(cw, 1) for (_, lbl), cw in zip(segments, ws))
    if needed_factor > 1.0:
        bar_w = int(bar_w * needed_factor) + 8
        w = max(w, bar_w + 56)
        x0 = (w - bar_w) / 2
        ws = [cw * needed_factor for cw in ws]
        parts = [_dim_h(x0, x0 + bar_w, y0 - 10, total_lbl, above=True)] if total_lbl else []
    cx = x0
    for i, ((_, lbl), cw) in enumerate(zip(segments, ws)):
        is_q = ("?" in str(lbl) or "؟" in str(lbl))
        fc = "#fed7aa" if is_q else palette[i % len(palette)]
        parts.append(f'<rect x="{cx:.1f}" y="{y0}" width="{cw:.1f}" height="{bh}" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(_nlabel(cx + cw / 2, y0 + 27, str(lbl), size=11 if len(str(lbl)) > 7 else 12, color=(ORANGE if is_q else DARK)))
        cx += cw
    if sub_lbl:
        parts.append(_nlabel(w / 2, y0 + bh + 25, sub_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=w, h=h, disp_w=min(440, max(370, w + 24)))


# 30. Circular Repeating Cycle / Modular Ring
def svg_cycle_ring(items, top_lbl: str = "", center_lbl: str = "") -> str:
    n = max(2, len(items))
    max_ch = max(len(str(x)) for x in items)
    nr = max(16, min(24, int(max_ch * 4.2 + 10)))
    ring_r = max(54, int(n * (nr + 6) / math.pi))
    ring_r = min(74, ring_r)
    w = max(310, int(2 * (ring_r + nr) + 76), int(len(str(top_lbl)) * 7.6 + 48))
    cy = (36 if top_lbl else 16) + ring_r + nr + 6
    h = cy + ring_r + nr + 18
    cx = w / 2
    parts = []
    if top_lbl:
        parts.append(_nlabel(cx, 22, top_lbl, size=12, color=BLUE))
    pts = []
    for i in range(n):
        ang = math.radians(-90 + i * (360.0 / n))
        pts.append((cx + ring_r * math.cos(ang), cy + ring_r * math.sin(ang), ang))
    for i in range(n):
        x1, y1, _ = pts[i]
        x2, y2, _ = pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        dist = max(math.hypot(dx, dy), 1.0)
        sx, sy = x1 + (nr + 3) * dx / dist, y1 + (nr + 3) * dy / dist
        ex, ey = x2 - (nr + 5) * dx / dist, y2 - (nr + 5) * dy / dist
        parts.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{MUTED}" stroke-width="1.7"/>')
        px, py = -dy / dist, dx / dist
        parts.append(
            f'<polygon points="{ex:.1f},{ey:.1f} {ex - 6*dx/dist + 3.5*px:.1f},{ey - 6*dy/dist + 3.5*py:.1f} '
            f'{ex - 6*dx/dist - 3.5*px:.1f},{ey - 6*dy/dist - 3.5*py:.1f}" fill="{ORANGE}"/>'
        )
    for i, (x, y, _) in enumerate(pts):
        fc = SHADE if i == 0 else WATER
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{nr}" fill="{fc}" stroke="{STROKE}" stroke-width="1.8"/>')
        fs = 12 if len(str(items[i])) <= 3 else 10
        parts.append(_nlabel(x, y + 4, str(items[i]), size=fs))
    if center_lbl:
        parts.append(_nlabel(cx, cy + 4, center_lbl, size=11, color=STROKE))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(410, int(w) + 30))


# 31. m x n Grid Dimensions (Counting Sub-Rectangles, Adjacent Pairs, Matchstick Grids)
def svg_grid_dimensions(cols: int, rows: int, col_lbl: str = "", row_lbl: str = "", mode: str = "subrect") -> str:
    dc = min(cols, 6)
    dr = min(rows, 5)
    u = min(28, 130 // max(dc, dr, 1))
    gw, gh = dc * u, dr * u
    w = max(300, gw + 116)
    h = gh + 72
    ox = (w - gw) / 2 - 10
    oy = 24
    parts = [f'<rect x="{ox:.1f}" y="{oy}" width="{gw}" height="{gh}" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>']
    if mode == "subrect" and dc >= 2 and dr >= 2:
        parts.append(f'<rect x="{ox + u:.1f}" y="{oy + u}" width="{min(2, dc-1)*u}" height="{u}" fill="{SHADE}" fill-opacity="0.75" stroke="none"/>')
    elif mode == "domino" and dc >= 2:
        parts.append(f'<rect x="{ox:.1f}" y="{oy}" width="{2*u}" height="{u}" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>')
    for c in range(1, dc):
        parts.append(f'<line x1="{ox + c*u:.1f}" y1="{oy}" x2="{ox + c*u:.1f}" y2="{oy+gh}" stroke="{STROKE}" stroke-width="1.4"/>')
    for r in range(1, dr):
        parts.append(f'<line x1="{ox:.1f}" y1="{oy + r*u}" x2="{ox+gw:.1f}" y2="{oy + r*u}" stroke="{STROKE}" stroke-width="1.4"/>')
    if mode == "matchsticks":
        for c in range(dc + 1):
            for r in range(dr + 1):
                parts.append(f'<circle cx="{ox + c*u:.1f}" cy="{oy + r*u:.1f}" r="2.3" fill="{ORANGE}"/>')
    cl = col_lbl or str(cols)
    rl = row_lbl or str(rows)
    parts.append(_dim_h(ox, ox + gw, oy + gh + 16, cl, above=False))
    parts.append(_dim_v(ox + gw + 14, oy, oy + gh, rl, right=True))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=380)


# 32. Logic / Constraint Statement Cards (Knights & Knaves, One False Statement, Simultaneous Mod)
def svg_statement_cards(cards, header_lbl: str = "") -> str:
    # cards: list of (badge_str, statement_str)
    n = len(cards)
    max_txt = max((len(str(b)) + len(str(s)) for b, s in cards), default=14)
    card_w = max(256, min(390, int(max_txt * 6.9 + 58)))
    w = max(310, card_w + 36, int(len(str(header_lbl)) * 7.6 + 44))
    y0 = 38 if header_lbl else 16
    rh = 30
    gap = 7
    h = y0 + n * rh + max(0, n - 1) * gap + 18
    x0 = (w - card_w) / 2
    parts = []
    if header_lbl:
        parts.append(_nlabel(w / 2, 23, header_lbl, size=12, color=BLUE))
    for i, (b, s) in enumerate(cards):
        y = y0 + i * (rh + gap)
        bw = max(36, int(len(str(b)) * 7.2 + 16))
        parts.append(f'<rect x="{x0:.1f}" y="{y}" width="{card_w}" height="{rh}" rx="7" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(f'<rect x="{x0:.1f}" y="{y}" width="{bw}" height="{rh}" rx="7" fill="{SHADE if i % 2 == 0 else WATER}" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(_nlabel(x0 + bw / 2, y + 19, str(b), size=11, color=STROKE))
        parts.append(_nlabel(x0 + bw + (card_w - bw) / 2, y + 19, str(s), size=11, color=DARK, bold=False))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(430, int(w) + 24))


# 33. Complete Chord / Handshake / Committee Graph on n Nodes
def svg_graph_chord_polygon(n_nodes: int, sub_lbl: str = "", bad_edge: bool = False) -> str:
    k = max(4, min(n_nodes, 8))
    cx, cy, r = 160, 84, 56
    h = 186 if sub_lbl else 166
    pts = []
    for i in range(k):
        ang = math.radians(-90 + i * (360.0 / k))
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang), ang))
    parts = []
    for i in range(k):
        for j in range(i + 1, k):
            if bad_edge and i == 0 and j == 1:
                parts.append(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{RED}" stroke-width="2.2" stroke-dasharray="4,3"/>')
            else:
                parts.append(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{GRID}" stroke-width="1.3"/>')
    for i, (px, py, ang) in enumerate(pts):
        fc = "#fecdd3" if (bad_edge and i in (0, 1)) else (SHADE if i == 0 else WATER)
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="11" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        lbl = str(i + 1) if (i < k - 1 or n_nodes <= 8) else str(n_nodes)
        parts.append(_nlabel(px, py + 4, lbl, size=10))
    if sub_lbl:
        w = max(320, int(len(str(sub_lbl)) * 7.5 + 48))
        if w != 320:
            # Recenter if wider subtitle
            dx = (w - 320) / 2
            return svg_algebra_flow([(sub_lbl, f"n = {n_nodes}")]) if dx > 90 else wrap_svg(
                f'<g transform="translate({dx:.1f},0)">{"".join(parts)}</g>' + _nlabel(w / 2, 170, sub_lbl, size=11, color=MUTED),
                w=int(w), h=h, disp_w=min(420, int(w) + 24),
            )
        parts.append(_nlabel(160, 170, sub_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=320, h=h, disp_w=370)


# 34. Pigeonhole / Stars-and-Bars / Coin-Stamp / Urn Bins
def svg_pigeonhole_bins(bins, header_lbl: str = "", footer_lbl: str = "") -> str:
    # bins: list of (top_name, inside_val)
    n = max(1, len(bins))
    max_in = max(max(len(str(a)), len(str(b))) for a, b in bins)
    bw = max(52, min(104, int(max_in * 7.6 + 20)))
    gap = 12
    tot_w = n * bw + (n - 1) * gap
    w = max(310, tot_w + 48, int(len(str(header_lbl)) * 7.5 + 48), int(len(str(footer_lbl)) * 7.5 + 48))
    x0 = (w - tot_w) / 2
    y0 = 48 if header_lbl else 28
    bh = 52
    h = y0 + bh + (50 if footer_lbl else 32)
    parts = []
    if header_lbl:
        parts.append(_nlabel(w / 2, 24, header_lbl, size=12, color=BLUE))
    cols = [WATER, SHADE, "#fde68a", "#bbf7d0", "#fecdd3"]
    for i, (bname, bval) in enumerate(bins):
        bx = x0 + i * (bw + gap)
        fc = cols[i % len(cols)]
        parts.append(f'<rect x="{bx:.1f}" y="{y0 + 14}" width="{bw}" height="{bh - 14}" rx="4" fill="{fc}" fill-opacity="0.7" stroke="none"/>')
        parts.append(f'<path d="M {bx:.1f} {y0} L {bx:.1f} {y0+bh} L {bx+bw:.1f} {y0+bh} L {bx+bw:.1f} {y0}" fill="none" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>')
        parts.append(_nlabel(bx + bw / 2, y0 + 34, str(bval), size=12 if len(str(bval)) <= 6 else 10))
        parts.append(_nlabel(bx + bw / 2, y0 + bh + 17, str(bname), size=11, color=MUTED, bold=False))
    if footer_lbl:
        parts.append(_nlabel(w / 2, y0 + bh + 38, footer_lbl, size=11, color=STROKE))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(430, int(w) + 26))


# 35. 6x6 Two-Dice Sample Space Grid
def svg_two_dice_grid(title_lbl: str = "6 × 6 = 36", d1_lbl: str = "1..6", d2_lbl: str = "1..6") -> str:
    u = 20
    ox, oy = 104, 42
    w = max(310, int(len(str(title_lbl)) * 7.5 + 54))
    ox = (w - 6 * u) / 2
    parts = [_nlabel(w / 2, 22, title_lbl, size=12, color=BLUE)]
    for k in range(6):
        parts.append(_nlabel(ox + k * u + u / 2, oy - 6, str(k + 1), size=10, color=STROKE))
        parts.append(_nlabel(ox - 10, oy + k * u + 14, str(k + 1), size=10, color=STROKE))
    for r in range(6):
        for c in range(6):
            fc = "#f3e8ff" if (r + c) % 2 == 0 else "#f0f9ff"
            parts.append(f'<rect x="{ox + c*u:.1f}" y="{oy + r*u}" width="{u}" height="{u}" fill="{fc}" stroke="{STROKE}" stroke-width="1.1"/>')
    parts.append(_nlabel(w / 2, oy + 6 * u + 18, f"{d1_lbl} × {d2_lbl}", size=11, color=MUTED, bold=False))
    return wrap_svg("".join(parts), w=int(w), h=188, disp_w=370)


# 36. Two-Pan Balance Scale (Counterfeit Coins, Symmetric Sums, Two-Value Totals)
def svg_pan_balance_coins(top_lbl: str, left_lbl: str, right_lbl: str, sub_lbl: str = "") -> str:
    w = max(320, int(len(str(top_lbl)) * 7.6 + 52), int(len(str(sub_lbl)) * 7.6 + 52))
    cx = w / 2
    lx, rx = cx - 84, cx + 84
    h = 186 if sub_lbl else 166
    pw = max(68, int(max(len(str(left_lbl)), len(str(right_lbl))) * 7.2 + 20))
    parts = [
        _nlabel(cx, 24, top_lbl, size=12, color=BLUE),
        # Base & pillar
        f'<polygon points="{cx-26},146 {cx+26},146 {cx},124" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<line x1="{cx}" y1="54" x2="{cx}" y2="126" stroke="{STROKE}" stroke-width="2.6"/>',
        # Beam
        f'<line x1="{lx}" y1="58" x2="{rx}" y2="58" stroke="{STROKE}" stroke-width="2.6"/>',
        f'<circle cx="{cx}" cy="58" r="4" fill="{ORANGE}" stroke="{STROKE}" stroke-width="1.5"/>',
        # Strings
        f'<line x1="{lx}" y1="58" x2="{lx - 22}" y2="98" stroke="{MUTED}" stroke-width="1.4"/>',
        f'<line x1="{lx}" y1="58" x2="{lx + 22}" y2="98" stroke="{MUTED}" stroke-width="1.4"/>',
        f'<line x1="{rx}" y1="58" x2="{rx - 22}" y2="98" stroke="{MUTED}" stroke-width="1.4"/>',
        f'<line x1="{rx}" y1="58" x2="{rx + 22}" y2="98" stroke="{MUTED}" stroke-width="1.4"/>',
        # Pans + labels
        f'<rect x="{lx - pw/2:.1f}" y="82" width="{pw}" height="24" rx="6" fill="{WATER}" stroke="{STROKE}" stroke-width="1.6"/>',
        _nlabel(lx, 98, left_lbl, size=11),
        f'<rect x="{rx - pw/2:.1f}" y="82" width="{pw}" height="24" rx="6" fill="#fde68a" stroke="{STROKE}" stroke-width="1.6"/>',
        _nlabel(rx, 98, right_lbl, size=11),
    ]
    if sub_lbl:
        parts.append(_nlabel(cx, 170, sub_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=h, disp_w=min(420, int(w) + 24))


# 37. Real Number Line / Sign Chart / Floor Jump Intervals
def svg_number_line_sign_chart(ticks, intervals=None, header_lbl: str = "", footer_lbl: str = "") -> str:
    # ticks: list of (label_str, is_closed_bool)
    m_cnt = max(2, len(ticks))
    min_gap = max(56, max(len(str(t)) for t, _ in ticks) * 8 + 18)
    line_w = max(230, (m_cnt - 1) * min_gap + 56)
    w = max(320, line_w + 56, int(len(str(header_lbl)) * 7.6 + 48), int(len(str(footer_lbl)) * 7.6 + 48))
    x0 = (w - line_w) / 2
    x1 = x0 + line_w
    y = 84 if header_lbl else 62
    h = y + (68 if footer_lbl else 46)
    parts = []
    if header_lbl:
        parts.append(_nlabel(w / 2, 26, header_lbl, size=12, color=BLUE))
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{STROKE}" stroke-width="2.2"/>')
    parts.append(f'<polygon points="{x1+6},{y} {x1-2},{y-4.5} {x1-2},{y+4.5}" fill="{STROKE}"/>')
    parts.append(f'<polygon points="{x0-6},{y} {x0+2},{y-4.5} {x0+2},{y+4.5}" fill="{STROKE}"/>')
    xs = [x0 + 28 + i * ((line_w - 56) / max(1, m_cnt - 1)) for i in range(m_cnt)]
    if intervals:
        pts_all = [x0 + 6] + xs + [x1 - 6]
        for idx, ilbl in enumerate(intervals[: len(pts_all) - 1]):
            mx = (pts_all[idx] + pts_all[idx + 1]) / 2
            col = GREEN if "+" in str(ilbl) else (RED if "−" in str(ilbl) or "-" in str(ilbl) else ORANGE)
            parts.append(_nlabel(mx, y - 16, str(ilbl), size=12, color=col))
    for x, (tlbl, closed) in zip(xs, ticks):
        fc = STROKE if closed else "#ffffff"
        parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="4.8" fill="{fc}" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(_nlabel(x, y + 23, str(tlbl), size=11))
    if footer_lbl:
        parts.append(_nlabel(w / 2, y + 48, footer_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(430, int(w) + 24))


# 38. Divisor-Pairing Rainbow Arcs (d <-> N/d)
def svg_divisor_rainbow(title_lbl: str, nodes, sub_lbl: str = "") -> str:
    # nodes: even or odd list of strings e.g. ["1", "2", "...", "N/2", "N"]
    n = len(nodes)
    gap = max(48, max(len(str(x)) for x in nodes) * 8 + 18)
    tot_w = (n - 1) * gap
    w = max(320, tot_w + 76, int(len(str(title_lbl)) * 7.6 + 48), int(len(str(sub_lbl)) * 7.6 + 48))
    x0 = (w - tot_w) / 2
    yb = 118
    h = 166 if sub_lbl else 146
    parts = [_nlabel(w / 2, 24, title_lbl, size=12, color=BLUE)]
    xs = [x0 + i * gap for i in range(n)]
    arc_cols = [ORANGE, BLUE, "#7c3aed"]
    for i in range(n // 2):
        xl, xr = xs[i], xs[n - 1 - i]
        rx = (xr - xl) / 2
        ry = max(18, 46 - i * 12)
        col = arc_cols[i % len(arc_cols)]
        parts.append(f'<path d="M {xl:.1f},{yb - 14} A {rx:.1f},{ry:.1f} 0 0,1 {xr:.1f},{yb - 14}" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="4,2"/>')
    for x, lbl in zip(xs, nodes):
        bw = max(34, len(str(lbl)) * 7.4 + 14)
        parts.append(f'<rect x="{x - bw/2:.1f}" y="{yb - 13}" width="{bw:.1f}" height="26" rx="6" fill="{WATER if lbl != "..." else "#f8fafc"}" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(_nlabel(x, yb + 4, str(lbl), size=11))
    if sub_lbl:
        parts.append(_nlabel(w / 2, 150, sub_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=h, disp_w=min(430, int(w) + 24))


# 39. Legendre p-adic / Factorial Prime-Power Step Bars
def svg_factorial_padic_bars(title_lbl: str, cols_data, footer_lbl: str = "") -> str:
    # cols_data: list of (label_bottom, height_ratio_0_1, top_tag)
    n = max(1, len(cols_data))
    bw = max(56, max(max(len(str(b)), len(str(t))) for b, _, t in cols_data) * 7 + 16)
    gap = 16
    tot_w = n * bw + (n - 1) * gap
    w = max(320, tot_w + 64, int(len(str(title_lbl)) * 7.6 + 48), int(len(str(footer_lbl)) * 7.6 + 48))
    x0 = (w - tot_w) / 2
    yb = 128
    h = 182 if footer_lbl else 160
    parts = [
        _nlabel(w / 2, 22, title_lbl, size=12, color=BLUE),
        f'<line x1="{x0 - 12:.1f}" y1="{yb}" x2="{x0 + tot_w + 12:.1f}" y2="{yb}" stroke="{STROKE}" stroke-width="1.8"/>',
    ]
    fills = [WATER, SHADE, "#fde68a", "#bbf7d0"]
    for i, (blbl, hr, tlbl) in enumerate(cols_data):
        bx = x0 + i * (bw + gap)
        bh = max(16, min(72, float(hr) * 72))
        parts.append(f'<rect x="{bx:.1f}" y="{yb - bh:.1f}" width="{bw}" height="{bh:.1f}" rx="4" fill="{fills[i % len(fills)]}" stroke="{STROKE}" stroke-width="1.7"/>')
        parts.append(_nlabel(bx + bw / 2, yb - bh - 7, str(tlbl), size=11, color=STROKE))
        parts.append(_nlabel(bx + bw / 2, yb + 18, str(blbl), size=11, color=DARK, bold=False))
    if footer_lbl:
        parts.append(_nlabel(w / 2, 166, footer_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=h, disp_w=min(430, int(w) + 24))


# 40. Telescoping / Paired Sequence Chain
def svg_telescoping_chain(terms, op_sym: str = "+", title_lbl: str = "", footer_lbl: str = "", slash_middle: bool = True) -> str:
    n = len(terms)
    cws = [max(48, int(len(str(t)) * 7.6 + 18)) for t in terms]
    op_w = 20 if op_sym else 8
    tot_w = sum(cws) + (n - 1) * op_w
    w = max(320, tot_w + 48, int(len(str(title_lbl)) * 7.6 + 48), int(len(str(footer_lbl)) * 7.6 + 48))
    x0 = (w - tot_w) / 2
    y0 = 46 if title_lbl else 24
    ch = 38
    h = y0 + ch + (44 if footer_lbl else 24)
    parts = []
    if title_lbl:
        parts.append(_nlabel(w / 2, 24, title_lbl, size=12, color=BLUE))
    cx = x0
    for i, (t, cw) in enumerate(zip(terms, cws)):
        is_end = i in (0, n - 1)
        is_dots = str(t) in ("...", "···", "⋯")
        fc = SHADE if (is_end and not is_dots) else ("#f8fafc" if is_dots else WATER)
        parts.append(f'<rect x="{cx:.1f}" y="{y0}" width="{cw}" height="{ch}" rx="7" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        parts.append(_nlabel(cx + cw / 2, y0 + 24, str(t), size=11 if len(str(t)) > 7 else 12))
        if slash_middle and not is_end and not is_dots:
            parts.append(f'<line x1="{cx + 8:.1f}" y1="{y0 + ch - 6}" x2="{cx + cw - 8:.1f}" y2="{y0 + 6}" stroke="{ORANGE}" stroke-width="2" stroke-opacity="0.85"/>')
        cx += cw
        if i < n - 1 and op_sym:
            parts.append(_nlabel(cx + op_w / 2, y0 + 24, op_sym, size=13, color=MUTED))
            cx += op_w
        elif i < n - 1:
            cx += op_w
    if footer_lbl:
        parts.append(_nlabel(w / 2, y0 + ch + 25, footer_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(440, int(w) + 24))


# 41. Clean Past-Paper Data / Standings / Rates Table
def svg_score_table(headers, rows, title_lbl: str = "") -> str:
    ncols = len(headers)
    col_ws = []
    for c in range(ncols):
        mx = len(str(headers[c]))
        for r in rows:
            if c < len(r):
                mx = max(mx, len(str(r[c])))
        col_ws.append(max(58, int(mx * 7.6 + 22)))
    tw = sum(col_ws)
    w = max(310, tw + 44, int(len(str(title_lbl)) * 7.6 + 48))
    x0 = (w - tw) / 2
    y0 = 38 if title_lbl else 16
    rh = 27
    h = y0 + (len(rows) + 1) * rh + 18
    parts = []
    if title_lbl:
        parts.append(_nlabel(w / 2, 23, title_lbl, size=12, color=BLUE))
    # Header row
    cx = x0
    for c, cw in enumerate(col_ws):
        parts.append(f'<rect x="{cx:.1f}" y="{y0}" width="{cw}" height="{rh}" fill="{SHADE}" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(_nlabel(cx + cw / 2, y0 + 18, str(headers[c]), size=11, color=STROKE))
        cx += cw
    for r_idx, row in enumerate(rows):
        ry = y0 + (r_idx + 1) * rh
        cx = x0
        fc = "#ffffff" if r_idx % 2 == 0 else "#f8fafc"
        for c, cw in enumerate(col_ws):
            val = str(row[c]) if c < len(row) else ""
            is_q = ("?" in val or "؟" in val)
            cell_fc = "#fef3c7" if is_q else fc
            parts.append(f'<rect x="{cx:.1f}" y="{ry}" width="{cw}" height="{rh}" fill="{cell_fc}" stroke="{STROKE}" stroke-width="1.4"/>')
            parts.append(_nlabel(cx + cw / 2, ry + 18, val, size=11, color=(ORANGE if is_q else DARK), bold=(is_q or c == 0)))
            cx += cw
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(430, int(w) + 24))


# 42. Coordinate Curve / Symmetry / Extremum Plot
def svg_symmetry_curve(mode: str = "odd_shift", title_lbl: str = "", p1_lbl: str = "", p2_lbl: str = "") -> str:
    w = max(316, int(len(str(title_lbl)) * 7.6 + 48))
    cx = w / 2
    parts = []
    if title_lbl:
        parts.append(_nlabel(cx, 22, title_lbl, size=12, color=BLUE))
    # Axes
    parts.append(f'<line x1="{cx - 118:.1f}" y1="126" x2="{cx + 118:.1f}" y2="126" stroke="{MUTED}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{cx:.1f}" y1="36" x2="{cx:.1f}" y2="162" stroke="{MUTED}" stroke-width="1.5"/>')
    if mode == "odd_shift":
        # Central point (0, c) at (cx, 88), symmetric curve through (cx-64, 114) and (cx+64, 62)
        parts.append(f'<line x1="{cx - 104:.1f}" y1="88" x2="{cx + 104:.1f}" y2="88" stroke="{ORANGE}" stroke-width="1.3" stroke-dasharray="4,3"/>')
        parts.append(f'<path d="M {cx - 96:.1f},130 C {cx - 42:.1f},124 {cx + 42:.1f},52 {cx + 96:.1f},46" fill="none" stroke="{BLUE}" stroke-width="2.4"/>')
        parts.extend([_vdot(cx, 88, 3.4), _vdot(cx - 64, 114, 3.2), _vdot(cx + 64, 62, 3.2)])
        if p1_lbl:
            parts.append(_nlabel(cx - 64, 148, p1_lbl, size=11))
        if p2_lbl:
            parts.append(_nlabel(cx + 64, 44, p2_lbl, size=11, color=RED))
    elif mode == "abs_v":
        vx = cx + 16
        parts.append(f'<polyline points="{vx - 92:.1f},46 {vx:.1f},126 {vx + 76:.1f},58" fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-linejoin="round"/>')
        parts.append(f'<line x1="{cx - 106:.1f}" y1="82" x2="{cx + 106:.1f}" y2="82" stroke="{RED}" stroke-width="1.6" stroke-dasharray="4,3"/>')
        parts.extend([_vdot(vx, 126, 3.4)])
        if p1_lbl:
            parts.append(_nlabel(vx, 148, p1_lbl, size=11))
        if p2_lbl:
            parts.append(_nlabel(cx - 82, 74, p2_lbl, size=11, color=RED))
    else:
        # Concave product / parabola extremum arch
        parts.append(f'<path d="M {cx - 88:.1f},136 Q {cx:.1f},-12 {cx + 88:.1f},136" fill="none" stroke="{BLUE}" stroke-width="2.4"/>')
        parts.extend([_vdot(cx, 62, 3.6)])
        if p1_lbl:
            parts.append(_nlabel(cx, 48, p1_lbl, size=11, color=ORANGE))
        if p2_lbl:
            parts.append(_nlabel(cx + 68, 148, p2_lbl, size=11))
    return wrap_svg("".join(parts), w=int(w), h=176, disp_w=min(410, int(w) + 24))


# 43. Geometric a^2 - b^2 L-Gnomon (Difference of Squares)
def svg_gnomon_diff_squares(a_lbl: str = "a", b_lbl: str = "b", note_lbl: str = "") -> str:
    x0, y0, sa, sb = 86, 22, 110, 46
    w = max(300, int(len(str(note_lbl)) * 7.5 + 52))
    x0 = (w - sa) / 2
    h = 198 if note_lbl else 168
    # L-shape: outer square (x0,y0,sa,sa) minus top-right corner (x0+sa-sb, y0, sb, sb)
    pts = (
        f"{x0:.1f},{y0} {x0+sa-sb:.1f},{y0} {x0+sa-sb:.1f},{y0+sb} "
        f"{x0+sa:.1f},{y0+sb} {x0+sa:.1f},{y0+sa} {x0:.1f},{y0+sa}"
    )
    parts = [
        f'<rect x="{x0+sa-sb:.1f}" y="{y0}" width="{sb}" height="{sb}" fill="#f8fafc" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,3"/>',
        f'<polygon points="{pts}" fill="{SHADE}" fill-opacity="0.78" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        f'<line x1="{x0:.1f}" y1="{y0+sb}" x2="{x0+sa-sb:.1f}" y2="{y0+sb}" stroke="{BLUE}" stroke-width="1.4" stroke-dasharray="4,3"/>',
        _nlabel(x0 + sa - sb / 2, y0 + sb / 2 + 4, f"{b_lbl}²", size=11, color=MUTED),
        _dim_h(x0, x0 + sa, y0 + sa + 14, a_lbl, above=False),
        _dim_v(x0 - 12, y0, y0 + sa, a_lbl, right=False),
        _nlabel(x0 + sa - sb / 2, y0 - 6, b_lbl, size=11, color=ORANGE),
    ]
    if note_lbl:
        parts.append(_nlabel(w / 2, 184, note_lbl, size=11, color=BLUE))
    return wrap_svg("".join(parts), w=int(w), h=h, disp_w=min(400, int(w) + 24))


# 44. Multi-Card Algebraic / Structural Flow Diagram (Zero-Overflow Dynamic Sizing)
def svg_algebra_flow(cards, arrows=None, title_lbl: str = "", footer_lbl: str = "") -> str:
    # cards: list of (top_tag, main_expr) tuples
    n = max(1, len(cards))
    cws = [max(78, int(max(len(str(t)), len(str(e))) * 7.6 + 24)) for t, e in cards]
    arr_ws = []
    for i in range(n - 1):
        albl = arrows[i] if (arrows and i < len(arrows)) else ""
        arr_ws.append(max(30, int(len(str(albl)) * 7.0 + 18)))
    tot_w = sum(cws) + sum(arr_ws)
    w = max(316, tot_w + 48, int(len(str(title_lbl)) * 7.6 + 48), int(len(str(footer_lbl)) * 7.6 + 48))
    x0 = (w - tot_w) / 2
    y0 = 46 if title_lbl else 24
    ch = 58
    h = y0 + ch + (42 if footer_lbl else 22)
    parts = []
    if title_lbl:
        parts.append(_nlabel(w / 2, 24, title_lbl, size=12, color=BLUE))
    cx = x0
    fills = [WATER, SHADE, "#fde68a", "#bbf7d0"]
    for i, ((ttag, mexpr), cw) in enumerate(zip(cards, cws)):
        fc = fills[i % len(fills)]
        parts.append(f'<rect x="{cx:.1f}" y="{y0}" width="{cw}" height="{ch}" rx="9" fill="{fc}" fill-opacity="0.72" stroke="{STROKE}" stroke-width="1.8"/>')
        if ttag:
            parts.append(_nlabel(cx + cw / 2, y0 + 19, str(ttag), size=10, color=MUTED, bold=False))
            parts.append(_nlabel(cx + cw / 2, y0 + 42, str(mexpr), size=12 if len(str(mexpr)) <= 10 else 11, color=DARK))
        else:
            parts.append(_nlabel(cx + cw / 2, y0 + 34, str(mexpr), size=12 if len(str(mexpr)) <= 10 else 11, color=DARK))
        cx += cw
        if i < n - 1:
            aw = arr_ws[i]
            albl = arrows[i] if (arrows and i < len(arrows)) else ""
            ay = y0 + ch / 2
            parts.append(f'<line x1="{cx + 4:.1f}" y1="{ay:.1f}" x2="{cx + aw - 6:.1f}" y2="{ay:.1f}" stroke="{ORANGE}" stroke-width="2"/>')
            parts.append(f'<polygon points="{cx + aw - 4:.1f},{ay:.1f} {cx + aw - 11:.1f},{ay - 4.5:.1f} {cx + aw - 11:.1f},{ay + 4.5:.1f}" fill="{ORANGE}"/>')
            if albl:
                parts.append(_nlabel(cx + aw / 2, ay - 8, str(albl), size=10, color=ORANGE))
            cx += aw
    if footer_lbl:
        parts.append(_nlabel(w / 2, y0 + ch + 25, footer_lbl, size=11, color=MUTED))
    return wrap_svg("".join(parts), w=int(w), h=int(h), disp_w=min(440, int(w) + 24))
