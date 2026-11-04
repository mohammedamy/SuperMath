"""Bilingual Study Lessons for ETEC Nafes KSA National Assessment — Grade 9 (الصف الثالث المتوسط).

Covers 6 comprehensive study units (NAFS-L3-01 .. NAFS-L3-06), 24 official Grade 9 blueprints,
18/18 XML-valid concept SVGs, and 24/24 bespoke worked examples with 4-option (A–D) MCQs and SVGs.
"""
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
    svg_area_identity_square,
    svg_balance_scales,
    svg_bar_chart,
    svg_function_machine,
    svg_midpoint_square_shaded,
    svg_motion_timeline,
    svg_nafes_box_plot,
    svg_nafes_coordinate_line,
    svg_nafes_function_table,
    svg_nafes_pie_chart,
    svg_nafes_spinner,
    svg_number_strip,
    svg_parabola_roots,
    svg_pipe_tank,
    svg_regular_polygon,
    svg_square_circle_shaded,
    svg_venn_2,
)

LEVEL = "Grade 9"


# ==============================================================================
# Bespoke Grade 9 SVG Generators (all validated via _wrap_nafes_svg -> ET)
# ==============================================================================

def svg_g9_real_number_line(
    ticks: list[int],
    mark_pos: float,
    mark_lbl: str,
    caption: str = "",
    ray_dir: int = 0,
    closed_dot: bool = True,
) -> str:
    """Calibrated number line for irrational square-root bounds or linear inequality rays."""
    w, h = 380, (124 if caption else 104)
    x0, x1, y = 34, 346, 58
    lo, hi = min(ticks), max(ticks)
    span = max(1.0, float(hi - lo))

    def sx(v: float) -> float:
        return x0 + (v - lo) / span * (x1 - x0)

    parts = [
        f'<line x1="{x0 - 12}" y1="{y}" x2="{x1 + 12}" y2="{y}" stroke="{STROKE}" stroke-width="2"/>',
        f'<polygon points="{x0 - 16},{y} {x0 - 8},{y - 4} {x0 - 8},{y + 4}" fill="{STROKE}"/>',
        f'<polygon points="{x1 + 16},{y} {x1 + 8},{y - 4} {x1 + 8},{y + 4}" fill="{STROKE}"/>',
    ]
    for t in ticks:
        xt = sx(t)
        parts.append(f'<line x1="{xt:.1f}" y1="{y - 6}" x2="{xt:.1f}" y2="{y + 6}" stroke="{STROKE}" stroke-width="1.6"/>')
        parts.append(f'<text x="{xt:.1f}" y="{y + 22}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(t)}</text>')

    xm = max(x0, min(x1, sx(mark_pos)))
    if ray_dir > 0:
        parts.append(f'<line x1="{xm:.1f}" y1="{y}" x2="{x1 + 10}" y2="{y}" stroke="{BLUE}" stroke-width="4.2"/>')
        parts.append(f'<polygon points="{x1 + 16},{y} {x1 + 6},{y - 5} {x1 + 6},{y + 5}" fill="{BLUE}"/>')
    elif ray_dir < 0:
        parts.append(f'<line x1="{x0 - 10}" y1="{y}" x2="{xm:.1f}" y2="{y}" stroke="{BLUE}" stroke-width="4.2"/>')
        parts.append(f'<polygon points="{x0 - 16},{y} {x0 - 6},{y - 5} {x0 - 6},{y + 5}" fill="{BLUE}"/>')

    dot_fill = RED if closed_dot else "#ffffff"
    dot_stroke = RED if ray_dir == 0 else BLUE
    if ray_dir != 0 and closed_dot:
        dot_fill = BLUE
    parts.append(f'<circle cx="{xm:.1f}" cy="{y}" r="5.2" fill="{dot_fill}" stroke="{dot_stroke}" stroke-width="2.2"/>')
    parts.append(f'<text x="{xm:.1f}" y="{y - 14}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{dot_stroke}">{esc(mark_lbl)}</text>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 10}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_right_triangle(a_lbl: str, b_lbl: str, c_lbl: str, caption: str = "") -> str:
    """Right triangle with 90-degree corner marker and labeled legs a (vertical), b (horizontal), c (hypotenuse)."""
    w, h = 320, (196 if caption else 178)
    cx, cy = 78, 140
    ax, ay = 78, 34
    bx, by = 248, 140
    parts = [
        f'<polygon points="{ax},{ay} {cx},{cy} {bx},{by}" fill="{WATER}" fill-opacity="0.55" stroke="{STROKE}" stroke-width="2.2" stroke-linejoin="round"/>',
        f'<rect x="{cx}" y="{cy - 13}" width="13" height="13" fill="none" stroke="{STROKE}" stroke-width="1.6"/>',
        f'<circle cx="{ax}" cy="{ay}" r="3" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>',
        f'<circle cx="{bx}" cy="{by}" r="3" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>',
        f'<circle cx="{cx}" cy="{cy}" r="3" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>',
        f'<text x="{cx - 12}" y="{(ay + cy) / 2 + 4:.1f}" text-anchor="end" font-size="13" font-weight="800" fill="{BLUE}">{esc(a_lbl)}</text>',
        f'<text x="{(cx + bx) / 2:.1f}" y="{cy + 21}" text-anchor="middle" font-size="13" font-weight="800" fill="{GREEN}">{esc(b_lbl)}</text>',
        f'<text x="{(ax + bx) / 2 + 14:.1f}" y="{(ay + by) / 2 - 6:.1f}" text-anchor="start" font-size="13" font-weight="800" fill="{RED}">{esc(c_lbl)}</text>',
    ]
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_solid_3d(kind: str, r_lbl: str, h_lbl: str = "", caption: str = "") -> str:
    """3D geometry figure for cylinder, cone, square pyramid, or sphere."""
    w, h = 310, (198 if caption else 180)
    cx = 148
    parts = []
    if kind == "cylinder":
        yt, yb, rx, ry = 38, 138, 60, 17
        parts.extend([
            f'<rect x="{cx - rx}" y="{yt}" width="{2 * rx}" height="{yb - yt}" fill="{WATER}" fill-opacity="0.55"/>',
            f'<ellipse cx="{cx}" cy="{yb}" rx="{rx}" ry="{ry}" fill="{WATER}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="1.8" stroke-dasharray="4,3"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,0 {cx + rx},{yb}" fill="none" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<ellipse cx="{cx}" cy="{yt}" rx="{rx}" ry="{ry}" fill="#e0f2fe" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx - rx}" y1="{yt}" x2="{cx - rx}" y2="{yb}" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx + rx}" y1="{yt}" x2="{cx + rx}" y2="{yb}" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx}" y1="{yt}" x2="{cx + rx}" y2="{yt}" stroke="{RED}" stroke-width="2"/>',
            f'<circle cx="{cx}" cy="{yt}" r="2.8" fill="{RED}"/>',
            f'<text x="{cx + rx / 2:.1f}" y="{yt - 6}" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(r_lbl)}</text>',
            f'<line x1="{cx + rx + 16}" y1="{yt}" x2="{cx + rx + 16}" y2="{yb}" stroke="{BLUE}" stroke-width="1.6"/>',
            f'<text x="{cx + rx + 24}" y="{(yt + yb) / 2 + 4:.1f}" text-anchor="start" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(h_lbl)}</text>',
        ])
    elif kind == "cone":
        yt, yb, rx, ry = 28, 140, 62, 17
        parts.extend([
            f'<polygon points="{cx},{yt} {cx - rx},{yb} {cx + rx},{yb}" fill="{SHADE}" fill-opacity="0.55"/>',
            f'<ellipse cx="{cx}" cy="{yb}" rx="{rx}" ry="{ry}" fill="#f3e8ff" stroke="{STROKE}" stroke-width="1.6" stroke-dasharray="4,3"/>',
            f'<path d="M {cx - rx},{yb} A {rx},{ry} 0 0,0 {cx + rx},{yb}" fill="none" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx}" y1="{yt}" x2="{cx - rx}" y2="{yb}" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx}" y1="{yt}" x2="{cx + rx}" y2="{yb}" stroke="{STROKE}" stroke-width="2.1"/>',
            f'<line x1="{cx}" y1="{yt}" x2="{cx}" y2="{yb}" stroke="{BLUE}" stroke-width="1.7" stroke-dasharray="4,3"/>',
            f'<line x1="{cx}" y1="{yb}" x2="{cx + rx}" y2="{yb}" stroke="{RED}" stroke-width="2"/>',
            f'<circle cx="{cx}" cy="{yb}" r="2.8" fill="{RED}"/>',
            f'<text x="{cx + rx / 2:.1f}" y="{yb + 14}" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(r_lbl)}</text>',
            f'<text x="{cx - 8}" y="{(yt + yb) / 2 + 6:.1f}" text-anchor="end" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(h_lbl)}</text>',
        ])
    elif kind == "pyramid":
        ax, ay = cx, 26
        bl, br, fr, fl = (84, 140), (192, 140), (222, 116), (114, 116)
        cx_b, cy_b = (bl[0] + fr[0]) / 2, (bl[1] + fr[1]) / 2
        parts.extend([
            f'<polygon points="{ax},{ay} {bl[0]},{bl[1]} {br[0]},{br[1]}" fill="{SHADE}" fill-opacity="0.58" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
            f'<polygon points="{ax},{ay} {br[0]},{br[1]} {fr[0]},{fr[1]}" fill="{SHADE_ALT}" fill-opacity="0.65" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
            f'<polyline points="{bl[0]},{bl[1]} {fl[0]},{fl[1]} {fr[0]},{fr[1]}" fill="none" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,3"/>',
            f'<line x1="{ax}" y1="{ay}" x2="{fl[0]}" y2="{fl[1]}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4,3"/>',
            f'<line x1="{ax}" y1="{ay}" x2="{cx_b:.1f}" y2="{cy_b:.1f}" stroke="{BLUE}" stroke-width="1.8" stroke-dasharray="4,3"/>',
            f'<text x="{(bl[0] + br[0]) / 2:.1f}" y="{bl[1] + 18}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(r_lbl)}</text>',
            f'<text x="{cx_b - 8:.1f}" y="{(ay + cy_b) / 2 + 6:.1f}" text-anchor="end" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(h_lbl)}</text>',
        ])
    else:  # sphere
        cy, r = 92, 62
        parts.extend([
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WATER}" fill-opacity="0.6" stroke="{STROKE}" stroke-width="2.2"/>',
            f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="18" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4,3"/>',
            f'<path d="M {cx - r},{cy} A {r},18 0 0,0 {cx + r},{cy}" fill="none" stroke="{BLUE}" stroke-width="1.8"/>',
            f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{RED}" stroke-width="2.2"/>',
            f'<circle cx="{cx}" cy="{cy}" r="3" fill="{RED}"/>',
            f'<text x="{cx + r / 2:.1f}" y="{cy - 7}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(r_lbl)}</text>',
        ])
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 8}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_parallel_transversal(lbl1: str, lbl2: str, mode: str = "alt_int", lbl3: str = "") -> str:
    """Parallel lines cut by a transversal (alt_int, corr, co_int) or triangle exterior angle (ext_tri)."""
    w, h = 320, 178
    if mode == "ext_tri":
        parts = [
            f'<line x1="42" y1="142" x2="286" y2="142" stroke="{STROKE}" stroke-width="2.2"/>',
            f'<polygon points="68,142 142,38 214,142" fill="{WATER}" fill-opacity="0.5" stroke="{STROKE}" stroke-width="2.2" stroke-linejoin="round"/>',
            f'<text x="95" y="133" font-size="12" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>',
            f'<text x="142" y="68" text-anchor="middle" font-size="12" font-weight="800" fill="{GREEN}">{esc(lbl2)}</text>',
            f'<text x="236" y="133" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl3)}</text>',
        ]
        return _wrap_nafes_svg(w, h, "".join(parts))

    y1, y2 = 54, 130
    parts = [
        f'<line x1="36" y1="{y1}" x2="284" y2="{y1}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<line x1="36" y1="{y2}" x2="284" y2="{y2}" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<polygon points="260,{y1} 250,{y1 - 5} 250,{y1 + 5}" fill="{STROKE}"/>',
        f'<polygon points="260,{y2} 250,{y2 - 5} 250,{y2 + 5}" fill="{STROKE}"/>',
        f'<line x1="196" y1="18" x2="112" y2="164" stroke="{BLUE}" stroke-width="2.3"/>',
    ]
    # Intersection 1 at y1=54: x = 196 - (36/146)*84 = 175.3; Intersection 2 at y2=130: x = 131.6
    if mode == "corr":
        parts.append(f'<text x="192" y="{y1 - 8}" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="148" y="{y2 - 8}" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    elif mode == "co_int":
        parts.append(f'<text x="184" y="{y1 + 19}" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="150" y="{y2 - 8}" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    else:  # alt_int
        parts.append(f'<text x="156" y="{y1 + 19}" text-anchor="end" font-size="12.5" font-weight="800" fill="{BLUE}">{esc(lbl1)}</text>')
        parts.append(f'<text x="150" y="{y2 - 8}" font-size="12.5" font-weight="800" fill="{RED}">{esc(lbl2)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_similar_triangles(s1_a: str, s1_b: str, s2_a: str, s2_b: str, nested: bool = False) -> str:
    """Similar triangles diagram: either side-by-side pair or nested parallel-segment triangle."""
    w, h = 340, 176
    if nested:
        parts = [
            f'<polygon points="56,144 170,28 284,144" fill="#f8fafc" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
            f'<polygon points="108,91 170,28 232,91" fill="{SHADE}" fill-opacity="0.58" stroke="{BLUE}" stroke-width="2" stroke-linejoin="round"/>',
            f'<text x="170" y="86" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(s1_b)}</text>',
            f'<text x="170" y="162" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RED}">{esc(s2_b)}</text>',
            f'<text x="128" y="58" text-anchor="end" font-size="12" font-weight="800" fill="{BLUE}">{esc(s1_a)}</text>',
            f'<text x="72" y="118" text-anchor="end" font-size="12" font-weight="800" fill="{STROKE}">{esc(s2_a)}</text>',
        ]
        return _wrap_nafes_svg(w, h, "".join(parts))

    parts = [
        f'<polygon points="34,138 34,68 118,138" fill="{WATER}" fill-opacity="0.6" stroke="{STROKE}" stroke-width="2" stroke-linejoin="round"/>',
        f'<rect x="34" y="128" width="10" height="10" fill="none" stroke="{STROKE}" stroke-width="1.3"/>',
        f'<text x="26" y="108" text-anchor="end" font-size="12" font-weight="800" fill="{BLUE}">{esc(s1_a)}</text>',
        f'<text x="76" y="156" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(s1_b)}</text>',
        f'<text x="148" y="102" text-anchor="middle" font-size="16" font-weight="800" fill="{MUTED}">~</text>',
        f'<polygon points="184,144 184,34 312,144" fill="{SHADE}" fill-opacity="0.58" stroke="{STROKE}" stroke-width="2.1" stroke-linejoin="round"/>',
        f'<rect x="184" y="132" width="12" height="12" fill="none" stroke="{STROKE}" stroke-width="1.4"/>',
        f'<text x="176" y="94" text-anchor="end" font-size="12.5" font-weight="800" fill="{RED}">{esc(s2_a)}</text>',
        f'<text x="248" y="162" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(s2_b)}</text>',
    ]
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_sector_or_ring(r_lbl: str, extra_lbl: str, sweep_deg: float = 90.0, ring: bool = False) -> str:
    """Shaded circular sector (angle sweep_deg) or shaded concentric annulus ring."""
    w, h = 280, 180
    cx, cy, r = 140, 92, 64
    if ring:
        r_in = 36
        parts = [
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SHADE}" fill-opacity="0.78" stroke="{STROKE}" stroke-width="2"/>',
            f'<circle cx="{cx}" cy="{cy}" r="{r_in}" fill="#ffffff" stroke="{STROKE}" stroke-width="2"/>',
            f'<line x1="{cx}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{RED}" stroke-width="2"/>',
            f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r_in}" stroke="{BLUE}" stroke-width="2"/>',
            f'<circle cx="{cx}" cy="{cy}" r="2.8" fill="{STROKE}"/>',
            f'<text x="{cx + r / 2:.1f}" y="{cy + 15}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{RED}">{esc(r_lbl)}</text>',
            f'<text x="{cx - 8}" y="{cy - r_in / 2 + 4:.1f}" text-anchor="end" font-size="11.5" font-weight="800" fill="{BLUE}">{esc(extra_lbl)}</text>',
        ]
        return _wrap_nafes_svg(w, h, "".join(parts))

    a1 = math.radians(-90)
    a2 = math.radians(-90 + sweep_deg)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
    large = 1 if sweep_deg > 180 else 0
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.9"/>',
        f'<path d="M {cx} {cy} L {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f} Z" fill="{SHADE}" fill-opacity="0.82" stroke="{STROKE}" stroke-width="2"/>',
        f'<circle cx="{cx}" cy="{cy}" r="3" fill="{STROKE}"/>',
        f'<text x="{cx - 8}" y="{cy - r / 2:.1f}" text-anchor="end" font-size="12" font-weight="800" fill="{BLUE}">{esc(r_lbl)}</text>',
        f'<text x="{cx + 22}" y="{cy - 14}" font-size="12" font-weight="800" fill="{RED}">{esc(extra_lbl)}</text>',
    ]
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_histogram(bins: list[tuple[str, int, str]], title: str = "") -> str:
    """Contiguous grouped frequency histogram (touching bars with interval labels)."""
    w, h = 340, 188
    x0, y0, x1, y1 = 46, 30, 314, 150
    max_v = max(max(v for _, v, _ in bins), 1)
    n = max(1, len(bins))
    bw = (x1 - x0) / n
    parts = []
    if title:
        parts.append(f'<text x="{w / 2:.1f}" y="18" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(title)}</text>')
    for step in range(5):
        gy = y1 - (step / 4) * (y1 - y0)
        gv = round((step / 4) * max_v)
        parts.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="{GRID}" stroke-width="1"/>')
        parts.append(f'<text x="{x0 - 7}" y="{gy + 4:.1f}" text-anchor="end" font-size="10.5" fill="{MUTED}">{gv}</text>')
    palette = ["#bfdbfe", "#93c5fd", "#c4b5fd", "#a7f3d0", "#fde68a"]
    for i, (lbl, v, disp) in enumerate(bins):
        bx = x0 + i * bw
        bh = max(6.0, (v / max_v) * (y1 - y0 - 8))
        by = y1 - bh
        fc = "#fed7aa" if disp == "?" else palette[i % len(palette)]
        parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{fc}" stroke="{STROKE}" stroke-width="1.7"/>')
        parts.append(f'<text x="{bx + bw / 2:.1f}" y="{by - 5:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{RED if disp == "?" else STROKE}">{esc(disp)}</text>')
        parts.append(f'<text x="{bx + bw / 2:.1f}" y="{y1 + 17}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{STROKE}" stroke-width="1.8"/>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_code_slots(slots: list[str], caption: str = "") -> str:
    """Combinatorics slot boxes for Permutations P(n, r) and Combinations C(n, r)."""
    n = max(1, len(slots))
    cw, gap = 58, 12
    total_w = n * cw + (n - 1) * gap
    w = max(290, total_w + 52)
    h = 118 if caption else 96
    ox = (w - total_w) / 2
    parts = []
    for i, lbl in enumerate(slots):
        bx = ox + i * (cw + gap)
        parts.append(f'<rect x="{bx:.1f}" y="22" width="{cw}" height="44" rx="8" fill="#e0f2fe" stroke="{BLUE}" stroke-width="2"/>')
        parts.append(f'<text x="{bx + cw / 2:.1f}" y="49" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{esc(lbl)}</text>')
        if i < n - 1:
            parts.append(f'<text x="{bx + cw + gap / 2:.1f}" y="49" text-anchor="middle" font-size="13" font-weight="800" fill="{MUTED}">×</text>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 14}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def svg_g9_marble_bag(groups: list[tuple[str, int, str]], caption: str = "") -> str:
    """Probability urn/bag displaying counts of colored marbles/tokens for compound probability."""
    w, h = 320, (158 if caption else 138)
    parts = [
        f'<rect x="28" y="18" width="264" height="96" rx="16" fill="#f8fafc" stroke="{STROKE}" stroke-width="2"/>',
    ]
    ncols = max(1, len(groups))
    cw = 248 / ncols
    for idx, (name, cnt, fill_c) in enumerate(groups):
        cx = 36 + (idx + 0.5) * cw
        parts.append(f'<circle cx="{cx:.1f}" cy="52" r="18" fill="{fill_c}" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(f'<text x="{cx:.1f}" y="57" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{cnt}</text>')
        parts.append(f'<text x="{cx:.1f}" y="94" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(name)}</text>')
    if caption:
        parts.append(f'<text x="{w / 2:.1f}" y="{h - 10}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(caption)}</text>')
    return _wrap_nafes_svg(w, h, "".join(parts))


def _lesson_3_1() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-01",
        level=LEVEL,
        unit_num="3.1",
        topic="Numbers & Operations",
        title_en="Real Numbers, Radical Simplification, Laws of Exponents & Scientific Notation",
        title_ar="الأعداد الحقيقية، تبسيط الجذور التربيعية، قوانين الأسس، والصيغة العلمية",
        summary_en=(
            "Classify rational and irrational real numbers, locate non-perfect square roots between consecutive integers, "
            "simplify and combine square-root radicals, apply integer and negative laws of exponents, and compute with scientific notation."
        ),
        summary_ar=(
            "تصنيف الأعداد الحقيقية إلى نسبية وغير نسبية، وحصر الجذور الصمّاء بين عددين صحيحين متتاليين، وتبسيط الجذور التربيعية "
            "وجمعها وضربها، وتطبيق قوانين الأسس الصحيحة والسالبة، وإجراء العمليات بالصيغة العلمية."
        ),
        goals_en=[
            f"Distinguish rational numbers (terminating or repeating decimals) from irrational numbers such as {m(r'\pi')} and non-perfect {m(r'\sqrt{n}')}, and bound {m(r'\sqrt{n}')} between consecutive integers.",
            f"Simplify square roots by extracting largest square factors {m(r'\sqrt{k^2 b} = k\sqrt{b}')} and combine like radicals {m(r'a\sqrt{b} \pm c\sqrt{b}')}.",
            f"Apply product, power, quotient, zero, and negative exponent rules: {m(r'a^m \cdot a^n = a^{m+n}')}, {m(r'(a^m)^n = a^{mn}')}, and {m(r'a^{-n} = \frac{1}{a^n}')}.",
            f"Convert very large and very small numbers to standard scientific notation {m(r'a \times 10^k')} with {m(r'1 \le |a| < 10')} and evaluate products and quotients.",
        ],
        goals_ar=[
            f"التمييز بين الأعداد النسبية (العشرية المنتهية أو الدورية) وغير النسبية مثل {m(r'\pi')} والجذور غير المربعة {m(r'\sqrt{n}')}، وحصر {m(r'\sqrt{n}')} بين عددين صحيحين متتاليين.",
            f"تبسيط الجذور التربيعية باستخراج أكبر مربع كامل {m(r'\sqrt{k^2 b} = k\sqrt{b}')} وجمع وطرح الجذور المتشابهة {m(r'a\sqrt{b} \pm c\sqrt{b}')}.",
            f"تطبيق قوانين ضرب وقسمة وقوة الأسس والأس الصفري والسالب: {m(r'a^m \cdot a^n = a^{m+n}')} و{m(r'(a^m)^n = a^{mn}')} و{m(r'a^{-n} = \frac{1}{a^n}')}.",
            f"تحويل الأعداد الكبيرة جداً والصغيرة جداً إلى الصيغة العلمية القياسية {m(r'a \times 10^k')} حيث {m(r'1 \le |a| < 10')} وحساب ضربها وقسمتها.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Rational vs Irrational Numbers & Bounding Square Roots",
                title_ar="١. الأعداد النسبية وغير النسبية وحصر الجذور التربيعية",
                body_en=(
                    f"Every **rational number** can be written as a fraction {m(r'\frac{p}{q}')} ({m(r'q \ne 0')}), including integers, "
                    f"terminating decimals ({m('0.375')}), repeating decimals ({m(r'0.\overline{3} = \frac{1}{3}')}), and exact roots of perfect squares "
                    f"({m(r'\sqrt{49} = 7')}). If {m('n')} is not a perfect square, {m(r'\sqrt{n}')} is **irrational**. To locate {m(r'\sqrt{n}')} on the number line, "
                    f"trap {m('n')} between two consecutive perfect squares {m(r'k^2 < n < (k+1)^2')}, then compare distances to {m(r'k^2')} and {m(r'(k+1)^2')}."
                ),
                body_ar=(
                    f"كل **عدد نسبي** يُكتب على صورة كسر اعتيادي {m(r'\frac{p}{q}')} ({m(r'q \ne 0')})، ويشمل الأعداد الصحيحة، والكسور العشرية المنتهية "
                    f"({m('0.375')})، والدورية ({m(r'0.\overline{3} = \frac{1}{3}')})، وجذور المربعات الكاملة ({m(r'\sqrt{49} = 7')}). أما إذا لم يكن {m('n')} "
                    f"مربعاً كاملاً فإن {m(r'\sqrt{n}')} **عدد غير نسبي**. ولحصر {m(r'\sqrt{n}')} نجد مربعين كاملين متتاليين {m(r'k^2 < n < (k+1)^2')} فنستنتج {m(r'k < \sqrt{n} < k+1')}."
                ),
                formula_en=dm(r"k^2 < n < (k+1)^2 \implies k < \sqrt{n} < k + 1"),
                caption_ar="قاعدة حصر الجذر التربيعي غير الكامل بين عددين صحيحين متتاليين:",
                formula_math_ar=dm(r"k^2 < n < (k+1)^2 \implies k < \sqrt{n} < k + 1"),
                diagram_en=svg_g9_real_number_line([5, 6, 7, 8], math.sqrt(40), "√40", "36 < 40 < 49  ⇒  6 < √40 < 7"),
                diagram_ar=svg_g9_real_number_line([5, 6, 7, 8], math.sqrt(40), "√40", "36 < 40 < 49  ⇐  6 < √40 < 7"),
            ),
            nafes_concept(
                title_en="2. Simplifying, Adding & Multiplying Square-Root Radicals",
                title_ar="٢. تبسيط الجذور التربيعية وجمعها وضربها",
                body_en=(
                    f"To simplify {m(r'\sqrt{n}')}, factor out the **largest perfect square** {m(r'k^2')} dividing {m('n')}: "
                    f"{m(r'\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}')}. Radicals can be added or subtracted **only when their radicands match** "
                    f"after simplification ({m(r'a\sqrt{b} \pm c\sqrt{b} = (a \pm c)\sqrt{b}')}). For multiplication and division of positive radicands, "
                    f"combine directly under one radical: {m(r'\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}')}."
                ),
                body_ar=(
                    f"لتبسيط {m(r'\sqrt{n}')} نحلّل العدد إلى **أكبر مربع كامل** مضروبٍ في عامل خالٍ من المربعات: {m(r'\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}')}. "
                    f"لا تُجمع الجذور ولا تُطرح إلا إذا كانت **متشابهة** (لها نفس ما تحت الجذر بعد التبسيط): {m(r'a\sqrt{b} \pm c\sqrt{b} = (a \pm c)\sqrt{b}')}. "
                    f"أما في الضرب والقسمة فنضرب ما تحت الجذرين مباشرة: {m(r'\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}')}."
                ),
                formula_en=dm(r"\sqrt{k^2 b} = k\sqrt{b} \;(k > 0), \qquad a\sqrt{b} \pm c\sqrt{b} = (a \pm c)\sqrt{b}"),
                caption_ar="تبسيط الجذور التربيعية وجمع الجذور المتشابهة:",
                formula_math_ar=dm(r"\sqrt{k^2 b} = k\sqrt{b}, \qquad a\sqrt{b} \pm c\sqrt{b} = (a \pm c)\sqrt{b}"),
                diagram_en=svg_function_machine("√72 + √18", "6√2 + 3√2", "(6 + 3)√2", "9√2"),
            ),
            nafes_concept(
                title_en="3. Integer Exponent Laws & Scientific Notation",
                title_ar="٣. قوانين الأسس الصحيحة والصيغة العلمية",
                body_en=(
                    f"For any nonzero base {m('a')}: multiplying powers **adds** exponents ({m(r'a^m \cdot a^n = a^{m+n}')}), dividing **subtracts** exponents "
                    f"({m(r'\frac{a^m}{a^n} = a^{m-n}')}), a power of a power **multiplies** exponents ({m(r'(a^m)^n = a^{mn}')}), {m(r'a^0 = 1')}, and "
                    f"{m(r'a^{-n} = \frac{1}{a^n}')}. In **scientific notation** {m(r'c \times 10^k')}, the coefficient must satisfy {m(r'1 \le |c| < 10')}; "
                    f"if multiplying coefficients gives {m(r'c \ge 10')}, divide {m('c')} by {m('10')} and add {m('1')} to the exponent {m('k')}."
                ),
                body_ar=(
                    f"لأي أساس غير صفري {m('a')}: عند ضرب القوى **نجمع الأسس** ({m(r'a^m \cdot a^n = a^{m+n}')})، وعند القسمة **نطرح الأسس** "
                    f"({m(r'\frac{a^m}{a^n} = a^{m-n}')})، وعند رفع قوة لقوة **نضرب الأسس** ({m(r'(a^m)^n = a^{mn}')})، كما أن {m(r'a^0 = 1')} و{m(r'a^{-n} = \frac{1}{a^n}')}. "
                    f"وفي **الصيغة العلمية** {m(r'c \times 10^k')} يجب أن يحقق المعامل الشرط {m(r'1 \le |c| < 10')}؛ فإذا نتج معامل أكبر من أو يساوي {m('10')} نقسمه على {m('10')} ونزيد الأس {m('1')}."
                ),
                formula_en=dm(r"a^m \cdot a^n = a^{m+n}, \quad \frac{a^m}{a^n} = a^{m-n}, \quad a^{-n} = \frac{1}{a^n}, \quad 1 \le |c| < 10"),
                caption_ar="قوانين الأسس الصحيحة وشرط الصيغة العلمية القياسية:",
                formula_math_ar=dm(r"a^m \cdot a^n = a^{m+n}, \quad (a^m)^n = a^{mn}, \quad a^{-n} = \frac{1}{a^n}"),
                diagram_en=svg_nafes_function_table(
                    ["Rule", "Expression", "Simplified"],
                    [["Product", "2³ · 2⁴", "2⁷ = 128"], ["Negative", "5⁻²", "1/25"], ["Sci. Not.", "45,000", "4.5 × 10⁴"]],
                ),
                diagram_ar=svg_nafes_function_table(
                    ["القاعدة", "العبارة", "التبسيط"],
                    [["ضرب القوى", "2³ · 2⁴", "2⁷ = 128"], ["أس سالب", "5⁻²", "1/25"], ["صيغة علمية", "45,000", "4.5 × 10⁴"]],
                ),
            ),
        ],
        traps_en=[
            f"Adding radicands directly: {m(r'\sqrt{9} + \sqrt{16} = 3 + 4 = 7')}, NOT {m(r'\sqrt{25} = 5')}! Never write {m(r'\sqrt{a} + \sqrt{b} = \sqrt{a+b}')}.",
            f"Confusing a negative exponent with a negative sign: {m(r'3^{-2} = \frac{1}{9}')} (positive!), NOT {m('-9')} or {m('-6')}.",
            f"Leaving scientific notation un-normalized: {m(r'24 \times 10^5')} is NOT standard scientific notation because {m('24 \\ge 10')}; rewrite it as {m(r'2.4 \times 10^6')}.",
        ],
        traps_ar=[
            f"جمع ما تحت الجذرين مباشرة: {m(r'\sqrt{9} + \sqrt{16} = 3 + 4 = 7')} وليس {m(r'\sqrt{25} = 5')}! الجذر لا يتوزع على الجمع أو الطرح.",
            f"الخلط بين الأس السالب والإشارة السالبة: {m(r'3^{-2} = \frac{1}{9}')} عدد موجب، وليس {m('-9')} أو {m('-6')}.",
            f"ترك الصيغة العلمية دون ضبط المعامل: {m(r'24 \times 10^5')} ليست بالصيغة القياسية لأن {m('24 \\ge 10')}، والصواب {m(r'2.4 \times 10^6')}.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-01-EX1",
                title_en="Nearest Integer to an Irrational Square Root",
                title_ar="أقرب عدد صحيح لجذر تربيعي غير نسبي",
                q_en=f"On the real number line, which integer is closest to the irrational number {m(r'\sqrt{53}')}?",
                q_ar=f"على خط الأعداد الحقيقية، ما العدد الصحيح الأقرب إلى العدد غير النسبي {m(r'\sqrt{53}')}؟",
                correct_val=7,
                distractors=[6, 8, 9],
                idea_en=f"Bound {m('53')} between two consecutive perfect squares {m('49')} and {m('64')}, then compare how far {m('53')} is from each!",
                steps_en=[
                    f"Notice that {m('7^2 = 49')} and {m('8^2 = 64')}, so {m('49 < 53 < 64')} and therefore {m(r'7 < \sqrt{53} < 8')}.",
                    f"Compare distances to the two perfect squares: {m('53 - 49 = 4')} whereas {m('64 - 53 = 11')}.",
                    f"Because {m('53')} is much closer to {m('49')} than to {m('64')}, {m(r'\sqrt{53}')} is closest to {m('7')}.",
                ],
                check_en=f"{m('7.5^2 = 56.25 > 53')}, confirming {m(r'\sqrt{53} < 7.5')}, so it rounds to {m('7')}.",
                idea_ar=f"نحصر {m('53')} بين المربعين الكاملين المتتاليين {m('49')} و{m('64')}، ثم نقارن المسافة إلى كلٍّ منهما!",
                steps_ar=[
                    f"بما أن {m('7^2 = 49')} و{m('8^2 = 64')} فإن {m('49 < 53 < 64')}، ومنه {m(r'7 < \sqrt{53} < 8')}.",
                    f"الفرق عن {m('49')} هو {m('53 - 49 = 4')}، بينما الفرق عن {m('64')} هو {m('64 - 53 = 11')}.",
                    f"إذن العدد {m(r'\sqrt{53}')} أقرب إلى العدد الصحيح {m('7')}.",
                ],
                check_ar=f"{m('7.5^2 = 56.25 > 53')}، أي أن {m(r'\sqrt{53} < 7.5')} فهو أقرب إلى {m('7')}.",
                diagram_en=svg_g9_real_number_line([6, 7, 8, 9], math.sqrt(53), "√53", "49 < 53 < 64"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-01-EX2",
                title_en="Combining Simplified Square-Root Radicals",
                title_ar="تبسيط وجمع الجذور التربيعية المتشابهة",
                q_en=f"Simplify the radical expression {m(r'3\sqrt{50} - 2\sqrt{18} + \sqrt{8}')}.",
                q_ar=f"بسّط العبارة الجذرية {m(r'3\sqrt{50} - 2\sqrt{18} + \sqrt{8}')} في أبسط صورة.",
                correct_val=r"11\sqrt{2}",
                distractors=[r"9\sqrt{2}", r"21\sqrt{2}", r"2\sqrt{40}"],
                idea_en=f"Extract the largest perfect-square factor from {m('50')}, {m('18')}, and {m('8')} so every term becomes a multiple of {m(r'\sqrt{2}')}!",
                steps_en=[
                    f"Rewrite each radical: {m(r'3\sqrt{50} = 3\sqrt{25 \times 2} = 15\sqrt{2}')}, {m(r'2\sqrt{18} = 2\sqrt{9 \times 2} = 6\sqrt{2}')}, and {m(r'\sqrt{8} = \sqrt{4 \times 2} = 2\sqrt{2}')}.",
                    f"Combine coefficients of {m(r'\sqrt{2}')}: {m(r'(15 - 6 + 2)\sqrt{2} = 11\sqrt{2}')}.",
                ],
                check_en=f"Approximation check: {m(r'3(7.07) - 2(4.24) + 2.83 \approx 15.56 \approx 11(1.414)')}.",
                idea_ar=f"نحلّل الأعداد {m('50')} و{m('18')} و{m('8')} لاستخراج أكبر مربع كامل فيتحول كل حد إلى مضاعف لـ {m(r'\sqrt{2}')}!",
                steps_ar=[
                    f"نبسّط كل جذر: {m(r'3\sqrt{25 \times 2} = 15\sqrt{2}')}، و{m(r'2\sqrt{9 \times 2} = 6\sqrt{2}')}، و{m(r'\sqrt{4 \times 2} = 2\sqrt{2}')}.",
                    f"نجمع معاملات الجذور المتشابهة: {m(r'(15 - 6 + 2)\sqrt{2} = 11\sqrt{2}')}.",
                ],
                check_ar=f"جميع الحدود أصبحت متشابهة تحت الجذر {m(r'\sqrt{2}')} والمجموع {m('15 - 6 + 2 = 11')}.",
                diagram_en=svg_function_machine("3√50 − 2√18 + √8", "15√2 − 6√2 + 2√2", "(15−6+2)√2", "?"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-01-EX3",
                title_en="Evaluating Multi-Step Integer Exponent Quotients",
                title_ar="تبسيط عبارات القوى والأسس الصحيحة",
                q_en=f"What is the exact value of {m(r'\frac{2^5 \times (2^3)^2}{2^8}')}?",
                q_ar=f"ما القيمة الدقيقة للعبارة الأسية {m(r'\frac{2^5 \times (2^3)^2}{2^8}')}؟",
                correct_val=8,
                distractors=[4, 16, 32],
                idea_en="Simplify power-of-a-power first by multiplying exponents, add exponents in the numerator, then subtract the denominator's exponent!",
                steps_en=[
                    f"By the power rule, {m(r'(2^3)^2 = 2^{3 \times 2} = 2^6')}.",
                    f"Multiply in the numerator: {m(r'2^5 \times 2^6 = 2^{5 + 6} = 2^{11}')}.",
                    f"Divide by {m(r'2^8')}: {m(r'2^{11 - 8} = 2^3 = 8')}.",
                ],
                check_en=f"Direct check: {m(r'\frac{32 \times 64}{256} = \frac{2048}{256} = 8')}.",
                idea_ar="نطبّق قانون قوة القوة بضرب الأسس أولاً، ثم نجمع أسس البسط، وأخيراً نطرح أس المقام!",
                steps_ar=[
                    f"بقانون قوة القوة: {m(r'(2^3)^2 = 2^{3 \times 2} = 2^6')}.",
                    f"نضرب في البسط بجمع الأسس: {m(r'2^5 \times 2^6 = 2^{11}')}.",
                    f"نقسم بطرح الأسس: {m(r'2^{11 - 8} = 2^3 = 8')}.",
                ],
                check_ar=f"تحقق عددي مباشر: {m(r'\frac{32 \times 64}{256} = 8')}.",
                diagram_en=svg_number_strip(["2⁵ × (2³)²", "2⁵ × 2⁶ = 2¹¹", "2¹¹ ÷ 2⁸", "?"]),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-01-EX4",
                title_en="Multiplying & Normalizing Scientific Notation",
                title_ar="الضرب والكتابة بالصيغة العلمية القياسية",
                q_en=f"Express the product {m(r'(4 \times 10^5)(7.5 \times 10^{-2})')} in standard scientific notation.",
                q_ar=f"اكتب ناتج الضرب {m(r'(4 \times 10^5)(7.5 \times 10^{-2})')} بالصيغة العلمية القياسية.",
                correct_val=r"3 \times 10^4",
                distractors=[r"30 \times 10^3", r"3 \times 10^3", r"3 \times 10^2"],
                idea_en=f"Multiply the coefficients and add the powers of {m('10')}, then normalize the coefficient into {m('[1, 10)')}!",
                steps_en=[
                    f"Multiply coefficients and powers of {m('10')}: {m(r'(4 \times 7.5) \times 10^{5 + (-2)} = 30 \times 10^3')}.",
                    f"Since {m('30 \\ge 10')}, rewrite {m(r'30 = 3 \times 10^1')}, giving {m(r'3 \times 10^{1 + 3} = 3 \times 10^4')}.",
                ],
                check_en=f"Standard form check: {m('400{,}000 \\times 0.075 = 30{,}000 = 3 \\times 10^4')}.",
                idea_ar=f"نضرب المعاملات معاً ونجمع أسس العدد {m('10')}، ثم نضبط المعامل ليقع في الفترة {m('[1, 10)')}!",
                steps_ar=[
                    f"نضرب المعاملين ونجمع الأسين: {m(r'(4 \times 7.5) \times 10^{5 - 2} = 30 \times 10^3')}.",
                    f"بما أن {m('30 \\ge 10')} نكتب {m(r'30 = 3 \times 10^1')}، فيصبح الناتج {m(r'3 \times 10^4')}.",
                ],
                check_ar=f"تحقق بالصيغة القياسية: {m('400{,}000 \\times 0.075 = 30{,}000 = 3 \\times 10^4')}.",
                diagram_en=svg_nafes_function_table(
                    ["Factor A", "Factor B", "Standard Product"],
                    [["4 × 10⁵", "7.5 × 10⁻²", "?"]],
                    highlight_cell=(0, 2),
                ),
            ),
        ],
        blueprints=["G9-NUM-01", "G9-NUM-02", "G9-NUM-03", "G9-NUM-04"],
    )


def _lesson_3_2() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-02",
        level=LEVEL,
        unit_num="3.2",
        topic="Numbers & Operations",
        title_en="Successive Percent Change, Direct/Inverse Variation & Proportional Mixture/Rate Models",
        title_ar="التغير المئوي المتتابع، التغير الطردي والعكسي، ونماذج المعدلات والتناسب",
        summary_en=(
            "Chain successive discounts and 15% VAT multipliers, recover original prices, distinguish direct variation (y = kx) "
            "from inverse variation (xy = k), solve combined work and relative motion problems, and compute ratio partitions and mixtures."
        ),
        summary_ar=(
            "حساب التغيرات المئوية المتتابعة والخصومات وضريبة القيمة المضافة (15%) وإيجاد السعر الأصلي، والتمييز بين التغير الطردي "
            "والتغير العكسي، وحل مسائل العمل المشترك والحركة النسبية، وتقسيم النسب وحساب تراكيز المخاليط."
        ),
        goals_en=[
            f"Model successive percentage increases/decreases and Saudi VAT ({m('15\\%')}) using multiplicative factors {m(r'P_{\text{new}} = P_0(1 \pm r_1)(1 \pm r_2)')} and find original prices by division.",
            f"Identify and solve **direct variation** ({m('y = kx')}, constant ratio {m('y/x')}) and **inverse variation** ({m('xy = k')}, constant product {m('x \\cdot y')}).",
            f"Add unit rates for combined work/pipes ({m(r'\frac{1}{a} + \frac{1}{b} = \frac{1}{t}')}) and use relative speed ({m('v_1 + v_2')} opposite, {m('|v_1 - v_2|')} same direction).",
            f"Partition totals into multi-part ratios {m('a : b : c')} and compute weighted mixture concentrations.",
        ],
        goals_ar=[
            f"تمثيل الزيادة والنقصان المئوي المتتابع وضريبة القيمة المضافة ({m('15\\%')}) بضرب المعاملات {m(r'P_0(1 \pm r_1)(1 \pm r_2)')} وإيجاد السعر الأصلي بالقسمة.",
            f"التمييز بين **التغير الطردي** ({m('y = kx')} حيث النسبة ثابتة) و**التغير العكسي** ({m('xy = k')} حيث حاصل الضرب ثابت) وحل مسائل كلٍّ منهما.",
            f"جمع معدلات الإنجاز في مسائل العمل والصنابير ({m(r'\frac{1}{a} + \frac{1}{b} = \frac{1}{t}')}) واستخدام السرعة النسبية في الحركة.",
            f"تقسيم الكميات وفق نسب متعددة {m('a : b : c')} وحساب النسبة المئوية لتركيز المخاليط الموزونة.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Successive Percent Multipliers, VAT (15%) & Original Price",
                title_ar="١. معاملات التغير المئوي المتتابع، ضريبة القيمة المضافة (15%) والسعر الأصلي",
                body_en=(
                    f"Convert every percentage change into a decimal multiplier: a {m('20\\%')} discount multiplies by {m('1 - 0.20 = 0.80')}, "
                    f"and a {m('15\\%')} VAT multiplies by {m('1 + 0.15 = 1.15')}. Chain successive changes by **multiplying** their factors — "
                    f"never by adding percentages! To recover an unknown **original price** {m('P_0')} from a final price {m(r'P_{\text{final}}')}, "
                    f"**divide** {m(r'P_{\text{final}}')} by the combined multiplier."
                ),
                body_ar=(
                    f"نحوّل كل تغير مئوي إلى معامل ضربي: خصم {m('20\\%')} يعني الضرب في {m('0.80')}، وضريبة القيمة المضافة {m('15\\%')} تعني الضرب في {m('1.15')}. "
                    f"عند تعاقب تغيرين مئويين **نضرب المعاملين** ولا نجمع النسبتين المئويتين أبداً! ولإيجاد **السعر الأصلي** {m('P_0')} من السعر النهائي نقسم على المعامل الكلي."
                ),
                formula_en=dm(r"P_{\text{final}} = P_0 (1 - d)(1 + v) \implies P_0 = \frac{P_{\text{final}}}{(1 - d)(1 + v)}"),
                caption_ar="قانون التغير المئوي المتتابع واسترجاع السعر الأصلي:",
                formula_math_ar=dm(r"P_{\text{final}} = P_0 (1 - d)(1 + v), \qquad P_0 = \frac{P_{\text{final}}}{(1 - d)(1 + v)}"),
                diagram_en=svg_function_machine("P₀", "× 0.80 (−20%)", "× 1.15 (+15% VAT)", "0.92 P₀"),
            ),
            nafes_concept(
                title_en="2. Direct Variation (y = kx) vs Inverse Variation (xy = k)",
                title_ar="٢. التغير الطردي (y = kx) مقابل التغير العكسي (xy = k)",
                body_en=(
                    f"Two quantities vary **directly** when their ratio is constant ({m(r'\frac{y_1}{x_1} = \frac{y_2}{x_2} = k')}), such as distance vs time at fixed speed. "
                    f"They vary **inversely** when their product is constant ({m('x_1 y_1 = x_2 y_2 = k')}), such as the number of identical workers/pumps "
                    f"and the hours needed to finish a fixed job, or gear teeth and revolutions per minute."
                ),
                body_ar=(
                    f"تتغير كميتان **طردياً** إذا كانت نسبتهما ثابتة ({m(r'\frac{y_1}{x_1} = \frac{y_2}{x_2} = k')}) مثل المسافة والزمن عند ثبات السرعة. "
                    f"وتتغيران **عكسياً** إذا كان حاصل ضربهما ثابتاً ({m('x_1 y_1 = x_2 y_2 = k')}) مثل عدد العمال أو المضخات المتماثلة وزمن إنجاز العمل نفسه."
                ),
                formula_en=dm(r"\text{Direct: } \frac{y_1}{x_1} = \frac{y_2}{x_2}, \qquad \text{Inverse: } x_1 y_1 = x_2 y_2"),
                caption_ar="مقارنة معادلتي التغير الطردي والتغير العكسي:",
                formula_math_ar=dm(r"\frac{y_1}{x_1} = \frac{y_2}{x_2} \quad (\text{طردي}), \qquad x_1 y_1 = x_2 y_2 \quad (\text{عكسي})"),
                diagram_en=svg_nafes_function_table(
                    ["Workers (x)", "Hours (y)", "Product x·y"],
                    [["6", "12", "72"], ["9", "8", "72"], ["12", "6", "72"]],
                ),
                diagram_ar=svg_nafes_function_table(
                    ["العمال (x)", "الساعات (y)", "الضرب x·y"],
                    [["6", "12", "72"], ["9", "8", "72"], ["12", "6", "72"]],
                ),
            ),
            nafes_concept(
                title_en="3. Combined Work Rates, Relative Motion & Weighted Mixtures",
                title_ar="٣. معدلات العمل المشترك، الحركة النسبية، ومزج التراكيز",
                body_en=(
                    f"Never add completion times! Add **rates per hour**: if A takes {m('a')} hours and B takes {m('b')} hours, together they complete "
                    f"{m(r'\frac{1}{a} + \frac{1}{b} = \frac{1}{t}')} of the job per hour (subtract {m(r'\frac{1}{b}')} for a drain pipe). "
                    f"For two vehicles {m('d')} km apart moving toward each other, {m('t = d / (v_1 + v_2)')}. For mixing {m('m_1')} units at concentration "
                    f"{m('c_1\\%')} with {m('m_2')} units at {m('c_2\\%')}, track total pure solute: {m(r'c_{\text{mix}} = \frac{m_1 c_1 + m_2 c_2}{m_1 + m_2}')}."
                ),
                body_ar=(
                    f"لا نجمع أزمنة الإنجاز أبداً، بل نجمع **معدلات العمل في الساعة الواحدة**: {m(r'\frac{1}{a} + \frac{1}{b} = \frac{1}{t}')} (ونطرح معدل التفريغ). "
                    f"وفي الحركة المتقابلة تكون سرعة الاقتراب {m('v_1 + v_2')}. وعند خلط كميتين {m('m_1, m_2')} بتركيزين {m('c_1\\%, c_2\\%')} نحسب كمية المادة النقية الكلية مقسومةً على الحجم الكلي."
                ),
                formula_en=dm(r"\frac{1}{t} = \frac{1}{a} + \frac{1}{b}, \qquad c_{\text{mix}} = \frac{m_1 c_1 + m_2 c_2}{m_1 + m_2}"),
                caption_ar="معادلة العمل المشترك ومعادلة تركيز المزيج الموزون:",
                formula_math_ar=dm(r"\frac{1}{t} = \frac{1}{a} + \frac{1}{b}, \qquad c_{\text{mix}} = \frac{m_1 c_1 + m_2 c_2}{m_1 + m_2}"),
                diagram_en=svg_pipe_tank("+1/a hr⁻¹", "−1/b hr⁻¹"),
            ),
        ],
        traps_en=[
            f"Assuming a {m('20\\%')} increase followed by a {m('20\\%')} decrease returns to the original price: {m('1.20 \\times 0.80 = 0.96')}, which is a {m('4\\%')} net loss!",
            f"Subtracting {m('15\\%')} of the final VAT-inclusive price instead of dividing by {m('1.15')} when finding the pre-tax price.",
            f"Using a direct proportion {m('9/8 = 12/t')} on a workers-and-hours problem where more workers take **fewer** hours ({m('9 \\times 8 = 12 \\times t')}).",
        ],
        traps_ar=[
            f"الاعتقاد بأن زيادة {m('20\\%')} يتبعها خصم {m('20\\%')} يعيد السعر كما كان؛ الصواب {m('1.20 \\times 0.80 = 0.96')} أي خسارة صافية {m('4\\%')}!",
            f"طرح {m('15\\%')} من السعر الشامل للضريبة بدلاً من القسمة على {m('1.15')} عند حساب السعر قبل الضريبة.",
            f"استخدام التناسب الطردي في مسائل العمال وزمن الإنجاز؛ فزيادة العمال تقلل الزمن لذا العلاقة عكسية ({m('x_1 y_1 = x_2 y_2')}).",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-02-EX1",
                title_en="Recovering Original Price Before Discount & 15% VAT",
                title_ar="إيجاد السعر الأصلي قبل الخصم وضريبة القيمة المضافة 15%",
                q_en=(
                    f"An electronics store applies a {m('20\\%')} discount to a laptop's original price, then adds {m('15\\%')} VAT "
                    f"to the discounted price. If the customer pays {m('2{,}760')} SAR, what was the original price in SAR?"
                ),
                q_ar=(
                    f"يقدّم متجر إلكترونيات خصماً نسبته {m('20\\%')} على السعر الأصلي لحاسوب محمول، ثم يضيف ضريبة القيمة المضافة {m('15\\%')} "
                    f"على السعر بعد الخصم. إذا دفع المشتري {m('2{,}760')} ريالاً، فما السعر الأصلي بالريال؟"
                ),
                correct_val=3000,
                distractors=[2898, 2905, 3200],
                idea_en=f"Chain the two multipliers {m('0.80 \\times 1.15 = 0.92')}, then divide {m('2{,}760')} by {m('0.92')}!",
                steps_en=[
                    f"Let {m('P_0')} be the original price. After a {m('20\\%')} discount, the price is {m('0.80 P_0')}.",
                    f"Adding {m('15\\%')} VAT multiplies by {m('1.15')}: {m('0.80 \\times 1.15 P_0 = 0.92 P_0')}.",
                    f"Solve {m('0.92 P_0 = 2{,}760 \\implies P_0 = \\frac{2{,}760}{0.92} = 3{,}000')} SAR.",
                ],
                check_en=f"{m('3{,}000 \\times 0.80 = 2{,}400')} SAR; {m('2{,}400 \\times 1.15 = 2{,}760')} SAR.",
                idea_ar=f"نضرب معاملي الخصم والضريبة {m('0.80 \\times 1.15 = 0.92')} ثم نقسم المبلغ النهائي {m('2{,}760')} على {m('0.92')}!",
                steps_ar=[
                    f"نفرض السعر الأصلي {m('P_0')}. بعد خصم {m('20\\%')} يصبح السعر {m('0.80 P_0')}.",
                    f"بإضافة ضريبة {m('15\\%')} يصبح المبلغ النهائي {m('0.80 \\times 1.15 P_0 = 0.92 P_0')}.",
                    f"نقسم: {m('P_0 = 2{,}760 \\div 0.92 = 3{,}000')} ريال.",
                ],
                check_ar=f"{m('3{,}000 \\times 0.80 = 2{,}400')} ريال، ثم {m('2{,}400 \\times 1.15 = 2{,}760')} ريال.",
                diagram_en=svg_function_machine("P₀ = ?", "× 0.80", "× 1.15", "2,760 SAR"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-02-EX2",
                title_en="Inverse Variation with Identical Maintenance Pumps",
                title_ar="التغير العكسي لعدد المضخات وزمن التفريغ",
                q_en=f"At a Riyadh Metro depot, {m('9')} identical pumps empty a drainage basin in {m('8')} hours. How many hours will {m('12')} of these pumps take to empty the same basin?",
                q_ar=f"في محطة صيانة لقطار الرياض، تفرّغ {m('9')} مضخات متماثلة حوض تصريف في {m('8')} ساعات. كم ساعة تستغرق {m('12')} مضخة مماثلة لتفريغ الحوض نفسه؟",
                correct_val=6,
                distractors=[5, 9, 11],
                idea_en=f"Number of pumps and hours vary **inversely**, so their product {m('x \\cdot y')} stays constant at {m('72')} pump-hours!",
                steps_en=[
                    f"Compute total pump-hours needed: {m('k = 9 \\times 8 = 72')}.",
                    f"With {m('12')} pumps, {m('12 \\times t = 72 \\implies t = \\frac{72}{12} = 6')} hours.",
                ],
                check_en=f"Increasing pumps by a factor of {m('4/3')} multiplies time by {m('3/4')}: {m('8 \\times \\frac{3}{4} = 6')} hours.",
                idea_ar=f"العلاقة بين عدد المضخات والزمن **تغير عكسي**، فحاصل الضرب ثابت ويساوي {m('72')} ساعة-مضخة!",
                steps_ar=[
                    f"نحسب ثابت التغير العكسي: {m('k = 9 \\times 8 = 72')}.",
                    f"عند تشغيل {m('12')} مضخة: {m('12 \\times t = 72 \\implies t = 6')} ساعات.",
                ],
                check_ar=f"تحقق: {m('9 \\times 8 = 72')} و{m('12 \\times 6 = 72')}.",
                diagram_en=svg_nafes_function_table(
                    ["Pumps (x)", "Hours (y)"],
                    [["9", "8"], ["12", "?"]],
                    highlight_cell=(1, 1),
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-02-EX3",
                title_en="Combined Work Rate of Two Desalination Valves",
                title_ar="معدل العمل المشترك لصمامي تحلية",
                q_en=f"Valve A can fill a desalination tank alone in {m('6')} hours, and Valve B can fill the same tank alone in {m('12')} hours. How many hours do both valves take when opened together?",
                q_ar=f"يمتلئ خزان تحلية عبر الصمام (أ) وحده في {m('6')} ساعات، وعبر الصمام (ب) وحده في {m('12')} ساعة. كم ساعة يستغرق ملء الخزان عند فتح الصمامين معاً؟",
                correct_val=4,
                distractors=[3, 8, 9],
                idea_en=f"Add hourly fractional rates {m(r'\frac{1}{6} + \frac{1}{12}')} and take the reciprocal!",
                steps_en=[
                    f"In {m('1')} hour, Valve A fills {m(r'\frac{1}{6}')} of the tank and Valve B fills {m(r'\frac{1}{12}')}.",
                    f"Together per hour: {m(r'\frac{1}{6} + \frac{1}{12} = \frac{2 + 1}{12} = \frac{3}{12} = \frac{1}{4}')} of the tank.",
                    f"Therefore the full tank is filled in {m('t = 4')} hours.",
                ],
                check_en=f"In {m('4')} hours, A fills {m('4/6 = 2/3')} and B fills {m('4/12 = 1/3')}, totaling {m('1')} full tank.",
                idea_ar=f"نجمع معدلي الملء في الساعة الواحدة {m(r'\frac{1}{6} + \frac{1}{12}')} ثم نقلب الناتج!",
                steps_ar=[
                    f"يملأ الصمام الأول {m(r'\frac{1}{6}')} من الخزان كل ساعة، والثاني {m(r'\frac{1}{12}')} كل ساعة.",
                    f"مجموع المعدلين: {m(r'\frac{1}{6} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4}')} خزان في الساعة.",
                    f"إذن يمتلئ الخزان كاملاً في {m('t = 4')} ساعات.",
                ],
                check_ar=f"في {m('4')} ساعات يملأ الأول {m('2/3')} والثاني {m('1/3')} والمجموع خزان كامل.",
                diagram_en=svg_pipe_tank("+1/6 hr⁻¹", "+1/12 hr⁻¹"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-02-EX4",
                title_en="Weighted Saline Mixture Concentration",
                title_ar="تركيز مزيج ملحي موزون",
                q_en=f"A science lab mixes {m('3')} liters of a {m('20\\%')} salt solution with {m('2')} liters of a {m('45\\%')} salt solution. What is the salt percentage of the resulting {m('5')}-liter mixture?",
                q_ar=f"خلط فني مختبر {m('3')} لترات من محلول ملحي تركيزه {m('20\\%')} مع {m('2')} لتر من محلول ملحي تركيزه {m('45\\%')}. ما النسبة المئوية للملح في المزيج الناتج؟",
                correct_val=30,
                distractors=[25, 32, 35],
                suffix=r"\%",
                idea_en="Divide the total pure salt from both solutions by the combined volume of 5 liters!",
                steps_en=[
                    f"Pure salt from first solution: {m('3 \\times 20\\% = 0.60')} L; from second solution: {m('2 \\times 45\\% = 0.90')} L.",
                    f"Total pure salt is {m('0.60 + 0.90 = 1.50')} L inside {m('3 + 2 = 5')} L total solution.",
                    f"Mixture concentration: {m(r'\frac{1.50}{5} \times 100\% = 30\%')}.",
                ],
                check_en=f"{m('30\\%')} lies closer to {m('20\\%')} than to {m('45\\%')} in the exact {m('2:3')} inverse weight ratio.",
                idea_ar="نحسب كمية الملح النقي في المحلولين معاً ثم نقسمها على الحجم الكلي البالغ 5 لترات!",
                steps_ar=[
                    f"كمية الملح في الأول {m('3 \\times 0.20 = 0.60')} لتر، وفي الثاني {m('2 \\times 0.45 = 0.90')} لتر.",
                    f"إجمالي الملح {m('0.60 + 0.90 = 1.50')} لتر في حجم كلي قدره {m('5')} لترات.",
                    f"نسبة التركيز الجديدة: {m(r'\frac{1.50}{5} \times 100\% = 30\%')}.",
                ],
                check_ar=f"{m('3(20) + 2(45) = 60 + 90 = 150')}، وقسمة {m('150')} على {m('5')} تعطي {m('30\\%')}.",
                diagram_en=svg_nafes_function_table(
                    ["Solution", "Volume (L)", "Salt %"],
                    [["A", "3", "20%"], ["B", "2", "45%"], ["Mix", "5", "?"]],
                    highlight_cell=(2, 2),
                ),
            ),
        ],
        blueprints=["G9-NUM-05", "G9-NUM-06", "G9-NUM-07", "G9-NUM-08"],
    )


def _lesson_3_3() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-03",
        level=LEVEL,
        unit_num="3.3",
        topic="Algebra",
        title_en="Linear Equations, Inequalities, Slope-Intercept Systems, Polynomials & Quadratics",
        title_ar="المعادلات والمتباينات الخطية، أنظمة المستقيمات والميل، كثيرات الحدود، والمعادلات التربيعية",
        summary_en=(
            "Solve multi-step linear equations, absolute-value equations, and inequalities; analyze slope, parallel/perpendicular lines, "
            "and 2×2 linear systems; expand special polynomial identities; and factor quadratics to find roots and parabola vertices."
        ),
        summary_ar=(
            "حل المعادلات الخطية متعددة الخطوات ومعادلات القيمة المطلقة والمتباينات، وتحليل الميل والتوازي والتعامد وأنظمة المعادلات "
            "الخطية، وفك المتطابقات الشهيرة لكثيرات الحدود، وتحليل المعادلات التربيعية وإيجاد الجذور ورأس القطع المكافئ."
        ),
        goals_en=[
            f"Solve linear equations with variables on both sides, split {m('|ax + b| = c')} ({m('c \\ge 0')}) into two cases, and reverse inequality signs when multiplying or dividing by a negative number.",
            f"Compute slope {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')}, write {m('y = mx + b')}, identify parallel ({m('m_1 = m_2')}) and perpendicular ({m('m_1 m_2 = -1')}) lines, and solve {m('2 \\times 2')} linear systems.",
            f"Add, subtract, and multiply polynomials using special-product identities {m('(a \\pm b)^2 = a^2 \\pm 2ab + b^2')} and {m('(a - b)(a + b) = a^2 - b^2')}.",
            f"Factor quadratics {m('x^2 + bx + c = 0')} to find roots and determine the axis of symmetry {m(r'x = -\frac{b}{2a}')} and vertex extremum.",
        ],
        goals_ar=[
            f"حل المعادلات الخطية ذات المتغير في الطرفين، وفك معادلة القيمة المطلقة {m('|ax + b| = c')} لحالتين، وعكس رمز المتباينة عند الضرب أو القسمة في عدد سالب.",
            f"حساب الميل {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')} وكتابة {m('y = mx + b')}، وتمييز المستقيمات المتوازية ({m('m_1 = m_2')}) والمتعامدة ({m('m_1 m_2 = -1')})، وحل نظام معادلتين خطيتين.",
            f"جمع وضرب كثيرات الحدود وتطبيق المتطابقات التربيعية {m('(a \\pm b)^2 = a^2 \\pm 2ab + b^2')} والفرق بين مربعين {m('a^2 - b^2')}.",
            f"تحليل العبارة التربيعية {m('x^2 + bx + c = 0')} لإيجاد الجذور وتحديد معادلة محور التماثل {m(r'x = -\frac{b}{2a}')} وإحداثيي الرأس.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Multi-Step Linear Equations, Absolute Value & Inequalities",
                title_ar="١. المعادلات الخطية متعددة الخطوات، القيمة المطلقة، والمتباينات",
                body_en=(
                    f"Collect variable terms on one side and constants on the other. An absolute-value equation {m('|ax + b| = c')} with {m('c > 0')} "
                    f"splits into **two linear equations**: {m('ax + b = c')} or {m('ax + b = -c')} (if {m('c < 0')}, there is **no real solution**). "
                    f"When solving a linear inequality, **dividing or multiplying both sides by a negative number flips the inequality direction**."
                ),
                body_ar=(
                    f"نجمع الحدود المتضمنة للمتغير في طرف والثوابت في الطرف الآخر. معادلة القيمة المطلقة {m('|ax + b| = c')} عندما {m('c > 0')} تنقسم إلى "
                    f"**معادلتين**: {m('ax + b = c')} أو {m('ax + b = -c')} (وإذا كان {m('c < 0')} فمجموعة الحل خالية {m(r'\varnothing')}). وفي المتباينات **تنعكس إشارة المتباينة عند الضرب أو القسمة على عدد سالب**."
                ),
                formula_en=dm(r"|ax + b| = c \;(c \ge 0) \iff ax + b = c \;\text{ or }\; ax + b = -c"),
                caption_ar="قاعدة حل معادلة القيمة المطلقة وعكس إشارة المتباينة:",
                formula_math_ar=dm(r"|ax + b| = c \iff ax + b = c \;\;\text{أو}\;\; ax + b = -c"),
                diagram_en=svg_g9_real_number_line([-4, -2, 0, 2, 4], -2, "x ≤ −2", "−3x ≥ 6  ⇒  x ≤ −2", ray_dir=-1, closed_dot=True),
            ),
            nafes_concept(
                title_en="2. Slope, Parallel/Perpendicular Lines & 2×2 Linear Systems",
                title_ar="٢. ميل المستقيم، التوازي والتعامد، وأنظمة المعادلات الخطية",
                body_en=(
                    f"The slope through {m('(x_1, y_1)')} and {m('(x_2, y_2)')} is {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')}. In slope-intercept form {m('y = mx + b')}, "
                    f"{m('m')} is the slope and {m('b')} is the {m('y')}-intercept. Non-vertical **parallel** lines have equal slopes ({m('m_1 = m_2')}), "
                    f"while **perpendicular** lines have negative-reciprocal slopes ({m(r'm_2 = -\frac{1}{m_1}')}). Eliminate or substitute to find the intersection {m('(x, y)')} of two lines."
                ),
                body_ar=(
                    f"ميل المستقيم المار بالنقطتين {m('(x_1, y_1)')} و{m('(x_2, y_2)')} هو {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')}. في الصورة {m('y = mx + b')} يمثل {m('m')} الميل و{m('b')} المقطع الصادي. "
                    f"المستقيمان **المتوازيان** لهما نفس الميل ({m('m_1 = m_2')})، و**المتعامدان** حاصل ضرب ميليهما {m('-1')}. ويُمثّل تقاطع المستقيمين حل نظام المعادلتين بالحذف أو التعويض."
                ),
                formula_en=dm(r"m = \frac{y_2 - y_1}{x_2 - x_1}, \qquad \ell_1 \parallel \ell_2 \iff m_1 = m_2, \qquad \ell_1 \perp \ell_2 \iff m_1 m_2 = -1"),
                caption_ar="قانون الميل وشرطا التوازي والتعامد:",
                formula_math_ar=dm(r"m = \frac{y_2 - y_1}{x_2 - x_1}, \qquad m_1 = m_2 \;(\parallel), \qquad m_1 m_2 = -1 \;(\perp)"),
                diagram_en=svg_nafes_coordinate_line([(2, 3, "(2, 3)")], line_kb=(1, 1), line2_kb=(-1, 5), max_coord=6),
            ),
            nafes_concept(
                title_en="3. Special Polynomial Products, Trinomial Factoring & Parabola Vertex",
                title_ar="٣. المتطابقات التربيعية، تحليل ثلاثيات الحدود، ورأس القطع المكافئ",
                body_en=(
                    f"Memorize the three Grade 9 identities: {m('(a + b)^2 = a^2 + 2ab + b^2')}, {m('(a - b)^2 = a^2 - 2ab + b^2')}, and "
                    f"{m('(a - b)(a + b) = a^2 - b^2')}. To factor {m('x^2 + bx + c = 0')}, find two integers {m('p, q')} with {m('p + q = b')} and {m('pq = c')}, "
                    f"giving roots {m('-p')} and {m('-q')}. For {m('y = ax^2 + bx + c')}, the axis of symmetry is {m(r'x = -\frac{b}{2a}')} (also the midpoint of the roots!)."
                ),
                body_ar=(
                    f"احفظ المتطابقات الثلاث الأساسية: مربع المجموع {m('a^2 + 2ab + b^2')}، ومربع الفرق {m('a^2 - 2ab + b^2')}، والفرق بين مربعين {m('a^2 - b^2 = (a-b)(a+b)')}. "
                    f"لتحليل {m('x^2 + bx + c = 0')} نبحث عن عددين مجموعهما {m('b')} وحاصل ضربهما {m('c')}. ومعادلة محور التماثل للقطع المكافئ {m('y = ax^2 + bx + c')} هي {m(r'x = -\frac{b}{2a}')}."
                ),
                formula_en=dm(r"(a \pm b)^2 = a^2 \pm 2ab + b^2, \quad a^2 - b^2 = (a-b)(a+b), \quad x_{\text{vertex}} = -\frac{b}{2a}"),
                caption_ar="المتطابقات الشهيرة وإحداثي محور تماثل الدالة التربيعية:",
                formula_math_ar=dm(r"(a \pm b)^2 = a^2 \pm 2ab + b^2, \quad a^2 - b^2 = (a-b)(a+b), \quad x = -\frac{b}{2a}"),
                diagram_en=svg_area_identity_square("x", "3"),
            ),
        ],
        traps_en=[
            f"Forgetting the middle term {m('2ab')} when squaring a binomial: {m('(x + 4)^2 = x^2 + 8x + 16')}, NOT {m('x^2 + 16')}!",
            f"Failing to flip the inequality sign when dividing by a negative coefficient: {m('-2x < 10 \\implies x > -5')}, NOT {m('x < -5')}.",
            f"Confusing the factored signs with the roots: if {m('(x - 5)(x + 2) = 0')}, the roots are {m('x = 5')} and {m('x = -2')}, NOT {m('-5')} and {m('2')}.",
        ],
        traps_ar=[
            f"نسيان الحد الأوسط {m('2ab')} عند تربيع ثنائية حد: {m('(x + 4)^2 = x^2 + 8x + 16')} وليس {m('x^2 + 16')}!",
            f"عدم عكس اتجاه المتباينة عند القسمة على معامل سالب: {m('-2x < 10 \\implies x > -5')} وليس {m('x < -5')}.",
            f"الخلط بين إشارات العوامل وإشارات الجذور: حل المعادلة {m('(x - 5)(x + 2) = 0')} هو {m('x = 5')} أو {m('x = -2')}.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-03-EX1",
                title_en="Larger Root of an Absolute-Value Equation",
                title_ar="الحل الأكبر لمعادلة قيمة مطلقة",
                q_en=f"What is the larger solution of the equation {m('|2x - 5| = 9')}?",
                q_ar=f"ما قيمة الحل الأكبر لمعادلة القيمة المطلقة {m('|2x - 5| = 9')}؟",
                correct_val=7,
                distractors=[-2, 2, 5],
                idea_en=f"Split {m('|2x - 5| = 9')} into {m('2x - 5 = 9')} and {m('2x - 5 = -9')}, solve both, and pick the greater value!",
                steps_en=[
                    f"Case 1: {m('2x - 5 = 9 \\implies 2x = 14 \\implies x = 7')}.",
                    f"Case 2: {m('2x - 5 = -9 \\implies 2x = -4 \\implies x = -2')}.",
                    f"Comparing {m('7')} and {m('-2')}, the larger solution is {m('7')}.",
                ],
                check_en=f"Substitute {m('x = 7')}: {m('|2(7) - 5| = |9| = 9')}.",
                idea_ar=f"نفك المعادلة إلى حالتين {m('2x - 5 = 9')} و{m('2x - 5 = -9')} ثم نختار القيمة الكبرى!",
                steps_ar=[
                    f"الحالة الأولى: {m('2x - 5 = 9 \\implies 2x = 14 \\implies x = 7')}.",
                    f"الحالة الثانية: {m('2x - 5 = -9 \\implies 2x = -4 \\implies x = -2')}.",
                    f"القيمة الكبرى بين الحلين هي {m('7')}.",
                ],
                check_ar=f"بالتعويض: {m('|2(7) - 5| = |14 - 5| = 9')}.",
                diagram_en=svg_g9_real_number_line([-3, 0, 3, 7], 7, "x = 7", "|2x − 5| = 9"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-03-EX2",
                title_en="Intersection of a 2×2 Linear System by Elimination",
                title_ar="إيجاد نقطة تقاطع نظام معادلتين خطيتين بالحذف",
                q_en=f"If {m('(x, y)')} satisfies the linear system {m('2x + y = 11')} and {m('x - y = 4')}, what is the value of {m('y')}?",
                q_ar=f"إذا كان الزوج المرتب {m('(x, y)')} يحقق النظام الخطي {m('2x + y = 11')} و{m('x - y = 4')}، فما قيمة {m('y')}؟",
                correct_val=1,
                distractors=[2, 3, 5],
                idea_en=f"Add both equations directly to eliminate {m('y')}, find {m('x')}, and substitute back to get {m('y')}!",
                steps_en=[
                    f"Adding the two equations gives {m('(2x + y) + (x - y) = 11 + 4 \\implies 3x = 15 \\implies x = 5')}.",
                    f"Substitute {m('x = 5')} into {m('x - y = 4')}: {m('5 - y = 4 \\implies y = 1')}.",
                ],
                check_en=f"Check both: {m('2(5) + 1 = 11')} and {m('5 - 1 = 4')}.",
                idea_ar=f"نجمع المعادلتين مباشرة لحذف {m('y')} وإيجاد {m('x')} ثم نعوّض لإيجاد {m('y')}!",
                steps_ar=[
                    f"بجمع المعادلتين: {m('3x = 15 \\implies x = 5')}.",
                    f"نعوّض في {m('x - y = 4')}: {m('5 - y = 4 \\implies y = 1')}.",
                ],
                check_ar=f"تحقق: {m('2(5) + 1 = 11')} و{m('5 - 1 = 4')}.",
                diagram_en=svg_nafes_coordinate_line([(5, 1, "(5, 1)")], line_kb=(-2, 11), line2_kb=(1, -4), max_coord=6),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-03-EX3",
                title_en="Expanding a Square of a Difference",
                title_ar="فك مربع فرق حدين",
                q_en=f"Which polynomial is equivalent to {m('(2x - 3)^2')}?",
                q_ar=f"أي كثيرة حدود مما يلي تكافئ المربع الكامل {m('(2x - 3)^2')}؟",
                correct_val=r"4x^2 - 12x + 9",
                distractors=[r"4x^2 - 9", r"4x^2 + 12x + 9", r"2x^2 - 12x + 9"],
                idea_en=f"Apply {m('(a - b)^2 = a^2 - 2ab + b^2')} with {m('a = 2x')} and {m('b = 3')}!",
                steps_en=[
                    f"Square the first term: {m('(2x)^2 = 4x^2')}.",
                    f"Subtract twice the product: {m('-2(2x)(3) = -12x')}.",
                    f"Add the square of the last term: {m('(-3)^2 = +9')}, giving {m('4x^2 - 12x + 9')}.",
                ],
                check_en=f"Test {m('x = 2')}: {m('(4 - 3)^2 = 1')}, and {m('4(4) - 12(2) + 9 = 16 - 24 + 9 = 1')}.",
                idea_ar=f"نطبّق متطابقة مربع الفرق {m('(a - b)^2 = a^2 - 2ab + b^2')} بوضع {m('a = 2x')} و{m('b = 3')}!",
                steps_ar=[
                    f"مربع الحد الأول: {m('(2x)^2 = 4x^2')}.",
                    f"ناقص ضعفي الأول في الثاني: {m('-2(2x)(3) = -12x')}.",
                    f"زائد مربع الحد الثاني: {m('3^2 = +9')}، فتكون النتيجة {m('4x^2 - 12x + 9')}.",
                ],
                check_ar=f"عند {m('x = 2')}: {m('(4 - 3)^2 = 1')}، وكذلك {m('16 - 24 + 9 = 1')}.",
                diagram_en=svg_area_identity_square("2x", "3"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-03-EX4",
                title_en="Minimum Value at the Vertex of a Quadratic",
                title_ar="القيمة الصغرى عند رأس القطع المكافئ",
                q_en=f"What is the minimum value of the quadratic function {m('y = x^2 - 6x + 5')}?",
                q_ar=f"ما القيمة الصغرى للدالة التربيعية {m('y = x^2 - 6x + 5')}؟",
                correct_val=-4,
                distractors=[3, -5, 5],
                idea_en=f"Find the axis of symmetry {m(r'x = -\frac{b}{2a}')} first, then evaluate {m('y')} at that {m('x')}-coordinate!",
                steps_en=[
                    f"Here {m('a = 1 > 0')} and {m('b = -6')}, so the vertex {m('x')}-coordinate is {m(r'x = -\frac{-6}{2(1)} = 3')}.",
                    f"Substitute {m('x = 3')} into {m('y')}: {m('y_{\\min} = 3^2 - 6(3) + 5 = 9 - 18 + 5 = -4')}.",
                ],
                check_en=f"Completing the square: {m('y = (x - 3)^2 - 4 \\ge -4')}, with equality at {m('x = 3')}.",
                idea_ar=f"نوجد معادلة محور التماثل {m(r'x = -\frac{b}{2a}')} أولاً، ثم نعوّض بقيمة {m('x')} في الدالة لإيجاد القيمة الصغرى {m('y')}!",
                steps_ar=[
                    f"هنا {m('a = 1')} و{m('b = -6')}، فيكون إحداثي الرأس السيني {m(r'x = -\frac{-6}{2(1)} = 3')}.",
                    f"نعوّض {m('x = 3')}: {m('y_{\\min} = 9 - 18 + 5 = -4')}.",
                ],
                check_ar=f"بإكمال المربع: {m('y = (x - 3)^2 - 4')}، فأقل قيمة ممكنة هي {m('-4')}.",
                diagram_en=svg_parabola_roots("1", "5", "(3, −4)"),
            ),
        ],
        blueprints=["G9-ALG-01", "G9-ALG-02", "G9-ALG-03", "G9-ALG-04"],
    )


def _lesson_3_4() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-04",
        level=LEVEL,
        unit_num="3.4",
        topic="Geometry",
        title_en="Pythagorean Theorem, Coordinate Distance/Midpoint, Composite Areas & 3D Solid Volumes",
        title_ar="نظرية فيثاغورس، المسافة ونقطة المنتصف، المساحات المركبة، وحجوم المجسمات",
        summary_en=(
            "Use the Pythagorean theorem and classic triples in 2D/coordinate contexts, compute segment lengths and midpoints, "
            "find shaded circular composite areas, and calculate volumes and surface areas of cylinders, cones, pyramids, and spheres."
        ),
        summary_ar=(
            "تطبيق نظرية فيثاغورس والثلاثيات الشهيرة، وحساب المسافة وإحداثيات نقطة المنتصف في المستوى الإحداثي، وإيجاد مساحات "
            "الأشكال المظللة المركبة، وحساب حجوم ومساحات الأسطوانة والمخروط والهرم والكرة."
        ),
        goals_en=[
            f"Apply {m('a^2 + b^2 = c^2')} and recognize scaled Pythagorean triples ({m('3\\text{-}4\\text{-}5')}, {m('5\\text{-}12\\text{-}13')}, {m('8\\text{-}15\\text{-}17')}, {m('7\\text{-}24\\text{-}25')}) instantly.",
            f"Compute coordinate distance {m(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')} and midpoint {m(r'M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)')}, including missing endpoints.",
            f"Calculate shaded composite areas by subtracting inner cutouts (circles, sectors {m(r'\frac{\theta}{360}\pi r^2')}, semicircles, inscribed polygons).",
            f"Compute volumes and surface areas of cylinders ({m(r'\pi r^2 h')}), cones ({m(r'\frac{1}{3}\pi r^2 h')}), pyramids ({m(r'\frac{1}{3}Bh')}), and spheres ({m(r'\frac{4}{3}\pi r^3')}).",
        ],
        goals_ar=[
            f"تطبيق نظرية فيثاغورس {m('a^2 + b^2 = c^2')} واستخدام الثلاثيات الفيثاغورسية الشهيرة ({m('3\\text{-}4\\text{-}5')}، {m('5\\text{-}12\\text{-}13')}، {m('8\\text{-}15\\text{-}17')}) بسرعة.",
            f"حساب المسافة {m(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')} ونقطة المنتصف {m(r'M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)')} وإيجاد الطرف المجهول.",
            f"إيجاد المساحات المظللة المركبة بطرح المساحات غير المظللة (الدوائر، القطاعات الدائرية {m(r'\frac{\theta}{360}\pi r^2')}، أنصاف الدوائر).",
            f"حساب حجوم ومساحات الأسطوانة ({m(r'\pi r^2 h')}) والمخروط ({m(r'\frac{1}{3}\pi r^2 h')}) والهرم ({m(r'\frac{1}{3}Bh')}) والكرة ({m(r'\frac{4}{3}\pi r^3')}).",
        ],
        concepts=[
            nafes_concept(
                title_en="1. The Pythagorean Theorem & Pythagorean Triples",
                title_ar="١. نظرية فيثاغورس والثلاثيات الفيثاغورسية",
                body_en=(
                    f"In any right triangle, the square of the **hypotenuse** {m('c')} (opposite the {m('90^\\circ')} angle) equals the sum of the squares "
                    f"of the two legs: {m('a^2 + b^2 = c^2')}. If you know the hypotenuse {m('c')} and one leg {m('a')}, **subtract**: {m(r'b = \sqrt{c^2 - a^2}')}. "
                    f"Spotting multiples of {m('(3, 4, 5)')}, {m('(5, 12, 13)')}, and {m('(8, 15, 17)')} saves precious seconds on Nafes!"
                ),
                body_ar=(
                    f"في أي مثلث قائم الزاوية، مربع طول **الوتر** {m('c')} (الضلع المقابل للزاوية القائمة) يساوي مجموع مربعي ساقيه: {m('a^2 + b^2 = c^2')}. "
                    f"إذا عُلم الوتر {m('c')} وأحد الساقين {m('a')} فإننا **نطرح**: {m(r'b = \sqrt{c^2 - a^2}')}. تذكُّر مضاعفات الثلاثيات {m('(3,4,5)')} و{m('(5,12,13)')} و{m('(8,15,17)')} يوفّر وقتاً ثميناً!"
                ),
                formula_en=dm(r"a^2 + b^2 = c^2 \implies c = \sqrt{a^2 + b^2}, \qquad a = \sqrt{c^2 - b^2}"),
                caption_ar="نظرية فيثاغورس لإيجاد الوتر أو أحد الساقين:",
                formula_math_ar=dm(r"c = \sqrt{a^2 + b^2}, \qquad a = \sqrt{c^2 - b^2}"),
                diagram_en=svg_g9_right_triangle("a = 5", "b = 12", "c = 13", "5² + 12² = 13²"),
            ),
            nafes_concept(
                title_en="2. Coordinate Distance & Midpoint Formulas",
                title_ar="٢. قانون المسافة وإحداثيات نقطة المنتصف في المستوى",
                body_en=(
                    f"Connecting {m('A(x_1, y_1)')} and {m('B(x_2, y_2)')} forms a right triangle with horizontal leg {m('|x_2 - x_1|')} and vertical leg "
                    f"{m('|y_2 - y_1|')}, giving the distance formula. The **midpoint** {m('M')} averages the coordinates. When given {m('A')} and midpoint {m('M')}, "
                    f"double the midpoint and subtract {m('A')}: {m('(x_2, y_2) = (2x_M - x_1,\\; 2y_M - y_1)')}!"
                ),
                body_ar=(
                    f"تُشكّل القطعة الواصلة بين {m('A(x_1, y_1)')} و{m('B(x_2, y_2)')} وتراً لمثلث قائم أفقيه {m('|x_2 - x_1|')} ورأسيه {m('|y_2 - y_1|')}. "
                    f"**نقطة المنتصف** {m('M')} هي متوسط الإحداثيين السينيين والصاديين؛ وإذا عُلمت {m('M')} وأحد الطرفين {m('A')} فإن الطرف الآخر {m('(2x_M - x_1,\\; 2y_M - y_1)')}."
                ),
                formula_en=dm(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}, \qquad M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)"),
                caption_ar="قانون المسافة بين نقطتين وقانون إحداثيات نقطة المنتصف:",
                formula_math_ar=dm(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}, \qquad M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)"),
                diagram_en=svg_nafes_coordinate_line([(-2, -1, "A(-2,-1)"), (1, 1, "M(1,1)"), (4, 3, "B(4,3)")], max_coord=5),
            ),
            nafes_concept(
                title_en="3. Shaded Circular Regions & Volumes of 3D Solids",
                title_ar="٣. المساحات المظللة المركبة وحجوم المجسمات الثلاثية",
                body_en=(
                    f"For shaded composite figures, compute {m(r'\text{Area}_{\text{outer}} - \text{Area}_{\text{cutout}}')}. Notice that a circle inscribed in a square of side {m('s')} "
                    f"has radius {m('r = s/2')} (not {m('s')}!). In 3D geometry, a cone and a pyramid hold **exactly one-third** the volume of the prism or cylinder "
                    f"sharing the same base and height, while a sphere of radius {m('r')} has volume {m(r'\frac{4}{3}\pi r^3')} and surface area {m(r'4\pi r^2')}."
                ),
                body_ar=(
                    f"في الأشكال المركبة المظللة نطرح المساحة المفرّغة من المساحة الكلية، مع الانتباه إلى أن الدائرة المرسومة داخل مربع طول ضلعه {m('s')} نصف قطرها {m('r = s/2')}. "
                    f"وفي الفضاء الثلاثي، حجم المخروط أو الهرم يساوي **ثلث** حجم الأسطوانة أو المنشور المشترك معه في القاعدة والارتفاع، وحجم الكرة {m(r'\frac{4}{3}\pi r^3')}."
                ),
                formula_en=dm(r"V_{\text{cyl}} = \pi r^2 h, \qquad V_{\text{cone}} = \frac{1}{3}\pi r^2 h, \qquad V_{\text{pyr}} = \frac{1}{3}Bh, \qquad V_{\text{sphere}} = \frac{4}{3}\pi r^3"),
                caption_ar="قوانين حجوم الأسطوانة والمخروط والهرم والكرة:",
                formula_math_ar=dm(r"V_{\text{cyl}} = \pi r^2 h, \quad V_{\text{cone}} = \frac{1}{3}\pi r^2 h, \quad V_{\text{pyr}} = \frac{1}{3}Bh, \quad V_{\text{sphere}} = \frac{4}{3}\pi r^3"),
                diagram_en=svg_g9_solid_3d("cylinder", "r", "h", "V = πr²h  |  Cone = ⅓πr²h"),
            ),
        ],
        traps_en=[
            f"Adding squares when the hypotenuse is already given: if a ladder of length {m('13')} has base {m('5')}, height is {m(r'\sqrt{13^2 - 5^2} = 12')}, NOT {m(r'\sqrt{13^2 + 5^2}')}.",
            f"Using diameter {m('d')} instead of radius {m('r = d/2')} inside {m(r'\pi r^2')}, which makes the area **4 times too large**!",
            f"Forgetting the factor {m(r'\frac{1}{3}')} when computing the volume of a cone or pyramid.",
        ],
        traps_ar=[
            f"جمع المربعين عندما يكون الوتر معلوماً: إذا كان طول السلم {m('13')} وبعد قاعدته {m('5')} فالارتفاع {m(r'\sqrt{13^2 - 5^2} = 12')} وليس جمعاً.",
            f"التعويض بالقطر الكامل {m('d')} بدلاً من نصف القطر {m('r = d/2')} في قانون المساحة {m(r'\pi r^2')} مما يضاعف الناتج {m('4')} مرات!",
            f"نسيان الضرب في الكسر {m(r'\frac{1}{3}')} عند حساب حجم المخروط أو الهرم.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-04-EX1",
                title_en="Height Reached by a Rescue Ladder (Pythagoras)",
                title_ar="ارتفاع قمة سلم إنقاذ بنظرية فيثاغورس",
                q_en=f"A {m('13')}-meter rescue ladder leans against a vertical wall with its base {m('5')} meters from the wall. How high up the wall (in meters) does the ladder reach?",
                q_ar=f"يستند سلم إنقاذ طوله {m('13')} متراً إلى جدار رأسي، وتبعد قاعدته {m('5')} أمتار عن أسفل الجدار. على أي ارتفاع بالأمتار تصل قمة السلم؟",
                correct_val=12,
                distractors=[8, 10, 14],
                idea_en=f"The ladder is the hypotenuse {m('c = 13')} and the ground gap is {m('b = 5')}, so subtract squares {m('13^2 - 5^2')}!",
                steps_en=[
                    f"By the Pythagorean theorem, {m('h^2 + 5^2 = 13^2')}.",
                    f"Compute {m('h^2 = 169 - 25 = 144 \\implies h = \\sqrt{144} = 12')} meters.",
                ],
                check_en=f"Recognize the classic {m('5\\text{-}12\\text{-}13')} right triangle: {m('25 + 144 = 169')}.",
                idea_ar=f"السلم يمثل الوتر {m('c = 13')} والمسافة الأفقية {m('b = 5')}، لذا نطرح {m('13^2 - 5^2')}!",
                steps_ar=[
                    f"بتطبيق فيثاغورس: {m('h^2 + 5^2 = 13^2')}.",
                    f"نحسب {m('h^2 = 169 - 25 = 144 \\implies h = 12')} متراً.",
                ],
                check_ar=f"ثلاثية فيثاغورس الشهيرة {m('(5, 12, 13)')} تحقق {m('25 + 144 = 169')}.",
                diagram_en=svg_g9_right_triangle("h = ?", "5 m", "13 m"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-04-EX2",
                title_en="Finding a Missing Endpoint from the Midpoint",
                title_ar="إيجاد إحداثيي طرف قطعة مستقيمة بمعلومية المنتصف",
                q_en=f"Point {m('M(3, -1)')} is the midpoint of segment {m('AB')}. If endpoint {m('A')} is {m('(-1, 2)')}, what are the coordinates of endpoint {m('B')}?",
                q_ar=f"إذا كانت النقطة {m('M(3, -1)')} هي منتصف القطعة المستقيمة {m('AB')}، وكانت {m('A(-1, 2)')}، فما إحداثيا النقطة {m('B')}؟",
                correct_val="(7, -4)",
                distractors=["(1, 0.5)", "(5, -3)", "(7, 0)"],
                idea_en=f"Double the midpoint coordinates and subtract endpoint {m('A')}: {m('B = 2M - A')}!",
                steps_en=[
                    f"For the {m('x')}-coordinate: {m(r'\frac{-1 + x_B}{2} = 3 \implies -1 + x_B = 6 \implies x_B = 7')}.",
                    f"For the {m('y')}-coordinate: {m(r'\frac{2 + y_B}{2} = -1 \implies 2 + y_B = -2 \implies y_B = -4')}.",
                    f"Thus {m('B = (7, -4)')}.",
                ],
                check_en=f"Midpoint of {m('(-1, 2)')} and {m('(7, -4)')} is {m(r'\left(\frac{-1+7}{2}, \frac{2-4}{2}\right) = (3, -1)')}.",
                idea_ar=f"نضاعف إحداثيي نقطة المنتصف ونطرح إحداثيي النقطة {m('A')}: {m('B = 2M - A')}!",
                steps_ar=[
                    f"الإحداثي السيني: {m('x_B = 2(3) - (-1) = 6 + 1 = 7')}.",
                    f"الإحداثي الصادي: {m('y_B = 2(-1) - 2 = -4')}، فتكون {m('B(7, -4)')}.",
                ],
                check_ar=f"منتصف {m('(-1, 2)')} و{m('(7, -4)')} هو {m('((-1+7)/2, (2-4)/2) = (3, -1)')}.",
                diagram_en=svg_nafes_coordinate_line([(-1, 2, "A(-1,2)"), (3, -1, "M(3,-1)"), (7, -4, "B?")], max_coord=8),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-04-EX3",
                title_en="Shaded Corners Around an Inscribed Circle",
                title_ar="مساحة الأركان المظللة حول دائرة داخل مربع",
                q_en=f"A circle is inscribed inside a square of side length {m('14')} cm. Using {m(r'\pi = \frac{22}{7}')}, what is the area of the shaded region outside the circle (in {m(r'\text{cm}^2')})?",
                q_ar=f"رُسمت دائرة تمس أضلاع مربع طول ضلعه {m('14')} سم من الداخل. باعتبار {m(r'\pi = \frac{22}{7}')}، ما مساحة المنطقة المظللة خارج الدائرة وداخل المربع بالـ {m(r'\text{سم}^2')}؟",
                correct_val=42,
                distractors=[38, 49, 154],
                idea_en=f"Subtract the circle's area ({m('r = 7')} cm) from the square's area ({m('14^2 = 196')})!",
                steps_en=[
                    f"Square area: {m('A_{\\text{sq}} = 14 \\times 14 = 196\\text{ cm}^2')}.",
                    f"The inscribed circle has diameter {m('14')} cm, so radius {m('r = 7')} cm and area {m(r'A_{\text{cir}} = \frac{22}{7} \times 7^2 = 154\text{ cm}^2')}.",
                    f"Shaded area: {m('196 - 154 = 42\\text{ cm}^2')}.",
                ],
                check_en=f"{m('154 + 42 = 196\\text{ cm}^2')}, matching roughly {m('21.4\\%')} of the square.",
                idea_ar=f"نطرح مساحة الدائرة (نصف قطرها {m('r = 7')} سم) من مساحة المربع ({m('14^2 = 196')})!",
                steps_ar=[
                    f"مساحة المربع: {m('14 \\times 14 = 196')} سم².",
                    f"نصف قطر الدائرة {m('r = 14 \\div 2 = 7')} سم، ومساحتها {m(r'\frac{22}{7} \times 49 = 154')} سم².",
                    f"المساحة المظللة: {m('196 - 154 = 42')} سم².",
                ],
                check_ar=f"مجموع المساحتين {m('154 + 42 = 196')} سم².",
                diagram_en=svg_square_circle_shaded("14 cm", "inscribed_outside"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-04-EX4",
                title_en="Exact Volume of a Right Circular Cone",
                title_ar="حساب الحجم الدقيق للمخروط الدائري القائم",
                q_en=f"What is the exact volume (in {m(r'\text{cm}^3')}) of a right circular cone with base radius {m('r = 6')} cm and height {m('h = 10')} cm?",
                q_ar=f"ما الحجم الدقيق (بوحدة {m(r'\text{سم}^3')}) لمخروط دائري قائم نصف قطر قاعدته {m('r = 6')} سم وارتفاعه {m('h = 10')} سم بدلالة {m(r'\pi')}؟",
                correct_val=r"120\pi",
                distractors=[r"360\pi", r"60\pi", r"20\pi"],
                idea_en=f"Use {m(r'V = \frac{1}{3}\pi r^2 h')} — one-third of the cylinder with radius {m('6')} and height {m('10')}!",
                steps_en=[
                    f"Base area: {m(r'\pi r^2 = \pi(6^2) = 36\pi\text{ cm}^2')}.",
                    f"Multiply by {m(r'\frac{1}{3}h')}: {m(r'V = \frac{1}{3}(36\pi)(10) = 12\pi \times 10 = 120\pi\text{ cm}^3')}.",
                ],
                check_en=f"Cylinder volume is {m(r'360\pi')}, and {m(r'360\pi \div 3 = 120\pi')}.",
                idea_ar=f"نطبّق قانون حجم المخروط {m(r'V = \frac{1}{3}\pi r^2 h')}!",
                steps_ar=[
                    f"مساحة القاعدة الدائرية: {m(r'\pi (6)^2 = 36\pi')} سم².",
                    f"الحجم: {m(r'V = \frac{1}{3} \times 36\pi \times 10 = 120\pi')} سم³.",
                ],
                check_ar=f"حجم الأسطوانة المناظرة {m(r'360\pi')} وثلثه {m(r'120\pi')} تماماً.",
                diagram_en=svg_g9_solid_3d("cone", "r = 6", "h = 10"),
            ),
        ],
        blueprints=["G9-GEO-01", "G9-GEO-02", "G9-GEO-03", "G9-GEO-04"],
    )


