"""Rich Bilingual (EN + AR) Study Lessons & Bespoke Primary SVG Helpers for ETEC Nafes Grade 3."""
from fractions import Fraction
import math

from nafes_common import (
    BLUE,
    GREEN,
    GRID,
    MUTED,
    ORANGE,
    RED,
    SHADE,
    SHADE_ALT,
    STROKE,
    WATER,
    _wrap_nafes_svg,
    dm,
    esc,
    m,
    make_nafes_lesson,
    nafes_concept,
    nafes_worked_example,
    svg_bar_chart,
    svg_column_cryptarithm,
    svg_cube_stack_3d,
    svg_matchstick_squares,
    svg_nafes_analog_clock,
    svg_nafes_fraction_bars,
    svg_nafes_function_table,
    svg_nafes_pictograph,
    svg_nafes_place_value_blocks,
    svg_nafes_sar_money,
    svg_nafes_spinner,
    svg_number_strip,
)

LEVEL = "Grade 3"


# ==============================================================================
# Grade 3 Primary Bespoke SVG Diagram Helpers (XML-Validated via _wrap_nafes_svg)
# ==============================================================================


def svg_g3_number_line(
    ticks: list[tuple[float, str]],
    mark_pos: float = None,
    mark_lbl: str = "",
    arc: tuple[float, float, str] = None,
    lo: float = 0.0,
    hi: float = 100.0,
) -> str:
    """Calibrated horizontal number line for rounding, fractions, skip-counting, and timelines."""
    w, h = 380, 118
    x0, x1, y = 36, 344, 68
    span = max(1e-6, float(hi - lo))
    sx = lambda v: x0 + (float(v) - lo) / span * (x1 - x0)
    parts = [
        f'<line x1="{x0 - 10}" y1="{y}" x2="{x1 + 10}" y2="{y}" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{x0 - 14},{y} {x0 - 6},{y - 4} {x0 - 6},{y + 4}" fill="{STROKE}"/>',
        f'<polygon points="{x1 + 14},{y} {x1 + 6},{y - 4} {x1 + 6},{y + 4}" fill="{STROKE}"/>',
    ]
    for tv, tlbl in ticks:
        xv = sx(tv)
        parts.append(f'<line x1="{xv:.2f}" y1="{y - 6}" x2="{xv:.2f}" y2="{y + 6}" stroke="{STROKE}" stroke-width="1.7"/>')
        if tlbl:
            parts.append(f'<text x="{xv:.2f}" y="{y + 22}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(tlbl)}</text>')
    if arc is not None:
        xa, xb, albl = sx(arc[0]), sx(arc[1]), arc[2]
        xm = (xa + xb) / 2
        parts.append(f'<path d="M {xa:.2f},{y - 6} Q {xm:.2f},{y - 42} {xb:.2f},{y - 6}" fill="none" stroke="{BLUE}" stroke-width="2"/>')
        parts.append(f'<circle cx="{xb:.2f}" cy="{y - 6}" r="3" fill="{BLUE}"/>')
        parts.append(f'<text x="{xm:.2f}" y="{y - 29}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{BLUE}">{esc(albl)}</text>')
    if mark_pos is not None:
        xm = sx(mark_pos)
        parts.append(f'<circle cx="{xm:.2f}" cy="{y}" r="5.5" fill="{RED}" stroke="#ffffff" stroke-width="1.5"/>')
        if mark_lbl:
            parts.append(f'<text x="{xm:.2f}" y="{y - 13}" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(mark_lbl)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_equal_groups(groups: int, per_group: int, mode: str = "groups", caption: str = "") -> str:
    """Visual equal groups in baskets or a rectangular dot array for Grade 3 multiplication/division."""
    groups = max(1, min(10, groups))
    per_group = max(0, min(10, per_group))
    if mode == "array":
        r_cnt, c_cnt = groups, max(1, per_group)
        sp = min(22, int(130 / max(r_cnt, c_cnt)))
        gw, gh = (c_cnt - 1) * sp + 32, (r_cnt - 1) * sp + 32
        w = max(250, gw + 64)
        h = gh + (48 if caption else 30)
        ox, oy = (w - gw) / 2, 14
        parts = [f'<rect x="{ox:.1f}" y="{oy}" width="{gw}" height="{gh}" rx="9" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.6"/>']
        if per_group > 0:
            for r in range(r_cnt):
                for c in range(c_cnt):
                    cx = ox + 16 + c * sp
                    cy = oy + 16 + r * sp
                    parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{max(4.5, sp * 0.28):.1f}" fill="#93c5fd" stroke="{BLUE}" stroke-width="1.5"/>')
        if caption:
            parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(caption)}</text>')
        return _wrap_nafes_svg(w, h, "".join(parts))

    cols = min(5, groups)
    rows = (groups + cols - 1) // cols
    bw, bh = 62, 50
    w = max(250, cols * 72 + 24)
    h = rows * 58 + (38 if caption else 18)
    parts = []
    for g in range(groups):
        gr, gc = divmod(g, cols)
        bx = (w - (cols * 72 - 10)) / 2 + gc * 72
        by = 12 + gr * 58
        parts.append(f'<rect x="{bx:.1f}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="#fefce8" stroke="{ORANGE}" stroke-width="1.6"/>')
        dcols = min(5, max(1, per_group))
        for k in range(per_group):
            dr, dc = divmod(k, dcols)
            dx = bx + (bw - (dcols - 1) * 11) / 2 + dc * 11
            dy = by + (17 if per_group > 5 else 25) + dr * 15
            parts.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="4.2" fill="#86efac" stroke="{GREEN}" stroke-width="1.3"/>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_equation_balance(left_lbl: str, right_lbl: str, caption: str = "") -> str:
    """Two-pan primary classroom balance scale showing equal expressions."""
    w, h = 340, (152 if caption else 134)
    cx, yb = 170, 74
    parts = [
        f'<polygon points="{cx},{yb + 2} {cx - 22},{yb + 46} {cx + 22},{yb + 46}" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<rect x="{cx - 42}" y="{yb + 46}" width="84" height="8" rx="3" fill="{STROKE}"/>',
        f'<line x1="56" y1="{yb}" x2="284" y2="{yb}" stroke="{STROKE}" stroke-width="3" stroke-linecap="round"/>',
        f'<circle cx="{cx}" cy="{yb}" r="4.5" fill="{ORANGE}" stroke="{STROKE}" stroke-width="1.4"/>',
    ]
    for px, lbl, fc, sc in [(86, left_lbl, "#fef3c7", ORANGE), (254, right_lbl, "#dcfce7", GREEN)]:
        parts.append(f'<line x1="{px - 36}" y1="{yb}" x2="{px + 36}" y2="{yb}" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<rect x="{px - 44}" y="{yb - 36}" width="88" height="32" rx="6" fill="{fc}" stroke="{sc}" stroke-width="1.7"/>')
        parts.append(f'<text x="{px}" y="{yb - 15}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(lbl)}</text>')
    if caption:
        parts.append(f'<text x="{cx}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_metric_card(kind: str, main_lbl: str, sub_lbl: str = "", fill_frac: float = 0.6) -> str:
    """Everyday Grade 3 metric visual: length ruler, mass scale, or liquid beaker."""
    w, h = 320, 148
    parts = []
    if kind == "length":
        parts.append(f'<rect x="30" y="68" width="260" height="38" rx="4" fill="#fef08a" stroke="{STROKE}" stroke-width="1.7"/>')
        for i in range(21):
            tx = 40 + i * 12
            th = 14 if i % 5 == 0 else 8
            parts.append(f'<line x1="{tx}" y1="68" x2="{tx}" y2="{68 + th}" stroke="{STROKE}" stroke-width="1.3"/>')
        bar_w = max(48, min(236, int(236 * max(0.2, min(1.0, fill_frac)))))
        parts.append(f'<rect x="40" y="34" width="{bar_w}" height="20" rx="5" fill="#93c5fd" stroke="{BLUE}" stroke-width="1.6"/>')
        parts.append(f'<text x="{40 + bar_w / 2:.1f}" y="26" text-anchor="middle" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(main_lbl)}</text>')
    elif kind == "mass":
        lcd_fs = 11.5 if len(str(main_lbl)) > 11 else 12.5
        parts.append(f'<rect x="86" y="72" width="148" height="46" rx="10" fill="#e0f2fe" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(f'<rect x="102" y="84" width="116" height="24" rx="4" fill="#ffffff" stroke="{BLUE}" stroke-width="1.4"/>')
        parts.append(f'<text x="160" y="101" text-anchor="middle" font-size="{lcd_fs}" font-weight="800" fill="{RED}">{esc(main_lbl)}</text>')
        parts.append(f'<line x1="112" y1="62" x2="208" y2="62" stroke="{STROKE}" stroke-width="3"/>')
        parts.append(f'<line x1="160" y1="62" x2="160" y2="72" stroke="{STROKE}" stroke-width="3"/>')
        parts.append(f'<rect x="130" y="28" width="60" height="34" rx="6" fill="#fde68a" stroke="{ORANGE}" stroke-width="1.7"/>')
    else:
        jx, jy, jw, jh = 114, 22, 84, 94
        wh = max(8.0, min(1.0, fill_frac) * (jh - 8))
        parts.append(f'<rect x="{jx + 2}" y="{jy + jh - wh:.1f}" width="{jw - 4}" height="{wh:.1f}" rx="3" fill="#bae6fd"/>')
        parts.append(f'<rect x="{jx}" y="{jy}" width="{jw}" height="{jh}" rx="5" fill="none" stroke="{STROKE}" stroke-width="2"/>')
        for tk in (0.25, 0.5, 0.75):
            ty = jy + jh - tk * (jh - 8)
            parts.append(f'<line x1="{jx}" y1="{ty:.1f}" x2="{jx + 14}" y2="{ty:.1f}" stroke="{STROKE}" stroke-width="1.3"/>')
        parts.append(f'<text x="{jx + jw + 12}" y="{jy + 52}" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(main_lbl)}</text>')
    if sub_lbl:
        parts.append(f'<text x="160" y="136" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(sub_lbl)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_grid_rect(
    cols: int,
    rows: int,
    shaded_cells: list[tuple[int, int]] = None,
    top_lbl: str = "",
    side_lbl: str = "",
    caption: str = "",
) -> str:
    """Unit-square grid with shaded rectangle or composite rectilinear figure."""
    cols = max(1, min(12, cols))
    rows = max(1, min(9, rows))
    u = min(26, int(132 / max(cols, rows)))
    gw, gh = cols * u, rows * u
    w = max(260, gw + 96)
    h = gh + (58 if caption else 42)
    ox, oy = (w - gw) / 2, 24
    sset = set(shaded_cells) if shaded_cells is not None else {(c, r) for c in range(cols) for r in range(rows)}
    parts = []
    for r in range(rows):
        for c in range(cols):
            fc = "#bfdbfe" if (c, r) in sset else "#f8fafc"
            sc = STROKE if (c, r) in sset else GRID
            sw = "1.7" if (c, r) in sset else "1"
            parts.append(f'<rect x="{ox + c * u:.1f}" y="{oy + r * u:.1f}" width="{u}" height="{u}" fill="{fc}" stroke="{sc}" stroke-width="{sw}"/>')
    if top_lbl:
        parts.append(f'<text x="{ox + gw / 2:.1f}" y="{oy - 7}" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(top_lbl)}</text>')
    if side_lbl:
        parts.append(f'<text x="{ox + gw + 10:.1f}" y="{oy + gh / 2 + 4:.1f}" font-size="12" font-weight="800" fill="{ORANGE}">{esc(side_lbl)}</text>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_solid_3d(kind: str, caption: str = "") -> str:
    """Clean 3D solid diagrams for Grade 3: cube, prism, pyramid, cylinder, cone, sphere."""
    w, h = 260, (176 if caption else 156)
    parts = []
    if kind in ("cube", "prism"):
        fw = 68 if kind == "cube" else 98
        fh = 68 if kind == "cube" else 58
        dx, dy = 26, -20
        x0, y0 = (w - fw - dx) / 2, 46
        parts.extend([
            f'<polygon points="{x0},{y0} {x0 + dx},{y0 + dy} {x0 + fw + dx},{y0 + dy} {x0 + fw},{y0}" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<polygon points="{x0 + fw},{y0} {x0 + fw + dx},{y0 + dy} {x0 + fw + dx},{y0 + fh + dy} {x0 + fw},{y0 + fh}" fill="#93c5fd" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<rect x="{x0}" y="{y0}" width="{fw}" height="{fh}" fill="#eff6ff" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<line x1="{x0}" y1="{y0 + fh}" x2="{x0 + dx}" y2="{y0 + fh + dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
            f'<line x1="{x0 + dx}" y1="{y0 + dy}" x2="{x0 + dx}" y2="{y0 + fh + dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
            f'<line x1="{x0 + dx}" y1="{y0 + fh + dy}" x2="{x0 + fw + dx}" y2="{y0 + fh + dy}" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
        ])
    elif kind == "pyramid":
        ax, ay = 130, 24
        b1, b2, b3, b4 = (76, 118), (156, 118), (186, 94), (106, 94)
        parts.extend([
            f'<polygon points="{ax},{ay} {b1[0]},{b1[1]} {b2[0]},{b2[1]}" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<polygon points="{ax},{ay} {b2[0]},{b2[1]} {b3[0]},{b3[1]}" fill="#fde68a" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<line x1="{b1[0]}" y1="{b1[1]}" x2="{b4[0]}" y2="{b4[1]}" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="3,3"/>',
            f'<line x1="{b4[0]}" y1="{b4[1]}" x2="{b3[0]}" y2="{b3[1]}" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="3,3"/>',
            f'<line x1="{ax}" y1="{ay}" x2="{b4[0]}" y2="{b4[1]}" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="3,3"/>',
        ])
    elif kind == "cylinder":
        cx, yt, yb, rx, ry = 130, 38, 116, 48, 14
        parts.extend([
            f'<rect x="{cx - rx}" y="{yt}" width="{2 * rx}" height="{yb - yt}" fill="#dcfce7" stroke="none"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,0 {cx + rx},{yb}" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,1 {cx + rx},{yb}" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
            f'<line x1="{cx - rx}" y1="{yt}" x2="{cx - rx}" y2="{yb}" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<line x1="{cx + rx}" y1="{yt}" x2="{cx + rx}" y2="{yb}" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<ellipse cx="{cx}" cy="{yt}" rx="{rx}" ry="{ry}" fill="#bbf7d0" stroke="{STROKE}" stroke-width="1.8"/>',
        ])
    elif kind == "cone":
        cx, ay, yb, rx, ry = 130, 24, 116, 50, 14
        parts.extend([
            f'<polygon points="{cx},{ay} {cx - rx},{yb} {cx + rx},{yb}" fill="#fce7f3" stroke="none"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,0 {cx + rx},{yb}" fill="#fce7f3" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,1 {cx + rx},{yb}" fill="none" stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3,3"/>',
            f'<line x1="{cx}" y1="{ay}" x2="{cx - rx}" y2="{yb}" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<line x1="{cx}" y1="{ay}" x2="{cx + rx}" y2="{yb}" stroke="{STROKE}" stroke-width="1.8"/>',
        ])
    else:
        cx, cy, r = 130, 78, 48
        parts.extend([
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e0e7ff" stroke="{STROKE}" stroke-width="1.8"/>',
            f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="15" fill="none" stroke="{BLUE}" stroke-width="1.3" stroke-dasharray="4,3"/>',
        ])
    if caption:
        parts.append(f'<text x="130" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_symmetry_fig(kind: str, show_line: str = "V", caption: str = "") -> str:
    """2D symmetry & congruence visual with optional dashed line(s) of symmetry."""
    w, h = 270, (172 if caption else 152)
    cx, cy = 135, 76
    parts = []
    if kind == "isosceles_tri":
        parts.append(f'<polygon points="{cx},24 {cx - 56},126 {cx + 56},126" fill="#dbeafe" stroke="{STROKE}" stroke-width="2"/>')
    elif kind == "rectangle":
        parts.append(f'<rect x="{cx - 64}" y="{cy - 38}" width="128" height="76" fill="#dcfce7" stroke="{STROKE}" stroke-width="2"/>')
    elif kind == "square":
        parts.append(f'<rect x="{cx - 46}" y="{cy - 46}" width="92" height="92" fill="#fef3c7" stroke="{STROKE}" stroke-width="2"/>')
    elif kind == "butterfly":
        parts.append(
            f'<polygon points="{cx},46 {cx - 56},24 {cx - 46},76 {cx - 52},122 {cx},98 '
            f'{cx + 52},122 {cx + 46},76 {cx + 56},24" fill="#f3e8ff" stroke="{STROKE}" stroke-width="1.9"/>'
        )
    elif kind == "L_tile":
        parts.append(f'<polygon points="88,28 124,28 124,94 182,94 182,126 88,126" fill="#ffedd5" stroke="{STROKE}" stroke-width="2"/>')
    elif kind == "congruent_pair":
        parts.append(f'<rect x="44" y="44" width="66" height="66" fill="#dbeafe" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<rect x="160" y="44" width="66" height="66" fill="#dbeafe" stroke="{STROKE}" stroke-width="2"/>')
    elif kind == "non_congruent_pair":
        parts.append(f'<rect x="44" y="38" width="76" height="76" fill="#dbeafe" stroke="{STROKE}" stroke-width="2"/>')
        parts.append(f'<rect x="166" y="56" width="44" height="44" fill="#fef3c7" stroke="{STROKE}" stroke-width="2"/>')
    else:
        parts.append(f'<polygon points="74,56 146,56 146,34 198,76 146,118 146,96 74,96" fill="#ccfbf1" stroke="{STROKE}" stroke-width="2"/>')

    if show_line in ("V", "BOTH", "ALL4"):
        parts.append(f'<line x1="{cx}" y1="14" x2="{cx}" y2="138" stroke="{RED}" stroke-width="2" stroke-dasharray="5,4"/>')
    if show_line in ("H", "BOTH", "ALL4"):
        parts.append(f'<line x1="52" y1="{cy}" x2="218" y2="{cy}" stroke="{RED}" stroke-width="2" stroke-dasharray="5,4"/>')
    if show_line in ("DIAG", "ALL4"):
        parts.append(f'<line x1="{cx - 56}" y1="{cy - 56}" x2="{cx + 56}" y2="{cy + 56}" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5,4"/>')
    if show_line == "ALL4":
        parts.append(f'<line x1="{cx + 56}" y1="{cy - 56}" x2="{cx - 56}" y2="{cy + 56}" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5,4"/>')
    if caption:
        parts.append(f'<text x="{cx}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_tally_table(cat_header: str, rows: list[tuple[str, int]], hide_idx: int = -1) -> str:
    """Authentic Grade 3 tally chart drawing crossed 5-bundles and single strokes."""
    w = 350
    rh = 30
    h = (len(rows) + 1) * rh + 28
    x0, y0 = 16, 14
    tw, th = w - 32, (len(rows) + 1) * rh
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{tw}" height="{th}" rx="8" fill="#ffffff" stroke="{STROKE}" stroke-width="1.6"/>',
        f'<rect x="{x0}" y="{y0}" width="{tw}" height="{rh}" rx="8" fill="#e0f2fe" stroke="{STROKE}" stroke-width="1.4"/>',
        f'<line x1="128" y1="{y0}" x2="128" y2="{y0 + th}" stroke="{GRID}" stroke-width="1.3"/>',
        f'<text x="72" y="{y0 + 19}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(cat_header)}</text>',
        f'<text x="230" y="{y0 + 19}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">Tally</text>',
    ]
    for idx, (lbl, cnt) in enumerate(rows):
        ry = y0 + (idx + 1) * rh
        parts.append(f'<line x1="{x0}" y1="{ry}" x2="{x0 + tw}" y2="{ry}" stroke="{GRID}" stroke-width="1.1"/>')
        parts.append(f'<text x="72" y="{ry + 19}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
        if idx == hide_idx:
            parts.append(f'<text x="230" y="{ry + 20}" text-anchor="middle" font-size="14" font-weight="800" fill="{RED}">?</text>')
            continue
        bundles, rem = divmod(max(0, min(29, cnt)), 5)
        bx = 142
        for b in range(bundles):
            gx = bx + b * 32
            for s_i in range(4):
                parts.append(f'<line x1="{gx + s_i * 5}" y1="{ry + 7}" x2="{gx + s_i * 5}" y2="{ry + 23}" stroke="{BLUE}" stroke-width="1.9"/>')
            parts.append(f'<line x1="{gx - 3}" y1="{ry + 21}" x2="{gx + 18}" y2="{ry + 9}" stroke="{RED}" stroke-width="1.9"/>')
        rx_s = bx + bundles * 32
        for s_i in range(rem):
            parts.append(f'<line x1="{rx_s + s_i * 5}" y1="{ry + 7}" x2="{rx_s + s_i * 5}" y2="{ry + 23}" stroke="{BLUE}" stroke-width="1.9"/>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g3_marble_bag(counts: list[tuple[str, int, str]], caption: str = "") -> str:
    """Clear marble jar with colored marbles and legend for Grade 3 probability."""
    w, h = 330, (170 if caption else 152)
    parts = [
        f'<rect x="28" y="24" width="128" height="110" rx="18" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="54" y="14" width="76" height="12" rx="4" fill="#cbd5e1" stroke="{STROKE}" stroke-width="1.5"/>',
    ]
    marbles = []
    for lbl, cnt, col in counts:
        marbles.extend([col] * max(0, cnt))
    for idx, col in enumerate(marbles[:15]):
        r, c = divmod(idx, 5)
        mx = 48 + c * 22
        my = 112 - r * 24
        parts.append(f'<circle cx="{mx}" cy="{my}" r="8.5" fill="{col}" stroke="{STROKE}" stroke-width="1.4"/>')
    for idx, (lbl, cnt, col) in enumerate(counts):
        ly = 44 + idx * 28
        parts.append(f'<circle cx="186" cy="{ly - 4}" r="7.5" fill="{col}" stroke="{STROKE}" stroke-width="1.4"/>')
        parts.append(f'<text x="202" y="{ly}" font-size="12" font-weight="700" fill="{STROKE}">{esc(f"{lbl}: {cnt}")}</text>')
    if caption:
        parts.append(f'<text x="165" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


# ==============================================================================
# Lesson 1.1 (NAFS-L1-01) & Lesson 1.2 (NAFS-L1-02)
# ==============================================================================


def _lesson_1_1() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-01",
        level=LEVEL,
        unit_num="1.1",
        topic="Numbers & Operations",
        title_en="4-Digit Place Value, Rounding & Regrouping Addition/Subtraction",
        title_ar="القيمة المنزلية حتى الألوف، التقريب، والجمع والطرح بإعادة التجميع",
        summary_en=(
            "Welcome to Grade 3 Nafes! Master how 4-digit numbers up to 9,999 are built from thousands, "
            "hundreds, tens, and ones, how to compare and round numbers cleanly on a number line, and "
            "how to add with regrouping or subtract smoothly across zeros."
        ),
        summary_ar=(
            "أهلاً بك في رحلة التفوق في اختبار نافس للصف الثالث الابتدائي! سنتعلّم كيف تتكوّن الأعداد حتى 9,999 "
            "من آحاد وعشرات ومئات وألوف، وكيف نقارن الأعداد ونقرّبها على خط الأعداد، وكيف نجمع ونطرح بإعادة التجميع بثقة."
        ),
        goals_en=[
            "Read, write, and decompose **4-digit numbers** into standard, word, and expanded form.",
            "Compare and order 3-digit and 4-digit numbers and **round** to the nearest 10, 100, or 1,000.",
            "Solve **multi-digit addition** with regrouping and two-step primary story totals.",
            "Subtract **across zeros** accurately and check answers using inverse addition.",
        ],
        goals_ar=[
            "قراءة وكتابة وتحليل **الأعداد المكوّنة من 4 أرقام** بالصيغ القياسية واللفظية والتحليلية.",
            "مقارنة وترتيب الأعداد وتقريبها إلى **أقرب 10 أو 100 أو 1,000**.",
            "إتقان **الجمع بإعادة التجميع** وحل المسائل اللفظية الحياتية من خطوتين.",
            "تنفيذ **الطرح عبر الأصفار** بدقة والتحقق من صحة الناتج باستعمال الجمع العكسي.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Thousands, Hundreds, Tens & Ones in Expanded Form",
                title_ar="١. الآحاد والعشرات والمئات والألوف والصيغة التحليلية",
                body_en=(
                    f"Every digit in a 4-digit number has a **place** and a **value**. In {m('3,426')}, the digit {m(3)} "
                    f"stands in the thousands place so its value is {m(3000)}, {m(4)} is worth {m(400)}, {m(2)} is worth {m(20)}, "
                    f"and {m(6)} is worth {m(6)}. If a place has {m(0)}, keep that zero in standard form as a placeholder!"
                ),
                body_ar=(
                    f"لكل رقم في العدد الرباعي **اسم منزلة** و**قيمة منزلية**. في العدد {m('3,426')} يقع الرقم {m(3)} في منزلة الألوف "
                    f"فقيمته {m(3000)}، وقيمة {m(4)} هي {m(400)}، وقيمة {m(2)} هي {m(20)}، وقيمة {m(6)} هي {m(6)}. "
                    f"وإذا خلت منزلة من الوحدات نكتب فيها صفراً {m(0)} لحفظ المنزلة في الصيغة القياسية."
                ),
                formula_en=dm("3{,}426 = 3000 + 400 + 20 + 6"),
                caption_ar="الصيغة التحليلية للعدد من أربعة أرقام:",
                formula_math_ar=dm("3{,}426 = 3000 + 400 + 20 + 6"),
                diagram_en=svg_nafes_place_value_blocks(3, 4, 2, 6, "3,426 = 3000 + 400 + 20 + 6"),
            ),
            nafes_concept(
                title_en="2. Comparing Left-to-Right & the Halfway Rounding Rule",
                title_ar="٢. المقارنة من اليسار وقاعدة المنتصف في التقريب",
                body_en=(
                    f"To compare two whole numbers, first count their digits—any 4-digit number beats any 3-digit number! "
                    f"If both have 4 digits, compare from the **leftmost (thousands) place**. To round, look one place to the right: "
                    f"if that neighbor digit is {m('0, 1, 2, 3,')} or {m(4)}, stay down; if it is {m('5, 6, 7, 8,')} or {m(9)}, round up!"
                ),
                body_ar=(
                    f"لمقارنة عددين نعدّ أرقامهما أولاً؛ فالعدد الرباعي أكبر دائماً من الثلاثي. وإذا تساوى عدد الأرقام نقارن بدءاً من **أقصى اليسار (الألوف)**. "
                    f"وعند التقريب ننظر إلى الرقم عن يمين المنزلة المطلوبة: إذا كان {m('0,1,2,3,4')} يبقى الرقم كما هو، وإذا كان {m('5,6,7,8,9')} نضيف {m(1)} ونصفّر اليمين."
                ),
                formula_en=dm("470 \\xrightarrow{\\text{nearest } 100} 500 \\quad (\\text{tens digit } 7 \\ge 5)"),
                caption_ar="مثال التقريب إلى أقرب مئة على خط الأعداد:",
                formula_math_ar=dm("470 \\longrightarrow 500"),
                diagram_en=svg_g3_number_line(
                    [(400, "400"), (450, "450"), (500, "500")],
                    mark_pos=470,
                    mark_lbl="470 -> 500",
                    lo=400,
                    hi=500,
                ),
            ),
            nafes_concept(
                title_en="3. Regrouping in Addition & Subtracting Across Zeros",
                title_ar="٣. الجمع بإعادة التجميع والطرح عبر الأصفار",
                body_en=(
                    f"Whenever ones add up to {m(10)} or more, trade {m(10)} ones for {m(1)} ten; trade {m(10)} tens for {m(1)} hundred. "
                    f"When subtracting across zeros such as {m('600 - 247')}, think of {m(600)} as {m(60)} tens: borrow {m(1)} ten to turn "
                    f"the middle and right columns into {m(5)} hundreds, {m(9)} tens, and {m(10)} ones!"
                ),
                body_ar=(
                    f"عندما يصل مجموع الآحاد إلى {m(10)} أو أكثر نعيد تجميع {m(10)} آحاد في صورة {m(1)} عشرة، وكذلك {m(10)} عشرات في صورة {m(1)} مئة. "
                    f"وفي الطرح عبر الأصفار مثل {m('600 - 247')}، نفكّ {m(6)} مئات إلى {m(5)} مئات و{m(9)} عشرات و{m(10)} آحاد ثم نطرح بسهولة!"
                ),
                formula_en=dm("468 + 275 = 743, \\qquad 600 - 247 = 353"),
                caption_ar="الجمع العمودي بإعادة التجميع والطرح عبر الأصفار:",
                formula_math_ar=dm("468 + 275 = 743, \\qquad 600 - 247 = 353"),
                diagram_en=svg_column_cryptarithm(["468", "275"], "743"),
            ),
        ],
        traps_en=[
            "Confusing place name with digit value: in 5,732, the digit 7 is in the hundreds place, so its value is 700, NOT 7.",
            "Dropping placeholder zeros from expanded form: 4000 + 80 + 3 equals 4,083, NOT 483.",
            "Flipping subtraction across zeros: in 500 − 164, never do 6 − 0 = 6 and 4 − 0 = 4; regroup 500 as 4 hundreds, 9 tens, and 10 ones to get 336.",
        ],
        traps_ar=[
            "الخلط بين اسم المنزلة والقيمة المنزلية: في العدد 5,732 الرقم 7 في منزلة المئات فقيمته 700 وليست 7.",
            "نسيان صفر حفظ المنزلة: الصيغة 4000 + 80 + 3 تساوي 4,083 وليس 483 لأن منزلة المئات صفر.",
            "عكس الطرح عند وجود الأصفار: في 500 − 164 لا نطرح الصفر من 4 أو 6، بل نعيد تجميع 500 إلى 4 مئات و9 عشرات و10 آحاد فيكون الناتج 336.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-01-EX1",
                title_en="Standard Form with a Zero Hundred",
                title_ar="الصيغة القياسية مع صفر في المئات",
                q_en=f"Salman builds a number using {m(2)} thousands blocks, {m(0)} hundreds blocks, {m(5)} tens rods, and {m(8)} ones cubes. How is Salman's number written in standard form?",
                q_ar=f"كوّن سلمان عدداً باستعمال {m(2)} من مكعبات الألوف و{m(0)} من المئات و{m(5)} من أعمدة العشرات و{m(8)} من وحدات الآحاد. كيف يُكتب عدد سلمان بالصيغة القياسية؟",
                correct_val=2058,
                distractors=[258, 2508, 2580],
                idea_en="Place each digit into its matching column from thousands down to ones, keeping 0 in the empty hundreds spot.",
                steps_en=[
                    f"Thousands = {m(2)}, Hundreds = {m(0)}, Tens = {m(5)}, Ones = {m(8)}.",
                    f"Add the values: {m('2000 + 0 + 50 + 8 = 2058')}.",
                ],
                check_en=f"{m('2058')} has {m(4)} digits and shows {m(0)} hundreds cleanly.",
                idea_ar="نضع كل رقم في منزلته من الألوف حتى الآحاد مع وضع 0 لحفظ منزلة المئات الخالية.",
                steps_ar=[
                    f"الألوف = {m(2)}، المئات = {m(0)}، العشرات = {m(5)}، الآحاد = {m(8)}.",
                    f"نجمع القيم المنزلية: {m('2000 + 0 + 50 + 8 = 2058')}.",
                ],
                check_ar=f"العدد {m('2058')} مكوّن من 4 أرقام ورقم مئاته {m(0)}.",
                diagram_en=svg_nafes_place_value_blocks(2, 0, 5, 8, "2 thousands, 0 hundreds, 5 tens, 8 ones"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-01-EX2",
                title_en="Rounding Visitors to the Nearest Hundred",
                title_ar="تقريب عدد الزوار إلى أقرب مئة",
                q_en=f"On Thursday, {m(1652)} students visited the Riyadh Book Fair corner. What is {m(1652)} rounded to the nearest hundred?",
                q_ar=f"زار ركن القراءة في معرض الرياض للكتاب {m(1652)} طالباً يوم الخميس. ما تقريب العدد {m(1652)} إلى أقرب مئة؟",
                correct_val=1700,
                distractors=[1600, 1650, 2000],
                idea_en="Underline the hundreds digit and inspect the tens digit right beside it.",
                steps_en=[
                    f"In {m(1652)}, the hundreds digit is {m(6)} and the tens digit to its right is {m(5)}.",
                    f"Because {m('5 \\ge 5')}, round the hundreds digit up from {m(6)} to {m(7)} and replace tens and ones with zeros: {m(1700)}.",
                ],
                check_en=f"On a number line between {m(1600)} and {m(1700)}, {m(1652)} is past the halfway mark {m(1650)}.",
                idea_ar="نحدّد منزلة المئات وننظر إلى رقم العشرات على يمينها.",
                steps_ar=[
                    f"في العدد {m(1652)} رقم المئات هو {m(6)} ورقم العشرات عن يمينه هو {m(5)}.",
                    f"بما أن {m('5 \\ge 5')} نضيف {m(1)} إلى المئات فتصبح {m(7)} ونضع أصفاراً يمينها فنحصل على {m(1700)}.",
                ],
                check_ar=f"العدد {m(1652)} يتجاوز نقطة المنتصف {m(1650)} فهو أقرب إلى {m(1700)}.",
                diagram_en=svg_g3_number_line(
                    [(1600, "1600"), (1650, "1650"), (1700, "1700")],
                    mark_pos=1652,
                    mark_lbl="1652",
                    lo=1600,
                    hi=1700,
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-01-EX3",
                title_en="Two-Day Date Harvest Addition",
                title_ar="جمع محصول التمور في يومين",
                q_en=f"An Al-Qassim farm packed {m(376)} boxes of Sukkari dates in the morning and {m(285)} boxes in the afternoon. How many boxes did the farm pack in all?",
                q_ar=f"عبّأت مزرعة في القصيم {m(376)} صندوق تمر سكري صباحاً و{m(285)} صندوقاً مساءً. كم صندوقاً عبّأت المزرعة في اليوم كله؟",
                correct_val=661,
                distractors=[551, 651, 671],
                idea_en="Add column by column from right to left, regrouping ones into tens and tens into hundreds.",
                steps_en=[
                    f"Ones: {m('6 + 5 = 11')} -> write {m(1)} one and carry {m(1)} ten.",
                    f"Tens: {m('7 + 8 + 1 = 16')} tens -> write {m(6)} tens and carry {m(1)} hundred.",
                    f"Hundreds: {m('3 + 2 + 1 = 6')} hundreds -> total {m(661)}.",
                ],
                check_en=f"Estimate: {m('380 + 290 = 670')}, which is very close to {m(661)}.",
                idea_ar="نجمع عمودياً من الآحاد إلى المئات مع إعادة التجميع في كل منزلة تحتاج لذلك.",
                steps_ar=[
                    f"الآحاد: {m('6 + 5 = 11')}، نكتب {m(1)} ونعيد تجميع {m(1)} عشرة.",
                    f"العشرات: {m('7 + 8 + 1 = 16')} عشرة، نكتب {m(6)} ونعيد تجميع {m(1)} مئة.",
                    f"المئات: {m('3 + 2 + 1 = 6')} مئات، فيكون المجموع {m(661)}.",
                ],
                check_ar=f"التحقق بالطرح: {m('661 - 285 = 376')}.",
                diagram_en=svg_column_cryptarithm(["376", "285"], "?"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-01-EX4",
                title_en="School Library Subtraction Across Zeros",
                title_ar="طرح الكتب عبر الأصفار",
                q_en=f"A primary school library has {m(800)} storybooks. Students borrowed {m(346)} storybooks this week. How many storybooks remain on the shelves?",
                q_ar=f"في مكتبة المدرسة الابتدائية {m(800)} قصة، استعار الطلاب منها {m(346)} قصة هذا الأسبوع. كم قصة بقيت على الرفوف؟",
                correct_val=454,
                distractors=[446, 464, 546],
                idea_en="Regroup 800 as 7 hundreds, 9 tens, and 10 ones so every column can subtract cleanly.",
                steps_en=[
                    f"Rewrite {m(800)} as {m(7)} hundreds + {m(9)} tens + {m(10)} ones.",
                    f"Subtract each place: ones {m('10 - 6 = 4')}, tens {m('9 - 4 = 5')}, hundreds {m('7 - 3 = 4')}.",
                    f"Putting the digits together gives {m(454)}.",
                ],
                check_en=f"Inverse addition check: {m('454 + 346 = 800')}.",
                idea_ar="نفكّ 800 إلى 7 مئات و9 عشرات و10 آحاد ثم نطرح منزلةً بمنزلة.",
                steps_ar=[
                    f"نعيد تجميع {m(800)} ليصبح {m(7)} مئات و{m(9)} عشرات و{m(10)} آحاد.",
                    f"الآحاد {m('10 - 6 = 4')}، العشرات {m('9 - 4 = 5')}، والمئات {m('7 - 3 = 4')}.",
                    f"الناتج المتبقي هو {m(454)} قصة.",
                ],
                check_ar=f"التحقق بالجمع العكسي: {m('454 + 346 = 800')} بالضبط.",
                diagram_en=svg_number_strip(["800 total", "- 346 borrowed", "= ? left"]),
            ),
        ],
        blueprints=["G3-NUM-01", "G3-NUM-02", "G3-NUM-03", "G3-NUM-04"],
    )


def _lesson_1_2() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-02",
        level=LEVEL,
        unit_num="1.2",
        topic="Numbers & Operations",
        title_en="Equal Groups Multiplication, Division Sharing & Visual Fractions",
        title_ar="الضرب كشبكات ومجموعات متساوية، القسمة، والكسور الاعتيادية البصرية",
        summary_en=(
            "Discover how equal groups and neat rows turn repeated addition into fast multiplication, "
            "how division shares items fairly as the partner of multiplication, and how fraction strips "
            "help you name, compare, and add equal parts of a whole."
        ),
        summary_ar=(
            "اكتشف كيف تحوّل المجموعات المتساوية والشبكات المستطيلة الجمع المتكرر إلى ضرب سريع، "
            "وكيف توزّع القسمة الأشياء بالتساوي كعملية عكسية للضرب، وكيف تساعدك أشرطة الكسور على تسمية الكسور ومقارنتها وجمعها."
        ),
        goals_en=[
            "Model **multiplication (0–10)** using equal groups, repeated addition, and rectangular arrays.",
            "Solve **division** problems by equal sharing, equal grouping, and fact families.",
            "Identify **unit and proper fractions** of shaded shapes, fraction strips, and number lines.",
            "Compare fractions with the **same denominator or same numerator** and add like fractions.",
        ],
        goals_ar=[
            "تمثيل **حقائق الضرب (0–10)** باستعمال المجموعات المتساوية والجمع المتكرر والشبكات.",
            "حل مسائل **القسمة** بالتوزيع بالتساوي وتكوين المجموعات وعائلات الحقائق المترابطة.",
            "تمييز **كسور الوحدة والكسور الاعتيادية** في الأشكال المظللة وأشرطة الكسور وخط الأعداد.",
            "مقارنة الكسور ذات **المقام نفسه أو البسط نفسه** وجمع الكسور المتشابهة.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Equal Groups & Rectangular Arrays in Multiplication",
                title_ar="١. المجموعات المتساوية والشبكات في عملية الضرب",
                body_en=(
                    f"When every group holds the **same number** of items, we multiply! Four rows with {m(6)} counters in each row "
                    f"give {m('4 \\times 6 = 24')}. Swapping rows and columns keeps the total unchanged ({m('6 \\times 4 = 24')}). "
                    f"Also remember two special Grade 3 rules: multiplying by {m(1)} keeps a number the same, and multiplying by {m(0)} always gives {m(0)}!"
                ),
                body_ar=(
                    f"عندما تحتوي كل مجموعة على **العدد نفسه** من العناصر نستعمل الضرب! أربعة صفوف في كل منها {m(6)} قطع تعطي "
                    f"{m('4 \\times 6 = 24')}. وتبديل الصفوف والأعمدة لا يغيّر الناتج ({m('6 \\times 4 = 24')}). "
                    f"وتذكّر خاصيتين مهمتين: الضرب في {m(1)} يُبقي العدد كما هو، والضرب في {m(0)} يعطي {m(0)} دائماً!"
                ),
                formula_en=dm("4 \\text{ rows} \\times 6 \\text{ in each row} = 6 + 6 + 6 + 6 = 24"),
                caption_ar="تحويل الشبكة والجمع المتكرر إلى جملة ضرب:",
                formula_math_ar=dm("4 \\times 6 = 6 + 6 + 6 + 6 = 24"),
                diagram_en=svg_g3_equal_groups(4, 6, mode="array", caption="4 rows x 6 columns = 24"),
            ),
            nafes_concept(
                title_en="2. Fair Sharing Division & Inverse Fact Families",
                title_ar="٢. القسمة بالتساوي وعائلات الحقائق المترابطة",
                body_en=(
                    f"Division splits a total into **equal shares**. Sharing {m(15)} dates equally among {m(3)} baskets puts "
                    f"{m('15 \\div 3 = 5')} dates in each basket. Because division and multiplication are inverse partners, "
                    f"you can always solve {m('15 \\div 3 = \\square')} by asking: **what number times {m(3)} equals {m(15)}?**"
                ),
                body_ar=(
                    f"توزّع القسمة العدد الكلي إلى **حصص متساوية**. فتوزيع {m(15)} تمرة بالتساوي على {m(3)} سلال يضع "
                    f"{m('15 \\div 3 = 5')} تمرات في كل سلة. ولأن القسمة عكس الضرب، نحل {m('15 \\div 3 = \\square')} بالسؤال: "
                    f"**ما العدد الذي إذا ضربناه في {m(3)} كان الناتج {m(15)}؟**"
                ),
                formula_en=dm("3 \\times 5 = 15 \\;\\Longleftrightarrow\\; 15 \\div 3 = 5 \\;\\text{and}\\; 15 \\div 5 = 3"),
                caption_ar="عائلة الحقائق المترابطة للضرب والقسمة:",
                formula_math_ar=dm("3 \\times 5 = 15 \\;\\Longleftrightarrow\\; 15 \\div 3 = 5"),
                diagram_en=svg_g3_equal_groups(3, 5, mode="groups", caption="15 shared into 3 baskets = 5 each"),
            ),
            nafes_concept(
                title_en="3. Visual Fractions: Comparing & Adding Like Parts",
                title_ar="٣. الكسور البصرية: المقارنة وجمع الكسور المتشابهة",
                body_en=(
                    f"In a fraction {m('\\frac{\\text{top}}{\\text{bottom}}')}, the **denominator** (bottom) counts all **equal parts** in one whole, "
                    f"and the **numerator** (top) counts the shaded parts. With the **same denominator**, more parts mean a bigger fraction "
                    f"({m('\\frac{5}{8} > \\frac{3}{8}')}). With the **same numerator**, cutting into **fewer** pieces makes each piece **larger** "
                    f"({m('\\frac{1}{3} > \\frac{1}{6}')}). To add like fractions, add the numerators and keep the denominator!"
                ),
                body_ar=(
                    f"في الكسر يمثّل **المقام** (أسفل) عدد الأجزاء المتطابقة كلها في الواحد الصحيح، ويمثّل **البسط** (أعلى) عدد الأجزاء المظللة. "
                    f"إذا تساوى المقام فالبسط الأكبر هو الكسر الأكبر ({m('\\frac{5}{8} > \\frac{3}{8}')})، وإذا تساوى البسط فالمقام الأصغر يعطي قطعاً أكبر "
                    f"({m('\\frac{1}{3} > \\frac{1}{6}')}). وعند جمع كسرين متشابهين نجمع البسطين ويبقى المقام ثابتاً!"
                ),
                formula_en=dm("\\frac{2}{8} + \\frac{3}{8} = \\frac{2 + 3}{8} = \\frac{5}{8}"),
                caption_ar="جمع كسرين لهما المقام نفسه:",
                formula_math_ar=dm("\\frac{2}{8} + \\frac{3}{8} = \\frac{5}{8}"),
                diagram_en=svg_nafes_fraction_bars(3, 8, 5, 8, "3/8", "5/8"),
            ),
        ],
        traps_en=[
            "Zero multiplication slip: 8 × 0 is 0 (eight empty baskets hold 0 items), NOT 8!",
            "Bigger-bottom fraction trap: 1/8 is SMALLER than 1/4 because slicing one pie into 8 equal pieces makes tinier slices than slicing into 4.",
            "Adding denominators mistake: 2/6 + 3/6 equals 5/6, NEVER 5/12—the size of each sixth does not shrink when you combine slices!",
        ],
        traps_ar=[
            "خطأ الضرب في الصفر: ناتج 8 × 0 هو 0 (ثماني سلال فارغة ليس فيها شيء) وليس 8!",
            "فخ المقام الأكبر: الكسر 1/8 أصغر من 1/4 لأن تقسيم الفطيرة إلى 8 أجزاء يعطي قطعاً أصغر من تقسيمها إلى 4 أجزاء.",
            "جمع المقامين بالخطأ: ناتج 2/6 + 3/6 هو 5/6 وليس 5/12؛ فالمقام يصف حجم الجزء ويبقى ثابتاً.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-02-EX1",
                title_en="Classroom Chairs in a Rectangular Array",
                title_ar="كراسي الصف في شبكة مستطيلة",
                q_en=f"Students arranged chairs for a school assembly in {m(5)} equal rows with {m(7)} chairs in each row. How many chairs did they arrange altogether?",
                q_ar=f"رتّب الطلاب كراسي الإذاعة الصباحية في {m(5)} صفوف متساوية، وفي كل صف {m(7)} كراسي. كم كرسياً رتّبوا جميعاً؟",
                correct_val=35,
                distractors=[12, 30, 42],
                idea_en="Multiply the number of rows by the number of chairs in each row.",
                steps_en=[
                    f"Each of the {m(5)} rows has {m(7)} chairs.",
                    f"Multiply: {m('5 \\times 7 = 35')} chairs.",
                ],
                check_en=f"Skip-count by fives {m(7)} times: {m('5, 10, 15, 20, 25, 30, 35')}.",
                idea_ar="نضرب عدد الصفوف في عدد الكراسي في كل صف.",
                steps_ar=[
                    f"لدينا {m(5)} صفوف متساوية وفي كل صف {m(7)} كراسي.",
                    f"نحسب {m('5 \\times 7 = 35')} كرسياً.",
                ],
                check_ar=f"بالعد القفزي بالخمسات سبع مرات نحصل على {m(35)}.",
                diagram_en=svg_g3_equal_groups(5, 7, mode="array", caption="5 rows of 7 chairs"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-02-EX2",
                title_en="Sharing Colored Pencils Equally",
                title_ar="توزيع الأقلام الملونة بالتساوي",
                q_en=f"Teacher Noura shares {m(36)} colored pencils equally among {m(4)} art tables. How many pencils does each table get?",
                q_ar=f"وزّعت المعلمة نورة {m(36)} قلماً ملوناً بالتساوي على {m(4)} طاولات فنية. كم قلماً تأخذ كل طاولة؟",
                correct_val=9,
                distractors=[8, 7, 32],
                idea_en="Use the multiplication fact family of 4 to divide 36 into 4 equal groups.",
                steps_en=[
                    f"Write the division sentence: {m('36 \\div 4 = \\square')}.",
                    f"Recall that {m('4 \\times 9 = 36')}, so each table gets {m(9)} pencils.",
                ],
                check_en=f"{m('9 + 9 + 9 + 9 = 36')} pencils in total.",
                idea_ar="نستعمل حقيقة الضرب المترابطة للعدد 4 لإيجاد ناتج قسمة 36 على 4.",
                steps_ar=[
                    f"جملة القسمة هي {m('36 \\div 4 = \\square')}.",
                    f"بما أن {m('4 \\times 9 = 36')} فإن نصيب كل طاولة {m(9)} أقلام.",
                ],
                check_ar=f"التحقق بالجمع المتكرر: {m('9 + 9 + 9 + 9 = 36')}.",
                diagram_en=svg_g3_equal_groups(4, 9, mode="groups", caption="36 shared equally among 4 tables"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-02-EX3",
                title_en="Naming the Unshaded Fraction of a Strip",
                title_ar="تسمية الكسر غير المظلل في الشريط",
                q_en=f"A chocolate bar is divided into {m(8)} equal pieces, and Maysa eats {m(3)} shaded pieces. What fraction of the whole bar is **left unshaded**?",
                q_ar=f"قُسّم لوح شوكولاتة إلى {m(8)} قطع متطابقة، وأكلت ميساء {m(3)} قطع مظللة. ما الكسر الذي يمثّل الجزء **المتبقي غير المظلل** من اللوح؟",
                correct_val=Fraction(5, 8),
                distractors=[Fraction(3, 8), Fraction(3, 5), Fraction(5, 10)],
                idea_en="Subtract the eaten pieces from 8 total equal pieces, keeping 8 as the denominator.",
                steps_en=[
                    f"There are {m(8)} equal pieces in all, and {m('8 - 3 = 5')} pieces remain unshaded.",
                    f"Put {m(5)} in the numerator and {m(8)} in the denominator to get {m('\\frac{5}{8}')}.",
                ],
                check_en=f"{m('\\frac{3}{8} + \\frac{5}{8} = \\frac{8}{8} = 1')} whole bar.",
                idea_ar="نطرح القطع المأكولة من إجمالي 8 قطع متطابقة مع بقاء المقام 8.",
                steps_ar=[
                    f"إجمالي الأجزاء المتطابقة {m(8)}، والباقي غير المظلل {m('8 - 3 = 5')} أجزاء.",
                    f"نضع {m(5)} في البسط و{m(8)} في المقام فيكون الكسر المتبقي {m('\\frac{5}{8}')}.",
                ],
                check_ar=f"مجموع المظلل وغير المظلل {m('\\frac{3}{8} + \\frac{5}{8} = \\frac{8}{8} = 1')}.",
                diagram_en=svg_nafes_fraction_bars(3, 8, None, None, "3/8 eaten"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-02-EX4",
                title_en="Comparing Unit Fractions of Equal Pies",
                title_ar="مقارنة كسور الوحدة لفطائر متطابقة",
                q_en=f"Four identical pies are cut into equal slices. Which fraction represents the **largest** single slice?",
                q_ar=f"قُسّمت أربع فطائر متطابقة إلى أجزاء متساوية. أي كسر مما يلي يمثّل **أكبر** قطعة واحدة؟",
                correct_val=Fraction(1, 3),
                distractors=[Fraction(1, 4), Fraction(1, 6), Fraction(1, 8)],
                idea_en="When the numerator is 1, the smallest denominator gives the biggest slice.",
                steps_en=[
                    f"Compare denominators {m('3, 4, 6,')} and {m(8)}.",
                    f"Cutting a pie into only {m(3)} equal parts leaves bigger pieces than cutting into {m('4, 6,')} or {m(8)} parts, so {m('\\frac{1}{3}')} is largest.",
                ],
                check_en=f"On fraction strips: {m('\\frac{1}{3} > \\frac{1}{4} > \\frac{1}{6} > \\frac{1}{8}')}.",
                idea_ar="عندما يتساوى البسط عند 1 فإن المقام الأصغر يعطي الجزء الأكبر.",
                steps_ar=[
                    f"نقارن المقامات {m('3, 4, 6, 8')}.",
                    f"تقسيم الفطيرة إلى {m(3)} أجزاء فقط يعطي قطعة أكبر من تقسيمها إلى {m(4)} أو {m(6)} أو {m(8)} أجزاء، إذن {m('\\frac{1}{3}')} هو الأكبر.",
                ],
                check_ar=f"ترتيب الكسور من الأكبر للأصغر: {m('\\frac{1}{3} > \\frac{1}{4} > \\frac{1}{6} > \\frac{1}{8}')}.",
                diagram_en=svg_nafes_fraction_bars(1, 3, 1, 6, "1/3", "1/6"),
            ),
        ],
        blueprints=["G3-NUM-05", "G3-NUM-06", "G3-NUM-07", "G3-NUM-08"],
    )


# ==============================================================================
# Lesson 1.3 (NAFS-L1-03) & Lesson 1.4 (NAFS-L1-04)
# ==============================================================================


def _lesson_1_3() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-03",
        level=LEVEL,
        unit_num="1.3",
        topic="Algebra",
        title_en="Growing Patterns, Input-Output Function Tables & Missing-Number Sentences",
        title_ar="الأنماط العددية والبصرية، جداول المدخلات والمخرجات، والجمل العددية المفتوحة",
        summary_en=(
            "Spot the secret rule behind skip-counting sequences and tile designs! Learn how to check "
            "every row of an input-output machine table and use inverse operations or a classroom "
            "balance scale to uncover any missing number."
        ),
        summary_ar=(
            "اكتشف القاعدة السرية خلف الأنماط العددية وتصاميم البلاط المتنامية! سنتعلّم كيف نفحص كل صف "
            "في جدول المدخلات والمخرجات، وكيف نستعمل العملية العكسية أو كفتي الميزان لإيجاد العدد المفقود في الجمل العددية."
        ),
        goals_en=[
            "Extend **skip-counting and arithmetic number patterns** to find missing middle or next terms.",
            "Predict shapes and tile counts in **repeating visual cycles and growing step patterns**.",
            "Discover and apply **input-output rules** (+, −, ×, ÷) across function tables.",
            "Find unknown values in **missing-number sentences** and balanced toy scales.",
        ],
        goals_ar=[
            "توسيع **الأنماط العددية والعدّ القفزي** لإيجاد الحد المفقود في الوسط أو في النهاية.",
            "توقّع الشكل التالي وعدد المربعات في **الأنماط البصرية المتكررة والمتنامية**.",
            "استنتاج قاعدة **جداول المدخلات والمخرجات** بالجمع أو الطرح أو الضرب أو القسمة وتطبيقها.",
            "إيجاد العدد المفقود في **الجمل العددية المفتوحة** وموازين الألعاب المتعادلة.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Skip-Counting & Constant-Jump Number Patterns",
                title_ar="١. العدّ القفزي والأنماط العددية ذات القفزة الثابتة",
                body_en=(
                    f"To crack a number pattern, write the **jump** from each term to the next—check at least **two** "
                    f"neighbor pairs so you know the rule stays steady! In {m('14, 21, 28, \\square, 42')}, each step adds "
                    f"{m('+7')}, so the missing middle number is {m('28 + 7 = 35')}. If numbers shrink, subtract to find the step!"
                ),
                body_ar=(
                    f"لاكتشاف قاعدة النمط العددي نكتب **مقدار القفزة** بين كل عددين متجاورين، ونتحقق من **قفزتين على الأقل** للتأكد من ثبات القاعدة! "
                    f"في النمط {m('14, 21, 28, \\square, 42')} نزيد {m('+7')} في كل خطوة، فيكون العدد المفقود {m('28 + 7 = 35')}. وإذا تناقصت الأعداد نحسب الفرق بالطرح."
                ),
                formula_en=dm("14 \\xrightarrow{+7} 21 \\xrightarrow{+7} 28 \\xrightarrow{+7} 35 \\xrightarrow{+7} 42"),
                caption_ar="تتبّع القفزة الثابتة بين حدود النمط:",
                formula_math_ar=dm("14 \\xrightarrow{+7} 21 \\xrightarrow{+7} 28 \\xrightarrow{+7} 35 \\xrightarrow{+7} 42"),
                diagram_en=svg_number_strip(["14", "21", "28", "?", "42"]),
            ),
            nafes_concept(
                title_en="2. Repeating Visual Cycles & Growing Tile Steps",
                title_ar="٢. وحدة النمط المتكررة وأنماط البلاط المتنامية",
                body_en=(
                    f"Visual patterns come in two friendly types. A **repeating pattern** copies one core block over and over, "
                    f"such as **Circle, Circle, Star** (a cycle of {m(3)} shapes). A **growing pattern** adds the same number of "
                    f"tiles or sticks at every new step—count each step's total to turn the picture into a simple number pattern!"
                ),
                body_ar=(
                    f"للأنماط البصرية نوعان أساسيان: **نمط متكرر** يعيد **وحدة النمط** نفسها مراراً (مثل: دائرة، دائرة، نجمة بطول {m(3)} أشكال)، "
                    f"و**نمط متنامٍ** يضيف عدداً ثابتاً من المربعات أو الأعواد في كل خطوة جديدة—عدّ عناصر كل خطوة لتحوّل الرسم إلى نمط عددي سهل!"
                ),
                formula_en=dm("\\text{Step } 1: 4 \\text{ sticks}, \\quad \\text{Step } 2: 7 \\text{ sticks}, \\quad \\text{Step } 3: 10 \\text{ sticks } (+3)"),
                caption_ar="تحويل خطوات الرسم المتنامي إلى أعداد:",
                formula_math_ar=dm("4 \\xrightarrow{+3} 7 \\xrightarrow{+3} 10 \\xrightarrow{+3} 13"),
                diagram_en=svg_matchstick_squares((1, 2, 3)),
            ),
            nafes_concept(
                title_en="3. Input-Output Rule Tables & Balanced Sentences",
                title_ar="٣. جداول المدخلات والمخرجات والجمل العددية المتوازنة",
                body_en=(
                    f"In an **input-output table**, one hidden rule turns every Input into its Output—test your rule on **all** given rows! "
                    f"In a **missing-number sentence** like {m('\\square + 16 = 40')} or {m('6 \\times \\square = 42')}, the equals sign {m('=')} "
                    f"acts like a level balance scale: use the **inverse operation** ({m('40 - 16 = 24')} or {m('42 \\div 6 = 7')}) to solve!"
                ),
                body_ar=(
                    f"في **جدول المدخلات والمخرجات** تعمل قاعدة واحدة على جميع الصفوف، لذا اختبر قاعدتك على **كل صف معلوم** أولاً! "
                    f"وفي **الجملة العددية المفتوحة** مثل {m('\\square + 16 = 40')} أو {m('6 \\times \\square = 42')} تعمل علامة {m('=')} كالميزان المتعادل، "
                    f"فنستعمل **العملية العكسية** ({m('40 - 16 = 24')} أو {m('42 \\div 6 = 7')}) لإيجاد العدد المفقود."
                ),
                formula_en=dm("\\text{Rule } (\\times 4): \\quad 3 \\to 12, \\quad 5 \\to 20, \\quad 7 \\to 28"),
                caption_ar="قاعدة جدول المدخلات والمخرجات:",
                formula_math_ar=dm("3 \\times 4 = 12, \\qquad 5 \\times 4 = 20, \\qquad 7 \\times 4 = 28"),
                diagram_en=svg_nafes_function_table(["Input", "Output"], [[3, 12], [5, 20], [7, "?"]], highlight_cell=(2, 1)),
            ),
        ],
        traps_en=[
            "Guessing a table rule from only one row: 2 -> 6 could be + 4 OR × 3! Always check the second row (e.g., 5 -> 15 proves the rule is × 3).",
            "Reading down the Output column instead of across from Input to Output when inputs skip numbers (such as Inputs 2, 4, 7).",
            "Adding instead of subtracting in missing-addend equations: in □ + 19 = 45, the missing number is 45 − 19 = 26, NOT 45 + 19 = 64.",
        ],
        traps_ar=[
            "التسرع باستنتاج قاعدة الجدول من صف واحد فقط: الصف 2 -> 6 قد يعني + 4 أو × 3؛ افحص الصف الثاني دائماً للتأكد.",
            "النظر إلى عمود المخرجات وحده عمودياً وإهمال قراءة العلاقة أفقياً من المدخلة إلى المخرجة خاصة عندما تقفز المدخلات.",
            "جمع العددين بدلاً من الطرح في جملة الجمع المفتوحة: في □ + 19 = 45 العدد المفقود هو 45 − 19 = 26 وليس 64.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-03-EX1",
                title_en="Decreasing Skip-Counting Pattern",
                title_ar="نمط عددي متناقص بقفزة ثابتة",
                q_en=f"Look at Omar's number strip: {m('85, 76, 67, \\square, 49')}. What number belongs in the {m('?')} box?",
                q_ar=f"انظر إلى شريط الأعداد لدى عمر: {m('85, 76, 67, \\square, 49')}. ما العدد الذي يوضع مكان علامة {m('?')}؟",
                correct_val=58,
                distractors=[56, 57, 59],
                idea_en="Find the constant amount subtracted at each step and check that it reaches 49 on the next jump.",
                steps_en=[
                    f"Compute the step: {m('85 - 76 = 9')} and {m('76 - 67 = 9')}, so the rule is **subtract 9**.",
                    f"Apply the rule to {m(67)}: {m('67 - 9 = 58')}.",
                ],
                check_en=f"Next jump: {m('58 - 9 = 49')}, matching the last box!",
                idea_ar="نحسب الفرق الثابت بين الحدود المتتالية ثم نتحقق من الوصول إلى 49 في الخطوة التالية.",
                steps_ar=[
                    f"نطرح: {m('85 - 76 = 9')} و{m('76 - 67 = 9')}، إذن القاعدة هي **طرح 9**.",
                    f"نطبّق القاعدة على {m(67)}: {m('67 - 9 = 58')}.",
                ],
                check_ar=f"الخطوة التالية {m('58 - 9 = 49')} تطابق الخانة الأخيرة تماماً.",
                diagram_en=svg_number_strip(["85", "76", "67", "?", "49"]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-03-EX2",
                title_en="Growing Tile Stair Steps",
                title_ar="خطوات البلاط المتنامية",
                q_en=f"Layan builds tile figures: Step 1 uses {m(3)} tiles, Step 2 uses {m(6)} tiles, and Step 3 uses {m(9)} tiles. If the pattern continues in the same way, how many tiles will Step 5 use?",
                q_ar=f"تبني ليان أشكالاً بالبلاط الملون: الشكل 1 فيه {m(3)} بلاطات، والشكل 2 فيه {m(6)} بلاطات، والشكل 3 فيه {m(9)} بلاطات. إذا استمر النمط بالطريقة نفسها، فكم بلاطة في الشكل 5؟",
                correct_val=15,
                distractors=[12, 14, 18],
                idea_en="Each new step adds 3 tiles (or equals 3 times the step number).",
                steps_en=[
                    f"The tile counts are {m('3, 6, 9')}, adding {m('+3')} tiles each step.",
                    f"Step 4 has {m('9 + 3 = 12')} tiles, and Step 5 has {m('12 + 3 = 15')} tiles.",
                ],
                check_en=f"Notice Step {m(5)} equals {m('5 \\times 3 = 15')} tiles.",
                idea_ar="كل شكل جديد يزيد بمقدار 3 بلاطات (أي رقم الشكل مضروباً في 3).",
                steps_ar=[
                    f"أعداد البلاط هي {m('3, 6, 9')} بزيادة {m('+3')} في كل خطوة.",
                    f"الشكل 4 يحوي {m('9 + 3 = 12')} بلاطة، والشكل 5 يحوي {m('12 + 3 = 15')} بلاطة.",
                ],
                check_ar=f"لاحظ أيضاً أن {m('5 \\times 3 = 15')} بلاطة.",
                diagram_en=svg_cube_stack_3d((1, 2, 3)),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-03-EX3",
                title_en="Ticket Machine Input-Output Table",
                title_ar="جدول آلة التذاكر للمدخلات والمخرجات",
                q_en=f"A game machine uses the same multiplication rule for every row in the table shown. What Output number replaces {m('?')} when the Input is {m(8)}?",
                q_ar=f"تتبع آلة ألعاب قاعدة ضرب ثابتة في جميع صفوف الجدول الموضح. ما عدد المخرجة الذي يحل محل {m('?')} عندما تكون المدخلة {m(8)}؟",
                correct_val=48,
                distractors=[38, 42, 54],
                idea_en="Test how each Input becomes its Output across both known rows, then apply that rule to 8.",
                steps_en=[
                    f"Row 1: {m('4 \\times 6 = 24')}. Row 2: {m('6 \\times 6 = 36')}. Both rows multiply the Input by {m(6)}!",
                    f"For Input {m(8)}, compute {m('8 \\times 6 = 48')}.",
                ],
                check_en=f"{m('48 \\div 8 = 6')}, matching the machine's {m('\\times 6')} rule.",
                idea_ar="نستنتج قاعدة الضرب من الصفين المعلومين ثم نطبقها على المدخلة 8.",
                steps_ar=[
                    f"الصف الأول {m('4 \\times 6 = 24')} والصف الثاني {m('6 \\times 6 = 36')}؛ القاعدة هي **الضرب في 6**.",
                    f"عند المدخلة {m(8)} نحسب {m('8 \\times 6 = 48')}.",
                ],
                check_ar=f"التحقق بالقسمة: {m('48 \\div 8 = 6')}.",
                diagram_en=svg_nafes_function_table(["Input", "Output"], [[4, 24], [6, 36], [8, "?"]], highlight_cell=(2, 1)),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-03-EX4",
                title_en="Balanced Scale Missing Number",
                title_ar="العدد المفقود على الميزان المتعادل",
                q_en=f"The classroom scale is balanced: the left pan holds {m('\\square + 17')} grams and the right pan holds {m(43)} grams. What number goes in {m('\\square')}?",
                q_ar=f"ميزان الصف في حالة تعادل: الكفة اليسرى تحوي {m('\\square + 17')} جم والكفة اليمنى تحوي {m(43)} جم. ما العدد المناسب في المربع {m('\\square')}؟",
                correct_val=26,
                distractors=[24, 36, 60],
                idea_en="Since both pans have equal total mass, subtract 17 from 43.",
                steps_en=[
                    f"Balance equation: {m('\\square + 17 = 43')}.",
                    f"Use inverse subtraction: {m('\\square = 43 - 17 = 26')}.",
                ],
                check_en=f"Left pan check: {m('26 + 17 = 43')} grams, matching the right pan!",
                idea_ar="بما أن الكفتين متعادلتان نطرح 17 من 43 لإيجاد الكتلة المفقودة.",
                steps_ar=[
                    f"معادلة التوازن: {m('\\square + 17 = 43')}.",
                    f"بالطرح العكسي: {m('\\square = 43 - 17 = 26')}.",
                ],
                check_ar=f"التحقق: {m('26 + 17 = 43')} جم في الكفتين.",
                diagram_en=svg_g3_equation_balance("[ ] + 17", "43", "Balanced pans"),
            ),
        ],
        blueprints=["G3-ALG-01", "G3-ALG-02", "G3-ALG-03", "G3-ALG-04"],
    )


def _lesson_1_4() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-04",
        level=LEVEL,
        unit_num="1.4",
        topic="Geometry",
        title_en="Analog Clocks, Elapsed Time, Saudi Riyals & Everyday Metric Units",
        title_ar="قراءة الساعة والزمن المنقضي، النقود بالريال السعودي، ووحدات الطول والكتلة والسعة",
        summary_en=(
            "Connect Grade 3 math to everyday life in Saudi Arabia! Read hour and minute hands accurately, "
            "hop along timelines to find elapsed time, count Saudi Riyal banknotes and coins for shopping "
            "and change, and choose the right metric units for length, mass, and liquid capacity."
        ),
        summary_ar=(
            "اربط رياضيات الصف الثالث بحياتنا اليومية في المملكة! سنتعلّم قراءة عقربي الساعات والدقائق بدقة، "
            "وحساب الزمن المنقضي، وعدّ النقود بالريال السعودي وحساب الباقي، والتحويل بين وحدات الطول والكتلة والسعة."
        ),
        goals_en=[
            "Read **analog clocks** to 5-minute and 1-minute marks using the short hour hand and long minute hand.",
            "Calculate **elapsed time**, start/finish times, and calendar conversions (weeks and days).",
            "Count **Saudi Riyal (SAR)** bills and coins, find shopping totals, and compute exact change.",
            "Select and convert everyday **metric units** of length (cm, m, km), mass (g, kg), and capacity (mL, L).",
        ],
        goals_ar=[
            "قراءة **الساعة ذات العقارب** لأقرب 5 دقائق ولأقرب دقيقة باستعمال عقرب الساعات القصير وعقرب الدقائق الطويل.",
            "حساب **الزمن المنقضي** ووقت البداية أو النهاية والتحويل بين الأسابيع والأيام.",
            "عدّ فئات **الريال السعودي (SAR)** الورقية والمعدنية وحساب مجموع المشتريات والباقي.",
            "اختيار وتحويل **الوحدات المترية** للطول (سم، م، كم) والكتلة (جم، كجم) والسعة (مل، ل).",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Analog Clock Hands & Counting Elapsed Time",
                title_ar="١. عقربا الساعة وحساب الزمن المنقضي",
                body_en=(
                    f"On an analog clock, the **short red hand** shows the hour and the **long blue hand** counts minutes. "
                    f"Each big number jump around the dial is {m(5)} minutes ({m('12 \\times 5 = 60')} minutes = {m(1)} hour). "
                    f"When the minute hand reaches {m(7)}, that is {m('7 \\times 5 = 35')} minutes! To find **elapsed time**, "
                    f"hop forward to the next whole hour first, then add the remaining minutes."
                ),
                body_ar=(
                    f"في الساعة ذات العقارب يدل **العقرب القصير** على الساعات و**العقرب الطويل** على الدقائق. "
                    f"كل انتقال بين رقمين متتاليين يمثّل {m(5)} دقائق ({m('12 \\times 5 = 60')} دقيقة = ساعة واحدة). "
                    f"فعندما يشير عقرب الدقائق إلى {m(7)} تكون الدقائق {m('7 \\times 5 = 35')}! ولحساب **الزمن المنقضي** نقفز أولاً إلى الساعة الكاملة التالية ثم نجمع الدقائق المتبقية."
                ),
                formula_en=dm("1 \\text{ hour} = 60 \\text{ minutes}, \\qquad 1 \\text{ week} = 7 \\text{ days}"),
                caption_ar="علاقات الوقت الأساسية في الصف الثالث:",
                formula_math_ar=dm("1 \\text{ hr} = 60 \\text{ min}, \\qquad 1 \\text{ week} = 7 \\text{ days}"),
                diagram_en=svg_nafes_analog_clock(2, 35, "Time shown: 2:35"),
            ),
            nafes_concept(
                title_en="2. Counting Saudi Riyals (SAR) & Finding Change",
                title_ar="٢. عدّ الريالات السعودية وحساب الباقي عند الشراء",
                body_en=(
                    f"When counting **Saudi Riyal (SAR)** bills and coins, start with the **largest bill** first "
                    f"({m(500)}, {m(100)}, {m(50)}, {m(20)}, {m(10)}, {m(5)}) and finish with the {m(2)} SAR and {m(1)} SAR coins. "
                    f"To find **change** at the school canteen or bookstore, subtract the total price from the amount paid—or count up from the price to the bill!"
                ),
                body_ar=(
                    f"عند عدّ نقود **الريال السعودي** نبدأ دائماً **بالفئة الأكبر قيمة** ({m(500)}، {m(100)}، {m(50)}، {m(20)}، {m(10)}، {m(5)}) "
                    f"ثم نضيف العملات المعدنية من فئتي {m(2)} ريال و{m(1)} ريال. ولحساب **الباقي** نطرح ثمن المشتريات من المبلغ المدفوع."
                ),
                formula_en=dm("50 + 10 + 5 + 2 + 1 = 68 \\text{ SAR}, \\qquad \\text{Change} = \\text{Paid} - \\text{Price}"),
                caption_ar="جمع فئات الريال السعودي تنازلياً وحساب الباقي:",
                formula_math_ar=dm("50 + 10 + 5 + 2 + 1 = 68"),
                diagram_en=svg_nafes_sar_money([50, 10, 5, 2, 1], "Total = 68 SAR"),
            ),
            nafes_concept(
                title_en="3. Everyday Metric Length, Mass & Liquid Capacity",
                title_ar="٣. وحدات الطول والكتلة والسعة المترية في حياتنا",
                body_en=(
                    f"Match each tool and unit to its size! For **length**: a pencil in **centimeters (cm)**, a classroom in **meters (m)**, "
                    f"and highway distance in **kilometers (km)** ({m('1\\text{ m} = 100\\text{ cm}')}, {m('1\\text{ km} = 1000\\text{ m}')}). "
                    f"For **mass**: a paperclip in **grams (g)** and a bag of rice in **kilograms (kg)** ({m('1\\text{ kg} = 1000\\text{ g}')}). "
                    f"For **capacity**: a medicine spoon in **milliliters (mL)** and a milk jug in **liters (L)** ({m('1\\text{ L} = 1000\\text{ mL}')})."
                ),
                body_ar=(
                    f"اختر الوحدة المناسبة لكل مقدار! في **الطول**: القلم بالسنتيمتر (**سم**)، والغرفة بالمتر (**م**)، والمسافة بين المدن بالكيلومتر (**كم**) "
                    f"حيث {m('1\\text{ m} = 100\\text{ cm}')} و{m('1\\text{ km} = 1000\\text{ m}')}. وفي **الكتلة**: {m('1\\text{ kg} = 1000\\text{ g}')}. "
                    f"وفي **السعة**: قطرة الدواء بالمللتر (**مل**) وقارورة الماء باللتر (**ل**) حيث {m('1\\text{ L} = 1000\\text{ mL}')}."
                ),
                formula_en=dm("1\\text{ m} = 100\\text{ cm}, \\quad 1\\text{ km} = 1000\\text{ m}, \\quad 1\\text{ kg} = 1000\\text{ g}, \\quad 1\\text{ L} = 1000\\text{ mL}"),
                caption_ar="جدول التحويلات المترية الأساسية:",
                formula_math_ar=dm("1\\text{ m} = 100\\text{ cm}, \\qquad 1\\text{ kg} = 1000\\text{ g}, \\qquad 1\\text{ L} = 1000\\text{ mL}"),
                diagram_en=svg_g3_metric_card("capacity", "1 L = 1,000 mL", "600 mL shown in beaker", 0.6),
            ),
        ],
        traps_en=[
            "Late-hour clock trap: at 4:50, the hour hand is very close to 5, so students misread it as 5:50! Since it has not reached 5 yet, the hour is still 4.",
            "Treating 1 hour as 100 minutes: from 3:40 to 4:15 is 20 + 15 = 35 minutes, NEVER 415 − 340 = 75 minutes!",
            "Mixing up 100 and 1,000 in metric conversions: 1 meter is 100 cm (only 2 zeros), whereas 1 km, 1 kg, and 1 L each equal 1,000 smaller units (3 zeros).",
        ],
        traps_ar=[
            "فخ عقرب الساعات قُبيل تمام الساعة: عند 4:50 يقترب عقرب الساعات جداً من 5 فيقرؤه البعض 5:50 بالخطأ! ما دام لم يصل إلى 5 فالساعة لا تزال 4.",
            "اعتبار الساعة 100 دقيقة: الزمن من 3:40 إلى 4:15 هو 20 + 15 = 35 دقيقة، ولا نطرح 415 − 340 أبداً!",
            "الخلط بين 100 و1,000 في الوحدات: المتر الواحد يساوي 100 سم فقط، بينما الكيلومتر والكيلوجرام واللتر يساوي كلٌّ منها 1,000 وحدة صغيرة.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-04-EX1",
                title_en="Reading Quarter to Five on a Wall Clock",
                title_ar="قراءة الساعة الخامسة إلا ربعاً",
                q_en="Look at the classroom wall clock: the short hour hand is between 4 and 5, and the long minute hand points directly to 9. What time does the clock show?",
                q_ar="انظر إلى ساعة حائط الصف: عقرب الساعات القصير يقع بين 4 و5، وعقرب الدقائق الطويل يشير تماماً إلى الرقم 9. كم تشير الساعة؟",
                correct_val=0,
                distractors=[],
                bilingual_pairs=[
                    ("4:45", "4:45"),
                    ("5:45", "5:45"),
                    ("4:09", "4:09"),
                    ("9:20", "9:20"),
                ],
                correct_pair_idx=0,
                idea_en="Because the hour hand is between 4 and 5, the hour is still 4; multiply 9 by 5 for the minutes.",
                steps_en=[
                    f"The short hand has passed {m(4)} but has not reached {m(5)}, so the hour is {m(4)}.",
                    f"The minute hand on {m(9)} means {m('9 \\times 5 = 45')} minutes -> **4:45**.",
                ],
                check_en=f"In {m(15)} more minutes, the clock will reach {m('5:00')}, which explains why the hour hand is close to {m(5)}.",
                idea_ar="وجود عقرب الساعات بين 4 و5 يعني أن الساعة ما زالت 4، ونضرب 9 في 5 لإيجاد الدقائق.",
                steps_ar=[
                    f"تجاوز العقرب القصير {m(4)} ولم يبلغ {m(5)} بعد، فالساعة هي {m(4)}.",
                    f"عقرب الدقائق عند {m(9)} يعني {m('9 \\times 5 = 45')} دقيقة، أي **4:45**.",
                ],
                check_ar=f"بعد {m(15)} دقيقة ستصبح الساعة 5:00 تماماً.",
                diagram_en=svg_nafes_analog_clock(4, 45, "What time is shown?"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-04-EX2",
                title_en="Science Club Elapsed Minutes",
                title_ar="الزمن المنقضي في نادي العلوم",
                q_en="Tariq started his science experiment at 3:40 PM and finished at 4:25 PM. How many minutes did his experiment take?",
                q_ar="بدأ طارق تجربته العلمية الساعة 3:40 عصراً وأنهى التجربة الساعة 4:25 عصراً. كم دقيقة استغرقت التجربة؟",
                correct_val=45,
                distractors=[35, 55, 85],
                idea_en="Bridge through 4:00 PM on a timeline: count minutes from 3:40 to 4:00, then from 4:00 to 4:25.",
                steps_en=[
                    f"From 3:40 PM to 4:00 PM is {m('60 - 40 = 20')} minutes.",
                    f"From 4:00 PM to 4:25 PM is {m(25)} minutes.",
                    f"Total elapsed time: {m('20 + 25 = 45')} minutes.",
                ],
                check_en=f"Adding {m(20)} min to 3:40 reaches 4:00, plus {m(25)} min lands right on 4:25.",
                idea_ar="نقفز على خط الزمن إلى الساعة 4:00 أولاً ثم نكمل إلى 4:25.",
                steps_ar=[
                    f"من 3:40 إلى 4:00 توجد {m('60 - 40 = 20')} دقيقة.",
                    f"ومن 4:00 إلى 4:25 توجد {m(25)} دقيقة.",
                    f"الزمن المنقضي الكلي = {m('20 + 25 = 45')} دقيقة.",
                ],
                check_ar=f"3:40 زائد 20 دقيقة = 4:00، وزائد 25 دقيقة = 4:25.",
                diagram_en=svg_g3_number_line(
                    [(0, "3:40"), (20, "4:00"), (45, "4:25")],
                    arc=(0, 20, "+20 min"),
                    mark_pos=45,
                    mark_lbl="+25 min",
                    lo=0,
                    hi=45,
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-04-EX3",
                title_en="Bookstore Purchase & Saudi Riyal Change",
                title_ar="شراء من المكتبة وحساب الباقي بالريال",
                q_en=f"Reem buys a notebook for {m(14)} SAR and a pen set for {m(19)} SAR. She pays the cashier with a {m(50)} SAR bill. How many Riyals should she get back in change?",
                q_ar=f"اشترت ريم دفتراً بسعر {m(14)} ريالاً وعلبة أقلام بسعر {m(19)} ريالاً، ودفعت للبائع ورقة نقدية من فئة {m(50)} ريالاً. كم ريالاً تستردّ باقياً؟",
                correct_val=17,
                distractors=[16, 27, 33],
                idea_en="First add the two item prices to find the total bill, then subtract that total from 50 SAR.",
                steps_en=[
                    f"Total cost: {m('14 + 19 = 33')} SAR.",
                    f"Change back: {m('50 - 33 = 17')} SAR.",
                ],
                check_en=f"{m('33 + 17 = 50')} SAR.",
                idea_ar="نجمع ثمن الدفتر والأقلام أولاً، ثم نطرح المجموع من 50 ريالاً.",
                steps_ar=[
                    f"مجموع المشتريات: {m('14 + 19 = 33')} ريالاً.",
                    f"الباقي: {m('50 - 33 = 17')} ريالاً.",
                ],
                check_ar=f"التحقق بالجمع: {m('33 + 17 = 50')} ريالاً.",
                diagram_en=svg_nafes_sar_money([50], "Paid: 50 SAR | Cost: 14 + 19 = 33 SAR"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-04-EX4",
                title_en="Filling a 2-Liter Juice Pitcher",
                title_ar="تعبئة إبريق عصير سعته لتران",
                q_en=f"Mother pours {m(1350)} milliliters of orange juice into an empty {m(2)}-liter pitcher. How many more milliliters of juice are needed to fill the pitcher completely?",
                q_ar=f"سكبت الأم {m(1350)} مللتراً من عصير البرتقال في إبريق فارغ سعته {m(2)} لتر. كم مللتراً إضافياً يلزم لامتلاء الإبريق تماماً؟",
                correct_val=650,
                distractors=[350, 750, 1650],
                idea_en="Convert 2 liters into milliliters first so both quantities use the same unit, then subtract.",
                steps_en=[
                    f"Since {m('1\\text{ L} = 1000\\text{ mL}')}, a {m(2)}-liter pitcher holds {m('2000\\text{ mL}')}.",
                    f"Remaining space: {m('2000 - 1350 = 650\\text{ mL}')}.",
                ],
                check_en=f"{m('1350 + 650 = 2000\\text{ mL} = 2\\text{ L}')}.",
                idea_ar="نحوّل 2 لتر إلى مللترات أولاً لتوحيد الوحدة ثم نطرح.",
                steps_ar=[
                    f"بما أن {m('1\\text{ L} = 1000\\text{ mL}')} فإن {m(2)} لتر = {m('2000\\text{ mL}')}.",
                    f"المقدار المتبقي لامتلاء الإبريق = {m('2000 - 1350 = 650\\text{ mL}')}.",
                ],
                check_ar=f"{m('1350 + 650 = 2000\\text{ mL}')}.",
                diagram_en=svg_g3_metric_card("capacity", "1,350 / 2,000 mL", "2 L = 2,000 mL pitcher", 0.675),
            ),
        ],
        blueprints=["G3-GEO-01", "G3-GEO-02", "G3-GEO-03", "G3-GEO-04"],
    )


# ==============================================================================
# Lesson 1.5 (NAFS-L1-05), Lesson 1.6 (NAFS-L1-06) & Public Entry Point
# ==============================================================================


def _lesson_1_5() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-05",
        level=LEVEL,
        unit_num="1.5",
        topic="Geometry",
        title_en="Grid Perimeter & Area, 2D Polygons, 3D Solids & Symmetry",
        title_ar="المحيط والمساحة على الشبكات، المضلعات، المجسمات ثلاثية الأبعاد، والتماثل",
        summary_en=(
            "Explore shapes from flat grids to 3D blocks! Distinguish walking around the outer border "
            "(perimeter) from covering the inside with unit squares (area), count sides, faces, edges, "
            "and vertices on polygons and solids, and spot lines of symmetry and hidden cubes in stacks."
        ),
        summary_ar=(
            "استكشف الهندسة من الشبكات المربعة حتى المجسمات! فرّق بوضوح بين طول الإطار الخارجي (المحيط) "
            "وعدد المربعات الداخلية (المساحة)، وتعرّف أضلاع ورؤوس المضلعات وأوجه وأحرف المجسمات ومحاور التماثل."
        ),
        goals_en=[
            "Find the **perimeter** of rectangles, squares, and composite grid figures by summing outer side lengths.",
            "Measure the **area** of rectangles and rectilinear figures by counting unit squares or multiplying rows by columns.",
            "Classify **2D polygons** (sides, vertices, right angles) and **3D solids** (faces, edges, vertices).",
            "Identify **lines of symmetry**, congruent shapes, and total unit cubes in **3D stacks**.",
        ],
        goals_ar=[
            "حساب **محيط** المستطيل والمربع والأشكال المركبة على الشبكة بجمع أطوال الأضلاع الخارجية.",
            "إيجاد **مساحة** المستطيل والأشكال المظللة بعدّ الوحدات المربعة أو ضرب الطول في العرض.",
            "تصنيف **المضلعات ثنائية الأبعاد** و**المجسمات ثلاثية الأبعاد** حسب الأضلاع والأوجه والأحرف والرؤوس.",
            "تحديد **محاور التماثل** والأشكال المتطابقة وعدّ المكعبات الكلية في **المجسمات المتراصة**.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Perimeter Around the Rim vs. Area Inside the Grid",
                title_ar="١. المحيط حول الإطار الخارجي مقابل المساحة داخل الشبكة",
                body_en=(
                    f"Think of a garden fence vs. grass carpet! **Perimeter** is the total distance **around the outside edge** "
                    f"(measured in units like cm or m). For a {m('5\\text{ cm} \\times 3\\text{ cm}')} rectangle, walk all four sides: "
                    f"{m('5 + 3 + 5 + 3 = 16\\text{ cm}')}. **Area** counts the **unit squares covering the inside**: "
                    f"{m('5 \\times 3 = 15')} square centimeters!"
                ),
                body_ar=(
                    f"تخيّل الفرق بين سور الحديقة وعشبها الداخلي! **المحيط** هو مجموع أطوال **الحواف الخارجية** حول الشكل "
                    f"({m('5 + 3 + 5 + 3 = 16')} سم). أما **المساحة** فهي عدد **الوحدات المربعة التي تغطي الداخل**: "
                    f"{m('5 \\times 3 = 15')} وحدة مربعة!"
                ),
                formula_en=dm("\\text{Perimeter} = L + W + L + W = 2 \\times (L + W), \\qquad \\text{Area} = L \\times W"),
                caption_ar="مقارنة قانون المحيط وقانون المساحة للمستطيل:",
                formula_math_ar=dm("P = 2 \\times (L + W), \\qquad A = L \\times W"),
                diagram_en=svg_g3_grid_rect(5, 3, top_lbl="5 cm", side_lbl="3 cm", caption="Perimeter = 16 cm | Area = 15 sq cm"),
            ),
            nafes_concept(
                title_en="2. 2D Polygons & 3D Solid Faces, Edges, and Vertices",
                title_ar="٢. المضلعات ثنائية الأبعاد وأوجه وأحرف ورؤوس المجسمات",
                body_en=(
                    f"A **polygon** is a closed flat shape with straight sides: triangle ({m(3)}), quadrilateral ({m(4)}), "
                    f"pentagon ({m(5)}), hexagon ({m(6)}), octagon ({m(8)}). On 3D solids: a **cube** and **rectangular prism** "
                    f"each have {m(6)} flat faces, {m(12)} edges, and {m(8)} vertices; a **square pyramid** has {m(5)} faces, "
                    f"{m(8)} edges, and {m(5)} vertices; a **cylinder** has {m(2)} circular faces and {m(0)} vertices; a **cone** has {m(1)} circular face and {m(1)} vertex; a **sphere** has {m(0)} flat faces, {m(0)} edges, and {m(0)} vertices!"
                ),
                body_ar=(
                    f"**المضلع** شكل مستوٍ مغلق أضلاعه مستقيمة: مثلث ({m(3)})، رباعي ({m(4)})، خماسي ({m(5)})، سداسي ({m(6)})، ثماني ({m(8)}). "
                    f"وفي المجسمات: **للمكعب ومتوازي المستطيلات** {m(6)} أوجه و{m(12)} حرفاً و{m(8)} رؤوس؛ و**للهرم الرباعي** {m(5)} أوجه و{m(8)} أحرف و{m(5)} رؤوس؛ "
                    f"و**للأسطوانة** قاعدتان دائريتان و{m(0)} رأس؛ و**للمخروط** قاعدة دائرية واحدة ورأس واحد؛ و**للكرة** {m(0)} وجه و{m(0)} حرف و{m(0)} رأس!"
                ),
                formula_en=dm("\\text{Cube / Prism: } 6\\text{F},\\; 12\\text{E},\\; 8\\text{V} \\qquad \\text{Square Pyramid: } 5\\text{F},\\; 8\\text{E},\\; 5\\text{V}"),
                caption_ar="خصائص أشهر المجسمات في الصف الثالث:",
                formula_math_ar=dm("6\\text{F},\\; 12\\text{E},\\; 8\\text{V} \\quad | \\quad 5\\text{F},\\; 8\\text{E},\\; 5\\text{V}"),
                diagram_en=svg_g3_solid_3d("cube", "Cube: 6 faces, 12 edges, 8 vertices"),
            ),
            nafes_concept(
                title_en="3. Lines of Symmetry, Congruent Figures & 3D Cube Stacks",
                title_ar="٣. محاور التماثل، الأشكال المتطابقة، ومجسّمات المكعبات",
                body_en=(
                    f"A **line of symmetry** is a fold line where both halves match **exactly** (a square has {m(4)} lines of symmetry; "
                    f"a non-square rectangle has {m(2)}). Two figures are **congruent** when they have the **exact same shape AND size**. "
                    f"When counting unit cubes in a 3D stack, count **column by column** from bottom to top so hidden base cubes are never missed!"
                ),
                body_ar=(
                    f"**محور التماثل** خط طيّ يقسم الشكل إلى نصفين متطابقين تماماً (للمربع {m(4)} محاور تماثل، وللمستطيل غير المربع محوران فقط). "
                    f"ويكون الشكلان **متطابقين** إذا كان لهما **الشكل نفسه والقياس نفسه**. وعند عدّ المكعبات في مجسم متراصّ نعدّ **عموداً بعد عمود** حتى لا ننسى المكعبات السفلية المخفية!"
                ),
                formula_en=dm("\\text{Column Heights } (3, 2, 1) \\implies \\text{Total Cubes} = 3 + 2 + 1 = 6"),
                caption_ar="عدّ المكعبات بجمع ارتفاعات الأعمدة:",
                formula_math_ar=dm("3 + 2 + 1 = 6 \\text{ cubes}"),
                diagram_en=svg_cube_stack_3d((3, 2, 1)),
            ),
        ],
        traps_en=[
            "Half-perimeter mistake: adding only length + width (5 + 3 = 8) instead of all four sides (5 + 3 + 5 + 3 = 16) for a rectangle's perimeter.",
            "Counting inside grid lines as perimeter on L-shapes: perimeter counts ONLY outer boundary segments, while area counts unit squares inside.",
            "Diagonal fold trap on a non-square rectangle: folding an oblong rectangle along its diagonal makes corners miss—it has 2 lines of symmetry, NOT 4!",
        ],
        traps_ar=[
            "خطأ نصف المحيط: جمع الطول والعرض مرة واحدة (5 + 3 = 8) بدلاً من جمع الأضلاع الأربعة كلها (16) عند حساب محيط المستطيل.",
            "عدّ الخطوط الداخلية ضمن المحيط في الأشكال المركبة: المحيط يقيس الحافة الخارجية فقط بينما المساحة تعدّ المربعات الداخلية.",
            "فخ القطر في المستطيل: طيّ المستطيل غير المربع حول قطره لا يطابق الرؤوس؛ لذلك له محورا تماثل فقط وليس 4!",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-05-EX1",
                title_en="Perimeter of an L-Shaped Garden Path",
                title_ar="محيط ممر حديقة على شكل حرف L",
                q_en=f"On a {m('1\\text{ m}')} unit grid, Fahad shades an L-shaped garden made of {m(5)} unit squares: a vertical column of {m(3)} squares on the left plus {m(2)} more squares extending right along the bottom row. What is the **perimeter** of the shaded L-shape?",
                q_ar=f"على شبكة وحدتها {m('1\\text{ m}')} ظلّل فهد حديقة على شكل حرف L مكوّنة من {m(5)} مربعات: عمود رأسي من {m(3)} مربعات يساراً مع مربعين إضافيين يمتدان يميناً في الصف السفلي. ما **محيط** الشكل المظلل بالمتر؟",
                correct_val=12,
                distractors=[5, 10, 14],
                idea_en="Trace every outer unit edge all the way around the L-shape without counting interior shared edges.",
                steps_en=[
                    f"Left side = {m(3)}, bottom = {m(3)}, right-most step up = {m(1)}, inner horizontal = {m(2)}, inner vertical = {m(2)}, top = {m(1)}.",
                    f"Sum all outer edges: {m('3 + 3 + 1 + 2 + 2 + 1 = 12\\text{ m}')}.",
                ],
                check_en=f"Its bounding box is {m('3 \\times 3')}, whose perimeter is also {m('2 \\times (3 + 3) = 12\\text{ m}')}!",
                idea_ar="نتتبّع قطع الحافة الخارجية حول الشكل خطوةً بخطوة دون عدّ الخطوط الداخلية.",
                steps_ar=[
                    f"أطوال الحواف الخارجية بالترتيب: يسار {m(3)}، أسفل {m(3)}، يمين سفلي {m(1)}، أفقي داخلي {m(2)}، رأسي داخلي {m(2)}، أعلى {m(1)}.",
                    f"المحيط = {m('3 + 3 + 1 + 2 + 2 + 1 = 12')} متراً.",
                ],
                check_ar=f"لاحظ أن المساحة {m(5)} وحدات مربعة بينما المحيط الخارجي {m(12)} متراً.",
                diagram_en=svg_g3_grid_rect(3, 3, shaded_cells=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], caption="1 unit = 1 m"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-05-EX2",
                title_en="Area of a Classroom Prayer Rug",
                title_ar="مساحة سجادة بالوحدات المربعة",
                q_en=f"A rectangular rug covers {m(6)} unit squares along its length and {m(4)} unit squares along its width. What is the **area** of the rug in square units?",
                q_ar=f"تغطي سجادة مستطيلة {m(6)} وحدات طولاً و{m(4)} وحدات عرضاً على شبكة المربعات. ما **مساحة** السجادة بالوحدات المربعة؟",
                correct_val=24,
                distractors=[10, 20, 28],
                idea_en="Multiply the number of columns (6) by the number of rows (4) to count all unit squares inside.",
                steps_en=[
                    f"There are {m(4)} rows with {m(6)} unit squares in each row.",
                    f"Area = {m('6 \\times 4 = 24')} square units.",
                ],
                check_en=f"Do not confuse area ({m(24)} sq units) with perimeter ({m('2 \\times (6 + 4) = 20')} units)!",
                idea_ar="نضرب عدد الأعمدة (6) في عدد الصفوف (4) لحساب جميع المربعات الداخلية.",
                steps_ar=[
                    f"الشبكة تتكون من {m(4)} صفوف وفي كل صف {m(6)} مربعات متطابقة.",
                    f"المساحة = {m('6 \\times 4 = 24')} وحدة مربعة.",
                ],
                check_ar=f"انتبه لعدم الخلط بين المساحة ({m(24)}) والمحيط ({m(20)}).",
                diagram_en=svg_g3_grid_rect(6, 4, top_lbl="6 units", side_lbl="4 units"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-05-EX3",
                title_en="Edges of a Wooden Square Pyramid",
                title_ar="عدد أحرف الهرم الرباعي الخشبي",
                q_en="Joud holds a wooden **square pyramid** block in geometry class. How many **edges** does her square pyramid have?",
                q_ar="تمسك جود مجسّم **هرم رباعي** خشبي في حصة الهندسة. كم **حرفاً** للهرم الرباعي؟",
                correct_val=8,
                distractors=[5, 6, 12],
                idea_en="Count the 4 edges around the square base plus the 4 slanted edges rising to the top vertex.",
                steps_en=[
                    f"The bottom square face has {m(4)} base edges.",
                    f"From the {m(4)} base corners, {m(4)} slanted edges meet at the apex: {m('4 + 4 = 8')} edges.",
                ],
                check_en=f"Summary of a square pyramid: {m(5)} faces, {m(8)} edges, and {m(5)} vertices.",
                idea_ar="نعدّ أحرف القاعدة المربعة الأربعة ثم الأحرف الجانبية الأربعة المتجهة إلى الرأس العلوي.",
                steps_ar=[
                    f"للقاعدة المربعة السفلية {m(4)} أحرف.",
                    f"وتمتد من رؤوس القاعدة {m(4)} أحرف مائلة نحو القمة: {m('4 + 4 = 8')} أحرف.",
                ],
                check_ar=f"تذكّر: للهرم الرباعي {m(5)} أوجه و{m(8)} أحرف و{m(5)} رؤوس.",
                diagram_en=svg_g3_solid_3d("pyramid", "Square pyramid"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-05-EX4",
                title_en="Counting Cubes in a Four-Column Tower",
                title_ar="عدّ المكعبات في مجسم من أربعة أعمدة",
                q_en=f"Yasser glues unit cubes into {m(4)} side-by-side columns with heights {m(4)}, {m(3)}, {m(2)}, and {m(1)} cubes. How many unit cubes did Yasser use in all?",
                q_ar=f"ألصق ياسر مكعبات وحدة في {m(4)} أعمدة متجاورة ارتفاعاتها {m(4)} و{m(3)} و{m(2)} و{m(1)} من المكعبات. كم مكعب وحدة استعمل ياسر إجمالاً؟",
                correct_val=10,
                distractors=[7, 9, 12],
                idea_en="Add the full height of each column so every bottom cube supporting a tall column is counted.",
                steps_en=[
                    f"Column heights from left to right are {m(4)}, {m(3)}, {m(2)}, and {m(1)}.",
                    f"Total cubes: {m('4 + 3 + 2 + 1 = 10')} cubes.",
                ],
                check_en=f"Pairing ends gives {m('(4 + 1) + (3 + 2) = 5 + 5 = 10')}.",
                idea_ar="نجمع ارتفاع كل عمود بالكامل شاملاً المكعبات السفلية الحاملة للأعمدة.",
                steps_ar=[
                    f"ارتفاعات الأعمدة من اليسار إلى اليمين هي {m(4)} و{m(3)} و{m(2)} و{m(1)}.",
                    f"المجموع الكلي = {m('4 + 3 + 2 + 1 = 10')} مكعبات.",
                ],
                check_ar=f"{m('(4 + 1) + (3 + 2) = 5 + 5 = 10')}.",
                diagram_en=svg_cube_stack_3d((4, 3, 2, 1)),
            ),
        ],
        blueprints=["G3-GEO-05", "G3-GEO-06", "G3-GEO-07", "G3-GEO-08"],
    )


def _lesson_1_6() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L1-06",
        level=LEVEL,
        unit_num="1.6",
        topic="Data & Probability",
        title_en="Pictographs, Bar Charts, Tally Tables & Spinner Likelihood",
        title_ar="التمثيل بالرموز والأعمدة، جداول الإشارات، والاحتمالات بالقرص الدوّار",
        summary_en=(
            "Read classroom data like a detective! Always check the pictograph key first (especially "
            "for half-symbols), compare bar heights and tally bundles of five, and describe spinner or "
            "marble bag outcomes as certain, more likely, equally likely, less likely, or impossible."
        ),
        summary_ar=(
            "اقرأ البيانات المدرسية بمهارة! تعلّم قراءة مفتاح التمثيل بالرموز ونصف الرمز أولاً، ومقارنة "
            "الأعمدة البيانية وحِزم الإشارات الخماسية، ووصف الاحتمال بالكلمات والكسور على القرص الدوّار وكيس الكرات."
        ),
        goals_en=[
            "Interpret **pictographs** with keys of 2, 4, 5, or 10—including **half-symbols**.",
            "Read **bar charts** to answer 'how many more', 'how many fewer', and 'how many altogether' questions.",
            "Count **tally bundles of 5** and read two-attribute classroom frequency tables.",
            "Classify spinner and marble bag events (**certain, more likely, equally likely, less likely, impossible**) and write simple fraction probabilities.",
        ],
        goals_ar=[
            "تفسير **التمثيل بالرموز** بمفتاح 2 أو 4 أو 5 أو 10 شاملةً قراءة **نصف الرمز**.",
            "قراءة **التمثيل بالأعمدة** للإجابة عن أسئلة (كم يزيد، كم يقل، ما المجموع الكلي).",
            "عدّ **حِزم الإشارات الخماسية** واستخراج المعلومات من جداول التكرار المدرسية.",
            "وصف الحوادث (**أكيد، أكثر احتمالاً، متساوي الإمكانية، أقل احتمالاً، مستحيل**) وكتابة الاحتمال ككسر بسيط.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Pictograph Keys & Reading Half-Symbols",
                title_ar="١. مفتاح التمثيل بالرموز وقراءة نصف الرمز",
                body_en=(
                    f"Before counting anything in a pictograph, read the **Key** at the bottom! If **1 circle = 4 fruits**, "
                    f"then each full circle stands for {m(4)} and a **half-circle** stands for half of {m(4)}, which is {m('4 \\div 2 = 2')}. "
                    f"So a row with {m(3)} full circles and {m(1)} half-circle represents {m('3 \\times 4 + 2 = 14')} fruits!"
                ),
                body_ar=(
                    f"قبل عدّ الرموز اقرأ **مفتاح التمثيل** أسفل اللوحة دائماً! إذا كان **كل رمز = 4 ثمار** فإن الرمز الكامل يساوي {m(4)} "
                    f"و**نصف الرمز** يساوي نصف العدد {m(4)} أي {m('4 \\div 2 = 2')}. وبذلك فإن {m(3)} رموز كاملة ونصف رمز تمثّل {m('3 \\times 4 + 2 = 14')} ثمرة!"
                ),
                formula_en=dm("\\text{Value} = (\\text{Full Icons} \\times \\text{Key}) + \\frac{1}{2} \\text{Key} \\quad (\\text{if half-icon present})"),
                caption_ar="حساب قيمة الصف عند وجود نصف رمز:",
                formula_math_ar=dm("3 \\times 4 + 2 = 14"),
                diagram_en=svg_nafes_pictograph(
                    [("Dates", 3.5), ("Figs", 2.0), ("Apples", 3.0)],
                    "Key: Each circle = 4 fruits",
                ),
            ),
            nafes_concept(
                title_en="2. Bar Chart Comparisons & Tally Bundles of Five",
                title_ar="٢. مقارنات الأعمدة البيانية وحِزم الإشارات الخماسية",
                body_en=(
                    f"In a **tally table**, four upright strokes crossed by one diagonal slash make a neat bundle of **{m(5)}**—skip-count "
                    f"bundles by fives ({m('5, 10, 15, \\dots')}) and add any single strokes left over! In **bar charts**, "
                    f"**'how many more / fewer'** means **subtract** the two bar values, while **'altogether / in all'** means **add**!"
                ),
                body_ar=(
                    f"في **جدول الإشارات** تمثّل أربع شرطات رأسية يقطعها خط مائل حزمة كاملة من **{m(5)}**؛ عدّ الحِزم بالخمسات ثم أضف الإشارات المفردة! "
                    f"وفي **الأعمدة البيانية** تعني عبارة **«كم يزيد / بكم يقل»** عملية **الطرح**، بينما تعني **«معاً / إجمالاً»** عملية **الجمع**!"
                ),
                formula_en=dm("2 \\text{ tally bundles} + 2 \\text{ strokes} = 2 \\times 5 + 2 = 12"),
                caption_ar="حساب العدد من حِزم الإشارات الخماسية:",
                formula_math_ar=dm("2 \\times 5 + 2 = 12"),
                diagram_en=svg_g3_tally_table("Club", [("Science", 12), ("Art", 8), ("Reading", 15)]),
            ),
            nafes_concept(
                title_en="3. Spinner & Marble Bag Likelihood Words & Fractions",
                title_ar="٣. وصف الاحتمال بالكلمات والكسور على القرص الدوّار",
                body_en=(
                    f"When all sectors on a spinner are equal, compare how many sectors match your target! "
                    f"**Certain** = happens every time (all sectors match); **Impossible** = cannot happen ({m(0)} sectors match); "
                    f"**Equally likely** = exact half-and-half tie; **More likely** = more than half or the largest share. "
                    f"As a fraction, probability is **matching sectors over total equal sectors**!"
                ),
                body_ar=(
                    f"عندما تتساوى أجزاء القرص الدوّار نقارن عدد الأجزاء المطابقة! **أكيد** = كل الأجزاء تطابق الحدث؛ "
                    f"**مستحيل** = لا يوجد أي جزء مطابق ({m(0)})؛ **متساوي الإمكانية** = تساوٍ تام بالنصف؛ **أكثر احتمالاً** = النصيب الأكبر. "
                    f"وبالصورة الكسرية يساوي الاحتمال **عدد الأجزاء المطلوبة على إجمالي الأجزاء المتطابقة**!"
                ),
                formula_en=dm("\\text{Fraction Chance} = \\frac{\\text{Matching Equal Sectors}}{\\text{Total Equal Sectors}} = \\frac{4}{6}"),
                caption_ar="تمثيل فرصة الوقوف على اللون الأزرق بكسر:",
                formula_math_ar=dm("\\frac{4}{6}"),
                diagram_en=svg_nafes_spinner(["Blue", "Blue", "Blue", "Red", "Green", "Blue"], "6 equal sectors"),
            ),
        ],
        traps_en=[
            "Ignoring the pictograph key: counting 3 full icons and a half-icon as 3 or 4 instead of using the key (e.g., 3 × 4 + 2 = 14)!",
            "Miscounting crossed tally bundles as 4 or 6: the diagonal slash IS the 5th mark, so 4 vertical lines + 1 slash = 5.",
            "Calling the most common color 'Certain': if a bag has 7 blue marbles and 1 red marble, blue is 'More likely', NOT 'Certain', because red can still be picked!",
        ],
        traps_ar=[
            "إهمال مفتاح التمثيل بالرموز: عدّ الرموز كأن كل رمز يساوي 1 دون ضربها في قيمة المفتاح وحساب نصف الرمز!",
            "عدّ حزمة الإشارات الخماسية 4 أو 6 بالخطأ: الخط المائل هو الإشارة الخامسة، فالحزمة الكاملة تساوي 5 دائماً.",
            "وصف اللون الأكثر عدداً بأنه «أكيد»: عند وجود 7 كرات زرقاء وكرة حمراء واحدة فالحدث «أكثر احتمالاً» وليس «أكيداً» لأن سحب الحمراء ممكن.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L1-06-EX1",
                title_en="Pictograph with Half-Symbols for Trees Planted",
                title_ar="التمثيل بالرموز لشتلات الأشجار مع نصف رمز",
                q_en=f"In the Green Saudi School campaign pictograph, **each circle stands for {m(6)} saplings**. Grade 3A has {m(3)} full circles and {m(1)} half-circle. How many saplings did Grade 3A plant?",
                q_ar=f"في لوحة التمثيل بالرموز لحملة التشجير المدرسية **يمثّل كل رمز دائري {m(6)} شتلات**. أمام الصف الثالث (أ) {m(3)} دوائر كاملة ونصف دائرة. كم شتلة زرع الصف الثالث (أ)؟",
                correct_val=21,
                distractors=[18, 19, 24],
                idea_en="Multiply 3 full circles by 6, then add half of 6 for the half-circle.",
                steps_en=[
                    f"Three full circles: {m('3 \\times 6 = 18')} saplings.",
                    f"One half-circle: {m('6 \\div 2 = 3')} saplings.",
                    f"Total planted by Grade 3A: {m('18 + 3 = 21')} saplings.",
                ],
                check_en=f"{m(21)} lies halfway between {m('3 \\times 6 = 18')} and {m('4 \\times 6 = 24')}.",
                idea_ar="نضرب 3 دوائر كاملة في 6 ثم نضيف نصف العدد 6 مقابل نصف الدائرة.",
                steps_ar=[
                    f"قيمة 3 دوائر كاملة: {m('3 \\times 6 = 18')} شتلة.",
                    f"قيمة نصف الدائرة: {m('6 \\div 2 = 3')} شتلات.",
                    f"المجموع = {m('18 + 3 = 21')} شتلة.",
                ],
                check_ar=f"العدد {m(21)} يقع في المنتصف تماماً بين {m(18)} و{m(24)}.",
                diagram_en=svg_nafes_pictograph([("3A", 3.5), ("3B", 2.0), ("3C", 3.0)], "Key: Each circle = 6 saplings"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-06-EX2",
                title_en="Comparing Favorite Sports on a Bar Chart",
                title_ar="مقارنة الرياضات المفضلة في التمثيل بالأعمدة",
                q_en=f"The bar chart shows Grade 3 favorite sports: Football ({m(18)}), Swimming ({m(11)}), Running ({m(9)}), and Tennis ({m(6)}). How many **more** students chose Football than Running?",
                q_ar=f"يبيّن التمثيل بالأعمدة الرياضة المفضلة لطلاب الصف الثالث: كرة القدم ({m(18)})، السباحة ({m(11)})، الجري ({m(9)})، التنس ({m(6)}). بكم **يزيد** عدد من اختاروا كرة القدم على من اختاروا الجري؟",
                correct_val=9,
                distractors=[7, 12, 27],
                idea_en="'How many more' asks for the difference, so subtract Running from Football.",
                steps_en=[
                    f"Read the two bars: Football = {m(18)} and Running = {m(9)}.",
                    f"Subtract: {m('18 - 9 = 9')} more students.",
                ],
                check_en=f"{m('9 + 9 = 18')}.",
                idea_ar="عبارة «بكم يزيد» تعني إيجاد الفرق بالطرح بين عمود كرة القدم وعمود الجري.",
                steps_ar=[
                    f"قراءة العمودين: كرة القدم = {m(18)}، الجري = {m(9)}.",
                    f"نطرح: {m('18 - 9 = 9')} طلاب.",
                ],
                check_ar=f"التحقق بالجمع: {m('9 + 9 = 18')}.",
                diagram_en=svg_bar_chart([("Foot", 18, "18"), ("Swim", 11, "11"), ("Run", 9, "9"), ("Ten", 6, "6")], y_max=20),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-06-EX3",
                title_en="Counting Tally Bundles in a Canteen Survey",
                title_ar="عدّ الإشارات في استطلاع المقصف المدرسي",
                q_en="Students voted for their favorite juice using tally marks: Milk got 3 crossed bundles and 2 single marks, Apple got 2 crossed bundles and 4 single marks, and Berry got 1 crossed bundle and 3 single marks. How many students voted for **Milk**?",
                q_ar="صوّت الطلاب لمشروبهم المفضل بالإشارات: حصل الحليب على 3 حِزم خماسية وإشارتين مفردتين، والتفاح على حزمتين و4 إشارات، والتوت على حزمة و3 إشارات. كم طالباً اختار **الحليب**؟",
                correct_val=17,
                distractors=[14, 15, 22],
                idea_en="Each crossed bundle equals 5 votes; multiply 3 bundles by 5 and add the 2 extra strokes.",
                steps_en=[
                    f"Three bundles of five give {m('3 \\times 5 = 15')} votes.",
                    f"Add the {m(2)} single strokes: {m('15 + 2 = 17')} students.",
                ],
                check_en=f"Skip-counting: {m('5, 10, 15, 16, 17')}.",
                idea_ar="كل حزمة خماسية تمثّل 5 أصوات؛ نضرب 3 في 5 ثم نضيف الإشارتين المفردتين.",
                steps_ar=[
                    f"ثلاث حِزم خماسية تساوي {m('3 \\times 5 = 15')} صوتاً.",
                    f"نضيف الإشارتين المفردتين: {m('15 + 2 = 17')} طالباً.",
                ],
                check_ar=f"بالعد القفزي: {m('5, 10, 15, 16, 17')}.",
                diagram_en=svg_g3_tally_table("Drink", [("Milk", 17), ("Apple", 14), ("Berry", 8)]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L1-06-EX4",
                title_en="Describing Likelihood When Pulling a Marble",
                title_ar="وصف احتمال سحب كرة من الوعاء",
                q_en=f"A jar holds {m(7)} green marbles and {m(2)} yellow marbles, all the same size. Without looking, Huda picks {m(1)} marble. How likely is she to pick a **blue** marble?",
                q_ar=f"في وعاء {m(7)} كرات خضراء وكرتان صفراوان متماثلة الحجم. سحبت هدى كرة واحدة دون النظر. ما وصف احتمال سحب كرة **زرقاء**؟",
                correct_val=0,
                distractors=[],
                bilingual_pairs=[
                    ("Impossible", "مستحيل"),
                    ("Less likely", "أقل احتمالاً"),
                    ("More likely", "أكثر احتمالاً"),
                    ("Certain", "أكيد"),
                ],
                correct_pair_idx=0,
                idea_en="Check how many blue marbles are inside the jar—zero blue marbles means it can never happen!",
                steps_en=[
                    f"The jar contains only green ({m(7)}) and yellow ({m(2)}) marbles.",
                    f"Because there are {m(0)} blue marbles in the jar, picking blue is **Impossible**.",
                ],
                check_en="Green is 'More likely', yellow is 'Less likely', and blue is 'Impossible'.",
                idea_ar="نتحقق من عدد الكرات الزرقاء داخل الوعاء؛ عدم وجود أي كرة زرقاء يجعل الحدث مستحيلاً!",
                steps_ar=[
                    f"الوعاء يحتوي على كرات خضراء ({m(7)}) وصفراء ({m(2)}) فقط.",
                    f"بما أن عدد الكرات الزرقاء {m(0)}، فإن سحب كرة زرقاء حدث **مستحيل**.",
                ],
                check_ar="الأخضر أكثر احتمالاً، والأصفر أقل احتمالاً، والأزرق مستحيل.",
                diagram_en=svg_g3_marble_bag([("Green", 7, "#86efac"), ("Yellow", 2, "#fde047")], "9 marbles in jar"),
            ),
        ],
        blueprints=["G3-DAT-01", "G3-DAT-02", "G3-DAT-03", "G3-DAT-04"],
    )


def get_grade3_lessons() -> list[dict]:
    """Return all 6 bilingual ETEC Nafes Grade 3 lessons covering blueprints G3-NUM/ALG/GEO/DAT."""
    return [
        _lesson_1_1(),
        _lesson_1_2(),
        _lesson_1_3(),
        _lesson_1_4(),
        _lesson_1_5(),
        _lesson_1_6(),
    ]