def _lesson_3_5() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-05",
        level=LEVEL,
        unit_num="3.5",
        topic="Geometry",
        title_en="Parallel-Line Angles, Polygon Interior/Exterior Sums, Triangle Similarity & Transformations",
        title_ar="المستقيمات المتوازية، زوايا المضلعات، تشابه المثلثات، والتحويلات الهندسية",
        summary_en=(
            "Solve algebraic angle relationships across parallel lines and triangle exterior angles, calculate interior and exterior "
            "angles of regular polygons, apply linear vs area ratios in similar triangles, and perform coordinate transformations."
        ),
        summary_ar=(
            "حل المعادلات الجبرية لزوايا المستقيمات المتوازية والزاوية الخارجية للمثلث، وحساب الزوايا الداخلية والخارجية للمضلعات "
            "المنتظمة، وتطبيق نسب التشابه والمساحة للمثلثات المتشابهة، وإجراء التحويلات الهندسية في المستوى الإحداثي."
        ),
        goals_en=[
            f"Equate alternate interior and corresponding angles, set co-interior angles supplementary ({m('180^\\circ')}), and apply the triangle exterior angle theorem ({m(r'\angle_{\text{ext}} = \angle A + \angle B')}).",
            f"Use {m('S = (n - 2) \\times 180^\\circ')} and exterior sum {m('360^\\circ')} to find interior/exterior angles or side count {m('n')} of convex and regular polygons.",
            f"Set up proportions in similar triangles (shadows, parallel cross-segments, midsegments) and relate linear scale factor {m('k')} to area ratio {m('k^2')}.",
            f"Apply coordinate rules for translations {m('(x+a, y+b)')}, reflections across axes/{m('y=x')}, rotations ({m('90^\\circ, 180^\\circ')}), and dilations {m('(kx, ky)')}.",
        ],
        goals_ar=[
            f"مساواة الزوايا المتبادلة داخلياً والمتناظرة، وتكامل المتحالفتين ({m('180^\\circ')})، وتطبيق نظرية الزاوية الخارجية للمثلث ({m(r'\angle_{\text{ext}} = \angle A + \angle B')}).",
            f"حساب مجموع الزوايا الداخلية {m('(n - 2) \\times 180^\\circ')} والزاوية الخارجية للمضلع المنتظم {m('360^\\circ / n')} وإيجاد عدد الأضلاع {m('n')}.",
            f"كتابة تناسبات تشابه المثلثات (الظلال، القطعة المنصّفة) والربط بين معامل التشابه الخطي {m('k')} ونسبة المساحتين {m('k^2')}.",
            f"تطبيق قواعد الانسحاب {m('(x+a, y+b)')}، والانعكاس حول المحورين والمستقيم {m('y=x')}، والدوران بزاوية {m('90^\\circ, 180^\\circ')}، والتمدد.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Parallel Lines with Transversals & Triangle Exterior Angles",
                title_ar="١. القاطع لمستقيمين متوازيين والزاوية الخارجية للمثلث",
                body_en=(
                    f"When a transversal crosses parallel lines {m(r'\ell_1 \parallel \ell_2')}, **alternate interior** and **corresponding** angles are "
                    f"equal, whereas **co-interior** (same-side interior) angles add up to {m('180^\\circ')}. In any triangle, an **exterior angle** "
                    f"equals the sum of the two non-adjacent (remote) interior angles: {m(r'\angle_{\text{ext}} = \alpha + \beta')}."
                ),
                body_ar=(
                    f"إذا قطع مستقيم مستقيمين متوازيين {m(r'\ell_1 \parallel \ell_2')}، فإن كل زاويتين **متبادلتين داخلياً** أو **متناظرتين** متطابقتان، "
                    f"وكل زاويتين **متحالفتين** متكاملتان مجموعهما {m('180^\\circ')}. وفي أي مثلث، قياس **الزاوية الخارجية** يساوي مجموع الزاويتين الداخليتين البعيدتين."
                ),
                formula_en=dm(r"\text{Alt./Corr.: } \alpha = \beta, \qquad \text{Co-interior: } \alpha + \beta = 180^\circ, \qquad \angle_{\text{ext}} = \angle A + \angle B"),
                caption_ar="علاقات الزوايا على المستقيمين المتوازيين ونظرية الزاوية الخارجية:",
                formula_math_ar=dm(r"\alpha = \beta, \qquad \alpha + \beta = 180^\circ, \qquad \angle_{\text{ext}} = \angle A + \angle B"),
                diagram_en=svg_g9_parallel_transversal("α", "β", "co_int"),
            ),
            nafes_concept(
                title_en="2. Interior & Exterior Angle Sums of Convex Polygons",
                title_ar="٢. مجموع الزوايا الداخلية والخارجية للمضلعات المحدبة",
                body_en=(
                    f"An {m('n')}-gon splits into {m('n - 2')} triangles from one vertex, so its interior angles sum to {m('(n - 2) \\times 180^\\circ')}. "
                    f"Its exterior angles (one per vertex) **always sum to {m('360^\\circ')}**! Therefore, for a **regular** {m('n')}-gon, each exterior angle "
                    f"is {m('e = 360^\\circ / n')} and each interior angle is {m('180^\\circ - e')}, which gives {m('n = 360^\\circ / (180^\\circ - I)')} instantly."
                ),
                body_ar=(
                    f"ينقسم المضلع المحدب ذو {m('n')} أضلاع إلى {m('n - 2')} مثلثات، فمجموع زواياه الداخلية {m('(n - 2) \\times 180^\\circ')}، بينما مجموع زواياه الخارجية "
                    f"ثابت دائماً ويساوي {m('360^\\circ')}! لذا في المضلع المنتظم قياس الزاوية الخارجية {m('e = 360^\\circ / n')}، وعدد الأضلاع {m('n = 360^\\circ / (180^\\circ - I)')}."
                ),
                formula_en=dm(r"S_{\text{int}} = (n - 2) \times 180^\circ, \qquad e_{\text{reg}} = \frac{360^\circ}{n}, \qquad n = \frac{360^\circ}{180^\circ - I}"),
                caption_ar="مجموع الزوايا الداخلية وقانون عدد أضلاع المضلع المنتظم:",
                formula_math_ar=dm(r"S = (n - 2) \times 180^\circ, \qquad e = \frac{360^\circ}{n}, \qquad n = \frac{360^\circ}{180^\circ - I}"),
                diagram_en=svg_regular_polygon(6, [(0, 2), (0, 3), (0, 4)]),
            ),
            nafes_concept(
                title_en="3. Similar Triangles (k vs k²) & Coordinate Transformations",
                title_ar="٣. تشابه المثلثات (نسبة التشابه k ونسبة المساحة k²) والتحويلات الهندسية",
                body_en=(
                    f"If {m(r'\triangle ABC \sim \triangle DEF')} with scale factor {m('k')}, **all linear measures** (sides, altitudes, perimeters) scale by {m('k')}, "
                    f"whereas **areas scale by {m('k^2')}**! On the coordinate plane: reflection across the {m('x')}-axis gives {m('(x, -y)')}, across the {m('y')}-axis gives "
                    f"{m('(-x, y)')}, across {m('y = x')} gives {m('(y, x)')}, a {m('180^\\circ')} rotation about the origin gives {m('(-x, -y)')}, and a {m('90^\\circ')} counterclockwise rotation gives {m('(-y, x)')}."
                ),
                body_ar=(
                    f"إذا تشابه مثلثان بمعامل تشابه {m('k')}، فإن نسبة الأضلاع والمحيطين تساوي {m('k')}، أما **نسبة المساحتين فتساوي مربع النسبة {m('k^2')}**! "
                    f"وفي المستوى الإحداثي: الانعكاس حول محور السينات {m('(x, -y)')}، وحول محور الصادات {m('(-x, y)')}، وحول {m('y=x')} يعطي {m('(y, x)')}، والدوران {m('180^\\circ')} يعطي {m('(-x, -y)')}."
                ),
                formula_en=dm(r"\frac{P_2}{P_1} = k, \quad \frac{A_2}{A_1} = k^2, \quad R_x(x,y)=(x,-y), \quad R_y(x,y)=(-x,y), \quad \text{Rot}_{180^\circ}(x,y)=(-x,-y)"),
                caption_ar="نسب المحيط والمساحة في التشابه وقواعد الانعكاس والدوران:",
                formula_math_ar=dm(r"\frac{P_2}{P_1} = k, \quad \frac{A_2}{A_1} = k^2, \quad R_x(x,y)=(x,-y), \quad R_y(x,y)=(-x,y)"),
                diagram_en=svg_g9_similar_triangles("h₁", "b₁", "k·h₁", "k·b₁", nested=False),
            ),
        ],
        traps_en=[
            f"Setting co-interior angles equal instead of supplementary: angles on the **same side** between parallel lines add to {m('180^\\circ')}.",
            f"Using {m('k')} instead of {m('k^2')} for similar-triangle areas: doubling every side of a triangle multiplies its area by {m('2^2 = 4')}, NOT {m('2')}!",
            f"Swapping reflection rules: reflecting across the **{m('x')}-axis** negates **{m('y')}** ({m('(x, -y)')}), while reflecting across the **{m('y')}-axis** negates **{m('x')}** ({m('(-x, y)')}).",
        ],
        traps_ar=[
            f"مساواة الزاويتين المتحالفتين بدلاً من جمعهما إلى {m('180^\\circ')}؛ المتحالفتان متكاملتان وليستا متطابقتين بالضرورة.",
            f"استخدام النسبة {m('k')} بدلاً من {m('k^2')} للمساحات: مضاعفة أضلاع مثلث تضاعف مساحته {m('4')} مرات وليس مرتين!",
            f"عكس قاعدة الانعكاس: الانعكاس حول محور السينات يغيّر إشارة {m('y')}، وحول محور الصادات يغيّر إشارة {m('x')}.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-05-EX1",
                title_en="Algebraic Co-Interior Angles Across Parallel Lines",
                title_ar="معادلة زاويتين متحالفتين بين مستقيمين متوازيين",
                q_en=f"A transversal intersects two parallel lines, forming co-interior angles of {m('(3x + 15)^\\circ')} and {m('(2x + 25)^\\circ')}. What is the value of {m('x')}?",
                q_ar=f"يقطع قاطع مستقيمين متوازيين فيشكّل زاويتين داخليتين متحالفتين قياساهما {m('(3x + 15)^\\circ')} و{m('(2x + 25)^\\circ')}. ما قيمة {m('x')}؟",
                correct_val=28,
                distractors=[20, 32, 44],
                idea_en=f"Co-interior angles between parallel lines are supplementary, so their sum equals {m('180^\\circ')}!",
                steps_en=[
                    f"Set up the supplementary equation: {m('(3x + 15) + (2x + 25) = 180')}.",
                    f"Combine like terms: {m('5x + 40 = 180 \\implies 5x = 140 \\implies x = 28')}.",
                ],
                check_en=f"Angles are {m('3(28)+15 = 99^\\circ')} and {m('2(28)+25 = 81^\\circ')}, and {m('99^\\circ + 81^\\circ = 180^\\circ')}.",
                idea_ar=f"الزاويتان المتحالفتان بين مستقيمين متوازيين متكاملتان مجموعهما {m('180^\\circ')}!",
                steps_ar=[
                    f"نكتب المعادلة: {m('(3x + 15) + (2x + 25) = 180')}.",
                    f"نبسّط: {m('5x + 40 = 180 \\implies 5x = 140 \\implies x = 28')}.",
                ],
                check_ar=f"الزاويتان {m('99^\\circ')} و{m('81^\\circ')} ومجموعهما {m('180^\\circ')}.",
                diagram_en=svg_g9_parallel_transversal("3x + 15°", "2x + 25°", "co_int"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-05-EX2",
                title_en="Finding Polygon Sides from One Interior Angle",
                title_ar="إيجاد عدد أضلاع مضلع منتظم من زاويته الداخلية",
                q_en=f"Each interior angle of a regular polygon measures {m('140^\\circ')}. How many sides does this polygon have?",
                q_ar=f"إذا كان قياس كل زاوية داخلية في مضلع منتظم يساوي {m('140^\\circ')}، فما عدد أضلاع هذا المضلع؟",
                correct_val=9,
                distractors=[8, 10, 12],
                idea_en=f"Find the exterior angle {m('180^\\circ - 140^\\circ = 40^\\circ')} first, then divide {m('360^\\circ')} by {m('40^\\circ')}!",
                steps_en=[
                    f"Each exterior angle is {m('e = 180^\\circ - 140^\\circ = 40^\\circ')}.",
                    f"Since exterior angles sum to {m('360^\\circ')}, the number of sides is {m(r'n = \frac{360^\circ}{40^\circ} = 9')}.",
                ],
                check_en=f"Interior sum of a {m('9')}-gon is {m('7 \\times 180^\\circ = 1260^\\circ')}, and {m('1260^\\circ / 9 = 140^\\circ')}.",
                idea_ar=f"نحسب الزاوية الخارجية {m('180^\\circ - 140^\\circ = 40^\\circ')} أولاً ثم نقسم {m('360^\\circ')} على {m('40^\\circ')}!",
                steps_ar=[
                    f"قياس الزاوية الخارجية: {m('e = 180^\\circ - 140^\\circ = 40^\\circ')}.",
                    f"عدد الأضلاع: {m('n = 360^\\circ \\div 40^\\circ = 9')} أضلاع.",
                ],
                check_ar=f"مجموع زوايا التساعي {m('7 \\times 180^\\circ = 1260^\\circ')}، و{m('1260^\\circ \\div 9 = 140^\\circ')}.",
                diagram_en=svg_regular_polygon(9),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-05-EX3",
                title_en="Area Scaling in Similar Triangles",
                title_ar="حساب المساحة باستخدام مربع نسبة التشابه",
                q_en=f"Two similar triangles have corresponding side lengths in the ratio {m('2 : 5')}. If the smaller triangle has area {m('16\\text{ cm}^2')}, what is the area of the larger triangle (in {m(r'\text{cm}^2')})?",
                q_ar=f"مثلثان متشابهان النسبة بين طولي ضلعين متناظرين فيهما {m('2 : 5')}. إذا كانت مساحة المثلث الأصغر {m('16')} سم²، فما مساحة المثلث الأكبر بالـ سم²؟",
                correct_val=100,
                distractors=[40, 64, 80],
                idea_en=f"Square the side ratio {m('(2/5)^2 = 4/25')} to get the ratio of areas!",
                steps_en=[
                    f"Area ratio equals {m(r'\left(\frac{2}{5}\right)^2 = \frac{4}{25}')}.",
                    f"Solve {m(r'\frac{16}{A} = \frac{4}{25} \implies A = \frac{16 \times 25}{4} = 100\text{ cm}^2')}.",
                ],
                check_en=f"Scale factor is {m('k = 2.5')}, and {m('16 \\times 2.5^2 = 16 \\times 6.25 = 100')}.",
                idea_ar=f"نربّع نسبة التشابه {m('(2/5)^2 = 4/25')} للحصول على نسبة المساحتين!",
                steps_ar=[
                    f"نسبة المساحتين تساوي مربع نسبة الضلعين: {m(r'\frac{4}{25}')}.",
                    f"إذن {m(r'\frac{16}{A} = \frac{4}{25} \implies A = \frac{16 \times 25}{4} = 100')} سم².",
                ],
                check_ar=f"معامل التكبير {m('2.5')}، و{m('16 \\times (2.5)^2 = 100')}.",
                diagram_en=svg_g9_similar_triangles("2k", "A = 16", "5k", "A = ?", nested=False),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-05-EX4",
                title_en="Composite Reflection & Translation on the Plane",
                title_ar="تركيب انعكاس وانسحاب في المستوى الإحداثي",
                q_en=f"Point {m('P(-4, 3)')} is reflected across the {m('y')}-axis and then translated {m('2')} units down. What are the coordinates of the final image {m(r'P^{\prime\prime}')}?",
                q_ar=f"انعكست النقطة {m('P(-4, 3)')} حول محور الصادات {m('y')} ثم أُزيحت بمقدار وحدتين إلى الأسفل. ما إحداثيا الصورة النهائية {m(r'P^{\prime\prime}')}؟",
                correct_val="(4, 1)",
                distractors=["(-4, 1)", "(4, 5)", "(-4, -5)"],
                idea_en=f"Reflection across the {m('y')}-axis negates {m('x')}, and translating {m('2')} units down subtracts {m('2')} from {m('y')}!",
                steps_en=[
                    f"Reflect {m('P(-4, 3)')} across the {m('y')}-axis: {m(r'P^\prime = (-(-4), 3) = (4, 3)')}.",
                    f"Translate {m('2')} units down: {m(r'P^{\prime\prime} = (4, 3 - 2) = (4, 1)')}.",
                ],
                check_en=f"{m('(4, 1)')} lies in Quadrant I, {m('4')} units right of the {m('y')}-axis and {m('1')} unit above the {m('x')}-axis.",
                idea_ar=f"الانعكاس حول محور الصادات يعكس إشارة الإحداثي السيني {m('x')}، والانسحاب للأسفل يطرح {m('2')} من {m('y')}!",
                steps_ar=[
                    f"بالانعكاس حول محور الصادات تصبح النقطة {m(r'P^\prime(4, 3)')}.",
                    f"بالانسحاب وحدتين للأسفل: {m(r'P^{\prime\prime}(4, 3 - 2) = (4, 1)')}.",
                ],
                check_ar=f"النقطة {m('(4, 1)')} تقع في الربع الأول بعد عكس إشارة {m('-4')} وطرح {m('2')} من {m('3')}.",
                diagram_en=svg_nafes_coordinate_line([(-4, 3, "P(-4,3)"), (4, 3, "P'(4,3)"), (4, 1, "P''(4,1)")], max_coord=6),
            ),
        ],
        blueprints=["G9-GEO-05", "G9-GEO-06", "G9-GEO-07", "G9-GEO-08"],
    )


def _lesson_3_6() -> dict:
    return make_nafes_lesson(
        lesson_id="NAFS-L3-06",
        level=LEVEL,
        unit_num="3.6",
        topic="Data & Probability",
        title_en="Box Plots & Quartiles, Histograms/Two-Way Tables, Permutations/Combinations & Compound Probability",
        title_ar="الصندوق وطرفاه والربيعيات، المدرجات التكرارية، التباديل والتوافيق، والاحتمال المركب",
        summary_en=(
            "Interpret box-and-whisker quartiles and IQR, analyze grouped histograms, weighted means, and conditional two-way tables, "
            "distinguish permutations P(n, r) from combinations C(n, r), and compute compound probabilities."
        ),
        summary_ar=(
            "تفسير التمثيل بالصندوق وطرفيه والمدى الربيعي، وتحليل المدرجات التكرارية والمتوسط المرجح والجداول المزدوجة المشروطة، "
            "والتمييز بين التباديل والتوافيق، وحساب الاحتمالات المركبة المستقلة وغير المستقلة والمتنافية."
        ),
        goals_en=[
            f"Read minimum, {m('Q_1')}, median ({m('Q_2')}), {m('Q_3')}, maximum, range, and {m(r'\text{IQR} = Q_3 - Q_1')} from box plots, using {m('25\\%')} per section.",
            f"Compute weighted averages, read grouped histograms, and calculate joint and conditional relative frequencies from two-way tables.",
            f"Choose **permutations** {m('P(n, r) = \\frac{n!}{(n-r)!}')} when order matters (codes, ranks) and **combinations** {m(r'\binom{n}{r} = \frac{n!}{r!(n-r)!}')} when order does not (committees).",
            f"Calculate compound probabilities with replacement (independent), without replacement (dependent), and unions {m('P(A \\cup B) = P(A) + P(B) - P(A \\cap B)')}.",
        ],
        goals_ar=[
            f"قراءة القيمة الصغرى، الربيع الأدنى {m('Q_1')}، الوسيط، الربيع الأعلى {m('Q_3')}، القيمة العظمى، والمدى الربيعي {m('Q_3 - Q_1')} وتفسير نسب الأرباع ({m('25\\%')}).",
            f"حساب المتوسط الحسابي المرجح، وقراءة المدرجات التكرارية، وحساب التكرارات النسبية المشروطة من الجداول المزدوجة.",
            f"استخدام **التباديل** {m('P(n, r)')} عندما يكون الترتيب مهماً، و**التوافيق** {m('C(n, r)')} عندما لا يكون الترتيب مهماً (اللجان والفرق).",
            f"حساب الاحتمال المركب مع الإرجاع (مستقلة) وبدون إرجاع (غير مستقلة) واحتمال الاتحاد {m('P(A \\cup B) = P(A) + P(B) - P(A \\cap B)')}.",
        ],
        concepts=[
            nafes_concept(
                title_en="1. Five-Number Summary, Box Plots & Interquartile Range (IQR)",
                title_ar="١. الملخص الخماسي، التمثيل بالصندوق وطرفيه، والمدى الربيعي (IQR)",
                body_en=(
                    f"A **box-and-whisker plot** divides an ordered dataset into **four quarters** (about {m('25\\%')} of the data in each section): "
                    f"left whisker ({m(r'\text{Min} \to Q_1')}), left half of box ({m(r'Q_1 \to \text{Median}')}), right half of box ({m(r'\text{Median} \to Q_3')}), "
                    f"and right whisker ({m(r'Q_3 \to \text{Max}')}). Thus the central box holds the middle {m('50\\%')} of observations with spread {m(r'\text{IQR} = Q_3 - Q_1')}, "
                    f"and {m('75\\%')} of values lie at or above {m('Q_1')} (and {m('75\\%')} at or below {m('Q_3')})."
                ),
                body_ar=(
                    f"يقسّم **التمثيل بالصندوق وطرفيه** البيانات المرتبة إلى **أربعة أرباع** يحوي كل منها قرابة {m('25\\%')} من البيانات. "
                    f"يمتد الصندوق الأوسط من الربيع الأدنى {m('Q_1')} إلى الربيع الأعلى {m('Q_3')} ليضم {m('50\\%')} الوسطى من القيم، وطوله هو **المدى الربيعي** "
                    f"{m(r'\text{IQR} = Q_3 - Q_1')}، بينما المدى الكلي {m(r'\text{Max} - \text{Min}')}."
                ),
                formula_en=dm(r"\text{Range} = \text{Max} - \text{Min}, \qquad \text{IQR} = Q_3 - Q_1 \;\;(\text{middle } 50\%)"),
                caption_ar="قانون المدى الكلي والمدى الربيعي في الصندوق وطرفيه:",
                formula_math_ar=dm(r"\text{Range} = \text{Max} - \text{Min}, \qquad \text{IQR} = Q_3 - Q_1"),
                diagram_en=svg_nafes_box_plot(40, 55, 70, 82, 95, "25% | 25% | 25% | 25%"),
            ),
            nafes_concept(
                title_en="2. Grouped Histograms, Weighted Means & Two-Way Frequency Tables",
                title_ar="٢. المدرجات التكرارية، المتوسط المرجح، والجداول المزدوجة",
                body_en=(
                    f"In a **weighted mean**, multiply each value {m('x_i')} by its weight/frequency {m('w_i')} and divide by total weight {m(r'\sum w_i')}. "
                    f"In a **two-way contingency table**, pay strict attention to the denominator! A **joint** relative frequency divides by the **grand total**, "
                    f"whereas a **conditional** probability ('given that the student is in row R') divides only by that **row's marginal total**."
                ),
                body_ar=(
                    f"لحساب **المتوسط المرجح** نضرب كل قيمة {m('x_i')} في تكرارها أو وزنها {m('w_i')} ونقسم على مجموع الأوزان {m(r'\sum w_i')}. "
                    f"وفي **الجداول المزدوجة** انتبه للمقام بدقة! التكرار النسبي المشترك يقسم على **المجموع الكلي**، أما الاحتمال **المشروط** فيقسم على مجموع الصف أو العمود المشروط فقط."
                ),
                formula_en=dm(r"\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}, \qquad P(A \mid B) = \frac{\text{Count}(A \cap B)}{\text{Count}(B)}"),
                caption_ar="قانون المتوسط المرجح والاحتمال المشروط من الجدول المزدوج:",
                formula_math_ar=dm(r"\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}, \qquad P(A \mid B) = \frac{n(A \cap B)}{n(B)}"),
                diagram_en=svg_g9_histogram([("50–60", 4, "4"), ("60–70", 9, "9"), ("70–80", 12, "12"), ("80–90", 5, "5")], "Grouped Frequency Histogram"),
            ),
            nafes_concept(
                title_en="3. Permutations vs Combinations & Compound Probability",
                title_ar="٣. التباديل والتوافيق، والاحتمالات المركبة",
                body_en=(
                    f"Ask one decisive question: **Does changing the order create a different outcome?** For passwords, podium medals, or president/secretary roles, "
                    f"order **matters** — use permutations {m('P(n,r) = n(n-1)\\cdots(n-r+1)')}. For committees or handshakes, order **does not matter** — "
                    f"divide by {m('r!')} to get {m(r'C(n,r) = \binom{n}{r}')}. For two draws **without replacement**, reduce both the favorable count (if matched) and total by {m('1')} on the second draw!"
                ),
                body_ar=(
                    f"اسأل سؤالاً حاسماً: **هل تغيير الترتيب يعطي نتيجة مختلفة؟** في الأرقام السرية والمناصب والمراكز الترتيب **مهم** فنستخدم التباديل {m('P(n,r)')}؛ "
                    f"وفي اللجان والفرق والمصافحات الترتيب **غير مهم** فنقسم على {m('r!')} لاستخدام التوافيق {m('C(n,r)')}. وفي السحب **دون إرجاع** ينقص المقام بمقدار {m('1')} في السحبة الثانية!"
                ),
                formula_en=dm(r"P(n, r) = \frac{n!}{(n-r)!}, \qquad C(n, r) = \frac{P(n,r)}{r!}, \qquad P(A \cup B) = P(A) + P(B) - P(A \cap B)"),
                caption_ar="قوانين التباديل والتوافيق وقاعدة جمع الاحتمالات غير المتنافية:",
                formula_math_ar=dm(r"P(n, r) = \frac{n!}{(n-r)!}, \qquad C(n, r) = \frac{n!}{r!(n-r)!}, \qquad P(A \cup B) = P(A) + P(B) - P(A \cap B)"),
                diagram_en=svg_g9_code_slots(["n", "n − 1", "n − 2"], "P(n,3) ordered  |  C(n,3) = P(n,3) ÷ 3!"),
            ),
        ],
        traps_en=[
            f"Assuming a longer whisker in a box plot contains **more data points** than a shorter box section — every quartile section holds {m('25\\%')} of the data; length shows **spread**, not count!",
            f"Using {m('P(n, r)')} instead of {m('C(n, r)')} when choosing an unordered committee, overcounting by a factor of {m('r!')}.",
            f"Keeping the same denominator on the second draw in a **without-replacement** problem, or forgetting to subtract {m('P(A \\cap B)')} when events overlap.",
        ],
        traps_ar=[
            f"الظن بأن الطرف الأطول في الصندوق وطرفيه يحتوي بيانات أكثر؛ كل ربع يضم {m('25\\%')} من البيانات تماماً، والطول يقيس التشتت لا العدد!",
            f"استخدام التباديل {m('P(n, r)')} بدلاً من التوافيق {m('C(n, r)')} عند اختيار لجنة غير مرتبة مما يضاعف الإجابة {m('r!')} مرة.",
            f"إبقاء المقام ثابتاً في السحبة الثانية عند السحب **بدون إرجاع**، أو نسيان طرح التقاطع {m('P(A \\cap B)')} في الحوادث غير المتنافية.",
        ],
        examples=[
            nafes_worked_example(
                ex_id="NAFS-L3-06-EX1",
                title_en="Interquartile Range (IQR) from a Box Plot",
                title_ar="حساب المدى الربيعي من التمثيل بالصندوق وطرفيه",
                q_en=f"A box-and-whisker plot of Grade 9 science scores has minimum {m('48')}, {m('Q_1 = 62')}, median {m('74')}, {m('Q_3 = 85')}, and maximum {m('96')}. What is the interquartile range ({m(r'\text{IQR}')})?",
                q_ar=f"في تمثيل بالصندوق وطرفيه لدرجات طلاب الصف الثالث المتوسط في العلوم، كانت القيمة الصغرى {m('48')}، والربيع الأدنى {m('Q_1 = 62')}، والوسيط {m('74')}، والربيع الأعلى {m('Q_3 = 85')}، والعظمى {m('96')}. ما المدى الربيعي؟",
                correct_val=23,
                distractors=[12, 34, 48],
                idea_en=f"The interquartile range is the width of the box: {m(r'\text{IQR} = Q_3 - Q_1')}!",
                steps_en=[
                    f"Read the quartiles: {m('Q_1 = 62')} and {m('Q_3 = 85')}.",
                    f"Subtract: {m(r'\text{IQR} = 85 - 62 = 23')}.",
                ],
                check_en=f"Note that {m('96 - 48 = 48')} is the full range, while {m('85 - 62 = 23')} is the IQR of the middle {m('50\\%')}.",
                idea_ar=f"المدى الربيعي هو طول الصندوق الأوسط أي الفرق {m('Q_3 - Q_1')}!",
                steps_ar=[
                    f"نحدد الربيع الأعلى {m('Q_3 = 85')} والربيع الأدنى {m('Q_1 = 62')}.",
                    f"نطرح: {m(r'\text{IQR} = 85 - 62 = 23')}.",
                ],
                check_ar=f"المدى الكلي {m('96 - 48 = 48')}، أما المدى الربيعي فهو {m('85 - 62 = 23')}.",
                diagram_en=svg_nafes_box_plot(48, 62, 74, 85, 96, "Grade 9 Science Scores"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-06-EX2",
                title_en="Conditional Probability from a Two-Way Table",
                title_ar="الاحتمال المشروط من جدول تكراري مزدوج",
                q_en=(
                    f"In a two-way table of {m('120')} Grade 9 students, {m('27')} boys and {m('18')} girls joined Robotics, while {m('48')} boys and {m('27')} girls joined Coding. "
                    f"Given that a randomly chosen student is a **girl**, what is the probability she joined Robotics?"
                ),
                q_ar=(
                    f"في جدول مزدوج لـ {m('120')} طالباً وطالبة بالصف الثالث المتوسط، التحق بنادي الروبوت {m('27')} طالباً و{m('18')} طالبة، وبنادي البرمجة {m('48')} طالباً و{m('27')} طالبة. "
                    f"إذا اختيرت **طالبة** عشوائياً، فما احتمال أن تكون من نادي الروبوت؟"
                ),
                correct_val=Fraction(2, 5),
                distractors=[Fraction(3, 20), Fraction(2, 3), Fraction(3, 5)],
                idea_en="Restrict the sample space to the Girls row only (18 + 27 = 45 girls)!",
                steps_en=[
                    f"Total number of girls is {m('18 + 27 = 45')}.",
                    f"Among those {m('45')} girls, {m('18')} joined Robotics.",
                    f"Conditional probability: {m(r'\frac{18}{45} = \frac{2}{5}')}.",
                ],
                check_en=f"Girls in Coding give {m('27/45 = 3/5')}, and {m('2/5 + 3/5 = 1')}.",
                idea_ar="نحصر فضاء العينة في صف الطالبات فقط ({m('18 + 27 = 45')} طالبة)!",
                steps_ar=[
                    f"مجموع الطالبات: {m('18 + 27 = 45')} طالبة.",
                    f"عدد طالبات نادي الروبوت {m('18')}، فالاحتمال المشروط {m(r'\frac{18}{45} = \frac{2}{5}')}.",
                ],
                check_ar=f"احتمال البرمجة للطالبات {m('27/45 = 3/5')} ومجموعهما {m('1')}.",
                diagram_en=svg_nafes_function_table(
                    ["Group", "Robotics", "Coding", "Total"],
                    [["Boys", "27", "48", "75"], ["Girls", "18", "27", "45"]],
                    highlight_cell=(1, 1),
                ),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-06-EX3",
                title_en="Selecting an Unordered 3-Student Robotics Team",
                title_ar="اختيار فريق ثلاثي غير مرتب بالتوافيق",
                q_en=f"A coach selects a {m('3')}-student team (with no assigned roles) from {m('8')} qualified finalists. How many distinct teams can be formed?",
                q_ar=f"يختار مدرب فريقاً مكوناً من {m('3')} طلاب (دون تحديد مناصب) من بين {m('8')} متأهلين. بكم طريقة مختلفة يمكن تكوين الفريق؟",
                correct_val=56,
                distractors=[24, 168, 336],
                idea_en=f"Since roles are identical, order does NOT matter — compute {m(r'C(8, 3) = \binom{8}{3}')}!",
                steps_en=[
                    f"Ordered picks would be {m('8 \\times 7 \\times 6 = 336')}.",
                    f"Divide by {m('3! = 6')} to remove ordering: {m(r'\binom{8}{3} = \frac{336}{6} = 56')}.",
                ],
                check_en=f"{m(r'\frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 8 \times 7 = 56')}.",
                idea_ar=f"بما أنه لا توجد مناصب فإن الترتيب غير مهم، لذا نستخدم التوافيق {m(r'\binom{8}{3}')}!",
                steps_ar=[
                    f"نطبّق قانون التوافيق: {m(r'C(8, 3) = \frac{8 \times 7 \times 6}{3 \times 2 \times 1}')}.",
                    f"نختصر {m('6')} مع {m('3 \\times 2')} فينتج {m('8 \\times 7 = 56')} فريقاً مختلفاً.",
                ],
                check_ar=f"التباديل {m('336')} وقسمتها على {m('3! = 6')} تعطي {m('56')}.",
                diagram_en=svg_g9_code_slots(["8", "7", "6"], "Unordered team: C(8,3) = (8×7×6) ÷ 3!"),
            ),
            nafes_worked_example(
                ex_id="NAFS-L3-06-EX4",
                title_en="Dependent Compound Probability Without Replacement",
                title_ar="الاحتمال المركب لحادثتين غير مستقلتين بدون إرجاع",
                q_en=f"A box holds {m('5')} blue markers and {m('3')} red markers. If {m('2')} markers are drawn at random **without replacement**, what is the probability that both are blue?",
                q_ar=f"يحتوي صندوق على {m('5')} أقلام زرقاء و{m('3')} أقلام حمراء. إذا سُحب قلمان عشوائياً **دون إرجاع**، فما احتمال أن يكونا أزرقين معاً؟",
                correct_val=Fraction(5, 14),
                distractors=[Fraction(25, 64), Fraction(3, 28), Fraction(5, 8)],
                idea_en=f"Multiply {m('P(\\text{1st blue})')} by {m('P(\\text{2nd blue} \\mid \\text{1st blue})')}, decreasing both blue count and total by {m('1')}!",
                steps_en=[
                    f"First draw: {m('5')} blue out of {m('8')} total markers gives {m(r'\frac{5}{8}')}.",
                    f"Second draw (without replacement): {m('4')} blue remain out of {m('7')} markers, giving {m(r'\frac{4}{7}')}.",
                    f"Multiply: {m(r'\frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}')}.",
                ],
                check_en=f"Combinatorial check: {m(r'\frac{\binom{5}{2}}{\binom{8}{2}} = \frac{10}{28} = \frac{5}{14}')}.",
                idea_ar=f"نضرب احتمال سحب الأول أزرق في احتمال سحب الثاني أزرق بعد نقصان الأقلام الزرقاء والعدد الكلي بمقدار {m('1')}!",
                steps_ar=[
                    f"احتمال الأول أزرق: {m(r'\frac{5}{8}')}.",
                    f"بعد عدم الإرجاع يتبقى {m('4')} أقلام زرقاء من أصل {m('7')}، فاحتمال الثاني أزرق {m(r'\frac{4}{7}')}.",
                    f"الاحتمال المركب: {m(r'\frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}')}.",
                ],
                check_ar=f"بالتوافيق: {m(r'\frac{C(5,2)}{C(8,2)} = \frac{10}{28} = \frac{5}{14}')}.",
                diagram_en=svg_g9_marble_bag([("Blue", 5, "#93c5fd"), ("Red", 3, "#fca5a5")], "2 draws without replacement"),
            ),
        ],
        blueprints=["G9-DAT-01", "G9-DAT-02", "G9-DAT-03", "G9-DAT-04"],
    )


def get_grade9_lessons() -> list[dict]:
    """Return all 6 Grade 9 ETEC Nafes bilingual study lessons (NAFS-L3-01 .. NAFS-L3-06)."""
    return [
        _lesson_3_1(),
        _lesson_3_2(),
        _lesson_3_3(),
        _lesson_3_4(),
        _lesson_3_5(),
        _lesson_3_6(),
    ]
