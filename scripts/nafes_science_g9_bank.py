"""ETEC Nafes KSA Science Grade 9 (العلوم — الصف الثالث المتوسط) Question Bank — 360 Verified 4-Option (A–D) MCQs.

Covers all 24 Grade 9 science blueprints (G9-SCI-B01 .. G9-SCI-B24), 15 variants each
(5 Easy [Knowing], 5 Medium [Applying], 5 Hard [Reasoning] = 120 Easy + 120 Medium + 120 Hard = 360 questions),
with 4 domains of 90 questions each and comprehensive bilingual XML-valid SVG diagrams.
"""
from fractions import Fraction
import math
import re
import xml.etree.ElementTree as ET

from kmc_common import m, norm_text
from kmc_diagrams import BLUE, GREEN, MUTED, ORANGE, RED, SHADE, SHADE_ALT, STROKE, WATER, _esc as esc
from nafes_ext_common import (
    LINE_GRID,
    PURPLE,
    SLATE_BG,
    TEAL,
    _ext_svg,
    make_science_concept_q,
    make_science_math_q,
    svg_atom_bohr,
    svg_cell_diagram,
    svg_earth_layers,
    svg_energy_pyramid,
    svg_force_block,
    svg_motion_graph,
    svg_ohm_circuit,
    svg_ph_scale,
    svg_plate_boundary,
    svg_punnett_square,
    svg_wave_diagram,
)

LEVEL = "Science · Grade 9"

T_LIFE = "Life Sciences"
T_CHEM = "Chemistry & Matter"
T_PHYS = "Physics: Forces & Energy"
T_EARTH = "Earth & Space Sciences"


def _qid(idx: int) -> str:
    return f"NAFS-SCI-G9-{idx:03d}"


def _diff(idx: int) -> str:
    if idx < 5:
        return "Easy"
    if idx < 10:
        return "Medium"
    return "Hard"


# ==============================================================================
# Bilingual SVG Localization & Custom Grade 9 Science SVG Generators
# ==============================================================================

_BASE_AR_SVG_MAP = {
    "Cell Wall": "الجدار الخلوي",
    "Nucleus": "النواة",
    "Vacuole": "الفجوة",
    "Chloroplast": "البلاستيدة",
    "Membrane": "الغشاء",
    "Mitochondria": "الميتوكوندريا",
    "Cytoplasm": "السيتوبلازم",
    "Acidic": "حمضي",
    "Neutral (7)": "متعادل (7)",
    "Basic": "قاعدي",
    "Object": "جسم",
    "Crust": "القشرة",
    "Mantle": "الوشاح",
    "Outer Core": "اللب الخارجي",
    "Inner Core": "اللب الداخلي",
    "Plate A": "الصفيحة أ",
    "Plate B": "الصفيحة ب",
    "Boundary: Convergent": "حدود متقاربة",
    "Boundary: Divergent": "حدود متباعدة",
    "Boundary: Transform": "حدود تحويلية",
}

_SVG_TEXT_RE = re.compile(r"(<(?:text|title)[^>]*>)([^<]+)(</(?:text|title)>)")


def _ar_svg(svg_en: str, extra: dict[str, str] | None = None) -> str:
    """Translate <text> and <title> nodes in an English SVG to concise Arabic labels."""
    mapping = dict(_BASE_AR_SVG_MAP)
    if extra:
        mapping.update(extra)

    def _repl(match: re.Match) -> str:
        open_t, body, close_t = match.group(1), match.group(2), match.group(3)
        stripped = body.strip()
        if stripped in mapping:
            return f"{open_t}{esc(mapping[stripped])}{close_t}"
        for k, v in mapping.items():
            if k in stripped:
                stripped = stripped.replace(k, v)
        return f"{open_t}{esc(stripped)}{close_t}"

    out = _SVG_TEXT_RE.sub(_repl, svg_en)
    ET.fromstring(out)
    return out


def _svg_cell_division(mode: str, diploid_n: int, lang: str = "en") -> str:
    """Clean cell-division schematic comparing 2n -> 2n (Mitosis) vs 2n -> n (Meiosis)."""
    w, h = 360, 185
    n_val = diploid_n // 2
    is_ar = lang == "ar"
    if mode == "mitosis":
        title = "الانقسام المتساوي (2n ← 2n)" if is_ar else "Mitosis (2n → 2n)"
        parent_lbl = f"خلية أصل {diploid_n}" if is_ar else f"Parent: {diploid_n}"
        child_lbl = f"2n = {diploid_n}"
        count = 2
        col, fill = BLUE, "#dbeafe"
        sub = "خليتان متطابقتان" if is_ar else "2 identical diploid cells"
    else:
        title = "الانقسام المنصف (2n ← n)" if is_ar else "Meiosis (2n → n)"
        parent_lbl = f"خلية أصل {diploid_n}" if is_ar else f"Parent: {diploid_n}"
        child_lbl = f"n = {n_val}"
        count = 4
        col, fill = TEAL, "#ccfbf1"
        sub = "4 أمشاج أحادية المجموعة" if is_ar else "4 haploid gametes"

    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="72" cy="96" r="30" fill="#fef3c7" stroke="{ORANGE}" stroke-width="2"/>',
        f'<text x="72" y="100" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">2n = {diploid_n}</text>',
        f'<text x="72" y="142" text-anchor="middle" font-size="11.5" font-weight="600" fill="{MUTED}">{esc(parent_lbl)}</text>',
    ]
    if count == 2:
        ys = [72, 122]
        cx = 264
        for cy in ys:
            parts.append(f'<line x1="104" y1="96" x2="{cx-28}" y2="{cy}" stroke="{STROKE}" stroke-width="1.8"/>')
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="{fill}" stroke="{col}" stroke-width="1.8"/>')
            parts.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(child_lbl)}</text>')
    else:
        ys = [55, 84, 113, 142]
        cx = 270
        for cy in ys:
            parts.append(f'<line x1="104" y1="96" x2="{cx-22}" y2="{cy}" stroke="{STROKE}" stroke-width="1.5"/>')
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{fill}" stroke="{col}" stroke-width="1.7"/>')
            parts.append(f'<text x="{cx+22}" y="{cy+4}" font-size="12" font-weight="800" fill="{STROKE}">{esc(child_lbl)}</text>')
    parts.append(f'<text x="180" y="168" text-anchor="middle" font-size="11.5" font-weight="700" fill="{col}">{esc(sub)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_reflex_arc(blocked: str = "None", lang: str = "en") -> str:
    """5-node reflex arc pathway with optional lesion highlight."""
    w, h = 380, 150
    is_ar = lang == "ar"
    title = "مسار القوس الانعكاسي" if is_ar else "Reflex Arc Pathway"
    nodes = [
        ("Receptor", "المستقبل", "#fef3c7", ORANGE),
        ("Sensory", "عصبون حسي", "#dbeafe", BLUE),
        ("Spinal", "الحبل الشوكي", "#ede9fe", PURPLE),
        ("Motor", "عصبون حركي", "#ccfbf1", TEAL),
        ("Effector", "العضلة", "#dcfce7", GREEN),
    ]
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="190" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    bw, gap = 60, 10
    x0 = 20
    for idx, (en_lbl, ar_lbl, fc, ec) in enumerate(nodes):
        x = x0 + idx * (bw + gap)
        is_blk = blocked.lower() in en_lbl.lower() and blocked != "None"
        stroke_c = RED if is_blk else ec
        fill_c = "#fee2e2" if is_blk else fc
        lbl = ar_lbl if is_ar else en_lbl
        parts.append(f'<rect x="{x}" y="54" width="{bw}" height="48" rx="8" fill="{fill_c}" stroke="{stroke_c}" stroke-width="2"/>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
        if is_blk:
            blk_txt = "مقطوع X" if is_ar else "Blocked X"
            parts.append(f'<text x="{x+bw/2:.1f}" y="122" text-anchor="middle" font-size="11.5" font-weight="800" fill="{RED}">{esc(blk_txt)}</text>')
        if idx < len(nodes) - 1:
            ax1, ax2 = x + bw + 1, x + bw + gap - 2
            parts.append(f'<line x1="{ax1}" y1="78" x2="{ax2}" y2="78" stroke="{STROKE}" stroke-width="1.8"/>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_osmosis_membrane(left_pct: str, right_pct: str, left_lbl_en: str, right_lbl_en: str,
                          left_lbl_ar: str, right_lbl_ar: str, lang: str = "en") -> str:
    """Semi-permeable membrane split container comparing solute concentrations."""
    w, h = 360, 170
    is_ar = lang == "ar"
    title = "غشاء شبه منفذ (الأسموزية)" if is_ar else "Semi-Permeable Membrane"
    mem_txt = "غشاء" if is_ar else "Membrane"
    ll = left_lbl_ar if is_ar else left_lbl_en
    rl = right_lbl_ar if is_ar else right_lbl_en
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="44" y="48" width="136" height="84" fill="#e0f2fe" stroke="{BLUE}" stroke-width="1.6"/>',
        f'<rect x="180" y="48" width="136" height="84" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.6"/>',
        f'<line x1="180" y1="46" x2="180" y2="134" stroke="{RED}" stroke-width="3" stroke-dasharray="5 4"/>',
        f'<text x="112" y="82" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{esc(left_pct)}</text>',
        f'<text x="112" y="106" text-anchor="middle" font-size="12" font-weight="600" fill="{BLUE}">{esc(ll)}</text>',
        f'<text x="248" y="82" text-anchor="middle" font-size="13" font-weight="800" fill="{STROKE}">{esc(right_pct)}</text>',
        f'<text x="248" y="106" text-anchor="middle" font-size="12" font-weight="600" fill="{ORANGE}">{esc(rl)}</text>',
        f'<text x="180" y="152" text-anchor="middle" font-size="11.5" font-weight="700" fill="{RED}">{esc(mem_txt)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_mass_balance(react_en: str, prod_en: str, react_ar: str, prod_ar: str, lang: str = "en") -> str:
    """Closed-system reaction mass conservation box."""
    w, h = 360, 145
    is_ar = lang == "ar"
    title = "حفظ الكتلة في نظام مغلق" if is_ar else "Conservation of Mass (Closed System)"
    r_txt = react_ar if is_ar else react_en
    p_txt = prod_ar if is_ar else prod_en
    r_hdr = "المتفاعلات" if is_ar else "Reactants"
    p_hdr = "النواتج" if is_ar else "Products"
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="22" y="48" width="136" height="66" rx="9" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.8"/>',
        f'<text x="90" y="68" text-anchor="middle" font-size="11.5" font-weight="700" fill="{BLUE}">{esc(r_hdr)}</text>',
        f'<text x="90" y="94" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(r_txt)}</text>',
        f'<line x1="164" y1="81" x2="192" y2="81" stroke="{STROKE}" stroke-width="2.4"/>',
        f'<polygon points="192,75 200,81 192,87" fill="{STROKE}"/>',
        f'<rect x="202" y="48" width="136" height="66" rx="9" fill="#dcfce7" stroke="{GREEN}" stroke-width="1.8"/>',
        f'<text x="270" y="68" text-anchor="middle" font-size="11.5" font-weight="700" fill="{GREEN}">{esc(p_hdr)}</text>',
        f'<text x="270" y="94" text-anchor="middle" font-size="12.5" font-weight="800" fill="{STROKE}">{esc(p_txt)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_energy_profile(e_r: int, e_peak: int, e_p: int, e_cat: int | None = None, lang: str = "en") -> str:
    """Reaction potential-energy profile (kJ) with optional catalyzed dashed peak."""
    w, h = 360, 195
    is_ar = lang == "ar"
    title = "مخطط طاقة التفاعل (kJ)" if is_ar else "Reaction Energy Profile (kJ)"
    xlbl = "سير التفاعل" if is_ar else "Reaction Progress"
    max_e = max(e_peak, e_r, e_p) + 20
    ox, oy, gw, gh = 54, 152, 276, 102

    def sy(val: float) -> float:
        return oy - (val / max_e) * gh

    yr, yp_pk, yp = sy(e_r), sy(e_peak), sy(e_p)
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="{ox}" y1="{oy}" x2="{ox+gw}" y2="{oy}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-gh}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<path d="M {ox+12},{yr:.1f} L {ox+68},{yr:.1f} Q {ox+138},{yp_pk-26:.1f} {ox+195},{yp:.1f} L {ox+262},{yp:.1f}" '
        f'fill="none" stroke="{BLUE}" stroke-width="2.6"/>',
    ]
    peak_y = (yr + yp) * 0.5 + (yp_pk - 26 - (yr + yp) * 0.5) * 0.5
    # Simpler explicit quadratic peak passing right through (ox+138, yp_pk)
    parts[-1] = (
        f'<polyline points="{ox+12},{yr:.1f} {ox+68},{yr:.1f} {ox+138},{yp_pk:.1f} {ox+208},{yp:.1f} {ox+262},{yp:.1f}" '
        f'fill="none" stroke="{BLUE}" stroke-width="2.6" stroke-linejoin="round"/>'
    )
    if e_cat is not None:
        ycat = sy(e_cat)
        parts.append(
            f'<polyline points="{ox+68},{yr:.1f} {ox+138},{ycat:.1f} {ox+208},{yp:.1f}" '
            f'fill="none" stroke="{RED}" stroke-width="2.2" stroke-dasharray="5 3"/>'
        )
        parts.append(f'<text x="{ox+164}" y="{ycat+14:.1f}" font-size="11.5" font-weight="700" fill="{RED}">{e_cat} kJ</text>')
    parts.append(f'<text x="{ox+40}" y="{yr-8:.1f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{e_r} kJ</text>')
    parts.append(f'<text x="{ox+138}" y="{yp_pk-7:.1f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{BLUE}">{e_peak} kJ</text>')
    parts.append(f'<text x="{ox+236}" y="{yp-8:.1f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{GREEN}">{e_p} kJ</text>')
    parts.append(f'<text x="{ox+gw/2:.1f}" y="{h-14}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(xlbl)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_seismogram(t_p: int, t_s: int, lang: str = "en") -> str:
    """Seismogram showing P-wave and S-wave arrival times."""
    w, h = 360, 165
    is_ar = lang == "ar"
    title = "مخطط السيزموجرام (P و S)" if is_ar else "Seismogram P and S Arrivals"
    xlbl = "الزمن (ث)" if is_ar else "Time (s)"
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="34" y1="92" x2="326" y2="92" stroke="{MUTED}" stroke-width="1.3"/>',
        f'<polyline points="34,92 84,92 92,76 100,108 108,82 116,98 124,92 204,92 214,56 226,126 238,62 250,118 262,80 274,92 326,92" '
        f'fill="none" stroke="{BLUE}" stroke-width="2.2"/>',
        f'<text x="100" y="54" text-anchor="middle" font-size="12" font-weight="800" fill="{TEAL}">P: {t_p} s</text>',
        f'<text x="228" y="48" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">S: {t_s} s</text>',
        f'<text x="180" y="144" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(xlbl)}: Δt = {t_s - t_p} s</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_half_life(n0: int, hl: int, unit_en: str, unit_ar: str, k_steps: int, lang: str = "en") -> str:
    """Radioactive decay bar chart across half-life intervals."""
    w, h = 360, 185
    is_ar = lang == "ar"
    title = "منحنى الاضمحلال الإشعاعي" if is_ar else "Radioactive Half-Life Decay"
    unit = unit_ar if is_ar else unit_en
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="42" y1="142" x2="328" y2="142" stroke="{STROKE}" stroke-width="1.8"/>',
    ]
    n_bars = min(5, k_steps + 1)
    bw = 38
    gap = (276 - n_bars * bw) / max(1, n_bars - 1)
    max_bh = 86
    for i in range(n_bars):
        val = n0 / (2 ** i)
        bh = max(6, max_bh * (val / n0))
        x = 48 + i * (bw + gap)
        y = 142 - bh
        v_txt = f"{val:g}g"
        t_txt = f"{i*hl} {unit}"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{bh:.1f}" rx="4" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.6"/>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(v_txt)}</text>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="160" text-anchor="middle" font-size="11.5" font-weight="600" fill="{MUTED}">{esc(t_txt)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_atmosphere(highlight: str, lang: str = "en") -> str:
    """4 atmospheric layers stacked vertically with altitude bands."""
    w, h = 360, 195
    is_ar = lang == "ar"
    title = "طبقات الغلاف الجوي" if is_ar else "Atmospheric Layers"
    layers = [
        ("Thermosphere", "الثيرموسفير (80+ km)", "Thermosphere (80+ km)", "#ede9fe", PURPLE),
        ("Mesosphere", "الميزوسفير (50-80 km)", "Mesosphere (50-80 km)", "#e0f2fe", BLUE),
        ("Stratosphere", "الستراتوسفير (12-50 km)", "Stratosphere (12-50 km)", "#ccfbf1", TEAL),
        ("Troposphere", "التروبوسفير (0-12 km)", "Troposphere (0-12 km)", "#fef3c7", ORANGE),
    ]
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    y0, lh = 40, 32
    for idx, (key, ar_lbl, en_lbl, fc, ec) in enumerate(layers):
        y = y0 + idx * (lh + 4)
        is_hi = highlight.lower() in key.lower()
        sw = "2.6" if is_hi else "1.3"
        sc = RED if is_hi else ec
        lbl = ar_lbl if is_ar else en_lbl
        parts.append(f'<rect x="34" y="{y}" width="292" height="{lh}" rx="7" fill="{fc}" stroke="{sc}" stroke-width="{sw}"/>')
        parts.append(f'<text x="180" y="{y+21}" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_tides(tide_type: str = "Spring", lang: str = "en") -> str:
    """Sun-Earth-Moon geometry for Spring vs Neap tides."""
    w, h = 360, 170
    is_ar = lang == "ar"
    if tide_type == "Spring":
        title = "المد العالي (الربيعي): اصطفاف 180°" if is_ar else "Spring Tide Alignment (0°/180°)"
        moon_x, moon_y = 300, 96
        rx_b, ry_b = 46, 26
    else:
        title = "المد المنخفض (المحاقي): تعامد 90°" if is_ar else "Neap Tide Geometry (90°)"
        moon_x, moon_y = 216, 46
        rx_b, ry_b = 34, 30
    sun_lbl = "الشمس" if is_ar else "Sun"
    earth_lbl = "الأرض" if is_ar else "Earth"
    moon_lbl = "القمر" if is_ar else "Moon"
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="52" cy="96" r="22" fill="#fde047" stroke="{ORANGE}" stroke-width="2"/>',
        f'<text x="52" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(sun_lbl)}</text>',
        f'<ellipse cx="216" cy="96" rx="{rx_b}" ry="{ry_b}" fill="#bfdbfe" stroke="{BLUE}" stroke-width="1.4" stroke-dasharray="4 3"/>',
        f'<circle cx="216" cy="96" r="18" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>',
        f'<text x="216" y="142" text-anchor="middle" font-size="12" font-weight="700" fill="{BLUE}">{esc(earth_lbl)}</text>',
        f'<circle cx="{moon_x}" cy="{moon_y}" r="11" fill="#cbd5e1" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<text x="{moon_x}" y="{moon_y+24}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(moon_lbl)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_hr_diagram(star_en: str, star_ar: str, x_pct: float, y_pct: float, lang: str = "en") -> str:
    """Schematic H-R diagram (Hot Left -> Cool Right; Bright Top -> Dim Bottom)."""
    w, h = 360, 195
    is_ar = lang == "ar"
    title = "مخطط هرتزسبرونغ–راسل (H-R)" if is_ar else "Hertzsprung-Russell (H-R) Diagram"
    ox, oy, gw, gh = 54, 152, 268, 106
    sx = ox + max(0.05, min(0.95, x_pct)) * gw
    sy = oy - max(0.05, min(0.95, y_pct)) * gh
    star_lbl = star_ar if is_ar else star_en
    hot_l = "حار 30,000 K" if is_ar else "Hot 30,000 K"
    cool_l = "بارد 3,000 K" if is_ar else "Cool 3,000 K"
    ms_l = "التسلسل الرئيسي" if is_ar else "Main Sequence"
    rg_l = "العمالقة الحمر" if is_ar else "Red Giants"
    wd_l = "الأقزام البيضاء" if is_ar else "White Dwarfs"
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="{ox}" y1="{oy}" x2="{ox+gw}" y2="{oy}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-gh}" stroke="{STROKE}" stroke-width="1.8"/>',
        f'<line x1="{ox+22}" y1="{oy-92}" x2="{ox+gw-18}" y2="{oy-14}" stroke="{ORANGE}" stroke-width="8" stroke-opacity="0.35"/>',
        f'<text x="{ox+gw*0.52:.1f}" y="{oy-48}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{ORANGE}">{esc(ms_l)}</text>',
        f'<text x="{ox+gw-48}" y="{oy-88}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{RED}">{esc(rg_l)}</text>',
        f'<text x="{ox+58}" y="{oy-14}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{BLUE}">{esc(wd_l)}</text>',
        f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6.5" fill="{RED}" stroke="#ffffff" stroke-width="1.5"/>',
        f'<text x="{sx:.1f}" y="{sy-11:.1f}" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(star_lbl)}</text>',
        f'<text x="{ox+36}" y="{h-15}" text-anchor="middle" font-size="11.5" font-weight="600" fill="{BLUE}">{esc(hot_l)}</text>',
        f'<text x="{ox+gw-34}" y="{h-15}" text-anchor="middle" font-size="11.5" font-weight="600" fill="{RED}">{esc(cool_l)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_experiment_bars(title_en: str, title_ar: str,
                         bars: list[tuple[str, str, float, str]],
                         y_lbl_en: str, y_lbl_ar: str, lang: str = "en") -> str:
    w, h = 360, 196
    title = title_en if lang == "en" else title_ar
    y_lbl = y_lbl_en if lang == "en" else y_lbl_ar
    max_val = max((v for _, _, v, _ in bars), default=1.0) or 1.0
    palette = ["#3B82F6", "#0D9488", "#F59E0B", "#8B5CF6", "#EC4899"]
    parts = [
        f'<rect x="8" y="8" width="344" height="{h - 16}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{esc(title)}</text>',
        f'<text x="20" y="48" font-size="11.5" font-weight="600" fill="#475569" text-anchor="start">{esc(y_lbl)}</text>',
        '<line x1="20" y1="150" x2="340" y2="150" stroke="#475569" stroke-width="1.5"/>',
    ]
    n = max(len(bars), 1)
    slot = 300.0 / n
    bw = min(38.0, slot * 0.52)
    for i, (le, la, val, v_lbl) in enumerate(bars):
        cx = 30.0 + (i + 0.5) * slot
        bh = max(8.0, (val / max_val) * 76.0)
        by = 150.0 - bh
        lbl = le if lang == "en" else la
        col = palette[i % len(palette)]
        parts.append(f'<rect x="{cx - bw/2:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" fill="{col}" stroke="#1E293B" stroke-width="1.1"/>')
        parts.append(f'<text x="{cx:.1f}" y="{by - 6:.1f}" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">{esc(v_lbl)}</text>')
        parts.append(f'<text x="{cx:.1f}" y="168" font-size="11.5" font-weight="600" fill="#1E293B" text-anchor="middle">{esc(lbl)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_rock_strata(layers: list[tuple[str, str, str]],
                     dike: tuple[str, str] | None = None, lang: str = "en") -> str:
    w, h = 360, 198
    title = ("Rock Strata Cross-Section" if dike is None else "Cross-Cutting Rock Layers") if lang == "en" else ("مقطع الطبقات الصخرية" if dike is None else "الطبقات والقاطع الناري")
    parts = [
        f'<rect x="8" y="8" width="344" height="{h - 16}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{esc(title)}</text>',
    ]
    start_y, layer_h = 44, 34
    lbl_x = 180 if dike is None else 96
    for i, (le, la, fill) in enumerate(layers[:4]):
        ly = start_y + i * layer_h
        lbl = le if lang == "en" else la
        parts.append(f'<rect x="28" y="{ly}" width="304" height="{layer_h}" fill="{fill}" stroke="#334155" stroke-width="1.4"/>')
        parts.append(f'<text x="{lbl_x}" y="{ly + 22}" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">{esc(lbl)}</text>')
    if dike is not None:
        dlbl = dike[0] if lang == "en" else dike[1]
        parts.append('<rect x="164" y="78" width="32" height="104" fill="#B91C1C" stroke="#450A0A" stroke-width="1.4"/>')
        parts.append('<line x1="196" y1="129" x2="226" y2="129" stroke="#991B1B" stroke-width="2"/>')
        parts.append(f'<text x="232" y="133" font-size="12" font-weight="700" fill="#991B1B" text-anchor="start">{esc(dlbl)}</text>')
    return _ext_svg(w, h, "".join(parts), title)


def _svg_hydraulic_lift(f1_lbl: str, a1_lbl: str, a2_lbl: str,
                        f2_lbl: str = "F2 = ?", lang: str = "en") -> str:
    w, h = 360, 196
    title = "Hydraulic Lift System" if lang == "en" else "نظام المكبس الهيدروليكي"
    fluid_lbl = "Fluid" if lang == "en" else "سائل"
    parts = [
        f'<rect x="8" y="8" width="344" height="{h - 16}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{esc(title)}</text>',
        '<path d="M 46 98 L 94 98 L 94 126 L 196 126 L 196 98 L 296 98 L 296 154 L 46 154 Z" fill="#BFDBFE" stroke="none"/>',
        '<rect x="46" y="86" width="48" height="12" fill="#64748B" stroke="#1E293B" stroke-width="1.3"/>',
        '<rect x="196" y="86" width="100" height="12" fill="#64748B" stroke="#1E293B" stroke-width="1.3"/>',
        '<path d="M 46 66 L 46 154 L 296 154 L 296 66 M 94 66 L 94 126 L 196 126 L 196 66" fill="none" stroke="#1E293B" stroke-width="2"/>',
        '<line x1="70" y1="45" x2="70" y2="76" stroke="#DC2626" stroke-width="2.5"/>',
        '<polygon points="64,76 76,76 70,84" fill="#DC2626"/>',
        '<line x1="246" y1="84" x2="246" y2="53" stroke="#0D9488" stroke-width="2.5"/>',
        '<polygon points="240,53 252,53 246,45" fill="#0D9488"/>',
        f'<text x="102" y="64" font-size="11.5" font-weight="700" fill="#DC2626" text-anchor="start">{esc(f1_lbl)}</text>',
        f'<text x="302" y="64" font-size="11.5" font-weight="700" fill="#0D9488" text-anchor="start">{esc(f2_lbl)}</text>',
        f'<text x="145" y="144" font-size="11.5" font-weight="600" fill="#1E3A8A" text-anchor="middle">{esc(fluid_lbl)}</text>',
        f'<text x="70" y="175" font-size="11.5" font-weight="600" fill="#0F172A" text-anchor="middle">{esc(a1_lbl)}</text>',
        f'<text x="246" y="175" font-size="11.5" font-weight="600" fill="#0F172A" text-anchor="middle">{esc(a2_lbl)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_energy_ramp(f_push_lbl: str, len_lbl: str, h_lbl: str, w_lbl: str, lang: str = "en") -> str:
    w, h = 360, 196
    title = "Inclined Ramp System" if lang == "en" else "مستوى مائل"
    parts = [
        f'<rect x="8" y="8" width="344" height="{h - 16}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{esc(title)}</text>',
        '<polygon points="50,150 286,150 286,68" fill="#E2E8F0" stroke="#334155" stroke-width="1.8"/>',
        '<polygon points="145,103 175,92 183,115 153,126" fill="#3B82F6" stroke="#1E293B" stroke-width="1.4"/>',
        '<line x1="88" y1="126" x2="132" y2="110" stroke="#DC2626" stroke-width="2.5"/>',
        '<polygon points="128,105 138,108 132,116" fill="#DC2626"/>',
        f'<text x="150" y="72" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">{esc(len_lbl)}</text>',
        f'<text x="294" y="114" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="start">{esc(h_lbl)}</text>',
        f'<text x="92" y="174" font-size="11.5" font-weight="700" fill="#DC2626" text-anchor="middle">{esc(f_push_lbl)}</text>',
        f'<text x="245" y="174" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle">{esc(w_lbl)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


def _svg_gravity_pair(title_en: str, title_ar: str, m1_lbl: str, m2_lbl: str, r_lbl: str, lang: str = "en") -> str:
    w, h = 360, 165
    title = title_en if lang == "en" else title_ar
    parts = [
        f'<rect x="8" y="8" width="344" height="{h - 16}" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="180" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{esc(title)}</text>',
        '<circle cx="80" cy="96" r="24" fill="#3B82F6" stroke="#1E293B" stroke-width="1.5"/>',
        '<circle cx="280" cy="96" r="18" fill="#F59E0B" stroke="#1E293B" stroke-width="1.5"/>',
        '<line x1="114" y1="96" x2="252" y2="96" stroke="#334155" stroke-width="1.8" stroke-dasharray="4,3"/>',
        '<polygon points="116,91 107,96 116,101" fill="#334155"/>',
        '<polygon points="250,91 259,96 250,101" fill="#334155"/>',
        f'<text x="80" y="58" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">{esc(m1_lbl)}</text>',
        f'<text x="280" y="58" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">{esc(m2_lbl)}</text>',
        f'<text x="180" y="118" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">{esc(r_lbl)}</text>',
    ]
    return _ext_svg(w, h, "".join(parts), title)


# ==============================================================================
# DOMAIN 1: LIFE SCIENCES (G9-SCI-B01 .. G9-SCI-B06, IDs 001 .. 090)
# ==============================================================================

def _gen_sci_b01(start_idx: int) -> list[dict]:
    """G9-SCI-B01: Mitosis vs meiosis chromosome counts (2n vs n) & cell organization."""
    bp = "G9-SCI-B01"
    qs: list[dict] = []

    # 0 (Easy): Human skin cell mitosis
    qs.append(make_science_math_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        f"A human skin cell has a diploid chromosome number of {m('2n = 46')}. After undergoing one complete round of mitosis, how many chromosomes are in each daughter cell?",
        f"تحتوي خلية جلد بشرية على عدد كروموسومات ثنائي المجموعة مقداره {m('2n = 46')}. بعد انقسامها انقساماً متساوياً كاملاً، كم كروموسوماً يوجد في كل خلية ناتجة؟",
        46, [23, 92, 12],
        "Mitosis produces two genetically identical diploid daughter cells.",
        "ينتج عن الانقسام المتساوي خليتان متطابقتان وراثياً تحملان العدد الثنائي نفسه.",
        "Mitosis preserves the parent chromosome count.",
        [f"The parent cell is diploid with {m('2n = 46')}.", f"DNA replicates and divides equally into two daughter cells, each keeping {m('46')} chromosomes."],
        f"Each daughter cell matches the parent skin cell ({m('46')}).",
        "الانقسام المتساوي يحافظ على ثبات العدد الكروموسومي.",
        [f"الخلية الأصلية ثنائية المجموعة {m('2n = 46')}.", f"ينقسم الحمض النووي المتضاعف بالتساوي لتحتوي كل خلية ناتجة على {m('46')} كروموسوماً."],
        f"كل خلية بنوية تطابق الخلية الأصلية ({m('46')}).",
        diagram_en=_svg_cell_division("mitosis", 46, "en"),
        diagram_ar=_svg_cell_division("mitosis", 46, "ar"),
    ))

    # 1 (Easy): Garden pea meiosis
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        f"A garden pea plant has {m('2n = 14')} chromosomes in its leaf cells. How many chromosomes are present in a single haploid pollen grain produced by meiosis?",
        f"يحتوي نبات البازلاء على {m('2n = 14')} كروموسوماً في خلايا أوراقه. كم كروموسوماً يوجد في حبة لقاح واحدة ناتجة عن الانقسام المنصف؟",
        7, [14, 28, 4],
        "Meiosis reduces the chromosome number from diploid (2n) to haploid (n).",
        "يختزل الانقسام المنصف عدد الكروموسومات من (2n) إلى النصف (n).",
        f"Divide the diploid number {m('2n')} by {m('2')}.",
        [f"Leaf cells are diploid: {m('2n = 14')}.", f"Meiosis halves the count, giving {m('n = 14 \\div 2 = 7')} chromosomes per gamete."],
        f"Two haploid gametes fuse to restore {m('7 + 7 = 14')}.",
        "نقسم العدد الثنائي للكروموسومات على 2.",
        [f"خلايا الورقة ثنائية المجموعة: {m('2n = 14')}.", f"الانقسام المنصف ينصّف العدد ليصبح {m('n = 14 \\div 2 = 7')} كروموسومات."],
        f"عند الإخصاب يعود العدد إلى {m('7 + 7 = 14')}.",
        diagram_en=_svg_cell_division("meiosis", 14, "en"),
        diagram_ar=_svg_cell_division("meiosis", 14, "ar"),
    ))

    # 2 (Easy): Comparing mitosis vs meiosis outcome
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        "Which statement accurately contrasts meiosis with mitosis in sexually reproducing organisms?",
        "أي عبارة تصف الفرق الصحيح بين الانقسام المنصف والانقسام المتساوي في الكائنات التي تتكاثر جنسياً؟",
        [
            ("Meiosis forms 4 genetically varied haploid gametes; mitosis forms 2 identical diploid cells",
             "ينتج المنصف 4 أمشاج أحادية متباينة وراثياً، بينما ينتج المتساوي خليتين ثنائيتين متطابقتين"),
            ("Meiosis forms 2 identical diploid cells; mitosis forms 4 haploid gametes",
             "ينتج المنصف خليتين ثنائيتين متطابقتين، بينما ينتج المتساوي 4 أمشاج أحادية"),
            ("Both mitosis and meiosis double the parent chromosome number in every daughter cell",
             "كل من المتساوي والمنصف يضاعفان عدد الكروموسومات في الخلايا الناتجة"),
            ("Mitosis requires crossing-over between homologous chromosomes; meiosis skips DNA replication",
             "يتطلب المتساوي حدوث العبور الوراثي بينما يتجاوز المنصف تضاعف الحمض النووي"),
        ],
        "Think about how many divisions occur in mitosis (1) versus meiosis (2).",
        "قارن عدد مراحل الانقسام في المتساوي (مرحلة واحدة) والمنصف (مرحلتان).",
        "Count daughter cells, ploidy, and genetic diversity.",
        ["Mitosis has 1 division producing 2 genetically identical diploid cells for growth and repair.",
         "Meiosis has 2 divisions with crossing-over, yielding 4 genetically distinct haploid gametes."],
        "Gametes must be haploid (n) so fertilization restores 2n.",
        "نقارن عدد الخلايا الناتجة والعدد الكروموسومي والتنوع الوراثي.",
        ["المتساوي ينقسم مرة واحدة لينتج خليتين ثنائيتين متطابقتين للنمو وتعويض الأنسجة.",
         "المنصف ينقسم مرتين مع حدوث العبور لينتج 4 أمشاج أحادية مختلفة وراثياً."],
        "الأمشاج أحادية (n) ليعود العدد الثنائي (2n) عند الإخصاب.",
        diagram_en=_svg_cell_division("meiosis", 8, "en"),
        diagram_ar=_svg_cell_division("meiosis", 8, "ar"),
    ))

    # 3 (Easy): Plant cell organelle via svg_cell_diagram
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        "In the labeled plant cell diagram, which structure captures sunlight energy to synthesize glucose during photosynthesis?",
        "في رسم الخلية النباتية الموضح، أي تركيب يمتص طاقة ضوء الشمس لبناء الجلوكوز أثناء البناء الضوئي؟",
        [
            ("Chloroplast", "البلاستيدة الخضراء"),
            ("Cell Wall", "الجدار الخلوي"),
            ("Vacuole", "الفجوة العصارية"),
            ("Nucleus", "النواة"),
        ],
        "Look for the green photosynthetic organelle highlighted in red.",
        "ابحث عن العضية الخضراء المسؤولة عن البناء الضوئي والمحددة باللون الأحمر.",
        "Match each plant cell organelle to its primary function.",
        ["The chloroplast contains chlorophyll and converts light energy into chemical energy (glucose).",
         "The cell wall gives structural support, the vacuole stores water, and the nucleus houses DNA."],
        "Only plant and algal cells perform photosynthesis in chloroplasts.",
        "نربط كل عضية في الخلية النباتية بوظيفتها الأساسية.",
        ["البلاستيدة الخضراء تحتوي على الكلوروفيل وتحوّل الطاقة الضوئية إلى جلوكوز.",
         "الجدار الخلوي للدعم، والفجوة لتخزين الماء، والنواة لحفظ المادة الوراثية."],
        "البلاستيدات الخضراء خاصة بعملية البناء الضوئي.",
        diagram_en=svg_cell_diagram("plant", "Chloroplast", "Plant Cell Organelles"),
        diagram_ar=_ar_svg(svg_cell_diagram("plant", "Chloroplast", "Plant Cell Organelles"),
                           {"Plant Cell Organelles": "عضيات الخلية النباتية"}),
    ))

    # 4 (Easy): Animal cell nucleus via svg_cell_diagram
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "Before an animal cell begins mitosis or meiosis, in which organelle shown in the diagram must chromosomes replicate?",
        "قبل أن تبدأ الخلية الحيوانية الانقسام المتساوي أو المنصف، في أي عضية موضحة بالرسم يتضاعف الحمض النووي والكروموسومات؟",
        [
            ("Nucleus", "النواة"),
            ("Mitochondria", "الميتوكوندريا"),
            ("Cytoplasm", "السيتوبلازم"),
            ("Membrane", "الغشاء البلازمي"),
        ],
        "Identify the organelle that stores the cell's main chromosomal DNA.",
        "حدّد العضية التي تحتوي على الكروموسومات والمادة الوراثية الرئيسية.",
        "DNA replication occurs inside the nuclear envelope during S phase of interphase.",
        ["Chromosomes reside inside the nucleus, where S-phase DNA replication doubles each chromosome into sister chromatids.",
         "Mitochondria generate ATP, cytoplasm holds organelles, and the membrane regulates transport."],
        "Without nuclear DNA replication first, daughter cells would lack full chromosomes.",
        "يحدث تضاعف الكروموسومات داخل النواة في الطور البيني.",
        ["توجد الكروموسومات داخل النواة حيث يتضاعف الحمض النووي قبل الانقسام.",
         "الميتوكوندريا لإنتاج الطاقة، والسيتوبلازم والغشاء لأدوار أخرى."],
        "تضاعف المادة الوراثية في النواة ضروري لتوزيع نسخة كاملة لكل خلية.",
        diagram_en=svg_cell_diagram("animal", "Nucleus", "Animal Cell Organelles"),
        diagram_ar=_ar_svg(svg_cell_diagram("animal", "Nucleus", "Animal Cell Organelles"),
                           {"Animal Cell Organelles": "عضيات الخلية الحيوانية"}),
    ))

    # 5 (Medium): Maize fertilization restoration
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        f"A corn (maize) pollen grain is haploid with {m('n = 10')} chromosomes. After it fertilizes an egg cell, how many chromosomes will the resulting zygote and future root cells contain?",
        f"تحتوي حبة لقاح نبات الذرة على عدد أحادي مقداره {m('n = 10')} كروموسومات. بعد تلقيح البويضة وتكوين اللاقحة، كم كروموسوماً سيكون في خلايا الجذر الناتجة عن انقسامها المتساوي؟",
        20, [10, 30, 40],
        "Fertilization fuses two haploid gametes (n + n = 2n), and root cells grow by mitosis.",
        "يجمع الإخصاب مشيجين أحاديين (n + n = 2n)، وتنمو خلايا الجذر بالانقسام المتساوي.",
        f"Compute {m('2n = n + n')}.",
        [f"Each haploid gamete (pollen and egg) contributes {m('10')} chromosomes.",
         f"Fertilization restores the diploid count {m('2n = 10 + 10 = 20')}, which mitosis preserves in root cells."],
        f"Root cells are diploid ({m('20')}), double the gamete count ({m('10')}).",
        "نجمع كروموسومات المشيجين ثم نطبق ثبات الانقسام المتساوي.",
        [f"يسهم كل من حبة اللقاح والبويضة بـ {m('10')} كروموسومات.",
         f"تصبح اللاقحة ثنائية المجموعة {m('2n = 20')} ويحافظ الانقسام المتساوي على {m('20')} في الجذر."],
        f"خلايا الجذر ثنائية ({m('20')}) أي ضعف حبة اللقاح.",
        diagram_en=_svg_cell_division("meiosis", 20, "en"),
        diagram_ar=_svg_cell_division("meiosis", 20, "ar"),
    ))

    # 6 (Medium): Exponential cell count after 4 mitotic divisions
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        f"Starting from a single fertilized diploid zygote, how many total cells exist after {m('4')} consecutive rounds of normal mitotic cell division?",
        f"بدءاً من لاقحة واحدة ثنائية المجموعة، كم يصبح العدد الإجمالي للخلايا بعد {m('4')} دورات متتالية من الانقسام المتساوي؟",
        16, [8, 12, 32],
        "Each round of mitosis doubles the number of cells.",
        "كل دورة انقسام متساوي تضاعف عدد الخلايا.",
        f"Apply {m('2^k')} for {m('k = 4')} divisions.",
        [f"Round 1: {m('2')}; Round 2: {m('4')}; Round 3: {m('8')}; Round 4: {m('16')} cells.",
         f"Using the formula {m('2^4 = 16')} cells."],
        f"Every division multiplies count by {m('2')}: {m('1 \\to 2 \\to 4 \\to 8 \\to 16')}.",
        "نستخدم العلاقة الأسية 2 أس عدد الانقسامات.",
        [f"الدورة 1: {m('2')}؛ الدورة 2: {m('4')}؛ الدورة 3: {m('8')}؛ الدورة 4: {m('16')} خلية.",
         f"أي {m('2^4 = 16')} خلية."],
        f"المضاعفة أربع مرات تعطي {m('16')}.",
    ))

    # 7 (Medium): Sister chromatids in G2 vs chromosomes in gamete
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        f"A somatic body cell of a dog has {m('2n = 78')} chromosomes. Immediately after DNA replication (G2 phase, just before division), how many sister chromatids are inside that single cell?",
        f"تحتوي الخلية الجسمية للكلب على {m('2n = 78')} كروموسوماً. مباشرةً بعد تضاعف الحمض النووي في الطور البيني (G2) وقبل الانقسام، كم كروماتيداً شقيقاً يوجد داخل الخلية الواحدة؟",
        156, [78, 39, 312],
        "After S phase, each of the 78 chromosomes consists of 2 joined sister chromatids.",
        "بعد تضاعف DNA يصبح كل كروموسوم مكوناً من كروماتيدين شقيقين.",
        f"Multiply {m('78')} chromosomes by {m('2')} chromatids each.",
        [f"Before replication there are {m('78')} single-chromatid chromosomes.",
         f"After replication, all {m('78')} chromosomes duplicate, producing {m('78 \\times 2 = 156')} sister chromatids."],
        f"Dividing {m('156')} equally into 2 daughter cells gives {m('78')} each.",
        "نضرب عدد الكروموسومات الثنائي في 2.",
        [f"قبل التضاعف يوجد {m('78')} كروموسوماً مفرداً.",
         f"بعد التضاعف يتكون كل كروموسوم من كروماتيدين، فيكون المجموع {m('78 \\times 2 = 156')} كروماتيداً شقيقاً."],
        f"تتوزع الـ {m('156')} بالتساوي إلى {m('78')} في كل خلية بنوية.",
    ))

    # 8 (Medium): Total gametes from 6 primary germ cells
    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        f"If {m('6')} primary diploid germ cells each complete normal meiosis, how many total haploid gametes are formed?",
        f"إذا أكملت {m('6')} خلايا جرثومية ثنائية المجموعة الانقسام المنصف كاملاً، فكم مشيجاً أحادياً سينتج في المجموع؟",
        24, [12, 18, 48],
        "Each single diploid cell entering meiosis yields 4 haploid daughter cells.",
        "كل خلية أصلية تدخل الانقسام المنصف تعطي 4 خلايا أحادية المجموعة.",
        f"Multiply {m('6')} parent cells by {m('4')} gametes per meiosis.",
        [f"One round of meiosis produces {m('4')} haploid cells.",
         f"For {m('6')} initial cells: {m('6 \\times 4 = 24')} haploid gametes."],
        f"Notice mitosis would give {m('6 \\times 2 = 12')}, whereas meiosis gives {m('24')}.",
        "نضرب عدد الخلايا الأم في 4.",
        [f"الخلية الواحدة تعطي {m('4')} أمشاج في الانقسام المنصف.",
         f"إذن {m('6 \\times 4 = 24')} مشيجاً أحادياً."],
        f"الانقسام المتساوي ينتج {m('12')} بينما المنصف ينتج {m('24')}.",
        diagram_en=_svg_cell_division("meiosis", 16, "en"),
        diagram_ar=_svg_cell_division("meiosis", 16, "ar"),
    ))

    # 9 (Medium): Starting with 3 cells doing 4 mitotic divisions
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        f"A tissue culture starts with {m('3')} onion root cells ({m('2n = 16')}). If every cell completes {m('4')} successive mitotic divisions, how many total cells are present?",
        f"بدأت مزرعة أنسجة بعدد {m('3')} خلايا من جذر البصل ({m('2n = 16')}). إذا أكملت جميع الخلايا {m('4')} انقسامات متساوية متتالية، فكم يصبح العدد الكلي للخلايا؟",
        48, [16, 24, 96],
        "Each initial cell multiplies into 2^4 cells independently.",
        "تتضاعف كل خلية ابتدائية إلى 2 أس 4 خلايا.",
        f"Evaluate {m('3 \\times 2^4')}.",
        [f"After {m('4')} divisions, each starting cell produces {m('2^4 = 16')} cells.",
         f"Multiplying by {m('3')} starting cells gives {m('3 \\times 16 = 48')} total cells."],
        f"Sequence: {m('3 \\to 6 \\to 12 \\to 24 \\to 48')}.",
        "نضرب العدد الابتدائي في 2 أس عدد الانقسامات.",
        [f"كل خلية واحدة تنتج {m('2^4 = 16')} خلية.",
         f"إذن المجموع الكلي {m('3 \\times 16 = 48')} خلية."],
        f"التسلسل: {m('3 \\to 6 \\to 12 \\to 24 \\to 48')}.",
    ))

    # 10 (Hard): Nondisjunction in human meiosis -> trisomy zygote
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        f"During human meiosis ({m('2n = 46')}), one homologous chromosome pair fails to separate (nondisjunction) in Meiosis I. If an egg receiving the extra chromosome is fertilized by a normal sperm, how many chromosomes will the resulting zygote have?",
        f"أثناء الانقسام المنصف في الإنسان ({m('2n = 46')})، فشل زوج من الكروموسومات المتماثلة في الانفصال في المرحلة الأولى. إذا خُصّبت بويضة حصلت على الكروموسوم الزائد بحيوان منوي سليم، فكم كروموسوماً سيكون في اللاقحة الناتجة؟",
        47, [45, 46, 48],
        "Nondisjunction creates an (n + 1) gamete that fuses with a normal (n) gamete.",
        "ينتج عن عدم الانفصال مشيج يحمل (n + 1) ثم يندمج مع مشيج سليم يحمل (n).",
        f"Add {m('(n + 1)')} from the egg and {m('n')} from the sperm.",
        [f"A normal human gamete has {m('n = 23')} chromosomes.",
         f"The nondisjunction egg carries {m('23 + 1 = 24')} chromosomes.",
         f"Combining with a normal {m('23')}-chromosome sperm gives {m('24 + 23 = 47')} chromosomes (trisomy)."],
        f"Normal {m('46')} plus {m('1')} extra chromosome equals {m('47')}.",
        "نجمع عدد الكروموسومات في البويضة الشاذة والحيوان المنوي السليم.",
        [f"المشيج السليم يحمل {m('n = 23')} كروموسوماً.",
         f"البويضة بعد عدم الانفصال تحمل {m('23 + 1 = 24')} كروموسوماً.",
         f"بعد الإخصاب مع {m('23')} يصبح المجموع {m('24 + 23 = 47')} كروموسوماً."],
        f"العدد الطبيعي {m('46')} مضافاً إليه كروموسوم واحد زائد يساوي {m('47')}.",
    ))

    # 11 (Hard): Sequential mitosis then meiosis total gametes
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        f"A single diploid germ cell ({m('2n = 24')}) first undergoes {m('3')} rounds of mitosis, and then every resulting diploid cell completes meiosis. How many total haploid gametes are produced?",
        f"خلية جرثومية واحدة ({m('2n = 24')}) تنقسم أولاً {m('3')} انقسامات متساوية، ثم تدخل جميع الخلايا الناتجة الانقسام المنصف كاملاً. كم مشيجاً أحادياً سينتج في النهاية؟",
        32, [16, 24, 64],
        "Find the number of diploid cells after 3 mitoses, then multiply by 4 gametes per meiosis.",
        "احسب عدد الخلايا بعد 3 انقسامات متساوية ثم اضرب في 4 أمشاج لكل خلية.",
        f"Compute {m('2^3 \\times 4')}.",
        [f"Three mitotic divisions produce {m('2^3 = 8')} diploid cells ({m('2n = 24')}).",
         f"Each of those {m('8')} cells produces {m('4')} haploid gametes ({m('n = 12')}) via meiosis: {m('8 \\times 4 = 32')} gametes."],
        f"Each gamete still contains {m('12')} chromosomes regardless of how many mitoses preceded meiosis.",
        "نحسب الخلايا الثنائية أولاً ثم نضرب في ناتج المنصف.",
        [f"بعد {m('3')} انقسامات متساوية نحصل على {m('2^3 = 8')} خلايا ثنائية.",
         f"كل خلية منها تعطي {m('4')} أمشاج، فيكون المجموع {m('8 \\times 4 = 32')} مشيجاً."],
        f"يبقى عدد الكروموسومات في كل مشيج {m('12')}.",
        diagram_en=_svg_cell_division("meiosis", 24, "en"),
        diagram_ar=_svg_cell_division("meiosis", 24, "ar"),
    ))

    # 12 (Hard): Why siblings vary while clonal cuttings are identical
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        "Two olive trees grown from stem cuttings of the same parent tree are genetically identical, whereas two sibling lambs from the same parents differ genetically. Which pair of processes explains this contrast?",
        "شجرتا زيتون زُرعتا من عقل ساقية للأم نفسها متطابقتان وراثياً، بينما يختلف حملان شقيقان من الأبوين نفسيهما وراثياً. ما العمليتان اللتان تفسران هذا التباين؟",
        [
            ("Cuttings grow via mitosis only; sibling lambs arise from meiosis (crossing-over and independent assortment) plus fertilization",
             "تنمو العقل بالانقسام المتساوي فقط، بينما ينتج الحملان عن الانقسام المنصف (العبور والتوزيع الحر) ثم الإخصاب"),
            ("Cuttings undergo meiosis in root tips; lambs undergo only mitosis in germ cells",
             "تخضع العقل للانقسام المنصف في الجذور، بينما تخضع الحملان للمتساوي في الأمشاج"),
            ("Mitosis shuffles maternal and paternal alleles randomly during every division",
             "يخلط الانقسام المتساوي أليلات الأب والأم عشوائياً في كل انقسام"),
            ("Animal cells lack DNA replication before division, whereas plant cells replicate twice",
             "خلايا الحيوان لا تضاعف الحمض النووي قبل الانقسام بخلاف النبات"),
        ],
        "Distinguish vegetative (asexual) mitosis from sexual meiosis + random fertilization.",
        "ميّز بين التكاثر الخضري بالانقسام المتساوي والتكاثر الجنسي بالانقسام المنصف والإخصاب.",
        "Trace genetic variation sources in sexual vs asexual reproduction.",
        ["Stem cuttings divide strictly by mitosis, copying the parent genome identically.",
         "Sexual reproduction generates new allele combinations through crossing-over in prophase I, independent assortment in metaphase I, and random gamete fusion."],
        "Clonal propagation produces uniform crops; meiosis drives genetic diversity.",
        "نتتبع مصدر التطابق الوراثي مقابل التنوع الوراثي.",
        ["العقلة الساقية تتكاثر بالانقسام المتساوي فتنقل الجينوم نفسه دون تغيير.",
         "في التكاثر الجنسي يحدث العبور الوراثي والتوزيع الحر أثناء المنصف ثم الإخصاب العشوائي."],
        "الاستنساخ الخضري يحفظ الصفات، بينما المنصف يولّد تنوعاً وراثياً.",
    ))

    # 13 (Hard): Meiosis II nondisjunction in rice (2n = 24)
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        f"In a rice cell ({m('2n = 24')}), Meiosis I proceeds normally, but sister chromatids of one chromosome fail to separate during Meiosis II in one of the two secondary cells. What are the chromosome counts of the {m('4')} resulting gametes?",
        f"في خلية أرز ({m('2n = 24')})، سار الانقسام المنصف الأول بشكل طبيعي، لكن الكروماتيدين الشقيقين لكروموسوم واحد فشلا في الانفصال خلال المنصف الثاني في إحدى الخليتين الثانويتين. ما أعداد الكروموسومات في الأمشاج الأربعة الناتجة؟",
        [
            ("12, 12, 13, 11", "12، 12، 13، 11"),
            ("13, 13, 11, 11", "13، 13، 11، 11"),
            ("24, 24, 0, 0", "24، 24، 0، 0"),
            ("12, 12, 12, 12", "12، 12، 12، 12"),
        ],
        "One secondary cell divides normally (n, n), while the affected cell splits unevenly (n+1, n-1).",
        "إحدى الخليتين الثانويتين تنقسم طبيعياً (n و n)، والأخرى تنقسم بشكل غير متساوٍ (n+1 و n-1).",
        f"Use {m('n = 12')} for rice.",
        [f"Meiosis I normally yields two cells each with {m('12')} duplicated chromosomes.",
         f"The unaffected secondary cell yields two normal gametes: {m('12, 12')}.",
         f"The cell with Meiosis II nondisjunction gives both sister chromatids of one chromosome to one gamete ({m('13')}) and none to the other ({m('11')})."],
        "Notice 12 + 12 + 13 + 11 = 48 total chromatids conserved.",
        f"نطبق {m('n = 12')} على الخليتين الثانويتين.",
        [f"المنصف الأول ينتج خليتين في كل منهما {m('12')} كروموسوماً متضاعفاً.",
         f"الخلية السليمة تعطي مشيجين طبيعيين ({m('12, 12')}).",
         f"الخلية التي حدث فيها عدم انفصال تعطي ({m('13')}) و({m('11')})."],
        "المجموع الكلي للكروماتيدات محفوظ (12+12+13+11 = 48).",
    ))

    # 14 (Hard): Why triploid (3n = 33) seedless watermelon is sterile
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        f"Seedless watermelons are triploid ({m('3n = 33')}) rather than normal diploid ({m('2n = 22')}). Why are triploid plants unable to produce fertile seeds through normal meiosis?",
        f"البطيخ عديم البذور ثلاثي المجموعة الكروموسومية ({m('3n = 33')}) بدلاً من ثنائي المجموعة ({m('2n = 22')}). لماذا يعجز النبات ثلاثي المجموعة عن تكوين بذور خصبة عبر الانقسام المنصف الطبيعي؟",
        [
            ("An odd number (3) of chromosome sets cannot pair evenly as homologous pairs in Meiosis I, producing unbalanced gametes",
             "المجموعات الثلاث الفردية لا تستطيع الازدواج بالتساوي في المنصف الأول فتنتج أمشاج غير متوازنة"),
            ("Triploid cells lack nuclei and therefore cannot undergo DNA replication",
             "الخلايا ثلاثية المجموعة تفتقر إلى النواة فلا يتضاعف فيها الحمض النووي"),
            ("Triploid watermelons cannot perform mitosis in their leaves or stems",
             "لا تستطيع النباتات ثلاثية المجموعة إجراء الانقسام المتساوي في أوراقها"),
            ("33 chromosomes divide evenly by 2 to form viable gametes with 16.5 chromosomes",
             "ينقسم العدد 33 على 2 بالتساوي لينتج أمشاجاً سليمة تحوي 16.5 كروموسوماً"),
        ],
        "Meiosis requires homologous chromosomes to form pairs (synapsis) before separating.",
        "يتطلب الانقسام المنصف اصطفاف الكروموسومات المتماثلة في أزواج قبل انفصالها.",
        "Check whether 3 homologous copies per chromosome type can split equally into two poles.",
        ["With 3 homologous copies of each of the 11 chromosome types, chromosomes form uneven trivalents in Meiosis I.",
         "Random 2-versus-1 segregation across 11 sets makes balanced n or 2n gametes nearly impossible, rendering the plant sterile."],
        "Mitosis works fine in triploid tissue (so the fruit grows normally), only meiosis fails.",
        "نفحص إمكانية تقسيم ثلاث نسخ متماثلة بالتساوي بين خليتين.",
        ["وجود 3 نسخ لكل نوع كروموسومي يمنع التزاوج الثنائي المنتظم في المنصف الأول.",
         "تتوزع الكروموسومات بشكل غير متوازن (2 مقابل 1) فتفشل الأمشاج وتنعدم البذور."],
        "ينجح الانقسام المتساوي وتنمو الثمرة، ويفشل الانقسام المنصف فقط.",
    ))
    return qs


def _gen_sci_b02(start_idx: int) -> list[dict]:
    """G9-SCI-B02: DNA complementary base pairing (A=T, G=C) & Mendelian Punnett squares."""
    bp = "G9-SCI-B02"
    qs: list[dict] = []

    # 0 (Easy): DNA complementary strand
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        f"A template strand of DNA has the base sequence {m(r"\text{5'-A T G C C A T-3'}")}. What is the complementary DNA strand sequence from {m("3'")} to {m("5'")}?",
        f"إذا كان تسلسل القواعد النيتروجينية في أحد شريطي DNA هو {m(r"\text{5'-A T G C C A T-3'}")}، فما تسلسل الشريط المكمل من {m("3'")} إلى {m("5'")}؟",
        [
            (m(r"\text{3'-T A C G G T A-5'}"), m(r"\text{3'-T A C G G T A-5'}")),
            (m(r"\text{3'-U A C G G U A-5'}"), m(r"\text{3'-U A C G G U A-5'}")),
            (m(r"\text{3'-A T G C C A T-5'}"), m(r"\text{3'-A T G C C A T-5'}")),
            (m(r"\text{3'-C G T A A C G-5'}"), m(r"\text{3'-C G T A A C G-5'}")),
        ],
        "In DNA, Adenine (A) pairs with Thymine (T) and Guanine (G) pairs with Cytosine (C).",
        "في جزيء DNA يرتبط الأدينين (A) بالثايمين (T)، ويرتبط الجوانين (G) بالسايتوسين (C).",
        "Translate each base one-by-one: A↔T, G↔C.",
        ["A→T, T→A, G→C, C→G, C→G, A→T, T→A.",
         "Reading straight across gives 3'-T A C G G T A-5' (Uracil U belongs to RNA, not DNA)."],
        "Every A-T and G-C pair matches across both strands.",
        "نطبّق قاعدة تكامل القواعد: A مع T، و G مع C.",
        ["التحويل قاعدة بقاعدة: A←T، T←A، G←C، C←G، C←G، A←T، T←A.",
         "ينتج الشريط المكمل 3'-T A C G G T A-5' (القاعدة U توجد في RNA لا DNA)."],
        "عدد الأزواج المتقابلة متطابق على طول الشريطين.",
    ))

    # 1 (Easy): Chargaff %G from %A = 22%
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        f"In a double-stranded DNA molecule, Adenine (A) makes up {m(r"22\%")} of all nitrogenous bases. What percentage of the bases is Guanine (G)?",
        f"في جزيء DNA مزدوج الشريطين، تشكّل قاعدة الأدينين (A) نسبة {m(r"22\%")} من مجموع القواعد. ما النسبة المئوية لقاعدة الجوانين (G)؟",
        28, [22, 56, 78],
        "By Chargaff's rules, %A = %T and %G = %C, with %A + %T + %G + %C = 100%.",
        "وفق قاعدة تشارجاف: نسبة A تساوي T، ونسبة G تساوي C، والمجموع 100%.",
        f"Use {m(r"\%A + \%G = 50\%")}.",
        [f"Since {m('A = T')}, Thymine is also {m(r'22\%')}, so {m(r'A + T = 44\%')}.",
         f"Remaining {m(r'100\% - 44\% = 56\%')} is split equally between G and C: {m(r'56\% \div 2 = 28\%')}."],
        f"Check sum: {m(r'22\% + 22\% + 28\% + 28\% = 100\%')}.",
        "نستخدم العلاقة المختصرة: نسبة A + نسبة G = 50%.",
        [f"بما أن {m('A = T')} فإن الثايمين {m(r'22\%')}، ومجموعهما {m(r'44\%')}.",
         f"يتبقى {m(r'56\%')} لـ G و C بالتساوي، أي أن {m(r'G = 28\%')}."],
        f"المجموع: {m('22 + 22 + 28 + 28 = 100')}.",
        suffix=r"\%",
    ))

    # 2 (Easy): Punnett square Tt x Tt -> %tt
    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        f"In pea plants, tall stem ({m('T')}) is dominant over dwarf stem ({m('t')}). Based on the Punnett square for {m(r'\text{Tt} \times \text{Tt}')}, what percentage of offspring will have a dwarf stem ({m('tt')})?",
        f"في نبات البازلاء تسود صفة الساق الطويلة ({m('T')}) على القصيرة ({m('t')}). اعتماداً على مربع بانيت للتزاوج {m(r'\text{Tt} \times \text{Tt}')}، ما النسبة المئوية للأفراد الناتجة ذات الساق القصيرة ({m('tt')})؟",
        25, [50, 75, 100],
        "Count how many of the 4 Punnett boxes contain two lowercase alleles (tt).",
        "احسب عدد المربعات الأربعة التي تحتوي على جينين متنحيين (tt).",
        "One box out of 4 equals 25%.",
        ["The 4 boxes are TT, Tt, Tt, and tt.",
         f"Only {m('1')} out of {m('4')} boxes is homozygous recessive {m('tt')}, which is {m(r'25\%')}."],
        f"Phenotype ratio is {m('3')} tall ({m(r'75\%')}) to {m('1')} dwarf ({m(r'25\%')}).",
        "نعدّ المربعات التي تظهر فيها الصفة المتنحية فقط.",
        ["الأفراد الأربعة في المربع هي TT و Tt و Tt و tt.",
         f"يظهر الطراز {m('tt')} في مربع واحد فقط من 4، أي بنسبة {m(r'25\%')}."],
        f"النسبة المظهرية {m('3')} طويل ({m(r'75\%')}) إلى {m('1')} قصير ({m(r'25\%')}).",
        suffix=r"\%",
        diagram_en=svg_punnett_square("Tt", "Tt", ["TT", "Tt", "Tt", "tt"], "Punnett Square: Tt x Tt"),
        diagram_ar=_ar_svg(svg_punnett_square("Tt", "Tt", ["TT", "Tt", "Tt", "tt"], "Punnett Square: Tt x Tt"),
                           {"Punnett Square: Tt x Tt": "مربع بانيت: Tt × Tt"}),
    ))

    # 3 (Easy): Punnett square Bb x bb -> %dominant
    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        f"Black wool ({m('B')}) is dominant over white wool ({m('b')}) in sheep. According to the Punnett square for {m(r'\text{Bb} \times \text{bb}')}, what percentage of lambs are expected to have black wool?",
        f"يسود الصوف الأسود ({m('B')}) على الصوف الأبيض ({m('b')}) في الأغنام. وفق مربع بانيت للتزاوج {m(r'\text{Bb} \times \text{bb}')}، ما النسبة المئوية المتوقعة للحملان ذات الصوف الأسود؟",
        50, [25, 75, 0],
        "Any lamb carrying at least one dominant allele (B) shows black wool.",
        "أي فرد يحمل أليلاً سائداً واحداً على الأقل (B) يظهر الصفة السائدة.",
        "Count boxes with at least one B out of 4.",
        ["The 4 offspring boxes are Bb, Bb, bb, and bb.",
         f"{m('2')} out of {m('4')} boxes are {m('Bb')} (black wool), giving {m(r'50\%')}."],
        "A heterozygous × homozygous recessive testcross always yields a 1:1 (50%:50%) ratio.",
        "نعدّ المربعات المحتوية على الحرف الكبير B.",
        ["النتائج الأربعة هي Bb و Bb و bb و bb.",
         f"يوجد مربعان يحملان {m('B')} من أصل 4، أي بنسبة {m(r'50\%')}."],
        "التزاوج الاختباري يعطي دائماً نسبة 1:1 (50%).",
        suffix=r"\%",
        diagram_en=svg_punnett_square("Bb", "bb", ["Bb", "Bb", "bb", "bb"], "Punnett Square: Bb x bb"),
        diagram_ar=_ar_svg(svg_punnett_square("Bb", "bb", ["Bb", "Bb", "bb", "bb"], "Punnett Square: Bb x bb"),
                           {"Punnett Square: Bb x bb": "مربع بانيت: Bb × bb"}),
    ))

    # 4 (Easy): DNA backbone & bond structure
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "Which pair of molecules alternates along the two outer rails (backbone) of a DNA double helix?",
        "أي زوج من الجزيئات يتعاقب لتكوين العمود الفقري (الجانبين الخارجيين) لسلم جزيء DNA الحلزوني المزدوج؟",
        [
            ("Deoxyribose sugar and phosphate groups", "سكر منقوص الأكسجين ومجموعات الفوسفات"),
            ("Adenine and thymine bases only", "قواعد الأدينين والثايمين فقط"),
            ("Amino acids and fatty acid chains", "الأحماض الأمينية وسلاسل الأحماض الدهنية"),
            ("Ribose sugar and uracil bases", "سكر الريبوز وقواعد اليوراسيل"),
        ],
        "Picture DNA as a twisted ladder: what makes the side rails versus the rungs?",
        "تخيّل DNA كسلم ملتف: ممَّ يتكون جانبا السلم مقابل درجاته؟",
        "Separate backbone components from central base-pair rungs.",
        ["Nucleotides link via covalent bonds between deoxyribose sugar and phosphate groups to form the side rails.",
         "Nitrogenous bases (A-T and G-C) project inward to form the hydrogen-bonded rungs."],
        "Ribose and uracil belong to RNA rather than DNA.",
        "نميز بين جانبي السلم ودرجاته الوسطى.",
        ["ترتبط النيوكليوتيدات بروابط تساهمية بين سكر الديوكسي ريبوز والفوسفات لتكوين الجانبين.",
         "أما القواعد النيتروجينية (A-T و G-C) فتشكّل درجات السلم الوسطى."],
        "سكر الريبوز واليوراسيل خاصان بـ RNA.",
    ))

    # 5 (Medium): Base count from 400 total bases with 110 C
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        f"A double-stranded DNA fragment contains {m('400')} total nitrogenous bases, of which {m('110')} are Cytosine (C). How many Adenine (A) bases are in this fragment?",
        f"يحتوي جزء من جزيء DNA المزدوج على {m('400')} قاعدة نيتروجينية إجمالاً، منها {m('110')} قاعدة سايتوسين (C). كم قاعدة أدينين (A) توجد في هذا الجزء؟",
        90, [110, 180, 290],
        "First find Guanine (G = C), subtract C + G from 400, then split the rest equally between A and T.",
        "أوجد أولاً عدد الجوانين (G = C)، ثم اطرح مجموعهما من 400، واقسم الباقي بالتساوي بين A و T.",
        f"Apply {m('A + T + G + C = 400')} with {m('G = C = 110')}.",
        [f"Because {m('G = C')}, there are {m('110')} Guanines, so {m('G + C = 220')}.",
         f"Remaining bases: {m('A + T = 400 - 220 = 180')}. Since {m('A = T')}, {m('A = 180 \\div 2 = 90')}."],
        f"Check: {m('90 + 90 + 110 + 110 = 400')}.",
        "نطبق تساوي الأزواج المتكاملة على العدد الكلي.",
        [f"بما أن {m('G = C = 110')} فإن مجموعهما {m('220')} قاعدة.",
         f"يتبقى {m('400 - 220 = 180')} تتوزع بالتساوي على A و T، أي {m('A = 90')}."],
        f"التحقق: {m('90 + 90 + 110 + 110 = 400')}.",
    ))

    # 6 (Medium): Expected dominant offspring out of 240
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        f"Round seeds ({m('R')}) are dominant over wrinkled seeds ({m('r')}). If two heterozygous plants ({m(r'\text{Rr} \times \text{Rr}')}) produce {m('240')} total offspring seeds, how many are expected to be <strong>round</strong>?",
        f"تسود البذور الملساء ({m('R')}) على المجعدة ({m('r')}). إذا أنتج تزاوج نباتين هجينين ({m(r'\text{Rr} \times \text{Rr}')}) عدد {m('240')} بذرة، فكم بذرة يُتوقع أن تكون <strong>ملساء</strong>؟",
        180, [60, 120, 200],
        "In a monohybrid heterozygous cross, 3 out of 4 offspring show the dominant phenotype.",
        "في التزاوج الهجين الأحادي، تظهر الصفة السائدة في 3 من كل 4 أفراد.",
        f"Multiply {m('240')} by {m(r'\frac{3}{4}')}.",
        [f"From the Punnett square, {m('RR')}, {m('Rr')}, and {m('Rr')} all express round seeds ({m(r'3/4 = 75\%')}).",
         f"Expected round seeds: {m(r'\frac{3}{4} \times 240 = 180')}."],
        f"Remaining {m('240 - 180 = 60')} seeds are wrinkled ({m('rr')}).",
        "نضرب العدد الكلي في احتمال الصفة السائدة (3/4).",
        [f"من مربع بانيت تظهر الصفة السائدة في 3 مربعات من 4 ({m(r'75\%')}).",
         f"العدد المتوقع = {m(r'\frac{3}{4} \times 240 = 180')} بذرة ملساء."],
        f"البقية {m('60')} بذرة مجعدة ({m('rr')}).",
        diagram_en=svg_punnett_square("Rr", "Rr", ["RR", "Rr", "Rr", "rr"], "Punnett Square: Rr x Rr"),
        diagram_ar=_ar_svg(svg_punnett_square("Rr", "Rr", ["RR", "Rr", "Rr", "rr"], "Punnett Square: Rr x Rr"),
                           {"Punnett Square: Rr x Rr": "مربع بانيت: Rr × Rr"}),
    ))

    # 7 (Medium): Gg x gg out of 160 seedlings -> heterozygous count
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        f"In a genetic cross between {m('Gg')} (green pod) and {m('gg')} (yellow pod), {m('160')} seedlings grow. How many seedlings are expected to be heterozygous ({m('Gg')})?",
        f"في تزاوج بين نبات قرونه خضراء هجين ({m('Gg')}) وآخر قرونه صفراء ({m('gg')})، نمت {m('160')} شتلة. كم شتلة يُتوقع أن تكون متغايرة الجينات ({m('Gg')})؟",
        80, [40, 120, 160],
        "Half of the Punnett square boxes in Gg × gg are Gg.",
        "نصف مربعات بانيت في التزاوج Gg × gg تحمل الطراز Gg.",
        f"Multiply {m('160')} by {m(r'\frac{1}{2}')}.",
        [f"Crossing {m('Gg')} (gametes G, g) with {m('gg')} (gametes g, g) yields {m('2')} {m('Gg')} and {m('2')} {m('gg')} boxes.",
         f"Expected {m('Gg')} count: {m(r'\frac{1}{2} \times 160 = 80')} seedlings."],
        f"{m('80')} green ({m('Gg')}) and {m('80')} yellow ({m('gg')}).",
        "نضرب العدد الكلي في نسبة 50%.",
        [f"التزاوج يعطي مربعين {m('Gg')} ومربعين {m('gg')} من أصل 4.",
         f"العدد المتوقع لـ {m('Gg')} هو {m(r'\frac{1}{2} \times 160 = 80')} شتلة."],
        f"النتيجة 80 خضراء و80 صفراء.",
        diagram_en=svg_punnett_square("Gg", "gg", ["Gg", "Gg", "gg", "gg"], "Punnett Square: Gg x gg"),
        diagram_ar=_ar_svg(svg_punnett_square("Gg", "gg", ["Gg", "Gg", "gg", "gg"], "Punnett Square: Gg x gg"),
                           {"Punnett Square: Gg x gg": "مربع بانيت: Gg × gg"}),
    ))

    # 8 (Medium): 1200 bases with 18% G -> count of Thymine
    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        f"A {m('1,200')}-base double-stranded DNA gene contains {m(r'18\%')} Guanine (G). How many Thymine (T) bases does this gene contain?",
        f"يحتوي جين من DNA مزدوج الشريطين على {m('1,200')} قاعدة، منها {m(r'18\%')} جوانين (G). كم قاعدة ثايمين (T) توجد في هذا الجين؟",
        384, [216, 432, 768],
        "Find %T first using %G + %T = 50%, then multiply by 1,200.",
        "احسب نسبة الثايمين أولاً باستخدام %G + %T = 50%، ثم اضرب في 1,200.",
        f"Compute {m(r'\%T = 50\% - 18\% = 32\%')}, then find {m('0.32 \\times 1200')}.",
        [f"Since {m('C = G = 18\\%')}, {m('G + C = 36\\%')}, leaving {m('64\\%')} split equally between A and T ({m('32\\%')} each).",
         f"Thymine count: {m('0.32 \\times 1200 = 384')} bases."],
        f"Check: {m('384 + 384 + 216 + 216 = 1200')}.",
        "نحسب نسبة T ثم نضربها في إجمالي القواعد.",
        [f"بما أن {m('C = G = 18\\%')} فإن {m('G + C = 36\\%')}، ويتبقى {m('64\\%')} بالتساوي بين A و T أي {m('32\\%')} لـ T.",
         f"عدد قواعد الثايمين = {m('0.32 \\times 1200 = 384')} قاعدة."],
        f"التحقق: {m('384 + 384 + 216 + 216 = 1200')}.",
    ))

    # 9 (Medium): Genotype vs phenotype ratio in Tt x Tt
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        f"For the cross {m(r'\text{Tt} \times \text{Tt}')} shown in the Punnett square, why is the <strong>phenotypic</strong> ratio {m('3:1')} while the <strong>genotypic</strong> ratio is {m('1:2:1')}?",
        f"في التزاوج {m(r'\text{Tt} \times \text{Tt}')} الموضح بمربع بانيت، لماذا تكون النسبة <strong>المظهرية</strong> {m('3:1')} بينما النسبة <strong>الجينية</strong> {m('1:2:1')}؟",
        [
            ("Both homozygous dominant (TT) and heterozygous (Tt) individuals display the same dominant tall phenotype",
             "لأن كلاً من الفرد السائد النقي (TT) والهجين (Tt) يظهران الصفة السائدة نفسها (الطول)"),
            ("Heterozygous (Tt) individuals show a medium intermediate height",
             "لأن الفرد الهجين (Tt) يظهر صفة وسطية بين الطويل والقصير"),
            ("Recessive (tt) individuals convert into Tt during germination",
             "لأن الأفراد المتنحية (tt) تتحول إلى هجينة (Tt) عند الإنبات"),
            ("Only two of the four Punnett boxes represent viable embryos",
             "لأن مربعين فقط من الأربعة يمثلان أجنة قابلة للنمو"),
        ],
        "Compare the visible traits of TT and Tt under complete dominance.",
        "قارن المظهر الخارجي لكل من الطرازين الجينيين TT و Tt في السيادة التامة.",
        "Group the 1 TT + 2 Tt genotypes by phenotype.",
        ["Genotypes are 1 TT : 2 Tt : 1 tt (1:2:1).",
         "Because T is completely dominant over t, both TT and Tt appear tall (1 + 2 = 3 tall : 1 dwarf)."],
        "Incomplete dominance would give 1:2:1 for both, whereas complete dominance gives 3:1 phenotype.",
        "نجمع الطرز الجينية التي تعطي الطراز المظهري نفسه.",
        ["الطرز الجينية هي 1 TT : 2 Tt : 1 tt.",
         "في السيادة التامة يخفي الأليل T أثر t، فيظهر 3 طوال (TT و Tt) مقابل 1 قصير (tt)."],
        "في السيادة التامة تتوحد الصفة السائدة النقية والهجينة مظهرياً.",
        diagram_en=svg_punnett_square("Tt", "Tt", ["TT", "Tt", "Tt", "tt"], "Genotype vs Phenotype"),
        diagram_ar=_ar_svg(svg_punnett_square("Tt", "Tt", ["TT", "Tt", "Tt", "tt"], "Genotype vs Phenotype"),
                           {"Genotype vs Phenotype": "الطراز الجيني مقابل المظهري"}),
    ))

    # 10 (Hard): Reverse-engineering parental genotypes from 298:102
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        f"In pea plants, purple flowers ({m('P')}) are dominant over white ({m('p')}). A botanist crosses two purple-flowered plants and harvests {m('298')} purple-flowered and {m('102')} white-flowered offspring. What are the genotypes of the two parent plants?",
        f"في نبات البازلاء تسود الأزهار البنفسجية ({m('P')}) على البيضاء ({m('p')}). أجرى باحث تزاوجاً بين نباتين أزهارهما بنفسجية فحصل على {m('298')} نباتاً بنفسجي الأزهار و{m('102')} نباتاً أبيض الأزهار. ما الطراز الجيني للأبوين؟",
        [
            ("Heterozygous × Heterozygous (Pp × Pp)", "أبوان متغايرا الجينة (Pp × Pp)"),
            ("Homozygous dominant × Heterozygous (PP × Pp)", "سائد نقي × متغاير الجينة (PP × Pp)"),
            ("Homozygous dominant × Homozygous recessive (PP × pp)", "سائد نقي × متنحي نقي (PP × pp)"),
            ("Heterozygous × Homozygous recessive (Pp × pp)", "متغاير الجينة × متنحي نقي (Pp × pp)"),
        ],
        "Notice 298 : 102 is very close to 3 : 1, and both parents are purple.",
        "لاحظ أن النسبة 298 : 102 قريبة جداً من 3 : 1، وكلا الأبوين أزهاره بنفسجية.",
        "Check which parental genotypes can both look purple AND yield white (pp) offspring in a ~3:1 ratio.",
        ["White offspring (pp) require each parent to donate a recessive p allele, ruling out any PP parent.",
         "Both parents have purple flowers, so neither can be pp; thus both must be Pp, which matches the observed ~3:1 ratio (298:102 ≈ 3:1)."],
        "A Pp × Pp cross predicts 300 purple : 100 white out of 400 plants.",
        "نبحث عن أبوين مظهرهما بنفسجي وينتجان نسبة 3:1.",
        ["ظهور نباتات بيضاء (pp) يعني أن كل أب يحمل أليلاً متنحياً p، وهذا يستبعد وجود PP.",
         "وبما أن الأبوين بنفسجيان فلا يمكن أن يكون أي منهما pp، إذن كلاهما Pp."],
        "التزاوج Pp × Pp يتوقع 300 بنفسجي إلى 100 أبيض من 400.",
        diagram_en=svg_punnett_square("Pp", "Pp", ["PP", "Pp", "Pp", "pp"], "Reverse Cross: ~3:1"),
        diagram_ar=_ar_svg(svg_punnett_square("Pp", "Pp", ["PP", "Pp", "Pp", "pp"], "Reverse Cross: ~3:1"),
                           {"Reverse Cross: ~3:1": "تزاوج عكسي: نسبة ~3:1"}),
    ))

    # 11 (Hard): Conditional carrier probability (2/3)
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        f"Two healthy carrier parents ({m(r'\text{Aa} \times \text{Aa}')}) have a child who does <strong>not</strong> express the recessive condition ({m('aa')}). Given that the child is unaffected, what is the probability that this child is a carrier ({m('Aa')})?",
        f"أبوان حاملان سليمَان لصفة متنحية ({m(r'\text{Aa} \times \text{Aa}')}) أنجبا طفلاً <strong>لا</strong> تظهر عليه الصفة المتنحية ({m('aa')}). بشرط أن الطفل سليم مظهرياً، ما احتمال أن يكون حاملاً للصفة ({m('Aa')})؟",
        Fraction(2, 3), [Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)],
        "Because the child is known to be unaffected, eliminate the aa box from the sample space.",
        "بما أننا نعلم أن الطفل غير مصاب، نستبعد مربع (aa) من فضاء الاحتمالات.",
        "Count carrier boxes (Aa) out of the 3 unaffected boxes (AA, Aa, Aa).",
        ["The full Punnett square has 4 equally likely outcomes: AA, Aa, Aa, aa.",
         "Conditioning on being unaffected removes aa, leaving 3 equally likely outcomes: 1 AA and 2 Aa.",
         f"Therefore the conditional probability is {m(r'\frac{2}{3}')}."],
        "Do not confuse 2/4 = 1/2 (prior chance before phenotype is known) with 2/3 (given unaffected).",
        "نحصر الاحتمال في المربعات الثلاثة السليمة فقط.",
        ["النتائج الأربع الكلية هي AA و Aa و Aa و aa.",
         "استبعاد المربع المصاب aa يُبقي 3 احتمالات متساوية: واحد AA واثنان Aa.",
         f"إذن الاحتمال الشرطي هو {m(r'\frac{2}{3}')}."],
        "الاحتمال قبل معرفة سلامة الطفل هو 2/4، أما بشرط سلامته فهو 2/3.",
        diagram_en=svg_punnett_square("Aa", "Aa", ["AA", "Aa", "Aa", "aa"], "Carrier Cross: Aa x Aa"),
        diagram_ar=_ar_svg(svg_punnett_square("Aa", "Aa", ["AA", "Aa", "Aa", "aa"], "Carrier Cross: Aa x Aa"),
                           {"Carrier Cross: Aa x Aa": "تزاوج حاملين: Aa × Aa"}),
    ))

    # 12 (Hard): Two independent births from Aa x Aa both aa -> 1/16
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        f"Two heterozygous parents ({m(r'\text{Aa} \times \text{Aa}')}) plan to have two children. What is the probability that <strong>both</strong> the first and second child inherit the homozygous recessive genotype ({m('aa')})?",
        f"أبوان متغايرا الجينات ({m(r'\text{Aa} \times \text{Aa}')}) يخططان لإنجاب طفلين. ما احتمال أن يرث <strong>كلا</strong> الطفلين الطراز الجيني المتنحي ({m('aa')})؟",
        Fraction(1, 16), [Fraction(1, 4), Fraction(1, 8), Fraction(1, 2)],
        "Each birth is an independent event with P(aa) = 1/4.",
        "كل ولادة حدث مستقل احتماله 1/4.",
        f"Multiply {m(r'P(\text{aa}) \times P(\text{aa})')}.",
        [f"For each single birth from {m(r'\text{Aa} \times \text{Aa}')}, {m(r'P(\text{aa}) = \frac{1}{4}')}.",
         f"Since births are independent, {m(r'P(\text{both aa}) = \frac{1}{4} \times \frac{1}{4} = \frac{1}{16}')}."],
        f"In percentage, {m(r'1/16 = 6.25\%')}.",
        "نضرب احتمال الولادة الأولى في احتمال الولادة الثانية.",
        [f"احتمال إنجاب طفل {m('aa')} في المرة الواحدة هو {m(r'\frac{1}{4}')}.",
         f"لأن الحدثين مستقلان: {m(r'\frac{1}{4} \times \frac{1}{4} = \frac{1}{16}')}."],
        f"القيمة تعادل {m(r'6.25\%')}.",
    ))

    # 13 (Hard): Hydrogen bonds in 50-bp DNA duplex
    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        f"In DNA, each {m('A=T')} base pair is joined by {m('2')} hydrogen bonds, while each {m('G\\equiv C')} base pair is joined by {m('3')} hydrogen bonds. A {m('50')}-base-pair DNA segment has {m('18')} Adenines on one strand (and no Adenines on the opposite sites). Wait: if the {m('50')}-base-pair duplex contains {m('18')} {m('A=T')} pairs in total, how many hydrogen bonds hold the two strands together?",
        f"في DNA يرتبط زوج القواعد {m('A=T')} برابطتين هيدروجينيتين، بينما يرتبط زوج {m('G\\equiv C')} بثلاث روابط هيدروجينية. إذا احتوت قطعة DNA طولها {m('50')} زوجاً قاعدياً على {m('18')} زوج {m('A=T')}، فكم رابطة هيدروجينية تربط الشريطين معاً؟",
        132, [100, 118, 150],
        "Find the number of G≡C pairs (50 - 18), then multiply A=T pairs by 2 and G≡C pairs by 3.",
        "احسب عدد أزواج G≡C بطرح 18 من 50، ثم اضرب أزواج A=T في 2 وأزواج G≡C في 3.",
        f"Evaluate {m('18 \\times 2 + (50 - 18) \\times 3')}.",
        [f"Number of {m('G\\equiv C')} pairs = {m('50 - 18 = 32')}.",
         f"Total hydrogen bonds = {m('(18 \\times 2) + (32 \\times 3) = 36 + 96 = 132')}."],
        f"Notice {m('100 < 132 < 150')} since all A=T gives {m('100')} and all G≡C gives {m('150')}.",
        "نحسب عدد كل نوع من الأزواج ونضربه في عدد روابطه.",
        [f"عدد أزواج {m('G\\equiv C')} يساوي {m('50 - 18 = 32')} زوجاً.",
         f"إجمالي الروابط = {m('(18 \\times 2) + (32 \\times 3) = 36 + 96 = 132')} رابطة."],
        f"القيمة منطقية بين الحد الأدنى {m('100')} والحد الأقصى {m('150')}.",
    ))

    # 14 (Hard): Semi-conservative DNA replication after 3 cycles -> hybrid %
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        f"One DNA molecule made entirely of heavy nitrogen ({m('^{15}\\text{N}')}) is placed in light nitrogen ({m('^{14}\\text{N}')}) medium and replicates semi-conservatively for {m('3')} generations. What percentage of the resulting {m('8')} DNA molecules are hybrid ({m('^{15}\\text{N}/^{14}\\text{N}')})?",
        f"وُضع جزيء DNA واحد مكوّن بالكامل من النيتروجين الثقيل ({m('^{15}\\text{N}')}) في وسط من النيتروجين الخفيف ({m('^{14}\\text{N}')}) وتضاعف شبه محافظاً لـ {m('3')} أجيال. ما النسبة المئوية للجزيئات الهجينة ({m('^{15}\\text{N}/^{14}\\text{N}')}) من بين الجزيئات الـ {m('8')} الناتجة؟",
        25, [12.5, 50, 75],
        "The original 2 heavy single strands never disappear; each ends up in 1 hybrid duplex.",
        "الشريطان الأصليان الثقيلان لا يزولان، ويدخل كل منهما في تكوين جزيء هجين واحد.",
        f"Compute {m(r'\frac{2}{2^3} \times 100\%')}.",
        [f"After {m('3')} rounds of replication, there are {m('2^3 = 8')} DNA double helices.",
         f"Only {m('2')} molecules retain one original {m('^{15}\\text{N}')} strand paired with a new {m('^{14}\\text{N}')} strand.",
         f"Hybrid percentage = {m(r'\frac{2}{8} \times 100\% = 25\%')}."],
        f"The remaining {m('6')} molecules ({m(r'75\%')}) are pure light {m('^{14}\\text{N}/^{14}\\text{N}')}.",
        "نحدد عدد الجزيئات الهجينة الثابت (2) ونقسمه على العدد الكلي (8).",
        [f"بعد {m('3')} دورات تضاعف ينتج {m('2^3 = 8')} جزيئات DNA.",
         f"يحمل جزيئان فقط شريطاً أصلياً ثقيلاً مع شريط جديد خفيف (هجينان).",
         f"النسبة = {m(r'\frac{2}{8} \times 100\% = 25\%')}."],
        f"الـ {m('6')} جزيئات الأخرى ({m(r'75\%')}) خفيفة بالكامل.",
        suffix=r"\%",
    ))
    return qs


def _gen_sci_b03(start_idx: int) -> list[dict]:
    """G9-SCI-B03: Nervous reflex arc & endocrine hormone homeostasis."""
    bp = "G9-SCI-B03"
    qs: list[dict] = []

    # 0 (Easy): Reflex arc sequence
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        "Using the reflex arc diagram, what is the correct sequence of signal transmission when a hand pulls away from a hot pan?",
        "اعتماداً على مخطط القوس الانعكاسي، ما الترتيب الصحيح لانتقال السيال العصبي عند سحب اليد سريعاً عن إناء ساخن؟",
        [
            ("Receptor → Sensory neuron → Spinal interneuron → Motor neuron → Effector muscle",
             "المستقبل ← عصبون حسي ← عصبون موصل في الحبل الشوكي ← عصبون حركي ← العضلة المنفذة"),
            ("Effector muscle → Motor neuron → Brain cortex → Sensory neuron → Receptor",
             "العضلة المنفذة ← عصبون حركي ← قشرة الدماغ ← عصبون حسي ← المستقبل"),
            ("Sensory neuron → Receptor → Motor neuron → Spinal interneuron → Effector",
             "عصبون حسي ← المستقبل ← عصبون حركي ← الحبل الشوكي ← العضلة"),
            ("Receptor → Motor neuron → Spinal interneuron → Sensory neuron → Effector",
             "المستقبل ← عصبون حركي ← الحبل الشوكي ← عصبون حسي ← العضلة"),
        ],
        "Reflexes bypass conscious brain deliberation by routing directly through the spinal cord.",
        "يمر الفعل المنعكس مباشرة عبر الحبل الشوكي قبل الإدراك الواعي في الدماغ.",
        "Follow the arrows from stimulus detection to muscle contraction.",
        ["Thermal receptors detect heat and trigger the sensory neuron.",
         "The spinal cord interneuron relays the impulse immediately to the motor neuron, which contracts the arm muscle."],
        "Sensation reaches the brain slightly later, after the hand has already moved.",
        "نتتبع الأسهم من الإحساس بالمنبه إلى استجابة العضلة.",
        ["يرصد المستقبل الحرارة وينقلها عبر العصبون الحسي إلى الحبل الشوكي.",
         "يمرر العصبون الموصل الأمر فوراً للعصبون الحركي فتتقبض العضلة."],
        "هذا المسار السريع يحمي الجسم من الحروق قبل وصول الإدراك للدماغ.",
        diagram_en=_svg_reflex_arc("None", "en"),
        diagram_ar=_svg_reflex_arc("None", "ar"),
    ))

    # 1 (Easy): Insulin role
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        "Shortly after a carbohydrate-rich meal, blood glucose rises. Which hormone does the pancreas release, and how does it restore homeostasis?",
        "بعد تناول وجبة غنية بالكربوهيدرات يرتفع سكر الدم. ما الهرمون الذي يفرزه البنكرياس وكيف يعيد الاتزان الداخلي؟",
        [
            ("Insulin; stimulates body cells to absorb glucose and the liver to store it as glycogen",
             "الإنسولين؛ يحفز الخلايا على امتصاص الجلوكوز والكبد على تخزينه في صورة جلايكوجين"),
            ("Glucagon; breaks down liver glycogen to release more glucose into the blood",
             "الجلوكاجون؛ يحلّل جلايكوجين الكبد ليطلق مزيداً من الجلوكوز في الدم"),
            ("Adrenaline; slows cellular glucose uptake and raises blood pressure",
             "الأدرينالين؛ يبطئ امتصاص الخلايا للجلوكوز ويرفع ضغط الدم"),
            ("Thyroxine; converts blood glucose directly into urea in the kidneys",
             "الثيروكسين؛ يحول سكر الدم مباشرة إلى يوريا في الكليتين"),
        ],
        "Recall which pancreatic hormone lowers elevated blood sugar.",
        "تذكّر أي هرمون بنكرياسي يخفض سكر الدم المرتفع.",
        "Match insulin to glucose storage and glucagon to glucose release.",
        ["High blood glucose signals pancreatic beta cells to secrete insulin.",
         "Insulin enables glucose entry into muscle/fat cells and glycogen synthesis in the liver, lowering blood glucose back to ~90 mg/dL."],
        "Negative feedback stops insulin surge once normal levels return.",
        "نربط هرمون الإنسولين بتخزين الجلوكوز الزائد.",
        ["ارتفاع الجلوكوز ينبه خلايا بيتا في البنكرياس لإفراز الإنسولين.",
         "يساعد الإنسولين الخلايا على امتصاص الجلوكوز والكبد على تخزينه كجلايكوجين فينخفض السكر للمعدل الطبيعي."],
        "توقف التغذية الراجعة السلبية إفراز الإنسولين عند اعتدال المستوى.",
    ))

    # 2 (Easy): Glucagon role during fasting
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        "During extended fasting between meals, blood glucose begins to fall below normal. Which hormone restores blood glucose, and what is its target organ?",
        "أثناء الصيام الطويل يبدأ مستوى الجلوكوز في الدم بالانخفاض. ما الهرمون الذي يعيد رفعه وما العضو المستهدف؟",
        [
            ("Glucagon; acts on the liver to convert stored glycogen back into glucose",
             "الجلوكاجون؛ يعمل على الكبد لتحويل الجلايكوجين المخزّن إلى جلوكوز"),
            ("Insulin; acts on muscle cells to store excess glucose as glycogen",
             "الإنسولين؛ يعمل على العضلات لتخزين الجلوكوز الزائد كجلايكوجين"),
            ("Melatonin; acts on the kidneys to conserve water",
             "الميلاتونين؛ يعمل على الكليتين لحفظ الماء"),
            ("Testosterone; stimulates red blood cell synthesis in bone marrow",
             "التستوستيرون؛ يحفز إنتاج خلايا الدم الحمراء في نخاع العظم"),
        ],
        "Which hormone opposes insulin when blood glucose drops?",
        "ما الهرمون الذي يعاكس عمل الإنسولين عند هبوط سكر الدم؟",
        "Glucagon raises blood glucose by mobilizing liver glycogen.",
        ["Low blood glucose stimulates pancreatic alpha cells to release glucagon.",
         "Glucagon triggers glycogenolysis in liver cells, releasing glucose into the bloodstream."],
        "Insulin and glucagon form an antagonistic negative-feedback pair.",
        "يرفع الجلوكاجون سكر الدم عبر تكسير الجلايكوجين الكبدي.",
        ["انخفاض الجلوكوز ينبه خلايا ألفا لإفراز الجلوكاجون.",
         "يحفز الجلوكاجون الكبد على تفكيك الجلايكوجين وإطلاق الجلوكوز إلى الدم."],
        "الإنسولين والجلوكاجون يعملان بتضاد للحفاظ على ثبات السكر.",
    ))

    # 3 (Easy): Nervous vs Endocrine comparison
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        "How does signaling in the endocrine system differ from signaling in the nervous system?",
        "كيف يختلف نقل الإشارات في جهاز الغدد الصماء عن نقلها في الجهاز العصبي؟",
        [
            ("Endocrine uses chemical hormones via blood (slower, longer-lasting); nervous uses electrical impulses along neurons (very fast, brief)",
             "الغدد الصماء تستخدم هرمونات كيميائية عبر الدم (أبطأ وأطول أثراً)، بينما العصبي يستخدم سيالات كهربائية سريعة وقصيرة الأمد"),
            ("Endocrine signals travel only through bones; nervous signals travel through blood plasma",
             "تنتقل إشارات الغدد عبر العظام بينما تنتقل الإشارات العصبية عبر بلازما الدم"),
            ("Endocrine responses last milliseconds; nervous reflexes take hours to begin",
             "تستمر استجابة الغدد أجزاء من الثانية بينما تستغرق المنعكسات العصبية ساعات"),
            ("Only the nervous system uses chemical messengers at any point",
             "الجهاز العصبي فقط يستخدم نواقل كيميائية في أي مرحلة"),
        ],
        "Compare speed, transport medium, and duration of hormones vs action potentials.",
        "قارن بين السرعة ووسيلة النقل ومدة الأثر في الهرمونات مقابل السيال العصبي.",
        "Contrast bloodstream hormone transport with neuronal signaling.",
        ["Nerve impulses travel rapidly along axons to specific targets for millisecond precision.",
         "Hormones travel through the bloodstream to distant target cells carrying matching receptors, producing slower but sustained regulation."],
        "Both systems coordinate via negative feedback to preserve homeostasis.",
        "نقارن النقل الدموي بالانتقال عبر المحاور العصبية.",
        ["السيال العصبي سريع جداً ومحدد الهدف ومؤقت.",
         "الهرمونات تُنقل عبر الدم لتصل لأعضاء مستهدفة ذات مستقبلات خاصة ويدوم أثرها أطول."],
        "يتكامل الجهازان للحفاظ على الاتزان الداخلي.",
    ))

    # 4 (Easy): Thermoregulation negative feedback
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "On a hot summer afternoon in Riyadh, a runner's core temperature rises above 37 °C. Which two hypothalamic negative-feedback responses help cool the body?",
        "في ظهيرة صيف حارة بالرياض، ترتفع حرارة جسم عدّاء فوق 37 °س. ما الاستجابتان التنظيميتان اللتان يطلقهما تحت المهاد لتبريد الجسم؟",
        [
            ("Sweat gland secretion (evaporative cooling) and vasodilation of skin blood vessels",
             "إفراز العرق (للتبريد بالتبخر) وتوسع الأوعية الدموية الجلدية"),
            ("Rapid skeletal muscle shivering and vasoconstriction of skin vessels",
             "ارتعاش العضلات الهيكلية وتضيق الأوعية الدموية الجلدية"),
            ("Decreased breathing rate and elevated thyroxine secretion",
             "إبطاء معدل التنفس وزيادة إفراز الثيروكسين"),
            ("Stopping perspiration and raising metabolic heat production",
             "إيقاف التعرق وزيادة إنتاج الحرارة الأيضية"),
        ],
        "Think about how heat leaves the body at the skin surface.",
        "فكّر في كيفية تخلص الجسم من الحرارة الزائدة عبر سطح الجلد.",
        "Identify cooling effectors vs warming effectors.",
        ["Vasodilation brings warm blood closer to the skin surface to radiate heat.",
         "Sweating absorbs latent heat from the skin as water evaporates."],
        "Shivering and vasoconstriction conserve or generate heat when cold.",
        "نميّز استجابات التبريد عن استجابات التدفئة.",
        ["توسع الأوعية الجلدية يزيد تدفق الدم نحو السطح لتشتيت الحرارة.",
         "تبخر العرق يمتص حرارة من الجلد فيبرّد الجسم."],
        "الارتعاش وتضيق الأوعية يحدثان عند البرد لا الحر.",
    ))

    # 5 (Medium): Motor neuron lesion in reflex arc
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        "As shown in the reflex arc diagram, a patient suffers localized damage blocking only the <strong>motor neuron</strong> to the lower leg, while sensory neurons and spinal cord connections remain intact. What happens when a doctor taps the knee tendon?",
        "كما يظهر في مخطط القوس الانعكاسي، أصيب مريض بتلف موضعي في <strong>العصبون الحركي</strong> المتصل بالساق، مع سلامة العصبون الحسي والحبل الشوكي. ماذا يحدث عند طرق وتر الركبة؟",
        [
            ("The patient feels the tap normally, but the leg fails to kick forward",
             "يشعر المريض بالطرق بشكل طبيعي، لكن الساق لا تتحرك للرد بالركل"),
            ("The leg kicks strongly, but the patient feels no sensation at all",
             "تركل الساق بقوة لكن المريض لا يشعر بأي إحساس"),
            ("Both sensation and leg kick remain completely normal",
             "يبقى كل من الإحساس وحركة الركل طبيعيين تماماً"),
            ("The sensory neuron transforms into a muscle fiber to compensate",
             "يتحول العصبون الحسي إلى ليفة عضلية للتعويض"),
        ],
        "Follow the signal path: sensory signals still travel up to the brain, but motor signals cannot reach the muscle.",
        "تتبع المسار: الإشارة الحسية تصل للدماغ، لكن الأمر الحركي لا يصل للعضلة.",
        "Trace sensation (ascending sensory pathway) separately from movement (efferent motor pathway).",
        ["The intact sensory neuron carries the tap signal into the spinal cord and up to the brain, so sensation is preserved.",
         "Because the motor neuron is blocked, no command reaches the effector muscle, preventing the kick."],
        "Intact sensory + broken motor = feels touch without movement.",
        "نفصل مسار الإحساس الصاعد عن المسار الحركي الصادر.",
        ["العصبون الحسي سليم فينقل الإحساس إلى الحبل الشوكي والدماغ.",
         "انقطاع العصبون الحركي يمنع وصول الأمر إلى العضلة فلا تتحرك الساق."],
        "إحساس سليم مع غياب الحركة يعني خللاً في العصبون الحركي.",
        diagram_en=_svg_reflex_arc("Motor", "en"),
        diagram_ar=_svg_reflex_arc("Motor", "ar"),
    ))

    # 6 (Medium): Sensory neuron lesion in reflex arc
    qs.append(make_science_concept_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        "In the diagram, a local anesthetic temporarily blocks transmission along the <strong>sensory neuron</strong> of a finger. What occurs if the finger accidentally touches a sharp pin?",
        "في المخطط، قام مخدّر موضعي بتعطيل النقل مؤقتاً عبر <strong>العصبون الحسي</strong> للإصبع. ماذا يحدث عند ملامسة الإصبع لدبوس حاد؟",
        [
            ("Neither pain sensation nor automatic reflex withdrawal occurs",
             "لا يحدث إحساس بالألم ولا سحب لاإرادي للإصبع"),
            ("The finger withdraws rapidly even though no pain is felt",
             "ينسحب الإصبع سريعاً رغم عدم الشعور بالألم"),
            ("The finger feels sharp pain but cannot move",
             "يشعر الإصبع بألم حاد لكنه يعجز عن الحركة"),
            ("Endocrine hormones immediately trigger the muscle directly",
             "تحفز الهرمونات العضلة مباشرة وبشكل فوري"),
        ],
        "If the input wire from the receptor is cut, neither the spinal reflex nor the brain receives any message.",
        "إذا انقطع السلك الحسي القادم من المستقبل فلن تصل الإشارة لا للحبل الشوكي ولا للدماغ.",
        "Trace the consequence of blocking the very first neural link after the receptor.",
        ["Without sensory input reaching the spinal cord, the interneuron and motor neuron are never activated (no reflex).",
         "Because no signal ascends to the brain either, the person feels no pain."],
        "Local dental/skin anesthesia targets sensory nerves for this exact reason.",
        "نتتبع أثر انقطاع أول ناقل عصبي بعد المستقبل.",
        ["عدم وصول الإشارة الحسية للحبل الشوكي يمنع تنشيط العصبون الموصل والحركي (لا حركة).",
         "ولا تصعد إشارة إلى الدماغ، فلا يشعر الشخص بالألم."],
        "لهذا السبب تُستخدم المخدرات الموضعية لإيقاف الأعصاب الحسية.",
        diagram_en=_svg_reflex_arc("Sensory", "en"),
        diagram_ar=_svg_reflex_arc("Sensory", "ar"),
    ))

    # 7 (Medium): Blood glucose graph interpretation
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        "The graph shows a healthy student's blood glucose concentration after drinking juice at t = 0 min. During which interval is pancreatic <strong>insulin</strong> secretion highest to restore baseline glucose?",
        "يوضح الرسم البياني تركيز جلوكوز الدم لطالب سليم بعد شرب عصير عند الزمن 0 دقيقة. خلال أي فترة زمنية يكون إفراز هرمون <strong>الإنسولين</strong> في ذروته لإعادة السكر إلى مستواه الطبيعي؟",
        [
            ("Between 30 and 60 minutes, driving glucose down from 160 to 100 mg/dL",
             "بين 30 و 60 دقيقة، حيث يُخفض الجلوكوز من 160 إلى 100 mg/dL"),
            ("Between 0 and 30 minutes, causing glucose to rise sharply",
             "بين 0 و 30 دقيقة، مما يسبب ارتفاع الجلوكوز بحدة"),
            ("At 90 minutes, to prevent glucose from falling below 90 mg/dL",
             "عند 90 دقيقة لمنع الجلوكوز من الهبوط دون 90 mg/dL"),
            ("Only prior to drinking juice when glucose is already steady",
             "قبل شرب العصير فقط عندما يكون السكر مستقراً"),
        ],
        "Insulin responds to the peak blood glucose and drives the downward recovery slope.",
        "يستجيب الإنسولين لذروة ارتفاع السكر ويسبب الهبوط التدريجي نحو المستوى الطبيعي.",
        "Locate the peak at t = 30 min and the subsequent drop.",
        ["Blood glucose peaks at 160 mg/dL at t = 30 min.",
         "High insulin triggers rapid cellular uptake and liver glycogen storage between 30 and 60 min, returning glucose toward 90–100 mg/dL."],
        "During 0–30 min, intestinal absorption of juice raises glucose before insulin clears it.",
        "نحدد القمة عند 30 دقيقة ثم فترة الهبوط نحو الاعتدال.",
        ["يصل الجلوكوز إلى ذروته (160) عند الدقيقة 30.",
         "يرتفع الإنسولين عند الذروة ليخفض السكر بين الدقيقتين 30 و 60 نحو المعدل الطبيعي."],
        "الفترة 0–30 تمثل امتصاص السكر من الأمعاء إلى الدم.",
        diagram_en=svg_motion_graph([(0, 90), (30, 160), (60, 100), (90, 90)], "mg/dL", "Time (min)", "Glucose Curve"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 90), (30, 160), (60, 100), (90, 90)], "mg/dL", "Time (min)", "Glucose Curve"),
                           {"Time (min)": "الزمن (د)", "Glucose Curve": "منحنى جلوكوز الدم"}),
    ))

    # 8 (Medium): Adrenaline fight-or-flight physiological shift
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        "When startled by sudden danger, the adrenal glands release adrenaline (epinephrine). Which combination of physiological changes prepares the body for rapid action?",
        "عند التعرض لموقف مفاجئ وخطر، تفرز الغدة الكظرية هرمون الأدرينالين. أي مجموعة من التغيرات الفسيولوجية تهيئ الجسم للاستجابة السريعة؟",
        [
            ("Increased heart rate, dilated airways, glycogen breakdown to glucose, and reduced blood flow to digestion",
             "زيادة نبض القلب، توسع الممرات التنفسية، تحويل الجلايكوجين إلى جلوكوز، وتقليل الدم المتجه للهضم"),
            ("Decreased heart rate, constricted bronchioles, and stimulated stomach digestion",
             "انخفاض نبض القلب، تضيق القصيبات الهوائية، وتنشيط عملية الهضم في المعدة"),
            ("Increased insulin secretion to remove all glucose from muscle blood supply",
             "زيادة إفراز الإنسولين لسحب كل الجلوكوز من العضلات"),
            ("Sweat inhibition and slower breathing to conserve energy",
             "إيقاف التعرق وإبطاء التنفس لتوفير الطاقة"),
        ],
        "Fight-or-flight prioritizes oxygen and fuel delivery to skeletal muscles and brain.",
        "استجابة الكرّ والفرّ تعطي الأولوية لإيصال الأكسجين والوقود إلى العضلات والدماغ.",
        "Select changes that boost ATP production and oxygen flow while pausing non-urgent digestion.",
        ["Adrenaline raises heart rate and dilates bronchioles to deliver more oxygen.",
         "It converts liver glycogen into glucose for immediate muscle fuel and diverts blood away from the digestive tract."],
        "Digestion is temporarily slowed because survival movement is urgent.",
        "نختار التغيرات التي تزيد الأكسجين والطاقة وتؤجل الهضم.",
        ["يرفع الأدرينالين نبض القلب ويوسع الشعب الهوائية لزيادة الأكسجين.",
         "ويطلق الجلوكوز من الكبد للعضلات ويحوّل الدم من الجهاز الهضمي نحو العضلات."],
        "يُبطأ الهضم مؤقتاً لتوجيه الطاقة إلى العضلات.",
    ))

    # 9 (Medium): Quantitative glucose clearance rate
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        f"After a meal, a student's blood glucose peaks at {m('180')} mg/dL and is lowered by insulin to {m('90')} mg/dL over {m('60')} minutes. What is the average rate of blood glucose decrease (in mg/dL per minute)?",
        f"بعد وجبة، بلغ جلوكوز الدم ذروته عند {m('180')} mg/dL ثم خفضه الإنسولين إلى {m('90')} mg/dL خلال {m('60')} دقيقة. ما متوسط معدل انخفاض جلوكوز الدم (بوحدة mg/dL لكل دقيقة)؟",
        1.5, [0.5, 2.0, 3.0],
        "Divide the total drop in glucose concentration by the elapsed time in minutes.",
        "اقسم مقدار الانخفاض الكلي في تركيز الجلوكوز على الزمن المنقضي بالدقائق.",
        f"Compute {m(r'\frac{180 - 90}{60}')}.",
        [f"Glucose drop: {m('180 - 90 = 90')} mg/dL.",
         f"Average clearance rate = {m('90 \\div 60 = 1.5')} mg/dL per minute."],
        f"Check: {m('1.5 \\times 60 = 90')} mg/dL decrease.",
        "نقسم الفرق في التركيز على المدة الزمنية.",
        [f"مقدار الانخفاض = {m('180 - 90 = 90')} mg/dL.",
         f"المعدل المتوسط = {m('90 \\div 60 = 1.5')} mg/dL في الدقيقة."],
        f"التحقق: {m('1.5 \\times 60 = 90')}.",
        diagram_en=svg_motion_graph([(0, 180), (30, 135), (60, 90)], "mg/dL", "Time (min)", "Insulin Action"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 180), (30, 135), (60, 90)], "mg/dL", "Time (min)", "Insulin Action"),
                           {"Time (min)": "الزمن (د)", "Insulin Action": "عمل الإنسولين"}),
    ))

    # 10 (Hard): Type 1 vs Type 2 diabetes diagnosis
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        "Patient X has fasting blood glucose of 240 mg/dL with <strong>near-zero</strong> blood insulin, whereas Patient Y has fasting blood glucose of 230 mg/dL with <strong>abnormally high</strong> blood insulin. What best explains the two diagnoses?",
        "لدى المريض (س) سكر صائم 240 mg/dL مع مستوى إنسولين <strong>قريب من الصفر</strong>، بينما لدى المريض (ص) سكر صائم 230 mg/dL مع مستوى إنسولين <strong>مرتفع جداً</strong>. ما التفسير الأدق لحالتيهما؟",
        [
            ("Patient X has Type 1 diabetes (damaged beta cells produce no insulin); Patient Y has Type 2 diabetes (target cell receptors resist insulin)",
             "المريض (س) مصاب بالنوع الأول (تلف خلايا بيتا وعدم إفراز الإنسولين)، والمريض (ص) بالنوع الثاني (مقاومة مستقبلات الخلايا للإنسولين)"),
            ("Patient X has Type 2 diabetes due to excess receptor sensitivity; Patient Y has low glucagon",
             "المريض (س) مصاب بالنوع الثاني لفرط حساسية المستقبلات، والمريض (ص) بنقص الجلوكاجون"),
            ("Both patients lack liver glycogen stores completely",
             "كلا المريضين يفتقدان مخزون الجلايكوجين في الكبد بالكامل"),
            ("Patient Y produces excess insulin because blood glucose is too low",
             "المريض (ص) يفرز إنسوليناً كثيراً لأن سكر دمه منخفض جداً"),
        ],
        "Compare hormone production failure versus target-cell receptor resistance.",
        "قارن بين فشل إنتاج الهرمون مقابل عدم استجابة مستقبلات الخلايا له.",
        "Relate high glucose + zero insulin vs high glucose + high insulin.",
        ["In Type 1 diabetes, autoimmune destruction of pancreatic beta cells eliminates insulin secretion (Patient X).",
         "In Type 2 diabetes, cells become insulin-resistant, so glucose stays high and the pancreas keeps secreting more insulin unsuccessfully (Patient Y)."],
        "Both conditions exhibit hyperglycemia, yet require different treatments.",
        "نربط نقص الإنسولين بتلف البنكرياس، وارتفاعه مع ارتفاع السكر بمقاومة المستقبلات.",
        ["في السكري من النوع الأول تتلف خلايا بيتا فيتوقف إفراز الإنسولين (المريض س).",
         "في النوع الثاني لا تستجيب مستقبلات الخلايا للإنسولين فيزداد إفرازه دون فائدة (المريض ص)."],
        "كلاهما يسببان ارتفاع سكر الدم لكن آلية الخلل مختلفة.",
    ))

    # 11 (Hard): Pituitary-thyroid negative feedback (low T4 -> high TSH)
    qs.append(make_science_concept_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        "The pituitary gland secretes TSH to stimulate the thyroid gland to release thyroxine (T4), while high T4 inhibits the pituitary via negative feedback. If severe dietary iodine deficiency prevents a patient's thyroid from making T4, what happens to blood TSH levels?",
        "تفرز الغدة النخامية هرمون TSH لتحفيز الغدة الدرقية على إفراز الثيروكسين (T4)، ويثبط ارتفاع T4 النخامية بالتغذية الراجعة السلبية. إذا منع نقص اليود الشديد الغدة الدرقية من تصنيع T4، فماذا يحدث لمستوى TSH في الدم؟",
        [
            ("Blood TSH rises far above normal because negative feedback inhibition by T4 is lost",
             "يرتفع هرمون TSH كثيراً فوق الطبيعي لانعدام التثبيط الراجع من هرمون T4"),
            ("Blood TSH drops to zero because the thyroid stops functioning",
             "ينخفض هرمون TSH إلى الصفر بسبب توقف الغدة الدرقية"),
            ("Blood TSH stays completely constant regardless of T4 levels",
             "يبقى مستوى TSH ثابتاً تماماً بغض النظر عن مستوى T4"),
            ("The pituitary directly converts TSH into dietary iodine",
             "تحول الغدة النخامية هرمون TSH مباشرة إلى يود غذائي"),
        ],
        "When the inhibiting signal (T4) disappears, the pituitary tries harder to stimulate the thyroid.",
        "عندما يختفي الهرمون المثبط (T4)، تضاعف النخامية إفراز TSH لمحاولة تنشيط الدرقية.",
        "Trace negative feedback removal on the upstream gland.",
        ["Normally T4 acts as the brake on pituitary TSH secretion.",
         "Without T4, that brake is removed, so the pituitary secretes excessive TSH (often causing thyroid enlargement/goiter)."],
        "High TSH + low T4 is the hallmark lab signature of primary hypothyroidism.",
        "نتتبع زوال الكابح السلبي عن الغدة النخامية.",
        ["يعمل T4 طبيعياً كمكبح لإفراز TSH من النخامية.",
         "عند غياب T4 يزول الكبح فتُفرط النخامية في إفراز TSH مما يسبب تضخم الدرقية."],
        "ارتفاع TSH مع انخفاض T4 علامة مخبرية لقصور الدرقية.",
    ))

    # 12 (Hard): Pituitary-thyroid negative feedback (T4-secreting tumor -> low TSH)
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        "A benign thyroid nodule begins secreting excessive thyroxine (T4) independently of pituitary control. According to negative feedback, how will the patient's pituitary TSH level change?",
        "بدأت عقدة درقية حميدة بإفراز كميات مفرطة من الثيروكسين (T4) بشكل مستقل عن تحكم النخامية. وفق آلية التغذية الراجعة السلبية، كيف يتغير مستوى TSH النخامي في دم المريض؟",
        [
            ("TSH drops below normal because excess T4 strongly inhibits pituitary TSH release",
             "ينخفض TSH دون الطبيعي لأن زيادة T4 تثبط بشدة إفراز النخامية له"),
            ("TSH rises proportionally alongside T4 to amplify metabolism further",
             "يرتفع TSH طردياً مع T4 لزيادة معدل الأيض أكثر"),
            ("TSH converts into insulin inside the bloodstream",
             "يتحول TSH إلى إنسولين داخل مجرى الدم"),
            ("TSH remains completely unaffected by high T4",
             "لا يتأثر TSH إطلاقاً بارتفاع T4"),
        ],
        "High hormone output applies strong negative feedback to shut down the pituitary stimulator.",
        "ارتفاع الهرمون النهائي يطبق تثبيطاً راجعاً قوياً لإيقاف الهرمون المحفز من النخامية.",
        "Apply negative feedback inhibition to excess T4.",
        ["Excess T4 signals the hypothalamus and pituitary that thyroid hormone is already too high.",
         "Negative feedback suppresses pituitary TSH secretion to very low levels."],
        "High T4 + suppressed TSH identifies primary hyperthyroidism.",
        "نطبّق التثبيط الراجع عند فرط إفراز T4.",
        ["ارتفاع T4 يرسل إشارة للنخامية بأن مستوى الهرمون زائد عن الحاجة.",
         "تستجيب النخامية بخفض إفراز TSH إلى مستويات متدنية جداً."],
        "ارتفاع T4 مع انخفاض TSH يميز فرط نشاط الدرقية.",
    ))

    # 13 (Hard): Osmoregulation ADH dehydration loop
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        "During a long desert hike without water, blood solute concentration increases. How does the ADH (antidiuretic hormone) negative-feedback loop restore blood water balance?",
        "أثناء مشي طويل في الصحراء دون شرب الماء، يرتفع تركيز الأملاح في الدم. كيف تعيد حلقة التغذية الراجعة لهرمون ADH (المانع لإدرار البول) توازن ماء الدم؟",
        [
            ("Hypothalamus detects concentrated blood → pituitary releases more ADH → kidney ducts reabsorb more water → small volume of concentrated urine",
             "يرصد تحت المهاد تركّز الدم ← تفرز النخامية مزيداً من ADH ← تعيد الكلية امتصاص الماء ← يقل حجم البول ويصبح مركزاً"),
            ("Pituitary stops all ADH release → kidneys excrete large volumes of dilute urine",
             "توقف النخامية إفراز ADH ← تطرح الكلية كميات كبيرة من البول المخفف"),
            ("Kidneys secrete ADH to increase sweating across the skin",
             "تفرز الكلى هرمون ADH لزيادة التعرق عبر الجلد"),
            ("Pancreas releases glucagon so kidneys convert salt directly into water",
             "يفرز البنكرياس الجلوكاجون فتحوّل الكلى الملح إلى ماء"),
        ],
        "When dehydrated, the body must conserve water by making urine more concentrated.",
        "عند الجفاف يجب أن يحفظ الجسم الماء بإعادة امتصاصه في الكلى وجعل البول مركزاً.",
        "Trace sensor (hypothalamus) → hormone (ADH) → effector (kidney collecting ducts).",
        ["Osmoreceptors in the hypothalamus sense elevated blood solute concentration.",
         "Increased ADH makes kidney collecting ducts more permeable to water, returning water to blood and minimizing urine water loss."],
        "Drinking excess water reverses this: ADH drops and urine becomes dilute.",
        "نتتبع المستقبل ثم الهرمون ثم العضو المنفذ.",
        ["تستشعر مستقبلات الأسموزية في تحت المهاد ارتفاع تركيز الدم.",
         "يزيد هرمون ADH نفاذية الأنابيب الكلوية للماء فيُعاد للدم ويخرج بول قليل ومركز."],
        "عند شرب ماء كثير ينعكس المسار فينخفض ADH ويصبح البول مخففاً.",
    ))

    # 14 (Hard): Unidirectional synaptic transmission
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        "Why do nerve impulses normally cross a chemical synapse in <strong>one direction only</strong> (from axon terminal of neuron 1 to dendrite of neuron 2)?",
        "لماذا تعبر السيالات العصبية التشابك الكيميائي عادةً في <strong>اتجاه واحد فقط</strong> (من النهاية المحورية للعصبون الأول إلى الزوائد الشجيرية للعصبون الثاني)؟",
        [
            ("Neurotransmitter vesicles are located only in the presynaptic axon terminal, while matching receptors exist only on the postsynaptic membrane",
             "لأن حويصلات النواقل العصبية توجد فقط في النهاية قبل التشابكية، بينما توجد مستقبلاتها فقط على الغشاء بعد التشابكي"),
            ("Myelin sheaths block backward electrical flow inside every synapse",
             "لأن الغمد المايليني يسد التدفق العكسي داخل كل تشابك عصبي"),
            ("Synaptic clefts contain one-way mechanical valves made of bone cartilage",
             "لأن الشق التشابكي يحتوي على صمامات غضروفية ميكانيكية أحادية الاتجاه"),
            ("Dendrites release enzymes that destroy all axons upon contact",
             "لأن الزوائد الشجيرية تفرز إنزيمات تدمر المحاور عند التلامس"),
        ],
        "Compare the asymmetric structures on each side of the synaptic cleft.",
        "قارن البنية غير المتماثلة على جانبي الشق التشابكي.",
        "Locate neurotransmitter release sites versus receptor binding sites.",
        ["Action potentials trigger calcium-dependent release of neurotransmitters from vesicles stored exclusively in the presynaptic axon terminal.",
         "Only the postsynaptic dendrite/cell body membrane carries specific receptor proteins to open ion channels in response."],
        "Structural asymmetry enforces one-way information flow across neural circuits.",
        "نحدد موقع إفراز النواقل وموقع المستقبلات.",
        ["السيال يفتح قنوات الكالسيوم في النهاية المحورية لتنطلق النواقل العصبية من الحويصلات هناك فقط.",
         "الغشاء المقابل (بعد التشابكي) هو الذي يحمل مستقبلات تلك النواقل ليبدأ سيالاً جديداً."],
        "هذا عدم التماثل التركيبي يفرض مرور الإشارة باتجاه واحد فقط.",
    ))
    return qs


def _gen_sci_b04(start_idx: int) -> list[dict]:
    """G9-SCI-B04: Osmosis, diffusion, active transport & adaptive/innate immunity."""
    bp = "G9-SCI-B04"
    qs: list[dict] = []

    # 0 (Easy): Osmosis direction definition
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        "Looking at the semi-permeable membrane diagram (water can cross; salt cannot), in which direction is the net movement of water by <strong>osmosis</strong>?",
        "بالنظر إلى مخطط الغشاء شبه المنفذ (يسمح بمرور الماء ويمنع مرور الملح)، في أي اتجاه يكون صافي حركة الماء بـ <strong>الخاصية الأسموزية</strong>؟",
        [
            ("From the 2% salt side (higher water concentration) to the 10% salt side (lower water concentration)",
             "من جهة الملح 2% (تركيز الماء الأعلى) إلى جهة الملح 10% (تركيز الماء الأقل)"),
            ("From the 10% salt side to the 2% salt side until the left side dries out",
             "من جهة الملح 10% إلى جهة الملح 2% حتى تجف الجهة اليسرى"),
            ("Salt ions diffuse rapidly from 2% to 10% while water stays stationary",
             "تنتشر أيونات الملح سريعاً من 2% إلى 10% بينما يبقى الماء ساكناً"),
            ("No water molecules cross the membrane in either direction",
             "لا تعبر أي جزيئات ماء الغشاء في أي اتجاه"),
        ],
        "Water always moves by osmosis toward the side with higher solute (lower free water) concentration.",
        "يتحرك الماء بالأسموزية دائماً نحو الجهة ذات التركيز الأعلى للمذاب.",
        "Compare free water percentage: 98% water (left) vs 90% water (right).",
        ["Left chamber has 2% salt (98% water); right chamber has 10% salt (90% water).",
         "Net water movement flows from higher water concentration (left) to lower water concentration (right) to equalize solute concentrations."],
        "Osmosis is passive transport of water requiring zero cellular ATP.",
        "نقارن نسبة الماء الحر في الجهتين: 98% مقابل 90%.",
        ["الجانب الأيسر يحتوي 2% ملحاً (98% ماء) والأيمن 10% ملحاً (90% ماء).",
         "يتدفق الماء من التركيز المائي الأعلى (اليسار) نحو التركيز المائي الأقل (اليمين) لتعديل التركيز."],
        "الأسموزية نقل سلبي للماء لا يستهلك طاقة.",
        diagram_en=_svg_osmosis_membrane("2% Salt", "10% Salt", "Low Solute", "High Solute",
                                         "تركيز مذاب أقل", "تركيز مذاب أعلى", "en"),
        diagram_ar=_svg_osmosis_membrane("2% ملح", "10% ملح", "Low Solute", "High Solute",
                                         "تركيز مذاب أقل", "تركيز مذاب أعلى", "ar"),
    ))

    # 1 (Easy): Active transport ATP requirement
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        "Plant root hair cells absorb mineral nitrate ions from dilute soil water even when the inside of the root already has a <strong>higher</strong> nitrate concentration. Which transport process accomplishes this?",
        "تمتص خلايا الشعيرات الجذرية أيونات النترات من تربة مخففة رغم أن تركيز النترات داخل الجذر <strong>أعلى</strong> بالفعل. أي عملية نقل تحقق ذلك؟",
        [
            ("Active transport, using carrier proteins and cellular ATP energy",
             "النقل النشط، باستخدام بروتينات ناقلة وطاقة الخلية (ATP)"),
            ("Simple diffusion down the concentration gradient without energy",
             "الانتشار البسيط مع تدرج التركيز دون استهلاك طاقة"),
            ("Osmosis moving mineral solids passively across cellulose",
             "الأسموزية التي تنقل الأملاح الصلبة تلقائياً عبر السليلوز"),
            ("Passive evaporation through root hair membranes",
             "التبخر السلبي عبر أغشية الشعيرات الجذرية"),
        ],
        "Moving solutes against a concentration gradient (low → high) requires cellular energy.",
        "نقل المواد عكس تدرج التركيز (من الأقل إلى الأعلى) يتطلب طاقة خلوية.",
        "Distinguish passive (down gradient) from active (up gradient) transport.",
        ["Passive diffusion and osmosis only move particles from high to low concentration.",
         "Pumping mineral ions from low soil concentration into high root concentration requires ATP-driven active transport."],
        "This is why waterlogged roots lacking O2 for respiration fail to absorb minerals.",
        "نميز بين النقل السلبي والنقل النشط عكس التدرج.",
        ["الانتشار والأسموزية ينقلان فقط من التركيز الأعلى إلى الأقل.",
         "نقل الأيونات من التربة الأقل تركيزاً إلى الجذر الأعلى تركيزاً يحتاج طاقة ATP عبر النقل النشط."],
        "لهذا تتضرر الجذور في التربة الغارقة لنقص الأكسجين اللازم لإنتاج ATP.",
    ))

    # 2 (Easy): Innate first-line barriers
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        "Which set lists only <strong>nonspecific (innate) first-line defenses</strong> that prevent pathogens from entering human tissues?",
        "أي مجموعة تضم فقط <strong>خطوط الدفاع الأولية الفطرية (غير المتخصصة)</strong> التي تمنع دخول مسببات الأمراض إلى أنسجة الجسم؟",
        [
            ("Intact skin, respiratory mucus with cilia, and acidic stomach fluid (HCl)",
             "الجلد السليم، والمخاط والأهداب التنفسية، وحمض المعدة (HCl)"),
            ("B-lymphocyte antibodies and cytotoxic T-cells",
             "الأجسام المضادة من الخلايا البائية والخلايا التائية القاتلة"),
            ("Vaccine-induced memory B-cells and monoclonal antibodies",
             "خلايا الذاكرة البائية الناتجة عن اللقاحات والأجسام المضادة وحيدة النسيلة"),
            ("Antibiotics and injected antivenom serum",
             "المضادات الحيوية ومصل مضادات السموم المحقون"),
        ],
        "First-line defenses block any microbe indiscriminately before specific immune cells respond.",
        "خطوط الدفاع الأولى تعيق جميع الميكروبات دون تمييز قبل تدخل المناعة المتخصصة.",
        "Separate physical/chemical barriers from adaptive lymphocytes.",
        ["Skin acts as a physical barrier, cilia sweep trapped mucus out of airways, and stomach acid kills swallowed microbes.",
         "Antibodies, B-cells, and T-cells belong to specific (adaptive) immunity."],
        "First-line defenses respond identically to every pathogen.",
        "نفصل الحواجز الفيزيائية والكيميائية عن الخلايا اللمفاوية المتخصصة.",
        ["الجلد حاجز فيزيائي، والأهداب والمخاط تطرد الغبار والميكروبات، وحمض المعدة يقتل الجراثيم المبتلعة.",
         "أما الأجسام المضادة والخلايا B و T فهي مناعة مكتسبة متخصصة."],
        "الحواجز الأولية تحمي ضد أي ميكروب دون تخصيص.",
    ))

    # 3 (Easy): How vaccination works
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        "How does a routine childhood vaccine protect a person against future exposure to a dangerous virus?",
        "كيف يحمي اللقاح الروتيني الطفل من الإصابة بفيروس خطير عند التعرض له مستقبلاً؟",
        [
            ("It exposes the immune system to weakened/harmless antigens to generate long-lived memory cells",
             "يعرّض الجهاز المناعي لمستضدات مضعفة أو ميتة لتكوين خلايا ذاكرة طويلة الأمد"),
            ("It destroys the patient's white blood cells so the virus cannot infect them",
             "يدمر خلايا الدم البيضاء للمريض حتى لا يصيبها الفيروس"),
            ("It works identically to an antibiotic by dissolving viral cell walls directly",
             "يعمل كالمضاد الحيوي فيذيب جدار الخلية الفيروسية مباشرة"),
            ("It supplies antibodies that survive permanently without immune cell involvement",
             "يزود الجسم بأجسام مضادة تدوم للأبد دون مشاركة خلايا المناعة"),
        ],
        "Think about active immunization and immunological memory.",
        "فكّر في التحصين النشط وتكوين الذاكرة المناعية.",
        "Connect safe antigen exposure → B/T cell activation → memory cells.",
        ["Vaccines introduce harmless antigens (weakened pathogen or protein subunit).",
         "B and T lymphocytes mount a safe primary response and leave memory cells that trigger an ultra-fast secondary response upon real infection."],
        "Viruses have no cell walls, so antibiotics do not treat viral infections.",
        "نربط التعرض الآمن للمستضد بتكوّن خلايا الذاكرة.",
        ["يحتوي اللقاح على مستضد مضعف أو جزء آمن يحفز الخلايا البائية والتائية.",
         "تتكون خلايا ذاكرة تسرّع إنتاج الأجسام المضادة فور دخول الفيروس الحقيقي مستقبلاً."],
        "المضادات الحيوية لا تؤثر في الفيروسات.",
    ))

    # 4 (Easy): Plant cell wall prevents bursting in distilled water
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "When placed in distilled water, an animal red blood cell swells and bursts, whereas a plant leaf cell becomes firm (turgid) without bursting. Looking at the cell diagram, which structure prevents the plant cell from bursting?",
        "عند وضع خلية دم حمراء في ماء مقطر تنتفخ وتنفجر، بينما تنتفخ الخلية النباتية وتمتلئ دون أن تنفجر. بالاستعانة برسم الخلية، ما التركيب الذي يمنع انفجار الخلية النباتية؟",
        [
            ("Cell Wall", "الجدار الخلوي"),
            ("Vacuole", "الفجوة العصارية"),
            ("Chloroplast", "البلاستيدة الخضراء"),
            ("Nucleus", "النواة"),
        ],
        "Look for the rigid outer cellulose frame highlighted in red.",
        "ابحث عن الإطار الخارجي الصلب المحدد باللون الأحمر في الخلية النباتية.",
        "Relate osmotic water entry to turgor pressure against a rigid wall.",
        ["Water enters both cells by osmosis in a hypotonic solution.",
         "The rigid cellulose cell wall resists outward turgor pressure and stops expansion before the membrane ruptures."],
        "Animal cells lack cell walls, so unchecked water influx causes lysis.",
        "نربط دخول الماء بالأسموزية مع مقاومة الجدار الصلب.",
        ["يدخل الماء إلى كلتا الخليتين بالأسموزية في الماء المقطر.",
         "يقاوم الجدار الخلوي السليلوزي الصلب ضغط الامتلاء الداخلي ويمنع تمزق الغشاء."],
        "تفتقر الخلية الحيوانية إلى الجدار الخلوي فتنفجر.",
        diagram_en=svg_cell_diagram("plant", "Cell Wall", "Plant Cell Protection"),
        diagram_ar=_ar_svg(svg_cell_diagram("plant", "Cell Wall", "Plant Cell Protection"),
                           {"Plant Cell Protection": "حماية الخلية النباتية"}),
    ))

    # 5 (Medium): Dialysis bag 3% in 12% sucrose
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        "A dialysis bag containing 3% sucrose solution (impermeable to sucrose, permeable to water) is placed into a beaker containing 12% sucrose solution. What happens to the bag's mass over 30 minutes?",
        "وُضع كيس غسيل شبه منفذ (يسمح بمرور الماء ويمنع السكروز) يحتوي على محلول سكروز 3% داخل كأس به محلول سكروز 12%. ماذا يحدث لكتلة الكيس بعد 30 دقيقة؟",
        [
            ("Mass decreases because water moves out of the bag into the hypertonic 12% beaker",
             "تقل الكتلة لأن الماء يخرج من الكيس إلى المحلول الأعلى تركيزاً (12%)"),
            ("Mass increases because water enters the bag toward the 3% solution",
             "تزداد الكتلة لأن الماء يدخل إلى الكيس نحو محلول 3%"),
            ("Mass stays constant because sucrose diffuses out to balance 12%",
             "تبقى الكتلة ثابتة لأن السكروز ينتشر خارج الكيس"),
            ("Mass increases because sucrose enters from the beaker into the bag",
             "تزداد الكتلة لأن السكروز يدخل من الكأس إلى الكيس"),
        ],
        "Compare solute concentration inside (3%) vs outside (12%); water flows toward higher solute.",
        "قارن التركيز داخل الكيس (3%) وخارجه (12%)؛ يتجه الماء نحو المذاب الأعلى.",
        "Classify the external 12% solution relative to the 3% interior.",
        ["The beaker (12% sucrose, 88% water) is hypertonic relative to the bag (3% sucrose, 97% water).",
         "Water moves down its concentration gradient out of the bag into the beaker, reducing the bag's mass."],
        "Sucrose molecules are too large to cross the dialysis pores.",
        "نحدد نوع المحلول الخارجي مقارنة بالداخلي.",
        ["المحلول الخارجي (12% سكروز) مرتفع التركيز مقارنة بداخل الكيس (3%).",
         "يخرج الماء من الكيس إلى الكأس عبر الغشاء شبه المنفذ فتقل كتلة الكيس."],
        "جزيئات السكروز لا تستطيع عبور مسام الغشاء.",
        diagram_en=_svg_osmosis_membrane("3% Bag", "12% Beaker", "97% Water", "88% Water",
                                         "97% ماء", "88% ماء", "en"),
        diagram_ar=_svg_osmosis_membrane("3% كيس", "12% كأس", "97% Water", "88% Water",
                                         "97% ماء", "88% ماء", "ar"),
    ))

    # 6 (Medium): Potato strip 20 g gains 15% -> 23 g
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        f"A fresh potato cylinder with an initial mass of {m('20')} g is submerged in hypotonic distilled water for 1 hour and gains {m(r'15\%')} in mass due to osmotic water uptake. What is its final mass (in g)?",
        f"أُغمرت قطعة بطاطس طازجة كتلتها الابتدائية {m('20')} g في ماء مقطر منخفض التركيز لمدة ساعة فازدادت كتلتها بنسبة {m(r'15\%')} بفعل الأسموزية. ما كتلتها النهائية (بالجرام)؟",
        23, [17, 21.5, 35],
        "Calculate 15% of 20 g and add it to the original 20 g.",
        "احسب 15% من 20 جراماً ثم أضفها إلى الكتلة الابتدائية 20 جراماً.",
        f"Compute {m('20 \\times (1 + 0.15)')}.",
        [f"Mass gained = {m('0.15 \\times 20 = 3')} g.",
         f"Final mass = {m('20 + 3 = 23')} g."],
        f"Check percentage change: {m(r'\frac{23 - 20}{20} = \frac{3}{20} = 15\%')}.",
        "نحسب مقدار الزيادة ونضيفه للكتلة الأصلية.",
        [f"الزيادة = {m('0.15 \\times 20 = 3')} g.",
         f"الكتلة النهائية = {m('20 + 3 = 23')} g."],
        f"التحقق: {m(r'3/20 = 15\%')}.",
    ))

    # 7 (Medium): Active vs passive antibody immunity
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        "A hiker bitten by a venomous snake receives an injection of purified <strong>antivenom antibodies</strong> rather than a vaccine. Why does antivenom act immediately yet provide only short-term protection?",
        "حُقن متنزّه لدغته أفعى بمصل جاهز يحتوي على <strong>أجسام مضادة للسم</strong> بدلاً من لقاح. لماذا يعمل المصل فوراً لكنه يوفر حماية مؤقتة فقط؟",
        [
            ("It is passive immunity: ready-made antibodies neutralize toxin immediately, but the patient forms no memory cells",
             "إنها مناعة سلبية: الأجسام المضادة الجاهزة تعادل السم فوراً، لكن جسم المريض لا يكوّن خلايا ذاكرة"),
            ("It is active immunity that destroys all B-lymphocytes permanently",
             "إنها مناعة نشطة تدمر جميع الخلايا البائية للأبد"),
            ("Antivenom antibodies replicate continuously inside red blood cells for decades",
             "تتضاعف الأجسام المضادة للمصل داخل خلايا الدم الحمراء لعقود"),
            ("Vaccines act faster than antivenom because memory cells neutralize snake venom in seconds",
             "تعمل اللقاحات أسرع من المصل في معادلة سم الأفعى خلال ثوانٍ"),
        ],
        "Contrast receiving pre-made antibodies (passive) vs training your own B-cells (active).",
        "قارن بين تلقي أجسام مضادة جاهزة (مناعة سلبية) وتدريب خلاياك على إنتاجها (مناعة نشطة).",
        "Distinguish immediate neutralization from long-term immunological memory.",
        ["Injected antivenom antibodies bind and neutralize venom toxins right away without waiting 7–14 days for the patient's B-cells.",
         "Because the patient's own lymphocytes were not stimulated to produce memory cells, protection fades once the injected proteins degrade."],
        "Maternal antibodies passed through placenta/milk are another example of passive immunity.",
        "نميز بين المعادلة الفورية والذاكرة المناعية الدائمة.",
        ["الأجسام المضادة الجاهزة ترتبط بالسم وتعطله فوراً دون انتظار استجابة الجسم.",
         "لكنها بروتينات تتحلل مع الوقت ولا تترك خلايا ذاكرة، فتكون الحماية مؤقتة."],
        "نقل الأجسام المضادة من الأم للجنين مثال آخر للمناعة السلبية.",
    ))

    # 8 (Medium): Primary vs secondary immune response graph
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        "The graph compares blood antibody levels after first exposure (Day 0) and second exposure (Day 28) to the same pathogen. What explains the much steeper, taller peak after Day 28?",
        "يقارن الرسم مستوى الأجسام المضادة في الدم بعد التعرض الأول (اليوم 0) والتعرض الثاني (اليوم 28) لمسبب المرض نفسه. ما سبب القمة الأسرع والأعلى بكثير بعد اليوم 28؟",
        [
            ("Memory B-cells from the first encounter rapidly divide and differentiate into antibody-secreting plasma cells",
             "تنقسم خلايا الذاكرة البائية بسرعة وتتمايز إلى خلايا بلازمية مفرزة للأجسام المضادة بكثافة"),
            ("The skin thickens permanently on Day 28 to produce antibodies directly",
             "يزداد سمك الجلد في اليوم 28 لينتج أجساماً مضادة مباشرة"),
            ("Red blood cells convert hemoglobin into specific viral antibodies",
             "تحول خلايا الدم الحمراء الهيموجلوبين إلى أجسام مضادة"),
            ("The second infection stimulates innate stomach acid rather than white blood cells",
             "تحفز الإصابة الثانية حمض المعدة فقط دون خلايا الدم البيضاء"),
        ],
        "Compare the lag time and peak height of primary vs secondary adaptive immunity.",
        "قارن سرعة الاستجابة وارتفاع الذروة بين المناعة الأولية والمناعة الثانوية.",
        "Link secondary response kinetics to memory lymphocytes.",
        ["During primary exposure (Day 0–14), naive B-cells must be located and cloned, producing a slow, modest peak.",
         "Memory B-cells remain circulating after Day 14, launching a faster and far stronger secondary antibody surge upon Day 28 re-exposure."],
        "This rapid secondary response usually clears pathogens before symptoms even appear.",
        "نربط الاستجابة الثانوية السريعة بوجود خلايا الذاكرة.",
        ["في التعرض الأول يستغرق تنشيط الخلايا البائية البكر وقتاً فتكون القمة أضعف.",
         "تبقى خلايا الذاكرة جاهزة لتتضاعف فوراً عند التعرض الثاني منتجة كمية ضخمة من الأجسام المضادة."],
        "غالباً تقضي المناعة الثانوية على الميكروب قبل ظهور الأعراض.",
        diagram_en=svg_motion_graph([(0, 0), (10, 20), (20, 8), (28, 8), (33, 95), (42, 60)],
                                    "Antibody", "Days", "Immune Response"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 0), (10, 20), (20, 8), (28, 8), (33, 95), (42, 60)],
                                            "Antibody", "Days", "Immune Response"),
                           {"Antibody": "الأجسام المضادة", "Days": "الأيام", "Immune Response": "الاستجابة المناعية"}),
    ))

    # 9 (Medium): U-tube level rises on 10% side
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        "A U-tube is separated at the bottom by a membrane permeable only to water. Left arm A initially holds 10% glucose solution, and right arm B holds an equal height of 4% glucose solution. After 2 hours, how will the liquid levels compare?",
        "يحتوي أنبوب على شكل حرف U على غشاء شبه منفذ للماء فقط في أسفله. يضم الذراع الأيسر (أ) محلول جلوكوز 10%، والذراع الأيمن (ب) الارتفاع نفسه من محلول 4%. بعد ساعتين، كيف يصبح ارتفاع السائلين؟",
        [
            ("Water level rises in left arm A and falls in right arm B",
             "يرتفع مستوى الماء في الذراع الأيسر (أ) وينخفض في الذراع الأيمن (ب)"),
            ("Water level rises in right arm B and falls in left arm A",
             "يرتفع مستوى الماء في الذراع الأيمن (ب) وينخفض في الأيسر (أ)"),
            ("Both liquid levels stay at exactly equal height",
             "يبقى ارتفاع السائلين متساوياً تماماً في الذراعين"),
            ("Glucose molecules migrate from A to B until levels drop equally",
             "تنتقل جزيئات الجلوكوز من (أ) إلى (ب) حتى يتساوى التركيز"),
        ],
        "Since glucose cannot pass, water moves from the more dilute side (4%) into the more concentrated side (10%).",
        "بما أن الجلوكوز لا يعبر الغشاء، ينتقل الماء من الجانب المخفف (4%) نحو المركز (10%).",
        "Determine net water flux across the U-tube divider.",
        ["Arm B (4% glucose) has higher water concentration (96% water) than Arm A (10% glucose, 90% water).",
         "Water crosses from B to A, raising the fluid column in Arm A and lowering it in Arm B."],
        "Equilibrium balances osmotic pull against hydrostatic pressure difference.",
        "نحدد اتجاه صافي تدفق الماء عبر الغشاء.",
        ["الذراع (ب) بتركيز 4% يحتوي على نسبة ماء أعلى (96%) مقارنة بالذراع (أ) (90% ماء).",
         "ينتقل الماء من (ب) إلى (أ)، فيرتفع السائل في الذراع (أ) وينخفض في (ب)."],
        "يستمر الانتقال حتى يتعادل الضغط الهيدروستاتيكي مع الجذب الأسموزي.",
        diagram_en=_svg_osmosis_membrane("10% Glucose", "4% Glucose", "Arm A", "Arm B",
                                         "الذراع أ", "الذراع ب", "en"),
        diagram_ar=_svg_osmosis_membrane("10% جلوكوز", "4% جلوكوز", "Arm A", "Arm B",
                                         "الذراع أ", "الذراع ب", "ar"),
    ))

    # 10 (Hard): Potato isotonic concentration interpolation
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        "Identical potato cores are placed in sucrose solutions of 0%, 2%, 4%, 6%, and 8%, yielding mass changes of +14%, +7%, +1.5%, -4%, and -10% respectively. Between which two sucrose concentrations does the internal <strong>isotonic</strong> solute concentration of the potato cells lie?",
        "وُضعت قطع بطاطس متماثلة في محاليل سكروز تراكيزها 0% و2% و4% و6% و8%، فكانت نسب تغير الكتلة على الترتيب: +14% و+7% و+1.5% و-4% و-10%. بين أي تركيزين يقع التركيز <strong>المتعادل أسموزياً</strong> لخلايا البطاطس؟",
        [
            ("Between 4% and 6% sucrose (closer to 4.5%)",
             "بين 4% و 6% سكروز (أقرب إلى 4.5%)"),
            ("Between 0% and 2% sucrose", "بين 0% و 2% سكروز"),
            ("Between 2% and 4% sucrose", "بين 2% و 4% سكروز"),
            ("Greater than 8% sucrose", "أعلى من 8% سكروز"),
        ],
        "At the isotonic concentration, net water movement is zero (% mass change = 0%).",
        "عند التركيز المتعادل يكون صافي حركة الماء صفراً (تغير الكتلة = 0%).",
        "Locate where % mass change crosses from positive (+) to negative (-).",
        ["At 4% sucrose, potato cores still gain slightly (+1.5%), meaning the potato interior is slightly more concentrated than 4%.",
         "At 6% sucrose, potato cores lose mass (-4%), meaning 6% is hypertonic; thus 0% mass change lies between 4% and 6% (~4.5%)."],
        "Zero-crossing interpolation is standard lab analysis for cellular osmolarity.",
        "نبحث عن الموضع الذي ينتقل فيه تغير الكتلة من موجب (+) إلى سالب (-).",
        ["عند 4% تزداد الكتلة (+1.5%) أي أن الخلية ما زالت أعلى تركيزاً من 4%.",
         "وعند 6% تنقص الكتلة (-4%)، إذن نقطة الصفر (التعادل) تقع بين 4% و 6%."],
        "الاستيفاء عند الصفر يحدد الأسموزية الداخلية للخلية.",
        diagram_en=svg_motion_graph([(0, 14), (2, 7), (4, 1.5), (6, -4), (8, -10)],
                                    "% Mass", "Sucrose %", "Osmosis Curve"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 14), (2, 7), (4, 1.5), (6, -4), (8, -10)],
                                            "% Mass", "Sucrose %", "Osmosis Curve"),
                           {"% Mass": "% الكتلة", "Sucrose %": "% السكروز", "Osmosis Curve": "منحنى الأسموزية"}),
    ))

    # 11 (Hard): Quantitative U-tube osmotic equilibrium (50 mL moved)
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        f"Left chamber A contains {m('100')} mL of solution holding {m('6')} g of dissolved sugar, and right chamber B contains {m('100')} mL holding {m('2')} g of sugar. Only water can cross the membrane (ignore gravity). How many mL of water move from B to A until both chambers reach equal sugar concentration?",
        f"يحتوي الحيز الأيسر (أ) على {m('100')} mL من محلول يذوب فيه {m('6')} g سكر، والحيز الأيمن (ب) على {m('100')} mL يذوب فيه {m('2')} g سكر. يسمح الغشاء بمرور الماء فقط (بإهمال الجاذبية). كم مليلتراً من الماء ينتقل من (ب) إلى (أ) حتى يتساوى التركيز في الحيزين؟",
        50, [25, 40, 75],
        "Total water+volume stays 200 mL and total sugar stays 8 g; at equilibrium both sides match the overall 8 g / 200 mL concentration.",
        "يبقى الحجم الكلي 200 mL والكتلة الكلية للسكر 8 g؛ عند التوازن يصبح تركيز كل جهة مساوياً للتركيز الكلي 8g في 200mL.",
        f"Solve {m(r'\frac{6}{100 + x} = \frac{2}{100 - x}')}.",
        [f"Let {m('x')} mL move from B to A. Equal concentration requires {m(r'\frac{6}{100 + x} = \frac{2}{100 - x}')}.",
         f"Cross-multiplying gives {m('6(100 - x) = 2(100 + x)')}, so {m('600 - 6x = 200 + 2x')} and {m('8x = 400')}.",
         f"Solving gives {m('x = 50')} mL."],
        f"Check: A has {m('6 / 150 = 0.04')} g/mL and B has {m('2 / 50 = 0.04')} g/mL.",
        "نساوي التركيز النهائي في الجهتين بعد انتقال x مليلتر من الماء.",
        [f"نفرض انتقال {m('x')} mL من (ب) إلى (أ)، فيتساوى التركيز: {m(r'\frac{6}{100 + x} = \frac{2}{100 - x}')}.",
         f"بالضرب التبادلي: {m('600 - 6x = 200 + 2x')} ومنه {m('8x = 400')}.",
         f"إذن {m('x = 50')} mL."],
        f"التحقق: {m('6/150 = 2/50 = 0.04')} g/mL في الجهتين.",
    ))

    # 12 (Hard): Why medical IV drips use 0.9% isotonic saline
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        "Why do hospitals administer intravenous (IV) fluids using 0.9% NaCl saline rather than pure sterile water?",
        "لماذا تستخدم المستشفيات المحاليل الوريدية بتركيز 0.9% كلوريد صوديوم (محلول ملحي فسيولوجي) بدلاً من الماء المقطر النقي؟",
        [
            ("0.9% NaCl is isotonic to blood cells, preventing osmotic lysis (bursting) or crenation (shrinking)",
             "لأن تركيز 0.9% متعادل أسموزياً مع خلايا الدم، فيمنع انفجارها أو انكماشها"),
            ("Pure water cannot dissolve glucose or medical antibiotics",
             "لأن الماء النقي لا يستطيع إذابة الجلوكوز أو المضادات الحيوية"),
            ("0.9% NaCl is strongly hypertonic so it shrinks all white blood cells rapidly",
             "لأن محلول 0.9% مرتفع التركيز جداً فيقلص خلايا الدم البيضاء سريعاً"),
            ("Red blood cells possess thick cellulose walls that block pure water completely",
             "لأن خلايا الدم الحمراء تمتلك جداراً سليلوزياً سميكاً يمنع دخول الماء"),
        ],
        "Red blood cells have roughly 0.9% internal dissolved solute equivalent.",
        "التركيز الداخلي لخلايا الدم الحمراء يعادل تقريباً 0.9% ملحاً.",
        "Predict red blood cell fate in pure water vs 0.9% saline vs 5% saline.",
        ["Pure water (0% solute) is hypotonic, causing water to rush into red blood cells until they burst (hemolysis).",
         "0.9% saline matches blood plasma osmolarity (isotonic), keeping net water flux zero and cell shape intact."],
        "5% saline would be hypertonic, pulling water out and shriveling red blood cells.",
        "نقارن أثر الماء النقي والمحلول المتعادل والمرتفع التركيز في كريات الدم.",
        ["الماء النقي (0%) منخفض التركيز فيدخل الكريات الحمراء بالأسموزية حتى تنفجر.",
         "المحلول 0.9% متعادل التركيز مع البلازما فيحفظ توازن الماء وشكل الخلايا."],
        "المحلول الأعلى تركيزاً يسحب الماء من الكريات فتنكمش.",
    ))

    # 13 (Hard): Antigen specificity of antibodies
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        "A student recovers completely from measles and develops lifelong measles immunity, yet catches influenza later the same year. Why did measles antibodies fail to stop the influenza virus?",
        "تَعافى طالب من الحصبة واكتسب مناعة طويلة الأمد ضدها، لكنه أُصيب بالإنفلونزا في العام نفسه. لماذا لم تحمِه الأجسام المضادة للحصبة من فيروس الإنفلونزا؟",
        [
            ("Adaptive antibodies and memory B-cell receptors bind specifically to complementary three-dimensional surface antigens unique to each virus",
             "لأن الأجسام المضادة ومستقبلات خلايا الذاكرة ترتبط بنوعية دقيقة بمستضدات سطحية ثلاثية الأبعاد خاصة بكل فيروس"),
            ("Measles antibodies only operate in the stomach and cannot reach the lungs",
             "لأن أجسام الحصبة المضادة تعمل في المعدة فقط ولا تصل للرئتين"),
            ("Influenza viruses are bacteria, so viral memory cells ignore them",
             "لأن الإنفلونزا بكتيريا تتجاهلها خلايا الذاكرة الفيروسية"),
            ("Memory B-cells are deleted from bone marrow after three months",
             "لأن خلايا الذاكرة البائية تتحلل في نخاع العظم بعد ثلاثة أشهر"),
        ],
        "Think about the lock-and-key molecular specificity of adaptive immunity.",
        "فكّر في مبدأ القفل والمفتاح الدقيق في المناعة المكتسبة.",
        "Explain clonal selection and antigen-binding site shape.",
        ["Each antibody has variable binding tips shaped specifically for one pathogen's surface antigen (like a lock and key).",
         "Influenza carries completely different surface proteins (hemagglutinin/neuraminidase) that measles antibodies cannot bind."],
        "Each distinct pathogen requires its own specific B-cell and T-cell clone.",
        "نوضح تخصص موقع الارتباط على الجسم المضاد.",
        ["كل جسم مضاد يمتلك موقع ارتباط ذا شكل هندسي يطابق مستضداً محدداً فقط كالقفل والمفتاح.",
         "يحمل فيروس الإنفلونزا بروتينات سطحية مختلفة كلياً عن فيروس الحصبة."],
        "لذا يتطلب كل مسبب مرضي استنساخ خلايا مناعية خاصة به.",
    ))

    # 14 (Hard): Fertilizer burn / seawater plasmolysis in plant roots
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        "A farmer accidentally applies an overly concentrated chemical fertilizer solution around tomato roots, and the plants wilt severely within hours despite wet soil. What cellular process caused the wilting?",
        "أضاف مزارع محلول سماد كيميائياً عالي التركيز حول جذور الطماطم، فذبلت النباتات بشدة خلال ساعات رغم رطوبة التربة. ما العملية الخلوية التي سببت الذبول؟",
        [
            ("Hypertonic soil water pulled water out of root cells by osmosis (plasmolysis), reducing turgor pressure",
             "سحب ماء التربة المرتفع التركيز الماء من خلايا الجذر بالأسموزية (البلزمة) فانخفض ضغط الامتلاء"),
            ("Root hair cells absorbed excess fertilizer by active transport and burst open",
             "امتصت خلايا الجذر السماد الزائد بالنقل النشط فانفجرت"),
            ("Fertilizer blocked sunlight from reaching root chloroplasts",
             "منع السماد وصول ضوء الشمس إلى بلاستيدات الجذور"),
            ("Root membranes converted cellulose cell walls into salt crystals",
             "حوّلت أغشية الجذر الجدار السليلوزي إلى بلورات ملحية"),
        ],
        "Compare solute concentration of the wet soil water vs inside the root cells.",
        "قارن تركيز المذاب في التربة الرطبة مع داخل خلايا الجذر.",
        "Apply osmosis under hypertonic soil salinity.",
        ["Excess dissolved fertilizer salts make the soil solution hypertonic relative to root hair cytoplasm.",
         "Water leaves the root cells by osmosis, causing vacuoles to shrink and membranes to pull away from cell walls (plasmolysis), leading to wilting."],
        "Flushing the soil with fresh water reverses the gradient before cells die.",
        "نطبّق قاعدة الأسموزية في محلول عالي التركيز.",
        ["تزيد الأملاح المذابة تركيز محلول التربة فوق تركيز سيتوبلازم الجذر.",
         "يخرج الماء من الجذور إلى التربة بالأسموزية (البلزمة) فيفقد النبات ضغط الامتلاء ويذبل."],
        "غسل التربة بالماء العذب يعيد التدرج الأسموزي الطبيعي.",
    ))
    return qs


def _gen_sci_b05(start_idx: int) -> list[dict]:
    """G9-SCI-B05: 10% trophic energy pyramids & carbon/nitrogen cycles."""
    bp = "G9-SCI-B05"
    qs: list[dict] = []

    # 0 (Easy): Standard 10% energy pyramid forward (10,000 -> 100 J)
    qs.append(make_science_math_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        f"In the desert energy pyramid, producers (grasses) capture {m('10,000')} J of usable energy. Assuming the {m(r'10\%')} ecological transfer rule at every step, how many joules reach the <strong>secondary consumers</strong> (snakes)?",
        f"في هرم الطاقة الصحراوي، يختزن المنتج (الأعشاب) {m('10,000')} J من الطاقة القابلة للانتقال. بافتراض قاعدة انتقال {m(r'10\%')} في كل مستوى، كم جولاً يصل إلى <strong>المستهلكات الثانوية</strong> (الأفاعي)؟",
        100, [10, 1000, 9000],
        "Multiply by 0.10 twice: Producers → Primary Consumers → Secondary Consumers.",
        "اضرب في 0.10 مرتين: من المنتج ← المستهلك الأول ← المستهلك الثاني.",
        f"Compute {m('10,000 \\times 0.10 \\times 0.10')}.",
        [f"Primary consumers (mice) receive {m('10\\% \\times 10,000 = 1,000')} J.",
         f"Secondary consumers (snakes) receive {m('10\\% \\times 1,000 = 100')} J."],
        f"Hawks (tertiary) receive {m('10')} J, matching the pyramid.",
        "نطبّق قاعدة العُشر مرتين متتاليتين.",
        [f"المستهلك الأول (الفئران) يحصل على {m('10\\% \\times 10,000 = 1,000')} J.",
         f"المستهلك الثاني (الأفاعي) يحصل على {m('10\\% \\times 1,000 = 100')} J."],
        f"يصل إلى الصقر (الثالث) {m('10')} J فقط.",
        diagram_en=svg_energy_pyramid([("Hawk", "10 J"), ("Snake", "? J"), ("Mouse", "1,000 J"), ("Grass", "10,000 J")],
                                      "10% Energy Pyramid"),
        diagram_ar=_ar_svg(svg_energy_pyramid([("Hawk", "10 J"), ("Snake", "? J"), ("Mouse", "1,000 J"), ("Grass", "10,000 J")],
                                              "10% Energy Pyramid"),
                           {"Hawk": "صقر", "Snake": "أفعى", "Mouse": "فأر", "Grass": "أعشاب",
                            "10% Energy Pyramid": "هرم الطاقة (10%)"}),
    ))

    # 1 (Easy): Where the remaining 90% goes
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        "Only about 10% of the energy at one trophic level is stored in biomass for the next consumer level. What happens to most of the remaining ~90%?",
        "ينتقل نحو 10% فقط من طاقة المستوى الغذائي إلى المستوى الأعلى. أين يذهب معظم الـ 90% المتبقية؟",
        [
            ("Used by organisms for cellular respiration and life activities, and dissipated to the environment as heat",
             "يُستهلك في التنفس الخلوي والأنشطة الحيوية ويتبدد في البيئة على شكل حرارة"),
            ("Destroyed completely, violating conservation of energy",
             "يفنى تماماً ولا يتحول إلى أي شكل آخر"),
            ("Stored permanently as pure nuclear energy in animal bones",
             "يُخزن دائماً كطاقة نووية في عظام الحيوانات"),
            ("Converted back into sunlight and radiated back to the Sun",
             "يتحول إلى ضوء شمس ويعود نحو الشمس"),
        ],
        "Energy cannot be destroyed, yet biological metabolism releases thermal energy at each step.",
        "الطاقة لا تفنى، لكن العمليات الحيوية والتنفس الخلوي تطلق طاقة حرارية.",
        "Account for respiration, undigested waste, and thermal dissipation.",
        ["Organisms burn most assimilated food in cellular respiration to move, grow, and maintain body functions.",
         "Inefficient heat transfer radiates ~90% as thermal energy and indigestible waste goes to decomposers."],
        "Total energy is conserved, just converted into non-reusable heat.",
        "نتتبع مصير الطاقة عبر التنفس والحرارة والفضلات.",
        ["تستهلك الكائنات معظم الغذاء في التنفس الخلوي والحركة والنمو.",
         "يتبدد نحو 90% كطاقة حرارية غير قابلة لإعادة الاستخدام الغذائي، ويذهب بعضه للمحللات."],
        "هذا يوافق قانون حفظ الطاقة.",
    ))

    # 2 (Easy): Nitrogen-fixing bacteria
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        "Atmospheric air is 78% nitrogen gas (N₂), yet plants cannot absorb N₂ directly through their leaves. Which organisms convert N₂ into usable ammonia (NH₃) for plants?",
        "يشكّل غاز النيتروجين (N₂) نحو 78% من الهواء، لكن النباتات لا تمتصه مباشرة. ما الكائنات التي تحول النيتروجين الجوي إلى أمونيا (NH₃) صالحة لامتصاص النبات؟",
        [
            ("Nitrogen-fixing bacteria in soil and legume root nodules",
             "البكتيريا المثبتة للنيتروجين في التربة والعقد الجذرية للبقوليات"),
            ("Herbivores grazing on desert shrubs",
             "آكلات الأعشاب التي ترعى الشجيرات الصحراوية"),
            ("Photosynthetic algae releasing pure O₂ gas",
             "الطحالب الخضراء التي تطلق غاز الأكسجين"),
            ("Viruses infecting pine tree needles",
             "الفيروسات التي تصيب أوراق الصنوبر"),
        ],
        "Look for symbiotic soil microbes living inside root nodules of beans, alfalfa, and lentils.",
        "ابحث عن الميكروبات المتعايشة في العقد الجذرية للفول والبرسيم والعدس.",
        "Identify biological nitrogen fixation.",
        ["The strong N≡N triple bond cannot be broken by plant enzymes.",
         "Nitrogen-fixing bacteria (such as Rhizobium) possess nitrogenase enzymes that fix N₂ into ammonia/ammonium ions."],
        "Nitrifying bacteria then convert ammonium into nitrates (NO₃⁻) readily absorbed by roots.",
        "نحدد البكتيريا القادرة على تفكيك رابطة N₂ الثلاثية.",
        ["لا تستطيع إنزيمات النبات كسر الرابطة الثلاثية القوية في غاز النيتروجين.",
         "تمتلك البكتيريا المثبتة للنيتروجين إنزيماً يحول N₂ إلى أمونيا تستفيد منها الجذور."],
        "بعدها تحول بكتيريا النترتة الأمونيا إلى نترات سهلة الامتصاص.",
    ))

    # 3 (Easy): Carbon cycle photosynthesis vs respiration
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        "Which pair of biological processes moves carbon in <strong>opposite</strong> directions between atmospheric CO₂ and organic glucose?",
        "أي زوج من العمليات الحيوية ينقل الكربون في <strong>اتجاهين متعاكسين</strong> بين ثاني أكسيد الكربون الجوي والجلوكوز العضوي؟",
        [
            ("Photosynthesis removes atmospheric CO₂; cellular respiration releases CO₂ back to the air",
             "البناء الضوئي يسحب CO₂ من الجو، والتنفس الخلوي يعيد إطلاق CO₂ إلى الهواء"),
            ("Both photosynthesis and respiration permanently lock CO₂ underground as coal",
             "كلا العمليتين تحبسان CO₂ دائماً تحت الأرض كفحم حجري"),
            ("Transpiration absorbs CO₂ while nitrogen fixation breaks down glucose",
             "النتح يمتص CO₂ بينما تثبيت النيتروجين يحلل الجلوكوز"),
            ("Photosynthesis releases CO₂ while combustion removes CO₂ from air",
             "البناء الضوئي يطلق CO₂ والاحتراق يسحب CO₂ من الهواء"),
        ],
        "Think about the balanced chemical equations of chloroplasts vs mitochondria.",
        "قارن بين معادلة البناء الضوئي ومعادلة التنفس الخلوي.",
        "Contrast carbon uptake (producers) with carbon emission (all living cells).",
        ["Photosynthesis fixes CO₂ + H₂O into C₆H₁₂O₆ + O₂ using sunlight.",
         "Cellular respiration oxidizes C₆H₁₂O₆ + O₂ back into CO₂ + H₂O + ATP."],
        "Fossil fuel burning accelerates CO₂ return faster than photosynthesis/oceans absorb it.",
        "نقارن تثبيت الكربون بإطلاقه.",
        ["البناء الضوئي يثبت CO₂ والماء لتكوين الجلوكوز وإطلاق الأكسجين.",
         "التنفس الخلوي يؤكسد الجلوكوز مطلقاً CO₂ وماءً وطاقة."],
        "حرق الوقود الأحفوري يزيد إطلاق CO₂ فوق قدرة الامتصاص.",
    ))

    # 4 (Easy): Role of decomposers
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "If all saprophytic bacteria and fungi (decomposers) suddenly vanished from an ecosystem, what immediate crisis would disrupt the carbon and nitrogen cycles?",
        "لو اختفت جميع البكتيريا والفطريات المحللة فجأة من نظام بيئي، ما الخلل الفوري الذي يصيب دورتي الكربون والنيتروجين؟",
        [
            ("Dead organisms would pile up and mineral nutrients (nitrates, carbon) would stay locked out of soil and producers",
             "تتراكم الجثث والمواد الميتة وتنحبس المغذيات المعدنية كالنترات والكربون عن التربة والمنتجات"),
            ("Herbivores would immediately begin performing photosynthesis",
             "تبدأ آكلات الأعشاب فوراً بالقيام بعملية البناء الضوئي"),
            ("Atmospheric nitrogen gas would disappear within minutes",
             "يختفي غاز النيتروجين من الغلاف الجوي خلال دقائق"),
            ("Energy pyramids would invert so apex predators store 100 times more energy than plants",
             "ينقلب هرم الطاقة فتخزن المفترسات طاقة أكبر 100 مرة من النباتات"),
        ],
        "Decomposers are nature's recyclers returning matter from dead biomass back to soil and air.",
        "المحللات هي المسؤولة عن إعادة تدوير المادة من البقايا الميتة إلى التربة والهواء.",
        "Identify the matter-recycling bridge between dead consumers and living producers.",
        ["Unlike energy (which flows one-way), chemical matter (C, N, P) must be recycled.",
         "Without decomposers, nutrients remain trapped in dead tissues and plant growth quickly stalls."],
        "Energy enters from sunlight; matter cycles continuously via decomposers.",
        "نفصل بين مسار الطاقة أحادي الاتجاه ودورة المادة المغلقة.",
        ["الطاقة تتدفق باتجاه واحد من الشمس، بينما العناصر كالكربون والنيتروجين يجب أن تُعاد تدويرها.",
         "بغياب المحللات تُحتجز المغذيات في البقايا الميتة وتتوقف النباتات عن النمو."],
        "المحللات تغلق دورة المادة في النظام البيئي.",
    ))

    # 5 (Medium): Backward 10% pyramid calculation (45 J -> 45,000 J)
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        f"In an Arabian Gulf marine food chain (Phytoplankton → Zooplankton → Small Fish → Barracuda), the top barracuda population (level 4) holds {m('45')} kJ of energy. Using the {m(r'10\%')} rule at each transfer, how many kJ did the phytoplankton (producers) originally fix?",
        f"في سلسلة غذائية بحرية بالخليج العربي (عوالق نباتية ← عوالق حيوانية ← أسماك صغيرة ← باراكودا)، تختزن أسماك الباراكودا (المستوى الرابع) طاقة مقدارها {m('45')} kJ. وفق قاعدة الـ {m(r'10\%')} في كل خطوة، كم كيلوجولاً اختزنته العوالق النباتية (المنتجات) أصلاً؟",
        45000, [450, 4500, 450000],
        "Going down 3 trophic steps multiplies energy by 10 three times (× 1,000).",
        "النزول 3 مستويات غذائية إلى القاعدة يضرب الطاقة في 10 ثلاث مرات (× 1,000).",
        f"Compute {m('45 \\times 10^3')}.",
        [f"Level 3 (small fish): {m('45 \\times 10 = 450')} kJ.",
         f"Level 2 (zooplankton): {m('450 \\times 10 = 4,500')} kJ; Level 1 (phytoplankton): {m('4,500 \\times 10 = 45,000')} kJ."],
        f"Forward check: {m('45,000 \\to 4,500 \\to 450 \\to 45')} kJ.",
        "نصعد بالضرب في 10 عبر ثلاثة مستويات للعودة إلى المنتج.",
        [f"الأسماك الصغيرة: {m('45 \\times 10 = 450')} kJ.",
         f"العوالق الحيوانية: {m('4,500')} kJ، والعوالق النباتية: {m('45,000')} kJ."],
        f"التحقق للأمام: {m('45,000 \\to 4,500 \\to 450 \\to 45')}.",
        diagram_en=svg_energy_pyramid([("Barracuda", "45 kJ"), ("Small Fish", "?"), ("Zooplankton", "?"), ("Phytoplankton", "? kJ")],
                                      "Marine Energy Pyramid"),
        diagram_ar=_ar_svg(svg_energy_pyramid([("Barracuda", "45 kJ"), ("Small Fish", "?"), ("Zooplankton", "?"), ("Phytoplankton", "? kJ")],
                                              "Marine Energy Pyramid"),
                           {"Barracuda": "باراكودا", "Small Fish": "أسماك صغيرة",
                            "Zooplankton": "عوالق حيوانية", "Phytoplankton": "عوالق نباتية",
                            "Marine Energy Pyramid": "هرم الطاقة البحري"}),
    ))

    # 6 (Medium): Custom transfer efficiencies (12% then 8%)
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        f"Producers in an Asir highland meadow store {m('25,000')} kJ. Herbivores assimilate {m(r'12\%')} of producer energy, and carnivores assimilate {m(r'8\%')} of herbivore energy. How many kJ reach the carnivores?",
        f"تختزن المنتجات في مرج بمرتفعات عسير {m('25,000')} kJ. تكتسب آكلات الأعشاب {m(r'12\%')} من طاقة المنتجات، وتكتسب آكلات اللحوم {m(r'8\%')} من طاقة آكلات الأعشاب. كم كيلوجولاً يصل إلى آكلات اللحوم؟",
        240, [300, 2000, 3000],
        "Apply 12% first to find herbivore energy, then take 8% of that result.",
        "احسب 12% أولاً لإيجاد طاقة آكلات الأعشاب، ثم احسب 8% من الناتج.",
        f"Compute {m('25,000 \\times 0.12 \\times 0.08')}.",
        [f"Herbivore energy = {m('25,000 \\times 0.12 = 3,000')} kJ.",
         f"Carnivore energy = {m('3,000 \\times 0.08 = 240')} kJ."],
        f"Combined efficiency is {m(r'0.12 \times 0.08 = 0.0096 = 0.96\%')}, and {m('0.0096 \\times 25,000 = 240')}.",
        "نضرب في النسبتين على التوالي.",
        [f"طاقة آكلات الأعشاب = {m('25,000 \\times 0.12 = 3,000')} kJ.",
         f"طاقة آكلات اللحوم = {m('3,000 \\times 0.08 = 240')} kJ."],
        f"الكفاءة الكلية {m(r'0.96\%')} وتعطي {m('240')} kJ.",
    ))

    # 7 (Medium): Why food chains rarely exceed 4-5 levels
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        "Why do terrestrial food chains rarely support more than 4 or 5 trophic levels?",
        "لماذا نادراً ما تتجاوز السلاسل الغذائية البرية 4 أو 5 مستويات غذائية؟",
        [
            ("Because ~90% of energy is lost at every transfer, leaving too little usable energy above level 4–5 to sustain a viable population",
             "لأن فقدان نحو 90% من الطاقة عند كل انتقال يُبقي طاقة ضئيلة جداً بعد المستوى 4 أو 5 لا تكفي لإعالة جماعة حيوية"),
            ("Because apex predators cannot digest proteins from secondary consumers",
             "لأن المفترسات العليا تعجز عن هضم بروتينات المستهلكات الثانوية"),
            ("Because sunlight only reaches the first two trophic levels directly",
             "لأن ضوء الشمس لا يصل إلا لأول مستويين غذائيين فقط"),
            ("Because the carbon cycle stops completely at the fourth consumer",
             "لأن دورة الكربون تتوقف تماماً عند المستهلك الرابع"),
        ],
        "Think about what remains after dividing by 10 four or five times in a row.",
        "فكّر في مقدار الطاقة المتبقي بعد القسمة على 10 أربع أو خمس مرات متتالية.",
        "Connect exponential 90% loss to minimum viable predator biomass.",
        ["After 4 transfers at 10% efficiency, only 0.01% (1/10,000) of original plant energy remains.",
         "There is insufficient energy left to support active hunting and reproduction of a 6th-level predator."],
        "This also explains why apex predators have much smaller populations than herbivores.",
        "نربط الفقد الأسي للطاقة بقدرة إعالة المفترسات.",
        ["بعد 4 انتقالات بنسبة 10% يبقى جزء من عشرة آلاف فقط من طاقة النباتات.",
         "لا تكفي هذه الطاقة الضئيلة لإعالة مفترسات مستوى سادس وتكاثرها."],
        "ولهذا يكون عدد المفترسات العليا أقل بكثير من آكلات الأعشاب.",
        diagram_en=svg_energy_pyramid([("L4: 10 J", "0.1%"), ("L3: 100 J", "1%"), ("L2: 1,000 J", "10%"), ("L1: 10,000 J", "100%")],
                                      "Trophic Attenuation"),
        diagram_ar=_ar_svg(svg_energy_pyramid([("L4: 10 J", "0.1%"), ("L3: 100 J", "1%"), ("L2: 1,000 J", "10%"), ("L1: 10,000 J", "100%")],
                                              "Trophic Attenuation"),
                           {"Trophic Attenuation": "تضاؤل الطاقة الغذائية"}),
    ))

    # 8 (Medium): Denitrification in waterlogged soil
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        "Over-irrigated, poorly drained soil often becomes oxygen-depleted (anaerobic), causing anaerobic <strong>denitrifying bacteria</strong> to multiply. How does this hurt crop yields?",
        "تصبح التربة المغدقة بالري وسيئة الصرف فقيرة بالأكسجين (لا هوائية)، فتنشط فيها <strong>بكتيريا نزع النترتة</strong> اللاهوائية. كيف يضر ذلك بمحصول النباتات؟",
        [
            ("Denitrifying bacteria convert usable soil nitrates (NO₃⁻) back into atmospheric N₂ gas, depleting soil fertility",
             "تحول بكتيريا نزع النترتة نترات التربة الصالحة للامتصاص (NO₃⁻) إلى غاز N₂ يتصاعد للهواء فتفقر التربة"),
            ("Denitrifying bacteria fix extra N₂ into toxic liquid ammonia inside leaves",
             "تثبت بكتيريا نزع النترتة غاز N₂ بكثرة داخل الأوراق"),
            ("They oxidize all soil glucose into cellulose crystals",
             "تؤكسد جميع سكريات التربة إلى بلورات سليلوز"),
            ("They turn soil water into concentrated hydrochloric acid",
             "تحول ماء التربة إلى حمض هيدروكلوريك مركز"),
        ],
        "Contrast nitrification (ammonia → nitrates for plants) with denitrification (nitrates → N₂ gas).",
        "قارن بين النترتة (تكوين نترات للتربة) ونزع النترتة (إرجاع النترات إلى غاز N₂).",
        "Trace the nitrogen loss pathway in anaerobic soil.",
        ["Plants rely on dissolved soil nitrate (NO₃⁻) and ammonium (NH₄⁺) to synthesize amino acids and DNA.",
         "In oxygen-poor mud, denitrifying bacteria strip oxygen from NO₃⁻, releasing N₂ gas to the atmosphere."],
        "Proper soil aeration keeps nitrifying bacteria active and reduces denitrification.",
        "نتتبع فقدان النترات في التربة سيئة التهوية.",
        ["تحتاج النباتات إلى النترات الذائبة لبناء البروتينات والحمض النووي.",
         "في غياب الأكسجين تسحب البكتيريا النازعة للنيتروجين الأكسجين من NO₃⁻ وتطلق N₂ للجو."],
        "تهوية التربة وتحسين الصرف يقللان فقدان النيتروجين.",
    ))

    # 9 (Medium): Net carbon budget calculation
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        f"In one year, a regional forest absorbs {m('420')} tons of CO₂ via photosynthesis, releases {m('290')} tons via plant and decomposer respiration, and nearby traffic emits {m('180')} tons. What is the <strong>net change</strong> (in tons) of atmospheric CO₂ in this region?",
        f"في سنة واحدة، تمتص غابة إقليمية {m('420')} طناً من CO₂ بالبناء الضوئي، وتطلق {m('290')} طناً عبر تنفس النباتات والمحللات، وتنبعث {m('180')} طناً من المركبات المجاورة. ما <strong>التغير الصافي</strong> (بالطن) في CO₂ الجوي لهذه المنطقة؟",
        50, [-50, 130, 890],
        "Add all CO₂ emissions (respiration + traffic) and subtract CO₂ uptake (photosynthesis).",
        "اجمع كل انبعاثات CO₂ (التنفس + المركبات) ثم اطرح كمية الامتصاص (البناء الضوئي).",
        f"Compute {m('(290 + 180) - 420')}.",
        [f"Total CO₂ emitted to the air = {m('290 + 180 = 470')} tons.",
         f"Total CO₂ removed by photosynthesis = {m('420')} tons.",
         f"Net atmospheric CO₂ change = {m('470 - 420 = +50')} tons."],
        "Positive +50 tons means emissions exceeded absorption, adding net carbon to the air.",
        "نطرح الامتصاص من إجمالي الانبعاثات.",
        [f"إجمالي المنبعث للجو = {m('290 + 180 = 470')} طناً.",
         f"الممتص بالبناء الضوئي = {m('420')} طناً.",
         f"الصافي = {m('470 - 420 = 50')} طناً زيادة في الجو."],
        "النتيجة الموجبة تعني زيادة صافية في ثاني أكسيد الكربون الجوي.",
    ))

    # 10 (Hard): Split-diet food web energy calculation
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        f"In a desert food web, a fox eats {m('4,000')} J worth of herbivores (level 2) and {m('1,500')} J worth of insectivorous lizards (level 3). If the fox assimilates {m(r'10\%')} of all energy it consumes, and simultaneously plants originally had to supply energy at {m(r'10\%')} transfer per step, wait: how many joules of <strong>producer (plant) energy</strong> were required to support just the fox's {m('1,500')} J lizard meal?",
        f"في شبكة غذائية صحراوية، تتغذى سحلية آكلة حشرات (مستوى 3) في سلسلة بنسبة انتقال {m(r'10\%')} في كل خطوة. إذا استهلك ثعلب سحالي تختزن {m('1,500')} J، فكم جولاً من طاقة <strong>النباتات المنتجة</strong> (المستوى 1) لزم أصلاً لإنتاج تلك الـ {m('1,500')} J من السحالي؟",
        150000, [15000, 1500000, 30000],
        "Lizards are at trophic level 3 (Plants → Insects → Lizards), which is 2 steps above plants.",
        "تقع السحالي في المستوى الثالث (نبات ← حشرة ← سحلية)، أي خطوتين فوق النباتات.",
        f"Multiply {m('1,500')} by {m('10^2 = 100')}.",
        [f"Insects (level 2) needed {m('1,500 \\times 10 = 15,000')} J to support {m('1,500')} J of lizards.",
         f"Plants (level 1) needed {m('15,000 \\times 10 = 150,000')} J to support {m('15,000')} J of insects."],
        f"Check: {m('150,000 \\xrightarrow{10\\%} 15,000 \\xrightarrow{10\\%} 1,500')} J.",
        "نرجع مستويين للخلف بالضرب في 10 مرتين.",
        [f"تحتاج السحالي ({m('1,500')} J) إلى {m('15,000')} J في مستوى الحشرات.",
         f"وتحتاج الحشرات إلى {m('15,000 \\times 10 = 150,000')} J من النباتات."],
        f"التحقق: {m('150,000 \\to 15,000 \\to 1,500')} J.",
    ))

    # 11 (Hard): Biomagnification vs Energy Pyramid
    qs.append(make_science_concept_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        "In a polluted coastal food web, usable <strong>energy</strong> drops by 90% at each trophic step, yet the concentration of persistent fat-soluble <strong>mercury</strong> increases dramatically from algae to fish-eating ospreys. Why do energy and toxin concentrations move in opposite directions?",
        "في شبكة غذائية ساحلية ملوثة، تقل <strong>الطاقة</strong> المتاحة بنسبة 90% عند كل مستوى، بينما يرتفع تركيز <strong>الزئبق</strong> الذائب في الدهون بشكل حاد من الطحالب إلى الطيور المفترسة. لماذا يتجهان في اتجاهين متعاكسين؟",
        [
            ("Energy is respired away as heat at each level, whereas fat-soluble toxins are neither respired nor excreted, accumulating from many prey into top predators",
             "الطاقة تُستهلك وتُفقد كحرارة في التنفس عند كل مستوى، بينما لا يتحلل السم ولا يُطرح فيتراكم من مئات الفرائس في جسم المفترس الأعلى"),
            ("Apex predators synthesize mercury inside their livers from sunlight",
             "المفترسات العليا تصنّع الزئبق داخل أكبادها من ضوء الشمس"),
            ("Bacteria pump toxins downward from predators back into phytoplankton",
             "تضخ البكتيريا السموم للأسفل من المفترسات إلى الطحالب"),
            ("Mercury multiplies its atomic mass during cellular respiration",
             "يتضاعف الوزن الذري للزئبق أثناء التنفس الخلوي"),
        ],
        "Compare biodegradable/respired energy with persistent non-degradable toxins (biomagnification).",
        "قارن بين الطاقة المستهلكة حرارياً والسموم الثابتة غير القابلة للتحلل (التراكم الحيوي).",
        "Explain biological magnification across trophic biomass compression.",
        ["Because ~90% of eaten biomass is respired to CO₂/H₂O, a predator must eat ~10 kg of prey to build 1 kg of predator tissue.",
         "All persistent mercury stored in that 10 kg of prey remains trapped in the predator's 1 kg of fat/tissue, concentrating ~10× per level."],
        "Energy dissipates upward; persistent toxins concentrate upward (biomagnification).",
        "نفسر ظاهرة التضخم الحيوي عبر تركز الكتلة.",
        ["لإنتاج 1 كجم من لحم المفترس عليه أكل نحو 10 كجم من الفرائس لأن معظم الغذاء يحترق في التنفس.",
         "الزئبق الموجود في 10 كجم من الفرائس لا يتحلل ولا يخرج، فيتركز كله في 1 كجم من جسم المفترس."],
        "الطاقة تتناقص صعوداً بينما السموم الثابتة تتركز صعوداً.",
        diagram_en=svg_energy_pyramid([("Osprey", "10 ppm"), ("Big Fish", "1 ppm"), ("Small Fish", "0.1 ppm"), ("Algae", "0.01 ppm")],
                                      "Biomagnification (ppm)"),
        diagram_ar=_ar_svg(svg_energy_pyramid([("Osprey", "10 ppm"), ("Big Fish", "1 ppm"), ("Small Fish", "0.1 ppm"), ("Algae", "0.01 ppm")],
                                              "Biomagnification (ppm)"),
                           {"Osprey": "نسر بحري", "Big Fish": "سمك كبير", "Small Fish": "سمك صغير",
                            "Algae": "طحالب", "Biomagnification (ppm)": "التضخم الحيوي (ppm)"}),
    ))

    # 12 (Hard): Crop rotation with legumes
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        "A farmer rotates wheat fields every other season with alfalfa (a legume) rather than growing wheat continuously. How does this practice naturally reduce the need for synthetic nitrogen fertilizer?",
        "يتبع مزارع دورة زراعية يزرع فيها القمح موسماً والبرسيم (من البقوليات) موسماً آخر بدلاً من زراعة القمح باستمرار. كيف يقلل هذا التدوير الحاجة إلى الأسمدة النيتروجينية الصناعية؟",
        [
            ("Symbiotic Rhizobium bacteria in legume root nodules fix atmospheric N₂ into soil nitrogen compounds that enrich the next wheat crop",
             "تثبت بكتيريا الرايزوبيوم في العقد الجذرية للبقوليات غاز N₂ الجوي وتحوله لمركبات نيتروجينية تغذي محصول القمح التالي"),
            ("Alfalfa roots release nitrates straight into the upper atmosphere",
             "تطلق جذور البرسيم النترات مباشرة إلى طبقات الجو العليا"),
            ("Wheat destroys all soil bacteria unless alfalfa kills weeds with acid",
             "القمح يقتل كل بكتيريا التربة ما لم يفرز البرسيم أحماضاً"),
            ("Legumes perform photosynthesis without needing any nitrogen atoms in proteins",
             "تقوم البقوليات بالبناء الضوئي دون حاجة لبناء أي بروتينات تحوي النيتروجين"),
        ],
        "Connect legumes to root-nodule nitrogen-fixing bacteria.",
        "اربط البقوليات بالبكتيريا المثبتة للنيتروجين في العقد الجذرية.",
        "Explain how wheat depletes nitrates while legumes replenish them.",
        ["Wheat cannot fix atmospheric N₂ and steadily removes soil nitrates to synthesize grain proteins.",
         "Alfalfa hosts nitrogen-fixing bacteria inside root nodules; when alfalfa residue decomposes, soil ammonium and nitrates are replenished."],
        "Legume-cereal rotation is a foundational sustainable agriculture practice.",
        "نوضح كيف يستنفد القمح النترات وكيف يعوضها البرسيم.",
        ["القمح يمتص نترات التربة باستمرار ولا يستطيع تثبيت نيتروجين الهواء.",
         "البرسيم يستضيف بكتيريا تثبيت النيتروجين في جذوره، فتُخصب التربة طبيعياً للموسم التالي."],
        "الدورة الزراعية بالبقوليات تحافظ على خصوبة التربة المستدامة.",
    ))

    # 13 (Hard): Eutrophication oxygen-depletion cascade
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        "Excess nitrate and phosphate fertilizer washes into a closed lake, triggering a massive surface algal bloom. Weeks later, thousands of fish suffocate. What is the <strong>direct</strong> biological cause of the oxygen depletion?",
        "تسرّب فائض من أسمدة النترات والفوسفات إلى بحيرة مغلقة، مما أشعل ازدهاراً هائلاً للطحالب السطحية، وبعد أسابيع نفق آلاف الأسماك اختناقاً. ما السبب الحيوي <strong>المباشر</strong> لنفاد الأكسجين المذاب؟",
        [
            ("Aerobic decomposer bacteria multiply rapidly on dying algae and consume dissolved O₂ via cellular respiration",
             "تتكاثر البكتيريا المحللة الهوائية بكثافة على الطحالب الميتة وتستهلك الأكسجين المذاب في التنفس الخلوي"),
            ("Fertilizer molecules chemically react with H₂O to turn O₂ into nitrogen gas",
             "تتفاعل الأسمدة كيميائياً مع الماء لتحويل الأكسجين إلى نيتروجين"),
            ("Living algae stop photosynthesis permanently as soon as nitrates enter water",
             "تتوقف الطحالب الحية عن البناء الضوئي فور دخول النترات"),
            ("Fish absorb nitrates instead of oxygen through their gills",
             "تمتص الأسماك النترات عبر خياشيمها بدلاً من الأكسجين"),
        ],
        "Algae produce O₂ while alive and sunlit, so ask what happens after the overgrown bloom shades and dies.",
        "تنتج الطحالب الأكسجين وهي حية، ففكّر فيما يحدث بعد موتها وتحللها.",
        "Trace the eutrophication sequence: nutrients → bloom → shade/death → aerobic decomposition → hypoxia.",
        ["Surface algae block sunlight to deeper plants and eventually exhaust nutrients and die.",
         "Decomposer bacteria break down the massive dead algal biomass using aerobic cellular respiration, stripping dissolved O₂ from the water."],
        "This process is cultural eutrophication.",
        "نتتبع سلسلة الإثراء الغذائي حتى استهلاك الأكسجين.",
        ["تحجب الطحالب السطحية الضوء ثم تموت بكميات ضخمة بعد استنفاد المغذيات.",
         "تنشط البكتيريا المحللة الهوائية لتفكيكها فتستهلك معظم الأكسجين المذاب بالتنفس الخلوي وتختنق الأسماك."],
        "تُعرف هذه الظاهرة بالإثراء الغذائي للمسطحات المائية.",
    ))

    # 14 (Hard): Variable trophic efficiency calculation (8000 -> 960 -> 144 J)
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        f"In an oasis ecosystem pyramid, producers store {m('8,000')} J, primary consumers store {m('960')} J, and secondary consumers store {m('144')} J. What is the trophic transfer efficiency (in {m(r'\%')}) from <strong>primary consumers to secondary consumers</strong>?",
        f"في هرم بيئي لواحة، تختزن المنتجات {m('8,000')} J، والمستهلكات الأولية {m('960')} J، والمستهلكات الثانوية {m('144')} J. ما كفاءة انتقال الطاقة (بوحدة {m(r'\%')}) من <strong>المستهلكات الأولية إلى الثانوية</strong>؟",
        15, [12, 1.8, 18],
        "Divide the energy of secondary consumers by the energy of primary consumers, then multiply by 100%.",
        "اقسم طاقة المستهلكات الثانوية على طاقة المستهلكات الأولية واضرب في 100%.",
        f"Compute {m(r'\frac{144}{960} \times 100\%')}.",
        [f"Primary consumer energy = {m('960')} J; Secondary consumer energy = {m('144')} J.",
         f"Transfer efficiency = {m(r'\frac{144}{960} \times 100\% = 0.15 \times 100\% = 15\%')}."],
        f"Notice producer→primary was {m(r'960/8000 = 12\%')}, whereas primary→secondary is {m(r'15\%')}.",
        "نحسب نسبة طاقة المستوى الأعلى إلى المستوى الذي يسبقه مباشرة.",
        [f"طاقة المستهلك الأول {m('960')} J، وطاقة المستهلك الثاني {m('144')} J.",
         f"كفاءة الانتقال = {m(r'\frac{144}{960} \times 100\% = 15\%')}."],
        f"كفاءة الخطوة الأولى كانت {m(r'12\%')} أما الثانية فهي {m(r'15\%')}.",
        suffix=r"\%",
        diagram_en=svg_energy_pyramid([("2°: 144 J", "?%"), ("1°: 960 J", "12%"), ("Prod: 8,000 J", "100%")],
                                      "Oasis Efficiency"),
        diagram_ar=_ar_svg(svg_energy_pyramid([("2°: 144 J", "?%"), ("1°: 960 J", "12%"), ("Prod: 8,000 J", "100%")],
                                              "Oasis Efficiency"),
                           {"Prod": "المنتج", "Oasis Efficiency": "كفاءة هرم الواحة"}),
    ))
    return qs


def _gen_sci_b06(start_idx: int) -> list[dict]:
    """G9-SCI-B06: Natural selection, adaptation & experimental controls/hypotheses."""
    bp = "G9-SCI-B06"
    qs: list[dict] = []

    # 0 (Easy): Identifying IV and DV
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_LIFE, "Easy", bp,
        "A student tests how four different water temperatures (15 °C, 25 °C, 35 °C, 45 °C) affect the number of oxygen bubbles released per minute by an aquatic Elodea plant, keeping light brightness and CO₂ constant. What are the independent and dependent variables?",
        "يختبر طالب أثر أربع درجات حرارة للماء (15، 25، 35، 45 °س) في عدد فقاعات الأكسجين المنطلقة في الدقيقة من نبات مائي، مع تثبيت شدة الإضاءة وتركيز CO₂. ما المتغير المستقل وما المتغير التابع؟",
        [
            ("Independent: water temperature; Dependent: oxygen bubbles per minute",
             "المستقل: درجة حرارة الماء؛ التابع: عدد فقاعات الأكسجين في الدقيقة"),
            ("Independent: oxygen bubbles per minute; Dependent: water temperature",
             "المستقل: عدد فقاعات الأكسجين؛ التابع: درجة حرارة الماء"),
            ("Independent: light brightness; Dependent: CO₂ concentration",
             "المستقل: شدة الإضاءة؛ التابع: تركيز CO₂"),
            ("Independent: Elodea species; Dependent: beaker volume",
             "المستقل: نوع النبات؛ التابع: حجم الكأس"),
        ],
        "The independent variable is what the experimenter deliberately changes; the dependent variable is what is measured.",
        "المتغير المستقل هو ما يغيّره الباحث عمداً، والتابع هو ما يُقاس استجابةً له.",
        "Separate manipulated input, measured output, and controlled constants.",
        ["The student systematically varies water temperature (15–45 °C) → independent variable.",
         "The resulting photosynthesis rate (bubbles/min) is measured → dependent variable; light and CO₂ are controls."],
        "Only one independent variable should change per fair test.",
        "نميز بين المدخل المتغيّر عمداً والناتج المقاس والثوابت.",
        ["درجة الحرارة هي العامل الذي يبدّله الباحث عمداً (المتغير المستقل).",
         "معدل الفقاعات هو النتيجة المقاسة (المتغير التابع)، بينما الإضاءة وCO₂ متغيرات ثابتة."],
        "التجربة العادلة تغير متغيراً مستقلاً واحداً فقط.",
    ))

    # 1 (Easy): Purpose of a control group
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_LIFE, "Easy", bp,
        "Researchers test a new drought-tolerance spray on 50 date palm saplings while spraying 50 identical saplings with plain water under the same sunlight and soil. Why is the plain-water group necessary?",
        "اختبر باحثون بخاخاً جديداً لزيادة تحمل الجفاف على 50 شتلة نخيل، ورشوا 50 شتلة مماثلة بالماء العادي فقط تحت الإضاءة والتربة نفسيهما. لماذا تعد مجموعة الماء العادي ضرورية؟",
        [
            ("It serves as a control group baseline to isolate the effect of the active chemical from water, soil, or weather",
             "تمثل مجموعة ضابطة مرجعية لعزل أثر المادة الفعالة عن أثر الماء والتربة والطقس"),
            ("It increases the total concentration of spray applied to the test plants",
             "تزيد من تركيز البخاخ الكيميائي المطبق على نباتات الاختبار"),
            ("It proves the hypothesis automatically even before measuring growth",
             "تثبت صحة الفرضية تلقائياً قبل قياس النمو"),
            ("It converts the dependent variable into an unmeasured opinion",
             "تحول المتغير التابع إلى رأي غير قابل للقياس"),
        ],
        "Without an untreated baseline, you cannot tell whether changes came from the spray or normal water/growth.",
        "بدون مجموعة مقارنة مرجعية لا يمكن الجزم بأن النتيجة سببها البخاخ أم الماء والظروف.",
        "Identify the role of an experimental control group.",
        ["Spraying plain water matches the physical act of wetting leaves without the active compound.",
         "Comparing treated vs control survival proves whether the active ingredient itself caused any improvement."],
        "Controls eliminate alternative explanations.",
        "نوضح وظيفة المجموعة الضابطة في التجربة العلمية.",
        ["رش الماء العادي يماثل عملية الترطيب دون المادة الكيميائية المختبرة.",
         "المقارنة بين المجموعتين تثبت إن كان التحسن ناتجاً عن البخاخ فعلاً."],
        "المجموعة الضابطة تستبعد التفسيرات البديلة.",
        diagram_en=_svg_experiment_bars("Drought Spray Trial", "تجربة رذاذ الجفاف", [("Control", "ضابطة", 50, "n=50"), ("Spray", "رذاذ", 50, "n=50")], "Sample Size", "حجم العينة", "en"),
        diagram_ar=_svg_experiment_bars("Drought Spray Trial", "تجربة رذاذ الجفاف", [("Control", "ضابطة", 50, "n=50"), ("Spray", "رذاذ", 50, "n=50")], "Sample Size", "حجم العينة", "ar"),
    ))

    # 2 (Easy): Core mechanism of natural selection
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_LIFE, "Easy", bp,
        "Which statement accurately explains how <strong>natural selection</strong> produces adaptation in a desert lizard population over many generations?",
        "أي عبارة تشرح بدقة كيف يُنتج <strong>الانتخاب الطبيعي</strong> التكيف في جماعة سحالي صحراوية عبر أجيال عديدة؟",
        [
            ("Individuals born with heritable traits better suited to the habitat survive and reproduce more, passing those alleles to offspring",
             "الأفراد المولودون بصفات وراثية أكثر ملاءمة للبيئة ينجون ويتكاثرون أكثر، فينقلون تلك الجينات لنسلهم"),
            ("Individual lizards consciously decide to mutate their skin DNA when the desert gets hotter",
             "تقرر السحلية الفردية بوعي أن تعدّل حمضها النووي عندما يشتد الحر"),
            ("Acquired muscles or scars gained during one lizard's lifetime are automatically inherited by its eggs",
             "الصفات المكتسبة والندوب التي يكتسبها الفرد في حياته تورّث تلقائياً في البيض"),
            ("All individuals in a population are genetically identical clones before selection begins",
             "جميع أفراد الجماعة متطابقون وراثياً تماماً قبل بدء الانتخاب"),
        ],
        "Natural selection acts on pre-existing heritable genetic variation, not conscious effort.",
        "يعمل الانتخاب الطبيعي على التنوع الوراثي الموجود مسبقاً وليس بإرادة الكائن.",
        "Check the three requirements: variation, heritability, differential reproduction.",
        ["Random genetic mutations and meiosis create pre-existing variation within a population.",
         "Environmental pressures favor individuals with advantageous heritable alleles, raising those alleles' frequency in future generations."],
        "Populations evolve across generations; individual organisms do not evolve new DNA on demand.",
        "نتحقق من شروط الانتخاب: التنوع، والتوريث، وتفاوت البقاء والتكاثر.",
        ["توجد اختلافات وراثية مسبقة بين أفراد الجماعة.",
         "الأكثر ملاءمة يعيش ويتكاثر أكثر، فتزداد نسبة أليلاته المفيدة في الأجيال القادمة."],
        "التكيف يظهر على مستوى الجماعة عبر الأجيال وليس بتغيّر إرادي للفرد.",
    ))

    # 3 (Easy): Antibiotic resistance & completing prescriptions
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_LIFE, "Easy", bp,
        "Why do physicians strongly advise patients to complete a full prescribed antibiotic course even if symptoms disappear after 3 days?",
        "لماذا يشدد الأطباء على إكمال جرعة المضاد الحيوي كاملة حتى لو اختفت الأعراض بعد 3 أيام؟",
        [
            ("Stopping early leaves partially resistant bacteria alive to multiply and pass resistance genes to a harder-to-treat population",
             "التوقف المبكر يُبقي البكتيريا الأكثر مقاومةً حية لتتكاثر وتنشر جينات المقاومة في جيل يصعب علاجه"),
            ("Antibiotics transform human red blood cells into bacteria if stopped early",
             "التوقف المبكر يحول كريات الدم الحمراء إلى بكتيريا"),
            ("Remaining pills lose all chemical mass after 3 days",
             "تفقد الأقراص المتبقية كتلتها الكيميائية بعد 3 أيام"),
            ("Stopping early teaches viruses how to build cellulose walls",
             "التوقف المبكر يعلّم الفيروسات بناء جدران سليلوزية"),
        ],
        "Who survives first when antibiotic concentration drops halfway through treatment?",
        "أي سلالات بكتيرية تصمد أكثر عند إيقاف المضاد في منتصف العلاج؟",
        "Apply natural selection to bacterial survival inside the host.",
        ["Sensitive bacteria die during days 1–3, relieving symptoms while slightly more resistant mutants still survive.",
         "Finishing the full course maintains lethal antibiotic concentrations long enough to eliminate those tougher survivors before they repopulate."],
        "Misuse of antibiotics accelerates the evolution of superbugs.",
        "نطبّق مبدأ الانتخاب الطبيعي على البكتيريا داخل الجسم.",
        ["تموت البكتيريا الحساسة في الأيام الأولى فتخف الأعراض بينما تبقى سلالات أكثر تحملاً.",
         "إكمال الجرعة يبقي التركيز كافياً للقضاء على البكتيريا المقاومة قبل تكاثرها."],
        "الاستخدام الناقص للمضادات يسرّع انتشار البكتيريا المقاومة.",
    ))

    # 4 (Easy): Testable hypothesis criterion
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_LIFE, "Easy", bp,
        "Which statement is a valid, <strong>testable scientific hypothesis</strong>?",
        "أي عبارة تمثل <strong>فرضية علمية صحيحة قابلة للاختبار</strong>؟",
        [
            ("If soil salinity increases from 0% to 2%, then barley seed germination percentage will decrease",
             "إذا ارتفعت ملوحة التربة من 0% إلى 2%، فإن نسبة إنبات بذور الشعير ستنخفض"),
            ("Date palms are more beautiful than desert acacia trees",
             "أشجار النخيل أجمل من أشجار الطلح الصحراوية"),
            ("Every planet in the universe ought to host friendly creatures",
             "ينبغي أن يحتوي كل كوكب في الكون على مخلوقات لطيفة"),
            ("Water is the most wonderful substance ever discovered",
             "الماء هو أروع مادة تم اكتشافها على الإطلاق"),
        ],
        "A scientific hypothesis must make a falsifiable, measurable prediction linking variables.",
        "الفرضية العلمية يجب أن تقدم تنبؤاً قابلاً للقياس والتكذيب يربط بين متغيرين.",
        "Check which statement can be tested and disproved by an experiment.",
        ["Soil salinity (IV) and germination percentage (DV) are both objectively measurable.",
         "Beauty, preference, and moral 'ought' statements cannot be tested scientifically."],
        "An If–Then relationship between measurable variables defines a testable hypothesis.",
        "نختار العبارة التي تربط متغيرين قابلين للقياس والتجريب.",
        ["نسبة الملوحة ونسبة الإنبات كميتان قابلتان للقياس والاختبار المخبري.",
         "الأحكام الجمالية أو الانطباعات الشخصية لا تخضع للتجربة العلمية."],
        "صياغة (إذا تغيّر كذا ← يحدث كذا) القابلة للقياس تميز الفرضية العلمية.",
    ))

    # 5 (Medium): Beetle allele/phenotype frequency shift (6 percentage points)
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_LIFE, "Medium", bp,
        f"On dark volcanic basalt rock in Harrat Khaybar, an initial survey of {m('500')} desert beetles finds {m('420')} dark-shelled and {m('80')} sand-colored beetles. Three generations later, out of {m('600')} beetles, {m('540')} are dark-shelled. By how many <strong>percentage points</strong> did the dark-shelled beetle frequency increase?",
        f"على صخور البازلت الداكنة في حرة خيبر، وجد مسح أولي لـ {m('500')} خنفساء صحراوية أن {m('420')} منها داكنة و{m('80')} رملية اللون. بعد ثلاثة أجيال، ومن بين {m('600')} خنفساء، أصبحت {m('540')} داكنة اللون. بكم <strong>نقطة مئوية</strong> ارتفعت نسبة الخنافس الداكنة؟",
        6, [12, 24, 120],
        "Calculate the percentage of dark beetles initially (420/500) and after 3 generations (540/600), then subtract.",
        "احسب النسبة المئوية للخنافس الداكنة في البداية (420/500) وبعد ثلاثة أجيال (540/600)، ثم اطرحهما.",
        f"Compute {m(r'\frac{540}{600} \times 100\% - \frac{420}{500} \times 100\%')}.",
        [f"Initial dark frequency: {m(r'\frac{420}{500} = 84\%')}.",
         f"Final dark frequency: {m(r'\frac{540}{600} = 90\%')}.",
         f"Increase: {m(r'90\% - 84\% = 6')} percentage points."],
        f"Bird predators spot sand-colored beetles more easily on black basalt, raising dark survival from {m('84\\%')} to {m('90\\%')}.",
        "نحسب النسبتين المئويتين ثم نوجد الفرق.",
        [f"النسبة الابتدائية = {m(r'420/500 = 84\%')}.",
         f"النسبة بعد 3 أجيال = {m(r'540/600 = 90\%')}.",
         f"الزيادة = {m('90 - 84 = 6')} نقاط مئوية."],
        "التمويه الأفضل على الصخر الداكن رفع نسبة البقاء.",
        diagram_en=_svg_experiment_bars("Beetle Survey Counts", "مسح أعداد الخنافس", [("Gen 0 Dark", "ج0 داكن", 420, "420/500"), ("Gen 3 Dark", "ج3 داكن", 540, "540/600")], "Observed Beetles", "عدد الخنافس", "en"),
        diagram_ar=_svg_experiment_bars("Beetle Survey Counts", "مسح أعداد الخنافس", [("Gen 0 Dark", "ج0 داكن", 420, "420/500"), ("Gen 3 Dark", "ج3 داكن", 540, "540/600")], "Observed Beetles", "عدد الخنافس", "ar"),
    ))

    # 6 (Medium): Flawed multi-variable experiment critique
    qs.append(make_science_concept_q(
        _qid(start_idx + 6), LEVEL, T_LIFE, "Medium", bp,
        "A student wants to test whether Fertilizer X boosts tomato height. She places Pot A in full sunlight with Fertilizer X and daily watering, and Pot B in shade without Fertilizer X and weekly watering. After 3 weeks, Pot A is taller. Why is her conclusion invalid?",
        "تريد طالبة اختبار أثر السماد (X) في طول نبات الطماطم. وضعت الأصيص (أ) في شمس كاملة مع السماد وري يومي، والأصيص (ب) في الظل دون سماد مع ري أسبوعي. بعد 3 أسابيع طال (أ) أكثر. لماذا يُعد استنتاجها غير صالح علمياً؟",
        [
            ("She changed three variables at once (fertilizer, sunlight, and watering), introducing confounding variables",
             "لأنها غيّرت ثلاثة متغيرات معاً (السماد، الشمس، والري) مما أدخل متغيرات مشوّشة تمنع عزل أثر السماد"),
            ("She waited only 3 weeks instead of 30 years",
             "لأنها انتظرت 3 أسابيع فقط بدلاً من 30 سنة"),
            ("Tomato plants cannot respond to any fertilizer",
             "لأن نبات الطماطم لا يتأثر بأي نوع من الأسمدة"),
            ("She forgot to measure the color of the plastic pots",
             "لأنها نسيت قياس لون الأصيص البلاستيكي"),
        ],
        "How many independent variables may differ between the experimental and control groups?",
        "كم متغيراً مستقلاً يُسمح بتغييره بين المجموعة التجريبية والمجموعة الضابطة؟",
        "Check for confounded variables (sunlight and water varied alongside fertilizer).",
        ["Pot A received more light and water in addition to Fertilizer X.",
         "Because multiple factors changed simultaneously, it is impossible to tell whether Fertilizer X, extra sunlight, or daily watering caused the extra growth."],
        "To fix the experiment, keep sunlight and watering identical for both pots and use multiple plants per group.",
        "نفحص وجود متغيرات غير مضبوطة تغيّرت مع المتغير المستقل.",
        ["الأصيص (أ) تلقى شمساً وماءً أكثر إضافةً للسماد.",
         "تغير عدة عوامل معاً يمنع معرفة السبب الحقيقي للنمو، وللتصحيح يجب تثبيت الضوء والري للجميع."],
        "توحيد الظروف وعزل متغير واحد أساس التجربة المضبوطة.",
    ))

    # 7 (Medium): Enzyme experiment controlled variables
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_LIFE, "Medium", bp,
        "A lab team investigates how <strong>temperature</strong> (10 °C, 30 °C, 50 °C, 70 °C) affects the speed of starch digestion by salivary amylase. Which set of factors MUST be held constant across all four test tubes?",
        "يدرس فريق مخبري أثر <strong>درجة الحرارة</strong> (10، 30، 50، 70 °س) في سرعة هضم النشا بإنزيم الأميليز. أي مجموعة من العوامل يجب <strong>تثبيتها</strong> في جميع الأنابيب الأربعة؟",
        [
            ("Solution pH, amylase enzyme concentration, initial starch concentration, and total liquid volume",
             "الرقم الهيدروجيني (pH)، وتركيز إنزيم الأميليز، وتركيز النشا الابتدائي، وحجم المحلول الكلي"),
            ("Only the temperature of each water bath",
             "درجة حرارة كل حمام مائي فقط"),
            ("The time required for starch to vanish completely",
             "الزمن اللازم لاختفاء النشا تماماً"),
            ("The color change speed of iodine indicator",
             "سرعة تغير لون كاشف اليود"),
        ],
        "Temperature is the independent variable and digestion speed is the dependent variable; everything else affecting enzyme rate must stay fixed.",
        "الحرارة هي المتغير المستقل وسرعة الهضم هي المتغير التابع؛ كل عامل آخر يؤثر في الإنزيم يجب تثبيته.",
        "Identify variables known to alter enzyme activity besides temperature.",
        ["Enzymes are highly sensitive to pH as well as enzyme and substrate (starch) concentrations.",
         "Holding pH, enzyme amount, starch amount, and volume constant ensures only temperature drives differences in reaction rate."],
        "The digestion time is the dependent outcome being measured, not a fixed parameter.",
        "نحدد العوامل المؤثرة في نشاط الإنزيم عدا الحرارة.",
        ["يتأثر الإنزيم بشدة بدرجة الحموضة (pH) وبتركيز الإنزيم والنشا.",
         "تثبيت هذه العوامل يضمن أن الفرق في السرعة ناتج عن تغير الحرارة وحدها."],
        "أما زمن الهضم فهو المتغير التابع الذي نقيسه.",
    ))

    # 8 (Medium): Artificial vs natural selection
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_LIFE, "Medium", bp,
        "Over centuries, pastoralists bred Arabian camels with the highest milk production, whereas desert wild foxes evolved large ears that radiate excess body heat. How do these two processes compare?",
        "على مدى قرون، اختار المربون الإبل الأكثر إدراراً للحليب للتزاوج، بينما تطورت لثعالب الصحراء آذان كبيرة تشع الحرارة الزائدة. كيف تتم مقارنة العمليتين؟",
        [
            ("Camel breeding is artificial selection driven by human choice; fox ear evolution is natural selection driven by desert survival",
             "تربية الإبل انتخاب اصطناعي يوجهه اختيار الإنسان، بينما تطور آذان الثعلب انتخاب طبيعي تفرضه البقاء في الصحراء"),
            ("Both are identical examples of random genetic drift with zero selection",
             "كلاهما مثالان متطابقان للانحراف الوراثي العشوائي دون أي انتخاب"),
            ("Fox ears evolved through artificial selection by desert plants",
             "تطورت آذان الثعالب بانتخاب اصطناعي من نباتات الصحراء"),
            ("Artificial selection acts only on plants and cannot work on mammals",
             "الانتخاب الاصطناعي يعمل على النباتات فقط ولا يمكن تطبيقه على الثدييات"),
        ],
        "Who chooses which traits reproduce in farming versus in wild ecosystems?",
        "من يحدد الأفراد التي تتكاثر في المزارع مقابل البرية؟",
        "Distinguish human-directed breeding from environmental survival pressure.",
        ["In artificial selection, humans choose parents exhibiting desired agricultural traits (milk yield, grain size).",
         "In natural selection, environmental challenges (desert heat) favor traits aiding survival and reproduction."],
        "Both rely on heritable genetic variation.",
        "نميز بين التوجيه البشري وضغط البيئة الطبيعي.",
        ["في الانتخاب الاصطناعي يختار الإنسان الآباء ذوي الصفات المرغوبة كإدرار الحليب.",
         "في الانتخاب الطبيعي تفرض البيئة (كالحر الشديد) بقاء الأفراد ذوي الصفة التكيفية."],
        "كلاهما يعتمد على وجود تنوع وراثي قابل للتوريث.",
    ))

    # 9 (Medium): Multi-trial germination mean excluding anomalous trial
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_LIFE, "Medium", bp,
        f"A botanist measures seed germination counts out of {m('50')} seeds across 5 identical replicate dishes: {m('41, 43, 42, 9, 42')}. Upon inspection, Dish 4 ({m('9')}) had heavy fungal mold contamination from an unsterilized lid. Excluding the contaminated outlier, what is the true mean germination percentage (in {m(r'\%')}) across the 4 valid dishes?",
        f"قاس باحث عدد البذور المنبتة من أصل {m('50')} بذرة في 5 أطباق متماثلة فكانت: {m('41, 43, 42, 9, 42')}. تبيّن تلوث الطبق الرابع ({m('9')}) بعفن فطري بسبب غطاء غير معقم. باستثناء الطبق الملوث، ما متوسط نسبة الإنبات الصحيحة (بوحدة {m(r'\%')}) في الأطباق الأربعة السليمة؟",
        84, [67.2, 42, 85],
        "Average the 4 valid counts first, then divide by 50 seeds and multiply by 100%.",
        "احسب متوسط الأطباق الأربعة السليمة أولاً، ثم اقسمه على 50 بذرة واضرب في 100%.",
        f"Compute {m(r'\frac{(41+43+42+42)/4}{50} \times 100\%')}.",
        [f"Sum of 4 valid dishes: {m('41 + 43 + 42 + 42 = 168')}, so mean count = {m('168 \\div 4 = 42')} seeds.",
         f"Germination percentage = {m(r'\frac{42}{50} \times 100\% = 84\%')}."],
        f"Notice including the contaminated dish drops the false mean to {m(r'67.2\%')}.",
        "نستثني القيمة الشاذة المبررة مخبرياً ونحسب المتوسط من 50.",
        [f"مجموع الأطباق السليمة الأربعة = {m('168')}، والمتوسط = {m('42')} بذرة.",
         f"النسبة المئوية = {m(r'\frac{42}{50} \times 100\% = 84\%')}."],
        f"إدخال الطبق الملوث كان سيشوه المتوسط إلى {m(r'67.2\%')}.",
        suffix=r"\%",
    ))

    # 10 (Hard): Blank sterile disk control in Kirby-Bauer assay
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_LIFE, "Hard", bp,
        "To test whether an extract from desert <em>Artemisia</em> (sheeh) kills <em>E. coli</em> bacteria, a student dissolves the extract in <strong>70% ethanol</strong>, soaks paper Disk A in it, and places Disk A on a bacterial lawn. A clear bacteria-free ring appears around Disk A. Before claiming the plant extract kills <em>E. coli</em>, what essential control disk MUST be placed on the same agar plate?",
        "لاختبار قدرة مستخلص نبات الشيح الصحراوي على قتل بكتيريا E. coli، أذاب طالب المستخلص في <strong>إيثانول 70%</strong> وغمس فيه القرص (أ) ووضعه على طبق بكتيريا فظهرت هالة خالية من النمو. قبل الجزم بأن مستخلص النبات هو القاتل، ما القرص الضابط الأساسي الواجب وضعه على الطبق نفسه؟",
        [
            ("A blank sterile paper disk soaked in 70% ethanol solvent alone (without plant extract)",
             "قرص ورقي معقم مبلل بمذيب الإيثانول 70% وحده (دون مستخلص النبات)"),
            ("A disk soaked in boiling water added to a separate fridge",
             "قرص مبلل بالماء المغلي يوضع في ثلاجة منفصلة"),
            ("A disk coated with sucrose sugar solution only",
             "قرص مغطى بمحلول السكروز فقط"),
            ("An extra plate with no bacteria at all",
             "طبق إضافي خالٍ تماماً من البكتيريا"),
        ],
        "70% ethanol itself kills bacteria! You must isolate the solvent's effect from the plant extract's effect.",
        "الإيثانول 70% نفسه يقتل البكتيريا! يجب عزل أثر المذيب عن أثر مستخلص النبات.",
        "Design a vehicle (solvent) control matching everything except the active test extract.",
        ["Because 70% ethanol is a disinfectant, the clear ring around Disk A might come entirely from the ethanol solvent.",
         "Comparing Disk A (extract + ethanol) against a control disk (ethanol only) tests whether the plant extract adds extra antibacterial killing."],
        "Solvent controls are mandatory whenever testing dissolved compounds.",
        "نصمم مجموعة ضابطة للمذيب تطابق كل شيء ما عدا المستخلص النباتي.",
        ["بما أن الإيثانول 70% مطهر يقتل البكتيريا، فقد تكون الهالة بسببه وحده.",
         "المقارنة مع قرص يحتوي إيثانول فقط تثبت إن كان لمستخلص الشيح أثر قاتل إضافي."],
        "ضبط المذيب شرط أساسي عند اختبار المواد المذابة.",
    ))

    # 11 (Hard): Reversal of selection pressure
    qs.append(make_science_concept_q(
        _qid(start_idx + 11), LEVEL, T_LIFE, "Hard", bp,
        "In a moth population, dark wing color was favored on soot-blackened trees for 40 years, raising dark-moth frequency to 88%. After clean-air laws restore pale lichen-covered bark, how will the population's genetic makeup most likely shift over the next 20 generations?",
        "في جماعة عث، كان اللون الداكن مفضلاً على جذوع الأشجار المسودة بالسخام لمدة 40 عاماً فبلغت نسبته 88%. بعد تطبيق قوانين الهواء النظيف وعودة الأشنات الفاتحة للجذوع، كيف سيتغير التركيب الوراثي للجماعة خلال العشرين جيلاً القادمة؟",
        [
            ("Pale moths gain camouflage advantage, survive predators more often, and increase the frequency of pale-wing alleles",
             "تكتسب الفراشات الفاتحة أفضلية التمويه فتنجو أكثر من المفترسات وتزداد نسبة أليلات اللون الفاتح"),
            ("Dark moths intentionally change their own DNA to become white during their lifetime",
             "تغيّر الفراشات الداكنة حمضها النووي عمداً لتصبح بيضاء خلال حياتها"),
            ("All dark moths vanish instantly in the very first generation",
             "تختفي جميع الفراشات الداكنة فوراً في الجيل الأول"),
            ("Pale alleles can never reappear once dark frequency passes 50%",
             "لا يمكن لأليلات اللون الفاتح أن تزداد ثانية بعد تجاوز الداكن 50%"),
        ],
        "Natural selection reverses direction whenever environmental selective pressure reverses, provided variation still exists.",
        "ينعكس اتجاه الانتخاب الطبيعي عند انعكاس البيئة، ما دام التنوع الوراثي موجوداً.",
        "Check remaining variation (12% pale + heterozygotes) and reversed predator visibility.",
        ["The 12% pale individuals (plus heterozygous carriers) retain pale alleles in the gene pool.",
         "On pale bark, dark moths stand out to birds while pale moths stay camouflaged, shifting allele frequencies back toward pale."],
        "Evolution tracks shifting environments rather than moving toward a fixed 'final' goal.",
        "نتتبع بقاء الأليلات الفاتحة وانعكاس أفضلية التمويه.",
        ["ما زالت نسبة 12% والأفراد الهجينة تحتفظ بأليلات اللون الفاتح في المخزون الوراثي.",
         "على اللحاء الفاتح تصبح الفراشات الداكنة مكشوفة للطيور فتزداد نسبة الأليلات الفاتحة تدريجياً."],
        "الانتخاب الطبيعي يتبع تغير البيئة ولا يسير في مسار واحد جامد.",
        diagram_en=_svg_experiment_bars("Moth Color Survey", "مسح ألوان العث", [("Light", "فاتح", 12, "12%"), ("Dark", "داكن", 88, "88%")], "Population %", "النسبة %", "en"),
        diagram_ar=_svg_experiment_bars("Moth Color Survey", "مسح ألوان العث", [("Light", "فاتح", 12, "12%"), ("Dark", "داكن", 88, "88%")], "Population %", "النسبة %", "ar"),
    ))

    # 12 (Hard): Correlation vs causation lurking variable
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_LIFE, "Hard", bp,
        "A health report finds a strong positive correlation between monthly ice-cream sales and monthly heatstroke hospital visits, concluding that eating ice cream causes heatstroke. What is the scientific flaw in this reasoning?",
        "أظهر تقرير إحصائي ارتباطاً طردياً قوياً بين مبيعات المثلجات الشهرية وحالات ضربة الشمس في المستشفيات، فاستنتج الكاتب أن أكل المثلجات يسبب ضربة الشمس. ما الخلل العلمي في هذا الاستنتاج؟",
        [
            ("It confuses correlation with causation; a confounding variable (high summer temperature) drives both ice-cream sales and heatstroke independently",
             "يخلط بين الارتباط والسببية؛ فهناك متغير خفي مشترك (ارتفاع حرارة الصيف) يزيد مبيعات المثلجات وضربات الشمس معاً"),
            ("Ice cream contains bacteria that instantly cause heatstroke",
             "تحتوي المثلجات على بكتيريا تسبب ضربة الشمس فوراً"),
            ("Correlation always proves direct biological causation unless negative",
             "الارتباط يثبت دائماً السببية المباشرة ما لم يكن سالباً"),
            ("Hospital records cannot be graphed against retail sales data",
             "لا يجوز تمثيل بيانات المستشفيات مع بيانات المبيعات بيانياً"),
        ],
        "Look for a third underlying seasonal factor driving both variables simultaneously.",
        "ابحث عن عامل ثالث موسمي يرفع كلاً من المتغيرين في الوقت نفسه.",
        "Identify the confounding (lurking) variable.",
        ["Hot summer weather independently makes people buy more ice cream AND increases heatstroke risk.",
         "Observational correlation alone never proves causation without controlling confounding variables."],
        "A controlled experiment or stratified temperature analysis separates true causation from coincidence.",
        "نحدد المتغير المشوّش المشترك.",
        ["حرارة الصيف المرتفعة تدفع الناس لشراء المثلجات وترفع خطر ضربات الشمس في الوقت نفسه.",
         "الارتباط الإحصائي وحده لا يثبت السببية دون استبعاد العوامل المشوّشة."],
        "العلاقة السببية تتطلب تجربة مضبوطة تعزل المؤثر الحقيقي.",
    ))

    # 13 (Hard): Sample size & replication critique
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_LIFE, "Hard", bp,
        "Two teams test the same probiotic supplement on seedling growth. Team 1 uses 2 seedlings per group (n = 2); Team 2 uses 40 randomly assigned seedlings per group (n = 40). Why is Team 2's conclusion far more scientifically reliable?",
        "اختبر فريقان مكملاً حيوياً على نمو الشتلات: استخدم الفريق الأول شتلتين لكل مجموعة (n = 2)، واستخدم الفريق الثاني 40 شتلة موزعة عشوائياً لكل مجموعة (n = 40). لماذا تكون نتائج الفريق الثاني أكثر موثوقية علمياً؟",
        [
            ("Large sample size and random assignment average out random biological variation and reduce sampling error",
             "حجم العينة الكبير والتوزيع العشوائي يقللان أثر التباين الفردي العشوائي ويخفضان خطأ المعاينة"),
            ("Using 40 seedlings doubles the chemical molarity of the probiotic automatically",
             "استخدام 40 شتلة يضاعف التركيز المولاري للمكمل تلقائياً"),
            ("Smaller groups (n = 2) have zero genetic differences between plants",
             "المجموعات الصغيرة (n = 2) تنعدم فيها الفروق الوراثية تماماً"),
            ("Large samples guarantee every single plant grows to the exact same millimeter",
             "العينات الكبيرة تضمن نمو كل شتلة بالطول نفسه تماماً دون تفاوت"),
        ],
        "Think about what happens to a tiny sample if one plant happens to carry a weak seed gene by chance.",
        "فكّر في أثر وجود بذرة ضعيفة بالصدفة عندما يكون حجم العينة شتلتين فقط.",
        "Relate replication (n) and randomization to statistical reliability.",
        ["With only n = 2, one unusually strong or weak seed skews the group average dramatically.",
         "Randomly assigning n = 40 plants minimizes genetic/micro-environment bias and random noise."],
        "Replication plus randomization underpins valid biological inference.",
        "نربط تكرار العينة والعشوائية بتقليل الخطأ العشوائي.",
        ["عند n = 2 يكفي تفاوت فردي واحد في بذرة لتشويه المتوسط بالكامل.",
         "العشوائية مع n = 40 توزّع التفاوتات الطبيعية بالتساوي وتُظهر الأثر الحقيقي للعلاج."],
        "التكرار والتوزيع العشوائي ركيزتان لصحة الاستنتاج التجريبي.",
        diagram_en=_svg_experiment_bars("Study Sample Sizes", "حجم العينة في الدراستين", [("Team 1", "فريق 1", 2, "n=2"), ("Team 2", "فريق 2", 40, "n=40")], "Plants per Group", "عدد النباتات", "en"),
        diagram_ar=_svg_experiment_bars("Study Sample Sizes", "حجم العينة في الدراستين", [("Team 1", "فريق 1", 2, "n=2"), ("Team 2", "فريق 2", 40, "n=40")], "Plants per Group", "عدد النباتات", "ar"),
    ))

    # 14 (Hard): Double-blind randomized clinical design
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_LIFE, "Hard", bp,
        "In a medical trial testing a new blood-pressure pill, why is a <strong>double-blind</strong> placebo-controlled design (neither patients nor evaluating doctors know who receives the pill vs placebo) considered the gold standard?",
        "في تجربة سريرية لاختبار دواء جديد لضغط الدم، لماذا يُعد التصميم <strong>المزدوج التعمية</strong> مع دواء وهمي (لا يعرف المريض ولا الطبيب المقيم من أخذ الدواء الحقيقي أو الوهمي) المعيار الذهبي؟",
        [
            ("It eliminates both patient placebo expectations and unconscious observer measurement bias",
             "يزيل كلاً من تأثير التوقع النفسي لدى المريض وانحياز القياس اللاواعي لدى الباحث"),
            ("It ensures every patient receives twice the normal drug dose",
             "يضمن حصول كل مريض على ضعف الجرعة الدوائية المعتادة"),
            ("It removes the need for measuring blood pressure with instruments",
             "يلغي الحاجة لقياس ضغط الدم بالأجهزة"),
            ("It allows doctors to switch patients between groups whenever blood pressure rises",
             "يسمح للأطباء بتبديل المرضى بين المجموعات أثناء التجربة"),
        ],
        "Consider psychological effects on patients AND subtle recording biases by researchers.",
        "فكّر في الأثر النفسي على المريض وانحياز الملاحظة لدى الطبيب.",
        "Account for the two layers of 'blinding' (patient + evaluator).",
        ["Blinding patients with an identical placebo pill isolates real pharmacology from psychological expectation (placebo effect).",
         "Blinding evaluating clinicians prevents subtle bias in how borderline symptoms or readings are recorded."],
        "Randomization + placebo + double-blinding gives clean causal inference.",
        "نوضح فائدة التعمية المزدوجة على المستويين.",
        ["إعطاء قرص وهمي مطابق يعزل الأثر الدوائي الفعلي عن التحسن النفسي (أثر الدواء الوهمي).",
         "إخفاء المجموعة عن الطبيب يمنع أي تحيز غير مقصود عند تسجيل القياسات."],
        "التعشية والتعمية المزدوجة تضبطان التجارب السريرية بدقة.",
    ))
    return qs


# ==============================================================================
# DOMAIN 2: CHEMISTRY & MATTER (G9-SCI-B07 .. G9-SCI-B12, IDs 091 .. 180)
# ==============================================================================

def _gen_sci_b07(start_idx: int) -> list[dict]:
    """G9-SCI-B07: Atomic number Z, mass number A, neutrons A-Z, ions & isotopes."""
    bp = "G9-SCI-B07"
    qs: list[dict] = []

    # 0 (Easy): Mass number from Bohr model of Carbon-12
    qs.append(make_science_math_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        f"Look at the Bohr model for a neutral Carbon atom showing {m('p^+ = 6')}, {m('n^0 = 6')}, and {m('e^- = 6')}. What is the <strong>mass number</strong> ({m('A')}) of this atom?",
        f"انظر إلى نموذج بور لذرة كربون متعادلة يظهر فيه {m('p^+ = 6')} و{m('n^0 = 6')} و{m('e^- = 6')}. ما <strong>العدد الكتلي</strong> ({m('A')}) لهذه الذرة؟",
        12, [6, 18, 24],
        "Mass number A equals protons plus neutrons inside the nucleus (electrons have negligible mass).",
        "العدد الكتلي A يساوي مجموع البروتونات والنيوترونات في النواة.",
        f"Use {m('A = Z + N')}.",
        [f"Number of protons {m('Z = 6')} and neutrons {m('N = 6')}.",
         f"Mass number {m('A = 6 + 6 = 12')}."],
        f"Atomic number is {m('6')}, while mass number is {m('12')}.",
        "نجمع البروتونات والنيوترونات.",
        [f"عدد البروتونات {m('Z = 6')} والنيوترونات {m('N = 6')}.",
         f"العدد الكتلي {m('A = 6 + 6 = 12')}."],
        f"العدد الذري {m('6')} والعدد الكتلي {m('12')}.",
        diagram_en=svg_atom_bohr("C", 6, 6, [2, 4], "Carbon Bohr Model"),
        diagram_ar=_ar_svg(svg_atom_bohr("C", 6, 6, [2, 4], "Carbon Bohr Model"),
                           {"Carbon Bohr Model": "نموذج بور للكربون"}),
    ))

    # 1 (Easy): Neutrons N = A - Z in Aluminum-27
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        f"An Aluminum atom has atomic number {m('Z = 13')} and mass number {m('A = 27')}. How many <strong>neutrons</strong> are in its nucleus?",
        f"تمتلك ذرة الألومنيوم عدداً ذرياً {m('Z = 13')} وعدداً كتلياً {m('A = 27')}. كم <strong>نيوتروناً</strong> يوجد في نواتها؟",
        14, [13, 27, 40],
        "Subtract the atomic number Z (protons) from the mass number A.",
        "اطرح العدد الذري Z (البروتونات) من العدد الكتلي A.",
        f"Compute {m('N = A - Z')}.",
        [f"Protons {m('Z = 13')} and total nucleons {m('A = 27')}.",
         f"Neutrons {m('N = 27 - 13 = 14')}."],
        f"Check sum: {m('13 + 14 = 27')}.",
        "نطرح العدد الذري من العدد الكتلي.",
        [f"عدد البروتونات {m('13')} ومجموع مكونات النواة {m('27')}.",
         f"عدد النيوترونات = {m('27 - 13 = 14')}."],
        f"التحقق: {m('13 + 14 = 27')}.",
        diagram_en=svg_atom_bohr("Al", 13, 14, [2, 8, 3], "Aluminum-27"),
        diagram_ar=_ar_svg(svg_atom_bohr("Al", 13, 14, [2, 8, 3], "Aluminum-27"),
                           {"Aluminum-27": "ألومنيوم-27"}),
    ))

    # 2 (Easy): Definition of isotopes (C-12 vs C-14)
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        f"How do the two carbon isotopes {m('^{12}_{6}\\text{C}')} and {m('^{14}_{6}\\text{C}')} compare in subatomic structure?",
        f"كيف يقارن نظيرا الكربون {m('^{12}_{6}\\text{C}')} و{m('^{14}_{6}\\text{C}')} من حيث الجسيمات دون الذرية؟",
        [
            ("Both have 6 protons and 6 electrons, but C-14 has 8 neutrons instead of 6",
             "كلاهما يمتلك 6 بروتونات و6 إلكترونات، لكن كربون-14 يحتوي 8 نيوترونات بدلاً من 6"),
            ("Both have 6 neutrons, but C-14 has 8 protons",
             "كلاهما يحتوي 6 نيوترونات، لكن كربون-14 يحتوي 8 بروتونات"),
            ("C-14 has a +2 net electrical charge while C-12 is neutral",
             "كربون-14 يحمل شحنة +2 بينما كربون-12 متعادل"),
            ("C-12 and C-14 belong to two different elements in the periodic table",
             "ينتمي كربون-12 وكربون-14 إلى عنصرين مختلفين في الجدول الدوري"),
        ],
        "Isotopes belong to the same element (identical Z) and differ only in neutron number.",
        "النظائر تتبع العنصر نفسه (نفس Z) وتختلف فقط في عدد النيوترونات.",
        "Compare Z = 6 and N = A - Z for both atoms.",
        ["Both have Z = 6 protons (making both Carbon) and 6 electrons in neutral atoms.",
         "Carbon-12 has 12 - 6 = 6 neutrons; Carbon-14 has 14 - 6 = 8 neutrons."],
        "Isotopes share nearly identical chemical behavior because electron shells match.",
        "نقارن العدد الذري وعدد النيوترونات لكل نظير.",
        ["كلاهما يحمل 6 بروتونات لذا كلاهما كربون، وفي الحالة المتعادلة 6 إلكترونات.",
         "كربون-12 فيه 6 نيوترونات بينما كربون-14 فيه 8 نيوترونات."],
        "للنظائر الخصائص الكيميائية نفسها لتشابه إلكتروناتها.",
    ))

    # 3 (Easy): Neutral Magnesium electrons
    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        f"In an electrically neutral Magnesium atom ({m('^{24}_{12}\\text{Mg}')}), how many electrons orbit the nucleus?",
        f"في ذرة مغنيسيوم متعادلة كهربائياً ({m('^{24}_{12}\\text{Mg}')})، كم إلكتروناً يدور حول النواة؟",
        12, [24, 36, 2],
        "In a neutral atom, negative electrons equal positive protons (Z).",
        "في الذرة المتعادلة يتساوى عدد الإلكترونات السالبة مع البروتونات الموجبة (Z).",
        f"Read the atomic number {m('Z = 12')}.",
        [f"The subscript {m('12')} gives the proton count ({m('p^+ = 12')}).",
         f"Electrical neutrality requires {m('e^- = p^+ = 12')} electrons (arranged 2, 8, 2)."],
        f"Total charge: {m('+12 + (-12) = 0')}.",
        "في الذرة المتعادلة عدد الإلكترونات يساوي العدد الذري.",
        [f"العدد الذري السفلي {m('12')} يمثل البروتونات.",
         f"لتعادل الشحنة يكون عدد الإلكترونات {m('12')} (توزيعها 2، 8، 2)."],
        f"الشحنة الكلية {m('+12 - 12 = 0')}.",
        diagram_en=svg_atom_bohr("Mg", 12, 12, [2, 8, 2], "Magnesium Atom"),
        diagram_ar=_ar_svg(svg_atom_bohr("Mg", 12, 12, [2, 8, 2], "Magnesium Atom"),
                           {"Magnesium Atom": "ذرة المغنيسيوم"}),
    ))

    # 4 (Easy): Subatomic particle charges and locations
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        "Which subatomic particles account for nearly all of an atom's <strong>mass</strong>, and where are they located?",
        "أي جسيمات دون ذرية تشكّل معظم <strong>كتلة</strong> الذرة تقريباً، وأين تقع؟",
        [
            ("Protons (+1) and neutrons (0), tightly packed in the central nucleus",
             "البروتونات (+1) والنيوترونات (0)، مجتمعة في النواة المركزية"),
            ("Electrons (-1) and protons (+1), orbiting in outer energy shells",
             "الإلكترونات (-1) والبروتونات (+1)، وتدور في المدارات الخارجية"),
            ("Neutrons (0) and electrons (-1), orbiting outside the nucleus",
             "النيوترونات (0) والإلكترونات (-1)، وتدور خارج النواة"),
            ("Electrons (-1) alone, spread uniformly across empty atomic space",
             "الإلكترونات (-1) وحدها، موزعة في الفراغ الذري"),
        ],
        "Each proton or neutron has ~1 amu, about 1,836 times heavier than one electron.",
        "كتلة البروتون أو النيوترون تقارب 1 وحدة كتلة ذرية، أي أثقل بنحو 1,836 مرة من الإلكترون.",
        "Locate heavy nucleons vs nearly massless shell electrons.",
        ["Protons and neutrons each have mass ~1 amu and reside in the dense nucleus.",
         "Electrons orbit in shells around the nucleus and contribute less than 0.06% of atomic mass."],
        "Mass number A counts only protons + neutrons.",
        "نحدد الجسيمات الثقيلة في النواة مقابل الإلكترونات الخفيفة.",
        ["تتركز الكتلة في النواة حيث يوجد البروتونات والنيوترونات.",
         "الإلكترونات تدور في المدارات وكتلتها ضئيلة جداً تُهمل عند حساب العدد الكتلي."],
        "لذلك يجمع العدد الكتلي البروتونات والنيوترونات فقط.",
    ))

    # 5 (Medium): Sodium ion Na+ electron count
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"A Sodium atom ({m('^{23}_{11}\\text{Na}')}) loses one outer valence electron to form a {m('\\text{Na}^+')} ion. How many electrons remain in the {m('\\text{Na}^+')} ion?",
        f"فقدت ذرة صوديوم ({m('^{23}_{11}\\text{Na}')}) إلكترون تكافؤ واحداً لتكوّن أيون {m('\\text{Na}^+')} الموجب. كم إلكتروناً يتبقى في أيون {m('\\text{Na}^+')}؟",
        10, [11, 12, 22],
        "Losing 1 negatively charged electron creates a +1 cation with 1 fewer electron than protons.",
        "فقدان إلكترون واحد سالب الشحنة ينتج أيوناً موجباً (+1) يقل إلكتروناً واحداً عن البروتونات.",
        f"Apply {m('e^- = Z - \\text{charge}')}.",
        [f"Neutral Na has {m('Z = 11')} protons and {m('11')} electrons ({m('2, 8, 1')}).",
         f"After losing 1 electron, {m('\\text{Na}^+')} has {m('11 - 1 = 10')} electrons ({m('2, 8')}) and charge {m('+1')}."],
        f"Check charge: {m('(+11) + (-10) = +1')}.",
        "نطرح مقدار الشحنة الموجبة من العدد الذري.",
        [f"الصوديوم المتعادل فيه {m('11')} بروتوناً و{m('11')} إلكتروناً.",
         f"بعد فقد إلكترون واحد يتبقى {m('11 - 1 = 10')} إلكترونات بتوزيع مستقر ({m('2, 8')})."],
        f"التحقق: {m('(+11) + (-10) = +1')}.",
        diagram_en=svg_atom_bohr("Na+", 11, 12, [2, 8], "Sodium Ion Na+"),
        diagram_ar=_ar_svg(svg_atom_bohr("Na+", 11, 12, [2, 8], "Sodium Ion Na+"),
                           {"Sodium Ion Na+": "أيون الصوديوم Na+"}),
    ))

    # 6 (Medium): Chloride ion Cl- electron count
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        f"Looking at the Bohr model of a chloride ion ({m('^{35}_{17}\\text{Cl}^-')}), how many <strong>electrons</strong> orbit the nucleus in total?",
        f"انظر إلى نموذج بور لأيون الكلوريد ({m('^{35}_{17}\\text{Cl}^-')})، ما العدد الإجمالي لـ <strong>الإلكترونات</strong> التي تدور حول النواة؟",
        18, [17, 16, 35],
        "A -1 anion gained 1 extra electron beyond its 17 protons.",
        "الأيون السالب (-1) اكتسب إلكتروناً إضافياً واحداً فوق بروتوناته الـ 17.",
        f"Compute {m('e^- = 17 + 1')}.",
        [f"Chlorine has {m('Z = 17')} protons and {m('35 - 17 = 18')} neutrons.",
         f"Gaining 1 electron to fill its 3rd shell gives {m('17 + 1 = 18')} electrons ({m('2, 8, 8')})."],
        f"Charge check: {m('(+17) + (-18) = -1')}.",
        "نضيف إلكتروناً واحداً على العدد الذري 17.",
        [f"الكلور يمتلك {m('17')} بروتوناً و{m('18')} نيوتروناً.",
         f"باكتساب إلكترون لتكوين شحنة {m('-1')} يصبح عدد الإلكترونات {m('17 + 1 = 18')}."],
        f"التحقق: {m('(+17) + (-18) = -1')}.",
        diagram_en=svg_atom_bohr("Cl-", 17, 18, [2, 8, 8], "Chloride Ion Cl-"),
        diagram_ar=_ar_svg(svg_atom_bohr("Cl-", 17, 18, [2, 8, 8], "Chloride Ion Cl-"),
                           {"Chloride Ion Cl-": "أيون الكلوريد Cl-"}),
    ))

    # 7 (Medium): Identifying isotope pair from subatomic table
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        "Four species have the following (protons, neutrons, electrons): W = (8, 8, 8), X = (9, 10, 10), Y = (8, 10, 8), and Z = (7, 8, 10). Which two species are <strong>isotopes of the same element</strong>?",
        "أربع ذرات/أيونات لها الأعداد (بروتونات، نيوترونات، إلكترونات): W = (8, 8, 8)، X = (9, 10, 10)، Y = (8, 10, 8)، Z = (7, 8, 10). أي اثنتين هما <strong>نظيران للعنصر نفسه</strong>؟",
        [
            ("W and Y (both have 8 protons, oxygen, with 8 vs 10 neutrons)",
             "W و Y (كلاهما يمتلك 8 بروتونات للأكسجين، مع 8 مقابل 10 نيوترونات)"),
            ("W and Z (both have 8 neutrons)", "W و Z (كلاهما يمتلك 8 نيوترونات)"),
            ("X and Y (both have 10 neutrons)", "X و Y (كلاهما يمتلك 10 نيوترونات)"),
            ("X and Z (both have 10 electrons)", "X و Z (كلاهما يمتلك 10 إلكترونات)"),
        ],
        "The element identity is fixed solely by proton number (Z), never neutron or electron count.",
        "هوية العنصر يحددها عدد البروتونات فقط، لا النيوترونات ولا الإلكترونات.",
        "Find the pair sharing identical proton count.",
        ["W has 8 protons (O-16) and Y also has 8 protons (O-18), making both Oxygen isotopes.",
         "X has 9 protons (Fluorine) and Z has 7 protons (Nitrogen), so they are different elements even when sharing 10 neutrons or 10 electrons."],
        "Same Z + different N = isotopes.",
        "نبحث عن الزوج المتساوي في عدد البروتونات.",
        ["يمتلك W عدد 8 بروتونات ويمتلك Y عدد 8 بروتونات أيضاً، فكلاهما أكسجين باختلاف النيوترونات (8 و 10).",
         "بينما X (9 بروتونات) و Z (7 بروتونات) عنصران مختلفان تماماً."],
        "تساوي البروتونات واختلاف النيوترونات هو تعريف النظائر.",
    ))

    # 8 (Medium): Finding mass number A of divalent cation X2+
    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        f"An ion {m('\\text{X}^{2+}')} has {m('18')} electrons and {m('20')} neutrons. What is the <strong>mass number</strong> ({m('A')}) of atom {m('\\text{X}')}?",
        f"أيون {m('\\text{X}^{2+}')} يحتوي على {m('18')} إلكتروناً و{m('20')} نيوتروناً. ما <strong>العدد الكتلي</strong> ({m('A')}) للذرة {m('\\text{X}')}؟",
        40, [38, 36, 42],
        "A +2 charge means the atom lost 2 electrons, so protons = 18 + 2 = 20.",
        "الشحنة +2 تعني فقد إلكترونين، لذا عدد البروتونات = 18 + 2 = 20.",
        f"Find {m('Z')} from {m('e^-')} and charge, then compute {m('A = Z + N')}.",
        [f"Since {m('\\text{X}^{2+}')} lost 2 electrons to leave {m('18')}, neutral {m('\\text{X}')} has {m('Z = 18 + 2 = 20')} protons (Calcium).",
         f"Mass number {m('A = 20 + 20 = 40')}."],
        f"Check: {m('^{40}_{20}\\text{Ca}^{2+}')} has {m('20')} p+, {m('20')} n0, {m('18')} e-.",
        "نسترجع عدد البروتونات أولاً ثم نجمعه مع النيوترونات.",
        [f"فقدت الذرة إلكترونين ليصبح الباقي {m('18')}، إذن عدد البروتونات {m('Z = 18 + 2 = 20')} (كالسيوم).",
         f"العدد الكتلي {m('A = 20 + 20 = 40')}."],
        f"التحقق: الكالسيوم-40 له 20 بروتوناً و20 نيوتروناً.",
    ))

    # 9 (Medium): Total subatomic particles in sulfide ion 32S2-
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        f"A sulfide ion is written as {m('^{32}_{16}\\text{S}^{2-}')}. What is the <strong>sum</strong> of all protons, neutrons, and electrons inside this single ion?",
        f"يُكتب أيون الكبريتيد بالصيغة {m('^{32}_{16}\\text{S}^{2-}')}. ما <strong>مجموع</strong> أعداد البروتونات والنيوترونات والإلكترونات في هذا الأيون الواحد؟",
        50, [48, 46, 34],
        "Count p+ = 16, n0 = 32 - 16 = 16, and e- = 16 + 2 = 18, then add all three.",
        "احسب البروتونات (16) والنيوترونات (32-16) والإلكترونات (16+2) ثم اجمعها.",
        f"Evaluate {m('p^+ + n^0 + e^-')}.",
        [f"Protons {m('p^+ = 16')}; Neutrons {m('n^0 = 32 - 16 = 16')}.",
         f"Because of the {m('2-')} charge, electrons {m('e^- = 16 + 2 = 18')}.",
         f"Total subatomic particles = {m('16 + 16 + 18 = 50')}."],
        f"Notice {m('p^+ + n^0 = A = 32')}, plus {m('18')} electrons = {m('50')}.",
        "نحسب عدد كل جسيم ثم نجمع القيم الثلاث.",
        [f"البروتونات = {m('16')}، والنيوترونات = {m('32 - 16 = 16')}.",
         f"بسبب الشحنة {m('-2')} فالإلكترونات = {m('16 + 2 = 18')}.",
         f"المجموع = {m('16 + 16 + 18 = 50')} جسيماً."],
        f"مجموع النواة {m('32')} زائد {m('18')} إلكتروناً يساوي {m('50')}.",
    ))

    # 10 (Hard): Weighted average atomic mass of Chlorine (35.5 amu)
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"Naturally occurring Chlorine consists of {m(r'75\%')} {m('^{35}\\text{Cl}')} (mass {m('35')} amu) and {m(r'25\%')} {m('^{37}\\text{Cl}')} (mass {m('37')} amu). What is the weighted average atomic mass of Chlorine (in amu)?",
        f"يتكون الكلور الطبيعي من {m(r'75\%')} من النظير {m('^{35}\\text{Cl}')} (كتلته {m('35')} amu) و{m(r'25\%')} من النظير {m('^{37}\\text{Cl}')} (كتلته {m('37')} amu). ما متوسط الكتلة الذرية الموزون للكلور (بوحدة amu)؟",
        35.5, [36.0, 35.2, 36.5],
        "Multiply each isotope mass by its decimal abundance and add: 0.75(35) + 0.25(37).",
        "اضرب كتلة كل نظير في نسبته العشرية ثم اجمع الناتجين.",
        f"Compute {m('0.75 \\times 35 + 0.25 \\times 37')}.",
        [f"Contribution from Cl-35: {m('0.75 \\times 35 = 26.25')} amu.",
         f"Contribution from Cl-37: {m('0.25 \\times 37 = 9.25')} amu.",
         f"Weighted average = {m('26.25 + 9.25 = 35.5')} amu."],
        "Because Cl-35 is 3× more abundant, the average lies closer to 35 than to 37.",
        "نحسب المتوسط الموزون بضرب كل كتلة في نسبتها.",
        [f"مساهمة كلور-35 = {m('0.75 \\times 35 = 26.25')}.",
         f"مساهمة كلور-37 = {m('0.25 \\times 37 = 9.25')}.",
         f"المجموع = {m('35.5')} amu."],
        "يميل المتوسط نحو 35 لأن وفرته ثلاث أضعاف وفرة 37.",
    ))

    # 11 (Hard): Reverse isotope abundance for Boron-11 (80%)
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"Boron has two natural isotopes: {m('^{10}\\text{B}')} (mass {m('10')} amu) and {m('^{11}\\text{B}')} (mass {m('11')} amu). Given that Boron's average atomic mass is {m('10.8')} amu, what percentage of natural Boron is {m('^{11}\\text{B}')}?",
        f"للبورون نظيران طبيعيان: {m('^{10}\\text{B}')} (كتلته {m('10')} amu) و{m('^{11}\\text{B}')} (كتلته {m('11')} amu). إذا كان متوسط الكتلة الذرية للبورون {m('10.8')} amu، فما النسبة المئوية للنظير {m('^{11}\\text{B}')}؟",
        80, [20, 75, 85],
        "Let fraction of B-11 be x and B-10 be 1 - x; solve 10(1 - x) + 11x = 10.8.",
        "افرض نسبة البورون-11 تساوي x ونسبة البورون-10 تساوي (1 - x)، ثم حل 10(1 - x) + 11x = 10.8.",
        f"Solve {m('10(1 - x) + 11x = 10.8')}.",
        [f"Expanding gives {m('10 - 10x + 11x = 10.8')}, simplifying to {m('10 + x = 10.8')}.",
         f"Thus {m('x = 0.8 = 80\\%')} for {m('^{11}\\text{B}')} (and {m('20\\%')} for {m('^{10}\\text{B}')})."],
        f"Check: {m('0.20(10) + 0.80(11) = 2.0 + 8.8 = 10.8')} amu.",
        "نكوّن معادلة خطية للمتوسط الموزون ونحلها.",
        [f"نكتب {m('10(1 - x) + 11x = 10.8')} فنجد {m('10 + x = 10.8')}.",
         f"إذن {m('x = 0.8')} أي {m('80\\%')} للنظير {m('^{11}\\text{B}')}."],
        f"التحقق: {m('0.2(10) + 0.8(11) = 10.8')}.",
        suffix=r"\%",
    ))

    # 12 (Hard): Copper average atomic mass (63.6 amu)
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        f"A sample of Copper consists of {m(r'70\%')} {m('^{63}\\text{Cu}')} ({m('63')} amu) and {m(r'30\%')} {m('^{65}\\text{Cu}')} ({m('65')} amu). What is the weighted average atomic mass of this Copper sample (in amu)?",
        f"تتكون عينة نحاس من {m(r'70\%')} من {m('^{63}\\text{Cu}')} ({m('63')} amu) و{m(r'30\%')} من {m('^{65}\\text{Cu}')} ({m('65')} amu). ما متوسط الكتلة الذرية لهذه العينة (بوحدة amu)؟",
        63.6, [64.0, 64.4, 63.3],
        "Multiply 63 by 0.70 and 65 by 0.30, then add.",
        "اضرب 63 في 0.70 و65 في 0.30 ثم اجمعهما.",
        f"Compute {m('0.70 \\times 63 + 0.30 \\times 65')}.",
        [f"{m('0.70 \\times 63 = 44.1')} amu and {m('0.30 \\times 65 = 19.5')} amu.",
         f"Average atomic mass = {m('44.1 + 19.5 = 63.6')} amu."],
        f"Shortcut: {m('63 + 0.30 \\times (65 - 63) = 63 + 0.6 = 63.6')} amu.",
        "نحسب المجموع الموزون للكتلتين.",
        [f"{m('0.70 \\times 63 = 44.1')} و{m('0.30 \\times 65 = 19.5')}.",
         f"المجموع = {m('63.6')} amu."],
        f"التحقق السريع: {m('63 + 0.3 \\times 2 = 63.6')}.",
    ))

    # 13 (Hard): Algebraic subatomic puzzle for Al3+
    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        f"A trivalent cation {m('\\text{M}^{3+}')} has {m('10')} electrons, and its nucleus contains {m('1')} more neutron than proton. What is the mass number ({m('A')}) of {m('\\text{M}')}?",
        f"أيون ثلاثي التكافؤ {m('\\text{M}^{3+}')} يمتلك {m('10')} إلكترونات، وتحتوي نواته على نيوترون واحد أكثر من عدد بروتوناته. ما العدد الكتلي ({m('A')}) للعنصر {m('\\text{M}')}؟",
        27, [26, 21, 24],
        "First find protons Z from e- = 10 and charge +3, then find neutrons = Z + 1.",
        "أوجد عدد البروتونات Z أولاً من الإلكترونات 10 والشحنة +3، ثم أوجد النيوترونات = Z + 1.",
        f"Compute {m('Z = 10 + 3')}, then {m('N = Z + 1')}, then {m('A = Z + N')}.",
        [f"Since {m('\\text{M}^{3+}')} lost 3 electrons to have {m('10')}, {m('Z = 10 + 3 = 13')} protons (Aluminum).",
         f"Neutrons {m('N = 13 + 1 = 14')}.",
         f"Mass number {m('A = 13 + 14 = 27')}."],
        f"Aluminum-27 ({m('^{27}_{13}\\text{Al}^{3+}')}) has 13 p+, 14 n0, 10 e-.",
        "نحسب Z ثم N ثم A بالترتيب.",
        [f"فقدت الذرة 3 إلكترونات فبقي {m('10')}، إذن {m('Z = 13')} بروتوناً (الألومنيوم).",
         f"النيوترونات {m('N = 13 + 1 = 14')}، فالعدد الكتلي {m('A = 13 + 14 = 27')}."],
        f"التحقق: {m('^{27}_{13}\\text{Al}^{3+}')}.",
    ))

    # 14 (Hard): Isoelectronic ionic radius comparison
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        f"The four species {m('\\text{O}^{2-}')}, {m('\\text{F}^-')}, {m('\\text{Ne}')}, and {m('\\text{Mg}^{2+}')} are isoelectronic: every one has exactly {m('10')} electrons ({m('2, 8')}). Which species has the <strong>smallest</strong> radius, and why?",
        f"الجسيمات الأربعة {m('\\text{O}^{2-}')} و{m('\\text{F}^-')} و{m('\\text{Ne}')} و{m('\\text{Mg}^{2+}')} متساوية الإلكترونات: لكل منها {m('10')} إلكترونات ({m('2, 8')}). أيها يمتلك <strong>أصغر</strong> نصف قطر، ولماذا؟",
        [
            (m("\\text{Mg}^{2+}") + " — its 12 protons exert the strongest inward pull on the 10 electrons",
             m("\\text{Mg}^{2+}") + " — لأن نواته تحوي 12 بروتوناً تجذب الإلكترونات العشرة بأقوى شد نحو الداخل"),
            (m("\\text{O}^{2-}") + " — its 8 protons pull the 10 electrons tightest",
             m("\\text{O}^{2-}") + " — لأن 8 بروتونات تشد الإلكترونات بقوة أكبر"),
            (m("\\text{Ne}") + " — noble gases have zero nuclear attraction",
             m("\\text{Ne}") + " — لأن الغازات النبيلة تنعدم فيها الجاذبية النووية"),
            ("All four have the exact same radius because electron counts are identical",
             "جميعها متساوية تماماً في نصف القطر لتساوي عدد إلكتروناتها"),
        ],
        "When electron shells are identical (10 e-), compare the positive nuclear charge (protons Z).",
        "عند تساوي الأغلفة الإلكترونية (10 إلكترونات)، قارن الشحنة الموجبة للنواة (عدد البروتونات Z).",
        "Rank proton counts: O (8), F (9), Ne (10), Mg (12).",
        ["All four possess the same 2 filled shells [2, 8], so shielding is similar.",
         "Mg²⁺ has the largest nuclear charge (+12), pulling the 10-electron cloud closest to the nucleus; O²⁻ (+8) is largest."],
        "Higher Z across an isoelectronic series always shrinks ionic radius.",
        "نقارن عدد البروتونات الجاذبة للسحابة الإلكترونية نفسها.",
        ["تمتلك الجسيمات الأربعة الأغلفة نفسها [2، 8] و10 إلكترونات.",
         "يمتلك أيون المغنيسيوم Mg²⁺ أكبر عدد من البروتونات (12)، فيجذب الإلكترونات العشرة بقوة أكبر ويُصغّر نصف قطره."],
        "في السلسلة متساوية الإلكترونات كلما زاد Z صغر الحجم.",
        diagram_en=svg_atom_bohr("Mg2+", 12, 12, [2, 8], "Isoelectronic 10 e- Cloud"),
        diagram_ar=_ar_svg(svg_atom_bohr("Mg2+", 12, 12, [2, 8], "Isoelectronic 10 e- Cloud"),
                           {"Isoelectronic 10 e- Cloud": "سحابة 10 إلكترونات متساوية"}),
    ))
    return qs


def _gen_sci_b08(start_idx: int) -> list[dict]:
    """G9-SCI-B08: Periodic table groups/periods & valence electron trends."""
    bp = "G9-SCI-B08"
    qs: list[dict] = []

    # 0 (Easy): Locate Sulfur (2, 8, 6) -> Period 3, Group 16
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        "Using the Bohr diagram of Sulfur (electron configuration 2, 8, 6), which <strong>Period</strong> and <strong>Group</strong> does Sulfur belong to in the modern periodic table?",
        "من نموذج بور لذرة الكبريت (التوزيع الإلكتروني 2، 8، 6)، ما <strong>الدورة</strong> و<strong>المجموعة</strong> اللتان ينتمي إليهما الكبريت في الجدول الدوري الحديث؟",
        [
            ("Period 3, Group 16 (6 valence electrons)", "الدورة 3، المجموعة 16 (6 إلكترونات تكافؤ)"),
            ("Period 6, Group 3 (3 valence electrons)", "الدورة 6، المجموعة 3 (3 إلكترونات تكافؤ)"),
            ("Period 3, Group 6 (8 valence electrons)", "الدورة 3، المجموعة 6 (8 إلكترونات تكافؤ)"),
            ("Period 2, Group 16 (2 valence electrons)", "الدورة 2، المجموعة 16 (إلكترونان تكافؤ)"),
        ],
        "Count occupied shells for the Period, and valence (outermost) electrons for the main-group number.",
        "عدد مستويات الطاقة المشغولة يحدد الدورة، وإلكترونات المستوى الأخير تحدد المجموعة.",
        "3 shells = Period 3; 6 outer electrons = Group 16.",
        ["Sulfur occupies 3 electron shells (2 in K, 8 in L, 6 in M) → Period 3.",
         "Having 6 valence electrons in the outer shell places it in Group 16 (the oxygen/chalcogen family)."],
        "Main-group numbers 13–18 equal 10 + valence electrons (10 + 6 = 16).",
        "نعد المدارات للدورة وإلكترونات المدار الأخير للمجموعة.",
        ["تشغل إلكترونات الكبريت 3 مستويات طاقة، إذن يقع في الدورة 3.",
         "يحتوي المستوى الأخير على 6 إلكترونات تكافؤ، لذا يقع في المجموعة 16."],
        "المجموعات 13–18 تساوي 10 + عدد إلكترونات التكافؤ.",
        diagram_en=svg_atom_bohr("S", 16, 16, [2, 8, 6], "Sulfur [2, 8, 6]"),
        diagram_ar=_ar_svg(svg_atom_bohr("S", 16, 16, [2, 8, 6], "Sulfur [2, 8, 6]"),
                           {"Sulfur [2, 8, 6]": "الكبريت [2، 8، 6]"}),
    ))

    # 1 (Easy): Noble gases inertness
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        "Look at the Bohr model of Argon (Z = 18, shells 2, 8, 8). Why are Argon and other Group 18 <strong>noble gases</strong> chemically unreactive under normal conditions?",
        "انظر إلى نموذج بور للأرجون (Z = 18، التوزيع 2، 8، 8). لماذا يُعد الأرجون وبقية <strong>الغازات النبيلة</strong> في المجموعة 18 خاملاً كيميائياً في الظروف العادية؟",
        [
            ("Their outermost valence electron shell is completely filled (octet stability), so they neither gain nor lose electrons easily",
             "لأن مستوى الطاقة الأخير مكتمل تماماً بالإلكترونات (8 إلكترونات)، فلا تميل لفقد أو كسب الإلكترونات"),
            ("Their nuclei contain zero protons, creating no electric field",
             "لأن نواتها تخلو من البروتونات فلا تملك شحنة كهربائية"),
            ("They have only 1 valence electron tightly bonded to the core",
             "لأنها تملك إلكترون تكافؤ واحداً فقط"),
            ("All noble gases are heavy solid metals at room temperature",
             "لأن جميع الغازات النبيلة فلزات صلبة ثقيلة"),
        ],
        "Notice the outer 3rd shell holds 8 valence electrons (full octet).",
        "لاحظ أن المستوى الثالث الأخير يحتوي على 8 إلكترونات مكتملة.",
        "Connect filled outer octet to chemical stability.",
        ["Elements react primarily to achieve a full outer electron shell (2 for He, 8 for Ne/Ar/Kr).",
         "Because Group 18 atoms already have complete valence shells, they have minimal tendency to form chemical bonds."],
        "Neon signs and Argon-filled lightbulbs exploit this inertness.",
        "نربط اكتمال الغلاف الخارجي بالاستقرار الكيميائي.",
        ["تميل الذرات للتفاعل للوصول إلى غلاف خارجي مكتمل بـ 8 إلكترونات (أو 2 للهيليوم).",
         "الغازات النبيلة ممتلئة الغلاف أصلاً لذا هي مستقرة وخاملة كيميائياً."],
        "تُستخدم في المصابيح لمنع احتراق الفتيل لخمولها.",
        diagram_en=svg_atom_bohr("Ar", 18, 22, [2, 8, 8], "Argon [2, 8, 8]"),
        diagram_ar=_ar_svg(svg_atom_bohr("Ar", 18, 22, [2, 8, 8], "Argon [2, 8, 8]"),
                           {"Argon [2, 8, 8]": "الأرجون [2، 8، 8]"}),
    ))

    # 2 (Easy): Alkali metals (Group 1) properties
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        "Which description best fits the <strong>alkali metals</strong> (Group 1: Li, Na, K) in the periodic table?",
        "أي وصف ينطبق بدقة على <strong>الفلزات القلوية</strong> (المجموعة 1: الليثيوم والصوديوم والبوتاسيوم) في الجدول الدوري؟",
        [
            ("Soft silvery metals with 1 valence electron that react vigorously with water and form +1 ions",
             "فلزات فضية لينة لها إلكترون تكافؤ واحد، تتفاعل بعنف مع الماء وتكوّن أيونات (+1)"),
            ("Unreactive monatomic gases with 8 valence electrons",
             "غازات أحادية الذرة خاملة لها 8 إلكترونات تكافؤ"),
            ("Toxic nonmetals with 7 valence electrons that form -1 halide ions",
             "لافلزات سامة لها 7 إلكترونات تكافؤ وتكوّن أيونات (-1)"),
            ("Brittle semiconductors located strictly along the metalloid staircase",
             "أشباه موصلات هشة تقع على الخط المتعرج لأشباه الفلزات"),
        ],
        "Group 1 elements hold a single outer electron that is easily donated.",
        "تمتلك عناصر المجموعة الأولى إلكترون تكافؤ واحداً تفقدها بسهولة بالغة.",
        "Match Group 1 valence (1 e-) to high metallic reactivity and +1 cation charge.",
        ["With 1 loosely held valence electron, alkali metals lose that electron rapidly to water or halogens.",
         "Because they lose 1 negative electron, they reliably form +1 cations (Li⁺, Na⁺, K⁺) and must be stored under oil."],
        "Hydrogen (top of Group 1) is an exception—it is a nonmetal gas.",
        "نربط إلكترون التكافؤ الوحيد بنشاطها الفلزي وتكوين أيونات (+1).",
        ["فقدان إلكترون التكافؤ الوحيد يجعلها شديدة النشاط مع الماء والهواء.",
         "عند الفقد تتحول إلى أيونات موجبة (+1) لذا تُحفظ تحت الزيت."],
        "الهيدروجين في أعلى العمود الأول استثناء كونه لافلزاً غازياً.",
    ))

    # 3 (Easy): Halogens (Group 17)
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        "Elements in Group 17 (F, Cl, Br, I) are known as the <strong>halogens</strong>. How many valence electrons do halogens have, and what ion charge do they typically form when reacting with metals?",
        "تُعرف عناصر المجموعة 17 (F, Cl, Br, I) باسم <strong>الهالوجينات</strong>. كم إلكترون تكافؤ لديها، وما شحنة الأيون التي تكوّنها عادةً عند التفاعل مع الفلزات؟",
        [
            ("7 valence electrons; form -1 anions (such as Cl⁻)",
             "7 إلكترونات تكافؤ؛ وتكوّن أيونات سالبة (-1) مثل Cl⁻"),
            ("1 valence electron; form +1 cations",
             "إلكترون تكافؤ واحد؛ وتكوّن أيونات (+1)"),
            ("2 valence electrons; form +2 cations",
             "إلكترونان تكافؤ؛ وتكوّن أيونات (+2)"),
            ("8 valence electrons; form no ions at all",
             "8 إلكترونات تكافؤ؛ ولا تكوّن أي أيونات"),
        ],
        "Group 17 sits one column left of the Noble Gases (Group 18).",
        "تقع المجموعة 17 قبل عمود الغازات النبيلة (المجموعة 18) بعمود واحد فقط.",
        "7 valence electrons need 1 more electron to reach a stable octet of 8.",
        ["Group 17 atoms each carry 7 outer valence electrons.",
         "Gaining 1 electron fills the octet (8) and gives a net -1 charge (F⁻, Cl⁻, Br⁻)."],
        "Halogen means 'salt-former' (e.g., NaCl, KBr).",
        "تحتاج الذرة إلى إلكترون واحد لتكمل الثمانية المستقرة.",
        ["كل ذرة هالوجين تحمل 7 إلكترونات في غلافها الخارجي.",
         "اكتساب إلكترون واحد يكمل الثمانية ويعطي شحنة (-1)."],
        "كلمة هالوجين تعني مكوّن الأملاح (مثل ملح الطعام NaCl).",
    ))

    # 4 (Easy): Group 2 valence & Bohr check
    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        f"Based on the Bohr model of Beryllium ({m('Z = 4')}) or any Group 2 Alkaline Earth metal such as Calcium ({m('Z = 20')}), how many <strong>valence electrons</strong> are present in the outermost shell?",
        f"اعتماداً على نموذج بور للبيريليوم ({m('Z = 4')}) أو أي عنصر في المجموعة 2 (الفلزات القلوية الأرضية كالمغنيسيوم والكالسيوم)، كم عدد <strong>إلكترونات التكافؤ</strong> في الغلاف الخارجي؟",
        2, [4, 6, 8],
        "All elements in Group 2 share the exact same number of outer valence electrons.",
        "جميع عناصر المجموعة 2 تتشارك العدد نفسه من إلكترونات التكافؤ.",
        "Read the outermost shell electron count in [2, 2].",
        [f"Beryllium ({m('Z = 4')}) has {m('2')} inner electrons and {m('2')} outer valence electrons.",
         f"Likewise Magnesium ({m('[2, 8, 2]')}) and Calcium ({m('[2, 8, 8, 2]')}) all have {m('2')} valence electrons."],
        "Group 2 elements lose these 2 valence electrons to form +2 ions.",
        "نقرأ عدد الإلكترونات في الغلاف الأخير.",
        [f"توزيع البيريليوم ({m('2, 2')}) والمغنيسيوم ({m('2, 8, 2')})، لذا فعدد إلكترونات التكافؤ {m('2')}."],
        "تفقد عناصر المجموعة 2 هذين الإلكترونين لتكوين أيونات (+2).",
        diagram_en=svg_atom_bohr("Be", 4, 5, [2, 2], "Beryllium [2, 2]"),
        diagram_ar=_ar_svg(svg_atom_bohr("Be", 4, 5, [2, 2], "Beryllium [2, 2]"),
                           {"Beryllium [2, 2]": "البيريليوم [2، 2]"}),
    ))

    # 5 (Medium): Matching chemical behavior by valence shell (Z=9 and Z=17)
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"Fluorine has atomic number {m('Z = 9')} (electron shells {m('[2, 7]')}). Which other element's atomic number among {m('11, 14, 17, 18')} shares the <strong>most similar</strong> chemical properties to Fluorine?",
        f"عنصر الفلور عدده الذري {m('Z = 9')} وتوزيعه الإلكتروني {m('[2, 7]')}. أي عدد ذري من بين {m('11, 14, 17, 18')} يمتلك خصائص كيميائية <strong>مماثلة جداً</strong> للفلور؟",
        17, [11, 14, 18],
        "Elements in the same Group have the same number of valence electrons (7).",
        "العناصر الواقعة في المجموعة نفسها تمتلك عدد إلكترونات التكافؤ نفسه (7).",
        "Write shell configurations for 11, 14, 17, and 18 and match 7 valence electrons.",
        [f"{m('Z = 11')} is {m('[2, 8, 1]')} (1 valence); {m('Z = 14')} is {m('[2, 8, 4]')} (4 valence).",
         f"{m('Z = 17')} (Chlorine) is {m('[2, 8, 7]')}, matching Fluorine's {m('7')} valence electrons in Group 17!"],
        f"{m('Z = 18')} is {m('[2, 8, 8]')} (unreactive noble gas Argon).",
        "نوزع الإلكترونات لنبحث عن العنصر الذي ينتهي غلافه بـ 7 إلكترونات.",
        [f"توزيع {m('Z = 17')} (الكلور) هو {m('[2, 8, 7]')}، أي يمتلك {m('7')} إلكترونات تكافؤ مثل الفلور {m('[2, 7]')}.",
         "العنصران في المجموعة 17 (الهالوجينات) لذا يتشابه سلوكهما الكيميائي."],
        "توزيع 11 ينتهي بـ 1، و14 بـ 4، و18 بـ 8.",
        diagram_en=svg_atom_bohr("F", 9, 10, [2, 7], "Fluorine [2, 7]"),
        diagram_ar=_ar_svg(svg_atom_bohr("F", 9, 10, [2, 7], "Fluorine [2, 7]"),
                           {"Fluorine [2, 7]": "الفلور [2، 7]"}),
    ))

    # 6 (Medium): Atomic radius trend across Period 3
    qs.append(make_science_concept_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        "Moving left to right across Period 3 from Sodium (Na, Z = 11) to Chlorine (Cl, Z = 17), how and why does <strong>atomic radius</strong> change?",
        "عند الانتقال من اليسار إلى اليمين عبر الدورة الثالثة من الصوديوم (Na, Z = 11) إلى الكلور (Cl, Z = 17)، كيف يتغير <strong>نصف القطر الذري</strong> ولماذا؟",
        [
            ("It decreases, because increasing nuclear proton charge pulls electrons in the same 3rd shell closer to the nucleus",
             "ينقص، لأن زيادة الشحنة الموجبة للبروتونات تجذب إلكترونات المستوى الثالث نفسه بقوة أكبر نحو النواة"),
            ("It increases, because each element adds a brand-new 4th, 5th, and 6th shell",
             "يزداد، لأن كل عنصر يضيف مستوى طاقة رابعاً وخامساً جديداً"),
            ("It stays identical across the entire period because all have 3 shells",
             "يبقى متساوياً تماماً لأنها جميعاً تمتلك 3 مستويات طاقة"),
            ("It decreases only for metals and then jumps tenfold at Silicon",
             "ينقص للفلزات فقط ثم يقفز عشرة أضعاف عند السيليكون"),
        ],
        "All Period 3 elements have 3 shells, so compare the growing positive nuclear pull (+11 → +17).",
        "جميع عناصر الدورة 3 لها 3 مستويات طاقة، ففكّر في تزايد شحنة النواة الموجبة (+11 ← +17).",
        "Balance constant shell number (3) against increasing nuclear charge (Z).",
        ["Moving across Period 3 adds electrons into the SAME 3rd shell while adding protons to the nucleus.",
         "Higher positive charge (+17 in Cl vs +11 in Na) pulls the valence shell noticeably inward, shrinking atomic radius."],
        "Down a group, radius increases because whole new shells are added.",
        "نقارن ثبات عدد المستويات مع ازدياد جاذبية النواة.",
        ["في الدورة الثالثة تضاف الإلكترونات إلى الغلاف الثالث نفسه بينما تزداد البروتونات في النواة.",
         "زيادة الجذب النووي تشد الغلاف الخارجي نحو الداخل فيصغر نصف القطر."],
        "أما النزول في المجموعة فيزيد الحجم لإضافة مستويات جديدة.",
    ))

    # 7 (Medium): Group 1 reactivity trend (K > Na > Li)
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        "When dropped into water, Lithium (Period 2) fizzes gently, Sodium (Period 3) melts and darts rapidly, and Potassium (Period 4) ignites immediately with a lilac flame. Why does alkali metal reactivity <strong>increase</strong> down Group 1?",
        "عند وضعها في الماء، يفور الليثيوم (الدورة 2) ببطء، وينصهر الصوديوم (الدورة 3) ويفور بقوة، ويشتعل البوتاسيوم (الدورة 4) فوراً بلهب بنفسجي. لماذا <strong>يزداد</strong> نشاط الفلزات القلوية نزولاً في المجموعة الأولى؟",
        [
            ("Larger atomic radius and extra inner shielding shells place the single valence electron farther from the nucleus, making it easier to lose",
             "كبر نصف القطر وزيادة الأغلفة الحاجبة يبعدان إلكترون التكافؤ الوحيد عن النواة فيسهل فقده"),
            ("Potassium has more protons so it holds its outer electron tighter than Lithium",
             "يمتلك البوتاسيوم بروتونات أكثر فتجذب إلكترونه الخارجي بقوة أكبر من الليثيوم"),
            ("Lithium has 7 valence electrons while Potassium has only 1",
             "يمتلك الليثيوم 7 إلكترونات تكافؤ بينما للبوتاسيوم إلكترون واحد"),
            ("Water molecules only react with atoms containing 4 shells",
             "لا يتفاعل الماء إلا مع الذرات التي تحوي 4 مستويات طاقة"),
        ],
        "Alkali metals react by LOSING 1 electron; losing an electron is easier when it sits farther away and shielded.",
        "تتفاعل الفلزات القلوية بفقد إلكترون واحد؛ وكلما ابتعد الإلكترون عن النواة سهل نزعه.",
        "Relate atomic distance + inner-shell shielding to ease of electron loss.",
        ["Descending Group 1 adds full inner shells (2 → 3 → 4 shells), shielding the valence electron from nuclear attraction.",
         "With weaker hold on its 4th-shell electron, Potassium loses that electron with far less energy than Lithium."],
        "Nonmetal halogens show the opposite reactivity trend (F > Cl > Br > I).",
        "نربط زيادة الحجم والبعد عن النواة بسهولة فقدان الإلكترون.",
        ["النزول في المجموعة الأولى يضيف مستويات داخلية تحجب جذب النواة عن الإلكترون الخارجي.",
         "ضعف الارتباط يجعل فقد إلكترون البوتاسيوم أسرع وأعنف من الليثيوم."],
        "اللافلزات في المجموعة 17 تعكس هذا الاتجاه لأنها تكتسب إلكترونات.",
    ))

    # 8 (Medium): Halogen reactivity trend (F > Cl > Br)
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        "In Group 17 (halogens), Fluorine (Z = 9) is chemically more reactive than Chlorine (Z = 17) and Bromine (Z = 35). Why does halogen reactivity <strong>decrease</strong> going down Group 17?",
        "في المجموعة 17 (الهالوجينات)، الفلور (Z = 9) أنشط كيميائياً من الكلور (Z = 17) والبروم (Z = 35). لماذا <strong>يقل</strong> نشاط الهالوجينات نزولاً في المجموعة؟",
        [
            ("Halogens react by gaining an electron; a smaller Fluorine atom pulls an incoming electron much closer to its nucleus than larger Br or I",
             "تتفاعل الهالوجينات باكتساب إلكترون؛ والفلور الأصغر حجماً يجذب الإلكترون الجديد بقرب وقوة أكبر من البروم واليود"),
            ("Bromine already has 8 valence electrons so it never reacts",
             "يمتلك البروم 8 إلكترونات تكافؤ بالفعل فلا يتفاعل"),
            ("Fluorine reacts by losing 7 electrons faster than Bromine",
             "يتفاعل الفلور بفقد 7 إلكترونات أسرع من البروم"),
            ("Chlorine and Bromine cannot form ionic compounds with Sodium",
             "يعجز الكلور والبروم عن تكوين مركبات أيونية مع الصوديوم"),
        ],
        "Contrast metals (want to lose e-) vs nonmetals (want to gain e-): a smaller radius helps attract an incoming e-.",
        "اللافلزات تسعى لاكتساب إلكترون؛ والذرة الأصغر والأقرب نواتها للغلاف الأخير تجذبه بقوة أكبر.",
        "Link smaller atomic radius + fewer shielding shells to stronger electron affinity.",
        ["Halogens need 1 electron to fill their outer shell.",
         "In tiny Fluorine (2 shells), the incoming electron feels strong attraction close to the nucleus; in larger Bromine (4 shells), distance and shielding weaken attraction."],
        "Hence Cl₂ can displace Br⁻ from NaBr, and F₂ displaces Cl⁻.",
        "نربط صغر نصف القطر بقوة جذب الإلكترون المكتسب.",
        ["تكتسب الهالوجينات إلكتروناً لإكمال غلافها الخارجي.",
         "في الفلور الصغير (غلافان) يكون الغلاف الخارجي قريباً جداً من النواة الموجبة فيجذب الإلكترون بشدة أكبر."],
        "لذا يطرد الكلور البروم من أملاحه في تفاعلات الإحلال.",
    ))

    # 9 (Medium): Classifying Period 3 elements (Na, Si, Cl, Ar)
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        "Consider four Period 3 elements: Sodium (Z = 11), Silicon (Z = 14), Chlorine (Z = 17), and Argon (Z = 18). Which sequence correctly lists (1) conductive shiny metal, (2) microchip metalloid, (3) reactive nonmetal gas, and (4) inert gas?",
        "لديك أربعة عناصر في الدورة الثالثة: الصوديوم (Z=11)، السيليكون (Z=14)، الكلور (Z=17)، الأرجون (Z=18). أي ترتيب يطابق بالترتيب: (1) فلز موصل لامع، (2) شبه فلز للشرائح، (3) لافلز نشط، (4) غاز خامل؟",
        [
            ("Na (11), Si (14), Cl (17), Ar (18)", "Na (11)، ثم Si (14)، ثم Cl (17)، ثم Ar (18)"),
            ("Cl (17), Ar (18), Na (11), Si (14)", "Cl (17)، ثم Ar (18)، ثم Na (11)، ثم Si (14)"),
            ("Si (14), Na (11), Ar (18), Cl (17)", "Si (14)، ثم Na (11)، ثم Ar (18)، ثم Cl (17)"),
            ("Na (11), Cl (17), Si (14), Ar (18)", "Na (11)، ثم Cl (17)، ثم Si (14)، ثم Ar (18)"),
        ],
        "As you scan left-to-right across Period 3, elements transition from Metal → Metalloid → Nonmetal → Noble Gas.",
        "من اليسار إلى اليمين في الدورة الثالثة تتدرج العناصر: فلز ← شبه فلز ← لافلز ← غاز نبيل.",
        "Map Groups 1, 14, 17, 18 across Period 3.",
        ["Z = 11 (Na, Group 1) is a soft conductive metal; Z = 14 (Si, Group 14) is the classic semiconductor metalloid.",
         "Z = 17 (Cl, Group 17) is a reactive nonmetal halogen; Z = 18 (Ar, Group 18) is an inert noble gas."],
        "Metallic character decreases steadily left-to-right across every period.",
        "نربط أرقام المجموعات بالخواص الدورية في الدورة الثالثة.",
        ["الصوديوم (مجموعة 1) فلز موصل، والسيليكون (مجموعة 14) شبه فلز موصل جزئياً للشرائح.",
         "الكلور (مجموعة 17) لافلز نشط، والأرجون (مجموعة 18) غاز نبيل خامل."],
        "تقل الصفة الفلزية بالاتجاه يميناً في الدورة.",
    ))

    # 10 (Hard): Ionization energy jump puzzle -> Group 2
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"A Period 3 element {m('\\text{E}')} has successive ionization energies {m('IE_1 = 738')}, {m('IE_2 = 1,451')}, and {m('IE_3 = 7,733')} kJ/mol. Based on the huge jump after removing the 2nd electron, how many <strong>valence electrons</strong> does {m('\\text{E}')} have?",
        f"عنصر {m('\\text{E}')} في الدورة الثالثة طاقات تأينه المتتابعة هي {m('IE_1 = 738')} و{m('IE_2 = 1,451')} و{m('IE_3 = 7,733')} kJ/mol. بناءً على القفزة الهائلة عند نزع الإلكترون الثالث، كم <strong>إلكترون تكافؤ</strong> يمتلكه العنصر {m('\\text{E}')}؟",
        2, [1, 3, 8],
        "The sudden 5× jump in ionization energy happens when you break into a stable filled inner shell.",
        "القفزة الهائلة تحدث عند محاولة نزع إلكترون من الغلاف الداخلي الممتلئ المستقر.",
        "Count how many electrons were removed easily before the giant jump.",
        [f"Removing the 1st ({m('738')}) and 2nd ({m('1,451')}) electrons requires modest energy.",
         f"Removing the 3rd electron jumps over fivefold to {m('7,733')} kJ/mol because it comes from the filled inner 2nd shell ({m('[2, 8]')}).",
         f"Therefore {m('\\text{E}')} has {m('2')} valence electrons (Magnesium, Group 2)."],
        "Group 2 elements always display a huge jump between IE₂ and IE₃.",
        "نعدّ الإلكترونات السهلة النزع قبل القفزة الكبيرة.",
        [f"نزع الإلكترون الأول ({m('738')}) والثاني ({m('1,451')}) يحتاج طاقة معتدلة.",
         f"الإلكترون الثالث يقفز إلى {m('7,733')} لأنه داخل غلاف داخلي مكتمل ومستقر.",
         f"إذن عدد إلكترونات التكافؤ {m('2')} (المغنيسيوم في المجموعة 2)."],
        "القفزة بين التأين الثاني والثالث تميز عناصر المجموعة 2.",
    ))

    # 11 (Hard): Unknown Period 3 element Q2- is [2, 8, 8] -> Z = 16
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"A Period 3 nonmetal {m('\\text{Q}')} gains electrons to form the anion {m('\\text{Q}^{2-}')}, which then has the noble-gas shell configuration {m('[2, 8, 8]')}. What is the <strong>atomic number</strong> ({m('Z')}) of neutral element {m('\\text{Q}')}?",
        f"يكتسب لافلز {m('\\text{Q}')} من الدورة الثالثة إلكترونات ليكوّن الأيون {m('\\text{Q}^{2-}')} الذي يصبح توزيعه مماثلاً للغاز النبيل {m('[2, 8, 8]')}. ما <strong>العدد الذري</strong> ({m('Z')}) للعنصر {m('\\text{Q}')} المتعادل؟",
        16, [18, 14, 20],
        "Count total electrons in Q²⁻ (18), then subtract the 2 gained electrons to get neutral Q's protons.",
        "اجمع إلكترونات الأيون Q²⁻ (18)، ثم اطرح الإلكترونين المكتسبين لإيجاد العدد الذري للذرة المتعادلة.",
        f"Compute {m('Z = (2 + 8 + 8) - 2')}.",
        [f"The ion {m('\\text{Q}^{2-}')} contains {m('2 + 8 + 8 = 18')} electrons.",
         f"Because the {m('2-')} charge came from gaining {m('2')} electrons, neutral {m('\\text{Q}')} had {m('18 - 2 = 16')} electrons and {m('Z = 16')} protons (Sulfur)."],
        f"Neutral Sulfur has configuration {m('[2, 8, 6]')} in Group 16.",
        "نطرح الشحنة السالبة المكتسبة من عدد إلكترونات الأيون.",
        [f"الأيون {m('\\text{Q}^{2-}')} يحتوي على {m('2 + 8 + 8 = 18')} إلكتروناً.",
         f"بما أنه اكتسب إلكترونين ليحمل شحنة {m('-2')}، فإن الذرة المتعادلة لها {m('18 - 2 = 16')} بروتوناً (الكبريت)."],
        f"توزيع الكبريت المتعادل {m('[2, 8, 6]')}.",
        diagram_en=svg_atom_bohr("Q2-", 16, 16, [2, 8, 8], "Anion Q2- [2, 8, 8]"),
        diagram_ar=_ar_svg(svg_atom_bohr("Q2-", 16, 16, [2, 8, 8], "Anion Q2- [2, 8, 8]"),
                           {"Anion Q2- [2, 8, 8]": "الأيون Q2- [2، 8، 8]"}),
    ))

    # 12 (Hard): Why Hydrogen sits above Group 1 yet is a nonmetal
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        "Hydrogen (Z = 1) is placed above Group 1 in the periodic table, yet unlike Lithium and Sodium it is a colorless diatomic gas (H₂) that forms covalent bonds with nonmetals. What explains both its placement and its nonmetallic behavior?",
        "يوضع الهيدروجين (Z = 1) فوق المجموعة الأولى، لكنه خلافاً لليثيوم والصوديوم غاز ثنائي الذرة (H₂) يكوّن روابط تساهمية مع اللافلزات. ما تفسير موقعه وسلوكه اللافلزي معاً؟",
        [
            ("Hydrogen has 1 valence electron (matching Group 1), but its tiny 1st shell needs only 1 more electron to fill, so it shares electrons covalently rather than behaving as a metal",
             "يمتلك إلكترون تكافؤ واحداً (كالمجموعة 1)، لكن مداره الأول الصغير يمتلئ بإلكترون واحد إضافي، فيشارك إلكتروناته تساهمياً كاللافلزات"),
            ("Hydrogen actually has 7 valence electrons like a halogen",
             "يمتلك الهيدروجين 7 إلكترونات تكافؤ في الواقع مثل الهالوجينات"),
            ("Hydrogen nuclei have 2 protons that attract covalent electrons",
             "تحوي نواة الهيدروجين بروتونين يجذبان الإلكترونات التساهمية"),
            ("Lithium and Sodium are also diatomic gases at room temperature",
             "الليثيوم والصوديوم غازان ثنائيا الذرة أيضاً في درجة حرارة الغرفة"),
        ],
        "The 1st shell holds at most 2 electrons, so 1 valence electron is simultaneously 1 electron above empty AND 1 electron short of full!",
        "المستوى الأول يتسع لإلكترونين فقط، لذا إلكترون واحد يعني امتلاكه إلكترون تكافؤ واحداً وحاجته لإلكترون واحد فقط للاكتمال!",
        "Connect Hydrogen's 1s¹ shell capacity (2 e-) to its dual periodic traits.",
        ["With 1 valence electron, Hydrogen aligns electronically with Group 1.",
         "However, holding that single electron tightly in shell 1 makes losing it very costly (high ionization energy), so H shares electrons in H₂, H₂O, and CH₄ like a nonmetal."],
        "Hydrogen is truly unique and often shaded separately on periodic tables.",
        "نربط سعة المدار الأول (2 إلكترون) بصفتي الهيدروجين.",
        ["وجود إلكترون تكافؤ واحد يضعه مع المجموعة 1 في الترتيب الإلكتروني.",
         "لكن قرب الإلكترون الوحيد من النواة يصعّب فقده، فيفضل المشاركة التساهمية لإكمال المدار الأول إلى إلكترونين."],
        "لذلك يُعامل الهيدروجين كحالة فريدة في الجدول الدوري.",
    ))

    # 13 (Hard): Physical state and reactivity trend across Group 17
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        "At 25 °C and 1 atm, Fluorine (F₂) and Chlorine (Cl₂) are gases, Bromine (Br₂) is a liquid, and Iodine (I₂) is a solid. Which statement correctly relates <strong>physical state</strong> and <strong>chemical reactivity</strong> down Group 17?",
        "عند 25 °س وضغط 1 جو، يكون الفلور والكلور غازين، والبروم سائلاً، واليود صلباً. أي عبارة تربط بدقة بين <strong>الحالة الفيزيائية</strong> و<strong>النشاط الكيميائي</strong> نزولاً في المجموعة 17؟",
        [
            ("Melting/boiling points increase down the group (gas → liquid → solid) as molecules grow heavier, while chemical reactivity decreases",
             "ترتفع درجات الانصهار والغليان نزولاً (غاز ← سائل ← صلب) لكبر الكتلة الجزيئية وتجاذبها، بينما يقل النشاط الكيميائي"),
            ("Both boiling points and chemical reactivity increase steadily from F₂ to I₂",
             "يزداد كل من الغليان والنشاط الكيميائي من الفلور إلى اليود"),
            ("Melting points decrease down Group 17 while reactivity explodes at I₂",
             "تنخفض درجات الانصهار نزولاً بينما يزداد النشاط بشدة عند اليود"),
            ("All halogens become metallic conductors when cooled below 25 °C",
             "تتحول جميع الهالوجينات إلى فلزات موصلة عند تبريدها"),
        ],
        "Separate intermolecular attraction (boiling point) from nuclear attraction for an extra electron (reactivity).",
        "افصل بين قوى التجاذب بين الجزيئات (درجة الغليان) وبين قدرة الذرة على جذب إلكترون (النشاط).",
        "Check opposite trends down Group 17: heavier molecules = higher boiling point; larger radius = lower reactivity.",
        ["Larger electron clouds in Br₂ and I₂ create stronger intermolecular dispersion forces, shifting state from gas → liquid → solid.",
         "Meanwhile, greater shell radius weakens attraction for an incoming valence electron, reducing reactivity from F₂ down to I₂."],
        "Trend mastery distinguishes intermolecular physics from valence chemistry.",
        "نميّز بين التجاذب بين الجزيئات والنشاط الكيميائي للذرة.",
        ["كبر الجزيئات وزيادة إلكتروناتها من F₂ إلى I₂ تقوي التجاذب الجزيئي فترتفع درجة الغليان (غاز ← سائل ← صلب).",
         "بينما بعد الغلاف الخارجي عن النواة يضعف جذب الإلكترون الجديد فيقل النشاط الكيميائي."],
        "الخواص الفيزيائية والنشاط الكيميائي قد يتجهان باتجاهين متعاكسين في المجموعة.",
    ))

    # 14 (Hard): Period 2 1:1 ionic compound pair
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        "In Period 2, four elements have atomic numbers W (Z = 3), X (Z = 4), Y (Z = 7), and Z (Z = 8). Which pair combines in an exact <strong>1:1 ionic formula</strong> (one metal cation to one nonmetal anion)?",
        "في الدورة الثانية أربعة عناصر أعدادها الذرية: W (Z = 3)، X (Z = 4)، Y (Z = 7)، Z (Z = 8). أي زوج يتحد بصيغة أيونية بنسبة <strong>1:1</strong> تماماً (أيون فلزي موجب واحد مقابل أيون لافلزي سالب واحد)؟",
        [
            ("X and Z (Be²⁺ + O²⁻ → BeO)", "X و Z (أيون Be²⁺ مع أيون O²⁻ ← صيغة 1:1)"),
            ("W and Z (Li⁺ + O²⁻ → Li₂O)", "W و Z (يعطي نسبة 2:1)"),
            ("W and Y (Li⁺ + N³⁻ → Li₃N)", "W و Y (يعطي نسبة 3:1)"),
            ("X and Y (Be²⁺ + N³⁻ → Be₃N₂)", "X و Y (يعطي نسبة 3:2)"),
        ],
        "Find the ion charges from valence electrons: Z=3 (+1), Z=4 (+2), Z=7 (-3), Z=8 (-2).",
        "حدد شحنة كل أيون: Z=3 (+1)، Z=4 (+2)، Z=7 (-3)، Z=8 (-2).",
        "Check which positive and negative magnitudes are equal.",
        ["W (Z = 3, Li) has 1 valence e⁻ → +1; X (Z = 4, Be) has 2 valence e⁻ → +2.",
         "Y (Z = 7, N) has 5 valence e⁻ → -3; Z (Z = 8, O) has 6 valence e⁻ → -2.",
         "Only X (+2) and Z (-2) balance charges 1:1 to form XZ (BeO)."],
        "Notice W₂Z = Li₂O (2:1), W₃Y = Li₃N (3:1), and X₃Y₂ = Be₃N₂ (3:2).",
        "نبحث عن فلز ولافلز تتساوى قيمة شحنتيهما الموجبة والسالبة.",
        ["الفلزان: W (+1) و X (+2)؛ واللافلزان: Y (-3) و Z (-2).",
         "تتساوى الشحنة المطلقة فقط بين X (+2) و Z (-2) فتتكون صيغة 1:1."],
        "بقية الأزواج تعطي نسب 2:1 أو 3:1 أو 3:2.",
    ))
    return qs


def _gen_sci_b09(start_idx: int) -> list[dict]:
    """G9-SCI-B09: Ionic vs covalent bonding & crisscross chemical formulas."""
    bp = "G9-SCI-B09"
    qs: list[dict] = []

    # 0 (Easy): Ionic vs covalent mechanism
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        "How does the chemical bonding in table salt (NaCl) differ fundamentally from that in carbon dioxide (CO₂)?",
        "كيف يختلف الترابط الكيميائي في ملح الطعام (NaCl) جوهرياً عنه في ثاني أكسيد الكربون (CO₂)؟",
        [
            ("NaCl forms by electron transfer from a metal to a nonmetal (ionic); CO₂ forms by sharing electrons between nonmetals (covalent)",
             "يتكون NaCl بانتقال الإلكترونات من فلز إلى لافلز (رابطة أيونية)، بينما يتكون CO₂ بمشاركة الإلكترونات بين لافلزين (تساهمية)"),
            ("NaCl shares electrons equally between two nonmetals; CO₂ transfers protons",
             "يتشارك NaCl الإلكترونات بين لافلزين، بينما ينقل CO₂ البروتونات"),
            ("Both compounds consist solely of metallic bonds with free electron seas",
             "يتكون كلا المركبين من روابط فلزية خالصة"),
            ("CO₂ forms an extended crystal lattice of +4 carbon ions while NaCl forms gas molecules",
             "يكوّن CO₂ شبكة بلورية أيونية بينما يكوّن NaCl جزيئات غازية منفردة"),
        ],
        "Check element types: Na (metal) + Cl (nonmetal) vs C (nonmetal) + O (nonmetal).",
        "افحص نوع العناصر: الصوديوم فلز والكلور لافلز، بينما الكربون والأكسجين كلاهما لافلز.",
        "Distinguish electron transfer (ionic) from electron sharing (covalent).",
        ["Sodium transfers 1 valence electron to Chlorine, forming oppositely charged Na⁺ and Cl⁻ ions attracted electrostatically.",
         "Carbon and Oxygen are both nonmetals that achieve octets by sharing electron pairs in discrete CO₂ molecules."],
        "Metal + Nonmetal typically yields ionic; Nonmetal + Nonmetal yields molecular covalent.",
        "نميز بين فقد واكتساب الإلكترونات (أيوني) والمشاركة بالإلكترونات (تساهمي).",
        ["يفقد الصوديوم إلكتروناً لصالح الكلور فتنشأ أيونات Na⁺ و Cl⁻ متجاذبة كهربائياً (أيونية).",
         "الكربون والأكسجين لافلزان يتشاركان الإلكترونات في جزيئات تساهمية منفصلة."],
        "فلز + لافلز يعطي مركباً أيونياً؛ لافلز + لافلز يعطي مركباً تساهمياً.",
    ))

    # 1 (Easy): Simple binary formula Mg2+ and Cl-
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        f"Magnesium ({m('\\text{Mg}^{2+}')}) reacts with Chlorine ({m('\\text{Cl}^-')}) to form Magnesium chloride. What is its correct chemical formula?",
        f"يتفاعل المغنيسيوم ({m('\\text{Mg}^{2+}')}) مع الكلور ({m('\\text{Cl}^-')}) لتكوين كلوريد المغنيسيوم. ما الصيغة الكيميائية الصحيحة للمركب؟",
        [
            (m("\\text{MgCl}_2"), m("\\text{MgCl}_2")),
            (m("\\text{Mg}_2\\text{Cl}"), m("\\text{Mg}_2\\text{Cl}")),
            (m("\\text{MgCl}"), m("\\text{MgCl}")),
            (m("\\text{Mg}_2\\text{Cl}_2"), m("\\text{Mg}_2\\text{Cl}_2")),
        ],
        "Neutrality requires total positive charge (+2) to balance total negative charge (2 × -1 = -2).",
        "التعادل الكهربائي يتطلب أن تساوي الشحنة الموجبة (+2) مجموع الشحنة السالبة (2 × -1).",
        "Crisscross the ion charges 2 and 1.",
        ["Mg carries +2 charge and Cl carries -1 charge.",
         "Crisscrossing gives 1 Mg²⁺ and 2 Cl⁻ ions → MgCl₂, since (+2) + 2(-1) = 0."],
        "Subscript 1 is omitted by standard chemical convention.",
        "نطبق طريقة المقص لتبادل التكافؤات مع التبسيط.",
        ["شحنة المغنيسيوم +2 وشحنة الكلوريد -1.",
         "نحتاج أيوني كلوريد لمعادلة أيون مغنيسيوم واحد: MgCl₂."],
        "مجموع الشحنات (+2) + 2(-1) = 0.",
        diagram_en=svg_atom_bohr("Mg", 12, 12, [2, 8, 2], "Magnesium [2, 8, 2]"),
        diagram_ar=_ar_svg(svg_atom_bohr("Mg", 12, 12, [2, 8, 2], "Magnesium [2, 8, 2]"),
                           {"Magnesium [2, 8, 2]": "المغنيسيوم [2، 8، 2]"}),
    ))

    # 2 (Easy): Physical properties of ionic solids
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        "Why does solid table salt (NaCl) fail to conduct electricity as a dry crystal, yet conduct electricity strongly when dissolved in water or melted?",
        "لماذا لا توصل بلورات ملح الطعام (NaCl) الجافة التيار الكهربائي في الحالة الصلبة، بينما توصل الكهرباء بقوة عند إذابتها في الماء أو صهرها؟",
        [
            ("In solid crystals, ions are locked in a rigid lattice; melting or dissolving frees Na⁺ and Cl⁻ ions to move and carry charge",
             "في الحالة الصلبة تكون الأيونات مقيدة في شبكة بلورية صلبة، وعند الذوبان أو الانصهار تصبح الأيونات حرة الحركة لنقل الشحنة"),
            ("Water turns Na⁺ and Cl⁻ ions into solid copper metal wires",
             "يحول الماء أيونات الملح إلى أسلاك نحاسية صلبة"),
            ("NaCl has zero ions in the solid state and only creates ions above 100 °C",
             "يخلو الملح الصلب من الأيونات ولا تتكون إلا عند التسخين"),
            ("Covalent sharing stops in water, releasing free neutrons",
             "تتوقف الروابط التساهمية في الماء فتتحرر نيوترونات حرة"),
        ],
        "Electrical conduction requires mobile charged particles (either free electrons in metals or mobile ions in liquids/solutions).",
        "التوصيل الكهربائي يتطلب حاملات شحنة حرة الحركة (إلكترونات حرة في الفلزات أو أيونات حرة في المحاليل والمصاهير).",
        "Compare ion mobility in solid crystal lattice vs aqueous/molten state.",
        ["Solid NaCl already consists of Na⁺ and Cl⁻ ions, but electrostatic attraction locks them at fixed lattice positions.",
         "Dissolving in water or heating past its melting point (801 °C) frees those ions to migrate toward electrodes."],
        "Sugar (covalent) dissolves in water as neutral molecules and still does not conduct.",
        "نقارن حرية حركة الأيونات في الصلب مقابل المحلول والمصهور.",
        ["الملح الصلب يحتوي أيونات بالفعل لكنها مقيدة في مواضع ثابتة بالشبكة البلورية فلا تتحرك.",
         "الذوبان أو الصهر يحرر الأيونات فتتحرك نحو الأقطاب وتوصل التيار."],
        "أما السكر التساهمي فيذوب كجزيئات متعادلة فلا يوصل التيار.",
    ))

    # 3 (Easy): Counting total atoms in Al2(SO4)3
    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        f"How many <strong>total atoms</strong> are represented in one formula unit of aluminum sulfate, {m('\\text{Al}_2(\\text{SO}_4)_3')}?",
        f"ما <strong>العدد الإجمالي للذرات</strong> في وحدة صيغة واحدة من كبريتات الألومنيوم {m('\\text{Al}_2(\\text{SO}_4)_3')}؟",
        17, [9, 12, 14],
        "Multiply subscripts inside the parentheses by 3, then add the 2 Al atoms.",
        "اضرب الأعداد داخل القوس في 3، ثم أضف ذرتي الألومنيوم.",
        f"Count Al, S, and O separately: {m('2 + 3(1 + 4)')}.",
        [f"Aluminum atoms: {m('2')}.",
         f"Inside 3 sulfate groups: Sulfur = {m('3 \\times 1 = 3')}; Oxygen = {m('3 \\times 4 = 12')}.",
         f"Total atoms = {m('2 + 3 + 12 = 17')}."],
        f"Remember {m('(\\text{SO}_4)_3')} multiplies BOTH S and O by {m('3')}.",
        "نعد ذرات كل عنصر مع توزيع الرقم خارج القوس.",
        [f"ذرات الألومنيوم = {m('2')}.",
         f"داخل ثلاث مجموعات كبريتات: الكبريت = {m('3 \\times 1 = 3')}، والأكسجين = {m('3 \\times 4 = 12')}.",
         f"المجموع = {m('2 + 3 + 12 = 17')} ذرة."],
        f"الرقم 3 خارج القوس يضرب كلاً من S و O.",
    ))

    # 4 (Easy): Covalent bond pairs in N2, O2, Cl2
    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        f"In a nitrogen gas molecule ({m('\\text{N}_2')}), each nitrogen atom ({m('Z = 7')}, shells {m('[2, 5]')}) needs 3 more electrons for an octet, so the two atoms form a triple covalent bond. How many <strong>total electrons</strong> are shared in that triple bond?",
        f"في جزيء غاز النيتروجين ({m('\\text{N}_2')})، تحتاج كل ذرة نيتروجين ({m('[2, 5]')}) إلى 3 إلكترونات لإكمال الثمانية، فتكوّنان رابطة تساهمية ثلاثية. ما <strong>العدد الكلي للإلكترونات</strong> المشتركة في هذه الرابطة الثلاثية؟",
        6, [3, 4, 2],
        "Each single covalent bond consists of 1 shared pair = 2 electrons.",
        "كل رابطة تساهمية واحدة تمثل زوجاً واحداً من الإلكترونات (إلكترونين).",
        f"Multiply {m('3')} shared pairs by {m('2')} electrons per pair.",
        [f"A single bond shares {m('2')} electrons; a double bond shares {m('4')}.",
         f"A triple covalent bond ({m('\\text{N}\\equiv\\text{N}')}) shares {m('3')} pairs = {m('6')} electrons."],
        f"Each N also keeps 1 unshared lone pair ({m('2')} e⁻), reaching {m('6 + 2 = 8')} valence electrons.",
        "نضرب عدد الروابط المشتركة في 2.",
        [f"الرابطة الأحادية تشارك إلكترونين، والثنائية 4 إلكترونات.",
         f"الرابطة الثلاثية ({m('\\text{N}\\equiv\\text{N}')}) تشارك 3 أزواج = {m('6')} إلكترونات."],
        "مع الزوج الحر لكل ذرة (2) تبلغ كل ذرة 8 إلكترونات.",
        diagram_en=svg_atom_bohr("N", 7, 7, [2, 5], "Nitrogen [2, 5] (5 Valence)"),
        diagram_ar=_ar_svg(svg_atom_bohr("N", 7, 7, [2, 5], "Nitrogen [2, 5] (5 Valence)"),
                           {"Nitrogen [2, 5] (5 Valence)": "النيتروجين [2، 5]"}),
    ))

    # 5 (Medium): Crisscross Al3+ and O2- -> Al2O3
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"Using the crisscross method, what is the correct ionic formula formed between Aluminum ions ({m('\\text{Al}^{3+}')}) and Oxide ions ({m('\\text{O}^{2-}')})?",
        f"باستخدام طريقة المقص (تبادل التكافؤات)، ما الصيغة الكيميائية الصحيحة للمركب الأيوني الناتج من أيون الألومنيوم ({m('\\text{Al}^{3+}')}) وأيون الأكسيد ({m('\\text{O}^{2-}')})؟",
        [
            (m("\\text{Al}_2\\text{O}_3"), m("\\text{Al}_2\\text{O}_3")),
            (m("\\text{Al}_3\\text{O}_2"), m("\\text{Al}_3\\text{O}_2")),
            (m("\\text{AlO}"), m("\\text{AlO}")),
            (m("\\text{Al}_2\\text{O}"), m("\\text{Al}_2\\text{O}")),
        ],
        "Cross the 3 from Al³⁺ to O and the 2 from O²⁻ to Al, then check total charge = 0.",
        "تبادل الرقم 3 إلى الأكسجين والرقم 2 إلى الألومنيوم، ثم تحقق من تساوي الشحنات.",
        "Balance least common multiple of +3 and -2 (which is 6).",
        ["2 Al³⁺ ions give 2 × (+3) = +6 charge.",
         "3 O²⁻ ions give 3 × (-2) = -6 charge; total = 0 → Al₂O₃."],
        "Notice gcd(2, 3) = 1 so no further simplification is needed.",
        "نوازن الشحنات باستخدام المضاعف المشترك الأصغر (6).",
        ["أيونان من الألومنيوم يعطيان 2 × (+3) = +6.",
         "ثلاثة أيونات أكسيد تعطي 3 × (-2) = -6، فتكون الصيغة المتعادلة Al₂O₃."],
        "العددان 2 و 3 أبسط ما يكون.",
        diagram_en=svg_atom_bohr("Al", 13, 14, [2, 8, 3], "Aluminum [2, 8, 3]"),
        diagram_ar=_ar_svg(svg_atom_bohr("Al", 13, 14, [2, 8, 3], "Aluminum [2, 8, 3]"),
                           {"Aluminum [2, 8, 3]": "الألومنيوم [2، 8، 3]"}),
    ))

    # 6 (Medium): Crisscross with simplification Ca2+ + O2- -> CaO
    qs.append(make_science_concept_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        f"When Calcium ({m('\\text{Ca}^{2+}')}) combines with Oxygen ({m('\\text{O}^{2-}')}), what is the correct <strong>simplified</strong> ionic formula of calcium oxide?",
        f"عند اتحاد الكالسيوم ({m('\\text{Ca}^{2+}')}) مع الأكسجين ({m('\\text{O}^{2-}')})، ما الصيغة الأيونية <strong>المبسّطة</strong> الصحيحة لأكسيد الكالسيوم؟",
        [
            (m("\\text{CaO}"), m("\\text{CaO}")),
            (m("\\text{Ca}_2\\text{O}_2"), m("\\text{Ca}_2\\text{O}_2")),
            (m("\\text{CaO}_2"), m("\\text{CaO}_2")),
            (m("\\text{Ca}_2\\text{O}"), m("\\text{Ca}_2\\text{O}")),
        ],
        "Ionic formulas represent the simplest whole-number ratio (empirical formula) of ions.",
        "تُكتب الصيغ الأيونية دائماً بأبسط نسبة عددية صحيحة للأيونات.",
        "Divide subscripts in Ca₂O₂ by their greatest common factor (2).",
        ["Crisscrossing +2 and -2 initially gives subscripts 2 and 2 (Ca₂O₂).",
         "Since ionic solids form continuous crystal lattices rather than molecules, reduce 2:2 to 1:1 → CaO."],
        "Check: (+2) + (-2) = 0 directly with 1 Ca²⁺ and 1 O²⁻.",
        "نبسّط النسبة بالقسمة على العامل المشترك الأكبر (2).",
        ["تبادل التكافؤين يعطي مبدئياً Ca₂O₂.",
         "لأن المركبات الأيونية شبكات بلورية نبسّط النسبة إلى أبسط صورة فتصبح CaO."],
        "شحنة (+2) تتعادل مباشرة مع (-2) بنسبة 1:1.",
        diagram_en=svg_atom_bohr("O", 8, 8, [2, 6], "Oxygen [2, 6]"),
        diagram_ar=_ar_svg(svg_atom_bohr("O", 8, 8, [2, 6], "Oxygen [2, 6]"),
                           {"Oxygen [2, 6]": "الأكسجين [2، 6]"}),
    ))

    # 7 (Medium): Polyatomic crisscross Ca2+ and PO4 3- -> Ca3(PO4)2
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        f"Phosphate rock mined in northern Saudi Arabia contains calcium phosphate, formed from {m('\\text{Ca}^{2+}')} and phosphate ({m('\\text{PO}_4^{3-}')}) ions. What is the correct formula?",
        f"يحتوي صخر الفوسفات المستخرج في شمال المملكة على فوسفات الكالسيوم المكون من أيونات {m('\\text{Ca}^{2+}')} وأيونات الفوسفات ({m('\\text{PO}_4^{3-}')}). ما الصيغة الصحيحة للمركب؟",
        [
            (m("\\text{Ca}_3(\\text{PO}_4)_2"), m("\\text{Ca}_3(\\text{PO}_4)_2")),
            (m("\\text{Ca}_2(\\text{PO}_4)_3"), m("\\text{Ca}_2(\\text{PO}_4)_3")),
            (m("\\text{Ca}_3\\text{PO}_4"), m("\\text{Ca}_3\\text{PO}_4")),
            (m("\\text{CaPO}_4"), m("\\text{CaPO}_4")),
        ],
        "Wrap polyatomic PO₄ in parentheses before applying the crossed subscript 2.",
        "ضع المجموعة الذرية PO₄ بين قوسين قبل وضع الرقم 2 المتبادل أسفلها.",
        "Verify 3(+2) + 2(-3) = 0.",
        ["Crisscrossing 2+ and 3- assigns subscript 3 to Ca and subscript 2 to the entire phosphate group.",
         "Using parentheses gives Ca₃(PO₄)₂ with total charge 3(+2) + 2(-3) = 0."],
        "Without parentheses, Ca₃PO₄₂ would mistakenly indicate 42 oxygen atoms!",
        "نتأكد من تعادل الشحنات ووضع الأقواس للمجموعة الذرية.",
        ["تبادل التكافؤين 2 و 3 يعطي 3 لذرات الكالسيوم و 2 لمجموعة الفوسفات كاملة.",
         "نضع المجموعة بين قوسين: Ca₃(PO₄)₂ حيث 3(+2) + 2(-3) = 0."],
        "ترك الأقواس سيخلط الأرقام مع ذرات الأكسجين.",
    ))

    # 8 (Medium): Ammonium sulfate formula (NH4)2SO4
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        f"Ammonium sulfate fertilizer is composed of ammonium ions ({m('\\text{NH}_4^+')}) and sulfate ions ({m('\\text{SO}_4^{2-}')}). What is its chemical formula?",
        f"يتكون سماد كبريتات الأمونيوم من أيونات الأمونيوم ({m('\\text{NH}_4^+')}) وأيونات الكبريتات ({m('\\text{SO}_4^{2-}')}). ما صيغته الكيميائية الصحيحة؟",
        [
            (m("(\\text{NH}_4)_2\\text{SO}_4"), m("(\\text{NH}_4)_2\\text{SO}_4")),
            (m("\\text{NH}_4(\\text{SO}_4)_2"), m("\\text{NH}_4(\\text{SO}_4)_2")),
            (m("\\text{NH}_4\\text{SO}_4"), m("\\text{NH}_4\\text{SO}_4")),
            (m("\\text{N}_2\\text{H}_8\\text{S}_2\\text{O}_4"), m("\\text{N}_2\\text{H}_8\\text{S}_2\\text{O}_4")),
        ],
        "Two +1 ammonium ions are needed to balance one -2 sulfate ion.",
        "يلزم أيونا أمونيوم (+1) لمعادلة أيون كبريتات واحد (-2).",
        "Use parentheses around NH₄⁺ for subscript 2; no parentheses needed around single SO₄²⁻.",
        ["2 × (+1) + 1 × (-2) = 0.",
         "Wrapping NH₄ in parentheses gives (NH₄)₂SO₄."],
        "Even though NH₄⁺ and SO₄²⁻ contain covalent bonds inside each ion, the compound itself is ionic.",
        "نضع القوسين حول مجموعة الأمونيوم عند تكرارها مرتين.",
        ["تتعادل شحنتا (+1) مرتين مع شحنة (-2) مرة واحدة.",
         "تُكتب الصيغة (NH₄)₂SO₄ مع إبقاء مجموعة الكبريتات المفردة دون أقواس."],
        "المركب أيوني رغم وجود روابط تساهمية داخل كل مجموعة ذرية.",
    ))

    # 9 (Medium): Lab classification table (ionic vs molecular covalent)
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        "A student tests two unknown white crystalline solids. Solid P melts at 801 °C and conducts electricity strongly when dissolved in water. Solid Q melts at 114 °C, dissolves in water, and its solution does NOT conduct electricity. How should P and Q be classified?",
        "اختبر طالب مادتين صلبتين بيضاوين: المادة P تنصهر عند 801 °س ومحلولها المائي يوصل الكهرباء بقوة، والمادة Q تنصهر عند 114 °س وتذوب في الماء لكن محلولها لا يوصل الكهرباء. كيف تُصنف المادتان؟",
        [
            ("P is an ionic compound; Q is a molecular covalent compound",
             "P مركب أيوني، و Q مركب جزيئي تساهمي"),
            ("P is a molecular covalent compound; Q is an ionic salt",
             "P مركب تساهمي جزيئي، و Q ملح أيوني"),
            ("Both P and Q are pure elemental metals",
             "كلتا المادتين فلزان نقيان"),
            ("Both P and Q are noble gases frozen into crystals",
             "كلتا المادتين غازان نبيلان متجمدان"),
        ],
        "Compare melting point and aqueous electrical conductivity (electrolyte vs non-electrolyte).",
        "قارن درجة الانصهار والتوصيل الكهربائي للمحلول المائي (إلكتروليت مقابل غير إلكتروليت).",
        "Link high MP + conductive solution to ionic bonding, and low MP + nonconductive solution to molecular covalent.",
        ["Strong electrostatic lattice forces give ionic solids high melting points (~800 °C) and mobile ions in water (Solid P).",
         "Weak intermolecular forces give molecular covalent solids low melting points and neutral dissolved molecules (Solid Q, like glucose)."],
        "Metals do not dissolve as simple neutral crystals in water.",
        "نربط الانصهار المرتفع والتوصيل بالمركب الأيوني، والمنخفض غير الموصل بالتساهمي.",
        ["القوى الأيونية القوية ترفع درجة انصهار P وتحرر أيونات موصلة عند الذوبان.",
         "أما Q فجزيئات تساهمية متعادلة ذات قوى تجاذب ضعيفة فلا توصل عند الذوبان (كالسكر)."],
        "هذا الاختبار معيار مخبري لتصنيف الروابط.",
    ))

    # 10 (Hard): Inferring valence from M2O3 -> M(NO3)3
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"An unknown metal {m('\\text{M}')} forms a pure oxide with the formula {m('\\text{M}_2\\text{O}_3')}. What formula will metal {m('\\text{M}')} form when bonded to nitrate ions ({m('\\text{NO}_3^-')})?",
        f"يكوّن فلز مجهول {m('\\text{M}')} أكسيداً صيغته {m('\\text{M}_2\\text{O}_3')}. ما الصيغة التي يكوّنها الفلز {m('\\text{M}')} عند اتحاده مع أيونات النترات ({m('\\text{NO}_3^-')})؟",
        [
            (m("\\text{M}(\\text{NO}_3)_3"), m("\\text{M}(\\text{NO}_3)_3")),
            (m("\\text{M}(\\text{NO}_3)_2"), m("\\text{M}(\\text{NO}_3)_2")),
            (m("\\text{M}_2(\\text{NO}_3)_3"), m("\\text{M}_2(\\text{NO}_3)_3")),
            (m("\\text{M}_3\\text{NO}_3"), m("\\text{M}_3\\text{NO}_3")),
        ],
        "First deduce the ion charge of M from M₂O₃ knowing Oxygen is always -2.",
        "استنتج أولاً شحنة أيون M من الصيغة M₂O₃ علماً بأن الأكسجين (-2).",
        "Solve 2(charge of M) + 3(-2) = 0, then crisscross with NO₃⁻.",
        ["Three O²⁻ ions contribute 3 × (-2) = -6 total negative charge.",
         "Two M ions must sum to +6, so each M ion carries +3 (M³⁺).",
         "Balancing M³⁺ with NO₃⁻ (-1) gives M(NO₃)₃."],
        "For example, Fe₂O₃ corresponds to Fe(NO₃)₃, and Al₂O₃ to Al(NO₃)₃.",
        "نحسب تكافؤ الفلز M من صيغة الأكسيد ثم نطبقه مع النترات.",
        ["ثلاث ذرات أكسجين تعطي شحنة إجمالية (-6).",
         "إذن ذرتا M تحملان (+6)، أي أن كل أيون يحمل (+3).",
         "مع أيون النترات (-1) تنتج الصيغة M(NO₃)₃."],
        "مثال ذلك أكسيد الألومنيوم ونترات الألومنيوم.",
    ))

    # 11 (Hard): Nonmetal X forms Na2X -> Period 3 identity & hydride H2X
    qs.append(make_science_concept_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"A Period 3 nonmetal {m('\\text{X}')} forms the ionic salt {m('\\text{Na}_2\\text{X}')} with sodium. Which Group does {m('\\text{X}')} belong to, and what covalent formula does it form with Hydrogen?",
        f"يكوّن اللافلز {m('\\text{X}')} من الدورة الثالثة الملح الأيوني {m('\\text{Na}_2\\text{X}')} مع الصوديوم. إلى أي مجموعة ينتمي {m('\\text{X}')}، وما صيغة المركب التساهمي الذي يكوّنه مع الهيدروجين؟",
        [
            ("Group 16 (Sulfur); covalent formula H₂X (H₂S)",
             "المجموعة 16 (الكبريت)؛ الصيغة التساهمية H₂X (مثل H₂S)"),
            ("Group 17 (Chlorine); covalent formula HX",
             "المجموعة 17 (الكلور)؛ الصيغة HX"),
            ("Group 15 (Phosphorus); covalent formula H₃X",
             "المجموعة 15 (الفوسفور)؛ الصيغة H₃X"),
            ("Group 2 (Magnesium); ionic formula XH₂",
             "المجموعة 2 (المغنيسيوم)؛ الصيغة XH₂"),
        ],
        "Each Na⁺ is +1, so two Na⁺ (+2) tell you the charge of X.",
        "كل أيون صوديوم (+1)، إذن أيونان (+2) يكشفان شحنة الأيون X.",
        "Deduce valence electrons of X from charge -2, then bond with H (1 bond each).",
        ["In Na₂X, two Na⁺ ions give +2, so X forms X²⁻ (needs 2 electrons → 6 valence electrons → Group 16, Sulfur).",
         "To complete its octet covalently, Sulfur shares 2 electrons with 2 Hydrogen atoms → H₂S (H₂X)."],
        "Same valence pattern gives H₂O in Period 2.",
        "نستنتج شحنة X ومنها رقم المجموعة وعدد الروابط مع الهيدروجين.",
        ["في Na₂X توجد ذرتا صوديوم (+2)، لذا شحنة X هي (-2) وله 6 إلكترونات تكافؤ (المجموعة 16: الكبريت).",
         "مع الهيدروجين يشارك الكبريت إلكترونين ليكوّن H₂S (الصيغة H₂X)."],
        "يتشابه مع الأكسجين في تكوين H₂O.",
    ))

    # 12 (Hard): Bohr-to-compound Mg [2,8,2] + N [2,5] -> Mg3N2
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        "Element A has Bohr shells [2, 8, 2] and element B has Bohr shells [2, 5]. What bond type and chemical formula result when A reacts completely with B?",
        "للعنصر A توزيع إلكتروني [2، 8، 2] وللعنصر B توزيع [2، 5]. ما نوع الرابطة والصيغة الكيميائية الناتجة عند اتحادهما التام؟",
        [
            (m("\\text{Ionic bond; formula } \\text{A}_3\\text{B}_2"),
             "رابطة أيونية؛ الصيغة " + m("\\text{A}_3\\text{B}_2")),
            (m("\\text{Covalent bond; formula } \\text{AB}_2"),
             "رابطة تساهمية؛ الصيغة " + m("\\text{AB}_2")),
            (m("\\text{Ionic bond; formula } \\text{A}_2\\text{B}_3"),
             "رابطة أيونية؛ الصيغة " + m("\\text{A}_2\\text{B}_3")),
            (m("\\text{Metallic bond; formula } \\text{AB}"),
             "رابطة فلزية؛ الصيغة " + m("\\text{AB}")),
        ],
        "Identify metal vs nonmetal from valence counts (2 vs 5), find ion charges (+2 vs -3), and crisscross.",
        "حدد الفلز واللافلز من التكافؤ (2 مقابل 5)، أوجد الشحنات (+2 و -3)، ثم بادل الأرقام.",
        "Compute LCM of +2 and -3 (6 electrons transferred).",
        ["A [2, 8, 2] is a metal (Mg) that loses 2 electrons to form A²⁺.",
         "B [2, 5] is a nonmetal (N) that gains 3 electrons to form B³⁻.",
         "Crisscrossing gives ionic A₃B₂ (Mg₃N₂), transferring 6 electrons total."],
        "3(+2) + 2(-3) = 0.",
        "نحدد الأيونين ثم نطبق المقص.",
        ["العنصر A [2، 8، 2] فلز يفقد إلكترونين ليكون A²⁺، والعنصر B [2، 5] لافلز يكتسب 3 إلكترونات ليكون B³⁻.",
         "التبادل يعطي الصيغة الأيونية A₃B₂ (مثل Mg₃N₂)."],
        "مجموع الشحنات 3(+2) + 2(-3) = 0.",
        diagram_en=svg_atom_bohr("A", 12, 12, [2, 8, 2], "Element A [2, 8, 2]"),
        diagram_ar=_ar_svg(svg_atom_bohr("A", 12, 12, [2, 8, 2], "Element A [2, 8, 2]"),
                           {"Element A [2, 8, 2]": "العنصر A [2، 8، 2]"}),
    ))

    # 13 (Hard): Metallic sea of electrons vs ionic lattice conductivity
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        "Solid copper (Cu) conducts electricity immediately at room temperature and bends cleanly when hammered, whereas solid sodium chloride (NaCl) is an insulator and shatters when struck. What structural difference explains BOTH contrasts?",
        "يوصل النحاس الصلب (Cu) الكهرباء فوراً وينثني عند طرقه دون أن يتفتت، بينما يعزل ملح الطعام الصلب (NaCl) الكهرباء ويتكسر عند طرقه. ما الفرق التركيبي الذي يفسر <strong>كلتا</strong> الصفتين؟",
        [
            ("Copper has positive cations in a mobile sea of delocalized electrons that conduct and allow layers to slide; NaCl has rigid alternating ions that repel and shatter if shifted",
             "في النحاس تسبح الأيونات الموجبة في بحر إلكترونات حرة متحركة تسمح بالتوصيل وانزلاق الطبقات، بينما في NaCl انزياح الطبقات يواجه الأيونات المتشابهة فتتنافر وتتكسر"),
            ("Copper atoms are bonded covalently in rigid molecules",
             "ترتبط ذرات النحاس بروابط تساهمية صلبة"),
            ("Solid NaCl contains zero charged particles of any kind",
             "يخلو ملح الطعام الصلب من أي جسيمات مشحونة"),
            ("Copper conducts via moving protons while NaCl blocks protons",
             "يوصل النحاس عبر حركة البروتونات الموجبة في السلك"),
        ],
        "Picture what happens when one layer of atoms slides over another in a metal vs an alternating +/- ionic crystal.",
        "تخيل انزلاق طبقة ذرات في الفلز مقابل انزلاقها في بلورة أيونية متناوبة الشحنة (+ و -).",
        "Explain both conductivity and malleability vs brittleness from bonding geometry.",
        ["In copper, delocalized valence electrons flow freely under voltage (conductivity) and cushion metal cations as planes slide (malleability).",
         "In NaCl, shifting one crystal layer places + next to + and - next to -, causing strong electrostatic repulsion that fractures the crystal (brittleness)."],
        "The 'electron sea' model explains metallic luster, malleability, and conductivity together.",
        "نفسر التوصيل والطرق معاً من نموذج بحر الإلكترونات والشبكة الأيونية.",
        ["بحر الإلكترونات الحرة في الفلز ينقل التيار ويسمح بانزلاق طبقات الأيونات الموجبة دون تنافر.",
         "أما في البلورة الأيونية فانزلاق صف واحد يضع المتشابهين (+ مع +) فيحدث تنافر فوري يكسر البلورة."],
        "التركيب البلوري يفسر الخواص الميكانيكية والكهربائية معاً.",
    ))

    # 14 (Hard): Counting shared bonding electrons in CO2
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        f"In a molecule of carbon dioxide ({m('\\text{O=C=O}')}), carbon forms two double covalent bonds—one with each oxygen atom—so that every atom completes an octet. How many <strong>total shared bonding electrons</strong> exist inside a single {m('\\text{CO}_2')} molecule?",
        f"في جزيء ثاني أكسيد الكربون ({m('\\text{O=C=O}')})، يكوّن الكربون رابطتين تساهميتين ثنائيتين (واحدة مع كل ذرة أكسجين) لتصل كل ذرة إلى حالة الثمانية. ما <strong>العدد الكلي للإلكترونات المشتركة في الروابط</strong> داخل جزيء واحد من {m('\\text{CO}_2')}؟",
        8, [4, 16, 12],
        "Each double bond contains 2 shared electron pairs = 4 shared electrons.",
        "كل رابطة ثنائية تحتوي على زوجين مشتركين = 4 إلكترونات مشتركة.",
        f"Multiply {m('2')} double bonds by {m('4')} shared electrons each.",
        [f"Each {m('\\text{C=O}')} double bond consists of {m('2')} shared pairs = {m('4')} electrons.",
         f"Across both double bonds in {m('\\text{O=C=O}')}, total shared electrons = {m('2 \\times 4 = 8')}."],
        f"Carbon has {m('8')} bonding electrons around it; each Oxygen also keeps {m('4')} nonbonding lone-pair electrons ({m('16')} valence e⁻ total).",
        "نضرب عدد الروابط الثنائية في 4 إلكترونات.",
        [f"كل رابطة ثنائية تتكون من زوجين أي {m('4')} إلكترونات مشتركة.",
         f"بوجود رابطتين ثنائيتين يكون عدد الإلكترونات المشتركة = {m('2 \\times 4 = 8')} إلكترونات."],
        f"إجمالي إلكترونات التكافؤ في الجزيء 16 منها {m('8')} مشتركة و8 حرة.",
        diagram_en=svg_atom_bohr("C", 6, 6, [2, 4], "Carbon [2, 4]"),
        diagram_ar=_ar_svg(svg_atom_bohr("C", 6, 6, [2, 4], "Carbon [2, 4]"),
                           {"Carbon [2, 4]": "الكربون [2، 4]"}),
    ))
    return qs


def _gen_sci_b10(start_idx: int) -> list[dict]:
    """G9-SCI-B10: Conservation of mass stoichiometry & balancing chemical coefficients."""
    bp = "G9-SCI-B10"
    qs: list[dict] = []

    # 0 (Easy): Closed-flask mass conservation 24 g Mg + 16 g O2 -> 40 g MgO
    qs.append(make_science_math_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        f"In a sealed crucible, {m('24')} g of Magnesium ribbon burns completely with {m('16')} g of Oxygen gas to form Magnesium oxide ({m('\\text{MgO}')}) with no leftover reactants. How many grams of {m('\\text{MgO}')} are formed?",
        f"في بوتقة مغلقة، احترق {m('24')} g من شريط المغنيسيوم كلياً مع {m('16')} g من غاز الأكسجين لتكوين أكسيد المغنيسيوم ({m('\\text{MgO}')}) دون بقايا. كم جراماً من {m('\\text{MgO}')} يتكوّن؟",
        40, [8, 32, 48],
        "By the Law of Conservation of Mass, total product mass equals total reactant mass.",
        "وفق قانون حفظ الكتلة، تساوي كتلة النواتج مجموع كتل المتفاعلات.",
        f"Add {m('24 + 16')}.",
        [f"Total reactant mass = {m('24 + 16 = 40')} g.",
         f"No mass enters or leaves the sealed container, so product mass = {m('40')} g."],
        f"Notice {m('24:16 = 3:2')} matches the atomic mass ratio of Mg (24) to O (16).",
        "نجمع كتلتي المتفاعلين لتطبيق قانون حفظ الكتلة.",
        [f"مجموع كتل المتفاعلات = {m('24 + 16 = 40')} g.",
         f"لأن النظام مغلق فإن كتلة أكسيد المغنيسيوم الناتج = {m('40')} g."],
        f"النسبة {m('24:16')} تطابق الكتلتين الذريتين للمغنيسيوم والأكسجين.",
        diagram_en=_svg_mass_balance("24 g Mg + 16 g O2", "? g MgO", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "24 g Mg + 16 g O2", "? g MgO", "ar"),
    ))

    # 1 (Easy): Open beaker apparent mass loss explanation
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        "A student places an open beaker containing baking soda and vinegar on a digital balance reading 150.0 g. After bubbling finishes, the scale reads 146.4 g. Why did the scale reading drop?",
        "وضع طالب كأساً مفتوحاً به بيكربونات الصوديوم والخل على ميزان رقمي فقرأ 150.0 g. بعد انتهاء الفوران قرأ الميزان 146.4 g. لماذا انخفضت قراءة الميزان؟",
        [
            ("CO₂ gas escaped into the open air; mass is conserved when the 3.6 g of escaped gas is included",
             "تصاعد غاز CO₂ إلى الهواء المفتوح؛ والكتلة محفوظة عند احتساب 3.6 g من الغاز المتصاعد"),
            ("Chemical reactions destroy about 2% of matter automatically",
             "التفاعلات الكيميائية تفني نحو 2% من المادة تلقائياً"),
            ("Vinegar evaporated completely into pure energy",
             "تحوّل الخل بالكامل إلى طاقة صرفة دون كتلة"),
            ("Sodium atoms shrank in atomic mass during neutralization",
             "نقصت الكتلة الذرية لذرات الصوديوم أثناء التفاعل"),
        ],
        "Mass conservation holds strictly in closed systems where gases cannot escape.",
        "يتحقق قانون حفظ الكتلة بدقة في الأنظمة المغلقة التي تمنع تسرب الغازات.",
        "Account for the missing 3.6 g as escaped gaseous product.",
        ["Acid + bicarbonate produces aqueous salt, water, and carbon dioxide gas (CO₂).",
         "In an open beaker, 3.6 g of CO₂ floats away unweighed; capping with a balloon keeps the scale at 150.0 g."],
        "Matter is never created or destroyed in chemical reactions.",
        "نفسر النقص الظاهري بتسرب الغاز الناتج في الوعاء المفتوح.",
        ["ينتج عن التفاعل غاز ثاني أكسيد الكربون الذي يتصاعد لكون الكأس مفتوحاً.",
         "لو أُغلق الكأس ببالون لبقيت القراءة ثابتة عند 150.0 g لأن الكتلة محفوظة."],
        "المادة لا تفنى في التفاعلات الكيميائية.",
    ))

    # 2 (Easy): Balancing 2H2 + O2 -> 2H2O (coefficient of H2)
    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        f"In the balanced chemical equation {m('a\\,\\text{H}_2 + b\\,\\text{O}_2 \\to c\\,\\text{H}_2\\text{O}')}, using smallest whole-number coefficients, what is the value of {m('a')} (the coefficient of {m('\\text{H}_2')})?",
        f"في المعادلة الكيميائية الموزونة {m('a\\,\\text{H}_2 + b\\,\\text{O}_2 \\to c\\,\\text{H}_2\\text{O}')} بأصغر أعداد صحيحة، ما قيمة المعامل {m('a')} (معامل غاز الهيدروجين {m('\\text{H}_2')})؟",
        2, [1, 3, 4],
        "Balance Oxygen atoms first (2 on left from O₂), which requires 2 H₂O on the right.",
        "وازن ذرات الأكسجين أولاً (ذرتان في اليسار من O₂)، مما يتطلب جزيئي ماء 2 H₂O في اليمين.",
        "Count H and O atoms on both sides.",
        [f"Right side needs {m('2')} O atoms → set {m('c = 2')} ({m('2\\,\\text{H}_2\\text{O}')}).",
         f"That gives {m('4')} H atoms on the right, so {m('a = 2')} ({m('2\\,\\text{H}_2')}) and {m('b = 1')}."],
        f"Balanced equation: {m('2\\,\\text{H}_2 + \\text{O}_2 \\to 2\\,\\text{H}_2\\text{O}')} (4 H, 2 O each side).",
        "نوازن الأكسجين ثم الهيدروجين.",
        [f"الطرف الأيمن يحتاج ذرتي أكسجين، فنضع {m('c = 2')} لتكوين {m('2\\,\\text{H}_2\\text{O}')}.",
         f"أصبح في اليمين 4 ذرات هيدروجين، لذا نضع {m('a = 2')} ليكون الناتج {m('2\\,\\text{H}_2 + \\text{O}_2 \\to 2\\,\\text{H}_2\\text{O}')}."],
        "الذرات متساوية: 4 H و 2 O في كل طرف.",
    ))

    # 3 (Easy): Decomposition 100 g CaCO3 -> 56 g CaO + ? g CO2
    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        f"When {m('100')} g of calcium carbonate ({m('\\text{CaCO}_3')}) is heated in a closed vessel, it decomposes completely into {m('56')} g of solid calcium oxide ({m('\\text{CaO}')}) and carbon dioxide gas ({m('\\text{CO}_2')}). How many grams of {m('\\text{CO}_2')} are produced?",
        f"عند تسخين {m('100')} g من كربونات الكالسيوم ({m('\\text{CaCO}_3')}) في وعاء مغلق، تتحلل كلياً إلى {m('56')} g من أكسيد الكالسيوم الصلب ({m('\\text{CaO}')}) وغاز {m('\\text{CO}_2')}. كم جراماً من {m('\\text{CO}_2')} ينتج؟",
        44, [56, 156, 28],
        "Subtract the mass of CaO from the initial mass of CaCO₃.",
        "اطرح كتلة أكسيد الكالسيوم من الكتلة الابتدائية لكربونات الكالسيوم.",
        f"Solve {m('100 = 56 + m_{\\text{CO}_2}')}.",
        [f"Reactant mass = {m('100')} g; total product mass must also equal {m('100')} g.",
         f"{m('m_{\\text{CO}_2} = 100 - 56 = 44')} g."],
        f"Check: {m('56 + 44 = 100')} g (matches molar masses 56 + 44 = 100 g/mol).",
        "نطبق حفظ الكتلة بطرح كتلة الصلب المتبقي من الكتلة الكلية.",
        [f"كتلة المتفاعلات {m('100')} g، لذا مجموع النواتج {m('100')} g.",
         f"كتلة غاز ثاني أكسيد الكربون = {m('100 - 56 = 44')} g."],
        f"التحقق: {m('56 + 44 = 100')} g.",
        diagram_en=_svg_mass_balance("100 g CaCO3", "56 g CaO + ? g CO2", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "100 g CaCO3", "56 g CaO + ? g CO2", "ar"),
    ))

    # 4 (Easy): Ammonia synthesis coefficient of H2 (3)
    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        f"When the ammonia synthesis equation {m('a\\,\\text{N}_2 + b\\,\\text{H}_2 \\to c\\,\\text{NH}_3')} is balanced using the smallest positive integers, what is the coefficient {m('b')} in front of {m('\\text{H}_2')}?",
        f"عند وزن معادلة تحضير الأمونيا {m('a\\,\\text{N}_2 + b\\,\\text{H}_2 \\to c\\,\\text{NH}_3')} بأصغر أعداد صحيحة، ما قيمة المعامل {m('b')} أمام {m('\\text{H}_2')}؟",
        3, [1, 2, 6],
        "Balance N atoms first by placing 2 in front of NH₃, then count H atoms.",
        "وازن ذرات النيتروجين أولاً بوضع 2 أمام NH₃، ثم احسب ذرات الهيدروجين.",
        "Match 2 N and 6 H on both sides.",
        [f"With {m('a = 1')} ({m('\\text{N}_2')}), {m('c = 2')} ({m('2\\,\\text{NH}_3')}) balances the 2 N atoms.",
         f"Then {m('2\\,\\text{NH}_3')} contains {m('2 \\times 3 = 6')} H atoms, requiring {m('b = 3')} ({m('3\\,\\text{H}_2')})."],
        f"Balanced: {m('\\text{N}_2 + 3\\,\\text{H}_2 \\to 2\\,\\text{NH}_3')}.",
        "نوازن النيتروجين ثم الهيدروجين.",
        [f"نضع {m('c = 2')} لموازنة ذرتي النيتروجين.",
         f"يصبح الهيدروجين {m('2 \\times 3 = 6')} ذرات، فنضع {m('b = 3')} أمام {m('\\text{H}_2')}."],
        f"المعادلة الموزونة: {m('\\text{N}_2 + 3\\,\\text{H}_2 \\to 2\\,\\text{NH}_3')}.",
    ))

    # 5 (Medium): Two-product mass balance CH4 + O2 -> CO2 + H2O
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"In a closed calorimeter, {m('16')} g of methane ({m('\\text{CH}_4')}) burns completely with {m('64')} g of oxygen ({m('\\text{O}_2')}) to produce {m('44')} g of carbon dioxide ({m('\\text{CO}_2')}) plus water vapor ({m('\\text{H}_2\\text{O}')}). How many grams of water vapor form?",
        f"في مسعر مغلق، احترق {m('16')} g من الميثان ({m('\\text{CH}_4')}) كلياً مع {m('64')} g من الأكسجين ({m('\\text{O}_2')}) لينتج {m('44')} g من {m('\\text{CO}_2')} وبخار ماء ({m('\\text{H}_2\\text{O}')}). كم جراماً من بخار الماء ينتج؟",
        36, [20, 48, 80],
        "Total reactant mass (16 + 64) equals total product mass (44 + m_H2O).",
        "مجموع كتل المتفاعلات (16 + 64) يساوي مجموع كتل النواتج (44 + كتلة الماء).",
        f"Solve {m('16 + 64 = 44 + m_{\\text{H}_2\\text{O}}')}.",
        [f"Total reactant mass = {m('16 + 64 = 80')} g.",
         f"Water mass = {m('80 - 44 = 36')} g."],
        f"Check: {m('44 + 36 = 80')} g (matches 2 H₂O = 36 g/mol).",
        "نساوي مجموع كتل الطرفين.",
        [f"مجموع المتفاعلات = {m('16 + 64 = 80')} g.",
         f"كتلة بخار الماء = {m('80 - 44 = 36')} g."],
        f"التحقق: {m('44 + 36 = 80')} g.",
        diagram_en=_svg_mass_balance("16g CH4 + 64g O2", "44g CO2 + ?g H2O", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "16g CH4 + 64g O2", "44g CO2 + ?g H2O", "ar"),
    ))

    # 6 (Medium): Sum of coefficients in Fe + Cl2 -> FeCl3 (2+3+2 = 7)
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        f"Balance the equation {m('a\\,\\text{Fe} + b\\,\\text{Cl}_2 \\to c\\,\\text{FeCl}_3')} using the smallest positive integers. What is the <strong>sum</strong> of all stoichiometric coefficients {m('a + b + c')}?",
        f"زن المعادلة {m('a\\,\\text{Fe} + b\\,\\text{Cl}_2 \\to c\\,\\text{FeCl}_3')} بأصغر أعداد صحيحة موجبة. ما <strong>مجموع</strong> جميع المعاملات {m('a + b + c')}؟",
        7, [5, 6, 8],
        "Use the least common multiple of 2 and 3 (6 Cl atoms) to balance Chlorine.",
        "استخدم المضاعف المشترك الأصغر للعددين 2 و 3 (أي 6 ذرات كلور) لموازنة الكلور.",
        f"Set {m('b = 3')} and {m('c = 2')}, then balance Fe.",
        [f"To match Cl atoms (2 on left, 3 on right), reach 6 Cl atoms: {m('3\\,\\text{Cl}_2')} and {m('2\\,\\text{FeCl}_3')}.",
         f"That requires {m('2\\,\\text{Fe}')}, giving {m('2\\,\\text{Fe} + 3\\,\\text{Cl}_2 \\to 2\\,\\text{FeCl}_3')}.",
         f"Sum = {m('2 + 3 + 2 = 7')}."],
        "Atom check: 2 Fe and 6 Cl on both sides.",
        "نوازن الكلور أولاً بالمضاعف المشترك الأصغر (6).",
        [f"نضع {m('b = 3')} و {m('c = 2')} لتصبح ذرات الكلور 6 في الطرفين.",
         f"ثم نضع {m('a = 2')} لموازنة الحديد: {m('2\\,\\text{Fe} + 3\\,\\text{Cl}_2 \\to 2\\,\\text{FeCl}_3')}.",
         f"مجموع المعاملات = {m('2 + 3 + 2 = 7')}."],
        "الذرات موزونة: 2 حديد و6 كلور في كل طرف.",
    ))

    # 7 (Medium): Sum of coefficients in Al + O2 -> Al2O3 (4+3+2 = 9)
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        f"Balance the oxidation of aluminum: {m('a\\,\\text{Al} + b\\,\\text{O}_2 \\to c\\,\\text{Al}_2\\text{O}_3')} with smallest whole-number coefficients. What is {m('a + b + c')}?",
        f"زن معادلة أكسدة الألومنيوم: {m('a\\,\\text{Al} + b\\,\\text{O}_2 \\to c\\,\\text{Al}_2\\text{O}_3')} بأصغر أعداد صحيحة. ما قيمة {m('a + b + c')}؟",
        9, [6, 7, 11],
        "Balance Oxygen to 6 atoms on each side (3 O₂ and 2 Al₂O₃), then balance Al.",
        "وازن الأكسجين إلى 6 ذرات في الطرفين (3 O₂ و 2 Al₂O₃) ثم وازن الألومنيوم.",
        f"Find {m('a, b, c')} and add them.",
        [f"LCM of 2 and 3 O atoms is 6 → {m('b = 3')} and {m('c = 2')}.",
         f"{m('2\\,\\text{Al}_2\\text{O}_3')} contains {m('4')} Al atoms → {m('a = 4')}.",
         f"Sum = {m('4 + 3 + 2 = 9')}."],
        f"Balanced: {m('4\\,\\text{Al} + 3\\,\\text{O}_2 \\to 2\\,\\text{Al}_2\\text{O}_3')}.",
        "نوازن الأكسجين أولاً ثم الألومنيوم.",
        [f"لموازنة الأكسجين (2 و 3) نصل إلى 6 ذرات: {m('b = 3')} و {m('c = 2')}.",
         f"يحتوي {m('2\\,\\text{Al}_2\\text{O}_3')} على 4 ذرات ألومنيوم، إذن {m('a = 4')}.",
         f"المجموع = {m('4 + 3 + 2 = 9')}."],
        f"المعادلة الموزونة: {m('4\\,\\text{Al} + 3\\,\\text{O}_2 \\to 2\\,\\text{Al}_2\\text{O}_3')}.",
    ))

    # 8 (Medium): Excess reactant mass reacted (20 g A + 30 g B -> 42 g AB + 8 g leftover A)
    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        f"In a sealed flask, {m('20')} g of reactant {m('\\text{A}')} is mixed with {m('30')} g of reactant {m('\\text{B}')}. When reaction stops, {m('42')} g of compound {m('\\text{AB}')} has formed and all {m('30')} g of {m('\\text{B}')} is consumed, leaving some unreacted {m('\\text{A}')}. How many grams of {m('\\text{A}')} <strong>actually reacted</strong>?",
        f"في دورق مغلق، خُلط {m('20')} g من المادة {m('\\text{A}')} مع {m('30')} g من المادة {m('\\text{B}')}. عند توقف التفاعل تكوّن {m('42')} g من المركب {m('\\text{AB}')} واستُهلكت كل الـ {m('30')} g من {m('\\text{B}')} مع بقاء فائض من {m('\\text{A}')}. كم جراماً من {m('\\text{A}')} <strong>تفاعل فعلياً</strong>؟",
        12, [8, 20, 22],
        "All 30 g of B went into the 42 g of product AB; the rest of AB's mass came from A.",
        "دخلت كل الـ 30 g من B في تكوين 42 g من المركب AB، والباقي من كتلة AB مصدره المادة A.",
        f"Subtract {m('m_B = 30')} g from {m('m_{AB} = 42')} g.",
        [f"Product mass {m('\\text{AB} = 42')} g consists entirely of reacted {m('\\text{A}')} + reacted {m('\\text{B}')}.",
         f"Since all {m('30')} g of {m('\\text{B}')} reacted, reacted {m('\\text{A} = 42 - 30 = 12')} g (leaving {m('20 - 12 = 8')} g excess {m('\\text{A}')})."],
        f"Total flask mass check: {m('42 + 8 = 50 = 20 + 30')} g.",
        "نطرح كتلة المادة المستهلكة كلياً من كتلة الناتج.",
        [f"المركب الناتج {m('42')} g يتكون من كتلة B المستهلكة كلياً ({m('30')} g) زائد الكتلة المتفاعلة من A.",
         f"كتلة A المتفاعلة = {m('42 - 30 = 12')} g، ويتبقى {m('8')} g دون تفاعل."],
        f"الكتلة الكلية في الدورق تبقى {m('42 + 8 = 50')} g.",
        diagram_en=_svg_mass_balance("20g A + 30g B", "42g AB + excess A", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "20g A + 30g B", "42g AB + فائض A", "ar"),
    ))

    # 9 (Medium): Balancing Ca(OH)2 + H3PO4 -> Ca3(PO4)2 + H2O (water coeff = 6)
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        f"Balance the neutralization equation {m('a\\,\\text{Ca(OH)}_2 + b\\,\\text{H}_3\\text{PO}_4 \\to c\\,\\text{Ca}_3(\\text{PO}_4)_2 + d\\,\\text{H}_2\\text{O}')} using smallest whole numbers. What is the coefficient {m('d')} of water?",
        f"زن معادلة التعادل {m('a\\,\\text{Ca(OH)}_2 + b\\,\\text{H}_3\\text{PO}_4 \\to c\\,\\text{Ca}_3(\\text{PO}_4)_2 + d\\,\\text{H}_2\\text{O}')} بأصغر أعداد صحيحة. ما معامل الماء {m('d')}؟",
        6, [2, 3, 12],
        "Start by fixing c = 1 for Ca₃(PO₄)₂, which forces 3 Ca and 2 PO₄ groups on the left.",
        "ابدأ بتثبيت c = 1 للملح، مما يفرض وجود 3 كالسيوم ومجموعتي فوسفات في اليسار.",
        "Balance Ca and PO₄ first, then count total H and O in water.",
        [f"Setting {m('c = 1')} requires {m('a = 3')} ({m('3\\,\\text{Ca(OH)}_2')}) and {m('b = 2')} ({m('2\\,\\text{H}_3\\text{PO}_4')}).",
         f"Left side provides {m('3(2) = 6\\,\\text{OH}^-')} and {m('2(3) = 6\\,\\text{H}^+')}, combining into {m('d = 6')} ({m('6\\,\\text{H}_2\\text{O}')})."],
        f"Check H: {m('6 + 6 = 12 = 6(2)')}; check non-phosphate O: {m('6 = 6')}.",
        "نوازن أيونات الكالسيوم والفوسفات ثم نحسب جزيئات الماء الناتجة.",
        [f"لوضع {m('c = 1')} نحتاج {m('a = 3')} و {m('b = 2')}.",
         f"يعطي الطرف الأيسر {m('6')} أيونات OH⁻ و{m('6')} أيونات H⁺، فتتحد لتكوين {m('d = 6')} جزيئات ماء."],
        "التحقق: 12 ذرة هيدروجين في الطرفين.",
    ))

    # 10 (Hard): Definite proportions + limiting reactant (15 g C + 32 g O2 -> 44 g CO2)
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"Carbon and oxygen always combine in a fixed mass ratio of {m('3:8')} to form {m('\\text{CO}_2')} (so {m('12')} g C reacts completely with {m('32')} g {m('\\text{O}_2')} to form {m('44')} g {m('\\text{CO}_2')}). If {m('15')} g of Carbon is sealed with {m('32')} g of {m('\\text{O}_2')}, how many grams of {m('\\text{CO}_2')} are formed?",
        f"يتحد الكربون والأكسجين دائماً بنسبة كتلية ثابتة {m('3:8')} لتكوين {m('\\text{CO}_2')} (حيث يتفاعل {m('12')} g كربون مع {m('32')} g أكسجين لتكوين {m('44')} g {m('\\text{CO}_2')}). إذا أُحرق {m('15')} g كربون في وعاء مغلق مع {m('32')} g أكسجين، فكم جراماً من {m('\\text{CO}_2')} يتكوّن؟",
        44, [47, 55, 36],
        "Once all 32 g of Oxygen is used up by 12 g of Carbon, the remaining 3 g of Carbon has no oxygen left to react with.",
        "بمجرد استهلاك كل 32 g من الأكسجين مع 12 g كربون، لا يجد الـ 3 g المتبقي من الكربون أكسجيناً يتفاعل معه.",
        "Identify the limiting reactant (O₂) first.",
        [f"Following the {m('3:8')} ratio, {m('32')} g of {m('\\text{O}_2')} reacts with at most {m('32 \\times \\frac{3}{8} = 12')} g of C.",
         f"Thus {m('\\text{O}_2')} is the limiting reactant, producing {m('12 + 32 = 44')} g of {m('\\text{CO}_2')} (with {m('3')} g C left unreacted)."],
        "Do NOT add 15 + 32 = 47 g as product—that ignores excess unreacted carbon!",
        "نحدد المادة المحددة للتفاعل أولاً (الأكسجين).",
        [f"وفق النسبة الثابتة {m('3:8')}، يستهلك {m('32')} g أكسجين {m('12')} g كربون فقط.",
         f"فينفد الأكسجين ويتكون {m('12 + 32 = 44')} g من {m('\\text{CO}_2')} ويبقى {m('3')} g كربون دون تفاعل."],
        "الجمع المباشر 15+32=47 خطأ لأن 3g من الكربون لم تتفاعل.",
        diagram_en=_svg_mass_balance("15g C + 32g O2", "? g CO2 + excess C", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "15g C + 32g O2", "? g CO2 + فائض C", "ar"),
    ))

    # 11 (Hard): Copper + Sulfur stoichiometry excess S remaining
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"Copper and Sulfur combine in an exact {m('2:1')} mass ratio ({m('64')} g Cu + {m('32')} g S → {m('96')} g CuS). If {m('40')} g of Copper is heated with {m('25')} g of Sulfur in a closed tube, how many grams of <strong>unreacted Sulfur</strong> remain?",
        f"يتحد النحاس والكبريت بنسبة كتلية ثابتة {m('2:1')} ({m('64')} g نحاس + {m('32')} g كبريت ← {m('96')} g CuS). إذا سُخّن {m('40')} g نحاس مع {m('25')} g كبريت في أنبوب مغلق، فكم جراماً من <strong>الكبريت الفائض</strong> يتبقى دون تفاعل؟",
        5, [0, 15, 20],
        "Use the 2:1 ratio to calculate how much Sulfur is needed for 40 g of Copper.",
        "استخدم نسبة 2:1 لحساب كتلة الكبريت التي تستهلكها 40 g من النحاس.",
        f"Find S consumed by {m('40')} g Cu, then subtract from {m('25')} g.",
        [f"By the {m('2:1')} ratio, {m('40')} g of Cu reacts completely with {m('40 \\div 2 = 20')} g of S (forming {m('60')} g CuS).",
         f"Remaining unreacted Sulfur = {m('25 - 20 = 5')} g."],
        f"Total mass check: {m('60')} g CuS + {m('5')} g S = {m('65')} g = {m('40 + 25')} g.",
        "نحسب الكبريت المتفاعل ثم نطرحه من الكتلة الابتدائية.",
        [f"وفق نسبة {m('2:1')} يتفاعل {m('40')} g نحاس مع {m('20')} g كبريت فقط لتكوين {m('60')} g CuS.",
         f"الكبريت المتبقي = {m('25 - 20 = 5')} g."],
        f"التحقق: {m('60 + 5 = 40 + 25 = 65')} g.",
        diagram_en=_svg_mass_balance("40g Cu + 25g S", "CuS + ? g S", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "40g Cu + 25g S", "CuS + ? g S", "ar"),
    ))

    # 12 (Hard): Hydrocarbon combustion 2 C2H6 + 7 O2 -> 4 CO2 + 6 H2O (sum = 19)
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        f"Balance the complete combustion of ethane: {m('a\\,\\text{C}_2\\text{H}_6 + b\\,\\text{O}_2 \\to c\\,\\text{CO}_2 + d\\,\\text{H}_2\\text{O}')} using the smallest positive integers. What is {m('a + b + c + d')}?",
        f"زن معادلة الاحتراق الكامل للإيثان: {m('a\\,\\text{C}_2\\text{H}_6 + b\\,\\text{O}_2 \\to c\\,\\text{CO}_2 + d\\,\\text{H}_2\\text{O}')} بأصغر أعداد صحيحة موجبة. ما مجموع المعاملات {m('a + b + c + d')}؟",
        19, [13, 17, 21],
        "Start with 1 C₂H₆ → 2 CO₂ + 3 H₂O (7 O atoms on right → 7/2 O₂), then double every coefficient.",
        "ابدأ بـ 1 C₂H₆ ← 2 CO₂ + 3 H₂O (7 ذرات أكسجين ← 7/2 O₂)، ثم اضرب المعاملات كلها في 2.",
        "Balance C, then H, then O, and clear the fraction.",
        [f"With {m('a = 1')}, {m('c = 2')} and {m('d = 3')} give {m('4 + 3 = 7')} O atoms, needing {m('3.5\\,\\text{O}_2')}.",
         f"Doubling all coefficients gives integers: {m('2\\,\\text{C}_2\\text{H}_6 + 7\\,\\text{O}_2 \\to 4\\,\\text{CO}_2 + 6\\,\\text{H}_2\\text{O}')}.",
         f"Sum = {m('2 + 7 + 4 + 6 = 19')}."],
        "Atom check: 4 C, 12 H, 14 O on both sides.",
        "نوازن الكربون ثم الهيدروجين ثم نضاعف للتخلص من الكسر.",
        [f"لجزيء واحد من الإيثان نحتاج {m('2\\,\\text{CO}_2')} و{m('3\\,\\text{H}_2\\text{O}')} أي 7 ذرات أكسجين ({m('3.5\\,\\text{O}_2')}).",
         f"بالضرب في 2 تصبح: {m('2\\,\\text{C}_2\\text{H}_6 + 7\\,\\text{O}_2 \\to 4\\,\\text{CO}_2 + 6\\,\\text{H}_2\\text{O}')}.",
         f"المجموع = {m('2 + 7 + 4 + 6 = 19')}."],
        "التحقق: 4 C و 12 H و 14 O في الطرفين.",
    ))

    # 13 (Hard): Propane combustion C3H8 + 5 O2 -> 3 CO2 + 4 H2O (3 mol -> 15 mol O2)
    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        f"Propane fuel burns according to {m('a\\,\\text{C}_3\\text{H}_8 + b\\,\\text{O}_2 \\to c\\,\\text{CO}_2 + d\\,\\text{H}_2\\text{O}')}. After balancing the equation, how many molecules (or moles) of {m('\\text{O}_2')} are needed to completely burn {m('3')} molecules (or moles) of {m('\\text{C}_3\\text{H}_8')}?",
        f"يحترق غاز البروبان وفق المعادلة {m('a\\,\\text{C}_3\\text{H}_8 + b\\,\\text{O}_2 \\to c\\,\\text{CO}_2 + d\\,\\text{H}_2\\text{O}')}. بعد وزن المعادلة، كم جزيئاً (أو مولاً) من {m('\\text{O}_2')} يلزم لحرق {m('3')} جزيئات (أو مولات) من البروبان {m('\\text{C}_3\\text{H}_8')} كلياً؟",
        15, [5, 10, 18],
        "First balance 1 C₃H₈ → 3 CO₂ + 4 H₂O to find the O₂ coefficient b, then multiply by 3.",
        "وازن أولاً معادلة جزيء واحد C₃H₈ ← 3 CO₂ + 4 H₂O لإيجاد معامل O₂، ثم اضربه في 3.",
        f"Compute {m('b')} for 1 C₃H₈ and scale by {m('3')}.",
        [f"For 1 {m('\\text{C}_3\\text{H}_8')}: {m('c = 3')} ({m('3\\,\\text{CO}_2')}) and {m('d = 4')} ({m('4\\,\\text{H}_2\\text{O}')}).",
         f"Oxygen atoms on right = {m('3(2) + 4(1) = 10')}, so {m('b = 5')} ({m('5\\,\\text{O}_2')}).",
         f"Burning {m('3')} {m('\\text{C}_3\\text{H}_8')} requires {m('3 \\times 5 = 15')} {m('\\text{O}_2')}."],
        "Ratio C₃H₈ : O₂ is always 1 : 5.",
        "نستخرج معامل الأكسجين أولاً ثم نضرب في 3.",
        [f"المعادلة الموزونة: {m('\\text{C}_3\\text{H}_8 + 5\\,\\text{O}_2 \\to 3\\,\\text{CO}_2 + 4\\,\\text{H}_2\\text{O}')}.",
         f"كل جزيء بروبان يستهلك 5 من O₂، إذن 3 جزيئات تستهلك {m('3 \\times 5 = 15')} من O₂."],
        "النسبة المولية 1 : 5 ثابتة.",
    ))

    # 14 (Hard): Open-tube thermal decomposition KClO3 -> KCl + O2
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        f"A chemist heats {m('245')} g of pure solid potassium chlorate ({m('\\text{KClO}_3')}) in an <strong>open</strong> test tube according to {m('2\\,\\text{KClO}_3(s) \\to 2\\,\\text{KCl}(s) + 3\\,\\text{O}_2(g)')}. After complete reaction, {m('96')} g of oxygen gas has escaped into the air. What mass (in g) of solid {m('\\text{KCl}')} remains in the tube?",
        f"سخّن كيميائي {m('245')} g من كلورات البوتاسيوم الصلبة ({m('\\text{KClO}_3')}) في أنبوب اختبار <strong>مفتوح</strong> وفق التفاعل {m('2\\,\\text{KClO}_3(s) \\to 2\\,\\text{KCl}(s) + 3\\,\\text{O}_2(g)')}. بعد تمام التفاعل تصاعد {m('96')} g من غاز الأكسجين. ما كتلة ملح {m('\\text{KCl}')} الصلب المتبقي في الأنبوب (بالجرام)؟",
        149, [96, 192, 341],
        "By mass conservation, initial solid mass = solid KCl residue + escaped O₂ gas.",
        "بحفظ الكتلة: الكتلة الابتدائية = كتلة الملح الصلب المتبقي + كتلة الأكسجين المتصاعد.",
        f"Compute {m('245 - 96')}.",
        [f"Initial reactant mass = {m('245')} g.",
         f"Since {m('96')} g escaped as gas, remaining {m('\\text{KCl} = 245 - 96 = 149')} g."],
        f"Check with molar masses: {m('2(122.5) = 245')} g → {m('2(74.5) = 149')} g + {m('3(32) = 96')} g.",
        "نطرح كتلة الغاز المتصاعد من الكتلة الابتدائية.",
        [f"كتلة المتفاعل الابتدائي = {m('245')} g.",
         f"بعد طرح الغاز المتصاعد ({m('96')} g) يتبقى {m('245 - 96 = 149')} g من كلوريد البوتاسيوم."],
        f"التحقق: {m('149 + 96 = 245')} g.",
        diagram_en=_svg_mass_balance("245g KClO3", "? g KCl + 96g O2", "", "", "en"),
        diagram_ar=_svg_mass_balance("", "", "245g KClO3", "? g KCl + 96g O2", "ar"),
    ))
    return qs


def _gen_sci_b11(start_idx: int) -> list[dict]:
    """G9-SCI-B11: Reaction types, activation energy / endo-exothermic & catalyst rates."""
    bp = "G9-SCI-B11"
    qs: list[dict] = []

    # 0 (Easy): Synthesis reaction 2Mg + O2 -> 2MgO
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        f"How is the reaction {m('2\\,\\text{Mg} + \\text{O}_2 \\to 2\\,\\text{MgO}')} classified?",
        f"كيف يُصنف التفاعل الكيميائي {m('2\\,\\text{Mg} + \\text{O}_2 \\to 2\\,\\text{MgO}')}؟",
        [
            ("Synthesis (combination) reaction", "تفاعل اتحاد (تكوين)"),
            ("Decomposition reaction", "تفاعل تفكك (تحلل)"),
            ("Double-replacement reaction", "تفاعل إحلال مزدوج"),
            ("Endothermic neutralization", "تفاعل تعادل ماص للحرارة"),
        ],
        "Two simpler substances (Mg and O₂) combine to form a single product (MgO).",
        "تتحد مادتان أبسط لتكوين مركب واحد جديد فقط.",
        "Match general form A + B → AB.",
        ["Two elements react to build one more complex compound (AB).",
         "A + B → AB defines a synthesis (combination) reaction."],
        "Decomposition (AB → A + B) is the exact reverse.",
        "نطابق الصيغة العامة A + B → AB.",
        ["اتحاد عنصرين لإنتاج مركب واحد هو تفاعل اتحاد (تكوين).",
         "التفكك هو عكسه تماماً حيث ينقسم مركب واحد إلى مادتين أو أكثر."],
        "الصيغة A + B → AB تميز تفاعل التكوين.",
    ))

    # 1 (Easy): Single replacement Zn + 2HCl -> ZnCl2 + H2
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        f"When zinc metal reacts with hydrochloric acid ({m('\\text{Zn} + 2\\,\\text{HCl} \\to \\text{ZnCl}_2 + \\text{H}_2')}), which reaction type takes place?",
        f"عند تفاعل فلز الخارصين مع حمض الهيدروكلوريك ({m('\\text{Zn} + 2\\,\\text{HCl} \\to \\text{ZnCl}_2 + \\text{H}_2')})، ما نوع التفاعل الحادث؟",
        [
            ("Single-replacement (single-displacement) reaction", "تفاعل إحلال بسيط"),
            ("Synthesis reaction", "تفاعل اتحاد"),
            ("Decomposition reaction", "تفاعل تحلل"),
            ("Hydrocarbon combustion reaction", "تفاعل احتراق هيدروكربون"),
        ],
        "One free element (Zn) replaces another element (H) inside a compound (HCl).",
        "يحل عنصر حر (Zn) محل عنصر آخر (H) داخل مركب (HCl).",
        "Match general pattern A + BC → AC + B.",
        ["Free Zinc displaces Hydrogen from HCl to form ZnCl₂ and H₂ gas.",
         "An element trading places with an element inside a compound is single replacement."],
        "Double replacement involves two compounds swapping ions (AB + CD → AD + CB).",
        "نطابق النمط A + BC → AC + B.",
        ["يحل الخارصين محل الهيدروجين في الحمض فينطلق غاز H₂ ويتكوّن الملح.",
         "هذا يطابق تفاعل الإحلال البسيط."],
        "أما الإحلال المزدوج فيحدث بتبادل أيونات بين مركبين.",
    ))

    # 2 (Easy): Reading exothermic diagram
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        "In the reaction energy profile shown, reactants start at 80 kJ and products finish at 30 kJ. Is this reaction <strong>exothermic</strong> or <strong>endothermic</strong>, and what happens to the beaker temperature?",
        "في مخطط طاقة التفاعل الموضح، تبدأ المتفاعلات عند 80 kJ وتنتهي النواتج عند 30 kJ. هل هذا التفاعل <strong>طارد</strong> أم <strong>ماص</strong> للحرارة، وماذا يحدث لحرارة الكأس؟",
        [
            ("Exothermic; 50 kJ of energy is released, warming the surroundings",
             "طارد للحرارة؛ تنطلق 50 kJ من الطاقة فترتفع حرارة المحيط والكأس"),
            ("Endothermic; 50 kJ of energy is absorbed, cooling the surroundings",
             "ماص للحرارة؛ تُمتص 50 kJ من الطاقة فتبرد الكأس"),
            ("Exothermic; products store more potential energy than reactants",
             "طارد للحرارة؛ النواتج تخزن طاقة وضع أعلى من المتفاعلات"),
            ("Endothermic; no heat leaves or enters the beaker",
             "ماص للحرارة؛ لا تدخل ولا تخرج أي حرارة"),
        ],
        "Compare product energy (30 kJ) against reactant energy (80 kJ): the lost 50 kJ exits as heat.",
        "قارن طاقة النواتج (30 kJ) بطاقة المتفاعلات (80 kJ): الفرق 50 kJ يخرج كحرارة.",
        "Check sign of ΔH = E_products - E_reactants.",
        ["Products (30 kJ) sit lower than reactants (80 kJ), so ΔH = 30 - 80 = -50 kJ.",
         "Negative ΔH means energy flows outward into the solution/air, making the beaker warmer."],
        "Exothermic reactions feel warm to the touch.",
        "نحسب الفرق ΔH = طاقة النواتج - طاقة المتفاعلات.",
        ["طاقة النواتج (30) أقل من طاقة المتفاعلات (80)، فالفرق (-50 kJ) يتحرر للوسط.",
         "خروج الطاقة الحرارية يرفع حرارة المحلول والكأس (تفاعل طارد)."],
        "التفاعل الطارد يبعث حرارة يشعر بها الملاحظ.",
        diagram_en=_svg_energy_profile(80, 130, 30, None, "en"),
        diagram_ar=_svg_energy_profile(80, 130, 30, None, "ar"),
    ))

    # 3 (Easy): Catalyst mechanism
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        "In the energy diagram, adding an enzyme or solid catalyst creates the red dashed pathway. How does a <strong>catalyst</strong> speed up a chemical reaction?",
        "في مخطط الطاقة، يؤدي إضافة إنزيم أو عامل حفّاز إلى ظهور المسار الأحمر المتقطع. كيف يسرّع <strong>العامل الحفّاز</strong> التفاعل الكيميائي؟",
        [
            ("It lowers the activation energy barrier without changing ΔH or being consumed",
             "يخفض حاجز طاقة التنشيط اللازمة لبدء التفاعل دون تغيير ΔH ودون أن يُستهلك"),
            ("It raises the potential energy of the reactants permanently",
             "يرفع طاقة الوضع للمتفاعلات بشكل دائم"),
            ("It converts endothermic reactions into exothermic reactions",
             "يحوّل التفاعلات الماصة للحرارة إلى تفاعلات طاردة"),
            ("It acts as a reactant that disappears inside the final product formula",
             "يدخل كمتفاعل يُستهلك نهائياً داخل صيغة الناتج"),
        ],
        "Look at the dashed peak height vs the unchanged start (reactant) and end (product) levels.",
        "انظر إلى انخفاض القمة المتقطعة مع بقاء مستوى البداية والنهاية ثابتين تماماً.",
        "Note what changes (peak height = activation energy) vs what stays fixed (ΔH).",
        ["A catalyst provides an alternative pathway with a lower transition-state peak.",
         "More colliding molecules now exceed the lower activation energy, speeding up the reaction while leaving reactant/product energies and ΔH unchanged."],
        "Catalysts are recovered chemically unchanged at the end.",
        "نقارن ارتفاع القمة (طاقة التنشيط) بثبات طاقة البداية والنهاية.",
        ["يوفر العامل الحفّاز مساراً بديلاً ذا قمة تنشيط أقل.",
         "تتمكن جزيئات أكثر من تجاوز الحاجز فيتسرع التفاعل دون استهلاك الحفّاز أو تغير ΔH."],
        "يبقى الحفّاز دون تغيير في نهاية التفاعل.",
        diagram_en=_svg_energy_profile(60, 160, 25, 110, "en"),
        diagram_ar=_svg_energy_profile(60, 160, 25, 110, "ar"),
    ))

    # 4 (Easy): Surface area collision rate
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        "Crushing a 10 g lump of limestone (CaCO₃) into fine powder makes it fizz much faster in hydrochloric acid. According to collision theory, why does powdering increase the reaction rate?",
        "طحن قطعة كربونات كالسيوم كتلتها 10 g إلى مسحوق ناعم يجعلها تتفاعل وتفور أسرع بكثير مع حمض الهيدروكلوريك. وفق نظرية التصادم، لماذا يزيد الطحن سرعة التفاعل؟",
        [
            ("It dramatically increases exposed surface area, raising the frequency of effective particle collisions per second",
             "يزيد مساحة السطح المعرضة للتفاعل بشكل كبير، فيرفع عدد التصادمات الفعالة في الثانية"),
            ("Powdered CaCO₃ has a higher chemical mass than the original lump",
             "كتلة المسحوق الكيميائية أكبر من كتلة القطعة الأصلية"),
            ("Crushing turns CaCO₃ into a liquid acid automatically",
             "الطحن يحول كربونات الكالسيوم إلى حمض سائل تلقائياً"),
            ("Powdering eliminates the need for any molecular collisions",
             "يلغي الطحن الحاجة إلى تصادم الجزيئات تماماً"),
        ],
        "Acid molecules can only collide with outer exposed CaCO₃ ions.",
        "جزيئات الحمض لا تصطدم إلا بالسطح الخارجي المكشوف من المادة الصلبة.",
        "Connect smaller particle size → larger surface area → higher collision frequency.",
        ["Inside a single solid lump, interior CaCO₃ particles are shielded from acid molecules.",
         "Powdering exposes many fresh surfaces at once, multiplying collision opportunities per second."],
        "Total CO₂ gas yield remains the same (same 10 g mass), only reached sooner.",
        "نربط صغر حجم الحبيبات بزيادة مساحة السطح وتكرار التصادمات.",
        ["في القطعة الواحدة تكون الجزيئات الداخلية محجوبة عن الحمض.",
         "السحق يكشف مساحات سطحية جديدة فيزداد عدد التصادمات الناجحة في وحدة الزمن."],
        "تبقى كمية الغاز الكلية ثابتة لكنها تتكون بزمن أقصر.",
    ))

    # 5 (Medium): Forward Ea from energy profile (140 - 50 = 90 kJ)
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"In the energy profile diagram, reactants are at {m('50')} kJ, the transition-state peak is at {m('140')} kJ, and products are at {m('20')} kJ. What is the <strong>forward activation energy</strong> ({m('E_a')}, in kJ)?",
        f"في مخطط الطاقة الموضح، طاقة المتفاعلات {m('50')} kJ، وقمة الحالة الانتقالية {m('140')} kJ، وطاقة النواتج {m('20')} kJ. ما قيمة <strong>طاقة التنشيط الأمامية</strong> ({m('E_a')} بوحدة kJ)؟",
        90, [140, 120, 30],
        "Activation energy is measured from the REACTANTS up to the PEAK (not from 0).",
        "تُقاس طاقة التنشيط من مستوى المتفاعلات إلى قمة المنحنى (وليس من الصفر).",
        f"Compute {m('E_a = E_{\\text{peak}} - E_{\\text{reactants}}')}.",
        [f"Reactants begin at {m('50')} kJ and must climb to the transition peak at {m('140')} kJ.",
         f"Forward {m('E_a = 140 - 50 = 90')} kJ."],
        f"Note {m('\\Delta H = 20 - 50 = -30')} kJ, whereas {m('E_a = +90')} kJ.",
        "نطرح طاقة المتفاعلات من طاقة القمة.",
        [f"تبدأ المتفاعلات عند {m('50')} kJ وتصعد إلى القمة عند {m('140')} kJ.",
         f"طاقة التنشيط الأمامية = {m('140 - 50 = 90')} kJ."],
        f"أما التغير الحراري ΔH فيساوي {m('20 - 50 = -30')} kJ.",
        diagram_en=_svg_energy_profile(50, 140, 20, None, "en"),
        diagram_ar=_svg_energy_profile(50, 140, 20, None, "ar"),
    ))

    # 6 (Medium): Enthalpy change ΔH for endothermic profile (+70 kJ)
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        f"In the endothermic reaction profile shown, reactants sit at {m('40')} kJ, the peak is at {m('160')} kJ, and products finish at {m('110')} kJ. What is the overall enthalpy change {m('\\Delta H = E_{\\text{products}} - E_{\\text{reactants}}')} (in kJ)?",
        f"في مخطط التفاعل الماص للحرارة الموضح، طاقة المتفاعلات {m('40')} kJ، والقمة {m('160')} kJ، والنواتج {m('110')} kJ. ما قيمة التغير في المحتوى الحراري {m('\\Delta H')} (بوحدة kJ)؟",
        70, [120, -70, 50],
        "Subtract reactant energy from product energy: 110 - 40.",
        "اطرح طاقة المتفاعلات من طاقة النواتج: 110 - 40.",
        f"Evaluate {m('E_{\\text{prod}} - E_{\\text{react}}')}.",
        [f"Products finish at {m('110')} kJ, higher than reactants at {m('40')} kJ.",
         f"{m('\\Delta H = 110 - 40 = +70')} kJ (endothermic absorption)."],
        f"Forward {m('E_a = 160 - 40 = 120')} kJ is larger than {m('\\Delta H = 70')} kJ.",
        "نحسب الفرق بين مستوى النواتج ومستوى المتفاعلات.",
        [f"طاقة النواتج ({m('110')}) أعلى من طاقة المتفاعلات ({m('40')}).",
         f"التغير الحراري {m('\\Delta H = 110 - 40 = +70')} kJ (موجب أي ماص للحرارة)."],
        f"طاقة التنشيط {m('120')} kJ بينما ΔH تساوي {m('+70')} kJ.",
        diagram_en=_svg_energy_profile(40, 160, 110, None, "en"),
        diagram_ar=_svg_energy_profile(40, 160, 110, None, "ar"),
    ))

    # 7 (Medium): Catalyst reduction in Ea (180 - 125 = 55 kJ)
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        f"In the catalyzed reaction profile, reactants start at {m('60')} kJ, the uncatalyzed peak is {m('180')} kJ, the catalyzed peak (dashed red) is {m('125')} kJ, and products end at {m('20')} kJ. By how many kJ did the catalyst <strong>lower</strong> the activation energy?",
        f"في المخطط الموضح، طاقة المتفاعلات {m('60')} kJ، والقمة دون حفّاز {m('180')} kJ، والقمة بوجود الحفّاز (الأحمر المتقطع) {m('125')} kJ، والنواتج {m('20')} kJ. بكم كيلوجول <strong>خفّض</strong> العامل الحفّاز طاقة التنشيط؟",
        55, [65, 120, 40],
        "Compare uncatalyzed Ea (180 - 60 = 120 kJ) and catalyzed Ea (125 - 60 = 65 kJ).",
        "احسب طاقة التنشيط دون حفّاز (180 - 60) ثم بوجود الحفّاز (125 - 60) وأوجد الفرق.",
        f"Compute {m('(180 - 60) - (125 - 60) = 180 - 125')}.",
        [f"Uncatalyzed {m('E_a = 180 - 60 = 120')} kJ; catalyzed {m('E_a = 125 - 60 = 65')} kJ.",
         f"Activation energy reduction = {m('120 - 65 = 55')} kJ."],
        f"Check: {m('\\Delta H = 20 - 60 = -40')} kJ stays completely unchanged.",
        "نحسب الفرق بين القمتين أو بين طاقتي التنشيط.",
        [f"طاقة التنشيط دون حفّاز = {m('180 - 60 = 120')} kJ، ومع الحفّاز = {m('125 - 60 = 65')} kJ.",
         f"مقدار الانخفاض = {m('120 - 65 = 55')} kJ."],
        f"المحتوى الحراري ΔH بقي ثابتاً عند {m('-40')} kJ.",
        diagram_en=_svg_energy_profile(60, 180, 20, 125, "en"),
        diagram_ar=_svg_energy_profile(60, 180, 20, 125, "ar"),
    ))

    # 8 (Medium): Concentration & temperature collision effects
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        "A student reacts magnesium ribbon with hydrochloric acid in four trials. Which combination of acid concentration and temperature produces hydrogen gas at the <strong>fastest</strong> initial rate?",
        "تفاعلت شرائط مغنيسيوم متماثلة مع حمض الهيدروكلوريك في أربع تجارب. أي مزيج من تركيز الحمض ودرجة الحرارة ينتج غاز الهيدروجين بأقصى <strong>سرعة ابتدائية</strong>؟",
        [
            ("2.0 M HCl at 45 °C — more acid particles per liter plus faster molecular speeds and stronger collisions",
             "حمض 2.0 M عند 45 °س — جسيمات حمض أكثر في اللتر مع سرعة حركية أكبر وتصادمات أقوى"),
            ("0.5 M HCl at 45 °C — dilute acid collides more frequently",
             "حمض 0.5 M عند 45 °س — الحمض المخفف يتصادم أكثر"),
            ("2.0 M HCl at 10 °C — cooling speeds up particle kinetic energy",
             "حمض 2.0 M عند 10 °س — التبريد يرفع الطاقة الحركية"),
            ("0.5 M HCl at 10 °C — fewer collisions prevent energy waste",
             "حمض 0.5 M عند 10 °س — قلة التصادمات تسرع التفاعل"),
        ],
        "Higher concentration increases collision count; higher temperature increases both collision count and collision energy above Ea.",
        "زيادة التركيز تزيد عدد التصادمات، ورفع الحرارة يزيد عدد التصادمات وطاقتها فوق طاقة التنشيط.",
        "Maximize both concentration and temperature.",
        ["2.0 M HCl packs 4× as many H⁺ ions per unit volume as 0.5 M HCl.",
         "Heating to 45 °C increases average kinetic energy so far more collisions exceed activation energy."],
        "Both high concentration and high temperature accelerate reaction rate.",
        "نختار أعلى تركيز وأعلى درجة حرارة معاً.",
        ["التركيز 2.0 M يضاعف عدد أيونات الحمض 4 مرات مقارنة بـ 0.5 M فتزداد التصادمات.",
         "الحرارة 45 °س ترفع طاقة حركة الجزيئات فتتجاوز حاجز التنشيط بنسبة أعلى."],
        "اجتماع التركيز الأعلى والحرارة الأعلى يحقق أقصى سرعة.",
    ))

    # 9 (Medium): Identifying combustion, decomposition, double replacement
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        f"Match the three equations in order: (I) {m('2\\,\\text{H}_2\\text{O}_2 \\to 2\\,\\text{H}_2\\text{O} + \\text{O}_2')}, (II) {m('\\text{AgNO}_3 + \\text{NaCl} \\to \\text{AgCl} + \\text{NaNO}_3')}, (III) {m('\\text{CH}_4 + 2\\,\\text{O}_2 \\to \\text{CO}_2 + 2\\,\\text{H}_2\\text{O}')}.",
        f"صنّف المعادلات الثلاث بالترتيب: (I) {m('2\\,\\text{H}_2\\text{O}_2 \\to 2\\,\\text{H}_2\\text{O} + \\text{O}_2')}، (II) {m('\\text{AgNO}_3 + \\text{NaCl} \\to \\text{AgCl} + \\text{NaNO}_3')}، (III) {m('\\text{CH}_4 + 2\\,\\text{O}_2 \\to \\text{CO}_2 + 2\\,\\text{H}_2\\text{O}')}.",
        [
            ("(I) Decomposition, (II) Double replacement, (III) Combustion",
             "(I) تحلل، (II) إحلال مزدوج، (III) احتراق"),
            ("(I) Synthesis, (II) Single replacement, (III) Decomposition",
             "(I) اتحاد، (II) إحلال بسيط، (III) تحلل"),
            ("(I) Combustion, (II) Decomposition, (III) Synthesis",
             "(I) احتراق، (II) تحلل، (III) اتحاد"),
            ("(I) Double replacement, (II) Combustion, (III) Single replacement",
             "(I) إحلال مزدوج، (II) احتراق، (III) إحلال بسيط"),
        ],
        "One compound splitting apart = decomposition; two compounds swapping ions = double replacement; hydrocarbon + O₂ → CO₂ + H₂O = combustion.",
        "انقسام مركب واحد = تحلل؛ تبادل أيونات مركبين = إحلال مزدوج؛ وقود + O₂ ← CO₂ + H₂O = احتراق.",
        "Classify each reaction pattern independently.",
        ["H₂O₂ splits into two products (AB → A + B) → Decomposition.",
         "Ag⁺ and Na⁺ exchange partners NO₃⁻ and Cl⁻ → Double replacement.",
         "CH₄ reacts rapidly with O₂ forming CO₂ and H₂O → Combustion."],
        "Each pattern matches one standard Grade 9 reaction class.",
        "نطابق كل معادلة بنمطها القياسي.",
        ["تفكك H₂O₂ إلى ماء وأكسجين هو تحلل.",
         "تبادل الأيونات بين AgNO₃ و NaCl هو إحلال مزدوج، واحتراق الميثان مع الأكسجين احتراق."],
        "الأنماط الثلاثة واضحة ومميزة.",
    ))

    # 10 (Hard): Reverse activation energy Ea(rev) = 150 - 25 = 125 kJ
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"In the exothermic energy profile shown, reactants are at {m('60')} kJ, the peak is at {m('150')} kJ, and products are at {m('25')} kJ. What is the <strong>reverse activation energy</strong> ({m('E_{a,\\text{rev}}')}, in kJ) required for products to convert back into reactants?",
        f"في مخطط الطاقة الطارد الموضح، طاقة المتفاعلات {m('60')} kJ، والقمة {m('150')} kJ، والنواتج {m('25')} kJ. ما <strong>طاقة التنشيط العكسية</strong> ({m('E_{a,\\text{rev}}')} بوحدة kJ) اللازمة لتحول النواتج عائدةً إلى متفاعلات؟",
        125, [90, 35, 150],
        "The reverse reaction starts from PRODUCTS (25 kJ) and climbs up to the PEAK (150 kJ).",
        "التفاعل العكسي يبدأ من مستوى النواتج (25 kJ) ويصعد إلى القمة (150 kJ).",
        f"Compute {m('E_{a,\\text{rev}} = E_{\\text{peak}} - E_{\\text{products}}')}.",
        [f"Forward {m('E_a = 150 - 60 = 90')} kJ and {m('\\Delta H = 25 - 60 = -35')} kJ.",
         f"Climbing backwards from products ({m('25')} kJ) to the peak ({m('150')} kJ) requires {m('150 - 25 = 125')} kJ."],
        f"Check identity: {m('E_{a,\\text{rev}} = E_{a,\\text{fwd}} - \\Delta H = 90 - (-35) = 125')} kJ.",
        "نحسب المسافة الرأسية من النواتج حتى القمة.",
        [f"طاقة التنشيط الأمامية {m('90')} kJ والفرق الحراري {m('35')} kJ.",
         f"للعودة من النواتج ({m('25')}) إلى القمة ({m('150')}) يلزم {m('150 - 25 = 125')} kJ."],
        f"التحقق: {m('90 + 35 = 125')} kJ.",
        diagram_en=_svg_energy_profile(60, 150, 25, None, "en"),
        diagram_ar=_svg_energy_profile(60, 150, 25, None, "ar"),
    ))

    # 11 (Hard): Reverse Ea for endothermic profile (135 - 95 = 40 kJ)
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"An endothermic reaction has reactant energy {m('30')} kJ, transition peak {m('135')} kJ, and product energy {m('95')} kJ. What is the <strong>reverse activation energy</strong> ({m('E_{a,\\text{rev}}')}, in kJ)?",
        f"لتفاعل ماص للحرارة طاقة متفاعلات {m('30')} kJ، وقمة {m('135')} kJ، وطاقة نواتج {m('95')} kJ. ما قيمة <strong>طاقة التنشيط العكسية</strong> ({m('E_{a,\\text{rev}}')} بوحدة kJ)؟",
        40, [65, 105, 30],
        "Subtract product energy (95 kJ) from peak energy (135 kJ).",
        "اطرح طاقة النواتج (95 kJ) من طاقة القمة (135 kJ).",
        f"Compute {m('135 - 95')}.",
        [f"Forward {m('E_a = 135 - 30 = 105')} kJ and {m('\\Delta H = +65')} kJ.",
         f"Reverse {m('E_{a,\\text{rev}} = 135 - 95 = 40')} kJ."],
        f"Notice in endothermic reactions, {m('E_{a,\\text{rev}} < E_{a,\\text{fwd}}')}.",
        "نطرح طاقة النواتج من طاقة القمة.",
        [f"طاقة التنشيط الأمامية {m('105')} kJ و{m('\\Delta H = +65')} kJ.",
         f"طاقة التنشيط العكسية = {m('135 - 95 = 40')} kJ."],
        "في التفاعل الماص تكون طاقة التنشيط العكسية أصغر من الأمامية.",
        diagram_en=_svg_energy_profile(30, 135, 95, None, "en"),
        diagram_ar=_svg_energy_profile(30, 135, 95, None, "ar"),
    ))

    # 12 (Hard): Gas-volume-vs-time rate curves (same plateau 40 mL, steeper slope)
    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        "In a catalytic decomposition of 50 mL H₂O₂, the baseline curve reaches a final plateau of 40 mL O₂ gas at t = 60 s. Adding MnO₂ catalyst to an <strong>identical</strong> 50 mL H₂O₂ sample produces which change on a Gas Volume vs Time graph?",
        "في تحلل 50 mL من فوق أكسيد الهيدروجين H₂O₂، يصل المنحنى الأساسي إلى سقف ثابت مقداره 40 mL من غاز O₂ عند الزمن 60 ثانية. عند إضافة الحفّاز MnO₂ إلى عينة <strong>مماثلة</strong> (50 mL من H₂O₂)، كيف يتغير المنحنى على رسم الحجم مقابل الزمن؟",
        [
            ("Steeper initial slope reaching the same 40 mL plateau much earlier (e.g., t = 20 s)",
             "ميل ابتدائي أكثر انحداراً يصل إلى السقف نفسه (40 mL) في زمن أقصر بكثير (مثلاً 20 ثانية)"),
            ("Same 60 s time to finish, but final O₂ volume doubles to 80 mL",
             "يستغرق 60 ثانية نفسها لكن الحجم النهائي يتضاعف إلى 80 mL"),
            ("Steeper slope AND triple the final oxygen volume (120 mL)",
             "ميل أشد مع تضاعف حجم الأكسجين النهائي ثلاث مرات (120 mL)"),
            ("Shallower slope finishing later at t = 120 s with 20 mL O₂",
             "ميل أضعف ينتهي متأخراً عند 120 ثانية بحجم 20 mL"),
        ],
        "A catalyst speeds up the rate (steeper slope) without adding extra H₂O₂ reactant (same total yield).",
        "العامل الحفّاز يسرّع التفاعل (ميل أشد) دون أن يضيف مادة متفاعلة جديدة (المحصول النهائي نفسه).",
        "Separate reaction kinetics (initial slope) from stoichiometry (final plateau height).",
        ["The final volume of O₂ depends strictly on the fixed amount of H₂O₂ present (40 mL).",
         "MnO₂ catalyst increases collision success rate, making the curve rise steeper and flatten at 40 mL sooner."],
        "Only adding more H₂O₂ reactant raises the final plateau height.",
        "نميز بين سرعة التفاعل (الميل) وكمية الناتج الكلية (الارتفاع النهائي).",
        ["الحجم الكلي لغاز الأكسجين يعتمد فقط على كمية H₂O₂ الأصلية (40 mL).",
         "العامل الحفّاز يسرّع التفكك فيرتفع المنحنى بانحدار أشد ثم يستقر عند السقف 40 mL مبكراً."],
        "مضاعفة كمية H₂O₂ هي التي تضاعف السقف النهائي.",
        diagram_en=svg_motion_graph([(0, 0), (15, 22), (30, 36), (45, 40), (60, 40)], "O2 (mL)", "Time (s)", "Catalyzed Rate"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 0), (15, 22), (30, 36), (45, 40), (60, 40)], "O2 (mL)", "Time (s)", "Catalyzed Rate"),
                           {"Time (s)": "الزمن (ث)", "Catalyzed Rate": "سرعة التفاعل المحفز"}),
    ))

    # 13 (Hard): Doubling limiting metal vs adding catalyst
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        "Magnesium (0.5 g, limiting reactant) reacts completely with excess acid to yield 500 mL of H₂ gas in 40 s. In Trial 2, the student uses <strong>1.0 g</strong> of Magnesium powder (still excess acid) at the same temperature. How do the <strong>rate</strong> and <strong>total H₂ yield</strong> change?",
        "يتفاعل 0.5 g من شريط المغنيسيوم (مادة محددة) كلياً مع فائض من الحمض لينتج 500 mL من غاز H₂ خلال 40 ثانية. في التجربة 2 استخدم الطالب <strong>1.0 g</strong> من مسحوق المغنيسيوم مع الفائض نفسه من الحمض. كيف تتغير <strong>سرعة التفاعل</strong> و<strong>الحجم الكلي للغاز</strong>؟",
        [
            ("Both initial rate increases (powder surface area) and total H₂ volume doubles to 1,000 mL (twice the limiting Mg)",
             "تزداد السرعة الابتدائية (لزيادة مساحة السطح بالمسحوق) ويتضاعف الحجم الكلي للغاز إلى 1,000 mL (لمضاعفة المادة المحددة)"),
            ("Initial rate increases, but total H₂ stays fixed at 500 mL",
             "تزداد السرعة الابتدائية بينما يبقى الحجم الكلي ثابتاً عند 500 mL"),
            ("Total H₂ doubles to 1,000 mL, but initial rate drops by half",
             "يتضاعف الحجم إلى 1,000 mL وتنخفض السرعة إلى النصف"),
            ("Both rate and total H₂ volume stay unchanged because acid was already excess",
             "تبقى السرعة والحجم ثابتين لأن الحمض كان فائضاً أصلاً"),
        ],
        "Because Mg is the limiting reactant, doubling Mg doubles the maximum H₂ produced, AND powdering accelerates collisions.",
        "بما أن المغنيسيوم هو المادة المحددة، فمضاعفته تضاعف كمية الغاز، وسحقه لمسحوق يسرّع التفاعل.",
        "Analyze surface area effect (kinetics) + doubled limiting reactant (stoichiometry).",
        ["Powdering Mg exposes far more metal surface area to H⁺ ions → faster initial rate.",
         "Doubling the limiting reactant (0.5 g → 1.0 g) with excess acid doubles produced H₂ gas (500 mL → 1,000 mL)."],
        "Always check whether the doubled substance is limiting or excess!",
        "ندرس أثرين معاً: السحق يسرّع، ومضاعفة المادة المحددة تضاعف الناتج.",
        ["طحن المغنيسيوم يزيد مساحة السطح فيسرّع انطلاق الفقاعات.",
         "مضاعفة كتلة المادة المحددة (مع توفر حمض فائض) تضاعف حجم الهيدروجين الناتج إلى 1,000 mL."],
        "التحقق من المادة المحددة يحدد تغير المحصول النهائي.",
    ))

    # 14 (Hard): Cold pack endothermic enthalpy reasoning
    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        "When ammonium nitrate (NH₄NO₃) crystals dissolve inside an athletic instant cold pack, the water temperature drops from 24 °C down to 4 °C. Which energy change explains why the pack feels cold?",
        "عند ذوبان بلورات نترات الأمونيوم (NH₄NO₃) داخل كمادة تبريد رياضية فورية، تنخفض حرارة الماء من 24 °س إلى 4 °س. ما تفسير الطاقة الذي يسبب الشعور بالبرودة؟",
        [
            ("Dissolving is endothermic: breaking crystal forces absorbs thermal energy from the water and skin, raising products' potential energy",
             "الذوبان ماص للحرارة؛ إذ يمتص طاقة حرارية من الماء والجلد ليرفع طاقة وضع النواتج، فتبرد البيئة المحيطة"),
            ("Dissolving is exothermic: energy exits the cold pack into the athlete's skin",
             "الذوبان طارد للحرارة؛ إذ تخرج الحرارة من الكمادة إلى جلد الرياضي"),
            ("Thermal energy is permanently destroyed when ionic crystals dissolve",
             "تفنى الطاقة الحرارية نهائياً عند ذوبان البلورات الأيونية"),
            ("NH₄NO₃ radiates cold particles directly through plastic walls",
             "تشع بلورات نترات الأمونيوم جسيمات باردة عبر البلاستيك"),
        ],
        "The thermometer sits in the surrounding water, so a temperature drop means heat flowed OUT of the water into chemical potential energy.",
        "الترمومتر يقيس الوسط المحيط (الماء)؛ هبوط حرارته يعني أن التفاعل سحب حرارة منه لتخزينها كطاقة كيميائية.",
        "Relate cooling surroundings to positive ΔH (endothermic process).",
        ["Separating NH₄⁺ and NO₃⁻ crystal lattice ions costs more energy than hydration returns.",
         "That net energy deficit is pulled from the water's thermal kinetic energy, lowering temperature to 4 °C."],
        "Endothermic processes cool their surroundings; exothermic processes warm them.",
        "نربط انخفاض حرارة المحيط بامتصاص الطاقة (عملية ماصة للحرارة).",
        ["فصل أيونات الشبكة البلورية لـ NH₄NO₃ يحتاج طاقة أكبر من طاقة الإماهة الناتجة.",
         "يُسحب هذا الفرق من الطاقة الحرارية للماء فتبرد الكمادة إلى 4 °س."],
        "العملية الماصة تبرد المحيط بينما العملية الطاردة تسخنه.",
    ))
    return qs


def _gen_sci_b12(start_idx: int) -> list[dict]:
    """G9-SCI-B12: pH scale 10x step & acid-base neutralization."""
    bp = "G9-SCI-B12"
    qs: list[dict] = []

    # 0 (Easy): Vinegar pH 3 classification
    qs.append(make_science_concept_q(
        _qid(start_idx + 0), LEVEL, T_CHEM, "Easy", bp,
        "On the pH scale diagram, household vinegar is marked at pH 3. Which set of properties correctly describes a pH 3 solution?",
        "في مخطط مقياس الرقم الهيدروجيني (pH)، يقع الخل المنزلي عند pH = 3. أي مجموعة خصائص تصف محلولاً رقمه الهيدروجيني 3 بدقة؟",
        [
            ("Acidic; higher H⁺ ion concentration than pure water and turns blue litmus paper red",
             "حمضي؛ تركيز أيونات H⁺ فيه أعلى من الماء النقي ويحمر ورقة تباع الشمس الزرقاء"),
            ("Basic (alkaline); higher OH⁻ concentration and turns red litmus blue",
             "قاعدي؛ تركيز أيونات OH⁻ فيه أعلى ويزرّق ورقة تباع الشمس الحمراء"),
            ("Neutral; equal concentrations of H⁺ and OH⁻ ions",
             "متعادل؛ يتساوى فيه تركيز أيونات H⁺ و OH⁻"),
            ("Strongly alkaline; reacts vigorously with bases to release H₂ gas",
             "قاعدي قوي؛ يتفاعل مع القواعد لإطلاق غاز الهيدروجين"),
        ],
        "Values below 7 on the pH scale are acidic; remember Acid = Red litmus.",
        "القيم الأقل من 7 حمضية، والحمض يحوّل ورق تباع الشمس إلى اللون الأحمر.",
        "Check pH 3 < 7 and acid-indicator behavior.",
        ["pH 3 lies well below neutral pH 7, placing vinegar in the acidic region.",
         "Acids release excess hydrogen ions (H⁺) and turn blue litmus paper red."],
        "Bases (pH > 7) turn red litmus blue and feel slippery.",
        "نحدد المنطقة الحمضية تحت 7 وأثرها على الكاشف.",
        ["الرقم 3 أقل من 7 فهو محلول حمضي غني بأيونات H⁺.",
         "الأحماض تحوّل ورق تباع الشمس الأزرق إلى أحمر."],
        "القواعد فوق 7 تزرّق ورق تباع الشمس الأحمر.",
        diagram_en=svg_ph_scale(3, "Vinegar", "pH Scale: Vinegar"),
        diagram_ar=_ar_svg(svg_ph_scale(3, "Vinegar", "pH Scale: Vinegar"),
                           {"Vinegar": "الخل", "pH Scale: Vinegar": "مقياس pH: الخل"}),
    ))

    # 1 (Easy): Ammonia pH 11 classification
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_CHEM, "Easy", bp,
        "Household ammonia cleaner registers pH 11 on the scale shown. Which statement accurately describes this solution?",
        "يسجل منظف الأمونيا المنزلي قيمة pH = 11 على المقياس الموضح. أي عبارة تصف هذا المحلول بدقة؟",
        [
            ("Basic (alkaline); has higher OH⁻ than H⁺ concentration and turns red litmus paper blue",
             "قاعدي (قلوي)؛ تركيز OH⁻ فيه أعلى من H⁺ ويزرّق ورقة تباع الشمس الحمراء"),
            ("Acidic; donates excess H⁺ ions to turn blue litmus red",
             "حمضي؛ يمنح أيونات H⁺ الزائدة ويحمر ورق تباع الشمس"),
            ("Neutral; matches distilled water at 25 °C",
             "متعادل؛ يطابق الماء المقطر عند 25 °س"),
            ("Has zero hydroxide (OH⁻) ions present in solution",
             "يخلو المحلول تماماً من أيونات الهيدروكسيد (OH⁻)"),
        ],
        "Values above 7 up to 14 are basic (alkaline); remember Base = Blue litmus.",
        "القيم فوق 7 حتى 14 قاعدية، والقاعدة تزرّق ورق تباع الشمس.",
        "Identify pH 11 > 7 characteristics.",
        ["At pH 11, hydroxide ion concentration (OH⁻) vastly exceeds hydrogen ion concentration (H⁺).",
         "Basic solutions feel slippery, taste bitter (never taste chemicals in lab!), and turn red litmus paper blue."],
        "Strong bases like NaOH reach pH 13–14.",
        "نحدد خواص المحاليل القاعدية فوق 7.",
        ["عند pH = 11 يفوق تركيز أيونات الهيدروكسيد OH⁻ تركيز أيونات H⁺ بكثير.",
         "المحاليل القاعدية تزرّق ورق تباع الشمس الأحمر."],
        "القواعد القوية تصل قيمتها إلى 13–14.",
        diagram_en=svg_ph_scale(11, "Ammonia", "pH Scale: Ammonia"),
        diagram_ar=_ar_svg(svg_ph_scale(11, "Ammonia", "pH Scale: Ammonia"),
                           {"Ammonia": "الأمونيا", "pH Scale: Ammonia": "مقياس pH: الأمونيا"}),
    ))

    # 2 (Easy): Acid + Base neutralization products
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_CHEM, "Easy", bp,
        f"When hydrochloric acid ({m('\\text{HCl}')}) reacts completely with sodium hydroxide ({m('\\text{NaOH}')}) in an acid–base neutralization reaction, what two products form?",
        f"عند تفاعل حمض الهيدروكلوريك ({m('\\text{HCl}')}) كلياً مع هيدروكسيد الصوديوم ({m('\\text{NaOH}')}) في تفاعل تعادل، ما الناتجان المتكوّنان؟",
        [
            ("A salt (NaCl) and water (H₂O)", "ملح (NaCl) وماء (H₂O)"),
            ("Hydrogen gas (H₂) and solid sodium metal", "غاز الهيدروجين (H₂) وفلز الصوديوم"),
            ("Carbon dioxide (CO₂) and oxygen gas (O₂)", "ثاني أكسيد الكربون وغاز الأكسجين"),
            ("Pure hydrochloric acid and ammonia gas", "حمض الهيدروكلوريك النقي وغاز الأمونيا"),
        ],
        "H⁺ from the acid combines with OH⁻ from the base to make H₂O, leaving the cation and anion to form a salt.",
        "يتحد H⁺ من الحمض مع OH⁻ من القاعدة لتكوين الماء، ويتحد باقي الأيونين لتكوين الملح.",
        "Write HCl + NaOH → NaCl + H₂O.",
        ["H⁺ + OH⁻ → H₂O (neutral water).",
         "Na⁺ + Cl⁻ → NaCl (ionic salt)."],
        "Neutralization always produces a salt and water (plus CO₂ if a carbonate base is used).",
        "نكتب معادلة التعادل كاملة.",
        ["أيون الهيدروجين H⁺ يتحد مع الهيدروكسيد OH⁻ مكوناً جزيء الماء H₂O.",
         "ويتحد أيون الصوديوم Na⁺ مع الكلوريد Cl⁻ لتكوين ملح الطعام NaCl."],
        "القاعدة العامة للتعادل: حمض + قاعدة ← ملح + ماء.",
    ))

    # 3 (Easy): Neutral pH 7 condition
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_CHEM, "Easy", bp,
        "At 25 °C, pure distilled water has a pH of exactly 7.0. What is true about its hydrogen ion ([H⁺]) and hydroxide ion ([OH⁻]) concentrations?",
        "عند 25 °س، يبلغ الرقم الهيدروجيني للماء المقطر النقي 7.0 تماماً. ما العلاقة الصحيحة بين تركيز أيونات الهيدروجين [H⁺] وأيونات الهيدروكسيد [OH⁻] فيه؟",
        [
            ("They are equal: [H⁺] = [OH⁻]", "متساويان تماماً: [H⁺] = [OH⁻]"),
            ("[H⁺] is 7 times higher than [OH⁻]", "[H⁺] أكبر 7 مرات من [OH⁻]"),
            ("Neither H⁺ nor OH⁻ ions exist at all in pure water", "ينعدم وجود كل من H⁺ و OH⁻ تماماً"),
            ("[OH⁻] is 100 times greater than [H⁺]", "[OH⁻] أكبر 100 مرة من [H⁺]"),
        ],
        "Neutrality means positive H⁺ and negative OH⁻ ions from self-ionization balance identically.",
        "التعادل يعني تساوي أيونات الهيدروجين والهيدروكسيد الناتجة عن التأين الذاتي للماء.",
        "Recall [H⁺] = [OH⁻] = 10⁻⁷ M at pH 7.",
        ["Pure water undergoes tiny self-ionization: H₂O ⇌ H⁺ + OH⁻.",
         "Because each dissociated water molecule yields one H⁺ and one OH⁻, [H⁺] = [OH⁻] at pH 7."],
        "Adding acid raises [H⁺] and drops pH below 7; adding base raises [OH⁻] and pushes pH above 7.",
        "نربط الرقم الهيدروجيني 7 بتساوي الأيونين عند 25 °س.",
        ["يتأين الماء النقي ذاتياً بدرجة ضئيلة منتجاً عدداً متساوياً من أيونات H⁺ و OH⁻.",
         "لذا يتعادل التركيزان تماماً عند pH = 7."],
        "إضافة حمض ترفع H⁺ وتخفض pH؛ وإضافة قاعدة تعكس ذلك.",
        diagram_en=svg_ph_scale(7, "Water", "pH Scale: Pure Water"),
        diagram_ar=_ar_svg(svg_ph_scale(7, "Water", "pH Scale: Pure Water"),
                           {"Water": "الماء", "pH Scale: Pure Water": "مقياس pH: ماء نقي"}),
    ))

    # 4 (Easy): Most acidic among pH 2, 5, 7, 10
    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_CHEM, "Easy", bp,
        f"Four aqueous test samples have pH readings of {m('2, 5, 7,')} and {m('10')}. Which pH value corresponds to the sample with the <strong>highest</strong> concentration of hydrogen ions ({m('[\\text{H}^+]')})?",
        f"أربع عينات مائية قراءات رقمها الهيدروجيني هي {m('2, 5, 7,')} و{m('10')}. أي قيمة pH تمثل العينة ذات التركيز <strong>الأعلى</strong> من أيونات الهيدروجين ({m('[\\text{H}^+]')})؟",
        2, [5, 7, 10],
        "Lower pH numbers correspond to higher acidity and greater [H⁺] concentration.",
        "كلما صغرت قيمة pH زادت الحمضية وارتفع تركيز أيونات الهيدروجين [H⁺].",
        "Select the lowest number on the 0–14 pH scale.",
        [f"On the pH scale, acidity increases as pH decreases toward {m('0')}.",
         f"Among {m('2, 5, 7, 10')}, {m('\\text{pH} = 2')} has the greatest {m('[\\text{H}^+]')} concentration."],
        f"In fact, pH 2 has {m('1,000')} times higher {m('[\\text{H}^+]')} than pH 5!",
        "نختار أصغر رقم على مقياس pH لأنه يمثل الحمضية الأقوى.",
        [f"تزداد الحمضية وتركيز H⁺ كلما اقتربت قيمة pH من الصفر.",
         f"أصغر قيمة هي {m('2')}، لذا تملك أعلى تركيز لأيونات H⁺."],
        f"الرقم pH=2 أعلى حمضية بـ 1,000 مرة من pH=5.",
    ))

    # 5 (Medium): 10-fold step pH 2 vs pH 5 -> 1,000x
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_CHEM, "Medium", bp,
        f"Because the pH scale steps by a factor of {m('10')} per unit, lemon juice at {m('\\text{pH} = 2')} has how many times higher {m('[\\text{H}^+]')} concentration than black coffee at {m('\\text{pH} = 5')}?",
        f"نظراً لأن مقياس pH يتغير بمضاعفات {m('10')} لكل وحدة، كم مرة يزيد تركيز أيونات {m('[\\text{H}^+]')} في عصير الليمون ({m('\\text{pH} = 2')}) مقارنة بالقهوة السوداء ({m('\\text{pH} = 5')})؟",
        1000, [3, 30, 100],
        "Each drop of 1 pH unit multiplies [H⁺] by 10, so a 3-unit difference is 10³.",
        "كل نقص بمقدار وحدة واحدة في pH يضاعف [H⁺] بمقدار 10 مرات، ففرق 3 وحدات يعني 10 أس 3.",
        f"Compute {m('10^{5 - 2}')}.",
        [f"Difference in pH units = {m('5 - 2 = 3')}.",
         f"Factor = {m('10 \\times 10 \\times 10 = 10^3 = 1,000')} times higher {m('[\\text{H}^+]')}."],
        "Never multiply 3 × 10 = 30; the pH scale uses powers of 10!",
        "نرفع العدد 10 إلى أس الفرق بين قيمتي pH.",
        [f"الفرق في وحدات pH يساوي {m('5 - 2 = 3')}.",
         f"نسبة التركيز = {m('10^3 = 1,000')} مرة."],
        "المقياس يضرب في 10 عند كل وحدة وليس جمعاً أو ضرباً في 3.",
        diagram_en=svg_ph_scale(2, "Lemon", "10x Step per pH Unit"),
        diagram_ar=_ar_svg(svg_ph_scale(2, "Lemon", "10x Step per pH Unit"),
                           {"Lemon": "الليمون", "10x Step per pH Unit": "مضاعفة 10 مرات لكل وحدة pH"}),
    ))

    # 6 (Medium): Basic [OH-] step pH 12 vs pH 9 -> 1,000x
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_CHEM, "Medium", bp,
        f"Household bleach at {m('\\text{pH} = 12')} is compared to baking soda solution at {m('\\text{pH} = 9')}. How many times higher is the hydroxide ion concentration ({m('[\\text{OH}^-]')}) in bleach than in baking soda?",
        f"قورن محلول مبيّض منزلي ({m('\\text{pH} = 12')}) بمحلول صودا الخبز ({m('\\text{pH} = 9')}). كم مرة يزيد تركيز أيونات الهيدروكسيد ({m('[\\text{OH}^-]')}) في المبيّض مقارنة بصودا الخبز؟",
        1000, [3, 100, 10000],
        "Every 1-unit increase in pH raises [OH⁻] by a factor of 10.",
        "كل زيادة بمقدار وحدة واحدة في pH تزيد تركيز [OH⁻] بمقدار 10 أضعاف.",
        f"Compute {m('10^{12 - 9}')}.",
        [f"The pH rises by {m('12 - 9 = 3')} units.",
         f"Each unit multiplies {m('[\\text{OH}^-]')} by {m('10')}, giving {m('10^3 = 1,000')} times higher {m('[\\text{OH}^-]')}."],
        "Simultaneously, [H⁺] is 1,000 times lower at pH 12 than at pH 9.",
        "نحسب 10 أس فرق الوحدات.",
        [f"الفرق بين 12 و 9 هو {m('3')} وحدات.",
         f"زيادة كل وحدة تضاعف [OH⁻] عشر مرات: {m('10^3 = 1,000')} مرة."],
        "في الوقت نفسه يقل [H⁺] بمقدار 1,000 مرة.",
        diagram_en=svg_ph_scale(12, "Bleach", "Alkaline [OH-] Scaling"),
        diagram_ar=_ar_svg(svg_ph_scale(12, "Bleach", "Alkaline [OH-] Scaling"),
                           {"Bleach": "المبيض", "Alkaline [OH-] Scaling": "تدرج القاعدية [OH-]"}),
    ))

    # 7 (Medium): Balanced salt product H2SO4 + 2KOH -> K2SO4 + 2H2O
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_CHEM, "Medium", bp,
        f"Sulfuric acid ({m('\\text{H}_2\\text{SO}_4')}) is completely neutralized by potassium hydroxide ({m('\\text{KOH}')}). What is the correct balanced formula of the <strong>salt</strong> formed alongside water?",
        f"يتعادل حمض الكبريتيك ({m('\\text{H}_2\\text{SO}_4')}) كلياً مع هيدروكسيد البوتاسيوم ({m('\\text{KOH}')}). ما الصيغة الصحيحة <strong>للملح</strong> المتكون مع الماء؟",
        [
            (m("\\text{K}_2\\text{SO}_4"), m("\\text{K}_2\\text{SO}_4")),
            (m("\\text{KSO}_4"), m("\\text{KSO}_4")),
            (m("\\text{K}(\\text{SO}_4)_2"), m("\\text{K}(\\text{SO}_4)_2")),
            (m("\\text{KH}"), m("\\text{KH}")),
        ],
        "Combine the base cation (K⁺) with the acid anion (SO₄²⁻) using the crisscross rule.",
        "اجمع كاتيون القاعدة (K⁺) مع أنيون الحمض (SO₄²⁻) بطريقة المقص.",
        "Balance +1 Potassium ions with -2 Sulfate ion.",
        ["H₂SO₄ contributes sulfate ions SO₄²⁻ while KOH contributes potassium ions K⁺.",
         "Two K⁺ ions balance one SO₄²⁻ ion → K₂SO₄, via H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O."],
        "Always check ion charges: 2(+1) + (-2) = 0.",
        "نركب الملح من أيون الفلز في القاعدة والأيون السالب للحمض.",
        ["أيون البوتاسيوم K⁺ (+1) يتحد مع أيون الكبريتات SO₄²⁻ (-2).",
         "لتعادل الشحنة يلزم أيونا بوتاسيوم: K₂SO₄."],
        "المعادلة الكاملة: H₂SO₄ + 2KOH ← K₂SO₄ + 2H₂O.",
    ))

    # 8 (Medium): Reading titration equivalence volume from graph
    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_CHEM, "Medium", bp,
        "During a titration experiment, strong base NaOH is slowly dripped into 25 mL of HCl acid while a sensor logs pH as shown in the graph. How many <strong>mL of NaOH</strong> were required to reach exact neutralization (equivalence at pH = 7)?",
        "خلال تجربة معايرة، أُضيفت قاعدة NaOH تدريجياً إلى 25 mL من حمض HCl وسُجّل تغير pH في الرسم البياني. كم <strong>مللتراً من NaOH</strong> لزم للوصول إلى نقطة التعادل (pH = 7)؟",
        25, [15, 35, 50],
        "Find the horizontal Volume (mL) coordinate directly where the pH curve passes steeply through pH 7.",
        "اقرأ قيمة الحجم (mL) على المحور الأفقي عندما يعبر المنحنى النقطة pH = 7.",
        "Match pH = 7 on the vertical axis to the steep midpoint x-value.",
        ["From 0 to 20 mL, pH rises slowly from 1 to 2.5 (excess acid remains).",
         "At 25 mL, the curve shoots vertically through pH = 7 (equivalence point) before flattening near pH 12.5."],
        "After 25 mL, excess unreacted NaOH makes the solution strongly basic.",
        "نحدد على المحور الأفقي الحجم الموافق للارتفاع الحاد عند pH = 7.",
        ["بين 0 و 20 mL يظل الوسط حمضياً (pH منخفض).",
         "عند الحجم 25 mL يقفز المنحنى عمودياً ماراً بنقطة التعادل pH = 7."],
        "بعد 25 mL تصبح القاعدة زائدة ويرتفع pH نحو 13.",
        diagram_en=svg_motion_graph([(0, 1), (15, 2), (21, 3), (25, 7), (29, 11), (36, 12.5)],
                                    "pH", "NaOH (mL)", "Titration Curve"),
        diagram_ar=_ar_svg(svg_motion_graph([(0, 1), (15, 2), (21, 3), (25, 7), (29, 11), (36, 12.5)],
                                            "pH", "NaOH (mL)", "Titration Curve"),
                           {"NaOH (mL)": "حجم NaOH (مل)", "Titration Curve": "منحنى المعايرة"}),
    ))

    # 9 (Medium): Acid rain pH 4 vs normal rain pH 6 (100x)
    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_CHEM, "Medium", bp,
        f"Normal unpolluted rain has {m('\\text{pH} = 6')}, while industrial sulfur oxides produce acid rain at {m('\\text{pH} = 4')}. How many times more acidic (higher {m('[\\text{H}^+]')}) is the acid rain than normal rain?",
        f"للأمطار الطبيعية غير الملوثة {m('\\text{pH} = 6')}، بينما تسبب أكاسيد الكبريت الصناعية مطراً حمضياً عند {m('\\text{pH} = 4')}. كم مرة تزيد حمضية المطر الحمضي (تركيز {m('[\\text{H}^+]')}) مقارنة بالمطر الطبيعي؟",
        100, [2, 20, 1000],
        "Two pH units lower means 10 × 10 times more [H⁺].",
        "انخفاض وحدتين في pH يعني زيادة [H⁺] بمقدار 10 × 10 مرات.",
        f"Evaluate {m('10^{6 - 4}')}.",
        [f"The pH drop is {m('6 - 4 = 2')} units.",
         f"Concentration ratio = {m('10^2 = 100')} times higher {m('[\\text{H}^+]')}."],
        "Acid rain corrodes limestone monuments and acidifies freshwater lakes.",
        "نرفع 10 إلى أس فرق الوحدتين.",
        [f"الفرق بين 6 و 4 هو وحدتان.",
         f"نسبة التركيز = {m('10^2 = 100')} مرة."],
        "المطر الحمضي يآكل الصخور الجيرية ويضر بالبيئة المائية.",
        diagram_en=svg_ph_scale(4, "Acid Rain", "Acid Rain (pH 4)"),
        diagram_ar=_ar_svg(svg_ph_scale(4, "Acid Rain", "Acid Rain (pH 4)"),
                           {"Acid Rain": "مطر حمضي", "Acid Rain (pH 4)": "مطر حمضي (pH 4)"}),
    ))

    # 10 (Hard): 100-fold dilution of pH 2 strong acid -> pH 4
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_CHEM, "Hard", bp,
        f"A chemist takes {m('10')} mL of a strong hydrochloric acid solution at {m('\\text{pH} = 2')} and dilutes it with distilled water to a final volume of {m('1,000')} mL. What is the new pH of the diluted solution?",
        f"أخذ كيميائي {m('10')} mL من حمض الهيدروكلوريك القوي عند {m('\\text{pH} = 2')} وخففه بالماء المقطر حتى أصبح الحجم النهائي {m('1,000')} mL. ما قيمة pH الجديدة للمحلول المخفف؟",
        4, [0, 3, 200],
        "Find the dilution factor (1,000 / 10 = 100 = 10²); diluting an acid 100× lowers [H⁺] by 10², raising pH by 2.",
        "احسب معامل التخفيف (1,000 / 10 = 100 = 10²)؛ تقليل [H⁺] بمقدار 100 مرة يرفع pH بوحدتين.",
        f"Compute dilution factor {m('1,000 / 10 = 10^2')} and add {m('2')} to pH {m('2')}.",
        [f"Volume increases by a factor of {m('1,000 \\div 10 = 100 = 10^2')}.",
         f"Therefore {m('[\\text{H}^+]')} drops by a factor of {m('10^2')}, increasing pH by {m('2')} units: {m('2 + 2 = 4')}."],
        "Remember diluting an acid raises pH toward 7, never past 7!",
        "نحسب معامل التخفيف كقوة للعدد 10 ونضيف الأس إلى pH الحمض.",
        [f"تضاعف الحجم {m('1000 \\div 10 = 100 = 10^2')} مرة، فقل تركيز H⁺ مئة مرة.",
         f"يزداد pH بمقدار وحدتين: {m('2 + 2 = 4')}."],
        "تخفيف الحمض بالماء يرفع pH نحو 7 ولا يتجاوزها.",
    ))

    # 11 (Hard): [H+] ratio pH 3 vs pH 7 (10,000)
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_CHEM, "Hard", bp,
        f"Solution X measures {m('\\text{pH} = 3')} and neutral Solution Y measures {m('\\text{pH} = 7')}. What is the ratio {m('[\\text{H}^+]_X / [\\text{H}^+]_Y')}?",
        f"قيمة الرقم الهيدروجيني للمحلول X هي {m('\\text{pH} = 3')} وللمحلول المتعادل Y هي {m('\\text{pH} = 7')}. ما قيمة النسبة {m('[\\text{H}^+]_X / [\\text{H}^+]_Y')}؟",
        10000, [1000, 40, 100000],
        "Count the pH difference (7 - 3 = 4 units) and raise 10 to that power.",
        "احسب الفرق (7 - 3 = 4 وحدات) ثم ارفع العدد 10 لهذا الأس.",
        f"Compute {m('10^{7 - 3}')}.",
        [f"Solution X is {m('7 - 3 = 4')} pH units lower than Y.",
         f"Each unit multiplies {m('[\\text{H}^+]')} by {m('10')}, so the ratio is {m('10^4 = 10,000')}."],
        f"Check: {m('10^{-3} / 10^{-7} = 10^4 = 10,000')}.",
        "نطبق عامل الـ 10 أضعاف عبر 4 وحدات.",
        [f"الفرق بين 7 و 3 هو {m('4')} وحدات.",
         f"إذن النسبة = {m('10^4 = 10,000')}."],
        f"التحقق: {m('10^{-3} \\div 10^{-7} = 10^4 = 10,000')}.",
    ))

    # 12 (Hard): Diprotic H2SO4 vs NaOH neutralization volume (200 mL)
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_CHEM, "Hard", bp,
        f"Sulfuric acid ({m('\\text{H}_2\\text{SO}_4')}) releases {m('2\\,\\text{H}^+')} ions per molecule, reacting with {m('\\text{NaOH}')} via {m('\\text{H}_2\\text{SO}_4 + 2\\,\\text{NaOH} \\to \\text{Na}_2\\text{SO}_4 + 2\\,\\text{H}_2\\text{O}')}. How many mL of {m('0.1\\text{ M NaOH}')} are required to completely neutralize {m('100')} mL of {m('0.1\\text{ M H}_2\\text{SO}_4')}?",
        f"يعطي جزيء حمض الكبريتيك ({m('\\text{H}_2\\text{SO}_4')}) أيوني هيدروجين ({m('2\\,\\text{H}^+')}) وفق المعادلة {m('\\text{H}_2\\text{SO}_4 + 2\\,\\text{NaOH} \\to \\text{Na}_2\\text{SO}_4 + 2\\,\\text{H}_2\\text{O}')}. كم مللتراً من محلول {m('0.1\\text{ M NaOH}')} يلزم لمعادلة {m('100')} mL من {m('0.1\\text{ M H}_2\\text{SO}_4')} تماماً؟",
        200, [50, 100, 400],
        "Notice the 1 : 2 stoichiometry—each H₂SO₄ molecule requires TWO NaOH units to neutralize both H⁺ ions.",
        "لاحظ نسبة المعاملات 1 : 2 — كل جزيء H₂SO₄ يحتاج جزيئين من NaOH لمعادلة أيوني الهيدروجين.",
        "Double the equal-concentration acid volume because of the 2:1 NaOH:H₂SO₄ ratio.",
        [f"Both solutions have identical concentration ({m('0.1\\text{ M}')}), but each {m('\\text{H}_2\\text{SO}_4')} donates {m('2\\,\\text{H}^+')} while {m('\\text{NaOH}')} supplies {m('1\\,\\text{OH}^-')}.",
         f"Neutralizing {m('100')} mL of diprotic acid takes {m('2 \\times 100 = 200')} mL of monoprotic base."],
        "For monoprotic HCl (1 H⁺), 100 mL of 0.1 M HCl would take only 100 mL of 0.1 M NaOH.",
        "نضاعف حجم القاعدة بسبب ثنائية بروتونات حمض الكبريتيك.",
        [f"التركيزان متساويان (0.1 M)، لكن الحمض يعطي أيوني H⁺ بينما القاعدة تعطي OH⁻ واحداً فقط.",
         f"لذا يلزم ضعف الحجم: {m('2 \\times 100 = 200')} mL من NaOH."],
        "لو كان الحمض HCl أحادي الهيدروجين لاحتاج 100 mL فقط.",
    ))

    # 13 (Hard): Strong vs weak acid equal molarity neutralization comparison
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_CHEM, "Hard", bp,
        "Beaker 1 contains 50 mL of 0.1 M HCl (a strong acid, fully ionized, pH 1). Beaker 2 contains 50 mL of 0.1 M acetic acid (a weak acid, partially ionized, pH 3). How do the <strong>volumes of 0.1 M NaOH</strong> needed to completely neutralize Beaker 1 and Beaker 2 compare?",
        "الكأس 1 يحتوي 50 mL من حمض قوي HCl تركيزه 0.1 M (يتأين كلياً، pH=1)، والكأس 2 يحتوي 50 mL من حمض ضعيف CH₃COOH تركيزه 0.1 M (يتأين جزئياً، pH=3). كيف يقارن <strong>حجم محلول 0.1 M NaOH</strong> اللازم لمعادلة الكأسين كلياً؟",
        [
            ("Both require the exact same 50 mL of NaOH because both contain the same total moles of ionizable acid",
             "يتطلبان الحجم نفسه تماماً (50 mL) من NaOH لأن كليهما يحتوي عدد مولات الحمض القابل للتعادل نفسه"),
            ("Beaker 1 requires 100 times more NaOH because its pH is 2 units lower",
             "يحتاج الكأس 1 إلى 100 ضعف حجم NaOH لأن pH أقل بوحدتين"),
            ("Beaker 2 requires 3 times more NaOH because its pH is 3",
             "يحتاج الكأس 2 إلى 3 أضعاف حجم NaOH لأن pH يساوي 3"),
            ("Beaker 2 cannot be neutralized by NaOH because weak acids lack H⁺",
             "لا يتعادل الكأس 2 مع NaOH لأن الحمض الضعيف يخلو من H⁺"),
        ],
        "As NaOH consumes free H⁺ in Beaker 2, remaining un-ionized acetic acid molecules ionize completely until all 0.1 M is neutralized!",
        "كلما استهلكت القاعدة أيونات H⁺ الحرة في الكأس 2، يتأين مزيد من الحمض الضعيف حتى يتعادل المجموع الكلي نفسه.",
        "Distinguish initial pH (degree of ionization) from total titratable acid moles (M × V).",
        ["Both 50 mL × 0.1 M monoprotic acid solutions contain identical total acid molecules (0.005 moles each).",
         "Though Beaker 2 starts at pH 3 due to partial ionization, adding OH⁻ pulls its equilibrium completely forward so all 0.005 mol reacts with 50 mL NaOH."],
        "pH measures free [H⁺] at a moment; titration volume measures total acid capacity.",
        "نميز بين درجة التأين اللحظية (pH) وكمية الحمض الكلية المولية.",
        ["الحجم والتركيز متطابقان (50 mL × 0.1 M)، أي عدد الجزيئات الحمضية الكلي متساوٍ في الكأسين.",
         "إضافة القاعدة تسحب تأين الحمض الضعيف حتى يتفاعل بالكامل، فيستلزم 50 mL NaOH مثل الحمض القوي."],
        "pH يقيس [H⁺] الحر لحظياً، أما المعايرة فتقيس الكمية الكلية.",
    ))

    # 14 (Hard): Dilution of pH 1 acid by 1,000x -> pH 4
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_CHEM, "Hard", bp,
        f"A wastewater tank holds an acidic solution at {m('\\text{pH} = 1')}. Engineers neutralize or dilute the stream so that its hydrogen ion concentration {m('[\\text{H}^+]')} decreases by a factor of {m('1,000')}. What is the resulting pH?",
        f"يحتوي خزان مياه صرف صناعي على محلول حمضي عند {m('\\text{pH} = 1')}. عالج المهندسون المحلول فانخفض تركيز أيونات الهيدروجين {m('[\\text{H}^+]')} بمقدار {m('1,000')} مرة. ما قيمة pH الناتجة؟",
        4, [0, 3, 10],
        "Decreasing [H⁺] by 1,000 = 10³ shifts pH UP by 3 units.",
        "انخفاض [H⁺] بمقدار 1,000 = 10³ يرفع قيمة pH بمقدار 3 وحدات.",
        f"Note {m('1,000 = 10^3')} and add {m('3')} to initial pH {m('1')}.",
        [f"Since {m('1,000 = 10^3')}, reducing {m('[\\text{H}^+]')} by {m('1,000\\times')} raises pH by {m('3')} units.",
         f"New pH = {m('1 + 3 = 4')}."],
        f"Check reverse step: pH 1 has {m('10^{4-1} = 1,000\\times')} higher {m('[\\text{H}^+]')} than pH 4.",
        "نحول عامل التخفيف 1,000 إلى قوة للعدد 10 ونضيف الأس.",
        [f"بما أن {m('1,000 = 10^3')}، فإن خفض التركيز ألف مرة يرفع pH بمقدار {m('3')} وحدات.",
         f"القيمة الجديدة = {m('1 + 3 = 4')}."],
        f"التحقق: الفرق بين 4 و 1 يعطي نسبة {m('10^3 = 1,000')}.",
        diagram_en=svg_ph_scale(1, "HCl", "Initial pH 1"),
        diagram_ar=_ar_svg(svg_ph_scale(1, "HCl", "Initial pH 1"),
                           {"Initial pH 1": "البداية pH 1"}),
    ))
    return qs



def _gen_sci_b13(start_idx: int) -> list[dict]:
    """G9-SCI-B13: Kinematics, acceleration a=(vf-vi)/t, d-t & v-t slopes/area (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = svg_motion_graph([(0, 0), (5, 20)], y_label="Speed (m/s)", x_label="Time (s)", title="v-t Graph")
    ar_0 = _ar_svg(d_0, {"v-t Graph": "منحنى ع-ز", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B13",
        f"A car accelerates uniformly from rest to {m('20\\text{ m/s}')} in {m('5\\text{ s}')}, as shown in the speed-time graph. What is its acceleration in {m('\\text{m/s}^2')}?",
        f"تتسارع سيارة بانتظام من السكون لتصل إلى {m('20\\text{ م/ث}')} خلال {m('5\\text{ ث}')} كما في منحنى السرعة-الزمن. ما تسارعها بوحدة {m('\\text{م/ث}^2')}؟",
        4, [100, 15, 25],
        "Acceleration is the slope of a speed-time graph: change in speed divided by time.",
        "التسارع يساوي ميل منحنى السرعة-الزمن: التغير في السرعة مقسوماً على الزمن.",
        f"Apply {m('a = \\frac{v_f - v_i}{t}')}.",
        [f"Substitute {m('v_i = 0')}, {m('v_f = 20\\text{ m/s}')}, and {m('t = 5\\text{ s}')}.",
         f"Compute {m('a = \\frac{20 - 0}{5} = 4\\text{ m/s}^2')}."],
        f"Check: starting from rest, {m('4\\text{ m/s}^2 \\times 5\\text{ s} = 20\\text{ m/s}')}.",
        f"نطبق قانون التسارع {m('a = \\frac{v_f - v_i}{t}')}.",
        [f"نعوض {m('v_i = 0')} و{m('v_f = 20\\text{ م/ث}')} و{m('t = 5\\text{ ث}')}.",
         f"التسارع = {m('\\frac{20 - 0}{5} = 4\\text{ م/ث}^2')}."],
        f"التحقق: {m('4 \\times 5 = 20\\text{ م/ث}')}.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = svg_motion_graph([(0, 0), (6, 48)], y_label="Dist (m)", x_label="Time (s)", title="d-t Graph")
    ar_1 = _ar_svg(d_1, {"d-t Graph": "منحنى ف-ز", "Dist (m)": "المسافة (م)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B13",
        f"The distance-time graph shows a cyclist moving steadily from {m('0\\text{ m}')} to {m('48\\text{ m}')} in {m('6\\text{ s}')}. What is the cyclist's constant speed in {m('\\text{m/s}')}?",
        f"يوضح منحنى المسافة-الزمن حركة دراج بثبات من {m('0\\text{ م}')} إلى {m('48\\text{ م}')} خلال {m('6\\text{ ث}')}. ما سرعته الثابتة بوحدة {m('\\text{م/ث}')}؟",
        8, [6, 42, 288],
        "Speed equals the slope (rise divided by run) of a distance-time graph.",
        "السرعة تساوي ميل منحنى المسافة-الزمن (المسافة مقسومة على الزمن).",
        f"Compute slope {m('v = \\frac{\\Delta d}{\\Delta t}')}.",
        [f"Divide distance {m('48\\text{ m}')} by time {m('6\\text{ s}')}.",
         f"Speed = {m('\\frac{48}{6} = 8\\text{ m/s}')}."],
        f"Check: {m('8\\text{ m/s} \\times 6\\text{ s} = 48\\text{ m}')}.",
        f"نحسب الميل {m('v = \\frac{\\Delta d}{\\Delta t}')}.",
        [f"نقسم المسافة {m('48\\text{ م}')} على الزمن {m('6\\text{ ث}')}.",
         f"السرعة = {m('\\frac{48}{6} = 8\\text{ م/ث}')}."],
        f"التحقق: {m('8 \\times 6 = 48\\text{ م}')}.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    d_2 = svg_motion_graph([(0, 15), (3, 15), (6, 15)], y_label="Dist (m)", x_label="Time (s)", title="Flat d-t Graph")
    ar_2 = _ar_svg(d_2, {"Flat d-t Graph": "منحنى ف-ز أفقي", "Dist (m)": "المسافة (م)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B13",
        "A horizontal line at 15 m appears on a distance-time graph from t = 0 s to t = 6 s. What does this indicate about the object's motion?",
        "يظهر خط أفقي عند المسافة 15 م على منحنى المسافة-الزمن من ز = 0 ث إلى ز = 6 ث. علامَ يدل ذلك بالنسبة لحركة الجسم؟",
        [
            ("The object is stationary (at rest) with zero speed", "الجسم ساكن لا يتحرك وسرعته تساوي صفراً"),
            ("The object is moving at a constant speed of 15 m/s", "الجسم يتحرك بسرعة ثابتة مقدارها 15 م/ث"),
            ("The object has a uniform positive acceleration", "الجسم يتحرك بتسارع موجب منتظم"),
            ("The object is returning toward the origin", "الجسم يعود باتجاه نقطة الأصل"),
        ],
        "Check whether the position coordinate changes as time advances.",
        "تحقق مما إذا كانت قيمة المسافة تتغير مع مرور الزمن أم تبقى ثابتة.",
        "Slope on a distance-time graph gives speed.",
        ["From 0 s to 6 s, distance remains fixed at 15 m, so Δd = 0.",
         "Therefore speed = 0 / 6 = 0 m/s, meaning the object is stationary."],
        "A flat d-t line means no change in position over time.",
        "ميل منحنى المسافة-الزمن يمثل السرعة.",
        ["من 0 ث إلى 6 ث بقيت المسافة ثابتة عند 15 م أي أن التغير في المسافة صفر.",
         "إذن السرعة تساوي صفراً، مما يعني أن الجسم ساكن."],
        "الخط الأفقي في منحنى المسافة-الزمن يدل دائماً على السكون.",
        diagram_en=d_2, diagram_ar=ar_2,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B13",
        f"Starting from rest, a sprinter maintains a constant acceleration of {m('3\\text{ m/s}^2')} for {m('6\\text{ s}')}. What final speed in {m('\\text{m/s}')} does the sprinter reach?",
        f"ينطلق عدّاء من السكون بتسارع ثابت مقداره {m('3\\text{ م/ث}^2')} لمدة {m('6\\text{ ث}')}. ما السرعة النهائية التي يصل إليها بوحدة {m('\\text{م/ث}')}؟",
        18, [2, 9, 54],
        "Multiply acceleration by elapsed time when initial speed is zero.",
        "اضرب التسارع في الزمن عندما تكون السرعة الابتدائية صفراً.",
        f"Rearrange {m('a = \\frac{v_f - v_i}{t}')} to {m('v_f = v_i + at')}.",
        [f"With {m('v_i = 0')}, substitute {m('a = 3\\text{ m/s}^2')} and {m('t = 6\\text{ s}')}.",
         f"Calculate {m('v_f = 0 + 3 \\times 6 = 18\\text{ m/s}')}."],
        f"Check: {m('\\frac{18 - 0}{6} = 3\\text{ m/s}^2')}.",
        f"نعيد ترتيب العلاقة إلى {m('v_f = v_i + at')}.",
        [f"بما أن {m('v_i = 0')} نعوض {m('a = 3')} و{m('t = 6')}.",
         f"السرعة النهائية = {m('3 \\times 6 = 18\\text{ م/ث}')}."],
        f"التحقق: {m('\\frac{18}{6} = 3\\text{ م/ث}^2')}.",
    ))

    d_4 = svg_motion_graph([(0, 12), (5, 12)], y_label="Speed (m/s)", x_label="Time (s)", title="Flat v-t Graph")
    ar_4 = _ar_svg(d_4, {"Flat v-t Graph": "منحنى ع-ز أفقي", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B13",
        "The velocity-time graph shows a horizontal line at 12 m/s for 5 s. Which statement correctly describes the motion?",
        "يوضح منحنى السرعة-الزمن خطاً أفقياً عند 12 م/ث لمدة 5 ث. أي عبارة تصف الحركة وصفاً صحيحاً؟",
        [
            ("Constant velocity of 12 m/s with zero acceleration", "سرعة ثابتة مقدارها 12 م/ث وتسارع يساوي صفراً"),
            ("The object is stationary throughout the 5 s", "الجسم ساكن طوال الثواني الخمس"),
            ("Uniform positive acceleration of 12 m/s²", "تسارع موجب منتظم مقداره 12 م/ث²"),
            ("Uniform deceleration toward a full stop", "تباطؤ منتظم حتى التوقف التام"),
        ],
        "Read the vertical axis label carefully: this is a velocity-time graph, not distance-time.",
        "اقرأ اسم المحور الرأسي بدقة: هذا منحنى السرعة-الزمن وليس المسافة-الزمن.",
        "Slope of a v-t graph equals acceleration.",
        ["The velocity stays fixed at 12 m/s, so Δv = 0 m/s.",
         "Since a = Δv / t = 0, the object moves steadily with zero acceleration."],
        "A horizontal v-t line means constant nonzero velocity (not rest).",
        "ميل منحنى السرعة-الزمن يساوي التسارع.",
        ["تبقى السرعة ثابتة عند 12 م/ث، أي أن التغير في السرعة يساوي صفراً.",
         "وبما أن التسارع = صفر، يتحرك الجسم بسرعة ثابتة دون تسارع."],
        "الخط الأفقي فوق الصفر في منحنى ع-ز يدل على سرعة ثابتة لا على السكون.",
        diagram_en=d_4, diagram_ar=ar_4,
    ))

    # --- MEDIUM (5..9) ---
    d_5 = svg_motion_graph([(0, 28), (6, 4)], y_label="Speed (m/s)", x_label="Time (s)", title="Braking v-t")
    ar_5 = _ar_svg(d_5, {"Braking v-t": "تباطؤ ع-ز", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B13",
        f"A driver applies the brakes, slowing smoothly from {m('28\\text{ m/s}')} to {m('4\\text{ m/s}')} in {m('6\\text{ s}')}. What is the car's acceleration in {m('\\text{m/s}^2')}?",
        f"ضغط سائق على المكابح فتناقصت سرعة السيارة بانتظام من {m('28\\text{ م/ث}')} إلى {m('4\\text{ م/ث}')} خلال {m('6\\text{ ث}')}. ما تسارع السيارة بوحدة {m('\\text{م/ث}^2')}؟",
        -4, [4, -6, -24],
        "Subtract initial velocity from final velocity: v_f - v_i gives the sign of acceleration.",
        "اطرح السرعة الابتدائية من النهائية (v_f - v_i) لتحديد إشارة التسارع.",
        f"Use {m('a = \\frac{v_f - v_i}{t}')}.",
        [f"Substitute {m('v_f = 4\\text{ m/s}')}, {m('v_i = 28\\text{ m/s}')}, and {m('t = 6\\text{ s}')}.",
         f"Compute {m('a = \\frac{4 - 28}{6} = \\frac{-24}{6} = -4\\text{ m/s}^2')}."],
        "Check: slowing down corresponds to negative acceleration along the direction of motion.",
        f"نطبق {m('a = \\frac{v_f - v_i}{t}')}.",
        [f"نعوض {m('v_f = 4')} و{m('v_i = 28')} و{m('t = 6')}.",
         f"التسارع = {m('\\frac{4 - 28}{6} = -4\\text{ م/ث}^2')}."],
        "التحقق: التباطؤ يعني تسارعاً سالباً بعكس اتجاه الحركة.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    d_6 = svg_motion_graph([(0, 0), (5, 16)], y_label="Speed (m/s)", x_label="Time (s)", title="v-t Triangle")
    ar_6 = _ar_svg(d_6, {"v-t Triangle": "مثلث ع-ز", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B13",
        f"An object speeds up uniformly from rest to {m('16\\text{ m/s}')} over {m('5\\text{ s}')}, forming the triangle under the velocity-time graph. How far in {m('\\text{m}')} does it travel?",
        f"يتسارع جسم بانتظام من السكون إلى {m('16\\text{ م/ث}')} خلال {m('5\\text{ ث}')} كما يظهر في منحنى السرعة-الزمن. ما المسافة المقطوعة بالمتر؟",
        40, [80, 32, 21],
        "Distance traveled equals the area under the velocity-time graph.",
        "المسافة المقطوعة تساوي المساحة تحت منحنى السرعة-الزمن.",
        f"Compute the area of the right triangle: {m('d = \\frac{1}{2} \\times \\text{base} \\times \\text{height}')}.",
        [f"Base = {m('5\\text{ s}')} and height = {m('16\\text{ m/s}')}.",
         f"Compute {m('d = \\frac{1}{2} \\times 5 \\times 16 = 40\\text{ m}')}."],
        f"Check: average velocity is {m('8\\text{ m/s}')}, and {m('8 \\times 5 = 40\\text{ m}')}.",
        f"نحسب مساحة المثلث تحت المنحنى: {m('d = \\frac{1}{2} \\times \\text{القاعدة} \\times \\text{الارتفاع}')}.",
        [f"القاعدة = {m('5\\text{ ث}')} والارتفاع = {m('16\\text{ م/ث}')}.",
         f"المسافة = {m('\\frac{1}{2} \\times 5 \\times 16 = 40\\text{ م}')}."],
        f"التحقق: متوسط السرعة {m('8\\text{ م/ث}')}، و{m('8 \\times 5 = 40\\text{ م}')}.",
        diagram_en=d_6, diagram_ar=ar_6,
    ))

    d_7 = svg_motion_graph([(0, 0), (4, 10), (10, 10)], y_label="Speed (m/s)", x_label="Time (s)", title="Two-Stage v-t")
    ar_7 = _ar_svg(d_7, {"Two-Stage v-t": "حركة بمرحلتين", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B13",
        f"A train accelerates from {m('0')} to {m('10\\text{ m/s}')} in {m('4\\text{ s}')}, then cruises at {m('10\\text{ m/s}')} for the next {m('6\\text{ s}')}. What total distance in {m('\\text{m}')} does it cover in {m('10\\text{ s}')}?",
        f"يتسارع قطار من السكون إلى {m('10\\text{ م/ث}')} خلال {m('4\\text{ ث}')}، ثم يسير بسرعة ثابتة {m('10\\text{ م/ث}')} لمدة {m('6\\text{ ث}')}. ما المسافة الكلية المقطوعة خلال {m('10\\text{ ث}')} بالمتر؟",
        80, [100, 70, 50],
        "Split the area under the v-t graph into a triangle (0 to 4 s) plus a rectangle (4 to 10 s).",
        "اقسم المساحة تحت المنحنى إلى مثلث (من 0 إلى 4 ث) ومستطيل (من 4 إلى 10 ث).",
        "Total distance equals the sum of areas in both stages.",
        [f"Triangle area ({m('0')} to {m('4\\text{ s}')}): {m('\\frac{1}{2} \\times 4 \\times 10 = 20\\text{ m}')}.",
         f"Rectangle area ({m('4')} to {m('10\\text{ s}')}): {m('6 \\times 10 = 60\\text{ m}')}.",
         f"Total distance = {m('20 + 60 = 80\\text{ m}')}."],
        f"Check: trapezoid formula {m('\\frac{10 + 6}{2} \\times 10 = 80\\text{ m}')}.",
        "المسافة الكلية تساوي مجموع مساحتي المرحلتين.",
        [f"مساحة المثلث (0 إلى 4 ث) = {m('\\frac{1}{2} \\times 4 \\times 10 = 20\\text{ م}')}.",
         f"مساحة المستطيل (4 إلى 10 ث) = {m('6 \\times 10 = 60\\text{ م}')}.",
         f"المجموع = {m('20 + 60 = 80\\text{ م}')}."],
        f"التحقق بصيغة شبه المنحرف: {m('\\frac{10 + 6}{2} \\times 10 = 80\\text{ م}')}.",
        diagram_en=d_7, diagram_ar=ar_7,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B13",
        f"A motorcycle already moving at {m('6\\text{ m/s}')} accelerates at {m('4\\text{ m/s}^2')}. How many seconds does it take to reach {m('30\\text{ m/s}')}?",
        f"تتحرك دراجة نارية بسرعة {m('6\\text{ م/ث}')} وتتسارع بمعدل {m('4\\text{ م/ث}^2')}. كم ثانية تحتاج للوصول إلى سرعة {m('30\\text{ م/ث}')}؟",
        6, [7.5, 9, 4],
        "First find the speed increase Δv = 30 - 6, then divide by acceleration.",
        "أوجد مقدار الزيادة في السرعة (30 - 6) أولاً ثم اقسم على التسارع.",
        f"Solve {m('t = \\frac{v_f - v_i}{a}')}.",
        [f"Velocity change: {m('30 - 6 = 24\\text{ m/s}')}.",
         f"Time = {m('\\frac{24}{4} = 6\\text{ s}')}."],
        f"Check: {m('6 + 4 \\times 6 = 30\\text{ m/s}')}.",
        f"نحسب الزمن من العلاقة {m('t = \\frac{v_f - v_i}{a}')}.",
        [f"الزيادة في السرعة = {m('30 - 6 = 24\\text{ م/ث}')}.",
         f"الزمن = {m('\\frac{24}{4} = 6\\text{ ث}')}."],
        f"التحقق: {m('6 + 4 \\times 6 = 30\\text{ م/ث}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B13",
        f"On the same distance-time axes, Runner A travels {m('24\\text{ m}')} in {m('4\\text{ s}')} while Runner B travels {m('16\\text{ m}')} in {m('4\\text{ s}')}. How much greater is Runner A's speed than Runner B's in {m('\\text{m/s}')}?",
        f"على نفس محاور المسافة-الزمن، يقطع المتسابق أ مسافة {m('24\\text{ م}')} خلال {m('4\\text{ ث}')} بينما يقطع المتسابق ب {m('16\\text{ م}')} خلال {m('4\\text{ ث}')}. بكم تزيد سرعة أ عن سرعة ب بوحدة {m('\\text{م/ث}')}؟",
        2, [4, 6, 8],
        "Calculate the slope (speed) of each runner separately, then subtract.",
        "احسب ميل (سرعة) كل متسابق على حدة ثم اطرح السرعتين.",
        f"Compare {m('v_A - v_B')}.",
        [f"Runner A speed: {m('v_A = \\frac{24}{4} = 6\\text{ m/s}')}; Runner B speed: {m('v_B = \\frac{16}{4} = 4\\text{ m/s}')}.",
         f"Difference = {m('6 - 4 = 2\\text{ m/s}')}."],
        f"Check: {m('\\frac{24 - 16}{4} = 2\\text{ m/s}')}.",
        f"نقارن بين السرعتين بحساب {m('v_A - v_B')}.",
        [f"سرعة أ = {m('\\frac{24}{4} = 6\\text{ م/ث}')}، وسرعة ب = {m('\\frac{16}{4} = 4\\text{ م/ث}')}.",
         f"الفرق = {m('6 - 4 = 2\\text{ م/ث}')}."],
        f"التحقق: {m('\\frac{24 - 16}{4} = 2\\text{ م/ث}')}.",
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B13",
        f"A delivery van drives {m('120\\text{ km}')} to a warehouse at {m('60\\text{ km/h}')} and returns along the same {m('120\\text{ km}')} route at {m('40\\text{ km/h}')}. What is the van's average speed in {m('\\text{km/h}')} for the entire round trip?",
        f"تقطع شاحنة توصيل مسافة {m('120\\text{ كم}')} ذهاباً بسرعة {m('60\\text{ كم/س}')}، وتعود في نفس الطريق ({m('120\\text{ كم}')}) بسرعة {m('40\\text{ كم/س}')}. ما متوسط السرعة للرحلة كاملة بوحدة {m('\\text{كم/س}')}؟",
        48, [50, 45, 52],
        "Average speed is total distance divided by total time — NOT the arithmetic mean of the two speeds.",
        "متوسط السرعة يساوي المسافة الكلية مقسومة على الزمن الكلي، وليس المتوسط الحسابي للسرعتين.",
        f"Use {m('v_{\\text{avg}} = \\frac{d_{\\text{total}}}{t_{\\text{total}}}')}.",
        [f"Outbound time = {m('\\frac{120}{60} = 2\\text{ h}')}; return time = {m('\\frac{120}{40} = 3\\text{ h}')}.",
         f"Total distance = {m('240\\text{ km}')}, total time = {m('5\\text{ h}')}.",
         f"Average speed = {m('\\frac{240}{5} = 48\\text{ km/h}')}."],
        "Check: because the van spends more time moving at the slower speed, average speed must be below 50 km/h.",
        f"نستخدم العلاقة {m('v_{\\text{avg}} = \\frac{d_{\\text{total}}}{t_{\\text{total}}}')}.",
        [f"زمن الذهاب = {m('\\frac{120}{60} = 2\\text{ ساعة}')}، وزمن العودة = {m('\\frac{120}{40} = 3\\text{ ساعات}')}.",
         f"المسافة الكلية = {m('240\\text{ كم}')} والزمن الكلي = {m('5\\text{ ساعات}')}.",
         f"متوسط السرعة = {m('\\frac{240}{5} = 48\\text{ كم/س}')}."],
        "التحقق: تقضي الشاحنة وقتاً أطول بالسرعة الأبطأ لذا يكون المتوسط أقل من 50 كم/س.",
    ))

    d_11 = svg_motion_graph([(0, 20), (0.5, 20), (4.5, 0)], y_label="Speed (m/s)", x_label="Time (s)", title="Stop v-t Graph")
    ar_11 = _ar_svg(d_11, {"Stop v-t Graph": "منحنى التوقف", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B13",
        f"Traveling at {m('20\\text{ m/s}')}, a driver takes {m('0.5\\text{ s}')} to react before braking uniformly to rest over the next {m('4.0\\text{ s}')} (total {m('4.5\\text{ s}')}). What total stopping distance in {m('\\text{m}')} is covered?",
        f"يسير سائق بسرعة {m('20\\text{ م/ث}')} ويستغرق {m('0.5\\text{ ث}')} كزمن استجابة قبل الضغط على المكابح ليتوقف بانتظام خلال {m('4.0\\text{ ث}')} تالية. ما مسافة التوقف الكلية بالمتر؟",
        50, [40, 45, 90],
        "Add the constant-speed reaction distance (rectangle) and the braking distance (triangle).",
        "اجمع مسافة الاستجابة (مستطيل) مع مسافة الفرملة (مثلث).",
        "Compute reaction distance + braking distance under the v-t graph.",
        [f"Reaction distance ({m('0.5\\text{ s}')} at {m('20\\text{ m/s}')}): {m('20 \\times 0.5 = 10\\text{ m}')}.",
         f"Braking distance ({m('4.0\\text{ s}')} triangle): {m('\\frac{1}{2} \\times 4.0 \\times 20 = 40\\text{ m}')}.",
         f"Total stopping distance = {m('10 + 40 = 50\\text{ m}')}."],
        f"Check: trapezoid area = {m('\\frac{0.5 + 4.5}{2} \\times 20 = 50\\text{ m}')}.",
        "مسافة التوقف تساوي مجموع مساحتي مرحلتي الاستجابة والفرملة.",
        [f"مسافة الاستجابة = {m('20 \\times 0.5 = 10\\text{ م}')}.",
         f"مسافة الفرملة = {m('\\frac{1}{2} \\times 4.0 \\times 20 = 40\\text{ م}')}.",
         f"المسافة الكلية = {m('10 + 40 = 50\\text{ م}')}."],
        f"التحقق بمساحة شبه المنحرف: {m('\\frac{0.5 + 4.5}{2} \\times 20 = 50\\text{ م}')}.",
        diagram_en=d_11, diagram_ar=ar_11,
    ))

    d_12 = svg_motion_graph([(0, 8), (2, 8), (6, 24)], y_label="Speed (m/s)", x_label="Time (s)", title="Piecewise v-t")
    ar_12 = _ar_svg(d_12, {"Piecewise v-t": "منحنى متعدد المراحل", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B13",
        f"A boat cruises at {m('8\\text{ m/s}')} from {m('t = 0')} to {m('t = 2\\text{ s}')}, then speeds up linearly to {m('24\\text{ m/s}')} at {m('t = 6\\text{ s}')}. What is its acceleration in {m('\\text{m/s}^2')} strictly during the interval {m('2\\text{ s}')} to {m('6\\text{ s}')}?",
        f"يتحرك قارب بسرعة {m('8\\text{ م/ث}')} من {m('t = 0')} إلى {m('t = 2\\text{ ث}')}، ثم يتسارع خطياً إلى {m('24\\text{ م/ث}')} عند {m('t = 6\\text{ ث}')}. ما تسارعه بوحدة {m('\\text{م/ث}^2')} خلال الفترة من {m('2\\text{ ث}')} إلى {m('6\\text{ ث}')} فقط؟",
        4, [2.67, 6, 16],
        "Use Δt = 6 - 2 = 4 s for that specific segment, not total elapsed time 6 s.",
        "استخدم الفترة الزمنية لهذه المرحلة فقط Δt = 6 - 2 = 4 ث، وليس الزمن الكلي 6 ث.",
        "Evaluate slope of the second line segment only.",
        [f"Speed change: {m('24 - 8 = 16\\text{ m/s}')}; time span: {m('6 - 2 = 4\\text{ s}')}.",
         f"Acceleration = {m('\\frac{16}{4} = 4\\text{ m/s}^2')}."],
        f"Check: {m('8 + 4 \\times 4 = 24\\text{ m/s}')}.",
        "نحسب ميل القطعة الثانية فقط من المنحنى.",
        [f"التغير في السرعة = {m('24 - 8 = 16\\text{ م/ث}')} خلال {m('6 - 2 = 4\\text{ ث}')}.",
         f"التسارع = {m('\\frac{16}{4} = 4\\text{ م/ث}^2')}."],
        f"التحقق: {m('8 + 4 \\times 4 = 24\\text{ م/ث}')}.",
        diagram_en=d_12, diagram_ar=ar_12,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B13",
        "A ball is thrown straight upward and reaches its highest point. Which combination correctly describes its instantaneous velocity and acceleration at that exact peak?",
        "قُذفت كرة رأسياً إلى أعلى ووصلت إلى أقصى ارتفاع لها. أي خيار يصف سرعتها اللحظية وتسارعها عند تلك اللحظة وصفاً صحيحاً؟",
        [
            ("Velocity is 0 m/s; acceleration is 9.8 m/s² downward", "السرعة تساوي صفراً والتسارع 9.8 م/ث² نحو الأسفل"),
            ("Both velocity and acceleration are 0 m/s²", "السرعة والتسارع كلاهما يساوي صفراً"),
            ("Velocity is 9.8 m/s upward; acceleration is 0 m/s²", "السرعة 9.8 م/ث للأعلى والتسارع صفر"),
            ("Velocity is 0 m/s; acceleration reverses to point upward", "السرعة صفر وينعكس اتجاه التسارع للأعلى"),
        ],
        "Gravity acts continuously on the ball throughout flight, even when it momentarily pauses to reverse direction.",
        "تؤثر الجاذبية الأرضية باستمرار على الكرة طوال التحليق حتى في لحظة توقفها اللحظي.",
        "Separate instantaneous velocity v from rate of change of velocity a.",
        ["At the peak, upward motion stops before falling, so instantaneous velocity v = 0 m/s.",
         "Because gravity still pulls downward without pause, acceleration remains g = 9.8 m/s² downward."],
        "If acceleration were zero at the peak, the ball would float stationary in midair.",
        "افصل بين السرعة اللحظية ومعدل تغير السرعة (التسارع).",
        ["عند القمة تتوقف الكرة لحظياً قبل الهبوط فتكون سرعتها اللحظية صفراً.",
         "تستمر الجاذبية بالسحب للأسفل فيبقى التسارع 9.8 م/ث² نحو الأسفل."],
        "لو انعدم التسارع عند القمة لبقيت الكرة معلقة في الهواء.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B13",
        f"At {m('t = 0')}, a cyclist passes a line at constant speed {m('16\\text{ m/s}')}. At the exact same moment and place, a police motorbike starts from rest with constant acceleration {m('4\\text{ m/s}^2')} using {m('d = \\frac{1}{2}at^2')}. After how many seconds does the motorbike catch the cyclist?",
        f"عند {m('t = 0')} يعبر دراج خط البداية بسرعة ثابتة {m('16\\text{ م/ث}')}، وفي اللحظة والمكان نفسهما تنطلق دراجة شرطة من السكون بتسارع ثابت {m('4\\text{ م/ث}^2')} وفق {m('d = \\frac{1}{2}at^2')}. بعد كم ثانية تلحق دراجة الشرطة بالدراج؟",
        8, [4, 6, 16],
        "Set the cyclist's distance (16t) equal to the motorbike's distance (0.5 × 4 × t²) for t > 0.",
        "ساوِ بين مسافة الدراج (16t) ومسافة دراجة الشرطة (0.5 × 4 × t²) لقيمة t الموجبة.",
        f"Equate {m('d_{\\text{cyclist}} = d_{\\text{bike}}')}.",
        [f"Cyclist distance: {m('16t')}; motorbike distance: {m('\\frac{1}{2}(4)t^2 = 2t^2')}.",
         f"Set {m('2t^2 = 16t')} and divide by {m('2t')} (since {m('t > 0')}) to get {m('t = 8\\text{ s}')}."],
        f"Check: at {m('8\\text{ s}')}, cyclist covers {m('16 \\times 8 = 128\\text{ m}')} and bike covers {m('2 \\times 64 = 128\\text{ m}')}.",
        f"نساوي المسافتين {m('d_{\\text{cyclist}} = d_{\\text{bike}}')}.",
        [f"مسافة الدراج = {m('16t')}، ومسافة الشرطة = {m('2t^2')}.",
         f"بحل {m('2t^2 = 16t')} للقيمة الموجبة نحصل على {m('t = 8\\text{ ث}')}."],
        f"التحقق: عند {m('8\\text{ ث}')} يقطع كل منهما {m('128\\text{ م}')}.",
    ))

    return qs


def _gen_sci_b14(start_idx: int) -> list[dict]:
    """G9-SCI-B14: Newton's Laws, F=ma, W=mg, Net Force, Friction & Tension (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B14",
        f"What net horizontal force in newtons ({m('\\text{N}')}) is needed to give a {m('5\\text{ kg}')} bowling ball an acceleration of {m('4\\text{ m/s}^2')}?",
        f"ما محصلة القوة الأفقية بالنيوتن اللازمة لإكساب كرة كتلتها {m('5\\text{ كجم}')} تسارعاً مقداره {m('4\\text{ م/ث}^2')}؟",
        20, [9, 1.25, 16],
        "Apply Newton's second law directly: F = m × a.",
        "طبق قانون نيوتن الثاني مباشرة: القوة = الكتلة × التسارع.",
        f"Use {m('F = m a')}.",
        [f"Multiply mass {m('5\\text{ kg}')} by acceleration {m('4\\text{ m/s}^2')}.",
         f"Force = {m('5 \\times 4 = 20\\text{ N}')}."],
        f"Check: {m('20\\text{ N} / 5\\text{ kg} = 4\\text{ m/s}^2')}.",
        f"نستخدم القانون {m('F = m a')}.",
        [f"نضرب الكتلة {m('5\\text{ كجم}')} في التسارع {m('4\\text{ م/ث}^2')}.",
         f"القوة = {m('5 \\times 4 = 20\\text{ نيوتن}')}."],
        f"التحقق: {m('20 / 5 = 4\\text{ م/ث}^2')}.",
    ))

    d_1 = svg_force_block(7, 18, mass_kg=4)
    ar_1 = _ar_svg(d_1, {"Force Diagram": "مخطط القوى", "7 N": "7 نيوتن", "18 N": "18 نيوتن", "4 kg": "4 كجم"})
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B14",
        f"Two horizontal forces act on a {m('4\\text{ kg}')} block as shown: {m('18\\text{ N}')} to the right and {m('7\\text{ N}')} to the left. What is the magnitude of the net force in {m('\\text{N}')}?",
        f"تؤثر قوتان أفقيتان في جسم كتلته {m('4\\text{ كجم}')} كما في الشكل: {m('18\\text{ نيوتن}')} يميناً و{m('7\\text{ نيوتن}')} يساراً. ما مقدار القوة المحصلة بالنيوتن؟",
        11, [25, 4, 2.75],
        "Forces pointing in opposite directions subtract to give net force.",
        "القوى المتعاكسة في الاتجاه تُطرح لإيجاد القوة المحصلة.",
        f"Subtract the leftward force from the rightward force.",
        [f"Net force = {m('18\\text{ N} - 7\\text{ N} = 11\\text{ N}')} to the right."],
        "Check: opposite horizontal forces partially cancel each other.",
        "نطرح القوة المتجهة يساراً من القوة المتجهة يميناً.",
        [f"القوة المحصلة = {m('18 - 7 = 11\\text{ نيوتن}')} نحو اليمين."],
        "التحقق: القوتان المتعاكستان تُلغي إحداهما جزءاً من الأخرى.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B14",
        f"Using Earth's gravitational acceleration {m('g = 9.8\\text{ m/s}^2')}, what is the weight in {m('\\text{N}')} of a {m('10\\text{ kg}')} steel block?",
        f"باستخدام تسارع الجاذبية الأرضية {m('g = 9.8\\text{ م/ث}^2')}، ما وزن كتلة فولاذية مقدارها {m('10\\text{ كجم}')} بوحدة النيوتن؟",
        98, [10, 9.8, 19.8],
        "Weight is gravitational force: W = m × g.",
        "الوزن هو قوة الجاذبية: الوزن = الكتلة × تسارع الجاذبية.",
        f"Calculate {m('W = mg')}.",
        [f"Substitute {m('m = 10\\text{ kg}')} and {m('g = 9.8\\text{ m/s}^2')}.",
         f"Weight = {m('10 \\times 9.8 = 98\\text{ N}')}."],
        f"Check: roughly {m('100\\text{ N}')} since {m('g \\approx 10\\text{ m/s}^2')}.",
        f"نطبق العلاقة {m('W = mg')}.",
        [f"نعوض {m('m = 10\\text{ كجم}')} و{m('g = 9.8\\text{ م/ث}^2')}.",
         f"الوزن = {m('10 \\times 9.8 = 98\\text{ نيوتن}')}."],
        f"التحقق: قريب من 100 نيوتن لأن g قريبة من 10.",
    ))

    d_3 = svg_force_block(15, 15, mass_kg=3, title="Balanced Forces")
    ar_3 = _ar_svg(d_3, {"Balanced Forces": "قوى متزنة", "15 N": "15 نيوتن", "3 kg": "3 كجم"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B14",
        "A 3 kg sled is sliding right at 4 m/s across ice when equal 15 N forces act left and right simultaneously. What happens to the sled's motion?",
        "ينزلق زلاج كتلته 3 كجم يميناً بسرعة 4 م/ث على الجليد عندما تؤثر فيه قوتان متساويتان 15 نيوتن يميناً و15 نيوتن يساراً. ماذا يحدث لحركة الزلاج؟",
        [
            ("It continues sliding right at a constant speed of 4 m/s", "يستمر بالانزلاق يميناً بسرعة ثابتة مقدارها 4 م/ث"),
            ("It stops immediately because the net force is zero", "يتوقف فوراً لأن القوة المحصلة تساوي صفراً"),
            ("It accelerates to the right at 5 m/s²", "يتسارع نحو اليمين بمقدار 5 م/ث²"),
            ("It slows down uniformly until stopping", "يتباطأ بانتظام حتى يتوقف"),
        ],
        "Remember Newton's first law: zero net force preserves current velocity rather than forcing speed to zero.",
        "تذكر قانون نيوتن الأول: انعدام المحصلة يحافظ على السرعة الحالية ولا يوقف الجسم المتحرك.",
        "Compute net force first, then apply Newton's 1st law.",
        ["Net force = 15 N - 15 N = 0 N.",
         "With zero net force, acceleration is 0, so the sled maintains 4 m/s to the right."],
        "Balanced forces mean zero change in motion, not zero motion.",
        "نحسب المحصلة أولاً ثم نطبق قانون نيوتن الأول.",
        ["المحصلة = 15 - 15 = 0 نيوتن.",
         "انعدام المحصلة يعني انعدام التسارع، فيستمر الزلاج بسرعة 4 م/ث يميناً."],
        "القوى المتزنة تعني انعدام تغير الحركة لا انعدام الحركة نفسها.",
        diagram_en=d_3, diagram_ar=ar_3,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B14",
        f"A net force of {m('36\\text{ N}')} produces an acceleration of {m('6\\text{ m/s}^2')} on a cart. What is the cart's mass in {m('\\text{kg}')}?",
        f"أنتجت قوة محصلة مقدارها {m('36\\text{ نيوتن}')} تسارعاً قدره {m('6\\text{ م/ث}^2')} في عربة. ما كتلة العربة بالكيلوجرام؟",
        6, [216, 30, 42],
        "Divide force by acceleration to isolate mass: m = F / a.",
        "اقسم القوة على التسارع لحساب الكتلة: الكتلة = القوة / التسارع.",
        f"Use {m('m = \\frac{F}{a}')}.",
        [f"Substitute {m('F = 36\\text{ N}')} and {m('a = 6\\text{ m/s}^2')}.",
         f"Mass = {m('\\frac{36}{6} = 6\\text{ kg}')}."],
        f"Check: {m('6\\text{ kg} \\times 6\\text{ m/s}^2 = 36\\text{ N}')}.",
        f"نطبق {m('m = \\frac{F}{a}')}.",
        [f"نعوض {m('F = 36')} و{m('a = 6')}.",
         f"الكتلة = {m('\\frac{36}{6} = 6\\text{ كجم}')}."],
        f"التحقق: {m('6 \\times 6 = 36\\text{ نيوتن}')}.",
    ))

    # --- MEDIUM (5..9) ---
    d_5 = svg_force_block(8, 26, mass_kg=6)
    ar_5 = _ar_svg(d_5, {"Force Diagram": "مخطط القوى", "8 N": "8 نيوتن", "26 N": "26 نيوتن", "6 kg": "6 كجم"})
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B14",
        f"A {m('6\\text{ kg}')} crate experiences {m('26\\text{ N}')} forward and {m('8\\text{ N}')} of opposing friction as illustrated. What is the crate's acceleration in {m('\\text{m/s}^2')}?",
        f"يتأثر صندوق كتلته {m('6\\text{ كجم}')} بقوة دفع {m('26\\text{ نيوتن}')} وقوة احتكاك معاكسة {m('8\\text{ نيوتن}')} كما في الشكل. ما تسارع الصندوق بوحدة {m('\\text{م/ث}^2')}؟",
        3, [4.33, 5.67, 18],
        "Find net force first (26 - 8), then divide by mass (6 kg).",
        "أوجد القوة المحصلة أولاً (26 - 8) ثم اقسم على الكتلة (6 كجم).",
        f"Apply {m('a = \\frac{F_{\\text{net}}}{m}')}.",
        [f"Net force = {m('26 - 8 = 18\\text{ N}')}.",
         f"Acceleration = {m('\\frac{18}{6} = 3\\text{ m/s}^2')}."],
        f"Check: {m('6\\text{ kg} \\times 3\\text{ m/s}^2 + 8\\text{ N} = 26\\text{ N}')}.",
        f"نطبق {m('a = \\frac{F_{\\text{net}}}{m}')}.",
        [f"القوة المحصلة = {m('26 - 8 = 18\\text{ نيوتن}')}.",
         f"التسارع = {m('\\frac{18}{6} = 3\\text{ م/ث}^2')}."],
        f"التحقق: {m('6 \\times 3 + 8 = 26\\text{ نيوتن}')}.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B14",
        f"A worker pushes a {m('5\\text{ kg}')} box with a horizontal force of {m('32\\text{ N}')}, and the box accelerates at {m('4\\text{ m/s}^2')}. What is the magnitude of the opposing friction force in {m('\\text{N}')}?",
        f"يدفع عامل صندوقاً كتلته {m('5\\text{ كجم}')} بقوة أفقية {m('32\\text{ نيوتن}')} فيتسارع الصندوق بمعدل {m('4\\text{ م/ث}^2')}. ما مقدار قوة الاحتكاك المعاكسة بالنيوتن؟",
        12, [20, 52, 8],
        "Calculate F_net = m × a first; friction is the difference between applied force and F_net.",
        "احسب المحصلة أولاً (m × a)؛ والاحتكاك هو الفرق بين القوة المؤثرة والمحصلة.",
        f"Solve {m('F_{\\text{applied}} - f = ma')}.",
        [f"Net force required: {m('F_{\\text{net}} = 5 \\times 4 = 20\\text{ N}')}.",
         f"Friction force: {m('f = 32 - 20 = 12\\text{ N}')}."],
        f"Check: {m('(32 - 12) / 5 = 4\\text{ m/s}^2')}.",
        f"نحل المعادلة {m('F_{\\text{applied}} - f = ma')}.",
        [f"القوة المحصلة اللازمة = {m('5 \\times 4 = 20\\text{ نيوتن}')}.",
         f"قوة الاحتكاك = {m('32 - 20 = 12\\text{ نيوتن}')}."],
        f"التحقق: {m('(32 - 12) / 5 = 4\\text{ م/ث}^2')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B14",
        "An astronaut's toolkit has a mass of 15 kg on Earth. If taken to the Moon (where g = 1.6 m/s²), what are its mass and weight on the Moon?",
        "تبلغ كتلة صندوق أدوات رائد فضاء 15 كجم على الأرض. إذا نُقل إلى القمر حيث تسارع الجاذبية 1.6 م/ث²، فما كتلته ووزنه على سطح القمر؟",
        [
            ("Mass = 15 kg; Weight = 24 N", "الكتلة = 15 كجم؛ الوزن = 24 نيوتن"),
            ("Mass = 2.4 kg; Weight = 24 N", "الكتلة = 2.4 كجم؛ الوزن = 24 نيوتن"),
            ("Mass = 15 kg; Weight = 150 N", "الكتلة = 15 كجم؛ الوزن = 150 نيوتن"),
            ("Mass = 9.4 kg; Weight = 15 N", "الكتلة = 9.4 كجم؛ الوزن = 15 نيوتن"),
        ],
        "Mass measures amount of matter and never changes with location; weight changes with local g.",
        "الكتلة كمية المادة في الجسم ولا تتغير بتغير المكان، أما الوزن فيعتمد على الجاذبية.",
        "Keep mass invariant and recompute W = m × g_Moon.",
        ["Mass remains 15 kg everywhere in the universe.",
         "Moon weight: W = 15 kg × 1.6 m/s² = 24 N."],
        "Notice 24 N is roughly one-sixth of Earth weight (~147 N).",
        "تبقى الكتلة ثابتة ونحسب الوزن بجاذبية القمر.",
        ["الكتلة لا تتغير وتبقى 15 كجم.",
         "الوزن على القمر = 15 × 1.6 = 24 نيوتن."],
        "الوزن على القمر يعادل تقريباً سدس الوزن على الأرض.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B14",
        f"A {m('60\\text{ kg}')} ice skater pushes a {m('30\\text{ kg}')} child forward with a force of {m('90\\text{ N}')}. By Newton's third law, what force magnitude in {m('\\text{N}')} pushes backward on the skater?",
        f"يدفع متزلج كتلته {m('60\\text{ كجم}')} طفلاً كتلته {m('30\\text{ كجم}')} للأمام بقوة {m('90\\text{ نيوتن}')}. حسب قانون نيوتن الثالث، ما مقدار القوة المرتدة على المتزلج بالنيوتن؟",
        90, [45, 180, 30],
        "Action and reaction forces are always equal in magnitude regardless of differing masses.",
        "قوتا الفعل ورد الفعل متساويتان دائماً في المقدار مهما اختلفت الكتلتان.",
        "Apply Newton's 3rd Law directly.",
        [f"The child exerts an equal and opposite {m('90\\text{ N}')} reaction force on the skater.",
         "Different masses change their accelerations, NOT the interaction force magnitude."],
        "Check: the child accelerates twice as much as the skater, yet the force on each is 90 N.",
        "نطبق قانون نيوتن الثالث مباشرة.",
        ["يؤثر الطفل بقوة رد فعل مساوية في المقدار ومعاكسة في الاتجاه قدرها 90 نيوتن.",
         "اختلاف الكتلتين يغيّر التسارع فقط ولا يغيّر مقدار القوة المتبادلة."],
        "التحقق: يتسارع الطفل بضعف تسارع المتزلج رغم تساوي القوة على كل منهما.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B14",
        f"What average braking force magnitude in {m('\\text{N}')} stops a {m('1,200\\text{ kg}')} car moving at {m('20\\text{ m/s}')} uniformly in {m('8\\text{ s}')}?",
        f"ما مقدار متوسط قوة الفرملة بالنيوتن اللازمة لإيقاف سيارة كتلتها {m('1,200\\text{ كجم}')} تسير بسرعة {m('20\\text{ م/ث}')} بانتظام خلال {m('8\\text{ ث}')}؟",
        3000, [2400, 150, 9600],
        "First find acceleration magnitude a = Δv / t, then multiply by mass.",
        "احسب مقدار التسارع أولاً (Δv / t)، ثم اضربه في الكتلة.",
        f"Combine {m('a = \\frac{\\Delta v}{t}')} with {m('F = ma')}.",
        [f"Acceleration magnitude: {m('a = \\frac{20}{8} = 2.5\\text{ m/s}^2')}.",
         f"Braking force: {m('F = 1,200 \\times 2.5 = 3,000\\text{ N}')}."],
        f"Check: impulse {m('3,000 \\times 8 = 24,000\\text{ N}\\cdot\\text{s} = 1,200 \\times 20')}.",
        f"نجمع بين {m('a = \\frac{\\Delta v}{t}')} و{m('F = ma')}.",
        [f"مقدار التباطؤ = {m('\\frac{20}{8} = 2.5\\text{ م/ث}^2')}.",
         f"قوة الفرملة = {m('1,200 \\times 2.5 = 3,000\\text{ نيوتن}')}."],
        f"التحقق: الدفع {m('3,000 \\times 8 = 24,000')} يساوي الزخم الابتدائي.",
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B14",
        f"A {m('50\\text{ kg}')} load hangs inside an elevator accelerating upward at {m('2\\text{ m/s}^2')} (use {m('g = 10\\text{ m/s}^2')}). What is the cable tension in {m('\\text{N}')} supporting the load?",
        f"يتدلى ثقل كتلته {m('50\\text{ كجم}')} داخل مصعد يتسارع إلى أعلى بمعدل {m('2\\text{ م/ث}^2')} (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما قوة الشد في الحبل بالنيوتن؟",
        600, [500, 400, 100],
        "Tension must both support weight (mg) and provide upward net force (ma).",
        "يجب أن يعادل الشد الوزن (mg) مضافاً إليه القوة المحصلة الصاعدة (ma).",
        f"Set {m('T - mg = ma \\implies T = m(g + a)')}.",
        [f"Weight {m('mg = 50 \\times 10 = 500\\text{ N}')}; upward net force {m('ma = 50 \\times 2 = 100\\text{ N}')}.",
         f"Tension = {m('500 + 100 = 600\\text{ N}')}."],
        f"Check: net upward force {m('600 - 500 = 100\\text{ N}')}, giving {m('a = 100/50 = 2\\text{ m/s}^2')}.",
        f"نطبق {m('T - mg = ma')} أي {m('T = m(g + a)')}.",
        [f"الوزن = {m('50 \\times 10 = 500\\text{ نيوتن}')} والقوة المحصلة = {m('50 \\times 2 = 100\\text{ نيوتن}')}.",
         f"الشد = {m('500 + 100 = 600\\text{ نيوتن}')}."],
        f"التحقق: المحصلة الصاعدة {m('600 - 500 = 100\\text{ نيوتن}')} تعطي تسارع {m('2\\text{ م/ث}^2')}.",
    ))

    d_11 = svg_force_block(0, 50, mass_kg=10, title="System Total 10 kg")
    ar_11 = _ar_svg(d_11, {"System Total 10 kg": "جملة الكتلتين 10 كجم", "50 N": "50 نيوتن", "10 kg": "10 كجم"})
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B14",
        f"Two blocks ({m('4\\text{ kg}')} behind {m('6\\text{ kg}')}) touch on a frictionless floor as a {m('50\\text{ N}')} force pushes the {m('4\\text{ kg}')} block forward. What contact force in {m('\\text{N}')} pushes the {m('6\\text{ kg}')} block?",
        f"يتلامس صندوقان ({m('4\\text{ كجم}')} خلف {m('6\\text{ كجم}')}) على سطح عديم الاحتكاك وتؤثر قوة {m('50\\text{ نيوتن}')} في الصندوق ذي الـ {m('4\\text{ كجم}')}. ما قوة التلامس بالنيوتن المؤثرة في صندوق الـ {m('6\\text{ كجم}')}؟",
        30, [50, 20, 25],
        "Find the system acceleration using total mass (10 kg), then multiply by the front block's mass (6 kg).",
        "احسب تسارع الجملة بالكتلة الكلية (10 كجم)، ثم اضربه في كتلة الصندوق الأمامي (6 كجم).",
        "Treat both blocks together for a, then isolate the 6 kg block.",
        [f"Total mass = {m('4 + 6 = 10\\text{ kg}')}, so {m('a = \\frac{50}{10} = 5\\text{ m/s}^2')}.",
         f"Net force on front {m('6\\text{ kg}')} block = {m('6 \\times 5 = 30\\text{ N}')}."],
        f"Check: remaining {m('50 - 30 = 20\\text{ N}')} accelerates the {m('4\\text{ kg}')} block at {m('5\\text{ m/s}^2')}.",
        "نحسب تسارع النظام أولاً ثم نعزل الصندوق الأمامي.",
        [f"الكتلة الكلية = {m('10\\text{ كجم}')}، لذا {m('a = \\frac{50}{10} = 5\\text{ م/ث}^2')}.",
         f"قوة التلامس على كتلة {m('6\\text{ كجم}')} = {m('6 \\times 5 = 30\\text{ نيوتن}')}."],
        f"التحقق: المتبقي {m('20\\text{ نيوتن}')} يسرّع كتلة {m('4\\text{ كجم}')} بنفس التسارع.",
        diagram_en=d_11, diagram_ar=ar_11,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B14",
        "If the net force acting on a trolley is doubled while its mass is simultaneously cut in half, by what factor does its acceleration increase?",
        "إذا تضاعفت القوة المحصلة المؤثرة في عربة إلى المثلين وقُسمت كتلتها إلى النصف في الوقت نفسه، فكم مرة يتضاعف تسارعها؟",
        4, [2, 1, 8],
        "Substitute 2F and m/2 into a = F / m.",
        "عوض 2F و m/2 في العلاقة a = F / m.",
        f"Compare {m('a_{\\text{new}} = \\frac{2F}{m/2}')} to {m('a_{\\text{old}} = \\frac{F}{m}')}.",
        [f"Write {m('a_{\\text{new}} = \\frac{2F}{0.5m} = 4\\left(\\frac{F}{m}\\right) = 4\\,a_{\\text{old}}')}.",
         "Acceleration increases by a factor of 4."],
        "Check: doubling force doubles acceleration, and halving mass doubles it again (2 × 2 = 4).",
        f"نقارن {m('a_{\\text{new}} = \\frac{2F}{m/2}')} بالتسارع الأصلي.",
        [f"نجد أن {m('a_{\\text{new}} = \\frac{2}{0.5} \\frac{F}{m} = 4\\,a_{\\text{old}}')}.",
         "يتضاعف التسارع 4 مرات."],
        "التحقق: مضاعفة القوة تضاعف التسارع، وتنصيف الكتلة يضاعفه مرة أخرى (2 × 2 = 4).",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B14",
        "A skydiver with weight 700 N falls until upward air drag reaches 700 N. What happens at that point?",
        "يسقط مظلي وزنه 700 نيوتن حتى تصل قوة مقاومة الهواء للأعلى إلى 700 نيوتن. ماذا يحدث عندئذ؟",
        [
            ("Acceleration drops to zero and the diver falls at constant terminal velocity", "ينعدم التسارع ويهبط المظلي بسرعة حدية ثابتة"),
            ("The diver reverses direction and rises upward", "ينعكس اتجاه حركة المظلي ويرتفع لأعلى"),
            ("The diver hovers motionless in midair", "يتوقف المظلي ساكناً في الهواء دون هبوط"),
            ("Acceleration remains 9.8 m/s² downward", "يبقى التسارع 9.8 م/ث² نحو الأسفل"),
        ],
        "When upward drag matches downward weight, net force is zero — meaning zero change in existing downward speed.",
        "عندما تتساوى مقاومة الهواء مع الوزن تصبح المحصلة صفراً، فلا تتغير السرعة الحالية للأسفل.",
        "Apply Newton's 1st law to balanced vertical forces.",
        ["Net force = 700 N downward - 700 N upward = 0 N.",
         "Because the diver is already falling rapidly, zero acceleration keeps them falling steadily at terminal velocity."],
        "Equal opposing forces stop acceleration, not motion.",
        "نطبق قانون نيوتن الأول على القوى الرأسية المتزنة.",
        ["القوة المحصلة = 700 - 700 = 0 نيوتن.",
         "نظراً لأن المظلي كان هابطاً أصلاً، يستمر بالهبوط بسرعة حدية ثابتة."],
        "تساوي القوى المتعاكسة يوقف التسارع لا الحركة نفسها.",
    ))

    d_14 = svg_motion_graph([(0, 2), (4, 14)], y_label="Speed (m/s)", x_label="Time (s)", title="3 kg Object v-t")
    ar_14 = _ar_svg(d_14, {"3 kg Object v-t": "جسم 3 كجم ع-ز", "Speed (m/s)": "السرعة (م/ث)", "Time (s)": "الزمن (ث)"})
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B14",
        f"The velocity-time graph of a {m('3\\text{ kg}')} drone rises linearly from {m('2\\text{ m/s}')} to {m('14\\text{ m/s}')} in {m('4\\text{ s}')}. What net force in {m('\\text{N}')} acts on the drone?",
        f"ترتفع سرعة طائرة مسيّرة كتلتها {m('3\\text{ كجم}')} خطياً من {m('2\\text{ م/ث}')} إلى {m('14\\text{ م/ث}')} خلال {m('4\\text{ ث}')}. ما القوة المحصلة المؤثرة فيها بالنيوتن؟",
        9, [10.5, 12, 36],
        "First find acceleration from the graph slope, then multiply by the 3 kg mass.",
        "أوجد التسارع أولاً من ميل المنحنى، ثم اضربه في الكتلة (3 كجم).",
        f"Compute {m('a = \\frac{\\Delta v}{\\Delta t}')}, then {m('F = ma')}.",
        [f"Acceleration: {m('a = \\frac{14 - 2}{4} = 3\\text{ m/s}^2')}.",
         f"Net force: {m('F = 3\\text{ kg} \\times 3\\text{ m/s}^2 = 9\\text{ N}')}."],
        f"Check: impulse {m('9 \\times 4 = 36\\text{ N}\\cdot\\text{s} = 3 \\times (14 - 2)')}.",
        f"نحسب التسارع {m('a = \\frac{\\Delta v}{\\Delta t}')} ثم {m('F = ma')}.",
        [f"التسارع = {m('\\frac{14 - 2}{4} = 3\\text{ م/ث}^2')}.",
         f"القوة المحصلة = {m('3 \\times 3 = 9\\text{ نيوتن}')}."],
        f"التحقق: التغير في الزخم = {m('3 \\times 12 = 36')} يساوي الدفع {m('9 \\times 4')}.",
        diagram_en=d_14, diagram_ar=ar_14,
    ))

    return qs


def _gen_sci_b15(start_idx: int) -> list[dict]:
    """G9-SCI-B15: Work W=Fd, Power P=W/t, KE=0.5mv^2, PE=mgh, Conservation (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = svg_force_block(0, 25, title="Push 8 m")
    ar_0 = _ar_svg(d_0, {"Push 8 m": "دفع 8 م", "25 N": "25 نيوتن"})
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B15",
        f"A student pushes a trolley with a steady horizontal force of {m('25\\text{ N}')} over a distance of {m('8\\text{ m}')} in the direction of the force. How many joules ({m('\\text{J}')}) of work are done?",
        f"يدفع طالب عربة بقوة أفقية ثابتة مقدارها {m('25\\text{ نيوتن}')} لمسافة {m('8\\text{ م}')} في اتجاه القوة نفسه. ما الشغل المبذول بالجول؟",
        200, [33, 17, 3.125],
        "Work equals force multiplied by displacement along the force direction: W = F × d.",
        "الشغل يساوي حاصل ضرب القوة في الإزاحة باتجاهها: W = F × d.",
        f"Apply {m('W = Fd')}.",
        [f"Substitute {m('F = 25\\text{ N}')} and {m('d = 8\\text{ m}')}.",
         f"Work = {m('25 \\times 8 = 200\\text{ J}')}."],
        f"Check: {m('200\\text{ J} / 8\\text{ m} = 25\\text{ N}')}.",
        f"نطبق {m('W = Fd')}.",
        [f"نعوض {m('F = 25')} و{m('d = 8')}.",
         f"الشغل = {m('25 \\times 8 = 200\\text{ جول}')}."],
        f"التحقق: {m('200 / 8 = 25\\text{ نيوتن}')}.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B15",
        f"A small hoist performs {m('600\\text{ J}')} of work lifting supplies in {m('12\\text{ s}')}. What is its mechanical power output in watts ({m('\\text{W}')})?",
        f"تنجز رافعة صغيرة شغلاً مقداره {m('600\\text{ جول}')} في رفع مواد خلال {m('12\\text{ ث}')}. ما قدرتها الميكانيكية بالواط؟",
        50, [7200, 612, 120],
        "Power is work divided by time: P = W / t.",
        "القدرة هي الشغل مقسوماً على الزمن: P = W / t.",
        f"Compute {m('P = \\frac{W}{t}')}.",
        [f"Divide {m('600\\text{ J}')} by {m('12\\text{ s}')}.",
         f"Power = {m('\\frac{600}{12} = 50\\text{ W}')}."],
        f"Check: {m('50\\text{ W} \\times 12\\text{ s} = 600\\text{ J}')}.",
        f"نحسب القدرة {m('P = \\frac{W}{t}')}.",
        [f"نقسم {m('600\\text{ جول}')} على {m('12\\text{ ث}')}.",
         f"القدرة = {m('\\frac{600}{12} = 50\\text{ واط}')}."],
        f"التحقق: {m('50 \\times 12 = 600\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B15",
        f"A {m('4\\text{ kg}')} bowling ball rolls at {m('5\\text{ m/s}')}. What is its kinetic energy in {m('\\text{J}')}?",
        f"تتدحرج كرة كتلتها {m('4\\text{ كجم}')} بسرعة {m('5\\text{ م/ث}')}. ما طاقتها الحركية بالجول؟",
        50, [100, 20, 10],
        "Remember the half factor and the square on speed: KE = 0.5 × m × v².",
        "تذكر معامل النصف وتربيع السرعة: KE = 0.5 × m × v².",
        f"Use {m('KE = \\frac{1}{2}mv^2')}.",
        [f"Square the speed: {m('5^2 = 25')}.",
         f"Compute {m('KE = 0.5 \\times 4 \\times 25 = 50\\text{ J}')}."],
        f"Check: double of {m('50\\text{ J}')} is {m('mv^2 = 100')}.",
        f"نطبق {m('KE = \\frac{1}{2}mv^2')}.",
        [f"نربع السرعة: {m('5^2 = 25')}.",
         f"الطاقة الحركية = {m('0.5 \\times 4 \\times 25 = 50\\text{ جول}')}."],
        f"التحقق: نصف حاصل ضرب {m('4 \\times 25 = 100')} يساوي {m('50\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B15",
        f"A {m('6\\text{ kg}')} potted plant rests on a balcony {m('5\\text{ m}')} above the ground (use {m('g = 10\\text{ m/s}^2')}). What is its gravitational potential energy in {m('\\text{J}')}?",
        f"يستقر أصيص نبات كتلته {m('6\\text{ كجم}')} على شرفة بارتفاع {m('5\\text{ م}')} عن الأرض (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما طاقته الكامنة التثاقلية بالجول؟",
        300, [30, 60, 150],
        "Gravitational potential energy is PE = m × g × h.",
        "الطاقة الكامنة التثاقلية تساوي PE = m × g × h.",
        f"Apply {m('PE = mgh')}.",
        [f"Multiply {m('6\\text{ kg} \\times 10\\text{ m/s}^2 \\times 5\\text{ m}')}.",
         f"PE = {m('300\\text{ J}')}."],
        f"Check: weight {m('60\\text{ N}')} lifted {m('5\\text{ m}')} stores {m('60 \\times 5 = 300\\text{ J}')}.",
        f"نستخدم {m('PE = mgh')}.",
        [f"نضرب {m('6 \\times 10 \\times 5')}.",
         f"طاقة الوضع = {m('300\\text{ جول}')}."],
        f"التحقق: الوزن {m('60\\text{ نيوتن}')} على ارتفاع {m('5\\text{ م}')} يعطي {m('300\\text{ جول}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B15",
        "A student holds a 100 N backpack stationary on her shoulders while walking 15 m horizontally along a level hallway at constant speed. How much mechanical work does the upward supporting force do on the backpack?",
        "تحمل طالبة حقيبة وزنها 100 نيوتن بثبات على كتفيها وهي تسير أفقياً لمسافة 15 م في ممر مستوٍ بسرعة ثابتة. ما مقدار الشغل الميكانيكي الذي تبذله قوة الحمل الرأسية على الحقيبة؟",
        [
            ("0 J, because the upward force is perpendicular to the horizontal motion", "0 جول، لأن القوة الرأسية متعامدة مع اتجاه الحركة الأفقي"),
            ("1,500 J, because 100 N is carried over 15 m", "1,500 جول، لأن قوة 100 نيوتن حُملت لمسافة 15 م"),
            ("100 J, equal to the vertical weight of the bag", "100 جول، مساوياً لوزن الحقيبة الرأسي"),
            ("6.7 J, obtained by dividing weight by distance", "6.7 جول، بقسمة الوزن على المسافة"),
        ],
        "Scientific work requires force and displacement along the same line; perpendicular forces do zero work.",
        "يشترط الشغل الميكانيكي وجود إزاحة في اتجاه القوة؛ فالقوة العمودية على الحركة لا تبذل شغلاً.",
        "Check the angle between supporting force and displacement.",
        ["Supporting force points straight up while displacement is strictly horizontal (90° apart).",
         "Because there is zero displacement in the vertical direction, work done = 0 J."],
        "Neither height nor speed changed, confirming zero work on the backpack.",
        "نختبر اتجاه القوة مقارنة باتجاه الإزاحة.",
        ["قوة الحمل متجهة عمودياً للأعلى بينما الإزاحة أفقية بزاوية 90°.",
         "بما أنه لا توجد إزاحة في اتجاه القوة، فإن الشغل الميكانيكي يساوي صفراً."],
        "لم يتغير ارتفاع الحقيبة أو سرعتها مما يؤكد انعدام الشغل المبذول عليها.",
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B15",
        "If a car's speed doubles while its mass stays constant, by what factor does its kinetic energy increase?",
        "إذا تضاعفت سرعة سيارة إلى المثلين مع ثبات كتلتها، فكم مرة تزداد طاقتها الحركية؟",
        4, [2, 8, 16],
        "Kinetic energy depends on speed squared (v²), not speed linearly.",
        "تعتمد الطاقة الحركية على مربع السرعة (v²) وليس على السرعة مباشرة.",
        f"Replace {m('v')} with {m('2v')} in {m('KE = \\frac{1}{2}mv^2')}.",
        [f"New kinetic energy: {m('\\frac{1}{2}m(2v)^2 = 4\\left(\\frac{1}{2}mv^2\\right)')}.",
         "Therefore, kinetic energy becomes 4 times larger."],
        "Check: doubling speed quadruples stopping work and kinetic energy.",
        f"نعوض {m('2v')} بدلاً من {m('v')} في {m('KE = \\frac{1}{2}mv^2')}.",
        [f"الطاقة الجديدة = {m('\\frac{1}{2}m(2v)^2 = 4 \\times KE_{\\text{old}}')}.",
         "تزداد الطاقة الحركية 4 أضعاف."],
        "التحقق: مربع الاثنين يساوي 4.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B15",
        f"A construction crane lifts a {m('200\\text{ kg}')} steel beam vertically by {m('9\\text{ m}')} in {m('6\\text{ s}')} (use {m('g = 10\\text{ m/s}^2')}). What power in {m('\\text{W}')} does the crane deliver to the beam?",
        f"ترفع رافعة بناء عارضة فولاذية كتلتها {m('200\\text{ كجم}')} رأسياً لمسافة {m('9\\text{ م}')} خلال {m('6\\text{ ث}')} (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما القدرة التي تبذلها الرافعة على العارضة بالواط؟",
        3000, [18000, 300, 12000],
        "First find work done against gravity W = mgh, then divide by time t.",
        "احسب أولاً الشغل المبذول ضد الجاذبية W = mgh ثم اقسمه على الزمن t.",
        f"Compute {m('P = \\frac{mgh}{t}')}.",
        [f"Work = {m('200 \\times 10 \\times 9 = 18,000\\text{ J}')}.",
         f"Power = {m('\\frac{18,000}{6} = 3,000\\text{ W}')}."],
        f"Check: upward speed is {m('1.5\\text{ m/s}')}, and {m('2,000\\text{ N} \\times 1.5\\text{ m/s} = 3,000\\text{ W}')}.",
        f"نطبق {m('P = \\frac{mgh}{t}')}.",
        [f"الشغل = {m('200 \\times 10 \\times 9 = 18,000\\text{ جول}')}.",
         f"القدرة = {m('\\frac{18,000}{6} = 3,000\\text{ واط}')}."],
        f"التحقق: سرعة الرفع {m('1.5\\text{ م/ث}')} × الوزن {m('2,000\\text{ نيوتن}')} = {m('3,000\\text{ واط}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B15",
        f"Ignoring air resistance, a {m('2\\text{ kg}')} stone is dropped from rest at a height of {m('20\\text{ m}')} (use {m('g = 10\\text{ m/s}^2')}). What is its speed in {m('\\text{m/s}')} just before hitting the ground?",
        f"بإهمال مقاومة الهواء، سقط حجر كتلته {m('2\\text{ كجم}')} من السكون من ارتفاع {m('20\\text{ م}')} (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما سرعته بوحدة {m('\\text{م/ث}')} لحظة ملامسته الأرض؟",
        20, [400, 10, 40],
        "Equate initial potential energy (mgh) to final kinetic energy (0.5 mv²).",
        "ساوِ طاقة الوضع الابتدائية (mgh) بالطاقة الحركية النهائية (0.5 mv²).",
        f"Solve {m('mgh = \\frac{1}{2}mv^2')} for {m('v')}.",
        [f"Initial PE = {m('2 \\times 10 \\times 20 = 400\\text{ J}')}.",
         f"Set {m('0.5 \\times 2 \\times v^2 = 400 \\implies v^2 = 400 \\implies v = 20\\text{ m/s}')}."],
        f"Check: mass cancels out in {m('v = \\sqrt{2gh} = \\sqrt{400} = 20\\text{ m/s}')}.",
        f"نساوي {m('mgh = \\frac{1}{2}mv^2')}.",
        [f"طاقة الوضع الابتدائية = {m('2 \\times 10 \\times 20 = 400\\text{ جول}')}.",
         f"إذن {m('v^2 = 400')} ومنها {m('v = 20\\text{ م/ث}')}."],
        f"التحقق: {m('v = \\sqrt{2 \\times 10 \\times 20} = 20\\text{ م/ث}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B15",
        f"An {m('8\\text{ kg}')} medicine ball has a kinetic energy of {m('144\\text{ J}')}. What is its speed in {m('\\text{m/s}')}?",
        f"تمتلك كرة طبية كتلتها {m('8\\text{ كجم}')} طاقة حركية مقدارها {m('144\\text{ جول}')}. ما سرعتها بوحدة {m('\\text{م/ث}')}؟",
        6, [36, 18, 12],
        "Multiply KE by 2, divide by mass, then take the square root.",
        "اضرب الطاقة الحركية في 2، ثم اقسم على الكتلة، ثم خذ الجذر التربيعي.",
        f"Isolate {m('v')} in {m('KE = \\frac{1}{2}mv^2')}.",
        [f"Compute {m('v^2 = \\frac{2 \\times 144}{8} = \\frac{288}{8} = 36')}.",
         f"Take square root: {m('v = 6\\text{ m/s}')}."],
        f"Check: {m('0.5 \\times 8 \\times 6^2 = 4 \\times 36 = 144\\text{ J}')}.",
        f"نعزل السرعة من {m('KE = \\frac{1}{2}mv^2')}.",
        [f"نحسب {m('v^2 = \\frac{2 \\times 144}{8} = 36')}.",
         f"بأخذ الجذر التربيعي: {m('v = 6\\text{ م/ث}')}."],
        f"التحقق: {m('0.5 \\times 8 \\times 36 = 144\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B15",
        f"A worker pushes a {m('400\\text{ N}')} crate up an {m('8\\text{ m}')} long ramp to a loading dock {m('3\\text{ m}')} high using a {m('200\\text{ N}')} force along the ramp. What is the mechanical efficiency of the ramp?",
        f"يدفع عامل صندوقاً وزنه {m('400\\text{ نيوتن}')} على سطح مائل طوله {m('8\\text{ م}')} لرفعه إلى منصة ارتفاعها {m('3\\text{ م}')} بقوة {m('200\\text{ نيوتن}')} بموازاة السطح. ما الكفاءة الميكانيكية للسطح المائل؟",
        75, [50, 80, 62.5],
        "Efficiency = (useful output work / total input work) × 100%, where W_out = weight × height.",
        "الكفاءة = (الشغل الناتج المفيد ÷ الشغل المبذول) × 100%، حيث الشغل المفيد = الوزن × الارتفاع.",
        f"Calculate {m('\\text{Efficiency} = \\frac{W_{\\text{out}}}{W_{\\text{in}}} \\times 100\\%')}.",
        [f"Useful output work (gain in PE): {m('W_{\\text{out}} = 400 \\times 3 = 1,200\\text{ J}')}.",
         f"Input work pushed along ramp: {m('W_{\\text{in}} = 200 \\times 8 = 1,600\\text{ J}')}.",
         f"Efficiency = {m('\\frac{1,200}{1,600} \\times 100\\% = 75\\%')}."],
        "Check: the remaining 25% (400 J) goes into friction thermal energy.",
        f"نطبق {m('\\text{الكفاءة} = \\frac{W_{\\text{out}}}{W_{\\text{in}}} \\times 100\\%')}.",
        [f"الشغل الناتج = {m('400 \\times 3 = 1,200\\text{ جول}')}.",
         f"الشغل المبذول = {m('200 \\times 8 = 1,600\\text{ جول}')}.",
         f"الكفاءة = {m('\\frac{1,200}{1,600} \\times 100\\% = 75\\%')}."],
        "التحقق: الـ 25% المتبقية فُقدت كحرارة بسبب الاحتكاك.",
        suffix=r"\%",
        diagram_en=_svg_energy_ramp("F = 200 N", "L = 8 m", "h = 3 m", "W = 400 N", "en"),
        diagram_ar=_svg_energy_ramp("ق = 200 ن", "ط = 8 م", "ع = 3 م", "و = 400 ن", "ar"),
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B15",
        f"Ignoring air drag, a {m('4\\text{ kg}')} boulder falls freely from rest at a cliff height of {m('45\\text{ m}')} (use {m('g = 10\\text{ m/s}^2')}). What is its kinetic energy in {m('\\text{J}')} as it passes a ledge {m('15\\text{ m}')} above the ground?",
        f"بإهمال مقاومة الهواء، تسقط صخرة كتلتها {m('4\\text{ كجم}')} من السكون من حافة ارتفاعها {m('45\\text{ م}')} (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما طاقتها الحركية بالجول عند مرورها بارتفاع {m('15\\text{ م}')} فوق الأرض؟",
        1200, [600, 1800, 300],
        "Kinetic energy gained equals the potential energy lost during the 30 m drop (45 - 15).",
        "الطاقة الحركية المكتسبة تساوي النقص في طاقة الوضع أثناء الهبوط مسافة 30 م (45 - 15).",
        f"Use energy conservation: {m('KE = PE_i - PE_f = mg(h_i - h_f)')}.",
        [f"Height dropped: {m('\\Delta h = 45 - 15 = 30\\text{ m}')}.",
         f"Kinetic energy = {m('4 \\times 10 \\times 30 = 1,200\\text{ J}')}."],
        f"Check: remaining {m('PE_f = 4 \\times 10 \\times 15 = 600\\text{ J}')}, and {m('1,200 + 600 = 1,800\\text{ J}')}.",
        f"نستخدم حفظ الطاقة: {m('KE = mg(h_i - h_f)')}.",
        [f"المسافة المقطوعة للأسفل = {m('45 - 15 = 30\\text{ م}')}.",
         f"الطاقة الحركية = {m('4 \\times 10 \\times 30 = 1,200\\text{ جول}')}."],
        f"التحقق: {m('KE + PE = 1,200 + 600 = 1,800\\text{ جول}')} وتساوي الطاقة الكلية الابتدائية.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B15",
        f"A {m('1,000\\text{ kg}')} vehicle traveling at {m('10\\text{ m/s}')} brakes uniformly to a complete stop in {m('25\\text{ m}')}. What average braking force in {m('\\text{N}')} acted on it?",
        f"سيارة كتلتها {m('1,000\\text{ كجم}')} تسير بسرعة {m('10\\text{ م/ث}')} تتوقف تماماً بالفرملة خلال مسافة {m('25\\text{ م}')}. ما مقدار متوسط قوة الفرملة بالنيوتن؟",
        2000, [4000, 400, 25000],
        "Set braking work (F × d) equal to initial kinetic energy (0.5 m v²).",
        "ساوِ شغل الفرملة (F × d) بالطاقة الحركية الابتدائية (0.5 m v²).",
        f"Apply Work-Energy Theorem: {m('F d = \\frac{1}{2}mv^2')}.",
        [f"Initial KE = {m('0.5 \\times 1,000 \\times 10^2 = 50,000\\text{ J}')}.",
         f"Braking force = {m('\\frac{50,000}{25} = 2,000\\text{ N}')}."],
        f"Check: {m('2,000\\text{ N} \\times 25\\text{ m} = 50,000\\text{ J}')}.",
        f"نطبق مبرهنة الشغل والطاقة: {m('F d = \\frac{1}{2}mv^2')}.",
        [f"الطاقة الحركية الابتدائية = {m('0.5 \\times 1,000 \\times 100 = 50,000\\text{ جول}')}.",
         f"قوة الفرملة = {m('\\frac{50,000}{25} = 2,000\\text{ نيوتن}')}."],
        f"التحقق: {m('2,000 \\times 25 = 50,000\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B15",
        f"A {m('500\\text{ kg}')} roller-coaster car starts from rest at a {m('30\\text{ m}')} peak and passes the next {m('20\\text{ m}')} hill at {m('10\\text{ m/s}')} (use {m('g = 10\\text{ m/s}^2')}). How many joules ({m('\\text{J}')}) of mechanical energy were converted to thermal energy by friction?",
        f"تنطلق عربة أفعوانية كتلتها {m('500\\text{ كجم}')} من السكون عند قمة ارتفاعها {m('30\\text{ م}')}، وتمر فوق التل التالي بارتفاع {m('20\\text{ م}')} بسرعة {m('10\\text{ م/ث}')} (اعتبر {m('g = 10\\text{ م/ث}^2')}). ما مقدار الطاقة الميكانيكية المفقودة حرارياً بسبب الاحتكاك بالجول؟",
        25000, [50000, 75000, 125000],
        "Subtract total mechanical energy at the second hill (PE + KE) from the initial total energy.",
        "اطرح الطاقة الميكانيكية الكلية عند التل الثاني (الوضع + الحركة) من الطاقة الابتدائية.",
        f"Compute {m('E_{\\text{lost}} = E_i - (PE_f + KE_f)')}.",
        [f"Initial energy: {m('PE_i = 500 \\times 10 \\times 30 = 150,000\\text{ J}')}.",
         f"Final PE: {m('500 \\times 10 \\times 20 = 100,000\\text{ J}')}; Final KE: {m('0.5 \\times 500 \\times 100 = 25,000\\text{ J}')}.",
         f"Thermal loss = {m('150,000 - (100,000 + 25,000) = 25,000\\text{ J}')}."],
        f"Check: {m('100,000 + 25,000 + 25,000 = 150,000\\text{ J}')}.",
        f"نحسب الطاقة المفقودة {m('E_{\\text{lost}} = E_i - (PE_f + KE_f)')}.",
        [f"الطاقة الابتدائية = {m('500 \\times 10 \\times 30 = 150,000\\text{ جول}')}.",
         f"طاقة الوضع النهائية = {m('100,000\\text{ جول}')} والحركية = {m('25,000\\text{ جول}')}.",
         f"الطاقة المفقودة = {m('150,000 - 125,000 = 25,000\\text{ جول}')}."],
        f"التحقق: مجموع الطاقات الثلاث يساوي {m('150,000\\text{ جول}')}.",
    ))

    d_13 = svg_force_block(450, 450, mass_kg=300, title="Steady 2 m/s")
    ar_13 = _ar_svg(d_13, {"Steady 2 m/s": "سرعة ثابتة 2 م/ث", "450 N": "450 نيوتن", "300 kg": "300 كجم"})
    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B15",
        f"A winch pulls a {m('300\\text{ kg}')} sled across snow at a steady speed of {m('2\\text{ m/s}')} against a constant friction force of {m('450\\text{ N}')}. What mechanical power in {m('\\text{W}')} must the winch supply?",
        f"يسحب ونش زلاجة كتلتها {m('300\\text{ كجم}')} على الجليد بسرعة ثابتة {m('2\\text{ م/ث}')} في مواجهة احتكاك ثابت مقداره {m('450\\text{ نيوتن}')}. ما القدرة الميكانيكية بالواط التي يزودها الونش؟",
        900, [225, 600, 6000],
        "At constant speed, applied force equals opposing friction (450 N); use P = F × v.",
        "عند السرعة الثابتة تساوي قوة السحب قوة الاحتكاك (450 نيوتن)؛ استخدم P = F × v.",
        f"Use {m('P = \\frac{Fd}{t} = F v')}.",
        [f"Constant velocity requires pulling force {m('F = 450\\text{ N}')}.",
         f"Power = {m('450\\text{ N} \\times 2\\text{ m/s} = 900\\text{ W}')}."],
        "Check: mass (300 kg) only matters through the friction force already given as 450 N.",
        f"نستخدم العلاقة {m('P = F v')}.",
        [f"ثبات السرعة يعني أن قوة السحب تساوي الاحتكاك {m('450\\text{ نيوتن}')}.",
         f"القدرة = {m('450 \\times 2 = 900\\text{ واط}')}."],
        "التحقق: الكتلة لا تدخل مباشرة لأن قوة الاحتكاك معطاة أصلاً.",
        diagram_en=d_13, diagram_ar=ar_13,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B15",
        "Two pendulums with bobs of mass 2 kg and 8 kg are released simultaneously from the same height 1.25 m above their lowest point (no air drag). How do their speeds compare at the bottom?",
        "أُطلق بندولان كتلتهما 2 كجم و8 كجم في اللحظة نفسها من الارتفاع نفسه (1.25 م فوق أخفض نقطة) دون مقاومة هواء. كيف تقارن سرعتاهما عند أخفض نقطة؟",
        [
            ("Both bobs reach the exact same speed of 5 m/s because mass cancels out", "تصل الكتلتان إلى السرعة نفسها (5 م/ث) لأن الكتلة تختصر من المعادلة"),
            ("The 8 kg bob moves four times faster because it has four times the potential energy", "تتحرك كتلة 8 كجم بسرعة أكبر 4 مرات لأن طاقة وضعها 4 أضعاف"),
            ("The 2 kg bob moves faster because lighter objects accelerate more quickly", "تتحرك كتلة 2 كجم أسرع لأن الأجسام الأخف تتسارع بسهولة"),
            ("The 8 kg bob moves twice as fast as the 2 kg bob", "تتحرك كتلة 8 كجم بضعف سرعة كتلة 2 كجم"),
        ],
        "Write mgh = 0.5 mv² and look at what happens to mass m on both sides.",
        "اكتب معادلة حفظ الطاقة mgh = 0.5 mv² ولاحظ مصير الكتلة m في الطرفين.",
        "Eliminate m from mgh = 0.5 m v².",
        ["Dividing both sides by m leaves gh = 0.5 v², so v = √(2gh).",
         "With g = 10 m/s² and h = 1.25 m, both reach v = √(25) = 5 m/s."],
        "Heavier mass stores more total energy, but requires proportionally more energy to accelerate.",
        "نختصر الكتلة m من طرفي معادلة حفظ الطاقة.",
        ["بقسمة الطرفين على m تصبح السرعة v = √(2gh) مستقلة عن الكتلة.",
         "بتعويض g=10 و h=1.25 تصل كلتا الكتلتين إلى 5 م/ث."],
        "الكتلة الأكبر تمتلك طاقة أكبر لكنها تحتاج طاقة أكبر بنفس النسبة لتصل إلى السرعة نفسها.",
    ))

    return qs


def _gen_sci_b16(start_idx: int) -> list[dict]:
    """G9-SCI-B16: Thermal Energy Q=mcΔT, Phase Changes, Hydraulics & Pressure P=F/A (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B16",
        f"How much thermal energy in {m('\\text{J}')} is required to raise the temperature of {m('2\\text{ kg}')} of water ({m('c = 4,180\\text{ J/(kg}\\cdot^\\circ\\text{C})')}) by {m('10^\\circ\\text{C}')}?",
        f"ما كمية الطاقة الحرارية بالجول اللازمة لرفع درجة حرارة {m('2\\text{ كجم}')} من الماء ({m('c = 4,180\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}) بمقدار {m('10^\\circ\\text{م}')}؟",
        83600, [41800, 8360, 4180],
        "Use the specific heat formula Q = m × c × ΔT.",
        "استخدم قانون الحرارة النوعية Q = m × c × ΔT.",
        f"Apply {m('Q = m c \\Delta T')}.",
        [f"Substitute {m('m = 2\\text{ kg}')}, {m('c = 4,180')}, and {m('\\Delta T = 10^\\circ\\text{C}')}.",
         f"Compute {m('Q = 2 \\times 4,180 \\times 10 = 83,600\\text{ J}')}."],
        f"Check: {m('83,600 / 20 = 4,180')}.",
        f"نطبق {m('Q = m c \\Delta T')}.",
        [f"نعوض {m('m = 2')} و{m('c = 4,180')} و{m('\\Delta T = 10')}.",
         f"الحرارة = {m('2 \\times 4,180 \\times 10 = 83,600\\text{ جول}')}."],
        f"التحقق: {m('83,600 / 20 = 4,180')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B16",
        f"A stone sculpture weighing {m('400\\text{ N}')} rests evenly on a square pedestal base of area {m('0.25\\text{ m}^2')}. What pressure in pascals ({m('\\text{Pa}')}) does it exert on the pedestal?",
        f"يستقر تمثال حجري وزنه {m('400\\text{ نيوتن}')} بالتساوي على قاعدة مساحتها {m('0.25\\text{ م}^2')}. ما مقدار الضغط الذي يؤثر به على القاعدة بالباسكال؟",
        1600, [100, 400, 160],
        "Pressure equals perpendicular force divided by contact area: P = F / A.",
        "الضغط يساوي القوة العمودية مقسومة على المساحة: P = F / A.",
        f"Apply {m('P = \\frac{F}{A}')}.",
        [f"Divide {m('400\\text{ N}')} by {m('0.25\\text{ m}^2')}.",
         f"Pressure = {m('\\frac{400}{0.25} = 1,600\\text{ Pa}')}."],
        f"Check: {m('1,600\\text{ Pa} \\times 0.25\\text{ m}^2 = 400\\text{ N}')}.",
        f"نطبق {m('P = \\frac{F}{A}')}.",
        [f"نقسم {m('400\\text{ نيوتن}')} على {m('0.25\\text{ م}^2')}.",
         f"الضغط = {m('\\frac{400}{0.25} = 1,600\\text{ باسكال}')}."],
        f"التحقق: {m('1,600 \\times 0.25 = 400\\text{ نيوتن}')}.",
    ))

    d_2 = svg_motion_graph([(0, 20), (3, 100), (7, 100), (9, 120)], y_label="Temp (°C)", x_label="Time (min)", title="Heating Curve")
    ar_2 = _ar_svg(d_2, {"Heating Curve": "منحنى التسخين", "Temp (°C)": "الحرارة (°م)", "Time (min)": "الزمن (د)"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B16",
        "In the heating curve for water shown, the temperature stays flat at 100 °C from minute 3 to minute 7 while heat continues to flow in. What happens to that added thermal energy?",
        "في منحنى تسخين الماء الموضح، تبقى درجة الحرارة ثابتة عند 100 °م من الدقيقة 3 إلى الدقيقة 7 مع استمرار تزويد الحرارة. أين تذهب الطاقة الحرارية المضافة خلال تلك الفترة؟",
        [
            ("It overcomes attractions between water molecules during boiling (vaporization)", "تُستهلك في التغلب على قوى التجاذب بين الجزيئات لتحويل السائل إلى بخار"),
            ("It increases the average kinetic energy of liquid water molecules", "تزيد من متوسط الطاقة الحركية لجزيئات الماء السائل"),
            ("It creates new hydrogen and oxygen atoms from water", "تُنتج ذرات هيدروجين وأكسجين جديدة من الماء"),
            ("The burner stopped supplying heat during those minutes", "توقف الموقد عن تزويد الحرارة خلال تلك الدقائق"),
        ],
        "Temperature measures average kinetic energy; during a phase change, added heat changes potential energy instead.",
        "تقيس درجة الحرارة متوسط الطاقة الحركية؛ وأثناء تغير الحالة تتحول الحرارة إلى طاقة وضع بين الجزيئات.",
        "Identify the plateau at 100 °C as boiling (liquid-to-gas phase transition).",
        ["Temperature stays fixed because average molecular kinetic energy does not rise while boiling.",
         "Instead, latent heat breaks intermolecular forces so liquid escapes as steam."],
        "Phase changes occur at constant temperature.",
        "تمثل الهضبة الأفقية عند 100 °م عملية الغليان.",
        ["تثبت الحرارة لأن متوسط الطاقة الحركية للجزيئات لا يزداد أثناء الغليان.",
         "تُستخدم الحرارة الكامنة لكسر الترابط بين الجزيئات وتحويل الماء لبخار."],
        "تحدث تغيرات الحالة دائماً عند درجة حرارة ثابتة.",
        diagram_en=d_2, diagram_ar=ar_2,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B16",
        "Solar energy travels roughly 150 million km across the vacuum of space to warm Earth. By which heat-transfer mechanism does this occur?",
        "تنتقل الطاقة الشمسية عبر فراغ الفضاء مسافة 150 مليون كم تقريباً لتدفئة الأرض. بأي آلية انتقال حرارة يحدث ذلك؟",
        [
            ("Radiation, via electromagnetic waves needing no material medium", "الإشعاع الحراري عبر موجات كهرومغناطيسية لا تحتاج إلى وسط مادي"),
            ("Conduction through empty space molecules", "التوصيل الحراري عبر جزيئات الفراغ"),
            ("Convection currents rising from the Sun to Earth", "تيارات الحمل الصاعدة من الشمس إلى الأرض"),
            ("Evaporative cooling through the solar corona", "التبريد بالتبخر عبر الهالة الشمسية"),
        ],
        "Conduction and convection require colliding or flowing matter particles, which are absent in space.",
        "يتطلب التوصيل والحمل وجود جسيمات مادية، وهو ما يغيب في فراغ الفضاء.",
        "Match space vacuum constraints to the three modes of heat transfer.",
        ["Space is a near vacuum, ruling out conduction and convection.",
         "Thermal radiation carries energy via infrared and visible electromagnetic waves."],
        "Only radiation crosses vacuum efficiently.",
        "نقارن شروط كل آلية انتقال حرارة ببيئة الفضاء.",
        ["الفضاء فراغ يفتقر للوسط المادي اللازم للتوصيل والحمل.",
         "ينقل الإشعاع الطاقة بموجات كهرومغناطيسية عبر الفراغ."],
        "الإشعاع هو الآلية الوحيدة التي لا تتطلب وسطاً مادياً.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B16",
        f"A compressed gas exerts a uniform pressure of {m('30,000\\text{ Pa}')} against a flat piston head of area {m('0.04\\text{ m}^2')}. What total force in {m('\\text{N}')} pushes on the piston?",
        f"يؤثر غاز مضغوط بضغط منتظم مقداره {m('30,000\\text{ باسكال}')} على رأس مكبس مساحته {m('0.04\\text{ م}^2')}. ما مقدار القوة الكلية المؤثرة في المكبس بالنيوتن؟",
        1200, [750000, 120, 12000],
        "Rearrange P = F / A to F = P × A.",
        "أعد ترتيب قانون الضغط إلى: القوة = الضغط × المساحة.",
        f"Multiply pressure by area: {m('F = P A')}.",
        [f"Substitute {m('P = 30,000\\text{ Pa}')} and {m('A = 0.04\\text{ m}^2')}.",
         f"Force = {m('30,000 \\times 0.04 = 1,200\\text{ N}')}."],
        f"Check: {m('\\frac{1,200}{0.04} = 30,000\\text{ Pa}')}.",
        f"نضرب الضغط في المساحة: {m('F = P A')}.",
        [f"نعوض {m('P = 30,000')} و{m('A = 0.04')}.",
         f"القوة = {m('30,000 \\times 0.04 = 1,200\\text{ نيوتن}')}."],
        f"التحقق: {m('\\frac{1,200}{0.04} = 30,000\\text{ باسكال}')}.",
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B16",
        f"A {m('0.5\\text{ kg}')} iron pan ({m('c = 450\\text{ J/(kg}\\cdot^\\circ\\text{C})')}) starts at {m('20^\\circ\\text{C}')} and absorbs {m('18,000\\text{ J}')} of heat. What is its final temperature in {m('^\\circ\\text{C}')}?",
        f"مقلاة حديدية كتلتها {m('0.5\\text{ كجم}')} ({m('c = 450\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}) عند درجة {m('20^\\circ\\text{م}')} امتصت {m('18,000\\text{ جول}')} من الحرارة. ما درجة حرارتها النهائية بوحدة {m('^\\circ\\text{م}')}؟",
        100, [80, 60, 40],
        "Compute ΔT = Q / (m c) first, then ADD initial temperature 20 °C.",
        "احسب مقدار الارتفاع ΔT = Q / (m c) أولاً ثم أضف درجة الحرارة الابتدائية 20 °م.",
        f"Solve {m('\\Delta T = \\frac{Q}{m c}')} and find {m('T_f = T_i + \\Delta T')}.",
        [f"Denominator: {m('m c = 0.5 \\times 450 = 225\\text{ J/}^\\circ\\text{C}')}.",
         f"Temperature rise: {m('\\Delta T = \\frac{18,000}{225} = 80^\\circ\\text{C}')}.",
         f"Final temperature: {m('20 + 80 = 100^\\circ\\text{C}')}."],
        f"Check: {m('0.5 \\times 450 \\times (100 - 20) = 18,000\\text{ J}')}.",
        f"نحسب التغير في الحرارة ثم نضيفه إلى البداية.",
        [f"نضرب {m('0.5 \\times 450 = 225')}.",
         f"مقدار الارتفاع = {m('\\frac{18,000}{225} = 80^\\circ\\text{م}')}.",
         f"الحرارة النهائية = {m('20 + 80 = 100^\\circ\\text{م}')}."],
        f"التحقق: {m('0.5 \\times 450 \\times 80 = 18,000\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B16",
        f"Adding {m('1,560\\text{ J}')} of heat to a {m('0.2\\text{ kg}')} copper sample raises its temperature by {m('20^\\circ\\text{C}')}. What is copper's specific heat capacity in {m('\\text{J/(kg}\\cdot^\\circ\\text{C})')}?",
        f"تؤدي إضافة {m('1,560\\text{ جول}')} من الحرارة إلى عينة نحاس كتلتها {m('0.2\\text{ كجم}')} إلى رفع حرارتها بمقدار {m('20^\\circ\\text{م}')}. ما الحرارة النوعية للنحاس بوحدة {m('\\text{جول/(كجم}\\cdot^\\circ\\text{م})')}؟",
        390, [78, 195, 780],
        "Rearrange Q = m c ΔT to c = Q / (m ΔT).",
        "أعد ترتيب القانون إلى c = Q / (m ΔT).",
        f"Isolate {m('c = \\frac{Q}{m \\Delta T}')}.",
        [f"Compute {m('m \\Delta T = 0.2 \\times 20 = 4\\text{ kg}\\cdot^\\circ\\text{C}')}.",
         f"Specific heat: {m('c = \\frac{1,560}{4} = 390\\text{ J/(kg}\\cdot^\\circ\\text{C})')}."],
        f"Check: {m('0.2 \\times 390 \\times 20 = 1,560\\text{ J}')}.",
        f"نعزل الحرارة النوعية {m('c = \\frac{Q}{m \\Delta T}')}.",
        [f"نضرب {m('0.2 \\times 20 = 4')}.",
         f"الحرارة النوعية = {m('\\frac{1,560}{4} = 390\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}."],
        f"التحقق: {m('0.2 \\times 390 \\times 20 = 1,560\\text{ جول}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B16",
        f"In a hydraulic car lift, a {m('150\\text{ N}')} force pushes down on a small piston of area {m('0.02\\text{ m}^2')}. What upward output force in {m('\\text{N}')} acts on the large piston of area {m('0.40\\text{ m}^2')}?",
        f"في رافعة سيارات هيدروليكية، تؤثر قوة {m('150\\text{ نيوتن}')} في المكبس الصغير ذي المساحة {m('0.02\\text{ م}^2')}. ما مقدار القوة الرافعة بالنيوتن المؤثرة في المكبس الكبير ذي المساحة {m('0.40\\text{ م}^2')}؟",
        3000, [7.5, 300, 6000],
        "By Pascal's principle, hydraulic fluid transmits equal pressure: F1 / A1 = F2 / A2.",
        "حسب مبدأ باسكال، يتساوى الضغط في السائل المحصور: F1 / A1 = F2 / A2.",
        f"Solve {m('\\frac{F_1}{A_1} = \\frac{F_2}{A_2}')}.",
        [f"Area ratio: {m('\\frac{A_2}{A_1} = \\frac{0.40}{0.02} = 20')}.",
         f"Output force: {m('F_2 = 150 \\times 20 = 3,000\\text{ N}')}."],
        f"Check: pressure on both pistons is {m('\\frac{150}{0.02} = 7,500\\text{ Pa} = \\frac{3,000}{0.40}')}.",
        f"نساوي الضغطين {m('\\frac{F_1}{A_1} = \\frac{F_2}{A_2}')}.",
        [f"نسبة المساحتين = {m('\\frac{0.40}{0.02} = 20')}.",
         f"القوة الناتجة = {m('150 \\times 20 = 3,000\\text{ نيوتن}')}."],
        f"التحقق: الضغط في كلا المكبسين يساوي {m('7,500\\text{ باسكال}')}.",
        diagram_en=_svg_hydraulic_lift("F1 = 150 N", "A1 = 0.02 m2", "A2 = 0.40 m2", "F2 = ?", "en"),
        diagram_ar=_svg_hydraulic_lift("ق1 = 150 ن", "م1 = 0.02 م2", "م2 = 0.40 م2", "ق2 = ?", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B16",
        f"A rectangular solid brick measures {m('20\\text{ cm} \\times 10\\text{ cm} \\times 5\\text{ cm}')}. Compared with resting on its largest face, how many times greater is the pressure when resting on its smallest face?",
        f"قالب طوب مستطيل أبعاده {m('20\\text{ سم} \\times 10\\text{ سم} \\times 5\\text{ سم}')}. كم مرة يزيد الضغط الناتج عندما يرتكز على أصغر وجه له مقارنة بارتكازه على أكبر وجه له؟",
        4, [2, 8, 10],
        "Because force (weight) is constant, pressure ratio equals largest face area divided by smallest face area.",
        "بما أن الوزن ثابت، فإن نسبة الضغط تساوي مساحة أكبر وجه مقسومة على مساحة أصغر وجه.",
        f"Compare {m('A_{\\max}')} and {m('A_{\\min}')} under fixed weight {m('W')}.",
        [f"Largest face area: {m('20 \\times 10 = 200\\text{ cm}^2')}; smallest face area: {m('10 \\times 5 = 50\\text{ cm}^2')}.",
         f"Pressure ratio = {m('\\frac{200}{50} = 4')}.",],
        "Check: pressure is inversely proportional to contact area.",
        "نقارن بين أكبر مساحة وأصغر مساحة مع ثبات الوزن.",
        [f"أكبر وجه = {m('20 \\times 10 = 200\\text{ سم}^2')}، وأصغر وجه = {m('10 \\times 5 = 50\\text{ سم}^2')}.",
         f"نسبة الضغط = {m('\\frac{200}{50} = 4')} أضعاف."],
        "التحقق: يتناسب الضغط عكسياً مع مساحة التلامس.",
        diagram_en=_svg_experiment_bars("Brick Dimensions", "أبعاد قالب الطوب", [("Length", "الطول", 20, "20 cm"), ("Width", "العرض", 10, "10 cm"), ("Height", "الارتفاع", 5, "5 cm")], "Side (cm)", "البعد (سم)", "en"),
        diagram_ar=_svg_experiment_bars("Brick Dimensions", "أبعاد قالب الطوب", [("Length", "الطول", 20, "20 cm"), ("Width", "العرض", 10, "10 cm"), ("Height", "الارتفاع", 5, "5 cm")], "Side (cm)", "البعد (سم)", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B16",
        f"What gauge fluid pressure in {m('\\text{Pa}')} does freshwater ({m('\\rho = 1,000\\text{ kg/m}^3')}) exert at a depth of {m('5\\text{ m}')} (use {m('g = 10\\text{ m/s}^2')})?",
        f"ما ضغط المائع الإضافي بالباسكال الذي يولده الماء العذب ({m('\\rho = 1,000\\text{ كجم/م}^3')}) على عمق {m('5\\text{ م}')} (اعتبر {m('g = 10\\text{ م/ث}^2')})؟",
        50000, [5000, 200, 10000],
        "Use hydrostatic pressure P = ρ × g × h.",
        "استخدم قانون ضغط المائع P = ρ × g × h.",
        f"Apply {m('P = \\rho g h')}.",
        [f"Multiply {m('1,000\\text{ kg/m}^3 \\times 10\\text{ m/s}^2 \\times 5\\text{ m}')}.",
         f"Pressure = {m('50,000\\text{ Pa}')}."],
        "Check: 5 m of water produces roughly half an atmosphere (~50 kPa).",
        f"نطبق {m('P = \\rho g h')}.",
        [f"نضرب {m('1,000 \\times 10 \\times 5')}.",
         f"الضغط = {m('50,000\\text{ باسكال}')}."],
        "التحقق: كل متر عمق في الماء يضيف نحو 10,000 باسكال.",
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B16",
        f"In an insulated calorimeter, {m('1\\text{ kg}')} of hot aluminum ({m('c = 900\\text{ J/(kg}\\cdot^\\circ\\text{C})')}) at {m('100^\\circ\\text{C}')} is submerged in {m('1\\text{ kg}')} of oil ({m('c = 1,800\\text{ J/(kg}\\cdot^\\circ\\text{C})')}) at {m('25^\\circ\\text{C}')}. What equilibrium temperature in {m('^\\circ\\text{C}')} do they reach?",
        f"في مسعر معزول، وُضع {m('1\\text{ كجم}')} من الألومنيوم الساخن ({m('c = 900\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}) عند {m('100^\\circ\\text{م}')} داخل {m('1\\text{ كجم}')} من زيت ({m('c = 1,800\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}) عند {m('25^\\circ\\text{م}')}. ما درجة حرارة الاتزان الحراري بوحدة {m('^\\circ\\text{م}')}؟",
        50, [62.5, 40, 75],
        "Heat lost by aluminum equals heat gained by oil: m_Al c_Al (100 - T) = m_oil c_oil (T - 25).",
        "الحرارة المفقودة من الألومنيوم تساوي الحرارة المكتسبة للزيت: 900(100 - T) = 1800(T - 25).",
        f"Equate {m('Q_{\\text{lost}} = Q_{\\text{gained}}')}.",
        [f"Write {m('900(100 - T) = 1,800(T - 25)')}.",
         f"Divide both sides by {m('900')}: {m('100 - T = 2(T - 25) = 2T - 50')}.",
         f"Solve {m('3T = 150 \\implies T = 50^\\circ\\text{C}')}."],
        f"Check: aluminum loses {m('900 \\times 50 = 45,000\\text{ J}')}; oil gains {m('1,800 \\times 25 = 45,000\\text{ J}')}.",
        f"نساوي {m('Q_{\\text{lost}} = Q_{\\text{gained}}')}.",
        [f"نكتب {m('900(100 - T) = 1,800(T - 25)')}.",
         f"بقسمة الطرفين على 900: {m('100 - T = 2T - 50')}.",
         f"إذن {m('3T = 150')} ومنها {m('T = 50^\\circ\\text{م}')}."],
        f"التحقق: الألومنيوم يفقد {m('45,000\\text{ جول}')} والزيت يكتسب {m('45,000\\text{ جول}')}.",
        diagram_en=_svg_experiment_bars("Initial Temperatures", "درجات الحرارة الابتدائية", [("Aluminum", "ألومنيوم", 100, "100 C"), ("Oil", "زيت", 25, "25 C")], "Temp (C)", "الحرارة (م)", "en"),
        diagram_ar=_svg_experiment_bars("Initial Temperatures", "درجات الحرارة الابتدائية", [("Aluminum", "ألومنيوم", 100, "100 C"), ("Oil", "زيت", 25, "25 C")], "Temp (C)", "الحرارة (م)", "ar"),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B16",
        "On a sunny afternoon, beach sand (c ≈ 800 J/(kg·°C)) becomes painfully hot while adjacent seawater (c ≈ 4,180 J/(kg·°C)) remains cool under the same sunlight. Which explanation is scientifically accurate?",
        "في ظهيرة مشمسة تسخن رمال الشاطئ (حرارتها النوعية ≈ 800) بشدة بينما يبقى ماء البحر المجاور (حرارته النوعية ≈ 4,180) بارداً نسبياً تحت أشعة الشمس نفسها. أي تفسير علمي أدق؟",
        [
            ("Water's much higher specific heat means each joule of solar energy raises its temperature far less than sand", "الحرارة النوعية المرتفعة جداً للماء تعني أن كمية الطاقة نفسها ترفع حرارته بمقدار أقل بكثير من الرمل"),
            ("Sand absorbs solar radiation while water reflects 100% of sunlight", "يمتص الرمل الإشعاع الشمسي بينما يعكس الماء 100% من ضوء الشمس"),
            ("Sand has higher thermal conductivity so all heat stays trapped on top", "يمتلك الرمل توصيلاً حرارياً عالياً يحبس الحرارة في السطح"),
            ("Water cannot gain thermal energy from radiation, only from convection", "لا يكتسب الماء طاقة حرارية بالإشعاع بل بالحمل فقط"),
        ],
        "Look at ΔT = Q / (m c): when c is larger in the denominator, ΔT is smaller.",
        "انظر إلى العلاقة ΔT = Q / (m c): كلما كبرت الحرارة النوعية c في المقام قلّ الارتفاع ΔT.",
        "Compare temperature change inversely to specific heat capacity.",
        ["For equal mass and equal absorbed solar energy Q, ΔT is inversely proportional to c.",
         "Because water's c is over 5 times sand's c, water warms much more slowly."],
        "Water's high specific heat stabilizes coastal climates day and night.",
        "نقارن تغير درجة الحرارة عكسياً مع الحرارة النوعية.",
        ["عند تساوي الكتلة والطاقة الممتصة Q، يتناسب ΔT عكسياً مع الحرارة النوعية c.",
         "لأن حرارة الماء النوعية تفوق الرمل بأكثر من 5 أضعاف، يسخن الماء ببطء شديد."],
        "الحرارة النوعية العالية للماء تجعل مناخ السواحل أكثر اعتدالاً.",
    ))

    d_12 = svg_motion_graph([(0, 0), (4, 0), (6, 20)], y_label="Temp (°C)", x_label="Step", title="Ice Melt and Warm")
    ar_12 = _ar_svg(d_12, {"Ice Melt and Warm": "انصهار وتسخين", "Temp (°C)": "الحرارة (°م)", "Step": "المرحلة"})
    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B16",
        f"How much total thermal energy in {m('\\text{J}')} melts {m('2\\text{ kg}')} of ice at {m('0^\\circ\\text{C}')} ({m('L_f = 334,000\\text{ J/kg}')}) and then warms the resulting liquid water ({m('c = 4,200\\text{ J/(kg}\\cdot^\\circ\\text{C})')}) to {m('20^\\circ\\text{C}')}?",
        f"ما كمية الطاقة الحرارية الكلية بالجول اللازمة لصهر {m('2\\text{ كجم}')} من الجليد عند {m('0^\\circ\\text{م}')} ({m('L_f = 334,000\\text{ جول/كجم}')}) ثم تسخين الماء الناتج ({m('c = 4,200\\text{ جول/(كجم}\\cdot^\\circ\\text{م})')}) إلى {m('20^\\circ\\text{م}')}؟",
        836000, [668000, 168000, 500000],
        "Add two terms: latent heat to melt ice (m L_f) PLUS sensible heat to warm water (m c ΔT).",
        "اجمع مرحلتين: الحرارة الكامنة للانصهار (m L_f) + حرارة تسخين الماء الناتج (m c ΔT).",
        f"Compute {m('Q_{\\text{total}} = m L_f + m c \\Delta T')}.",
        [f"Melting ice at {m('0^\\circ\\text{C}')}: {m('Q_1 = 2 \\times 334,000 = 668,000\\text{ J}')}.",
         f"Warming water from {m('0')} to {m('20^\\circ\\text{C}')}: {m('Q_2 = 2 \\times 4,200 \\times 20 = 168,000\\text{ J}')}.",
         f"Total = {m('668,000 + 168,000 = 836,000\\text{ J}')}."],
        "Check: melting takes roughly four times more energy than warming the water by 20 °C.",
        f"نجمع {m('Q_{\\text{total}} = m L_f + m c \\Delta T')}.",
        [f"صهر الجليد = {m('2 \\times 334,000 = 668,000\\text{ جول}')}.",
         f"تسخين الماء = {m('2 \\times 4,200 \\times 20 = 168,000\\text{ جول}')}.",
         f"المجموع = {m('668,000 + 168,000 = 836,000\\text{ جول}')}."],
        "التحقق: يتطلب الانصهار طاقة تفوق تسخين الماء بنحو أربع مرات.",
        diagram_en=d_12, diagram_ar=ar_12,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B16",
        f"If atmospheric pressure at a lake surface is {m('101\\text{ kPa}')}, what is the total absolute pressure in {m('\\text{kPa}')} on a diver {m('15\\text{ m}')} below the surface ({m('\\rho = 1,000\\text{ kg/m}^3')}, {m('g = 10\\text{ m/s}^2')})?",
        f"إذا كان الضغط الجوي على سطح بحيرة يساوي {m('101\\text{ كيلوباسكال}')}، فما الضغط الكلي المطلق بالكيلوباسكال على غواص على عمق {m('15\\text{ م}')} ({m('\\rho = 1,000\\text{ كجم/م}^3')}، {m('g = 10\\text{ م/ث}^2')})؟",
        251, [150, 49, 251000],
        "Compute water pressure ρgh in Pa, convert to kPa (divide by 1,000), then add atmospheric 101 kPa.",
        "احسب ضغط الماء ρgh بالباسكال ثم حوّله إلى كيلوباسكال وأضف الضغط الجوي 101 كيلوباسكال.",
        f"Use {m('P_{\\text{total}} = P_{\\text{atm}} + \\rho g h')}.",
        [f"Water column pressure: {m('1,000 \\times 10 \\times 15 = 150,000\\text{ Pa} = 150\\text{ kPa}')}.",
         f"Total pressure = {m('101 + 150 = 251\\text{ kPa}')}."],
        "Check: every 10 m of freshwater adds 100 kPa (~1 atm), so 15 m adds 1.5 atm.",
        f"نطبق {m('P_{\\text{total}} = P_{\\text{atm}} + \\rho g h')}.",
        [f"ضغط الماء = {m('1,000 \\times 10 \\times 15 = 150,000\\text{ باسكال} = 150\\text{ كيلوباسكال}')}.",
         f"الضغط الكلي = {m('101 + 150 = 251\\text{ كيلوباسكال}')}."],
        "التحقق: كل 10 م عمق تضيف 100 كيلوباسكال، لذا 15 م تضيف 150 كيلوباسكال.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B16",
        f"A sealed syringe holds {m('6.0\\text{ L}')} of air at {m('120\\text{ kPa}')}. If the plunger slowly compresses the air at constant temperature to {m('1.5\\text{ L}')}, what is the new pressure in {m('\\text{kPa}')}?",
        f"تحتوي حقنة محكمة الإغلاق على {m('6.0\\text{ لتر}')} من الهواء عند ضغط {m('120\\text{ كيلوباسكال}')}. إذا ضُغط الهواء ببطء عند درجة حرارة ثابتة ليصبح حجمه {m('1.5\\text{ لتر}')}، فما الضغط الجديد بالكيلوباسكال؟",
        480, [30, 360, 720],
        "At constant temperature, Boyle's law gives P1 V1 = P2 V2.",
        "عند ثبات درجة الحرارة ينص قانون بويل على أن P1 V1 = P2 V2.",
        f"Solve {m('P_2 = \\frac{P_1 V_1}{V_2}')}.",
        [f"Volume shrinks by factor {m('\\frac{6.0}{1.5} = 4')}.",
         f"Pressure multiplies by 4: {m('P_2 = 120 \\times 4 = 480\\text{ kPa}')}."],
        f"Check: {m('120 \\times 6.0 = 720 = 480 \\times 1.5')}.",
        f"نطبق قانون بويل {m('P_2 = \\frac{P_1 V_1}{V_2}')}.",
        [f"تقلص الحجم إلى الربع ({m('6.0 / 1.5 = 4')}).",
         f"يتضاعف الضغط 4 مرات ليصبح {m('120 \\times 4 = 480\\text{ كيلوباسكال}')}."],
        f"التحقق: {m('120 \\times 6.0 = 480 \\times 1.5 = 720')}.",
    ))

    return qs


def _gen_sci_b17(start_idx: int) -> list[dict]:
    """G9-SCI-B17: Transverse Wave Speed v=fλ, f=1/T, Refraction, Echo & Energy (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = svg_wave_diagram(3.5, 0.8)
    ar_0 = _ar_svg(d_0, {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"})
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B17",
        f"A transverse wave shown has wavelength {m('\\lambda = 3.5\\text{ m}')} and vibrates at frequency {m('f = 12\\text{ Hz}')}. What is the wave speed in {m('\\text{m/s}')}?",
        f"توضح الرسمة موجة مستعرضة طولها الموجي {m('\\lambda = 3.5\\text{ م}')} وترددها {m('f = 12\\text{ هرتز}')}. ما سرعة انتشار الموجة بوحدة {m('\\text{م/ث}')}؟",
        42, [15.5, 0.29, 8.5],
        "Multiply frequency by wavelength using the wave speed equation v = f λ.",
        "اضرب التردد في الطول الموجي باستخدام معادلة سرعة الموجة v = f λ.",
        f"Apply {m('v = f \\lambda')}.",
        [f"Substitute {m('f = 12\\text{ Hz}')} and {m('\\lambda = 3.5\\text{ m}')}.",
         f"Speed = {m('12 \\times 3.5 = 42\\text{ m/s}')}."],
        f"Check: {m('12')} waves of {m('3.5\\text{ m}')} pass every second, totaling {m('42\\text{ m}')}.",
        f"نطبق معادلة الموجة {m('v = f \\lambda')}.",
        [f"نعوض {m('f = 12\\text{ هرتز}')} و{m('\\lambda = 3.5\\text{ م}')}.",
         f"السرعة = {m('12 \\times 3.5 = 42\\text{ م/ث}')}."],
        f"التحقق: تعبر 12 موجة بطول 3.5 م كل ثانية أي 42 م في الثانية.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B17",
        f"A guitar string completes one full vibration every {m('T = 0.05\\text{ s}')}. What is its frequency in hertz ({m('\\text{Hz}')})?",
        f"يُكمل وتر جيتار اهتزازة كاملة واحدة كل {m('T = 0.05\\text{ ث}')}. ما تردده بوحدة الهرتز؟",
        20, [5, 0.05, 50],
        "Frequency is the reciprocal of period: f = 1 / T.",
        "التردد هو مقلوب الزمن الدوري: f = 1 / T.",
        f"Compute {m('f = \\frac{1}{T}')}.",
        [f"Divide {m('1')} by {m('0.05\\text{ s}')}.",
         f"Frequency = {m('\\frac{1}{0.05} = 20\\text{ Hz}')}."],
        f"Check: {m('20 \\times 0.05 = 1')}.",
        f"نطبق {m('f = \\frac{1}{T}')}.",
        [f"نقسم {m('1')} على {m('0.05\\text{ ث}')}.",
         f"التردد = {m('\\frac{1}{0.05} = 20\\text{ هرتز}')}."],
        f"التحقق: {m('20 \\times 0.05 = 1')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B17",
        f"Sound waves travel through air at {m('340\\text{ m/s}')}. What is the wavelength in {m('\\text{m}')} of a tone whose frequency is {m('170\\text{ Hz}')}?",
        f"تنتقل الموجات الصوتية في الهواء بسرعة {m('340\\text{ م/ث}')}. ما الطول الموجي بالمتر لنغمة ترددها {m('170\\text{ هرتز}')}؟",
        2, [0.5, 510, 57800],
        "Divide wave speed by frequency: λ = v / f.",
        "اقسم سرعة الموجة على التردد: λ = v / f.",
        f"Rearrange {m('v = f \\lambda')} to {m('\\lambda = \\frac{v}{f}')}.",
        [f"Substitute {m('v = 340\\text{ m/s}')} and {m('f = 170\\text{ Hz}')}.",
         f"Wavelength = {m('\\frac{340}{170} = 2\\text{ m}')}."],
        f"Check: {m('170 \\times 2 = 340\\text{ m/s}')}.",
        f"نعزل الطول الموجي {m('\\lambda = \\frac{v}{f}')}.",
        [f"نعوض {m('v = 340')} و{m('f = 170')}.",
         f"الطول الموجي = {m('\\frac{340}{170} = 2\\text{ م}')}."],
        f"التحقق: {m('170 \\times 2 = 340\\text{ م/ث}')}.",
    ))

    d_3 = svg_wave_diagram(4.0, 1.2)
    ar_3 = _ar_svg(d_3, {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B17",
        "How does the oscillation of medium particles compare between a transverse wave and a longitudinal wave?",
        "كيف تختلف حركة اهتزاز دقائق الوسط بين الموجة المستعرضة والموجة الطولية؟",
        [
            ("Transverse particles vibrate perpendicular to wave travel; longitudinal particles vibrate parallel to wave travel", "في المستعرضة تهتز الدقائق عمودياً على اتجاه الانتشار، وفي الطولية تهتز موازية لاتجاه الانتشار"),
            ("Transverse particles travel all the way from source to receiver; longitudinal particles stay fixed", "في المستعرضة تنتقل الدقائق مع الموجة حتى الهدف، وفي الطولية تبقى ساكنة"),
            ("Both wave types oscillate perpendicular to energy propagation", "كلا النوعين يهتز عمودياً على اتجاه انتقال الطاقة"),
            ("Longitudinal waves can travel through vacuum while transverse waves cannot", "الموجات الطولية تنتقل في الفراغ بينما المستعرضة لا تنتقل"),
        ],
        "Recall water ripples (up-and-down while wave moves horizontally) vs sound compressions (back-and-forth along travel).",
        "تذكر تموجات الماء (أعلى وأسفل مع انتشار أفقي) مقابل موجات الصوت (تضاغطات باتجاه الانتشار نفسه).",
        "Contrast particle vibration geometry against energy travel direction.",
        ["In transverse waves (e.g., rope waves), particles move up/down perpendicular to travel.",
         "In longitudinal waves (e.g., sound), particles compress back/forth parallel to travel."],
        "Notice neither mechanical wave permanently transports matter along with the wave.",
        "نقارن اتجاه اهتزاز دقائق الوسط باتجاه انتشار الطاقة.",
        ["في الموجة المستعرضة تهتز الدقائق عمودياً على خط الانتشار (قمم وقيعان).",
         "في الموجة الطولية تهتز الدقائق للأمام والخلف موازية لخط الانتشار (تضاغطات وتخلخلات)."],
        "لا تنقل الموجات المادة نفسها معها بل تنقل الطاقة فقط.",
        diagram_en=d_3, diagram_ar=ar_3,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B17",
        f"A moored fishing buoy bobs up and down as {m('8')} complete ocean waves pass it in {m('4\\text{ s}')}. What is the period {m('T')} of each wave in seconds?",
        f"تطفو عوامة صيد فتمر بها {m('8')} موجات بحرية كاملة خلال {m('4\\text{ ث}')}. ما الزمن الدوري {m('T')} لكل موجة بالثانية؟",
        0.5, [2, 32, 0.25],
        "Period is seconds per single wave: T = total time / number of waves.",
        "الزمن الدوري هو زمن الموجة الواحدة: الزمن الكلي ÷ عدد الموجات.",
        f"Compute {m('T = \\frac{\\text{total time}}{\\text{number of waves}}')}.",
        [f"Divide {m('4\\text{ s}')} by {m('8')} waves.",
         f"Period = {m('\\frac{4}{8} = 0.5\\text{ s}')}."],
        f"Check: frequency is {m('f = 8 / 4 = 2\\text{ Hz}')}, and {m('T = 1/2 = 0.5\\text{ s}')}.",
        f"نحسب {m('T = \\frac{\\text{الزمن الكلي}}{\\text{عدد الموجات}}')}.",
        [f"نقسم {m('4\\text{ ث}')} على {m('8')} موجات.",
         f"الزمن الدوري = {m('\\frac{4}{8} = 0.5\\text{ ث}')}."],
        f"التحقق: التردد {m('2\\text{ هرتز}')} ومقلوبه {m('0.5\\text{ ث}')}.",
    ))

    # --- MEDIUM (5..9) ---
    d_5 = svg_wave_diagram(6.0, 1.5)
    ar_5 = _ar_svg(d_5, {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"})
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B17",
        f"Along a stretched spring oscillating at {m('5\\text{ Hz}')}, the horizontal distance from the 1st crest to the 5th crest ({m('4')} full wavelengths) is {m('24\\text{ m}')}. What is the wave speed in {m('\\text{m/s}')}?",
        f"في نابض مشدود يهتز بتردد {m('5\\text{ هرتز}')}، تبلغ المسافة الأفقية من القمة الأولى إلى القمة الخامسة ({m('4')} أطوال موجية كاملة) {m('24\\text{ م}')}. ما سرعة الموجة بوحدة {m('\\text{م/ث}')}؟",
        30, [120, 24, 15],
        "First find one wavelength λ = 24 / 4 = 6 m, then multiply by 5 Hz.",
        "أوجد الطول الموجي الواحد أولاً (24 ÷ 4 = 6 م) ثم اضربه في التردد 5 هرتز.",
        "Count wave intervals between crests, find λ, then compute v = fλ.",
        [f"From crest 1 to crest 5 spans {m('5 - 1 = 4')} wavelengths, so {m('\\lambda = \\frac{24}{4} = 6\\text{ m}')}.",
         f"Wave speed = {m('5\\text{ Hz} \\times 6\\text{ m} = 30\\text{ m/s}')}."],
        f"Check: {m('4')} waves cover {m('24\\text{ m}')}, and {m('5')} waves pass each second.",
        "نحسب عدد الأطوال الموجية بين القمتين ثم نطبق معادلة السرعة.",
        [f"من القمة 1 إلى القمة 5 توجد {m('4')} موجات كاملة، إذن {m('\\lambda = \\frac{24}{4} = 6\\text{ م}')}.",
         f"السرعة = {m('5 \\times 6 = 30\\text{ م/ث}')}."],
        f"التحقق: {m('5 \\times 6 = 30\\text{ م/ث}')}.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B17",
        f"An observer watches ripple waves of wavelength {m('2.5\\text{ m}')} pass a dock pole. Exactly {m('2.0\\text{ s}')} elapse between the 1st crest and the 11th crest passing the pole. What is the wave speed in {m('\\text{m/s}')}?",
        f"تبلغ المسافة الموجية لتموجات مائية {m('2.5\\text{ م}')}. تمر {m('2.0\\text{ ث}')} بالضبط بين عبور القمة الأولى والقمة الحادية عشرة عمود الرصيف. ما سرعة الموجة بوحدة {m('\\text{م/ث}')}؟",
        12.5, [13.75, 10, 25],
        "Crest 1 to crest 11 equals 10 complete cycles (11 - 1 = 10), not 11 cycles.",
        "المسافة الزمنية بين القمة 1 والقمة 11 تمثل 10 دورات كاملة (11 - 1) وليس 11 دورة.",
        "Find frequency from 10 cycles in 2 s, then multiply by λ.",
        [f"Number of full waves = {m('11 - 1 = 10')}, so {m('f = \\frac{10}{2.0} = 5\\text{ Hz}')}.",
         f"Wave speed = {m('5 \\times 2.5 = 12.5\\text{ m/s}')}."],
        f"Check: {m('10')} waves × {m('2.5\\text{ m}')} = {m('25\\text{ m}')} traveled in {m('2\\text{ s}')}, giving {m('12.5\\text{ m/s}')}.",
        "نحسب عدد الموجات الكاملة بين القمتين ثم نجد التردد والسرعة.",
        [f"عدد الدورات الكاملة = {m('11 - 1 = 10')} موجات، إذن {m('f = \\frac{10}{2.0} = 5\\text{ هرتز}')}.",
         f"السرعة = {m('5 \\times 2.5 = 12.5\\text{ م/ث}')}."],
        f"التحقق: تقطع 10 موجات مسافة {m('25\\text{ م}')} في {m('2\\text{ ث}')} أي {m('12.5\\text{ م/ث}')}.",
        diagram_en=svg_wave_diagram(2.5, 1.0),
        diagram_ar=_ar_svg(svg_wave_diagram(2.5, 1.0), {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"}),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B17",
        "Ocean waves move from deep water into a shallower coastal shelf, causing their speed to decrease. What happens to their frequency and wavelength?",
        "تنتقل أمواج محيطية من المياه العميقة إلى مياه ساحلية ضحلة فتقل سرعتها. ماذا يحدث لترددها وطولها الموجي؟",
        [
            ("Frequency remains constant while wavelength decreases", "يبقى التردد ثابتاً بينما يقل الطول الموجي"),
            ("Wavelength remains constant while frequency increases", "يبقى الطول الموجي ثابتاً بينما يزداد التردد"),
            ("Both frequency and wavelength increase together", "يزداد كل من التردد والطول الموجي معاً"),
            ("Both frequency and wavelength decrease proportionally", "يقل كل من التردد والطول الموجي بنفس النسبة"),
        ],
        "Frequency is fixed solely by the source generating the waves; only medium properties alter v and λ.",
        "التردد تحدده خصائص المصدر فقط ولا يتغير بتغير الوسط؛ بينما تتغير السرعة والطول الموجي.",
        "Apply v = f λ across a medium boundary.",
        ["Wave frequency f is set by the source and stays constant upon crossing into shallow water.",
         "Since v = f λ and speed v drops, wavelength λ must shorten proportionally."],
        "Look at incoming beach surf: wave crests bunch closer together near shore.",
        "نطبق معادلة الموجة v = f λ عند الانتقال بين وسطين.",
        ["التردد ثابت لأنه يعتمد على مصدر الاهتزاز فقط.",
         "وبما أن السرعة تقل، لا بد أن ينقص الطول الموجي بالتناسب نفسه."],
        "لذلك تتقارب قمم الأمواج بعضها من بعض كلما اقتربت من الشاطئ.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B17",
        f"A hiker shouts toward a canyon wall and hears the echo {m('1.6\\text{ s}')} later when sound speed is {m('340\\text{ m/s}')}. How far away in {m('\\text{m}')} is the canyon wall?",
        f"صاح متسلق جبال باتجاه جدار وادٍ فسمع الصدى بعد {m('1.6\\text{ ث}')} عندما كانت سرعة الصوت {m('340\\text{ م/ث}')}. كم يبعد الجدار بالمتر؟",
        272, [544, 136, 212.5],
        "An echo makes a round trip (to the wall and back), so divide the 1.6 s time in half.",
        "يقطع الصدى مسافة ذهاباً وإياباً، لذا اقسم الزمن 1.6 ث على 2 لحساب البعد الفعلي.",
        f"Use {m('d = \\frac{v t}{2}')}.",
        [f"One-way travel time = {m('\\frac{1.6}{2} = 0.8\\text{ s}')}.",
         f"Distance = {m('340 \\times 0.8 = 272\\text{ m}')}."],
        f"Check: round-trip distance is {m('544\\text{ m}')}, so one-way distance is {m('272\\text{ m}')}.",
        f"نستخدم العلاقة {m('d = \\frac{v t}{2}')}.",
        [f"زمن الذهاب وحده = {m('\\frac{1.6}{2} = 0.8\\text{ ث}')}.",
         f"المسافة = {m('340 \\times 0.8 = 272\\text{ م}')}."],
        f"التحقق: المسافة الكلية ذهاباً وإياباً {m('544\\text{ م}')} ونصفها {m('272\\text{ م}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B17",
        f"Green light has wavelength {m('\\lambda = 5.0 \\times 10^{-7}\\text{ m}')} and speed {m('c = 3.0 \\times 10^8\\text{ m/s}')} in vacuum. What is its frequency?",
        f"طول موجة الضوء الأخضر {m('\\lambda = 5.0 \\times 10^{-7}\\text{ م}')} وسرعته في الفراغ {m('c = 3.0 \\times 10^8\\text{ م/ث}')}. ما تردده؟",
        [
            (m(r"6.0 \times 10^{14}\text{ Hz}"), m(r"6.0 \times 10^{14}\text{ هرتز}")),
            (m(r"1.5 \times 10^{15}\text{ Hz}"), m(r"1.5 \times 10^{15}\text{ هرتز}")),
            (m(r"6.0 \times 10^{13}\text{ Hz}"), m(r"6.0 \times 10^{13}\text{ هرتز}")),
            (m(r"1.7 \times 10^{-15}\text{ Hz}"), m(r"1.7 \times 10^{-15}\text{ هرتز}")),
        ],
        "Divide c by λ and subtract exponents carefully: 8 - (-7) = 15.",
        "اقسم سرعة الضوء على الطول الموجي واطرح الأسس بدقة: 8 - (-7) = 15.",
        f"Calculate {m('f = \\frac{c}{\\lambda}')}.",
        [f"Write {m('f = \\frac{3.0 \\times 10^8}{5.0 \\times 10^{-7}} = 0.6 \\times 10^{15}')}.",
         f"Normalize scientific notation: {m('6.0 \\times 10^{14}\\text{ Hz}')}."],
        f"Check: {m('(6.0 \\times 10^{14})(5.0 \\times 10^{-7}) = 30 \\times 10^7 = 3.0 \\times 10^8\\text{ m/s}')}.",
        f"نطبق {m('f = \\frac{c}{\\lambda}')}.",
        [f"القسمة تعطي {m('0.6 \\times 10^{8 - (-7)} = 0.6 \\times 10^{15}')}.",
         f"بالصورة العلمية القياسية = {m('6.0 \\times 10^{14}\\text{ هرتز}')}."],
        f"التحقق: ضرب التردد في الطول الموجي يعيد {m('3.0 \\times 10^8\\text{ م/ث}')}.",
    ))

    # --- HARD (10..14) ---
    d_10 = svg_wave_diagram(2.0, 3.0)
    ar_10 = _ar_svg(d_10, {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"})
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B17",
        "Wave energy transported per second is proportional to the square of wave amplitude (E ∝ A²). If a wave generator triples the amplitude from 1.0 m to 3.0 m at unchanged frequency, by what factor does transmitted energy increase?",
        "تتناسب الطاقة التي تنقلها الموجة طردياً مع مربع سعتها (E ∝ A²). إذا ضاعف مولد موجات السعة ثلاث مرات من 1.0 م إلى 3.0 م مع ثبات التردد، فكم مرة تزداد الطاقة المنقولة؟",
        9, [3, 6, 27],
        "Square the amplitude scale factor (3²).",
        "ربّع عامل تضاعف السعة (3²).",
        f"Evaluate {m('\\frac{E_2}{E_1} = \\left(\\frac{A_2}{A_1}\\right)^2')}.",
        [f"Amplitude ratio = {m('\\frac{3.0}{1.0} = 3')}.",
         f"Energy ratio = {m('3^2 = 9')}."],
        "Check: squaring 3 gives 9 times as much energy.",
        f"نحسب {m('\\frac{E_2}{E_1} = \\left(\\frac{A_2}{A_1}\\right)^2')}.",
        [f"نسبة السعة = {m('3')}.",
         f"نسبة الطاقة = {m('3^2 = 9')} مرات."],
        "التحقق: مربع الثلاثة يساوي 9.",
        diagram_en=d_10, diagram_ar=ar_10,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B17",
        f"Surface waves in a ripple tank travel at {m('1.8\\text{ m/s}')} with wavelength {m('0.6\\text{ m}')} in the deep half. Upon entering the shallow half, speed slows to {m('1.2\\text{ m/s}')}. What is the new wavelength in {m('\\text{m}')}?",
        f"تتحرك موجات سطحية في حوض موجات بسرعة {m('1.8\\text{ م/ث}')} وطول موجي {m('0.6\\text{ م}')} في الجزء العميق. وعند دخولها الجزء الضحل تنخفض سرعتها إلى {m('1.2\\text{ م/ث}')}. ما الطول الموجي الجديد بالمتر؟",
        0.4, [0.9, 0.6, 0.2],
        "Find the unchanged frequency f = 1.8 / 0.6 first, then divide shallow speed by f.",
        "احسب التردد الثابت أولاً (1.8 ÷ 0.6) ثم اقسم السرعة الجديدة عليه.",
        f"Keep {m('f = \\frac{v_1}{\\lambda_1}')} invariant across the boundary.",
        [f"Frequency: {m('f = \\frac{1.8}{0.6} = 3\\text{ Hz}')}.",
         f"Shallow wavelength: {m('\\lambda_2 = \\frac{v_2}{f} = \\frac{1.2}{3} = 0.4\\text{ m}')}."],
        f"Check: wavelength ratio {m('0.4 / 0.6')} matches speed ratio {m('1.2 / 1.8 = 2/3')}.",
        "نحافظ على ثبات التردد عند الانتقال بين العميق والضحل.",
        [f"التردد = {m('\\frac{1.8}{0.6} = 3\\text{ هرتز}')}.",
         f"الطول الموجي الجديد = {m('\\frac{1.2}{3} = 0.4\\text{ م}')}."],
        f"التحقق: النسبة {m('0.4 / 0.6')} تطابق نسبة السرعتين {m('1.2 / 1.8')}.",
        diagram_en=_svg_experiment_bars("Wave Speed Across Depth", "سرعة الموجة حسب العمق", [("Deep", "عميق", 1.8, "1.8 m/s"), ("Shallow", "ضحل", 1.2, "1.2 m/s")], "Speed (m/s)", "السرعة (م/ث)", "en"),
        diagram_ar=_svg_experiment_bars("Wave Speed Across Depth", "سرعة الموجة حسب العمق", [("Deep", "عميق", 1.8, "1.8 m/s"), ("Shallow", "ضحل", 1.2, "1.2 m/s")], "Speed (m/s)", "السرعة (م/ث)", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B17",
        f"A survey ship sends a sonar pulse vertically downward ({m('v_{\\text{water}} = 1,500\\text{ m/s}')}). The top of a sunken ship reflects an echo at {m('0.8\\text{ s}')}, while the flat seafloor beneath it reflects at {m('1.2\\text{ s}')}. How tall in {m('\\text{m}')} does the wreck rise above the seafloor?",
        f"ترسل سفينة مسح نبضة سونار رأسياً نحو الأسفل ({m('v = 1,500\\text{ م/ث}')}). يصل صدى قمة حطام سفينة عند {m('0.8\\text{ ث}')} بينما يصل صدى قاع البحر المسطح عند {m('1.2\\text{ ث}')}. كم يرتفع الحطام بالمتر فوق القاع؟",
        300, [600, 900, 150],
        "Subtract the two round-trip times, divide by 2 for one-way height, and multiply by 1,500 m/s.",
        "اطرح زمني الذهاب والإياب ثم اقسم على 2 واضرب في سرعة الصوت في الماء.",
        f"Compute wreck depth and seafloor depth, or use {m('\\Delta h = \\frac{v(t_2 - t_1)}{2}')}.",
        [f"Wreck top depth: {m('\\frac{1,500 \\times 0.8}{2} = 600\\text{ m}')}; seafloor depth: {m('\\frac{1,500 \\times 1.2}{2} = 900\\text{ m}')}.",
         f"Wreck height = {m('900 - 600 = 300\\text{ m}')}."],
        f"Check: {m('1,500 \\times (1.2 - 0.8) / 2 = 300\\text{ m}')}.",
        f"نحسب عمقي القمة والقاع ثم نجد الفرق بينهما.",
        [f"عمق قمة الحطام = {m('600\\text{ م}')}، وعمق القاع = {m('900\\text{ م}')}.",
         f"ارتفاع الحطام = {m('900 - 600 = 300\\text{ م}')}."],
        f"التحقق: {m('1,500 \\times (1.2 - 0.8) / 2 = 300\\text{ م}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B17",
        "Two identical transverse pulses of amplitude +0.5 m and -0.5 m travel toward each other along a rope and overlap completely for an instant. What occurs during and after the overlap?",
        "تنتقل نبضتان مستعرضتان متطابقتان بسعة +0.5 م و -0.5 م متقابلتين على حبل وتنطبقان كلياً للحظة. ماذا يحدث أثناء الانطباق وبعده؟",
        [
            ("Destructive interference produces a momentarily flat rope, then both pulses emerge unchanged", "تداخل هدام يُسطّح الحبل لحظياً ثم تكمل كل نبضة سيرها دون تغير"),
            ("Both pulses cancel permanently and disappear completely", "تُفني النبضتان بعضهما دائماً وتختفيان كلياً"),
            ("Constructive interference doubles the crest height to +1.0 m", "تداخل بناء يضاعف ارتفاع القمة إلى +1.0 م"),
            ("Both pulses bounce backward without passing through each other", "ترتد كل نبضة للخلف دون أن تمر عبر الأخرى"),
        ],
        "Waves obey superposition: opposite amplitudes cancel while overlapping, then pass right through unaffected.",
        "تخضع الموجات لمبدأ التراكب: تتلاشى السعتان المتعاكستان لحظة التلاقي ثم تستمر كل موجة كأن شيئاً لم يحدث.",
        "Apply destructive interference and wave superposition.",
        ["At complete overlap, displacement sums to +0.5 + (-0.5) = 0 m (destructive interference).",
         "Because energy persists in particle motion, each pulse continues moving onward unchanged."],
        "Energy is conserved even when displacement temporarily cancels.",
        "نطبق التداخل الهدام ومبدأ التراكب.",
        ["عند الانطباق الكامل يكون المجموع الجبري للإزاحتين صفراً (تداخل هدام).",
         "تحتفظ الدقائق بطاقتها الحركية فتواصل النبضتان المرور من خلال بعضهما بلا تغيير."],
        "الطاقة محفوظة حتى لحظة انعدام الإزاحة الظاهرية.",
    ))

    d_14 = svg_wave_diagram(3.0, 0.4)
    ar_14 = _ar_svg(d_14, {"Transverse Wave": "موجة مستعرضة", "Wavelength": "الطول الموجي", "Amplitude": "السعة"})
    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B17",
        f"In a {m('10\\text{ Hz}')} water wave, the horizontal distance from a crest to its immediately adjacent trough is {m('1.5\\text{ m}')}, and the vertical distance from trough bottom to crest top is {m('0.8\\text{ m}')}. What is the wave speed in {m('\\text{m/s}')}?",
        f"في موجة مائية ترددها {m('10\\text{ هرتز}')}، تبلغ المسافة الأفقية بين قمة وقاع مجاور لها مباشرة {m('1.5\\text{ م}')}، والمسافة الرأسية من القاع إلى القمة {m('0.8\\text{ م}')}. ما سرعة الموجة بوحدة {m('\\text{م/ث}')}؟",
        30, [15, 8, 12],
        "Crest-to-adjacent-trough horizontally is half a wavelength (λ/2 = 1.5 m), while vertical span (0.8 m = 2A) does not affect v = fλ.",
        "المسافة الأفقية من القمة إلى القاع المجاور تساوي نصف الطول الموجي (λ/2 = 1.5 م)، ولا يدخل الارتفاع الرأسي في حساب السرعة.",
        f"Double crest-to-trough horizontal spacing to get {m('\\lambda')}, then apply {m('v = f \\lambda')}.",
        [f"Full wavelength: {m('\\lambda = 2 \\times 1.5 = 3.0\\text{ m}')}.",
         f"Speed: {m('v = 10\\text{ Hz} \\times 3.0\\text{ m} = 30\\text{ m/s}')} (amplitude {m('0.4\\text{ m}')} is irrelevant to speed)."],
        "Check: crest-to-crest distance is always twice crest-to-adjacent-trough distance.",
        "نضرب البعد الأفقي في 2 لإيجاد الطول الموجي ثم نضرب في التردد.",
        [f"الطول الموجي الكامل = {m('2 \\times 1.5 = 3.0\\text{ م}')}.",
         f"السرعة = {m('10 \\times 3.0 = 30\\text{ م/ث}')}، والسعة (0.4 م) لا تؤثر في السرعة."],
        "التحقق: البعد بين قمتين متتاليتين ضعف البعد بين قمة وقاع متجاورين.",
        diagram_en=d_14, diagram_ar=ar_14,
    ))

    return qs


def _gen_sci_b18(start_idx: int) -> list[dict]:
    """G9-SCI-B18: Ohm's Law V=IR, Power P=VI, Series & Parallel R_eq, Energy Cost (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = svg_ohm_circuit(12, [4], mode="series")
    ar_0 = _ar_svg(d_0, {"Electric Circuit": "دائرة كهربائية"})
    qs.append(make_science_math_q(
        _qid(start_idx), LEVEL, T_PHYS, _diff(0), "G9-SCI-B18",
        f"A {m('12\\text{ V}')} battery powers a single {m('4\\,\\Omega')} resistor as shown. What current in amperes ({m('\\text{A}')}) flows through the circuit?",
        f"تغذي بطارية جهدها {m('12\\text{ فولت}')} مقاومة وحيدة مقدارها {m('4\\,\\Omega')} كما في الدائرة. ما شدة التيار المار في الدائرة بالأمبير؟",
        3, [48, 8, 16],
        "Apply Ohm's Law: I = V / R.",
        "طبق قانون أوم: شدة التيار = الجهد ÷ المقاومة.",
        f"Use {m('I = \\frac{V}{R}')}.",
        [f"Substitute {m('V = 12\\text{ V}')} and {m('R = 4\\,\\Omega')}.",
         f"Current = {m('\\frac{12}{4} = 3\\text{ A}')}."],
        f"Check: {m('3\\text{ A} \\times 4\\,\\Omega = 12\\text{ V}')}.",
        f"نطبق {m('I = \\frac{V}{R}')}.",
        [f"نعوض {m('V = 12')} و{m('R = 4')}.",
         f"التيار = {m('\\frac{12}{4} = 3\\text{ أمبير}')}."],
        f"التحقق: {m('3 \\times 4 = 12\\text{ فولت}')}.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_PHYS, _diff(1), "G9-SCI-B18",
        f"A steady current of {m('2.5\\text{ A}')} passes through an {m('8\\,\\Omega')} heating element. What potential difference in volts ({m('\\text{V}')}) exists across the element?",
        f"يمر تيار ثابت شدته {m('2.5\\text{ أمبير}')} في عنصر تسخين مقاومته {m('8\\,\\Omega')}. ما فرق الجهد الكهربائي عبره بالفولت؟",
        20, [3.2, 10.5, 16],
        "Multiply current by resistance using V = I × R.",
        "اضرب شدة التيار في المقاومة باستخدام قانون أوم V = I × R.",
        f"Compute {m('V = I R')}.",
        [f"Substitute {m('I = 2.5\\text{ A}')} and {m('R = 8\\,\\Omega')}.",
         f"Voltage = {m('2.5 \\times 8 = 20\\text{ V}')}."],
        f"Check: {m('\\frac{20}{8} = 2.5\\text{ A}')}.",
        f"نطبق {m('V = I R')}.",
        [f"نعوض {m('I = 2.5')} و{m('R = 8')}.",
         f"فرق الجهد = {m('2.5 \\times 8 = 20\\text{ فولت}')}."],
        f"التحقق: {m('\\frac{20}{8} = 2.5\\text{ أمبير}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_PHYS, _diff(2), "G9-SCI-B18",
        f"An electric kettle operates on a {m('220\\text{ V}')} outlet while drawing {m('5\\text{ A}')}. What electrical power in {m('\\text{W}')} does it consume?",
        f"تعمل غلاية كهربائية على مصدر جهد {m('220\\text{ فولت}')} وتسحب تياراً شدته {m('5\\text{ أمبير}')}. ما القدرة الكهربائية المستهلكة بالواط؟",
        1100, [44, 225, 440],
        "Electrical power equals voltage multiplied by current: P = V × I.",
        "القدرة الكهربائية تساوي الجهد مضروباً في شدة التيار: P = V × I.",
        f"Apply {m('P = V I')}.",
        [f"Multiply {m('220\\text{ V} \\times 5\\text{ A}')}.",
         f"Power = {m('1,100\\text{ W}')}."],
        f"Check: {m('\\frac{1,100}{220} = 5\\text{ A}')}.",
        f"نطبق {m('P = V I')}.",
        [f"نضرب {m('220 \\times 5')}.",
         f"القدرة = {m('1,100\\text{ واط}')}."],
        f"التحقق: {m('\\frac{1,100}{220} = 5\\text{ أمبير}')}.",
    ))

    d_3 = svg_ohm_circuit(24, [6, 10], mode="series", title="Series Circuit")
    ar_3 = _ar_svg(d_3, {"Series Circuit": "دائرة على التوالي"})
    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_PHYS, _diff(3), "G9-SCI-B18",
        f"Two resistors of {m('6\\,\\Omega')} and {m('10\\,\\Omega')} are connected in series as illustrated. What is their equivalent total resistance in {m('\\Omega')}?",
        f"وصلت مقاومتان {m('6\\,\\Omega')} و{m('10\\,\\Omega')} على التوالي كما في الشكل. ما المقاومة المكافئة الكلية بوحدة الأوم؟",
        16, [3.75, 4, 60],
        "Resistors in series simply add together: R_eq = R1 + R2.",
        "في التوصيل على التوالي نجمع المقاومات جمعاً مباشراً: R_eq = R1 + R2.",
        f"Add series resistances: {m('R_{\\text{eq}} = R_1 + R_2')}.",
        [f"Compute {m('6 + 10 = 16\\,\\Omega')}."],
        "Check: total series resistance is always greater than either individual resistor.",
        f"نجمع المقاومتين على التوالي.",
        [f"المقاومة المكافئة = {m('6 + 10 = 16\\,\\Omega')}."],
        "التحقق: المقاومة المكافئة على التوالي أكبر دائماً من أكبر مقاومة مفردة.",
        diagram_en=d_3, diagram_ar=ar_3,
    ))

    d_4 = svg_ohm_circuit(12, [6, 6], mode="parallel", title="Parallel Circuit")
    ar_4 = _ar_svg(d_4, {"Parallel Circuit": "دائرة على التوازي"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_PHYS, _diff(4), "G9-SCI-B18",
        "Two identical 6 Ω lamps are wired in parallel across a 12 V battery. If the first lamp's filament burns out and opens its branch, what happens to the second lamp?",
        "وصل مصباحان متطابقان (6 Ω لكل منهما) على التوازي مع بطارية 12 فولت. إذا احترقت فتيلة المصباح الأول وانفتح فرعه، فماذا يحدث للمصباح الثاني؟",
        [
            ("It stays lit at the exact same brightness with 12 V across it", "يبقى مضاءً بالسطوع نفسه تماماً مع استمرار جهد 12 فولت عليه"),
            ("It goes out immediately because the circuit is broken", "ينطفئ فوراً لأن الدائرة انقطعت"),
            ("It shines twice as brightly because it gets double the current", "يزداد سطوعه للضعف لأنه يحصل على ضعف التيار"),
            ("Its brightness drops by half due to higher resistance", "ينخفض سطوعه إلى النصف بسبب زيادة المقاومة"),
        ],
        "Each parallel branch connects directly across the battery terminals independently.",
        "يتصل كل فرع في التوصيل على التوازي مباشرة بقطبي البطارية بصورة مستقلة.",
        "Trace independent current paths in a parallel network.",
        ["Opening branch 1 only interrupts current through lamp 1.",
         "Branch 2 still receives the full 12 V across its fixed 6 Ω resistance, so its current (2 A) and brightness stay unchanged."],
        "This is why home outlets and ceiling lights are wired in parallel.",
        "نتتبع مسارات التيار المستقلة في التوصيل على التوازي.",
        ["انقطاع الفرع الأول يوقف تيار المصباح الأول فقط.",
         "يظل الفرع الثاني متصلاً مباشرة بجهد 12 فولت فتبقى شدة تياره وسطوعه ثابتين."],
        "لهذا السبب تُوصل أجهزة المنزل ومصابيحه على التوازي.",
        diagram_en=d_4, diagram_ar=ar_4,
    ))

    # --- MEDIUM (5..9) ---
    d_5 = svg_ohm_circuit(24, [5, 7], mode="series", title="Series 24 V")
    ar_5 = _ar_svg(d_5, {"Series 24 V": "توالي 24 فولت"})
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_PHYS, _diff(5), "G9-SCI-B18",
        f"In the series circuit shown, a {m('24\\text{ V}')} battery drives current through {m('5\\,\\Omega')} and {m('7\\,\\Omega')} resistors. What current in {m('\\text{A}')} flows from the battery?",
        f"في دائرة التوالي الموضحة، تدفع بطارية {m('24\\text{ فولت}')} تياراً عبر مقاومتين {m('5\\,\\Omega')} و{m('7\\,\\Omega')}. ما شدة التيار الخارج من البطارية بالأمبير؟",
        2, [4.8, 3.43, 12],
        "Add the series resistors first to get R_eq = 12 Ω, then divide 24 V by 12 Ω.",
        "اجمع المقاومتين على التوالي أولاً لتحصل على 12 Ω ثم اقسم 24 فولت على 12 Ω.",
        f"Find {m('R_{\\text{eq}} = R_1 + R_2')}, then compute {m('I = \\frac{V}{R_{\\text{eq}}}')}.",
        [f"Equivalent resistance: {m('R_{\\text{eq}} = 5 + 7 = 12\\,\\Omega')}.",
         f"Circuit current: {m('I = \\frac{24}{12} = 2\\text{ A}')}."],
        f"Check: voltage drops {m('2(5) + 2(7) = 10 + 14 = 24\\text{ V}')}.",
        f"نجد المقاومة المكافئة ثم نطبق قانون أوم.",
        [f"المقاومة المكافئة = {m('5 + 7 = 12\\,\\Omega')}.",
         f"التيار = {m('\\frac{24}{12} = 2\\text{ أمبير}')}."],
        f"التحقق: مجموع الجهدين {m('10 + 14 = 24\\text{ فولت}')}.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    d_6 = svg_ohm_circuit(12, [6, 12], mode="parallel", title="Parallel R_eq")
    ar_6 = _ar_svg(d_6, {"Parallel R_eq": "مكافئة التوازي"})
    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_PHYS, _diff(6), "G9-SCI-B18",
        f"Two resistors of {m('6\\,\\Omega')} and {m('12\\,\\Omega')} are wired in parallel as shown. What is their equivalent resistance in {m('\\Omega')}?",
        f"وصلت مقاومتان {m('6\\,\\Omega')} و{m('12\\,\\Omega')} على التوازي كما في الشكل. ما مقاومتهما المكافئة بوحدة الأوم؟",
        4, [18, 9, 3],
        "Add reciprocals: 1/R_eq = 1/6 + 1/12, then invert the result.",
        "اجمع المقلوبين: 1/R_eq = 1/6 + 1/12 ثم اقلب الكسر الناتج.",
        f"Apply {m('\\frac{1}{R_{\\text{eq}}} = \\frac{1}{R_1} + \\frac{1}{R_2}')}.",
        [f"Sum reciprocals: {m('\\frac{1}{6} + \\frac{1}{12} = \\frac{2 + 1}{12} = \\frac{3}{12} = \\frac{1}{4}')}.",
         f"Invert to obtain {m('R_{\\text{eq}} = 4\\,\\Omega')}."],
        "Check: parallel equivalent resistance (4 Ω) is smaller than the smallest branch resistor (6 Ω).",
        f"نطبق {m('\\frac{1}{R_{\\text{eq}}} = \\frac{1}{6} + \\frac{1}{12}')}.",
        [f"مجموع المقلوبين = {m('\\frac{2}{12} + \\frac{1}{12} = \\frac{3}{12} = \\frac{1}{4}')}.",
         f"بقلب الكسر: {m('R_{\\text{eq}} = 4\\,\\Omega')}."],
        "التحقق: المكافئة على التوازي أصغر دائماً من أصغر مقاومة مفردة.",
        diagram_en=d_6, diagram_ar=ar_6,
    ))

    d_7 = svg_ohm_circuit(18, [6, 9], mode="parallel", title="Parallel Branches")
    ar_7 = _ar_svg(d_7, {"Parallel Branches": "فروع التوازي"})
    qs.append(make_science_math_q(
        _qid(start_idx + 7), LEVEL, T_PHYS, _diff(7), "G9-SCI-B18",
        f"An {m('18\\text{ V}')} battery feeds parallel branches of {m('6\\,\\Omega')} and {m('9\\,\\Omega')}. What total current in {m('\\text{A}')} leaves the battery?",
        f"تغذي بطارية جهدها {m('18\\text{ فولت}')} فرعين متوازيين مقاومتهما {m('6\\,\\Omega')} و{m('9\\,\\Omega')}. ما شدة التيار الكلي الخارج من البطارية بالأمبير؟",
        5, [1.2, 3, 2],
        "Each branch gets full 18 V; find I1 = 18/6 and I2 = 18/9, then add them.",
        "يحصل كل فرع على 18 فولت كاملة؛ احسب تيار كل فرع على حدة ثم اجمعهما.",
        f"Compute {m('I_{\\text{total}} = I_1 + I_2 = \\frac{V}{R_1} + \\frac{V}{R_2}')}.",
        [f"Branch currents: {m('I_1 = \\frac{18}{6} = 3\\text{ A}')} and {m('I_2 = \\frac{18}{9} = 2\\text{ A}')}.",
         f"Total current = {m('3 + 2 = 5\\text{ A}')}."],
        f"Check: {m('R_{\\text{eq}} = \\frac{6 \\times 9}{6 + 9} = 3.6\\,\\Omega')}, and {m('18 / 3.6 = 5\\text{ A}')}.",
        f"نجمع تياري الفرعين {m('I_{\\text{total}} = \\frac{V}{R_1} + \\frac{V}{R_2}')}.",
        [f"تيار الفرع الأول = {m('18/6 = 3\\text{ أمبير}')}، والفرع الثاني = {m('18/9 = 2\\text{ أمبير}')}.",
         f"التيار الكلي = {m('3 + 2 = 5\\text{ أمبير}')}."],
        f"التحقق: المقاومة المكافئة {m('3.6\\,\\Omega')} و{m('18 / 3.6 = 5\\text{ أمبير}')}.",
        diagram_en=d_7, diagram_ar=ar_7,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_PHYS, _diff(8), "G9-SCI-B18",
        f"A steady current of {m('4\\text{ A}')} passes through a {m('15\\,\\Omega')} toaster coil. What thermal power in {m('\\text{W}')} is generated in the coil?",
        f"يمر تيار ثابت شدته {m('4\\text{ أمبير}')} في ملف محمصة مقاومته {m('15\\,\\Omega')}. ما القدرة الحرارية المتولدة في الملف بالواط؟",
        240, [60, 960, 900],
        "Substitute V = IR into P = VI to get P = I² R.",
        "عوض V = IR في قانون القدرة لتحصل على P = I² R.",
        f"Apply {m('P = I^2 R')}.",
        [f"Square the current: {m('4^2 = 16')}.",
         f"Power = {m('16 \\times 15 = 240\\text{ W}')}."],
        f"Check: voltage is {m('V = 4 \\times 15 = 60\\text{ V}')}, and {m('P = 60 \\times 4 = 240\\text{ W}')}.",
        f"نطبق {m('P = I^2 R')}.",
        [f"نربع شدة التيار: {m('4^2 = 16')}.",
         f"القدرة = {m('16 \\times 15 = 240\\text{ واط}')}."],
        f"التحقق: الجهد = {m('60\\text{ فولت}')} و{m('60 \\times 4 = 240\\text{ واط}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_PHYS, _diff(9), "G9-SCI-B18",
        f"A {m('220\\text{ V}')} kitchen circuit is protected by a {m('15\\text{ A}')} circuit breaker. At most how many identical {m('550\\text{ W}')} appliances can run simultaneously in parallel without tripping the breaker?",
        f"دائرة مطبخ جهدها {m('220\\text{ فولت}')} محمية بقاطع تيار أقصاه {m('15\\text{ أمبير}')}. ما أقصى عدد من أجهزة متطابقة قدرة كل منها {m('550\\text{ واط}')} يمكن تشغيلها معاً على التوازي دون فصل القاطع؟",
        6, [5, 7, 15],
        "Compute current per appliance I = P / V = 550 / 220 = 2.5 A, then divide 15 A by 2.5 A.",
        "احسب تيار الجهاز الواحد I = 550 / 220 = 2.5 أمبير، ثم اقسم 15 أمبير على 2.5 أمبير.",
        f"Compare total current limit to individual load current {m('I = \\frac{P}{V}')}.",
        [f"Each appliance draws {m('I_1 = \\frac{550}{220} = 2.5\\text{ A}')}.",
         f"Maximum appliances: {m('\\frac{15}{2.5} = 6')}.",],
        f"Check: maximum circuit power is {m('220 \\times 15 = 3,300\\text{ W}')}, and {m('6 \\times 550 = 3,300\\text{ W}')}.",
        "نقسم الحد الأقصى للقدرة أو التيار على استهلاك الجهاز الواحد.",
        [f"تيار الجهاز الواحد = {m('\\frac{550}{220} = 2.5\\text{ أمبير}')}.",
         f"أقصى عدد = {m('\\frac{15}{2.5} = 6')} أجهزة."],
        f"التحقق: أقصى قدرة للدائرة {m('220 \\times 15 = 3,300\\text{ واط}')} وتساوي {m('6 \\times 550')}.",
    ))

    # --- HARD (10..14) ---
    d_10 = svg_ohm_circuit(30, [4, 6], mode="series", title="Series Power")
    ar_10 = _ar_svg(d_10, {"Series Power": "القدرة على التوالي"})
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_PHYS, _diff(10), "G9-SCI-B18",
        f"In the series circuit shown, a {m('30\\text{ V}')} battery drives current through {m('4\\,\\Omega')} and {m('6\\,\\Omega')} resistors. How much power in {m('\\text{W}')} is dissipated specifically inside the {m('6\\,\\Omega')} resistor?",
        f"في دائرة التوالي الموضحة، تغذي بطارية {m('30\\text{ فولت}')} مقاومتين {m('4\\,\\Omega')} و{m('6\\,\\Omega')}. ما القدرة المستهلكة بالواط داخل المقاومة {m('6\\,\\Omega')} تحديداً؟",
        54, [90, 36, 150],
        "First find series current I = 30 / (4 + 6) = 3 A, then compute P = I² R for the 6 Ω resistor.",
        "أوجد تيار الدائرة أولاً (30 ÷ 10 = 3 أمبير) ثم احسب قدرة مقاومة الـ 6 أوم عبر P = I² R.",
        f"Find circuit current {m('I')}, then calculate {m('P_2 = I^2 R_2')}.",
        [f"Series resistance = {m('4 + 6 = 10\\,\\Omega')}, so current = {m('\\frac{30}{10} = 3\\text{ A}')}.",
         f"Power in {m('6\\,\\Omega')}: {m('P = 3^2 \\times 6 = 54\\text{ W}')}."],
        f"Check: power in {m('4\\,\\Omega')} is {m('36\\text{ W}')}, and total power {m('54 + 36 = 90\\text{ W} = 30 \\times 3')}.",
        "نجد التيار الكلي أولاً لأنه متساوٍ في التوالي ثم نحسب قدرة المقاومة المطلوبة.",
        [f"المقاومة الكلية = {m('10\\,\\Omega')}، والتيار = {m('\\frac{30}{10} = 3\\text{ أمبير}')}.",
         f"القدرة في {m('6\\,\\Omega')} = {m('3^2 \\times 6 = 54\\text{ واط}')}."],
        f"التحقق: مجموع القدرتين {m('54 + 36 = 90\\text{ واط}')} ويساوي {m('30 \\times 3')}.",
        diagram_en=d_10, diagram_ar=ar_10,
    ))

    d_11 = svg_ohm_circuit(12, [4, 12], mode="parallel", title="Parallel Power")
    ar_11 = _ar_svg(d_11, {"Parallel Power": "القدرة على التوازي"})
    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_PHYS, _diff(11), "G9-SCI-B18",
        f"Resistors of {m('4\\,\\Omega')} and {m('12\\,\\Omega')} are connected in parallel across a {m('12\\text{ V}')} battery. What total electrical power in {m('\\text{W}')} do both resistors consume together?",
        f"وصلت مقاومتان {m('4\\,\\Omega')} و{m('12\\,\\Omega')} على التوازي مع بطارية {m('12\\text{ فولت}')}. ما مجموع القدرة الكهربائية المستهلكة في المقاومتين معاً بالواط؟",
        48, [36, 9, 24],
        "Calculate P = V² / R for each parallel branch and add them.",
        "احسب القدرة في كل فرع عبر P = V² / R ثم اجمعهما.",
        f"Compute {m('P_{\\text{total}} = \\frac{V^2}{R_1} + \\frac{V^2}{R_2}')}.",
        [f"Power in {m('4\\,\\Omega')}: {m('\\frac{12^2}{4} = 36\\text{ W}')}; power in {m('12\\,\\Omega')}: {m('\\frac{12^2}{12} = 12\\text{ W}')}.",
         f"Total power = {m('36 + 12 = 48\\text{ W}')}."],
        f"Check: {m('R_{\\text{eq}} = 3\\,\\Omega')}, {m('I = 4\\text{ A}')}, and {m('P = 12 \\times 4 = 48\\text{ W}')}.",
        f"نحسب قدرة كل فرع ثم نجمعهما.",
        [f"قدرة {m('4\\,\\Omega')} = {m('\\frac{144}{4} = 36\\text{ واط}')}، وقدرة {m('12\\,\\Omega')} = {m('12\\text{ واط}')}.",
         f"المجموع = {m('36 + 12 = 48\\text{ واط}')}."],
        f"التحقق: المكافئة {m('3\\,\\Omega')} والتيار الكلي {m('4\\text{ أمبير}')} و{m('12 \\times 4 = 48\\text{ واط}')}.",
        diagram_en=d_11, diagram_ar=ar_11,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_PHYS, _diff(12), "G9-SCI-B18",
        f"A {m('2,500\\text{ W}')} air conditioner runs {m('8\\text{ hours}')} per day for a {m('30\\text{-day}')} month. At a utility tariff of {m('0.18\\text{ SAR/kWh}')}, what is the monthly electricity cost in {m('\\text{SAR}')}?",
        f"يعمل مكيف هواء قدرته {m('2,500\\text{ واط}')} لمدة {m('8\\text{ ساعات}')} يومياً خلال شهر من {m('30\\text{ يوماً}')}. إذا كانت التعرفة {m('0.18\\text{ ريال/كيلوواط}\\cdot\\text{ساعة}')}، فما التكلفة الشهرية بالريال؟",
        108, [3.6, 600, 108000],
        "Convert 2,500 W to 2.5 kW first, multiply by total hours (240 h), then multiply by 0.18 SAR.",
        "حوّل 2,500 واط إلى 2.5 كيلوواط أولاً، ثم اضرب في إجمالي الساعات (240 ساعة) وفي 0.18 ريال.",
        f"Calculate {m('\\text{Energy (kWh)} = P_{\\text{kW}} \\times t_{\\text{h}}')}, then multiply by price.",
        [f"Power in kW: {m('2,500\\text{ W} = 2.5\\text{ kW}')}; total hours: {m('8 \\times 30 = 240\\text{ h}')}.",
         f"Energy used = {m('2.5 \\times 240 = 600\\text{ kWh}')}.",
         f"Cost = {m('600 \\times 0.18 = 108\\text{ SAR}')}."],
        f"Check: daily cost is {m('2.5 \\times 8 \\times 0.18 = 3.60\\text{ SAR}')}, × 30 days = {m('108\\text{ SAR}')}.",
        "نحول القدرة إلى كيلوواط ثم نضرب في الساعات وفي التعرفة.",
        [f"القدرة = {m('2.5\\text{ كيلوواط}')} وعدد الساعات = {m('8 \\times 30 = 240\\text{ ساعة}')}.",
         f"الطاقة المستهلكة = {m('2.5 \\times 240 = 600\\text{ كيلوواط}\\cdot\\text{ساعة}')}.",
         f"التكلفة = {m('600 \\times 0.18 = 108\\text{ ريال}')}."],
        f"التحقق: التكلفة اليومية {m('3.6\\text{ ريال}')} × 30 يوماً = {m('108\\text{ ريال}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_PHYS, _diff(13), "G9-SCI-B18",
        f"Two identical {m('10\\,\\Omega')} resistors are wired in series across a {m('20\\text{ V}')} battery, then rewired in parallel across the same {m('20\\text{ V}')} battery. How many times greater is the battery current in the parallel setup than in the series setup?",
        f"وصلت مقاومتان متطابقتان ({m('10\\,\\Omega')} لكل منهما) على التوالي مع بطارية {m('20\\text{ فولت}')}، ثم أعيد توصيلهما على التوازي مع البطارية نفسها. كم مرة يصبح التيار الكلي في التوازي أكبر منه في التوالي؟",
        4, [2, 8, 10],
        "Compare R_series = 20 Ω vs R_parallel = 5 Ω across the same 20 V voltage.",
        "قارن المقاومة المكافئة في التوالي (20 Ω) مقابل التوازي (5 Ω) مع ثبات الجهد 20 فولت.",
        f"Compute {m('I_{\\text{series}}')} and {m('I_{\\text{parallel}}')} separately.",
        [f"Series: {m('R_s = 10 + 10 = 20\\,\\Omega \\implies I_s = \\frac{20}{20} = 1\\text{ A}')}.",
         f"Parallel: {m('R_p = \\frac{10}{2} = 5\\,\\Omega \\implies I_p = \\frac{20}{5} = 4\\text{ A}')}.",
         f"Current ratio = {m('\\frac{4}{1} = 4')}."],
        "Check: parallel draws 4× current because R_p is one-fourth of R_s.",
        "نحسب التيار في كل حالة على حدة ثم نوجد النسبة.",
        [f"في التوالي: {m('R_s = 20\\,\\Omega')} فالتيار = {m('1\\text{ أمبير}')}.",
         f"في التوازي: {m('R_p = 5\\,\\Omega')} فالتيار = {m('4\\text{ أمبير}')}.",
         f"نسبة التيارين = {m('4')} مرات."],
        "التحقق: انخفضت المقاومة المكافئة للربع فتضاعف التيار 4 مرات.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_PHYS, _diff(14), "G9-SCI-B18",
        f"A {m('3\\,\\Omega')} resistor is wired in series with a parallel combination of {m('4\\,\\Omega')} and {m('12\\,\\Omega')} resistors across an {m('18\\text{ V}')} battery. What voltage in {m('\\text{V}')} appears across the parallel pair?",
        f"وصلت مقاومة {m('3\\,\\Omega')} على التوالي مع فرع توازي مكون من {m('4\\,\\Omega')} و{m('12\\,\\Omega')}، وربطت المجموعة ببطارية {m('18\\text{ فولت}')}. ما فرق الجهد بالفولت بين طرفي مجموعة التوازي؟",
        9, [6, 12, 3],
        "Reduce the parallel pair first (4 || 12 = 3 Ω), find total current (18 / 6 = 3 A), then find V = I × R_p.",
        "احسب مكافئة التوازي أولاً (4 مع 12 = 3 Ω)، ثم احسب التيار الكلي، ثم احسب جهد التوازي.",
        f"Collapse the network step by step using {m('R_p')} then Ohm's Law.",
        [f"Parallel pair: {m('R_p = \\frac{4 \\times 12}{4 + 12} = 3\\,\\Omega')}.",
         f"Total resistance: {m('3 + 3 = 6\\,\\Omega')}; battery current: {m('I = \\frac{18}{6} = 3\\text{ A}')}.",
         f"Voltage across parallel pair: {m('V_p = 3\\text{ A} \\times 3\\,\\Omega = 9\\text{ V}')}."],
        f"Check: remaining {m('3\\text{ A} \\times 3\\,\\Omega = 9\\text{ V}')} drops across the series resistor, summing to {m('18\\text{ V}')}.",
        "نبسط الدائرة بحساب مكافئة التوازي ثم التيار الكلي.",
        [f"مكافئة التوازي = {m('\\frac{4 \\times 12}{4 + 12} = 3\\,\\Omega')}.",
         f"المقاومة الكلية = {m('3 + 3 = 6\\,\\Omega')}، والتيار = {m('3\\text{ أمبير}')}.",
         f"الجهد على التوازي = {m('3 \\times 3 = 9\\text{ فولت}')}."],
        f"التحقق: يتوزع جهد 18 فولت بالتساوي لأن المقاومتين متساويتان (3 و 3 أوم).",
    ))

    return qs



# ==============================================================================
# DOMAIN 4: EARTH & SPACE SCIENCES (G9-SCI-B19 .. G9-SCI-B24, IDs 271 .. 360)
# ==============================================================================

def _gen_sci_b19(start_idx: int) -> list[dict]:
    """G9-SCI-B19: Plate Tectonics, Boundaries, Mantle Convection & Spreading (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = svg_plate_boundary("Convergent")
    ar_0 = _ar_svg(d_0)
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B19",
        "The cross-section illustrates two tectonic plates colliding so one dives beneath the other into the mantle. What type of plate boundary is shown, and which landforms commonly result?",
        "يوضح المقطع تقارب صفيحتين تكتونيتين بحيث تنغرس إحداهما تحت الأخرى في الوشاح. ما نوع الحدود التكتونية الموضحة وما التضاريس التي تنشأ عنها غالباً؟",
        [
            ("Convergent boundary; deep ocean trenches and volcanic mountain arcs", "حدود متقاربة؛ تنشأ عنها أخاديد محيطية عميقة وأقواس جبلية بركانية"),
            ("Divergent boundary; mid-ocean ridges and rift valleys", "حدود متباعدة؛ تنشأ عنها حيد وسط المحيط وأودية الصدع"),
            ("Transform boundary; horizontal strike-slip faults without magma", "حدود تحويلية؛ تنشأ عنها صدوع جانبية دون نشاط بركاني"),
            ("Passive continental margin; flat coastal plains", "حافة قارية خاملة؛ تنشأ عنها سهول ساحلية منبسطة"),
        ],
        "Look at the arrows pushing toward one another and the downward subduction slab.",
        "انظر إلى السهمين المتقابلين وإلى انغراس إحدى الصفيحتين نحو الأسفل.",
        "Match converging arrows and subduction to plate boundary classification.",
        ["Arrows moving toward each other define a convergent boundary.",
         "Subduction forms deep oceanic trenches and melts wet slab rock to feed volcanic arcs."],
        "Notice divergent plates pull apart and transform plates slide sideways.",
        "ترتبط الأسهم المتقابلة وانغراس الصفيحة بحدود التقارب.",
        ["تتحرك الصفيحتان نحو بعضهما فتُعد حدوداً متقاربة.",
         "يُكوّن الانغراس أخاديد عميقة وينصهر جزء من الصفيحة ليغذي براكين."],
        "الحدود المتباعدة تتباعد والتحويلية تنزلق جانبياً.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = svg_earth_layers("Mantle")
    ar_1 = _ar_svg(d_1)
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B19",
        "Which heat-driven mechanism inside Earth's highlighted asthenosphere and mantle primarily sustains slow lithospheric plate motion over millions of years?",
        "ما الآلية الحرارية داخل الوشاح المظلل التي تدعم استمرار حركة الصفائح الليثوسفيرية البطيئة عبر ملايين السنين؟",
        [
            ("Thermal convection currents rising as hot rock and sinking as cooler rock", "تيارات الحمل الحراري حيث تصعد الصخور الساخنة وتهبط الصخور الأبرد"),
            ("Surface ocean tides pulling continental granite across the crust", "مد والجزر المحيطي الذي يسحب القارات فوق القشرة"),
            ("Daily wind friction pushing mountain ranges westward", "احتكاك الرياح اليومية بسلاسل الجبال نحو الغرب"),
            ("Solid iron inner core spinning out into the crust", "اندفاع اللب الداخلي الصلب مباشرة نحو القشرة"),
        ],
        "Heat from Earth's deep interior drives slow ductile flow in the mantle.",
        "الحرارة المنبعثة من باطن الأرض تحرك الصخور اللدنة ببطء في طبقة الوشاح.",
        "Connect mantle thermal gradients to buoyancy-driven convection.",
        ["Deep heating lowers mantle rock density, causing buoyant upwelling beneath ridges.",
         "Cooling near the surface increases density, driving sinking flow back down."],
        "Convection operates in ductile mantle rock over geologic timescales.",
        "يربط التدرج الحراري في الوشاح صعود الصخور الساخنة وهبوط الأبرد.",
        ["تسخين الوشاح السفلي يقلل كثافة الصخور فتصعد ببطء ثم تبرد وتهبط.",
         "تُكوّن هذه الدورة تيارات حمل حراري تحرك الصفائح."],
        "تيارات الحمل في الوشاح هي المحرك الحراري الرئيسي للصفائح.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    d_2 = svg_plate_boundary("Divergent")
    ar_2 = _ar_svg(d_2)
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B19",
        "The diagram shows two lithospheric plates separating as magma wells up between them. Which geologic feature forms along this boundary?",
        "يوضح الشكل صفيحتين تتباعدان بينما تصعد الصهارة بينهما. أي مَعلم جيولوجي يتكوّن على طول هذه الحدود؟",
        [
            ("Mid-ocean ridge or continental rift valley with new basaltic crust", "حيد وسط المحيط أو وادي صدع قاري تتكون فيه قشرة بازلتية جديدة"),
            ("Folded collision mountain belt like the Himalayas", "سلسلة جبال التوائية متصادمة مثل الهيمالايا"),
            ("Deep oceanic subduction trench", "أخدود انغراس محيطي عميق"),
            ("Inactive transform fracture zone", "نطاق صدع تحويلي خامل"),
        ],
        "Diverging plates pull apart, letting magma solidify into brand-new oceanic lithosphere.",
        "تبتعد الصفيحتان عن بعضهما فتصعد الصهارة وتتصلب مكونة قشرة محيطية جديدة.",
        "Associate divergent separation with seafloor spreading and rifting.",
        ["Opposing outward arrows identify a divergent boundary.",
         "Upwelling basaltic magma builds mid-ocean ridges on the ocean floor or rift valleys on land."],
        "Examples include the Mid-Atlantic Ridge and the East African Rift.",
        "نربط الأسهم المتباعدة بتكوّن قشرة جديدة.",
        ["تشير الأسهم المتباعدة إلى حدود تباعد.",
         "تتصلب الصهارة الصاعدة مكونة حيداً محيطياً أو وادي صدع."],
        "مثالها حيد منتصف الأطلسي وصدع البحر الأحمر.",
        diagram_en=d_2, diagram_ar=ar_2,
    ))

    d_3 = svg_plate_boundary("Transform")
    ar_3 = _ar_svg(d_3)
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B19",
        "At the boundary shown, two plates grind horizontally past each other in opposite directions. Which hazard and characteristic belong to this boundary?",
        "في الحدود الموضحة، تنزلق صفيحتان أفقياً بمحاذاة بعضهما في اتجاهين متعاكسين. أي خاصية وظاهرة تميز هذه الحدود؟",
        [
            ("Frequent shallow earthquakes with little or no volcanic activity", "زلازل ضحلة متكررة مع انعدام النشاط البركاني تقريباً"),
            ("Continuous upwelling of basaltic magma creating new seafloor", "صعود مستمر للصهارة يبني قاع محيط جديد"),
            ("Deep-focus earthquakes down to 700 km along a subducting slab", "زلازل عميقة البؤرة تصل إلى 700 كم على امتداد صفيحة منغرسة"),
            ("Rising high folded peaks from continental collision", "ارتفاع قمم جبلية التوائية شاهقة نتيجة تصادم قارتين"),
        ],
        "Crust is neither created nor destroyed at a transform fault — stress builds and snaps along the fault plane.",
        "لا تتكون قشرة جديدة ولا تُستهلك عند الصدوع التحويلية، بل تتراكم الضغوط وتتحرر زلزالياً.",
        "Recognize transform shear motion without magma generation.",
        ["Side-by-side shear motion defines a transform boundary (such as the Dead Sea Transform).",
         "Because plates neither pull open nor subduct deep enough to melt, earthquakes dominate without volcanoes."],
        "Rock friction locks and abruptly slips along transform faults.",
        "تمثل الحركة الجانبية المتعاكسة حدوداً تحويلية.",
        ["تنزلق الصفيحتان جانبياً دون تباعد يفتح القشرة أو انغراس يصهرها.",
         "لذلك تتركز الظواهر في الزلازل الضحلة القوية دون براكين."],
        "يحتبس الإجهاد على الصدع ثم يتحرر فجأة على شكل زلزال.",
        diagram_en=d_3, diagram_ar=ar_3,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B19",
        f"A mid-ocean ridge widens at a total spreading rate of {m('4\\text{ cm/year}')}. By how many meters ({m('\\text{m}')}) does the ocean basin widen over {m('1,000\\text{ years}')}?",
        f"يتسع حيد وسط المحيط بمعدل كلي يبلغ {m('4\\text{ سم/سنة}')}. كم متراً يزداد عرض الحوض المحيطي خلال {m('1,000\\text{ سنة}')}؟",
        40, [4, 400, 4000],
        "Multiply 4 cm/yr by 1,000 years to get cm, then divide by 100 to convert cm to meters.",
        "اضرب 4 سم/سنة في 1,000 سنة للحصول على السنتيمترات ثم اقسم على 100 للتحويل إلى أمتار.",
        f"Compute total cm = rate × time, then convert {m('1\\text{ m} = 100\\text{ cm}')}.",
        [f"Widening in cm: {m('4\\text{ cm/yr} \\times 1,000\\text{ yr} = 4,000\\text{ cm}')}.",
         f"Convert to meters: {m('\\frac{4,000}{100} = 40\\text{ m}')}."],
        "Check: 4 cm is 0.04 m per year, so 0.04 × 1,000 = 40 m.",
        "نحسب المسافة بالسنتيمتر ثم نحولها إلى أمتار.",
        [f"الزيادة = {m('4 \\times 1,000 = 4,000\\text{ سم}')}.",
         f"بالتحويل إلى أمتار = {m('\\frac{4,000}{100} = 40\\text{ م}')}."],
        f"التحقق: {m('0.04\\text{ م/سنة} \\times 1,000\\text{ سنة} = 40\\text{ م}')}.",
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B19",
        "When an oceanic plate converges against a continental plate, why does the oceanic plate consistently subduct beneath the continental plate rather than vice versa?",
        "عندما تتصادم صفيحة محيطية مع صفيحة قارية، لماذا تنغرس الصفيحة المحيطية دائماً أسفل الصفيحة القارية وليس العكس؟",
        [
            ("Basaltic oceanic crust (~3.0 g/cm³) is denser than thicker granitic continental crust (~2.7 g/cm³)", "القشرة المحيطية البازلتية (~3.0 جم/سم³) أعلى كثافة من القشرة القارية الجرانيتية (~2.7 جم/سم³)"),
            ("Continental crust is much thinner and sinks easily into the mantle", "القشرة القارية أرق بكثير فتغوص بسهولة في الوشاح"),
            ("Ocean water pressure forces the oceanic plate downward from above", "ضغط مياه المحيط يدفع الصفيحة المحيطية نحو الأسفل"),
            ("Oceanic plates always travel ten times faster than continental plates", "الصفيحة المحيطية تتحرك دائماً أسرع بعشر مرات من القارية"),
        ],
        "Compare rock mineral density (basalt vs granite) governing buoyancy on the asthenosphere.",
        "قارن كثافة صخر البازلت المحيطي بكثافة الجرانيت القاري فوق الغلاف المائع.",
        "Apply density contrast between oceanic basalt and continental granite.",
        ["Oceanic plates consist mainly of dense mafic basalt (~3.0 g/cm³).",
         "Thick granitic continental crust (~2.7 g/cm³) floats higher on the mantle, forcing the denser oceanic plate underneath."],
        "Denser plates sink at subduction zones.",
        "نطبق مبدأ الطفو واختلاف الكثافة بين نوعي القشرة.",
        ["تتكون القشرة المحيطية من البازلت عالي الكثافة (~3.0 جم/سم³).",
         "تطفو القشرة القارية الجرانيتية الأقل كثافة (~2.7 جم/سم³) وتجبر المحيطية على الانغراس تحتها."],
        "الأعلى كثافة ينغرس دائماً عند مناطق الطرح.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B19",
        f"Ocean floor basalt sampled {m('300\\text{ km}')} east of a mid-ocean ridge axis is dated at {m('10\\text{ million years}')} old. What is the half-spreading rate of the eastern plate in {m('\\text{cm/year}')}?",
        f"عينة بازلت من قاع المحيط تبعد {m('300\\text{ كم}')} شرق محور حيد وسط المحيط قُدّر عمرها بـ {m('10\\text{ مليون سنة}')}. ما معدل انتشار الصفيحة الشرقية بوحدة {m('\\text{سم/سنة}')}؟",
        3, [30, 0.3, 6],
        "Convert 300 km to centimeters (1 km = 100,000 cm), then divide by 10,000,000 years.",
        "حوّل 300 كم إلى سنتيمترات (1 كم = 100,000 سم) ثم اقسم على 10,000,000 سنة.",
        f"Calculate {m('v = \\frac{d}{t}')} after converting km to cm.",
        [f"Distance in cm: {m('300\\text{ km} = 300 \\times 10^5\\text{ cm} = 3 \\times 10^7\\text{ cm}')}.",
         f"Time = {m('10^7\\text{ yr}')}, so rate = {m('\\frac{3 \\times 10^7}{10^7} = 3\\text{ cm/yr}')}."],
        "Check: 3 cm/yr × 10 Myr = 30 million cm = 300 km.",
        "نحول المسافة إلى سنتيمترات ثم نقسمها على العمر بالسنوات.",
        [f"المسافة = {m('300 \\times 100,000 = 3 \\times 10^7\\text{ سم}')}.",
         f"بالتقسيم على {m('10^7\\text{ سنة}')} نحصل على {m('3\\text{ سم/سنة}')}."],
        f"التحقق: {m('3\\text{ سم/سنة} \\times 10\\text{ مليون سنة} = 300\\text{ كم}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B19",
        "The Zagros Mountains formed as the Arabian Plate pushed northward into the Eurasian Plate (two continental crusts colliding). Why do tall folded mountains and strong earthquakes occur there with almost no active volcanoes?",
        "تشكلت جبال زاجروس مع اندفاع الصفيحة العربية شمالاً نحو الصفيحة الأوراسية (تصادم قاري-قاري). لماذا تنشأ جبال التوائية وزلازل قوية مع ندرة البراكين النشطة في هذا التصادم؟",
        [
            ("Both buoyant continental crusts resist deep subduction, crumpling upward instead of melting into magma", "كلتا الصفيحتين القاريتين خفيفتا الكثافة فتقاومان الانغراس العميق وتنثنيان للأعلى دون انصهار بركاني"),
            ("Continental granite cannot melt at any mantle temperature", "الجرانيت القاري لا ينصهر عند أي درجة حرارة في باطن الأرض"),
            ("Water from the ocean cools all magma beneath continental collisions", "مياه المحيط تبرد كل الصهارة تحت مناطق التصادم القاري"),
            ("The Arabian Plate actually slides sideways in a purely transform motion", "الصفيحة العربية تنزلق جانبياً فقط في حركة تحويلية بحتة"),
        ],
        "Magma arcs require wet oceanic crust subducting deep into the mantle; low-density continents collide and thicken instead.",
        "تتطلب البراكين انغراس قشرة محيطية رطبة بعمق في الوشاح؛ أما القارتان فتتراكبان وتنثنيان لقلة كثافتهما.",
        "Compare continental-continental collision to oceanic subduction.",
        ["Continental lithosphere has too low a density to sink deeply into the mantle.",
         "Instead, crustal shortening folds rock layers upward into high ranges while crustal faults generate frequent quakes."],
        "The same process built the Himalayas between India and Eurasia.",
        "نقارن التصادم القاري بانغراس القشرة المحيطية.",
        ["تمنع الكثافة المنخفضة للقارات انغراس إحداهما عميقاً في الوشاح.",
         "تنضغط الطبقات وتلتوي لأعلى مكونة جبالاً شاهقة وزلازل دون قوس بركاني."],
        "الآلية نفسها كوّنت جبال الهيمالايا.",
    ))

    d_8 = svg_plate_boundary("Divergent", title="Red Sea Rift")
    ar_8 = _ar_svg(d_8, {"Red Sea Rift": "صدع البحر الأحمر"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B19",
        "Geologically, the Red Sea is a young, widening ocean basin separating Saudi Arabia from northeastern Africa. What tectonic setting explains its origin and ongoing widening?",
        "جيولوجياً يُعد البحر الأحمر حوضاً محيطياً ناشئاً ومتسعاً يفصل شبه الجزيرة العربية عن شمال شرق أفريقيا. ما الوضع التكتوني المفسر لنشأته واستمرار اتساعه؟",
        [
            ("A divergent plate boundary pulling the Arabian Plate northeastward away from the African Plate", "حدود تباعد تفصل الصفيحة العربية شمال شرق بعيداً عن الصفيحة الأفريقية"),
            ("A convergent subduction trench swallowing Africa beneath Arabia", "أخدود انغراس يبتلع أفريقيا تحت شبه الجزيرة العربية"),
            ("A transform fault sliding Arabia south without forming new crust", "صدع تحويلي يزيح العربية جنوباً دون تكوين قشرة جديدة"),
            ("Erosion from seasonal desert rivers carving a deep trench", "تعرية الأنهار الموسمية التي حفرت أخدوداً عميقاً"),
        ],
        "New basaltic ocean floor is erupting along the central axial trough of the Red Sea as two plates drift apart.",
        "تندفع قشرة بازلتية جديدة في المحور الأوسط للبحر الأحمر مع تباعد الصفيحتين العربية والأفريقية.",
        "Link the widening axial trough of the Red Sea to divergent rifting.",
        ["Crustal rifting split the Afro-Arabian shield and created an axial seafloor-spreading ridge.",
         "Ongoing divergence pushes the Arabian Plate northeastward toward Eurasia."],
        "Geologists study the Red Sea as a modern analog for how the Atlantic Ocean began opening.",
        "نربط اتساع قاع البحر الأحمر بحدود التباعد القاري والمحيطي.",
        ["أدى التصدع التباعدي إلى انشقاق الدرع العربي الأفريقي وظهور حيد بحري وسطي.",
         "يستمر التباعد دافعاً الصفيحة العربية نحو الشمال الشرقي."],
        "يدرس الجيولوجيون البحر الأحمر كنموذج حي لبداية نشأة المحيطات.",
        diagram_en=d_8, diagram_ar=ar_8,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B19",
        "Magnetometer surveys across mid-ocean ridges reveal symmetric zebra-like stripes of normal and reversed magnetic polarity on opposite sides of the ridge. What does this evidence confirm?",
        "كشفت المسوحات المغناطيسية عبر حيد وسط المحيط عن أشرطة متماثلة من القطبية المغناطيسية العادية والمعكوسة على جانبي الحيد. ماذا يؤكد هذا الدليل؟",
        [
            ("New oceanic crust forms symmetrically at the ridge and spreads outward as Earth's magnetic field periodically reverses", "تتشكل قشرة محيطية جديدة بانتظام عند الحيد وتتباعد للجانبين مع انعكاس المجال المغناطيسي للأرض دورياً"),
            ("Ocean currents align iron grains after rocks solidify", "تيارات المحيط ترتب حبيبات الحديد بعد تصلب الصخور"),
            ("Subduction occurs directly along the top of mid-ocean ridges", "يحدث الانغراس مباشرة على قمة حيد وسط المحيط"),
            ("Earth's gravity reverses direction every few million years", "جاذبية الأرض تنعكس في اتجاهها كل بضعة ملايين من السنين"),
        ],
        "Cooling basalt locks in the magnetic north direction existing at the moment magma solidifies at the ridge crest.",
        "تحتفظ الصخور البازلتية عند تبردها باتجاه المجال المغناطيسي السائد لحظة تصلبها عند الحيد.",
        "Interpret mirror-image seafloor magnetic anomalies.",
        ["As magma erupts and cools at the ridge crest, iron-bearing minerals align with Earth's active dipole polarity.",
         "Split equally left and right by seafloor spreading, each polarity reversal creates matching mirror bands."],
        "Vine and Matthews (1963) used magnetic stripes as decisive proof of seafloor spreading.",
        "نفسر التماثل المغناطيسي المرآتي على جانبي الحيد.",
        ["عند تصلب الصهارة البازلتية تتجمد المعادن الحديدية باتجاه المجال المغناطيسي آنذاك.",
         "مع التباعد المتماثل على الجانبين والانعكاسات الدورية تتكون أشرطة متناظرة."],
        "تعد الأشرطة المغناطيسية الدليل الحاسم على توسع قاع المحيط.",
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B19",
        f"A chain of volcanic islands forms as a tectonic plate drifts over a stationary mantle hotspot. An extinct volcanic island lies {m('480\\text{ km}')} from the active hotspot volcano and formed {m('12\\text{ million years}')} ago. What is the plate's speed in {m('\\text{cm/year}')}?",
        f"تتشكل سلسلة جزر بركانية مع تحرك صفيحة تكتونية فوق بقعة ساخنة ثابتة في الوشاح. تقع جزيرة بركانية خامدة على مسافة {m('480\\text{ كم}')} من البركان النشط وقد تكونت قبل {m('12\\text{ مليون سنة}')}. ما سرعة حركة الصفيحة بوحدة {m('\\text{سم/سنة}')}؟",
        4, [40, 0.4, 12],
        "Convert 480 km to cm (× 100,000) and divide by 12,000,000 years.",
        "حوّل 480 كم إلى سنتيمترات (× 100,000) ثم اقسم على 12,000,000 سنة.",
        f"Divide hotspot track length by volcano age: {m('v = \\frac{d}{t}')}.",
        [f"Distance = {m('480 \\times 10^5 = 4.8 \\times 10^7\\text{ cm}')}.",
         f"Age = {m('1.2 \\times 10^7\\text{ yr}')}, so plate speed = {m('\\frac{4.8}{1.2} = 4\\text{ cm/yr}')}."],
        f"Check: {m('4\\text{ cm/yr} \\times 12\\text{ Myr} = 48\\text{ million cm} = 480\\text{ km}')}.",
        "نقسم طول المسار البركاني على عمر الجزيرة الخامدة.",
        [f"المسافة = {m('480 \\times 10^5 = 4.8 \\times 10^7\\text{ سم}')}.",
         f"السرعة = {m('\\frac{4.8 \\times 10^7}{1.2 \\times 10^7} = 4\\text{ سم/سنة}')}."],
        f"التحقق: {m('4 \\times 12 = 48\\text{ مليون سم} = 480\\text{ كم}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B19",
        f"Two continents approach each other across an ocean trench: the western plate moves east at {m('3.5\\text{ cm/year}')} and the eastern plate moves west at {m('2.5\\text{ cm/year}')}. At these steady speeds, in how many million years will a {m('600\\text{ km}')} wide sea between them close completely?",
        f"تقترب قارتان عبر أخدود محيطي: تتحرك الصفيحة الغربية شرقاً بسرعة {m('3.5\\text{ سم/سنة}')} وتتحرك الشرقية غرباً بسرعة {m('2.5\\text{ سم/سنة}')}. بعد كم مليون سنة سينغلق بحر عرضه {m('600\\text{ كم}')} بينهما كلياً؟",
        10, [17.1, 24, 1],
        "Add their speeds (3.5 + 2.5 = 6.0 cm/yr) because they move in opposite closing directions.",
        "اجمع السرعتين (3.5 + 2.5 = 6.0 سم/سنة) لأنهما تتحركان نحو بعضهما، ثم اقسم 600 كم بالسنتيمتر عليه.",
        "Compute relative closing rate, then divide ocean width by closing rate.",
        [f"Closing speed = {m('3.5 + 2.5 = 6.0\\text{ cm/yr}')}.",
         f"Width = {m('600\\text{ km} = 60,000,000\\text{ cm}')}.",
         f"Time = {m('\\frac{60,000,000}{6.0} = 10,000,000\\text{ yr} = 10\\text{ Myr}')}."],
        f"Check: western plate covers {m('350\\text{ km}')} and eastern plate covers {m('250\\text{ km}')}, totaling {m('600\\text{ km}')}.",
        "نحسب سرعة الاقتراب النسبية ثم نقسم المسافة عليها.",
        [f"سرعة الاقتراب النسبية = {m('3.5 + 2.5 = 6.0\\text{ سم/سنة}')}.",
         f"العرض = {m('60\\text{ مليون سم}')}، فالزمن = {m('\\frac{60}{6} = 10\\text{ مليون سنة}')}."],
        f"التحقق: تقطع الأولى {m('350\\text{ كم}')} والثانية {m('250\\text{ كم}')} ومجموعهما {m('600\\text{ كم}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B19",
        "Plates with long, cold subducting edges (like the Pacific Plate) travel several times faster than plates lacking large subduction zones (like the African Plate). Which mechanism explains this velocity difference?",
        "تتحرك الصفائح ذات الحواف المنغرسة الطويلة والباردة (كالصفيحة الهادئة) أسرع بعدة مرات من الصفائح التي تفتقر لمناطق طرح كبيرة (كالصفيحة الأفريقية). أي آلية تفسر هذا الفارق في السرعة؟",
        [
            ("Slab pull: cold, dense subducting lithosphere sinks into the mantle and pulls the trailing plate behind it", "سحب الصفيحة (Slab Pull): الصفيحة الباردة الكثيفة المنغرسة تغوص في الوشاح وتسحب بقية الصفيحة خلفها"),
            ("Ocean currents around the Pacific push the rock faster", "تيارات المحيط الهادئ المائية تدفع الصخر بسرعة أكبر"),
            ("Solar heating melts the Pacific crust and speeds up sliding", "التسخين الشمسي يصهر قشرة المحيط الهادئ ويسرّع انزلاقها"),
            ("Transform faults accelerate plates magnetically along mid-ocean ridges", "الصدوع التحويلية تسرّع الصفائح مغناطيسياً عند الحيد"),
        ],
        "Compare the strength of slab pull from dense sinking slabs against ridge push.",
        "قارن قوة سحب الصفيحة المنغرسة (Slab Pull) بقوة دفع الحيد (Ridge Push).",
        "Identify slab pull as the dominant plate-driving force.",
        ["Old oceanic lithosphere becomes cold and denser than the underlying asthenosphere.",
         "As it sinks at a trench, gravitational slab pull exerts a huge tensional drag that accelerates the entire plate."],
        "Geodynamic models show slab pull accounts for most of observed plate speed.",
        "نحدد سحب الصفيحة الكثيفة المنغرسة بوصفه القوة السائدة.",
        ["تصبح الصفيحة المحيطية القديمة باردة وأعلى كثافة من الغلاف المائع أسفلها.",
         "عند غوصها في الأخدود تسحب بقوة جاذبية هائلة كامل الصفيحة المتصلة بها."],
        "الصفائح المرتبطة بمناطق طرح واسعة هي الأسرع حركة على الأرض.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B19",
        "A global seismic catalog reveals earthquakes occurring along an inclined plane reaching depths of 650 km beneath an island arc, whereas mid-ocean ridge quakes stop above 30 km depth. What accounts for the 650 km deep earthquakes?",
        "يُظهر سجل الزلازل العالمي بؤراً زلزالية تمتد على مستوى مائل حتى عمق 650 كم تحت قوس جزر، بينما لا تتجاوز زلازل حيد وسط المحيط عمق 30 كم. ما سبب حدوث الزلازل على عمق 650 كم؟",
        [
            ("Brittle cold oceanic lithosphere remains rigid enough to fracture as it subducts deep into the mantle", "بقاء الصفيحة المحيطية الباردة هشة وصلبة بما يكفي للانكسار أثناء انغراسها عميقاً في الوشاح"),
            ("Hot liquid magma chambers explode at 650 km depth along the outer core", "انفجار غرف صهارة سائلة على عمق 650 كم قرب اللب الخارجي"),
            ("Thick granite roots of continents fracture inside mid-ocean ridges", "انكسار جذور القارات الجرانيتية السميكة داخل حيد وسط المحيط"),
            ("Tidal friction from the Moon cracks rock only below 500 km", "احتكاك المد القمري يكسر الصخور فقط أسفل عمق 500 كم"),
        ],
        "Normally mantle rock flows plastically below ~50 km, so brittle fracture at 650 km requires cold subducted rock (Wadati-Benioff zone).",
        "تنساب صخور الوشاح لدونةً تحت 50 كم عادة، لذا يستلزم الانكسار على عمق 650 كم وجود صخر بارد منغرس.",
        "Explain the inclined Wadati-Benioff seismic zone at subduction trenches.",
        ["At mid-ocean ridges, upwelling asthenosphere keeps brittle crust very thin (<30 km).",
         "In subduction zones, cold surface lithosphere plunges rapidly into the mantle before warming up, fracturing down to ~670 km."],
        "Deep-focus earthquakes map out the exact angle of the descending slab.",
        "نفسر نطاق واداتي-بينيوف الزلزالي المائل في مناطق الطرح.",
        ["عند الحيد المحيطي تسخن الصهارة الصاعدة القشرة فتبقى الطبقة القابلة للكسر رقيقة.",
         "أما في الانغراس فتهبط الصفيحة الباردة سريعاً قبل أن تسخن فتتصدع حتى عمق 670 كم تقريباً."],
        "ترسم البؤر الزلزالية العميقة زاوية ميل الصفيحة المنغرسة بدقة.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B19",
        f"Each side of an ocean rift moves away from the central ridge axis at {m('1.2\\text{ cm/year}')} (a total full spreading rate of {m('2.4\\text{ cm/year}')}). If the ocean floor between the two coasts is {m('240\\text{ km}')} wide, for how many million years has seafloor spreading formed this basin?",
        f"يبتعد كل جانب من جانبي صدع بحري عن المحور الأوسط بسرعة {m('1.2\\text{ سم/سنة}')} (بمعدل اتساع كلي {m('2.4\\text{ سم/سنة}')}). إذا بلغ عرض قاع البحر بين الساحلين {m('240\\text{ كم}')}، فكم مليون سنة استغرق تكوّن هذا الحوض؟",
        10, [20, 5, 12],
        "Divide total width 240 km (24,000,000 cm) by total spreading rate 2.4 cm/yr (or half-width 120 km by 1.2 cm/yr).",
        "اقسم العرض الكلي 240 كم (24 مليون سم) على معدل الاتساع الكلي 2.4 سم/سنة (أو نصف العرض 120 كم على 1.2 سم/سنة).",
        f"Match full basin width to full spreading rate: {m('t = \\frac{W}{v_{\\text{total}}}')}.",
        [f"Convert width: {m('240\\text{ km} = 2.4 \\times 10^7\\text{ cm}')}.",
         f"Divide by total spreading rate {m('2.4\\text{ cm/yr}')}: {m('t = \\frac{2.4 \\times 10^7}{2.4} = 10^7\\text{ yr} = 10\\text{ Myr}')}."],
        "Check: half-width 120 km / 1.2 cm/yr also equals 10 Myr.",
        "نطابق العرض الكلي مع المعدل الكلي للتوسع.",
        [f"العرض = {m('240\\text{ كم} = 2.4 \\times 10^7\\text{ سم}')}.",
         f"الزمن = {m('\\frac{2.4 \\times 10^7}{2.4} = 10\\text{ مليون سنة}')}."],
        "التحقق: نصف العرض 120 كم على نصف المعدل 1.2 سم/سنة يعطي النتيجة نفسها (10 ملايين سنة).",
    ))

    return qs


def _gen_sci_b20(start_idx: int) -> list[dict]:
    """G9-SCI-B20: Earthquakes, P/S Wave Lag, Outer Core, Volcanoes & Tsunamis (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = _svg_seismogram(12, 32, "en")
    ar_0 = _svg_seismogram(12, 32, "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B20",
        "On the seismogram shown, P-waves arrive before S-waves. Which statement accurately compares seismic P-waves and S-waves?",
        "في مخطط السيزموجرام الموضح تصل الموجات الأولية P قبل الموجات الثانوية S. أي عبارة تقارن بينهما مقارنة صحيحة؟",
        [
            ("P-waves are faster longitudinal compression waves passing through solids and liquids; S-waves are slower transverse waves passing only through solids", "الموجات P أسرع وتضاغطية طولية تمر بالصلب والسائل، أما S فأبطأ ومستعرضة تمر بالصلب فقط"),
            ("S-waves are longitudinal waves traveling faster than P-waves through the outer core", "الموجات S طولية وتنتقل أسرع من P عبر اللب الخارجي"),
            ("Both P-waves and S-waves travel exclusively along Earth's surface crust", "تنتقل موجات P وS حصرياً على سطح القشرة الأرضية فقط"),
            ("P-waves cannot pass through liquids, whereas S-waves pass freely through liquids", "لا تمر موجات P بالسوائل بينما تمر موجات S بالسوائل بحرية"),
        ],
        "P stands for Primary (first/fastest compressional); S stands for Secondary (slower shear/transverse, blocked by liquids).",
        "ترمز P إلى الأولية التضاغطية الأسرع النافذة في الصلب والسائل، وS إلى الثانوية المستعرضة المحجوبة بالسوائل.",
        "Contrast wave speed, oscillation mode, and liquid transmission.",
        ["P-waves arrive first at 12 s because compression travels fastest and propagates in solids and fluids.",
         "S-waves rely on shear rigidity, so liquids cannot transmit them and they lag behind."],
        "Surface waves arrive last and cause the strongest shaking.",
        "نقارن السرعة وطريقة الاهتزاز والنفاذ في السوائل.",
        ["تصل P أولاً عند 12 ث لأنها تضاغطية سريعة وتنتقل في الصلب والسائل.",
         "تعتمد S على قص الصخور الصلبة لذا تتأخر ولا تمر عبر السوائل."],
        "الموجات السطحية تصل أخيراً وتسبب أكبر دمار.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = _svg_seismogram(15, 40, "en")
    ar_1 = _svg_seismogram(15, 40, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B20",
        f"A seismic station records the first P-wave arrival at {m('15\\text{ s}')} and the first S-wave arrival at {m('40\\text{ s}')} on the seismogram. What is the S–P arrival time lag ({m('\\Delta t')}) in seconds?",
        f"رصدت محطة زلازل وصول الموجة الأولية P عند الثانية {m('15\\text{ ث}')} ووصول الموجة الثانوية S عند الثانية {m('40\\text{ ث}')}. ما الفارق الزمني ({m('\\Delta t')}) بين وصولهما بالثانية؟",
        25, [55, 15, 40],
        "Subtract P-wave arrival time from S-wave arrival time: t_S - t_P.",
        "اطرح زمن وصول الموجة P من زمن وصول الموجة S: t_S - t_P.",
        f"Compute {m('\\Delta t = t_S - t_P')}.",
        [f"Substitute {m('t_S = 40\\text{ s}')} and {m('t_P = 15\\text{ s}')}.",
         f"Lag = {m('40 - 15 = 25\\text{ s}')}."],
        f"Check: {m('15 + 25 = 40\\text{ s}')}.",
        f"نحسب {m('\\Delta t = t_S - t_P')}.",
        [f"نعوض {m('t_S = 40')} و{m('t_P = 15')}.",
         f"الفارق الزمني = {m('40 - 15 = 25\\text{ ث}')}."],
        f"التحقق: {m('15 + 25 = 40\\text{ ث}')}.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    d_2 = svg_earth_layers("Outer Core")
    ar_2 = _ar_svg(d_2)
    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B20",
        "After a large earthquake, stations across the opposite side of Earth detect P-waves but record a complete S-wave shadow zone (no direct S-waves). Which property of the highlighted Outer Core does this prove?",
        "بعد زلزال كبير، ترصد المحطات في الجهة المقابلة من الأرض موجات P ولكنها تسجل منطقة ظل كاملة تخلو من موجات S المباشرة. ما الصفة الفيزيائية للّب الخارجي المظلل التي يثبتها هذا الرصد؟",
        [
            ("The Outer Core is liquid, blocking transverse S-waves", "اللب الخارجي سائل مما يمنع مرور موجات S المستعرضة"),
            ("The Outer Core is frozen solid iron", "اللب الخارجي حديد صلب متجمد بالكامل"),
            ("Earth's Mantle absorbs all seismic waves completely", "يمتص الوشاح جميع الموجات الزلزالية كلياً"),
            ("The Outer Core consists purely of low-density gas", "يتكون اللب الخارجي من غازات منخفضة الكثافة فقط"),
        ],
        "Recall which physical state of matter blocks shear (transverse) S-waves while still transmitting P-waves.",
        "تذكر أي حالة فيزيائية للمادة تحجب موجات القص المستعرضة S بينما تسمح بمرور موجات P.",
        "Connect the S-wave shadow zone to shear modulus zero in liquids.",
        ["Liquids cannot sustain shear stress, so S-waves vanish upon entering Earth's Outer Core.",
         "Meanwhile P-waves refract through the liquid iron-nickel alloy and re-emerge."],
        "Seismic tomography remains our primary tool for probing Earth's deep interior.",
        "نربط منطقة ظل موجات S بطبيعة السوائل التي لا تنقل موجات القص.",
        ["السوائل لا تقاوم قوى القص فتختفي موجات S فور دخولها اللب الخارجي.",
         "بالمقابل تنكسر موجات P داخل الحديد والنيكل السائلين وتواصل طريقها."],
        "الموجات الزلزالية هي الأداة الأساسية لاكتشاف بنية باطن الأرض.",
        diagram_en=d_2, diagram_ar=ar_2,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B20",
        "What is the minimum number of geographically separated seismic recording stations required to pinpoint the unique location of an earthquake's epicenter on Earth's surface?",
        "ما أقل عدد من محطات الرصد الزلزالي المتباعدة اللازم لتحديد الموقع الوحيد والدقيق للمركز السطحي للزلزال؟",
        3, [1, 2, 4],
        "Each station draws one distance circle; two circles still intersect at two points, so another circle is needed.",
        "ترسم كل محطة دائرة بعد؛ تتقاطع دائرتان في نقطتين، لذا نحتاج دائرة ثالثة لحسم نقطة التقاطع الوحيدة.",
        "Apply circle intersection geometry (triangulation).",
        ["1 station gives a circle of possible epicenters; 2 circles narrow it to 2 points.",
         "A 3rd non-collinear station intersects at the single exact epicenter."],
        "Check: triangulation always needs at least 3 distance radii.",
        "نستخدم هندسة تقاطع الدوائر (التثليث).",
        ["محطة واحدة تعطي دائرة، ومحطتان تتقاطعان في نقطتين، فتأتي المحطة الثالثة لتحديد نقطة تقاطع وحيدة هي المركز السطحي."],
        "التحقق: يتطلب التثليث المساحي 3 محطات على الأقل.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B20",
        "How do shield volcanoes (such as Mauna Loa) differ from composite volcanoes (such as Mount Fuji) in lava viscosity and eruption style?",
        "كيف تختلف البراكين الدرعية عن البراكين المركبة من حيث لزوجة اللابة ونمط الثوران؟",
        [
            ("Shield volcanoes erupt fluid low-silica basalt quietly forming broad gentle slopes; composite volcanoes erupt thick high-silica magma explosively forming steep cones", "البراكين الدرعية تقذف لابة بازلتية قليلة السيليكا قليلة اللزوجة بهدوء وتكوّن منحدرات لطيفة؛ والمركبة تقذف صهارة عالية السيليكا ولزجة بعنف وتكوّن مخاريط شديدة الانحدار"),
            ("Shield volcanoes form steep cones from explosive ash layers; composite volcanoes form flat sheets", "البراكين الدرعية تبني مخاريط حادة من الرماد المتفجر، والمركبة تبني هضاباً منبسطة"),
            ("Both volcano types erupt exclusively high-viscosity rhyolite magma", "كلا النوعين يقذف صهارة ريوليتية شديدة اللزوجة فقط"),
            ("Composite volcanoes never produce pyroclastic ash flows", "البراكين المركبة لا تنتج سحباً بركانية أو رماداً مطلقاً"),
        ],
        "Silica content controls magma viscosity: low silica flows easily like syrup/water; high silica traps gas violently.",
        "تتحكم نسبة السيليكا باللزوجة: السيليكا القليلة تعطي لابة سائلة هادئة، والعالية تحبس الغازات وتنفجر.",
        "Link magma silica & viscosity to volcano cone shape.",
        ["Basaltic magma has ~50% silica, flows far sideways, and releases gas calmly -> broad shield profile.",
         "Andesitic/rhyolitic magma (>60% silica) traps gas under high pressure -> explosive layers of lava and ash (composite cone)."],
        "Harrat Rahat in western Saudi Arabia features extensive fluid basaltic lava fields.",
        "نربط نسبة السيليكا باللزوجة وبشكل المخروط البركاني.",
        ["اللابة البازلتية منخفضة السيليكا تنساب لمسافات بعيدة فتصنع بركاناً درعياً عريضاً قليل الميل.",
         "الصهارة الغنية بالسيليكا عالية اللزوجة تحبس الغازات فتنفجر وتراكم طبقات رماد ولابة بمخروط حاد."],
        "اللزوجة المنخفضة تصنع مخاريط درعية عريضة واللزوجة العالية تصنع براكين مركبة متفجرة.",
    ))

    # --- MEDIUM (5..9) ---
    d_5 = _svg_seismogram(10, 25, "en")
    ar_5 = _svg_seismogram(10, 25, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B20",
        f"Suppose crustal P-waves travel at {m('6\\text{ km/s}')} and S-waves travel at {m('3\\text{ km/s}')}. If the S–P arrival lag on a station's seismogram is {m('15\\text{ s}')}, how far away in {m('\\text{km}')} is the earthquake focus?",
        f"بافتراض أن سرعة موجات P في القشرة {m('6\\text{ كم/ث}')} وسرعة موجات S تساوي {m('3\\text{ كم/ث}')}، إذا بلغ الفارق الزمني بين وصولهما {m('15\\text{ ث}')}، فكم يبعد بؤرة الزلزال بالكيلومتر؟",
        90, [45, 135, 60],
        "Set t_S - t_P = d/3 - d/6 = 15 s and solve for distance d.",
        "اكتب معادلة الفارق الزمني d/3 - d/6 = 15 ث وحل لإيجاد المسافة d.",
        f"Solve {m('\\frac{d}{v_S} - \\frac{d}{v_P} = \\Delta t')}.",
        [f"Substitute speeds: {m('\\frac{d}{3} - \\frac{d}{6} = 15')}.",
         f"Combine fractions: {m('\\frac{2d - d}{6} = \\frac{d}{6} = 15 \\implies d = 90\\text{ km}')}."],
        f"Check: P-wave takes {m('90/6 = 15\\text{ s}')}; S-wave takes {m('90/3 = 30\\text{ s}')}; lag = {m('30 - 15 = 15\\text{ s}')}.",
        f"نحل {m('\\frac{d}{3} - \\frac{d}{6} = 15')}.",
        [f"نوحد المقامات: {m('\\frac{2d - d}{6} = 15')}.",
         f"إذن {m('\\frac{d}{6} = 15')} ومنها {m('d = 90\\text{ كم}')}."],
        f"التحقق: زمن P = {m('15\\text{ ث}')} وزمن S = {m('30\\text{ ث}')} والفرق {m('15\\text{ ث}')}.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B20",
        f"On the standard Richter scale, each increase of {m('+1.0')} magnitude unit multiplies maximum seismic ground-wave amplitude by {m('10')}. How many times larger is the wave amplitude of a magnitude {m('6.0')} earthquake than a magnitude {m('4.0')} earthquake?",
        f"في مقياس ريختر القياسي، تضاعف كل زيادة بمقدار {m('+1.0')} درجة سعة الموجة الزلزالية بمقدار {m('10')} مرات. كم مرة تزيد سعة موجة زلزال قوته {m('6.0')} عن سعة زلزال قوته {m('4.0')}؟",
        100, [20, 2, 1000],
        "Subtract magnitudes (6.0 - 4.0 = 2 steps), then compute 10².",
        "اطرح الدرجتين (6.0 - 4.0 = خطوتان) ثم احسب 10².",
        f"Multiply amplitude factor {m('10')} once per magnitude step: {m('10^{\\Delta M}')}.",
        [f"Magnitude difference: {m('\\Delta M = 6.0 - 4.0 = 2')}.",
         f"Amplitude ratio: {m('10^2 = 100')}."],
        "Check: magnitude 5 is 10× magnitude 4, and magnitude 6 is 10× magnitude 5 (10 × 10 = 100).",
        "نرفع الأساس 10 لأس فرق الدرجتين.",
        [f"الفرق في الدرجة = {m('6.0 - 4.0 = 2')}.",
         f"نسبة السعة = {m('10^2 = 100')} مرة."],
        "التحقق: الدرجة 5 تزيد 10 مرات عن 4، والدرجة 6 تزيد 10 مرات عن 5، أي 100 مرة.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B20",
        "In seismology reports, how is an earthquake's focus (hypocenter) distinguished from its epicenter?",
        "في التقارير الزلزالية، ما الفرق الدقيق بين بؤرة الزلزال ومركزه السطحي؟",
        [
            ("The focus is the underground fault rupture point where seismic waves originate; the epicenter is the surface point directly above it", "البؤرة هي نقطة تكسر الصخور تحت الأرض حيث تنشأ الموجات؛ والمركز السطحي هو النقطة على سطح الأرض فوقها عمودياً"),
            ("The epicenter is deep inside the mantle, whereas the focus is on Earth's surface", "المركز السطحي داخل الوشاح العميق بينما البؤرة على سطح الأرض"),
            ("The focus emits only S-waves while the epicenter emits only P-waves", "تطلق البؤرة موجات S فقط بينما يطلق المركز السطحي موجات P فقط"),
            ("Both terms refer to the exact same location at sea level", "المصطلحان يشيران إلى النقطة نفسها عند مستوى سطح البحر"),
        ],
        "Note the prefix 'epi-' (above/upon) in epicenter: directly above the underground focus.",
        "البؤرة تقع في الأعماق عند مكان الانكسار، أما المركز السطحي فعلى السطح فوقها مباشرة.",
        "Contrast subsurface rupture origin vs surface geographic projection.",
        ["Rock slips at depth along a fault plane — that 3D point is the focus.",
         "Projecting vertically straight up to the ground yields the epicenter plotted on maps."],
        "Shallow-focus earthquakes usually produce stronger shaking at the epicenter than deep ones of equal magnitude.",
        "نميز بين موقع الانكسار الجوفي وإسقاطه على السطح.",
        ["تتحرر الطاقة عند نقطة الانزلاق داخل باطن الأرض (البؤرة).",
         "النقطة الواقعة على السطح فوقها عمودياً هي المركز السطحي المحدد على الخرائط."],
        "الزلازل ذات البؤرة الضحلة تسبب غالباً اهتزازاً أشد عند المركز السطحي.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B20",
        f"A seismic P-wave propagates through deep bedrock at {m('8\\text{ km/s}')} from an earthquake located {m('240\\text{ km}')} away. How many seconds after the fault slips does the first P-wave reach the station?",
        f"تنتقل موجة زلزالية أولية P عبر صخور الأساس العميقة بسرعة {m('8\\text{ كم/ث}')} من زلزال يبعد {m('240\\text{ كم}')}. بعد كم ثانية من حدوث الكسر تصل أول موجة P إلى المحطة؟",
        30, [1920, 20, 48],
        "Divide distance by speed: t = d / v.",
        "اقسم المسافة على السرعة: الزمن = المسافة ÷ السرعة.",
        f"Calculate {m('t = \\frac{d}{v_P}')}.",
        [f"Substitute {m('d = 240\\text{ km}')} and {m('v_P = 8\\text{ km/s}')}.",
         f"Travel time = {m('\\frac{240}{8} = 30\\text{ s}')}."],
        f"Check: {m('8\\text{ km/s} \\times 30\\text{ s} = 240\\text{ km}')}.",
        f"نطبق {m('t = \\frac{d}{v_P}')}.",
        [f"نقسم {m('240\\text{ كم}')} على {m('8\\text{ كم/ث}')}.",
         f"الزمن = {m('30\\text{ ث}')}."],
        f"التحقق: {m('8 \\times 30 = 240\\text{ كم}')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B20",
        "Why do magma chambers rich in both dissolved water vapor and silica (greater than 65% SiO₂) produce far more violent volcanic eruptions than low-silica basaltic magmas?",
        "لماذا تسبب الصهارة الغنية ببخار الماء المذاب والسيليكا (أكثر من 65%) ثورانات بركانية أعنف بكثير من الصهارة البازلتية منخفضة السيليكا؟",
        [
            ("High silica makes magma thick and viscous, trapping expanding gas bubbles until pressure triggers an explosive blast", "ترفع السيليكا لزوجة الصهارة فتحتبس فقاعات الغاز المتمددة حتى يرتفع الضغط وتنفجر بعنف"),
            ("Water vapor freezes magma into solid ice inside the volcano vent", "يجمد بخار الماء الصهارة إلى جليد صلب داخل فوهة البركان"),
            ("Silica reacts chemically with oxygen in the atmosphere to burn continuously", "تتفاعل السيليكا كيميائياً مع الأكسجين الجوي لتشتعل باستمرار"),
            ("High silica decreases magma viscosity so gas bubbles race outward too fast", "تخفض السيليكا العالية لزوجة الصهارة فتندفع الفقاعات للخارج بسرعة"),
        ],
        "Silica tetrahedra link into long chains inside magma, thickening it like cold honey and trapping pressurized gas.",
        "تربط السيليكا السلاسل الجزيئية فتزداد اللزوجة كالعسل الكثيف وتُحبس الغازات المضغوطة حتى تنفجر.",
        "Connect silica polymerization -> high viscosity -> trapped volatiles -> explosivity.",
        ["Higher silica content creates long silicate chains, sharply increasing magma viscosity.",
         "Because gas bubbles cannot escape gently through thick magma, pressure spikes until rock shatters explosively."],
        "Compare opening a shaken soda bottle vs a calm cup of water.",
        "نربط السيليكا باللزوجة واحتباس الغازات المذابة.",
        ["تُكوّن السيليكا المرتفعة سلاسل تزيد لزوجة الصهارة وتعيق تصاعد فقاعات الغاز.",
         "يتراكم ضغط الغاز المحبوس ثم ينفجر دفعة واحدة محطماً الصخور إلى رماد."],
        "يشبه ذلك فتح زجاجة مشروب غازي مضغوطة مقارنة بسكب ماء هادئ.",
    ))

    # --- HARD (10..14) ---
    d_10 = _svg_seismogram(35, 45, "en")
    ar_10 = _svg_seismogram(35, 45, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B20",
        f"A monitoring clock starts at {m('t = 0\\text{ s}')}. An earthquake occurs at unknown origin time {m('t_0')}, sending P-waves at {m('6\\text{ km/s}')} and S-waves at {m('4\\text{ km/s}')}. The seismogram records P arrival at {m('35\\text{ s}')} and S arrival at {m('45\\text{ s}')}. At what clock time {m('t_0')} in seconds did the earthquake actually rupture?",
        f"تبدأ ساعة الرصد من {m('t = 0\\text{ ث}')}. وقع زلزال عند لحظة مجهولة {m('t_0')}، فأطلق موجات P بسرعة {m('6\\text{ كم/ث}')} وموجات S بسرعة {m('4\\text{ كم/ث}')}. سجل السيزموجرام وصول P عند {m('35\\text{ ث}')} وS عند {m('45\\text{ ث}')}. عند أي ثانية {m('t_0')} بدأ الزلزال فعلياً؟",
        15, [10, 20, 5],
        "First find distance d from Δt = 45 - 35 = 10 s (d/4 - d/6 = 10 -> d = 120 km), then subtract P travel time (120/6) from t_P = 35 s.",
        "أوجد المسافة d أولاً من الفارق 10 ث (d/4 - d/6 = 10 فتكون d = 120 كم)، ثم اطرح زمن سفر P من لحظة وصولها 35 ث.",
        "Solve distance from lag Δt, compute P travel duration, then subtract from arrival clock time.",
        [f"Lag {m('\\Delta t = 45 - 35 = 10\\text{ s}')}; solve {m('\\frac{d}{4} - \\frac{d}{6} = \\frac{d}{12} = 10 \\implies d = 120\\text{ km}')}.",
         f"P-wave travel time = {m('\\frac{120}{6} = 20\\text{ s}')}.",
         f"Origin time {m('t_0 = 35 - 20 = 15\\text{ s}')}."],
        f"Check: S-wave travel time is {m('120/4 = 30\\text{ s}')}, and {m('15 + 30 = 45\\text{ s}')}.",
        "نحسب المسافة من الفارق الزمني ثم نطرح زمن سفر P من ساعة الوصول.",
        [f"الفارق الزمني = {m('10\\text{ ث}')}، ومنها {m('\\frac{d}{12} = 10')} أي {m('d = 120\\text{ كم}')}.",
         f"زمن سفر P = {m('120 / 6 = 20\\text{ ث}')}، إذن لحظة حدوث الزلزال = {m('35 - 20 = 15\\text{ ث}')}."],
        f"التحقق: زمن سفر S يساوي {m('30\\text{ ث}')} و{m('15 + 30 = 45\\text{ ث}')}.",
        diagram_en=d_10, diagram_ar=ar_10,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B20",
        f"Every increase of {m('+1.0')} step on the seismic moment magnitude scale multiplies total radiated seismic energy by about {m('32')}. Approximately how many times more energy does a magnitude {m('7.0')} earthquake release than a magnitude {m('5.0')} earthquake?",
        f"كل زيادة بمقدار {m('+1.0')} درجة على مقياس العزم الزلزالي تضاعف الطاقة الزلزالية المتحررة بنحو {m('32')} مرة. بكم مرة تقريباً تفوق طاقة زلزال قوته {m('7.0')} طاقة زلزال قوته {m('5.0')}؟",
        1024, [64, 100, 200],
        "A +2.0 magnitude difference multiplies energy by 32 × 32 (not 2 × 32).",
        "زيادة بمقدار درجتين (+2.0) تضاعف الطاقة بمقدار 32 × 32 وليس 2 × 32.",
        f"Compute {m('32^{\\Delta M}')} for {m('\\Delta M = 2')}.",
        [f"Magnitude difference = {m('7.0 - 5.0 = 2.0')}.",
         f"Energy ratio = {m('32 \\times 32 = 1,024')}."],
        "Check: roughly 1,000 times more energy for every 2.0 units of magnitude.",
        "نرفع عامل الطاقة 32 لأس فرق الدرجتين.",
        [f"الفرق في القوة = {m('7.0 - 5.0 = 2.0')}.",
         f"نسبة الطاقة = {m('32^2 = 1,024')} مرة."],
        "التحقق: كل درجتين على مقياس الزلازل تعنيان نحو ألف ضعف من الطاقة.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B20",
        "Why do submarine megathrust earthquakes at subduction trenches frequently trigger devastating tsunamis, whereas equal-magnitude submarine strike-slip (transform) earthquakes rarely produce large tsunamis?",
        "لماذا تسبب الزلازل البحرية في أخاديد الطرح أمواج تسونامي مدمرة غالباً، بينما نادراً ما تسبب زلازل الصدوع التحويلية البحرية ذات القوة نفسها تسونامي كبيراً؟",
        [
            ("Subduction thrusting violently lifts or drops a huge block of seafloor vertically, displacing the entire overlying ocean water column", "دفع الانغراس يرفع أو يخفض كتلة هائلة من قاع البحر رأسياً فيزيح عمود الماء بأكمله فوقها"),
            ("Transform faults absorb ocean water underground into mantle magma", "الصدوع التحويلية تمتص مياه المحيط تحت الأرض نحو الصهارة"),
            ("Subduction faults move slower than ocean tides so waves grow steadily", "تتحرك صدوع الانغراس أبطأ من المد البحري فتكبر الموجة ببطء"),
            ("Strike-slip faults cannot generate P-waves through seawater", "الصدوع التحويلية لا تولد موجات أولية P في مياه البحر"),
        ],
        "To push an ocean-wide tsunami wave upward, seafloor rock must shift vertically up or down.",
        "لرفع موجة تسونامي عابرة للمحيط لا بد من إزاحة رأسية مفاجئة لقاع البحر ترفع عمود الماء.",
        "Contrast vertical dip-slip vs horizontal strike-slip seafloor displacement.",
        ["Thrust faulting during subduction snaps the overriding plate vertically by meters over hundreds of kilometers.",
         "Horizontal grinding along a transform fault displaces very little vertical water volume."],
        "Vertical ocean-floor displacement transfers gravitational potential energy directly to the ocean surface.",
        "نقارن الإزاحة الرأسية لقاع البحر بالإزاحة الأفقية الجانبية.",
        ["انفلات الصفيحة في مناطق الطرح يرفع القاع أو يخفضه أمتاراً عمودياً فيدفع كامل عمود الماء.",
         "أما الانزلاق الأفقي في الصدع التحويلي فلا يزيح حجم ماء كبيراً للأعلى."],
        "الشرط الحاسم لتوليد التسونامي هو تغير منسوب قاع البحر رأسياً فجأة.",
    ))

    d_13 = svg_earth_layers("Outer Core", title="Seismic Core Refraction")
    ar_13 = _ar_svg(d_13, {"Seismic Core Refraction": "انكسار الموجات في اللب"})
    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B20",
        "Even though P-waves CAN travel through liquids, seismometers between 104° and 140° angular distance from an epicenter detect no direct P-waves (the P-wave shadow zone). What causes this ring-shaped gap?",
        "رغم قدرة موجات P على المرور في السوائل، لا ترصد المحطات الواقعة بين 104° و140° بُعداً زاوياً عن المركز السطحي أي موجات P مباشرة (منطقة ظل P). ما سبب هذه الفجوة الحلقية؟",
        [
            ("P-waves slow down abruptly and bend inward (refract) upon entering the denser liquid Outer Core", "تنخفض سرعة موجات P فجأة وتنكسر للداخل عند دخولها اللب الخارجي السائل"),
            ("P-waves bounce backward completely off the top of the Crust", "ترتد موجات P بالكامل من أعلى طبقة القشرة الأرضية"),
            ("The solid Inner Core destroys all P-waves that touch its surface", "يحطم اللب الداخلي الصلب كل موجات P التي تلامسه"),
            ("P-waves speed up to infinite velocity in liquid iron", "تزداد سرعة موجات P إلى ما لا نهاية داخل الحديد السائل"),
        ],
        "When a wave crosses into a layer where its speed drops sharply, refraction bends rays inward away from 104°–140°.",
        "عندما تعبر موجة إلى وسط تنخفض فيه سرعتها فجأة، تنكسر أشعتها للداخل تاركة نطاقاً دون وصول مباشر.",
        "Apply wave refraction at the mantle–outer-core boundary.",
        ["P-wave speed jumps downward across the boundary from rigid mantle rock into liquid iron Outer Core.",
         "By Snell's law, rays touching the core bend sharply inward and emerge beyond 140°, leaving 104°–140° silent."],
        "Both the P-wave shadow zone and S-wave shadow zone independently constrain the Outer Core radius (~2,900 km depth).",
        "نطبق انكسار الموجات عند الحد بين الوشاح واللب الخارجي.",
        ["تهبط سرعة موجات P بحدة عند دخولها الحديد المنصهر في اللب الخارجي.",
         "نتيجة الانكسار تنحني الأشعة للداخل وتخرج بعد زاوية 140° فتنشأ منطقة ظل بين 104° و140°."],
        "أسهمت مناطق الظل في تحديد عمق اللب الخارجي بدقة (~2,900 كم).",
        diagram_en=d_13, diagram_ar=ar_13,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B20",
        f"Using a simplified local travel-time rule {m('d = 8\\text{ km/s} \\times \\Delta t')}, Seismic Station A records an S–P lag of {m('8\\text{ s}')} while Station B records an S–P lag of {m('12\\text{ s}')}. By how many kilometers ({m('\\text{km}')}) is the triangulation circle drawn around Station B larger in radius than Station A's circle?",
        f"وفق قاعدة مبسطة محلية للمسافة {m('d = 8\\text{ كم/ث} \\times \\Delta t')}، سجلت المحطة أ فارقاً زمنياً {m('8\\text{ ث}')} وسجلت المحطة ب فارقاً زمنياً {m('12\\text{ ث}')}. بكم كيلومتر يزيد نصف قطر دائرة البعد حول المحطة ب عن دائرة المحطة أ؟",
        32, [64, 96, 4],
        "Multiply the difference in S-P lag (12 - 8 = 4 s) by 8 km/s.",
        "اضرب الفرق بين الفارقين الزمنيين (12 - 8 = 4 ث) في 8 كم/ث.",
        f"Compute {m('r_B - r_A = 8(\\Delta t_B - \\Delta t_A)')}.",
        [f"Station A radius: {m('8 \\times 8 = 64\\text{ km}')}; Station B radius: {m('8 \\times 12 = 96\\text{ km}')}.",
         f"Difference = {m('96 - 64 = 32\\text{ km}')}."],
        f"Check: {m('8\\text{ km/s} \\times 4\\text{ s} = 32\\text{ km}')}.",
        "نحسب نصف قطر دائرة كل محطة ثم نطرحهما.",
        [f"نصف قطر أ = {m('64\\text{ كم}')}، ونصف قطر ب = {m('96\\text{ كم}')}.",
         f"الفرق = {m('96 - 64 = 32\\text{ كم}')}."],
        f"التحقق: {m('8 \\times (12 - 8) = 32\\text{ كم}')}.",
    ))

    return qs


def _gen_sci_b21(start_idx: int) -> list[dict]:
    """G9-SCI-B21: Rock Cycle, Superposition, Cross-Cutting & Half-Life Dating (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B21",
        "During the rock cycle, which sequence of geological processes transforms exposed granite into a clastic sedimentary rock such as sandstone?",
        "في دورة الصخور، ما تسلسل العمليات الجيولوجية الذي يحول الجرانيت المنكشف على السطح إلى صخر رسوبي فتاتي كالحجر الرملي؟",
        [
            ("Weathering, erosion, deposition, compaction, and cementation", "التجوية، فالتعرية، فالترسيب، فالتراص، فالتلاحم"),
            ("Complete melting into magma followed by slow cooling underground", "الانصهار التام إلى صهارة ثم التبريد البطيء تحت السطح"),
            ("Intense regional heat and directed pressure without melting", "حرارة إقليمية شديدة وضغط موجه دون انصهار"),
            ("Rapid crystallization of volcanic lava underwater", "التبلور السريع للابة البركانية تحت سطح البحر"),
        ],
        "Clastic sedimentary rocks require breaking existing rock into grains, moving them, burying them, and gluing them.",
        "تتكون الصخور الرسوبية الفتاتية بتفتيت الصخر ونقله وترسيبه ثم رصه ولحمه.",
        "Match surface breakdown and lithification to sedimentary rock formation.",
        ["Weathering breaks granite into quartz/feldspar sand grains; erosion transports them to a basin.",
         "Deposition, burial compaction, and mineral cementation bind the grains into sandstone."],
        "Melting produces igneous rock; solid-state recrystallization produces metamorphic rock.",
        "نرتب خطوات تكوّن الصخور الرسوبية في الدورة الصخرية.",
        ["تفتت التجوية الصخر، وتنقله التعرية، ثم يترسب في أحواض منخفضة.",
         "تحت ثقل الرواسب يتراص الفتات ويتلاحم بالمعادن المذابة ليصير صخراً رسوبياً."],
        "الانصهار يعطي صخوراً نارية والتحول بالضغط والحرارة يعطي صخوراً متحولة.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B21",
        "In an undisturbed vertical canyon wall, horizontal rock strata are stacked from bottom to top as Shale (lowest), Limestone, Sandstone, and Siltstone (highest). By the Law of Superposition, which layer is the oldest?",
        "في جدار وادٍ غير مضطرب، تتراكب طبقات أفقية من الأسفل إلى الأعلى: طفل صفحي (الأدنى)، فحجر جيري، فحجر رملي، فغرين (الأعلى). حسب مبدأ تعاقب الطبقات، أي طبقة هي الأقدم؟",
        [
            ("Shale, at the bottom of the sequence", "الطفل الصفحي في أسفل التتابع الطبقي"),
            ("Siltstone, at the top of the sequence", "صخر الغرين في أعلى التتابع"),
            ("Sandstone, near the middle of the wall", "الحجر الرملي في منتصف الجدار"),
            ("All four layers formed on the exact same day", "تكونت الطبقات الأربع جميعها في الوقت نفسه"),
        ],
        "In undisturbed sedimentary beds, newer sediments always settle on top of previously deposited layers.",
        "في الطبقات الرسوبية غير المقلوبة، تترسب الطبقة الأحدث دائماً فوق الطبقة الأقدم منها.",
        "Apply Steno's Law of Superposition.",
        ["Gravity deposits successive sediment layers from bottom upward.",
         "Therefore, the bottom layer (Shale) was laid down first and is oldest."],
        "Remember: only intense tectonic overturning can invert superposition.",
        "نطبق قانون تعاقب الطبقات (التراكب).",
        ["تتراكم الرواسب أفقياً من الأسفل إلى الأعلى بمرور الزمن.",
         "إذن الطبقة السفلى (الطفل الصفحي) هي الأقدم."],
        "العكس لا يحدث إلا إذا طوت الحركات التكتونية الطبقات وقلبتها.",
        diagram_en=_svg_rock_strata([("Siltstone", "غرين", "#CBD5E1"), ("Sandstone", "حجر رملي", "#FDE68A"), ("Limestone", "حجر جيري", "#E2E8F0"), ("Shale", "طفل صفحي", "#94A3B8")], None, "en"),
        diagram_ar=_svg_rock_strata([("Siltstone", "غرين", "#CBD5E1"), ("Sandstone", "حجر رملي", "#FDE68A"), ("Limestone", "حجر جيري", "#E2E8F0"), ("Shale", "طفل صفحي", "#94A3B8")], None, "ar"),
    ))

    d_2 = _svg_half_life(160, 5730, "yr", "سنة", 2, "en")
    ar_2 = _svg_half_life(160, 5730, "yr", "سنة", 2, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B21",
        f"A fossil wood sample initially held {m('160\\text{ g}')} of a radioactive isotope whose half-life is {m('5,730\\text{ years}')}. As shown on the decay chart, how many grams ({m('\\text{g}')}) of the original parent isotope remain after {m('11,460\\text{ years}')}?",
        f"احتوت عينة خشب أحفوري في البداية على {m('160\\text{ جم}')} من نظير مشع عمر نصفه {m('5,730\\text{ سنة}')}. كما في المخطط، كم جراماً من النظير المشع الأصلي يتبقى بعد مرور {m('11,460\\text{ سنة}')}؟",
        40, [80, 20, 120],
        "Divide total time 11,460 by half-life 5,730 to find k = 2 half-lives, then halve 160 twice.",
        "اقسم الزمن الكلي 11,460 على عمر النصف 5,730 لتجد عدد الفترات (2)، ثم نصّف 160 جم مرتين.",
        f"Apply {m('N = N_0 \\left(\\frac{1}{2}\\right)^k')}.",
        [f"Number of half-lives: {m('k = \\frac{11,460}{5,730} = 2')}.",
         f"Remaining mass: {m('160 \\times \\left(\\frac{1}{2}\\right)^2 = \\frac{160}{4} = 40\\text{ g}')}."],
        f"Check: after 1 half-life {m('80\\text{ g}')}; after 2 half-lives {m('40\\text{ g}')}.",
        f"نطبق قانون الاضمحلال {m('N = N_0 \\left(\\frac{1}{2}\\right)^k')}.",
        [f"عدد أنصاف العمر = {m('\\frac{11,460}{5,730} = 2')}.",
         f"المتبقي = {m('160 \\div 4 = 40\\text{ جم}')}."],
        f"التحقق: بعد فترة نصف عمر {m('80\\text{ جم}')}، وبعد فترتين {m('40\\text{ جم}')}.",
        diagram_en=d_2, diagram_ar=ar_2,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B21",
        "Granite and basalt share similar bulk chemical compositions in some settings, yet granite shows coarse visible crystals while basalt has microscopic grains. What explains granite's larger crystal size?",
        "يمتلك الجرانيت بلورات كبيرة مرئية بالعين بينما يمتلك البازلت حبيبات دقيقة مجهرية. ما العامل الذي يفسر كبر حجم بلورات الجرانيت؟",
        [
            ("Granite cooled slowly deep underground, giving atoms ample time to grow large crystals", "تبرّد الجرانيت ببطء شديد في الأعماق مما أتاح للذرات وقتاً طويلاً لنمو بلورات كبيرة"),
            ("Granite erupted explosively into cold ocean water", "اندفع الجرانيت بانفجار مفاجئ إلى مياه المحيط الباردة"),
            ("Granite was compressed from sand dunes in a desert", "انضغط الجرانيت من كثبان رملية صحراوية"),
            ("Basalt cooled over millions of years inside the lower mantle", "تبرّد البازلت عبر ملايين السنين داخل الوشاح السفلي"),
        ],
        "Slow intrusive cooling lets ions migrate into large crystal lattices; fast extrusive cooling freezes crystals small.",
        "التبريد البطيء تحت السطح يسمح بتجمع الأيونات في بلورات كبيرة، والتبريد السريع على السطح يعطي بلورات دقيقة.",
        "Relate igneous cooling rate to mineral crystal texture.",
        ["Magma insulated deep inside Earth's crust cools over thousands of years, forming coarse intrusive textures (granite).",
         "Lava exposed at the surface loses heat rapidly, yielding fine-grained extrusive textures (basalt)."],
        "Obsidian (volcanic glass) cools so fast that almost no crystals form at all.",
        "نربط معدل التبريد الناري بحجم البلورات.",
        ["الصهارة المحبوسة عميقاً في القشرة تبرد ببطء فتتكون بلورات كبيرة متداخلة (صخر ناري جوفي).",
         "اللابة المتدفقة على السطح تبرد سريعاً فتكون بلورات مجهرية دقيقة (صخر ناري سطحي)."],
        "السبج (الزجاج البركاني) يتصلب بسرعة فائقة فلا تتشكل فيه بلورات أصلاً.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B21",
        f"A mineral grain originally contained {m('100\\text{ g}')} of a radioactive isotope and now contains only {m('12.5\\text{ g}')}. How many half-lives have elapsed?",
        f"احتوت حبة معدن في الأصل على {m('100\\text{ جم}')} من نظير مشع ولم يتبقَّ منها الآن سوى {m('12.5\\text{ جم}')}. كم فترة نصف عمر قد مضت؟",
        3, [2, 4, 8],
        "Keep dividing 100 by 2 until reaching 12.5, and count the halving steps.",
        "اقسم 100 جم على 2 مراراً حتى تصل إلى 12.5 جم ثم عدّ مرات القسمة.",
        f"Solve {m('\\left(\\frac{1}{2}\\right)^k = \\frac{12.5}{100}')}.",
        [f"Fraction remaining: {m('\\frac{12.5}{100} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3')}.",
         f"Therefore {m('k = 3')} half-lives have elapsed."],
        f"Check step by step: {m('100 \\to 50 \\to 25 \\to 12.5\\text{ g}')} (3 steps).",
        "نحسب نسبة المتبقي ونحولها إلى قوة للعدد نصف.",
        [f"النسبة = {m('\\frac{12.5}{100} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3')}.",
         f"إذن عدد فترات نصف العمر = {m('3')}."],
        f"التحقق: {m('100 \\to 50 \\to 25 \\to 12.5')} في 3 خطوات.",
    ))

    # --- MEDIUM (5..9) ---
    d_5 = _svg_half_life(80, 40, "Myr", "م.س", 3, "en")
    ar_5 = _svg_half_life(80, 40, "Myr", "م.س", 3, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B21",
        f"An isotope with a half-life of {m('40\\text{ million years}')} decayed from an initial {m('80\\text{ g}')} down to {m('10\\text{ g}')}, as plotted. How old is the rock in millions of years?",
        f"اضمحل نظير مشع عمر نصفه {m('40\\text{ مليون سنة}')} من كتلة ابتدائية {m('80\\text{ جم}')} إلى {m('10\\text{ جم}')} كما في المخطط. ما عمر الصخر بملايين السنين؟",
        120, [80, 160, 40],
        "Determine how many times 80 halves to reach 10 (k = 3), then multiply 3 by 40 Myr.",
        "احسب عدد مرات تنصيف 80 للوصول إلى 10 (3 مرات)، ثم اضرب 3 × 40 مليون سنة.",
        "Find k first, then multiply k × half-life.",
        [f"Decay sequence: {m('80 \\to 40 \\to 20 \\to 10\\text{ g}')}, which is {m('k = 3')} half-lives.",
         f"Age = {m('3 \\times 40 = 120\\text{ million years}')}."],
        f"Check: {m('80 / 2^3 = 80 / 8 = 10\\text{ g}')}.",
        "نجد عدد أنصاف العمر ثم نضرب في قيمة نصف العمر الواحد.",
        [f"المسار: {m('80 \\to 40 \\to 20 \\to 10\\text{ جم}')}، أي {m('3')} فترات نصف عمر.",
         f"العمر = {m('3 \\times 40 = 120\\text{ مليون سنة}')}."],
        f"التحقق: {m('80 \\div 8 = 10\\text{ جم}')}.",
        diagram_en=d_5, diagram_ar=ar_5,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B21",
        f"A granite intrusion begins with {m('200\\text{ g}')} of radioactive parent isotope X (half-life {m('50\\text{ million years}')}) and zero daughter isotope Y. How many grams ({m('\\text{g}')}) of stable daughter isotope Y exist after {m('150\\text{ million years}')}?",
        f"يبدأ تداخل ناري من الجرانيت بـ {m('200\\text{ جم}')} من نظير أب مشع X (عمر نصفه {m('50\\text{ مليون سنة}')}) وصفر جرام من النظير الابن Y. كم جراماً من النظير الابن المستقر Y يتجمع بعد {m('150\\text{ مليون سنة}')}؟",
        175, [25, 150, 50],
        "Be careful: the question asks for the DAUGHTER mass (initial 200 g minus remaining parent), not remaining parent.",
        "انتبه: المطلوب كتلة النظير الابن المتكوّن (200 جم ناقص المتبقي من الأب)، وليس المتبقي من الأب نفسه.",
        f"Find remaining parent {m('N')} after {m('k = 3')} half-lives, then compute {m('D = N_0 - N')}.",
        [f"Number of half-lives: {m('k = \\frac{150}{50} = 3')}.",
         f"Remaining parent X: {m('\\frac{200}{2^3} = \\frac{200}{8} = 25\\text{ g}')}.",
         f"Accumulated daughter Y: {m('200 - 25 = 175\\text{ g}')}."],
        f"Check: parent + daughter mass stays conserved ({m('25 + 175 = 200\\text{ g}')}).",
        "نحسب المتبقي من النظير الأب بعد 3 فترات نصف عمر ثم نطرحه من 200.",
        [f"عدد الفترات = {m('150 / 50 = 3')}.",
         f"المتبقي من الأب X = {m('200 / 8 = 25\\text{ جم}')}.",
         f"المتكوّن من الابن Y = {m('200 - 25 = 175\\text{ جم}')}."],
        f"التحقق: مجموع الكتلتين ثابت ({m('25 + 175 = 200\\text{ جم}')}).",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B21",
        "In a cliff outcrop, horizontal sedimentary layers A (bottom), B, and C are cut vertically by a basalt dike X, and all of A, B, C, and X are overlain flatly by layer D at the top. What is the correct relative age order of basalt dike X?",
        "في مكشف صخري، تخترق قاطع ناري بازلتي X الطبقات الرسوبية الأفقية أ (الأسفل)، وب، وج، وتغطي الطبقة الأفقية د كلاً من ج والقاطع X من الأعلى. ما العمر النسبي الصحيح للقاطع البازلتي X؟",
        [
            ("Younger than layers A, B, and C, and older than layer D", "أحدث من الطبقات أ وب وج، وأقدم من الطبقة د"),
            ("Older than all four sedimentary layers A, B, C, and D", "أقدم من الطبقات الرسوبية الأربع كلها"),
            ("Younger than layer D at the top of the cliff", "أحدث من الطبقة د الموجودة في أعلى الجرف"),
            ("The exact same age as the bottom layer A", "له العمر نفسه تماماً للطبقة السفلى أ"),
        ],
        "By cross-cutting relationships, a dike must be younger than every rock unit it slices through.",
        "حسب مبدأ القاطع والمقطوع، يكون القاطع الناري أحدث من كل الطبقات التي يقطعها وأقدم من الطبقات التي تغطيه دون أن يقطعها.",
        "Combine cross-cutting relationships with superposition.",
        ["Because dike X cuts across A, B, and C, those three layers had to exist first (so X is younger than A, B, C).",
         "Because layer D lies intact on top without being cut by X, D formed after X eroded flat (so X is older than D)."],
        "A rock feature is always younger than anything it cuts or erodes.",
        "نجمع بين مبدأ القاطع والمقطوع ومبدأ التراكب.",
        ["بما أن القاطع X اخترق أ وب وج فلا بد أنها وُجدت قبله، إذن X أحدث منها.",
         "وبما أن الطبقة د ترسبت فوقه دون أن يقطعها فهي أحدث منه، أي X أقدم من د."],
        "القاطع دائماً أحدث من المقطوع.",
        diagram_en=_svg_rock_strata([("Layer D", "الطبقة د", "#E2E8F0"), ("Layer C", "الطبقة ج", "#FDE68A"), ("Layer B", "الطبقة ب", "#FED7AA"), ("Layer A", "الطبقة أ", "#CBD5E1")], ("Dike X", "القاطع X"), "en"),
        diagram_ar=_svg_rock_strata([("Layer D", "الطبقة د", "#E2E8F0"), ("Layer C", "الطبقة ج", "#FDE68A"), ("Layer B", "الطبقة ب", "#FED7AA"), ("Layer A", "الطبقة أ", "#CBD5E1")], ("Dike X", "القاطع X"), "ar"),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B21",
        "Why do trilobites and ammonites serve as excellent index fossils for matching rock layer ages across distant continents?",
        "لماذا تُعد ثلاثيات الفصوص والأمونيتات أحافير مرشدة ممتازة لمضاهاة أعمار الطبقات الصخرية عبر القارات المتباعدة؟",
        [
            ("They lived over wide geographic oceans during a short, well-defined geologic time span and left easily recognized hard shells", "انتشرت جغرافياً على نطاق واسع خلال مدى زمني جيولوجي قصير ومحدد وتركت أصدافاً يسهل تمييزها"),
            ("They survived unchanged for billions of years in one small cave", "عاشت دون تغير لمليارات السنين داخل كهف جغرافي واحد صغير"),
            ("They lacked hard skeletons so they dissolved into oil everywhere", "افتقرت إلى هياكل صلبة فتحولت إلى نفط في كل مكان"),
            ("They lived exclusively inside volcanic lava flows", "عاشت حصرياً داخل تدفقات اللابة البركانية"),
        ],
        "To correlate distant strata precisely in time, a fossil needs broad space coverage and narrow time duration.",
        "لمطابقة أعمار الصخور عالمياً نحتاج أحفورة واسعة الانتشار الجغرافي وقصيرة العمر الزمني لظهور النوع وانقراضه.",
        "Evaluate the twin criteria of index fossils: geographic range vs temporal range.",
        ["Wide ocean dispersal allows geologists to correlate layers across different continents.",
         "Rapid evolutionary turnover (short species lifespan) pins the containing rock to a narrow geologic age window."],
        "Living fossils spanning hundreds of millions of years make poor index fossils.",
        "نقيّم شرطي الأحفورة المرشدة: المكان الواسع والزمان القصير.",
        ["الانتشار الجغرافي الواسع يربط بين طبقات القارات المتباعدة.",
         "المدى الزمني القصير لوجود النوع يحصر عمر الطبقة الصخرية في حقبة دقيقة."],
        "الأحافير التي استمرت لمئات الملايين من السنين لا تصلح كأحافير مرشدة دقيقة.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B21",
        f"After exactly {m('4')} half-lives of radioactive decay, a zircon crystal contains {m('5\\text{ g}')} of remaining parent isotope. What was the original mass in {m('\\text{g}')} of the parent isotope when the crystal first formed?",
        f"بعد مرور {m('4')} فترات نصف عمر بالضبط من الاضمحلال الإشعاعي، تبقّى في بلورة زركون {m('5\\text{ جم}')} من النظير المشع الأب. ما الكتلة الابتدائية بالجرام لهذا النظير عند لحظة تبلور البلورة؟",
        80, [20, 40, 160],
        "Work backward by doubling 5 g four times (5 × 2⁴ = 5 × 16).",
        "اعمل عكسياً بمضاعفة 5 جم أربع مرات (5 × 2⁴ = 5 × 16).",
        f"Invert {m('N = N_0 (1/2)^4')} to {m('N_0 = N \\times 2^4')}.",
        [f"Compute {m('2^4 = 16')}.",
         f"Original mass = {m('5 \\times 16 = 80\\text{ g}')}."],
        f"Check forward: {m('80 \\to 40 \\to 20 \\to 10 \\to 5\\text{ g}')} after 4 half-lives.",
        f"نعكس المعادلة إلى {m('N_0 = N \\times 2^4')}.",
        [f"نحسب {m('2^4 = 16')}.",
         f"الكتلة الابتدائية = {m('5 \\times 16 = 80\\text{ جم}')}."],
        f"التحقق للأمام: {m('80 \\to 40 \\to 20 \\to 10 \\to 5\\text{ جم}')}.",
    ))

    # --- HARD (10..14) ---
    d_10 = _svg_half_life(120, 250, "Myr", "م.س", 3, "en")
    ar_10 = _svg_half_life(120, 250, "Myr", "م.س", 3, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B21",
        f"A sealed igneous mineral originally trapped parent isotope P (half-life {m('250\\text{ million years}')}) with zero daughter D. Today the crystal holds {m('15\\text{ g}')} of parent P and {m('105\\text{ g}')} of daughter D. What is the rock's radiometric age in millions of years?",
        f"حبس معدن ناري مغلق عند تكونه النظير الأب P (عمر نصفه {m('250\\text{ مليون سنة}')}) دون أي نظير ابن D. يحتوي المعدن اليوم على {m('15\\text{ جم}')} من الأب P و{m('105\\text{ جم}')} من الابن D. ما العمر الإشعاعي للصخر بملايين السنين؟",
        750, [500, 1000, 1750],
        "Initial parent mass equals P + D (15 + 105 = 120 g); fraction of parent left is 15 / 120 = 1/8.",
        "الكتلة الابتدائية للأب تساوي P + D (أي 15 + 105 = 120 جم)؛ فنسبة المتبقي = 15 / 120 = 1/8.",
        f"Reconstruct {m('N_0 = P + D')}, find {m('N / N_0')}, then find half-lives {m('k')}.",
        [f"Initial parent mass = {m('15 + 105 = 120\\text{ g}')}.",
         f"Fraction remaining = {m('\\frac{15}{120} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3')}, so {m('k = 3')} half-lives.",
         f"Rock age = {m('3 \\times 250 = 750\\text{ million years}')}."],
        f"Check: daughter-to-parent ratio is {m('105 : 15 = 7 : 1')}, which always characterizes 3 half-lives ({m('2^3 - 1 = 7')}).",
        "نعيد بناء الكتلة الأصلية للأب ثم نحدد عدد أنصاف العمر.",
        [f"الكتلة الأصلية للأب = {m('15 + 105 = 120\\text{ جم}')}.",
         f"نسبة المتبقي = {m('\\frac{15}{120} = \\frac{1}{8}')} أي {m('3')} فترات نصف عمر.",
         f"عمر الصخر = {m('3 \\times 250 = 750\\text{ مليون سنة}')}."],
        "التحقق: نسبة الابن إلى الأب 7:1 تميز دائماً مرور 3 فترات نصف عمر.",
        diagram_en=d_10, diagram_ar=ar_10,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B21",
        f"In a medical lab, a fresh {m('320\\text{ mg}')} radioisotope tracer decays down to {m('20\\text{ mg}')} in exactly {m('24\\text{ hours}')}. What is the half-life of this tracer in hours?",
        f"في مختبر طبي، اضمحل نظير مشع من {m('320\\text{ ملجم}')} إلى {m('20\\text{ ملجم}')} خلال {m('24\\text{ ساعة}')} بالضبط. ما عمر النصف لهذا النظير بالساعات؟",
        6, [8, 4, 12],
        "Count how many halvings turn 320 into 20 (320 -> 160 -> 80 -> 40 -> 20 = 4 half-lives), then divide 24 h by 4.",
        "احسب عدد مرات التنصيف من 320 إلى 20 (4 مرات)، ثم اقسم 24 ساعة على 4.",
        "Find k from 320 / 20 = 16 = 2^k, then compute t_1/2 = total time / k.",
        [f"Ratio {m('\\frac{20}{320} = \\frac{1}{16} = \\left(\\frac{1}{2}\\right)^4')}, so {m('k = 4')} half-lives occurred.",
         f"Half-life = {m('\\frac{24\\text{ h}}{4} = 6\\text{ h}')}."],
        f"Check: {m('320 \\xrightarrow{6\\text{h}} 160 \\xrightarrow{12\\text{h}} 80 \\xrightarrow{18\\text{h}} 40 \\xrightarrow{24\\text{h}} 20\\text{ mg}')}.",
        "نجد عدد أنصاف العمر أولاً ثم نقسم الزمن الكلي عليه.",
        [f"نسبة المتبقي = {m('\\frac{20}{320} = \\frac{1}{16} = \\left(\\frac{1}{2}\\right)^4')} أي {m('4')} فترات.",
         f"عمر النصف = {m('\\frac{24}{4} = 6\\text{ ساعات}')}."],
        f"التحقق: {m('320 \\to 160 \\to 80 \\to 40 \\to 20')} في 4 خطوات × 6 ساعات = 24 ساعة.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B21",
        "A horizontal sandstone layer rests directly on top of a volcanic ash bed radiometrically dated at 85 million years old, and is capped directly beneath an un-baked basalt lava flow dated at 68 million years old. Why do geologists bracket the sandstone's depositional age between 68 and 85 million years instead of radiometrically dating the sand grains inside the sandstone?",
        "تقع طبقة حجر رملي أفقية مباشرة فوق طبقة رماد بركاني عمرها الإشعاعي 85 مليون سنة، ومغطاة مباشرة بتدفق لابة بازلتية عمرها 68 مليون سنة. لماذا يحصر الجيولوجيون عمر ترسب الحجر الرملي بين 68 و85 مليون سنة بدلاً من تأريخ حبيبات الرمل نفسها إشعاعياً؟",
        [
            ("Sand grains weathered from much older eroded rocks retain those older source ages, not the age when the sand was deposited", "حبيبات الرمل المتآكلة من صخور قديمة تحتفظ بعمر الصخر الأم القديم لا بتاريخ ترسب الحجر الرملي"),
            ("Sandstone contains no radioactive atoms anywhere on Earth", "لا يحتوي الحجر الرملي على أي ذرات مشعة مطلقاً"),
            ("Basalt flow underneath pushes sandstone upward into the Mesozoic Era", "تدفق البازلت يرفع الحجر الرملي للأعلى زمنياً"),
            ("Radioactive decay speeds up tenfold inside loose sand grains", "يتسارع الاضمحلال الإشعاعي عشر مرات داخل حبيبات الرمل"),
        ],
        "Clastic sandstone grains came from pre-existing weathered mountains; radiometric clocks reset only upon crystallization or heating.",
        "حبيبات الحجر الرملي منقولة من صخور أقدم؛ والساعة الإشعاعية تُصفّر عند تبلور الصهارة أو الرماد البركاني فقط.",
        "Combine superposition bracketing with igneous vs clastic radiometric clocks.",
        ["Radiometric dating measures when a mineral last crystallized from magma (resetting the isotope clock).",
         "Detrital quartz/feldspar sand grains record when the eroded source granite formed — potentially hundreds of millions of years earlier — whereas bracketing volcanic layers pinpoint deposition between 68 and 85 Ma."],
        "Volcanic ash layers embedded in sedimentary basins are prized markers for calibrating the geologic time scale.",
        "نفرق بين عمر الصخر الناري المتبلور وعمر الفتات الرسوبي المنقول.",
        ["التأريخ الإشعاعي يقيس لحظة تبلور المعدن من الصهارة أو الرماد البركاني.",
         "حبيبات الرمل الفتاتية تحتفظ بعمر الصخور الأم التي تفتتت منها، لذا نحصر الترسب بين الطبقتين البركانيتين 85 و68 مليون سنة."],
        "الرماد البركاني هو الأداة الذهبية لضبط أعمار الصخور الرسوبية.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B21",
        "Deep underground, sedimentary limestone is transformed into marble, which is later carried into a subduction zone, completely melted, and erupted at a volcano to form basalt. What exact sequence of rock types did this material pass through?",
        "في الأعماق تحول الحجر الجيري الرسوبي إلى رخام، ثم سُحب إلى منطقة طرح فانصهر كلياً واندفع بركانياً مكوناً صخر البازلت. ما التسلسل الصحيح لأنواع الصخور التي مرت بها هذه المادة؟",
        [
            ("Sedimentary → Metamorphic → Magma → Extrusive Igneous", "رسوبي ← متحول ← صهارة ← ناري سطحي"),
            ("Metamorphic → Sedimentary → Intrusive Igneous → Magma", "متحول ← رسوبي ← ناري جوفي ← صهارة"),
            ("Sedimentary → Intrusive Igneous → Metamorphic → Basalt", "رسوبي ← ناري جوفي ← متحول ← بازلت"),
            ("Igneous → Sedimentary → Metamorphic → Evaporite", "ناري ← رسوبي ← متحول ← متبخر"),
        ],
        "Marble is metamorphosed limestone, and basalt is lava cooled at the surface (extrusive igneous).",
        "الرخام صخر متحول عن الحجر الجيري، والبازلت صخر ناري سطحي ناتج عن تبرد اللابة.",
        "Trace each named rock to its rock-cycle family.",
        ["Limestone is a chemical/biochemical sedimentary rock.",
         "Heat and pressure convert it without melting into marble (metamorphic), then melting creates magma, and surface eruption cools into basalt (extrusive igneous)."],
        "The rock cycle permits matter to cycle along many pathways, not a single fixed loop.",
        "نحدد فئة كل صخر في المراحل الأربع.",
        ["الحجر الجيري صخر رسوبي، وبالحرارة والضغط يتحول إلى رخام (متحول).",
         "الانصهار يعطي صهارة، والتبرد على السطح يكوّن البازلت (ناري سطحي)."],
        "دورة الصخور مسار متشعب يربط بين الأنواع الثلاثة.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B21",
        f"After exactly {m('5')} half-lives have elapsed, what percentage ({m('\\%')}) of an initial radioactive sample remains undecayed?",
        f"بعد مرور {m('5')} فترات نصف عمر بالضبط، ما النسبة المئوية المتبقية دون اضمحلال من العينة المشعة الابتدائية؟",
        3.125, [6.25, 1.5625, 10],
        "Start at 100% and halve five times: 100 -> 50 -> 25 -> 12.5 -> 6.25 -> 3.125%.",
        "ابدأ من 100% ونصّف خمس مرات: 100 ← 50 ← 25 ← 12.5 ← 6.25 ← 3.125%.",
        f"Evaluate {m('100\\% \\times \\left(\\frac{1}{2}\\right)^5 = \\frac{100\\%}{32}')}.",
        [f"Compute {m('2^5 = 32')}.",
         f"Remaining percentage = {m('\\frac{100\\%}{32} = 3.125\\%')}."],
        f"Check: {m('3.125 \\times 32 = 100')}.",
        f"نحسب {m('\\frac{100\\%}{2^5} = \\frac{100\\%}{32}')}.",
        [f"بما أن {m('2^5 = 32')}، فإن النسبة المتبقية = {m('\\frac{100}{32} = 3.125\\%')}."],
        f"التحقق: {m('3.125 \\times 32 = 100')}.",
        suffix=r"\%",
    ))

    return qs


def _gen_sci_b22(start_idx: int) -> list[dict]:
    """G9-SCI-B22: Atmosphere Layers, Lapse Rate, Coriolis, Sea Breeze & Carbon Budget (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = _svg_atmosphere("Troposphere", "en")
    ar_0 = _svg_atmosphere("Troposphere", "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B22",
        "In the highlighted lowest atmospheric layer (0–12 km), roughly 75% of total air mass and nearly all water vapor reside. Which phenomena occur almost exclusively inside this layer?",
        "في الطبقة الدنيا المظللة من الغلاف الجوي (0–12 كم)، تتركز نحو 75% من كتلة الهواء ومعظم بخار الماء. أي ظواهر تحدث حصرياً تقريباً داخل هذه الطبقة؟",
        [
            ("Clouds, rainfall, thunderstorms, and daily weather systems", "الغيوم والأمطار والعواصف الرعدية وأنظمة الطقس اليومية"),
            ("Auroras caused by solar wind particles hitting thin ions", "ظاهرة الشفق القطبي الناتجة عن الرياح الشمسية"),
            ("The main stratospheric ozone shield protecting Earth from UV rays", "طبقة الأوزون الرئيسية التي تحمي الأرض من الأشعة فوق البنفسجية"),
            ("Burning of high-speed space meteors at 70 km altitude", "احتراق الشهب الفضائية السريعة على ارتفاع 70 كم"),
        ],
        "Think about where clouds form and commercial jets cruise near the top boundary.",
        "فكّر أين تتشكل السحب وتحدث تقلبات الطقس والأمطار اليومية.",
        "Identify the Troposphere as Earth's weather sphere.",
        ["Because the Troposphere holds nearly all atmospheric water vapor and experiences surface heating convection, weather systems operate there.",
         "Ozone resides higher in the Stratosphere, meteors burn in the Mesosphere, and auroras glow in the Thermosphere."],
        "Tropo- means turning or mixing, referring to convective weather churn.",
        "نحدد التروبوسفير بوصفها طبقة الطقس والتقلبات الجوية.",
        ["تحتوي التروبوسفير على معظم بخار الماء وتنقل الحرارة بالحمل من سطح الأرض فتتكون السحب والأمطار.",
         "طبقة الأوزون في الستراتوسفير والشهب في الميزوسفير والشفق في الثيرموسفير."],
        "اسم التروبوسفير يعني طبقة التقلب والاضطراب الجوي.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = _svg_atmosphere("Stratosphere", "en")
    ar_1 = _svg_atmosphere("Stratosphere", "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B22",
        "The highlighted Stratosphere (12–50 km) contains a vital protective layer of triatomic oxygen (O₃). What primary life-protecting function does this ozone layer perform?",
        "تحتوي طبقة الستراتوسفير المظللة (12–50 كم) على درع حيوي من غاز الأوزون (O₃). ما الوظيفة الأساسية التي يؤديها الأوزون لحماية الحياة على الأرض؟",
        [
            ("Absorbing most harmful high-energy solar ultraviolet (UV) radiation", "امتصاص معظم الأشعة فوق البنفسجية الضارة عالية الطاقة القادمة من الشمس"),
            ("Trapping 100% of visible sunlight so Earth remains frozen", "حجب 100% من الضوء المرئي لإبقاء الأرض متجمدة"),
            ("Condensing ocean moisture into snowstorms", "تكثيف رطوبة المحيطات إلى عواصف ثلجية"),
            ("Generating Earth's planetary magnetic field", "توليد المجال المغناطيسي للكوكب"),
        ],
        "UV radiation breaks DNA bonds and causes skin damage; ozone intercepts UV-B and UV-C photons.",
        "تمتص جزيئات الأوزون الأشعة فوق البنفسجية الضارة التي تؤذي الخلايا والحمض النووي.",
        "Connect stratospheric ozone O3 to ultraviolet filtration.",
        ["Stratospheric O3 absorbs dangerous solar UV rays before they reach Earth's surface.",
         "Visible sunlight passes straight through to support photosynthesis and vision."],
        "Without the ozone shield, surface DNA damage would severely limit land life.",
        "نربط غاز الأوزون O3 بامتصاص الأشعة فوق البنفسجية.",
        ["يمتص الأوزون الأشعة فوق البنفسجية الضارة في الستراتوسفير ويمنع وصول معظمها للسطح.",
         "بينما يسمح بمرور الضوء المرئي الضروري للبناء الضوئي والحياة."],
        "تحمي طبقة الأوزون الكائنات الحية من طفرات الأشعة فوق البنفسجية.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B22",
        f"In the standard troposphere, air temperature drops by {m('6.5^\\circ\\text{C}')} for every {m('1\\text{ km}')} rise in altitude. If sea-level air temperature is {m('30^\\circ\\text{C}')}, what temperature in {m('^\\circ\\text{C}')} is expected at an altitude of {m('4\\text{ km}')}?",
        f"في طبقة التروبوسفير القياسية، تنخفض درجة حرارة الهواء بمقدار {m('6.5^\\circ\\text{م}')} لكل ارتفاع قدره {m('1\\text{ كم}')}. إذا كانت درجة الحرارة عند سطح البحر {m('30^\\circ\\text{م}')}، فما درجة الحرارة المتوقعة على ارتفاع {m('4\\text{ كم}')} بوحدة {m('^\\circ\\text{م}')}؟",
        4, [23.5, 56, 10],
        "Multiply 6.5 °C/km by 4 km to find total cooling (26 °C), then subtract from 30 °C.",
        "اضرب 6.5 °م/كم في 4 كم لحساب الانخفاض الكلي (26 °م)، ثم اطرحه من 30 °م.",
        f"Compute {m('T = T_0 - 6.5 \\times h')}.",
        [f"Cooling across {m('4\\text{ km}')}: {m('6.5 \\times 4 = 26^\\circ\\text{C}')}.",
         f"Air temperature at {m('4\\text{ km}')}: {m('30 - 26 = 4^\\circ\\text{C}')}."],
        f"Check: climbing {m('4\\text{ km}')} up a mountain drops air temperature near freezing ({m('4^\\circ\\text{C}')}).",
        f"نطبق {m('T = T_0 - 6.5 \\times h')}.",
        [f"مقدار الانخفاض = {m('6.5 \\times 4 = 26^\\circ\\text{م}')}.",
         f"درجة الحرارة = {m('30 - 26 = 4^\\circ\\text{م}')}."],
        f"التحقق: عند ارتفاع 4 كم تنخفض الحرارة كثيراً لتصل إلى {m('4^\\circ\\text{م}')}.",
        diagram_en=_svg_atmosphere("Troposphere", "en"),
        diagram_ar=_svg_atmosphere("Troposphere", "ar"),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B22",
        "Which gas composition accurately represents clean, dry air in Earth's lower atmosphere?",
        "أي تركيب غازي يمثل بدقة الهواء الجاف النقي في الغلاف الجوي السفلي للأرض؟",
        [
            ("About 78% Nitrogen (N₂), 21% Oxygen (O₂), and 1% Argon, CO₂, and trace gases", "نحو 78% نيتروجين (N₂) و21% أكسجين (O₂) و1% أرجون وثاني أكسيد الكربون وغازات أثرية"),
            ("About 78% Oxygen (O₂), 21% Nitrogen (N₂), and 1% Hydrogen", "نحو 78% أكسجين (O₂) و21% نيتروجين (N₂) و1% هيدروجين"),
            ("About 50% Carbon Dioxide (CO₂) and 50% Oxygen (O₂)", "نحو 50% ثاني أكسيد الكربون و50% أكسجين"),
            ("About 78% Water Vapor, 21% Argon, and 1% Nitrogen", "نحو 78% بخار ماء و21% أرجون و1% نيتروجين"),
        ],
        "Nitrogen makes up nearly four-fifths of Earth's atmosphere, oxygen about one-fifth.",
        "يشكل النيتروجين قرابة أربعة أخماس الغلاف الجوي والأكسجين نحو الخمس.",
        "Recall major dry-air atmospheric percentages.",
        ["Nitrogen (N₂) accounts for ~78% and Oxygen (O₂) for ~21%.",
         "Argon (~0.93%) and Carbon Dioxide (~0.04%) make up nearly all of the remaining 1%."],
        "Notice CO₂ is a trace gas (~0.04%) despite its powerful radiative effect.",
        "نستعرض النسب المئوية القياسية للهواء الجاف.",
        ["النيتروجين 78% والأكسجين 21% معاً يشكلان 99% من الهواء الجاف.",
         "النسبة المتبقية 1% معظمها أرجون (~0.93%) وقليل من ثاني أكسيد الكربون (~0.04%)."],
        "رغم ضآلة نسبة CO₂ فإنه يؤثر بقوة في الاتزان الحراري.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B22",
        "In the Troposphere temperature decreases with height, yet inside the Stratosphere temperature actually INCREASES with height. What directly heats the upper Stratosphere?",
        "تنخفض درجة الحرارة مع الارتفاع في التروبوسفير، لكنها تزداد مع الارتفاع داخل الستراتوسفير. ما المصدر المباشر الذي يسخّن الجزء العلوي من الستراتوسفير؟",
        [
            ("Absorption of solar ultraviolet radiation by stratospheric ozone molecules", "امتصاص جزيئات الأوزون للأشعة فوق البنفسجية الشمسية وتحويلها إلى حرارة"),
            ("Warm convective updrafts rising continuously from ocean waves", "تيارات الحمل الصاعدة باستمرار من أمواج المحيط"),
            ("Geothermal heat radiating from Earth's inner core through space", "الحرارة الجوفية الصاعدة من لب الأرض عبر الفضاء"),
            ("Friction from commercial airliners flying at 10 km altitude", "احتكاك الطائرات التجارية المحلقة على ارتفاع 10 كم"),
        ],
        "Look at where the ozone concentration sits: absorbing UV energy converts radiation directly into molecular kinetic energy.",
        "تتركز طبقة الأوزون في الستراتوسفير، وامتصاص الأشعة فوق البنفسجية يرفع الطاقة الحركية لجزيئات الهواء هناك.",
        "Explain the stratospheric thermal inversion using ozone UV absorption.",
        ["Unlike the Troposphere (heated from Earth's ground below), the Stratosphere absorbs solar UV photons directly via O₃.",
         "This internal heat source makes upper stratospheric layers warmer than its base, suppressing vertical convection."],
        "Stratospheric thermal stability explains why thunderstorm anvils flatten out at the tropopause.",
        "نربط الانقلاب الحراري في الستراتوسفير بامتصاص الأوزون للأشعة.",
        ["بينما تسخن التروبوسفير من سطح الأرض، تسخن الستراتوسفير داخلياً بامتصاص الأوزون للأشعة فوق البنفسجية.",
         "يمنع هذا الدفء العلوي صعود تيارات الحمل، مما يفسر استقرار هذه الطبقة."],
        "لذلك تتوقف قمم سحب العواصف الرعدية عند حدود الستراتوسفير.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B22",
        "Along a coastal city on a hot afternoon, cool ocean air flows steadily inland toward the beach. Why does this daytime sea breeze blow from water to land?",
        "في مدينة ساحلية خلال ظهيرة حارة، يهب نسيم بارد من البحر نحو اليابسة. لماذا يتجه نسيم البحر نهاراً من الماء إلى اليابسة؟",
        [
            ("Land warms faster than water, causing warm low-density air to rise over land while denser air over the cooler sea flows inland", "تسخن اليابسة أسرع من الماء فيصعد الهواء الدافئ الأقل كثافة فوقها، ويندفع الهواء الأبرد والأكثر كثافة من البحر ليحل محله"),
            ("Seawater warms much faster than sand, pulling coastal air out to sea", "يسخن ماء البحر أسرع بكثير من الرمل فيسحب هواء اليابسة نحو البحر"),
            ("The Coriolis force always forces winds perpendicular to every coastline", "قوة كوريوليس تدفع الرياح دائماً عمودياً على السواحل"),
            ("Ocean tides physically push surface air toward beaches every afternoon", "المد البحري يدفع الهواء السطحي نحو الشاطئ كل ظهيرة"),
        ],
        "Combine specific heat difference (sand heats faster than sea) with warm air rising (low surface pressure).",
        "اربط بين سرعة تسخين اليابسة مقارنة بالبحر وصعود الهواء الدافئ قليل الكثافة ليحل محله هواء البحر البارد.",
        "Build the daytime thermal convection loop between coast and sea.",
        ["Because sand has much lower specific heat than water, daytime land heats rapidly, warming and expanding the air above it.",
         "As warm air rises over land (forming lower surface pressure), cooler, denser air sweeps inland from the sea."],
        "At night, land cools faster than sea, reversing the circulation into a land breeze.",
        "نكوّن دورة الحمل الحراري النهارية على الساحل.",
        ["تسخن اليابسة نهاراً أسرع من البحر فيتمدد الهواء فوقها ويصعد مكوناً ضغطاً سطحياً منخفضاً.",
         "ينساب الهواء الأبرد والأثقل من فوق البحر نحو اليابسة في صورة نسيم البحر."],
        "ليلاً تبرد اليابسة أسرع فينعكس الاتجاه إلى نسيم البر.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B22",
        "Large-scale winds and ocean currents curve rather than moving straight from high pressure to low pressure. Because of the Coriolis effect caused by Earth's rotation, how do winds deflect in the Northern Hemisphere versus the Southern Hemisphere?",
        "تنحرف الرياح العالمية والتيارات المحيطية عن الخط المستقيم بين الضغط المرتفع والمنخفض. بسبب تأثير كوريوليس الناتج عن دوران الأرض، كيف تنحرف الرياح في نصف الكرة الشمالي مقابل الجنوبي؟",
        [
            ("Rightward relative to motion in the Northern Hemisphere; leftward in the Southern Hemisphere", "نحو اليمين بالنسبة لاتجاه حركتها في النصف الشمالي، ونحو اليسار في النصف الجنوبي"),
            ("Leftward in the Northern Hemisphere; rightward in the Southern Hemisphere", "نحو اليسار في النصف الشمالي، ونحو اليمين في النصف الجنوبي"),
            ("Always straight eastward regardless of hemisphere or wind direction", "نحو الشرق دائماً في كلا نصفي الكرة دون استثناء"),
            ("Upward at the North Pole and downward at the Equator", "للأعلى عند القطب الشمالي وللأسفل عند خط الاستواء"),
        ],
        "Face the direction the air is moving: in the Northern Hemisphere (including Saudi Arabia), Earth spins underneath causing apparent rightward curve.",
        "تخيل نفسك تنظر باتجاه سير الرياح: في النصف الشمالي تنحرف يميناً، وفي النصف الجنوبي يساراً.",
        "Recall Coriolis deflection direction by hemisphere.",
        ["Earth rotates eastward faster at the Equator (~1,670 km/h) than at higher latitudes.",
         "Conserving eastward velocity deflects moving fluids to the RIGHT of their path in the Northern Hemisphere and to the LEFT in the Southern Hemisphere."],
        "Coriolis vanishes strictly at the Equator (0° latitude) and peaks at the poles.",
        "نطبق اتجاه انحراف كوريوليس في نصفي الكرة.",
        ["تدور الأرض شرقاً بسرعة خطية أكبر عند الاستواء مقارنة بالعروض العليا.",
         "نتيجة لذلك تنحرف الرياح يمين مسارها في النصف الشمالي ويسار مسارها في النصف الجنوبي."],
        "ينعدم تأثير كوريوليس عند خط الاستواء تماماً.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B22",
        "How do greenhouse gases (H₂O, CO₂, CH₄) warm Earth's lower atmosphere through the natural greenhouse effect?",
        "كيف تسهم غازات الدفيئة (بخار الماء، CO₂، الميثان) في تدفئة الغلاف الجوي السفلي للأرض عبر ظاهرة الاحتباس الحراري الطبيعية؟",
        [
            ("They transmit incoming shortwave visible sunlight to warm Earth's surface, while absorbing and re-radiating outgoing longwave infrared radiation", "تسمح بمرور ضوء الشمس المرئي قصير الموجة لتسخين السطح، لكنها تمتص الأشعة تحت الحمراء طويلة الموجة الصادرة من الأرض وتعيد إشعاعها"),
            ("They reflect 100% of solar visible light back upward into the Stratosphere", "تعكس 100% من الضوء المرئي الشمسي إلى الستراتوسفير"),
            ("They release heat by burning nitrogen and oxygen in the Troposphere", "تولد الحرارة بحرق النيتروجين والأكسجين في التروبوسفير"),
            ("They prevent convection currents from rising inside ocean water", "تمنع صعود تيارات الحمل داخل مياه المحيطات"),
        ],
        "Distinguish incoming solar shortwave light (passes through) from outgoing terrestrial longwave heat (absorbed/re-emitted).",
        "ميّز بين ضوء الشمس الوارد قصير الموجة (ينفذ) والحرارة الأرضية الصادرة طويلة الموجة تحت الحمراء (تُمتص ويُعاد إشعاعها).",
        "Explain selective radiative transmission vs infrared absorption.",
        ["Greenhouse gas molecules are transparent to most visible sunlight reaching the surface.",
         "When Earth radiates warm infrared wavelengths upward, CO₂ and H₂O absorb them and re-emit part back down."],
        "Without the natural greenhouse effect, Earth's average surface temperature would be about -18 °C instead of +15 °C.",
        "نميز بين طيف الإشعاع الشمسي والإشعاع الأرضي.",
        ["جزيئات الدفيئة شفافة أمام الضوء المرئي للشمس فتصل الطاقة إلى سطح الأرض.",
         "تشع الأرض الدافئة أشعة تحت حمراء طويلة الموجة فتمتصها غازات الدفيئة وتعيد جزءاً منها للأسفل."],
        "لولا الاحتباس الحراري الطبيعي لكان متوسط حرارة الأرض نحو -18 °م بدلاً من +15 °م.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B22",
        f"A weather balloon launches from a coastal station at {m('28^\\circ\\text{C}')} and radios back a temperature of {m('-11^\\circ\\text{C}')}. Using the standard tropospheric lapse rate of {m('6.5^\\circ\\text{C/km}')}, at what altitude in {m('\\text{km}')} is the balloon?",
        f"انطلق بالون طقس من محطة ساحلية حرارتها {m('28^\\circ\\text{م}')} وأرسل قراءة حرارة تبلغ {m('-11^\\circ\\text{م}')}. باستخدام معدل التناقص الحراري القياسي {m('6.5^\\circ\\text{م/كم}')}، على أي ارتفاع بالكيلومتر يحلق البالون؟",
        6, [4, 2.6, 8],
        "Compute the full temperature drop from +28 °C down to -11 °C (28 - (-11) = 39 °C), then divide by 6.5.",
        "احسب الانخفاض الكامل في الحرارة من +28 °م إلى -11 °م (وهو 39 °م) ثم اقسم على 6.5.",
        f"Solve {m('h = \\frac{T_{\\text{surface}} - T_h}{6.5}')}.",
        [f"Temperature drop: {m('\\Delta T = 28 - (-11) = 39^\\circ\\text{C}')}.",
         f"Altitude: {m('h = \\frac{39}{6.5} = 6\\text{ km}')}."],
        f"Check: {m('28 - 6 \\times 6.5 = 28 - 39 = -11^\\circ\\text{C}')}.",
        f"نطبق {m('h = \\frac{T_{\\text{surface}} - T_h}{6.5}')}.",
        [f"مقدار الانخفاض = {m('28 - (-11) = 39^\\circ\\text{م}')}.",
         f"الارتفاع = {m('\\frac{39}{6.5} = 6\\text{ كم}')}."],
        f"التحقق: {m('28 - 6 \\times 6.5 = -11^\\circ\\text{م}')}.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_9 = _svg_atmosphere("Thermosphere", "en")
    ar_9 = _svg_atmosphere("Thermosphere", "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B22",
        "In the highlighted Thermosphere above 80 km, individual gas molecules race at extreme speeds corresponding to temperatures over 1,000 °C. Yet an astronaut holding out a bare metal probe there would NOT feel burned. Why?",
        "في طبقة الثيرموسفير المظللة فوق 80 كم، تتحرك جزيئات الغاز بسرعات هائلة تعادل درجات حرارة تتجاوز 1,000 °م. ومع ذلك لن يشعر مسبار معدني هناك باحتراق حراري فوري. لماذا؟",
        [
            ("Air density is extraordinarily low, so far too few molecules collide per second to transfer significant thermal energy", "كثافة الهواء منخفضة للغاية فلا يصطدم إلا عدد ضئيل جداً من الجزيئات بالثانية لنقل طاقة حرارية محسوسة"),
            ("The Celsius thermometer reads backwards above the Mesosphere", "تعمل موازين الحرارة بالعكس فوق طبقة الميزوسفير"),
            ("Ozone cools metal surfaces faster than molecules can hit them", "تبرد طبقة الأوزون المعادن أسرع من تصادم الجزيئات"),
            ("High-speed molecules carry negative kinetic energy", "تمتلك الجزيئات السريعة طاقة حركية سالبة"),
        ],
        "Distinguish TEMPERATURE (average kinetic energy per molecule) from HEAT (total thermal energy transferred by many particles).",
        "فرّق بين درجة الحرارة (متوسط طاقة الجزيء الواحد) وكمية الحرارة الكلية التي تتطلب عدداً كبيراً من التصادمات.",
        "Separate intensive molecular speed (temperature) from extensive particle flux (heat).",
        ["Temperature measures average kinetic energy per individual particle (very high due to solar X-ray/EUV absorption).",
         "However, air at 200 km is nearly a vacuum, so total heat transferred per second is tiny."],
        "Compare touching a spark from a sparkler (tiny mass at 1,500 °C) vs touching a pot of boiling water (large mass at 100 °C).",
        "نفرق بين درجة الحرارة وكمية الحرارة المنقولة.",
        ["تقيس درجة الحرارة متوسط سرعة الجزيء المفرد وهي مرتفعة لامتصاص الأشعة السينية الشمسية.",
         "لكن الهواء هناك شبه فراغ شديد التخلخل، فتكاد تنعدم التصادمات اللازمة لنقل حرارة محسوسة."],
        "يشبه ذلك ملامسة شرارة ضئيلة الكتلة بدرجة عالية دون أن تحرق مثل ماء مغلي كثيف.",
        diagram_en=d_9, diagram_ar=ar_9,
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_concept_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B22",
        "Arctic sea ice reflects ~85% of incoming sunlight (high albedo), whereas open dark ocean water reflects only ~6% (low albedo). How does Arctic ice melt create a positive climate feedback loop?",
        "يعكس جليد البحر القطبي نحو 85% من ضوء الشمس (ألبيدو مرتفع)، بينما يعكس ماء المحيط الداكن المكشوف نحو 6% فقط (ألبيدو منخفض). كيف يُنتج ذوبان الجليد حلقة تغذية راجعة موجبة في المناخ؟",
        [
            ("Melting bright ice exposes dark water that absorbs more solar energy, causing additional warming and even faster ice melt", "ذوبان الجليد العاكس يكشف ماءً داكناً يمتص طاقة شمسية أكبر فيرفع الحرارة ويسرّع الذوبان أكثر"),
            ("Dark water freezes instantly into thicker snow, cooling the Arctic indefinitely", "يتجمد الماء الداكن فوراً إلى ثلج سميك فيبرد القطب إلى الأبد"),
            ("Lower ocean albedo blocks infrared radiation from entering Earth", "انخفاض الألبيدو يمنع دخول الأشعة تحت الحمراء إلى الأرض"),
            ("Melting white ice increases global planetary reflectivity back to 95%", "يرفع ذوبان الجليد انعكاسية الكوكب العالمية إلى 95%"),
        ],
        "A positive feedback loop amplifies an initial perturbation rather than dampening it.",
        "التغذية الراجعة الموجبة تضخم التغير الابتدائي وتزيده في الاتجاه نفسه ولا تعاكسه.",
        "Trace the albedo-temperature amplification cycle.",
        ["Initial warming melts reflective white sea ice.",
         "Exposed dark ocean absorbs ~94% of sunlight instead of ~15%, accelerating regional warming and further melt."],
        "Positive here means self-reinforcing amplification, not beneficial.",
        "نتتبع حلقة التضخيم بين الألبيدو ودرجة الحرارة.",
        ["يؤدي الاحترار إلى ذوبان الجليد الأبيض شديد الانعكاس.",
         "يمتص المحيط الداكن المنكشف قرابة 94% من الإشعاع الشمسي فيزداد الاحترار ويتسارع الذوبان."],
        "كلمة موجبة تعني تعزيز الأثر الابتدائي وتضخيمه ذاتياً.",
        diagram_en=_svg_experiment_bars("Surface Albedo Comparison", "مقارنة معامل الانعكاس", [("Sea Ice", "جليد بحري", 85, "85%"), ("Ocean", "محيط", 6, "6%")], "Reflected Sunlight %", "الإشعاع المنعكس %", "en"),
        diagram_ar=_svg_experiment_bars("Surface Albedo Comparison", "مقارنة معامل الانعكاس", [("Sea Ice", "جليد بحري", 85, "85%"), ("Ocean", "محيط", 6, "6%")], "Reflected Sunlight %", "الإشعاع المنعكس %", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B22",
        f"Averaged over the whole globe, Earth receives {m('340\\text{ W/m}^2')} of solar power at the top of the atmosphere and reflects {m('30\\%')} (planetary albedo {m('0.30')}) straight back to space. How many {m('\\text{W/m}^2')} of solar energy are absorbed by Earth's atmosphere and surface?",
        f"كمتوسط عالمي، يتلقى أعلى الغلاف الجوي للأرض {m('340\\text{ واط/م}^2')} من القدرة الشمسية ويعكس {m('30\\%')} منها مباشرة إلى الفضاء (الألبيدو الكوكبي {m('0.30')}). كم {m('\\text{واط/م}^2')} من الطاقة الشمسية تمتصه الأرض وغلافها الجوي؟",
        238, [102, 310, 272],
        "If 30% is reflected, the absorbed fraction is 70% (0.70 × 340).",
        "إذا انعكس 30% من الطاقة، فإن النسبة الممتصة هي 70% (أي 0.70 × 340).",
        f"Compute {m('F_{\\text{abs}} = F_{\\text{in}} (1 - \\alpha)')}.",
        [f"Reflected flux = {m('0.30 \\times 340 = 102\\text{ W/m}^2')}.",
         f"Absorbed flux = {m('340 - 102 = 238\\text{ W/m}^2')} (or {m('0.70 \\times 340 = 238')})."],
        f"Check: {m('102 + 238 = 340\\text{ W/m}^2')}.",
        f"نطبق {m('F_{\\text{abs}} = F_{\\text{in}} (1 - 0.30)')}.",
        [f"المنعكس = {m('0.30 \\times 340 = 102\\text{ واط/م}^2')}.",
         f"الممتص = {m('340 - 102 = 238\\text{ واط/م}^2')}."],
        f"التحقق: {m('102 + 238 = 340\\text{ واط/م}^2')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B22",
        f"In a simplified global carbon budget model, fossil-fuel burning adds {m('9\\text{ GtC/year}')} and land clearing adds {m('1\\text{ GtC/year}')} to the atmosphere, while oceans absorb {m('3\\text{ GtC/year}')} and regrowing forests absorb {m('2\\text{ GtC/year}')}. What is the net annual carbon accumulation in the atmosphere in {m('\\text{GtC/year}')}?",
        f"في نموذج مبسط لميزانية الكربون العالمية، يضيف حرق الوقود الأحفوري {m('9\\text{ جيجاطن كربون/سنة}')} وإزالة الغابات {m('1\\text{ جيجاطن/سنة}')} إلى الجو، بينما تمتص المحيطات {m('3\\text{ جيجاطن/سنة}')} وتستعيد الغابات امتصاص {m('2\\text{ جيجاطن/سنة}')}. ما صافي الزيادة السنوية للكربون في الغلاف الجوي بوحدة {m('\\text{جيجاطن/سنة}')}؟",
        5, [15, 6, 4],
        "Subtract total carbon sinks (3 + 2 = 5) from total atmospheric sources (9 + 1 = 10).",
        "اطرح مجموع المصارف (3 + 2 = 5) من مجموع المصادر المضافة للجو (9 + 1 = 10).",
        f"Calculate {m('\\text{Net Flux} = \\text{Sources} - \\text{Sinks}')}.",
        [f"Total emissions into air: {m('9 + 1 = 10\\text{ GtC/yr}')}.",
         f"Total ocean + land uptake: {m('3 + 2 = 5\\text{ GtC/yr}')}.",
         f"Net annual atmospheric gain = {m('10 - 5 = 5\\text{ GtC/yr}')}."],
        "Check: half of human carbon emissions remain airborne in this budget, matching real-world observations (~50%).",
        f"نطبق {m('\\text{الصافي} = \\text{المصادر} - \\text{المصارف}')}.",
        [f"مجموع الانبعاثات = {m('9 + 1 = 10\\text{ جيجاطن/سنة}')}.",
         f"مجموع الامتصاص = {m('3 + 2 = 5\\text{ جيجاطن/سنة}')}.",
         f"الصافي المتراكم في الجو = {m('10 - 5 = 5\\text{ جيجاطن/سنة}')}."],
        "التحقق: يبقى نحو نصف الانبعاثات في الجو بينما تمتص المحيطات واليابسة النصف الآخر.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B22",
        "Moist ocean winds climb the western slopes of a tall coastal mountain range, dropping heavy rain and snow, while the eastern interior valleys beyond the ridge remain arid desert. What atmospheric physics explains this rain-shadow effect?",
        "تصعد رياح محيطية رطبة المنحدرات الغربية لسلسلة جبال ساحلية شاهقة فتُسقط أمطاراً غزيرة، بينما تظل الوديان الداخلية شرق القمة صحراء جافة. ما التفسير الفيزيائي الجوي لظاهرة ظل المطر؟",
        [
            ("Rising windward air expands, cools, and condenses moisture into rain; descending leeward air compresses, warms, and drops in relative humidity", "الهواء الصاعد يتمدد ويبرد فتتكثف رطوبته أمطاراً، ثم يهبط على الجانب الآخر جافاً فينضغط ويسخن وتنخفض رطوبته النسبية"),
            ("Mountain rocks chemically destroy all water molecules passing over the summit", "تحلل صخور الجبال جزيئات الماء كيميائياً عند القمة"),
            ("Descending leeward air expands and freezes into dry ice blocks", "الهواء الهابط يتمدد ويتجمد إلى جليد جاف"),
            ("Gravity pulls moisture downward only on the eastern side of mountains", "تجذب الجاذبية الرطوبة فقط على الجانب الشرقي للجبال"),
        ],
        "Air rising into lower pressure expands and cools (condensation); air sinking into higher pressure compresses and warms (evaporation/dryness).",
        "الهواء الصاعد يبرد بالتمدد فيمطر، والهواء الهابط الجاف يسخن بالانضغاط فتتبخر أي غيوم وتجف الأرض.",
        "Track adiabatic cooling on ascent vs adiabatic warming on descent.",
        ["Forced ascent up the windward slope expands air into lower-pressure altitudes, cooling it to its dew point and precipitating water.",
         "Having lost its moisture, the air sinks down the leeward side, warming by compression and holding any remaining vapor far below saturation."],
        "This process explains coastal rains along the western Sarawat mountains and arid plateaus farther inland.",
        "نتتبع التبريد بالتمدد في الصعود والتسخين بالانضغاط في الهبوط.",
        ["عند إجبار الهواء على الصعود يتمدد في الضغط الأقل ويبرد حتى يتكثف بخاره مطراً على الجانب المواجه للبحر.",
         "بعد فقدان رطوبته يهبط الهواء على السفح المعاكس فينضغط ويسخن وتقل رطوبته النسبية مسبباً جفافاً (ظل المطر)."],
        "تفسر هذه الظاهرة غزارة الأمطار على مرتفعات السروات الغربية وجفاف الهضاب الداخلية خلفها.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B22",
        "Meteorologists forecast clear, dry, sunny weather beneath a strong surface high-pressure system, whereas cloudy, stormy weather clusters around a low-pressure center. Why does vertical air motion produce these opposite conditions?",
        "يتوقع خبراء الأرصاد طقساً صافياً مشمساً وجافاً تحت مركز ضغط جوي مرتفع، بينما تتجمع الغيوم والعواصف حول مركز ضغط منخفض. ما حركة الهواء الرأسية المسببة لهاتين الحالتين المتعاكستين؟",
        [
            ("High pressure features sinking air that warms and evaporates clouds; low pressure draws surface air inward and upward to cool and condense clouds", "في الضغط المرتفع يهبط الهواء فيسخن وتتبخر السحب؛ وفي الضغط المنخفض يتجمع الهواء ويرتفع للأعلى فيبرد ويتكثف غيوماً"),
            ("High pressure pulls moist air straight upward into space", "يسحب الضغط المرتفع الهواء الرطب رأسياً إلى الفضاء الخارجي"),
            ("Low pressure forces cold stratosphere air downward onto the ocean", "يدفع الضغط المنخفض هواء الستراتوسفير البارد للأسفل نحو المحيط"),
            ("Air stops moving vertically in both pressure systems", "تتوقف حركة الهواء الرأسية تماماً في كلا النظامين"),
        ],
        "Sinking = compression warming = clear skies; Rising = expansion cooling = condensation/clouds.",
        "الهبوط يعني انضغاطاً وتسخيناً وصفاءً، والصعود يعني تمدداً وتبريداً وتكثفاً للغيوم.",
        "Contrast vertical divergence/subsidence in highs vs convergence/ascent in lows.",
        ["Surface low pressure pulls surrounding winds inward, forcing air to rise, expand, cool, and condense moisture into storms.",
         "Surface high pressure occurs where upper air sinks gently downward, warming adiabatically and suppressing cloud formation."],
        "Subtropical high-pressure belts (~30° latitude) account for Earth's major desert belts.",
        "نقارن هبوط الهواء في المرتفع الجوي بصعوده في المنخفض الجوي.",
        ["في المنخفض الجوي تتلاقى الرياح السطحية وتصعد للأعلى فتبرد وتتكثف غيوماً وأمطاراً.",
         "في المرتفع الجوي يهبط الهواء من الأعلى نحو السطح فيسخن وتتبخر الرطوبة ويسود الصحو."],
        "الأحزمة الصحراوية العالمية عند عرض 30° تقع تحت سيطرة مرتفعات جوية دائمة.",
    ))

    return qs


def _gen_sci_b23(start_idx: int) -> list[dict]:
    """G9-SCI-B23: Universal Gravitation, Kepler Orbits & Spring/Neap Tides (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = _svg_tides("Spring", "en")
    ar_0 = _svg_tides("Spring", "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B23",
        "When the Sun, Earth, and Moon align in a straight line (0° or 180°, at New Moon or Full Moon) as illustrated, what tidal condition occurs on Earth's oceans?",
        "عندما تصطف الشمس والأرض والقمر على استقامة واحدة (0° أو 180° عند المحاق أو البدر) كما في الشكل، أي حالة مد وجزر تحدث في المحيطات؟",
        [
            ("Spring tide, producing the largest difference between high tide and low tide", "المد العالي (الربيعي)، الذي ينتج أكبر فرق بين أعلى مد وأدنى جزر"),
            ("Neap tide, producing minimal tidal range with flat seas", "المد المنخفض (المحاقي)، الذي ينتج أقل مدى للمد والجزر"),
            ("Complete elimination of all ocean tides worldwide", "توقف ظاهرة المد والجزر كلياً في جميع أنحاء الأرض"),
            ("Ocean water freezes permanently at the Equator", "تجمد مياه المحيطات دائماً عند خط الاستواء"),
        ],
        "Aligned gravitational pulls from the Sun and Moon reinforce one another along the same axis.",
        "تتضافر قوتا جذب الشمس والقمر في الاتجاه نفسه عند الاصطفاف فتنتج أعلى مد وأدنى جزر.",
        "Match 0°/180° Sun-Earth-Moon alignment to Spring tides.",
        ["At New Moon and Full Moon, solar and lunar tidal bulges align constructively.",
         "Their combined pull raises unusually high high-tides and unusually low low-tides (maximum tidal range = Spring tide)."],
        "Remember: 'Spring' refers to water springing up highest, not the spring season.",
        "نربط اصطفاف الأجرام الثلاثة بتداخل قوى المد.",
        ["عند البدر والمحاق تتجمع قوتا المد الشمسي والقمري على خط واحد.",
         "يرتفع المد لأقصى مستوى وينخفض الجزر لأدنى مستوى فيُسمى المد الربيعي (العالي)."],
        "يحدث المد العالي مرتين شهرياً عند المحاق وعند البدر.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = _svg_tides("Neap", "en")
    ar_1 = _svg_tides("Neap", "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B23",
        "In the diagram, the Moon forms a 90° right angle with the Sun–Earth line (First or Third Quarter Moon). Which tidal pattern results?",
        "في المخطط الموضح، يصنع القمر زاوية قائمة 90° مع خط الشمس–الأرض (في التربيع الأول أو الأخير). أي نمط من المد والجزر ينتج عن هذا التعامد؟",
        [
            ("Neap tide, with the smallest difference between high tide and low tide", "المد المنخفض (المعتدل/المحاقي)، بأصغر فرق بين المد والجزر"),
            ("Spring tide, with extreme coastal flooding tides", "المد العالي جداً (الربيعي) بأقصى ارتفاع للمياه"),
            ("One single ocean bulge spanning only the South Pole", "انتفاخ بحري وحيد يغطي القطب الجنوبي فقط"),
            ("Reversal of Earth's orbital direction around the Sun", "انقلاب اتجاه دوران الأرض حول الشمس"),
        ],
        "When pulls act at 90° to one another, the Sun partially cancels the Moon's tidal bulge.",
        "عندما يتعامد اتجاه الجذب الشمسي والقمري بزاوية 90° يُضعف كل منهما أثر الآخر جزئياً.",
        "Match 90° quadrature geometry to Neap tides.",
        ["At First and Third Quarter Moon, solar and lunar tidal pulls act perpendicular to each other.",
         "Solar pull partially offsets lunar bulges, yielding moderate high tides and higher low tides (minimum range = Neap tide)."],
        "Spring tides alternate with Neap tides every ~7 days.",
        "نربط زاوية التعامد 90° بالمد المعتدل المنخفض.",
        ["في طوري التربيع الأول والأخير تتعامد قوتا المد الشمسي والقمري.",
         "يعادل المد الشمسي جزءاً من المد القمري فيقل الفرق بين المد والجزر (المد المنخفض)."],
        "يتناوب المد العالي والمنخفض كل نحو أسبوع خلال الشهر القمري.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B23",
        f"According to Newton's Law of Universal Gravitation ({m('F \\propto \\frac{m_1 m_2}{r^2}')}), if the center-to-center distance {m('r')} between two asteroids doubles while their masses stay constant, how does the gravitational attraction between them change?",
        f"وفق قانون الجذب العام لنيوتن ({m('F \\propto \\frac{m_1 m_2}{r^2}')})، إذا تضاعفت المسافة {m('r')} بين مركزي كويكبين إلى المثلين مع ثبات كتلتيهما، فكيف تتغير قوة التجاذب بينهما؟",
        [
            ("It drops to one-fourth (1/4) of its original strength", "تقل إلى الربع (1/4) من مقدارها الأصلي"),
            ("It drops to one-half (1/2) of its original strength", "تقل إلى النصف (1/2) من مقدارها الأصلي"),
            ("It doubles to twice (2×) its original strength", "تتضاعف إلى المثلين (2×) من مقدارها الأصلي"),
            ("It stays completely unchanged because mass is constant", "تبقى ثابتة تماماً لأن الكتلتين لم تتغيرا"),
        ],
        "Distance r appears squared in the denominator: doubling r divides force by 2² = 4.",
        "تظهر المسافة r مربّعة في المقام: مضاعفة المسافة تقسم القوة على 2² = 4.",
        f"Evaluate inverse-square scaling {m('F_{\\text{new}} = \\frac{F}{(2)^2}')}.",
        [f"Replacing {m('r')} with {m('2r')} yields {m('(2r)^2 = 4r^2')} in the denominator.",
         f"Thus {m('F_{\\text{new}} = \\frac{1}{4} F_{\\text{old}}')}."],
        "Inverse-square laws govern gravity, light intensity, and electrostatic force.",
        "نطبق قانون التربيع العكسي للجاذبية.",
        [f"بتعويض {m('2r')} في المقام يصبح {m('(2r)^2 = 4r^2')}.",
         f"تقل قوة الجذب إلى {m('\\frac{1}{4}')} قيمتها الأصلية."],
        "الجاذبية تتناسب عكسياً مع مربع المسافة.",
        diagram_en=_svg_gravity_pair("Gravitational Scaling", "تغير قوة التجاذب", "m1", "m2", "r -> 2r", "en"),
        diagram_ar=_svg_gravity_pair("Gravitational Scaling", "تغير قوة التجاذب", "m1", "m2", "r -> 2r", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B23",
        f"Kepler's Third Law for objects orbiting the Sun states {m('T^2 = a^3')}, where {m('T')} is orbital period in Earth years and {m('a')} is average orbital distance in astronomical units ({m('\\text{AU}')}). If an asteroid orbits at {m('a = 4\\text{ AU}')}, what is its orbital period {m('T')} in Earth years?",
        f"ينص قانون كبلر الثالث حول الشمس على {m('T^2 = a^3')}، حيث {m('T')} الزمن الدوري بالسنوات الأرضية و{m('a')} متوسط البعد بالوحدات الفلكية ({m('\\text{AU}')}). إذا دار كويكب على بعد {m('a = 4\\text{ AU}')}، فما زمنه المداري {m('T')} بالسنوات الأرضية؟",
        8, [16, 4, 64],
        "Cube 4 first (4³ = 64), then take the square root (√64 = 8).",
        "كعّب العدد 4 أولاً (4³ = 64)، ثم خذ الجذر التربيعي (√64 = 8).",
        f"Solve {m('T = \\sqrt{a^3}')}.",
        [f"Compute {m('a^3 = 4^3 = 64')}.",
         f"Take square root: {m('T = \\sqrt{64} = 8\\text{ years}')}."],
        f"Check: {m('8^2 = 64 = 4^3')}.",
        f"نحل {m('T^2 = a^3')}.",
        [f"نكعب البعد: {m('4^3 = 64')}.",
         f"نأخذ الجذر التربيعي: {m('T = \\sqrt{64} = 8\\text{ سنوات}')}."],
        f"التحقق: {m('8^2 = 64 = 4^3')}.",
        diagram_en=_svg_gravity_pair("Kepler Orbital Pair", "مدار كبلر حول الشمس", "Sun", "Asteroid", "a = 4 AU", "en"),
        diagram_ar=_svg_gravity_pair("Kepler Orbital Pair", "مدار كبلر حول الشمس", "الشمس", "كويكب", "a = 4 AU", "ar"),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B23",
        "Although the Sun is ~27 million times more massive than the Moon, the Moon creates more than twice as much tidal pull on Earth's oceans as the Sun. Why does the Moon dominate Earth's ocean tides?",
        "على الرغم من أن كتلة الشمس تفوق كتلة القمر بنحو 27 مليون مرة، فإن القمر يسبب أكثر من ضعف المد المحيطي الذي تسببه الشمس على الأرض. لماذا يهيمن القمر على ظاهرة المد والجزر؟",
        [
            ("Tidal force depends on gravitational difference across Earth's diameter (proportional to 1/r³), and the Moon is ~390 times closer than the Sun", "قوة المد تعتمد على فرق الجاذبية عبر قطر الأرض (تتناسب مع 1/r³)، والقمر أقرب بنحو 390 مرة من الشمس"),
            ("The Moon is composed of solid water ice that attracts liquid seawater", "يتكون القمر من جليد مائي صلب يجذب مياه المحيطات السائلة"),
            ("Solar light rays push ocean tides downward while lunar rays pull upward", "أشعة الشمس تدفع المد للأسفل بينما أشعة القمر تسحبه للأعلى"),
            ("Earth's oceans respond only to magnetic fields from the Moon", "تستجيب المحيطات فقط للمجال المغناطيسي القمري"),
        ],
        "Tides are caused by the gradient (stretch) of gravity across Earth's sides, which weakens rapidly with distance cubed (r³).",
        "ينتج المد عن فرق الجذب بين جانبي الأرض القريب والبعيد، وهذا الفرق يتناقص بشدة مع مكعب المسافة (r³).",
        "Explain inverse-cube tidal differential gravity across Earth's radius.",
        ["Direct pull holds Earth in orbit (varying as M/r²), whereas tidal stretching varies as M/r³.",
         "Because the Sun is ~390 times farther away, dividing by (390)³ ≈ 59 million reduces solar tidal force below half of lunar tidal force."],
        "Because the Sun still contributes nearly half as much tide as the Moon, alignment matters dramatically.",
        "نفرق بين الجاذبية المباشرة (M/r²) والقوة المدية التفاضلية (M/r³).",
        ["يعتمد التمدد المدي للمحيطات على فرق الجاذبية عبر قطر الأرض ويتناسب مع M/r³.",
         "بما أن الشمس أبعد بنحو 390 مرة، فإن مكعب هذه المسافة يضعف أثرها المدي ليصبح أقل من نصف أثر القمر القريب."],
        "لذلك تتغير ارتفاعات المد بشكل واضح بين الاقتران والتربيع.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B23",
        f"Between two moons of masses {m('m_1')} and {m('m_2')} separated by {m('r')}, suppose {m('m_1')} is tripled, {m('m_2')} is doubled, and separation {m('r')} is tripled. What is the new gravitational force {m('F_{\\text{new}}')} in terms of the original force {m('F')}?",
        f"بين قمرين كتلتاهما {m('m_1')} و{m('m_2')} تفصلهما مسافة {m('r')}، إذا تضاعفت {m('m_1')} ثلاث مرات، وتضاعفت {m('m_2')} مرتين، وتضاعفت المسافة {m('r')} ثلاث مرات. ما مقدار قوة الجذب الجديدة {m('F_{\\text{new}}')} بدلالة القوة الأصلية {m('F')}؟",
        [
            (m(r"\frac{2}{3} F"), m(r"\frac{2}{3} F")),
            (m(r"2 F"), m(r"2 F")),
            (m(r"6 F"), m(r"6 F")),
            (m(r"\frac{2}{9} F"), m(r"\frac{2}{9} F")),
        ],
        "Multiply mass scale factors in the numerator (3 × 2 = 6) and divide by the squared distance factor (3² = 9).",
        "اضرب عوامل الكتلتين في البسط (3 × 2 = 6) واقسم على مربع عامل المسافة (3² = 9).",
        f"Evaluate factor {m('\\frac{3 \\times 2}{3^2}')}.",
        [f"Numerator scales by {m('3 \\times 2 = 6')}; denominator scales by {m('3^2 = 9')}.",
         f"Force factor = {m('\\frac{6}{9} = \\frac{2}{3}')}, giving {m('\\frac{2}{3} F')}."],
        "Check: mass increases by 6× while distance-squared cuts it by 9×.",
        f"نحسب معامل التغير {m('\\frac{3 \\times 2}{3^2}')}.",
        [f"البسط يزداد بمعامل {m('3 \\times 2 = 6')} والمقام يزداد بمعامل {m('3^2 = 9')}.",
         f"النسبة = {m('\\frac{6}{9} = \\frac{2}{3} F')}."],
        "التحقق: الكتلتان ترفعان القوة 6 مرات والمسافة تخفضها 9 مرات فالمحصلة الثلثان.",
        diagram_en=_svg_gravity_pair("Mass and Distance Scaling", "تغير الكتلتين والمسافة", "3 m1", "2 m2", "3 r", "en"),
        diagram_ar=_svg_gravity_pair("Mass and Distance Scaling", "تغير الكتلتين والمسافة", "3 m1", "2 m2", "3 r", "ar"),
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B23",
        f"A communication satellite weighs {m('800\\text{ N}')} on Earth's surface (at distance {m('1\\,R_E')} from Earth's center). What gravitational force in {m('\\text{N}')} acts on it when placed at an altitude equal to one full Earth radius ({m('h = R_E')}) above the surface?",
        f"يزن قمر صناعي {m('800\\text{ نيوتن}')} على سطح الأرض (على بُعد {m('1\\,R_E')} من مركز الأرض). ما مقدار قوة الجاذبية المؤثرة فيه بالنيوتن عندما يوضع على ارتفاع يساوي نصف قطر الأرض ({m('h = R_E')}) فوق السطح؟",
        200, [400, 100, 800],
        "Distance from Earth's CENTER becomes R_E + R_E = 2 R_E, so force divides by 2² = 4.",
        "المسافة عن مركز الأرض تصبح R_E + R_E = 2 R_E، فتُقسم القوة على 2² = 4.",
        f"Measure distance {m('r')} from Earth's center, then apply {m('F \\propto 1/r^2')}.",
        [f"Total radial distance from Earth's center: {m('r = R_E + R_E = 2\\,R_E')}.",
         f"Gravitational weight = {m('\\frac{800}{2^2} = \\frac{800}{4} = 200\\text{ N}')}."],
        "Check: forgetting Earth's own radius is the classic trap here!",
        "نقيس البعد من مركز الأرض أولاً ثم نطبق التربيع العكسي.",
        [f"المسافة الكلية من مركز الأرض = {m('R_E + R_E = 2\\,R_E')}.",
         f"الوزن على هذا الارتفاع = {m('\\frac{800}{2^2} = 200\\text{ نيوتن}')}."],
        "التحقق: انتبه لجمع نصف قطر الأرض مع الارتفاع فوق السطح.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B23",
        "According to Kepler's Second Law (a planet sweeps out equal orbital areas in equal intervals of time), how does a comet's speed at perihelion (closest approach to the Sun) compare to its speed at aphelion (farthest point)?",
        "وفق قانون كبلر الثاني (يمسح الكوكب أو المذنب مساحات متساوية في أزمنة متساوية)، كيف تقارن سرعة مذنب عند الحضيض (أقرب نقطة للشمس) بسرعته عند الأوج (أبعد نقطة)؟",
        [
            ("It moves fastest at perihelion and slowest at aphelion", "تكون سرعته أكبر ما يمكن عند الحضيض وأبطأ ما يمكن عند الأوج"),
            ("It moves slowest at perihelion and fastest at aphelion", "تكون سرعته أبطأ عند الحضيض وأسرع عند الأوج"),
            ("It maintains the exact same constant speed around the entire ellipse", "يحافظ على السرعة نفسها ثابتة طوال مداره الإهليلجي"),
            ("It comes to a complete stop at aphelion before falling straight in", "يتوقف تماماً عند الأوج قبل أن يسقط نحو الشمس"),
        ],
        "To sweep out the same wedge area in equal time with a shorter Sun-to-comet radius r, the arc traveled must be much longer (faster).",
        "لمسح المساحة نفسها مع قِصر نصف القطر عند الحضيض لا بد أن يقطع المذنب قوساً أطول أي بسرعة أكبر.",
        "Apply Kepler's Equal-Areas Law to narrow vs long orbital wedges.",
        ["At perihelion, distance r to the Sun is smallest, so the comet must cover a long arc in a fixed Δt — maximum speed.",
         "At aphelion, radius r is huge, so even a short slow arc sweeps the same area — minimum speed."],
        "Energy conservation agrees: gravitational PE converts into maximum KE at perihelion.",
        "نطبق قانون المساحات المتساوية على المدار الإهليلجي.",
        ["عند الحضيض يكون الذراع قصيراً فيلزم قطع قوس طويل خلال الزمن نفسه لتحقيق المساحة نفسها (سرعة عظمى).",
         "عند الأوج يكون الذراع طويلاً فيكفي قوس قصير لمسح المساحة نفسها (سرعة دنيا)."],
        "هذا يتفق أيضاً مع تحول طاقة الوضع إلى طاقة حركية عظمى عند الاقتراب من الشمس.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B23",
        f"A newly discovered planet orbits a star of one solar mass with an orbital period of {m('T = 27\\text{ years}')}. Using {m('a^3 = T^2')}, what is the planet's average orbital radius {m('a')} in {m('\\text{AU}')}?",
        f"يدور كوكب مكتشف حديثاً حول نجم كتلته تساوي كتلة الشمس بزمن مداري مقداره {m('T = 27\\text{ سنة}')}. باستخدام {m('a^3 = T^2')}، ما متوسط نصف قطر مداره {m('a')} بالوحدات الفلكية ({m('\\text{AU}')})؟",
        9, [3, 81, 27],
        "Square T first (27² = 729), then take the cube root (or notice 27 = 3³, so 27² = 3⁶ and (3⁶)^(1/3) = 3²).",
        "ربّع 27 أولاً ثم خذ الجذر التكعيبي (أو لاحظ أن 27 = 3³، إذن 27² = (3²)³).",
        f"Solve {m('a^3 = 27^2')}.",
        [f"Rewrite {m('27 = 3^3')}, so {m('T^2 = (3^3)^2 = 3^6 = (3^2)^3 = 9^3')}.",
         f"Taking cube roots gives {m('a = 9\\text{ AU}')}."],
        f"Check: {m('9^3 = 729')} and {m('27^2 = 729')}.",
        f"نحل {m('a^3 = 27^2')}.",
        [f"نكتب {m('27^2 = (3^3)^2 = 3^6 = (3^2)^3 = 9^3')}.",
         f"بأخذ الجذر التكعيبي: {m('a = 9\\text{ AU}')}."],
        f"التحقق: {m('9^3 = 729 = 27^2')}.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B23",
        "Most coastal harbors experience TWO high tides and TWO low tides roughly every 24 hours 50 minutes rather than just one high tide per day. Why do two tidal bulges exist on opposite sides of Earth simultaneously?",
        "تشهد معظم الموانئ الساحلية مدّين وجزرين كل 24 ساعة و50 دقيقة تقريباً بدلاً من مدّ واحد يومياً. لماذا يتكون انتفاخان مدّيان على جانبي الأرض المتقابلين في الوقت نفسه؟",
        [
            ("One bulge faces the Moon where lunar pull is strongest; the opposite bulge forms where lunar pull on water is weaker than on Earth's center (inertia)", "يتكون انتفاخ نحو القمر حيث يكون جذبه أقوى، وانتفاخ مقابل على الجانب الآخر حيث يكون جذب القمر للماء أضعف من جذبه لمركز الأرض"),
            ("One bulge is made by the Sun and the other is caused by wind waves", "أحد الانتفاخين تصنعه الشمس والآخر تسببه أمواج الرياح"),
            ("Earth's outer core splashes water upward twice every 12 hours", "يقذف اللب الخارجي الماء للأعلى مرتين كل 12 ساعة"),
            ("One bulge is freshwater from rivers and the opposite bulge is seawater", "انتفاخ من مياه الأنهار العذبة وآخر من مياه المحيطات"),
        ],
        "Differential gravity pulls the near ocean harder than Earth's center, and pulls Earth's center harder than the far ocean.",
        "الجاذبية التفاضلية تسحب المحيط القريب أكثر من مركز الأرض، وتسحب مركز الأرض أكثر من المحيط البعيد فتتركه منتفخاً للخارج.",
        "Explain both sub-lunar and anti-lunar tidal bulges.",
        ["Water directly beneath the Moon is closer and pulled toward the Moon more strongly than Earth's rigid center.",
         "Water on the far side is farther away, experiencing weaker lunar pull than Earth's center — leaving an outward inertia bulge opposite the Moon."],
        "As Earth rotates daily beneath both bulges, coasts pass through two high tides (~12 h 25 min apart).",
        "نفسر الانتفاخين القريب والبعيد بالجاذبية التفاضلية.",
        ["ينجذب الماء المواجه للقمر بقوة أكبر من مركز الأرض فيبرز نحو القمر.",
         "ينجذب مركز الأرض بقوة أكبر من ماء الجانب البعيد فيبقى الماء البعيد متخلفاً منتفخاً للخارج."],
        "مع دوران الأرض اليومي يمر كل ساحل تحت الانتفاخين أي مدّان يومياً.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B23",
        f"A scientific probe weighs {m('900\\text{ N}')} on Earth's surface (distance {m('1\\,R_E')} from Earth's center). At what distance from Earth's center, measured in Earth radii ({m('R_E')}), does the probe's weight drop to {m('100\\text{ N}')}?",
        f"يزن مسبار علمي {m('900\\text{ نيوتن}')} على سطح الأرض (على بُعد {m('1\\,R_E')} من المركز). على أي بُعد من مركز الأرض بوحدة أنصاف أقطار الأرض ({m('R_E')}) ينخفض وزنه إلى {m('100\\text{ نيوتن}')}؟",
        3, [9, 2, 4.5],
        "Weight drops by a factor of 900 / 100 = 9; take the square root of 9 to find the distance multiple.",
        "انخفض الوزن بمعامل 900 / 100 = 9؛ خذ الجذر التربيعي للعدد 9 لإيجاد مضاعف المسافة.",
        f"Solve {m('\\frac{900}{100} = r^2')} for {m('r')} in units of {m('R_E')}.",
        [f"Force ratio: {m('\\frac{900}{100} = 9')}.",
         f"By inverse-square law, {m('r^2 = 9 \\implies r = 3\\,R_E')} from center."],
        f"Check: at {m('3\\,R_E')} (altitude {m('2\\,R_E')}), weight = {m('900 / 3^2 = 100\\text{ N}')}.",
        f"نطبق التربيع العكسي {m('r^2 = \\frac{900}{100}')}.",
        [f"انخفض الوزن {m('9')} مرات، إذن {m('r^2 = 9')}.",
         f"البعد عن المركز = {m('3\\,R_E')}."],
        f"التحقق: {m('900 / 3^2 = 100\\text{ نيوتن}')}.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B23",
        f"An exoplanet has {m('3')} times Earth's mass and {m('2')} times Earth's radius. An astronaut who weighs {m('800\\text{ N}')} on Earth lands on this exoplanet. What is the astronaut's weight there in {m('\\text{N}')}?",
        f"كوكب خارجي كتلته {m('3')} أضعاف كتلة الأرض ونصف قطره ضعف نصف قطر الأرض. هبط عليه رائد فضاء يزن {m('800\\text{ نيوتن}')} على الأرض. كم يبلغ وزنه على سطح هذا الكوكب بالنيوتن؟",
        600, [1200, 2400, 400],
        "Surface gravity scales as M / R² = 3 / 2² = 3/4 of Earth gravity.",
        "يتناسب تسارع الجاذبية السطحي مع M / R² = 3 / 2² = 3/4 جاذبية الأرض.",
        f"Multiply Earth weight by {m('\\frac{M_p/M_E}{(R_p/R_E)^2}')}.",
        [f"Gravity ratio: {m('\\frac{g_p}{g_E} = \\frac{3}{2^2} = \\frac{3}{4} = 0.75')}.",
         f"Weight on exoplanet = {m('800 \\times 0.75 = 600\\text{ N}')}."],
        "Check: mass triples pull, but doubling radius weakens it fourfold -> 3/4 overall.",
        f"نحسب نسبة الجاذبية {m('\\frac{3}{2^2} = \\frac{3}{4}')}.",
        [f"جاذبية الكوكب = {m('0.75')} من جاذبية الأرض.",
         f"وزن الرائد = {m('800 \\times 0.75 = 600\\text{ نيوتن}')}."],
        "التحقق: الكتلة تضرب بـ 3 ومربع نصف القطر يقسم على 4.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B23",
        "Inside the International Space Station orbiting 400 km above Earth, Earth's gravitational acceleration is still about 8.7 m/s² (~89% of surface gravity!). Yet astronauts float freely inside. Why do they experience apparent weightlessness?",
        "داخل محطة الفضاء الدولية التي تدور على ارتفاع 400 كم، لا تزال جاذبية الأرض تبلغ نحو 8.7 م/ث² (~89% من الجاذبية السطحية!). ومع ذلك يطفو رواد الفضاء بحرية. لماذا يشعرون بانعدام الوزن الظاهري؟",
        [
            ("Both the station and the astronauts are in continuous free fall around Earth at the same gravitational acceleration", "كل من المحطة ورواد الفضاء في حالة سقوط حر مستمر حول الأرض بالتسارع الجاذبي نفسه"),
            ("Earth's atmosphere pushes them upward with buoyant air lift", "يدفعهم الغلاف الجوي للأعلى بقوة طفو هوائية"),
            ("Solar wind cancels Earth's gravity exactly at 400 km altitude", "تلغي الرياح الشمسية جاذبية الأرض تماماً عند ارتفاع 400 كم"),
            ("Astronauts lose 100% of their inertial mass outside Earth's surface", "يفقد رواد الفضاء 100% من كتلتهم بمجرد مغادرة السطح"),
        ],
        "Think about being inside a falling elevator whose floor drops at the exact same rate you do: no normal support force acts on your feet.",
        "يشبه ذلك وجودك داخل مصعد يسقط سقوطاً حراً: أنت والمحطة تسقطان معاً حول الأرض فتنعدم قوة التلامس الداعمة.",
        "Explain orbital motion as perpetual horizontal free fall.",
        ["Gravity provides the centripetal force curving the ISS path around Earth's horizon.",
         "Because astronauts fall along the exact same trajectory as the station walls, there is zero normal force pressing them against the floor."],
        "Without gravity, the ISS would shoot off into deep space in a straight line.",
        "نفسر الدوران المداري بوصفه سقوطاً حراً دائماً حول انحناء الأرض.",
        ["تجذب الأرض المحطة والرواد بالتسارع نفسه ليدوروا حول الكوكب في سقوط حر متصل.",
         "نظراً لتساوي التسارعين تنعدم قوة رد الفعل بين أقدام الرواد وأرضية المحطة فيطفون."],
        "لو انعدمت الجاذبية في المدار لانطلقت المحطة في خط مستقيم نحو الفضاء العميق.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B23",
        f"A small star of mass {m('M')} and a larger star of mass {m('4M')} lie {m('300,000\\text{ km}')} apart. At what distance in {m('\\text{km}')} from the smaller star {m('M')} along the line between them does a probe experience ZERO net gravitational force?",
        f"يفصل بين نجم صغير كتلته {m('M')} ونجم أكبر كتلته {m('4M')} مسافة {m('300,000\\text{ كم}')}. على أي مسافة بالكيلومتر من النجم الأصغر {m('M')} (على الخط الواصل بينهما) تنعدم محصلة الجاذبية على مسبار؟",
        100000, [150000, 200000, 60000],
        "Equate magnitudes: G M / x² = G(4M) / (D - x)². Take square roots of both sides: 1/x = 2/(D - x).",
        "ساوِ قوتي الجذب: M/x² = 4M/(D-x)² ثم خذ الجذر التربيعي للطرفين: 1/x = 2/(D-x).",
        f"Solve {m('\\frac{M}{x^2} = \\frac{4M}{(300,000 - x)^2}')}.",
        [f"Cancel {m('M')} and take positive square roots: {m('\\frac{1}{x} = \\frac{2}{300,000 - x}')}.",
         f"Cross-multiply: {m('300,000 - x = 2x \\implies 3x = 300,000 \\implies x = 100,000\\text{ km}')}."],
        f"Check: distance to {m('4M')} is {m('200,000\\text{ km}')} (2× further), and {m('4 / 2^2 = 1')}.",
        f"نساوي القوتين {m('\\frac{M}{x^2} = \\frac{4M}{(300,000 - x)^2}')}.",
        [f"بأخذ الجذر التربيعي للطرفين: {m('\\frac{1}{x} = \\frac{2}{300,000 - x}')}.",
         f"بالضرب التبادلي: {m('300,000 - x = 2x')} ومنها {m('x = 100,000\\text{ كم}')}."],
        f"التحقق: البعد عن النجم الأكبر {m('200,000\\text{ كم}')} أي ضعف البعد، و{m('4 / 2^2 = 1')}.",
        diagram_en=_svg_gravity_pair("Zero-Gravity Balance Point", "نقطة انعدام الجاذبية", "Mass M", "Mass 4M", "D = 300,000 km", "en"),
        diagram_ar=_svg_gravity_pair("Zero-Gravity Balance Point", "نقطة انعدام الجاذبية", "الكتلة M", "الكتلة 4M", "D = 300,000 كم", "ar"),
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B23",
        "A lunar synodic cycle from New Moon back to New Moon takes ~29.5 days. How frequently do Spring tides occur during a single lunar month, and what follows roughly 7.4 days later?",
        "تستغرق الدورة القمرية الاقترانية من المحاق إلى المحاق التالي نحو 29.5 يوماً. كم مرة يتكرر المد العالي (الربيعي) خلال الشهر القمري الواحد، وما الذي يليه بعد ~7.4 أيام؟",
        [
            ("Spring tides occur twice per lunar month (at New Moon and Full Moon, ~14.8 days apart), followed ~7.4 days later by Neap tides", "يحدث المد العالي مرتين شهرياً (عند المحاق والبدر كل ~14.8 يوماً)، ويتبعه بعد ~7.4 أيام المد المنخفض"),
            ("Spring tides occur once a year only during March and April", "يحدث المد العالي مرة واحدة سنوياً في فصل الربيع فقط"),
            ("Spring tides occur every 24 hours followed immediately by Neap tides 12 hours later", "يحدث المد العالي كل 24 ساعة ويليه المد المنخفض بعد 12 ساعة"),
            ("Spring tides occur four times per lunar month at every quarter phase", "يحدث المد العالي أربع مرات شهرياً في كل ربع من أطوار القمر"),
        ],
        "Count both alignment points per orbit: 0° (New) and 180° (Full) — half a 29.5-day orbit apart.",
        "يحدث الاصطفاف مرتين في كل دورة قمرية (محاق 0° وبدر 180°)، وبينهما التعامد (تربيع أول وثانٍ).",
        "Map the 29.5-day lunar phase cycle onto Spring and Neap timing.",
        ["Spring tides happen at both 0° (New Moon) and 180° (Full Moon), giving 2 Spring tides per ~29.5-day month (~14.8 days apart).",
         "Quarter phases (90° and 270°) sit halfway between them (~7.4 days after each Spring tide), producing 2 Neap tides."],
        "Each ~29.5-day month therefore contains 2 Spring tides and 2 Neap tides.",
        "نربط أطوار القمر الأربعة بدورة المد خلال 29.5 يوماً.",
        ["يحدث المد العالي مرتين عند المحاق والبدر بفارق ~14.8 يوماً.",
         "بعد نحو ربع دورة (~7.4 أيام) يصل القمر للتربيع فتحدث حالة المد المنخفض."],
        "يتكرر المد العالي مرتين والمنخفض مرتين في كل شهر قمري.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    return qs


def _gen_sci_b24(start_idx: int) -> list[dict]:
    """G9-SCI-B24: H-R Diagram, Spectral Colors, Luminosity Scaling & Stellar Evolution (15 Qs)."""
    qs = []

    # --- EASY (0..4) ---
    d_0 = _svg_hr_diagram("Star X", "نجم X", 0.85, 0.52, "en")
    ar_0 = _svg_hr_diagram("Star X", "نجم X", 0.85, 0.52, "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx), LEVEL, T_EARTH, _diff(0), "G9-SCI-B24",
        "On the Hertzsprung–Russell (H–R) diagram, Star X is plotted in the upper-right region (cool ~3,500 K surface yet very high luminosity). To which stellar group does Star X belong?",
        "في مخطط هرتزسبرونغ–راسل (H-R) الموضح، يقع النجم X في المنطقة العلوية اليمنى (سطح بارد ~3,500 كلفن لكن بلمعان عالٍ جداً). إلى أي فئة نجمية ينتمي النجم X؟",
        [
            ("Red Giants / Red Supergiants", "العمالقة الحمر أو العمالقة العظمى الحمر"),
            ("White Dwarfs", "الأقزام البيضاء"),
            ("Blue Main-Sequence Stars", "نجوم التسلسل الرئيسي الزرقاء"),
            ("Brown Dwarf Remnants", "بقايا الأقزام البنية المعتمة"),
        ],
        "Cool surface (~3,500 K) radiates red light, and huge total luminosity from a cool surface requires an enormous radius (Red Giant).",
        "السطح البارد (~3,500 K) يبدو أحمر اللون، واللمعان العالي من سطح بارد يتطلب مساحة سطح عملاقة.",
        "Read the H-R axes: Cool = Right, High Luminosity = Top.",
        ["Right side of the H-R diagram represents cool red stars; upper side represents high luminosity.",
         "Upper-right is therefore occupied by huge Red Giants and Red Supergiants (such as Betelgeuse)."],
        "Remember: White Dwarfs lie in the opposite lower-left corner (hot yet dim).",
        "نقرأ محوري المخطط: يمين = بارد، أعلى = شديد اللمعان.",
        ["اليمين يشير إلى نجوم باردة حمراء، والأعلى يشير إلى لمعان إجمالي هائل.",
         "تجمع الزاوية العلوية اليمنى فئة العمالقة الحمر والعمالقة العظمى الحمر."],
        "بينما تقع الأقزام البيضاء في الزاوية المعاكسة السفلى اليسرى.",
        diagram_en=d_0, diagram_ar=ar_0,
    ))

    d_1 = _svg_hr_diagram("Star Y", "نجم Y", 0.16, 0.28, "en")
    ar_1 = _svg_hr_diagram("Star Y", "نجم Y", 0.16, 0.28, "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 1), LEVEL, T_EARTH, _diff(1), "G9-SCI-B24",
        "Star Y appears in the lower-left region of the H–R diagram (very hot >15,000 K surface yet extremely low luminosity). Which type of star is Star Y?",
        "يظهر النجم Y في المنطقة السفلية اليسرى من مخطط H-R (سطح حار جداً > 15,000 كلفن لكن بلمعان كلي ضعيف جداً). ما نوع النجم Y؟",
        [
            ("White Dwarf — a hot, Earth-sized stellar core remnant", "قزم أبيض — نواة نجم حارة وصغيرة بحجم الأرض تقريباً"),
            ("Red Supergiant — a huge expanding outer envelope", "عملاق أحمر عظيم بغلاف متمدد هائل"),
            ("Blue O-type Supergiant — a bright massive young star", "عملاق أزرق عظيم فتي شديد السطوع"),
            ("Protostar glowing solely in infrared inside dust", "نجم أولي يشع بالأشعة تحت الحمراء داخل سحابة غبارية"),
        ],
        "High temperature (left) but tiny total light output (bottom) implies a remarkably tiny radiating surface area.",
        "الحرارة العالية (يسار) مع السطوع الضعيف جداً (أسفل) تعني أن مساحة سطح النجم صغيرة للغاية.",
        "Read lower-left H-R region: Hot + Dim = tiny White Dwarf.",
        ["Left side indicates white-hot temperatures; bottom indicates very faint total luminosity.",
         "Only an Earth-sized dense core remnant (White Dwarf) can be both extremely hot and very dim."],
        "White Dwarfs no longer fuse hydrogen; they slowly radiate stored heat over billions of years.",
        "نقرأ المنطقة السفلية اليسرى: حار جداً وضعيف اللمعان.",
        ["اليسار يعني حرارة سطحية مرتفعة، والأسفل يعني إضاءة إجمالية منخفضة.",
         "يتحقق ذلك فقط في الأقزام البيضاء التي تمتلك نصف قطر صغيراً جداً يعادل الأرض تقريباً."],
        "القزم الأبيض يبرد ببطء عبر مليارات السنين دون اندماج نووي.",
        diagram_en=d_1, diagram_ar=ar_1,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 2), LEVEL, T_EARTH, _diff(2), "G9-SCI-B24",
        "In astronomy, star color directly reveals surface temperature. Which color ordering correctly lists stars from COOLEST surface temperature to HOTTEST surface temperature?",
        "في علم الفلك، يكشف لون النجم مباشرة عن درجة حرارة سطحه. أي ترتيب يصف النجوم من الأبرد سطحاً إلى الأسخن سطحاً؟",
        [
            ("Red → Orange → Yellow (Sun) → White → Blue-white", "أحمر ← برتقالي ← أصفر (الشمس) ← أبيض ← أزرق-أبيض"),
            ("Blue → White → Yellow → Orange → Red", "أزرق ← أبيض ← أصفر ← برتقالي ← أحمر"),
            ("Yellow → Red → Blue → Green → Black", "أصفر ← أحمر ← أزرق ← أخضر ← أسود"),
            ("White → Red → Blue → Orange → Yellow", "أبيض ← أحمر ← أزرق ← برتقالي ← أصفر"),
        ],
        "Remember everyday physics reversed from plumbing taps: red-hot coals are cooler than white-hot or blue-hot flames!",
        "تذكر حرارة اللهب: الجمر الأحمر أبرد من اللهب الأبيض ومن اللهب الأزرق الأشد حرارة!",
        "Order thermal peak color by Wien's wavelength law (cool longwave red -> hot shortwave blue).",
        ["Cool stars (~3,000 K) emit mostly red/infrared light; solar stars (~5,800 K) glow yellow-white.",
         "Extreme O- and B-type stars (15,000–40,000 K) emit strongly in blue and ultraviolet, appearing blue-white."],
        "Shorter wavelength blue photons carry higher energy than red photons.",
        "نرتب الألوان حسب طول الموجة والطاقة الحرارية.",
        ["النجوم الباردة (~3,000 K) تبدو حمراء، والمتوسطة كالشمس (~5,800 K) صفراء بيضاء.",
         "النجوم الأشد حرارة (> 15,000 K) تشع بشدة في الأزرق وفوق البنفسجي فتبدو زرقاء."],
        "الضوء الأزرق يحمل طاقة أعلى لكل فوتون من الضوء الأحمر.",
    ))

    d_3 = _svg_hr_diagram("Sun", "الشمس", 0.50, 0.66, "en")
    ar_3 = _svg_hr_diagram("Sun", "الشمس", 0.50, 0.66, "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 3), LEVEL, T_EARTH, _diff(3), "G9-SCI-B24",
        "Roughly 90% of observed stars — including our Sun — lie along the diagonal Main Sequence band of the H–R diagram. What core nuclear process supplies their steady energy output?",
        "تقع نحو 90% من النجوم المرصودة — ومنها شمسنا — على شريط التسلسل الرئيسي القطري في مخطط H-R. ما العملية النووية في النواة التي تمدها بهذه الطاقة المستقرة؟",
        [
            ("Nuclear fusion converting hydrogen nuclei into helium nuclei in the core", "الاندماج النووي الذي يحوّل نوى الهيدروجين إلى نوى هيليوم داخل النواة"),
            ("Chemical combustion of hydrogen gas with atmospheric oxygen", "الاحتراق الكيميائي لغاز الهيدروجين مع الأكسجين الجوي"),
            ("Nuclear fission splitting heavy uranium atoms into lead", "الانشطار النووي لذرات اليورانيوم الثقيلة إلى رصاص"),
            ("Gravitational shrinking with zero nuclear reactions", "الانكماش الثقالي المستمر دون أي تفاعلات نووية"),
        ],
        "Stars convert tiny fractions of hydrogen mass directly into energy via E = mc².",
        "تحوّل النجوم جزءاً ضئيلاً من كتلة الهيدروجين إلى طاقة هائلة عبر الاندماج النووي.",
        "Identify core hydrogen-to-helium fusion as the defining Main Sequence stage.",
        ["Extreme core temperatures (~15 million K in the Sun) overcome proton repulsion so four hydrogen nuclei fuse into helium.",
         "Outward thermal radiation pressure balances inward gravity (hydrostatic equilibrium)."],
        "Main Sequence lifetime ends when core hydrogen runs out.",
        "نحدد اندماج الهيدروجين إلى هيليوم بوصفه مصدر طاقة التسلسل الرئيسي.",
        ["عند حرارة النواة الفائقة (~15 مليون كلفن) تندمج نوى الهيدروجين لتكوين الهيليوم.",
         "يوازن ضغط الإشعاع الخارجي قوة الجاذبية للداخل في استقرار طويل الأمد."],
        "تنتهي مرحلة التسلسل الرئيسي عند نفاد الهيدروجين في النواة.",
        diagram_en=d_3, diagram_ar=ar_3,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 4), LEVEL, T_EARTH, _diff(4), "G9-SCI-B24",
        "After exhausting core hydrogen, what sequence of evolutionary stages will a low-to-medium-mass star like our Sun (~1 solar mass) follow?",
        "بعد استنفاد الهيدروجين في نواتها، ما تسلسل المراحل التطورية الذي ستسلكه نجمة منخفضة إلى متوسطة الكتلة مثل الشمس (~1 كتلة شمسية)؟",
        [
            ("Main Sequence → Red Giant → Planetary Nebula → White Dwarf", "التسلسل الرئيسي ← عملاق أحمر ← سديم كوكبي ← قزم أبيض"),
            ("Main Sequence → Red Supergiant → Supernova → Black Hole", "التسلسل الرئيسي ← عملاق عظيم أحمر ← مستعر أعظم ← ثقب أسود"),
            ("White Dwarf → Blue Giant → Neutron Star → Nebula", "قزم أبيض ← عملاق أزرق ← نجم نيوتروني ← سديم"),
            ("Main Sequence → Direct Explosion into a Neutron Star", "التسلسل الرئيسي ← انفجار مباشر إلى نجم نيوتروني"),
        ],
        "Sun-like stars do NOT explode as supernovae; they shed outer gas gently into a glowing planetary nebula.",
        "النجوم الشبيهة بالشمس لا تنفجر كمستعر أعظم، بل تلفظ غلافها بهدوء مكونة سديماً كوكبياً ثم قزماً أبيض.",
        "Trace low/solar-mass stellar evolution path.",
        ["When core hydrogen depletes, the outer envelope swells and cools into a Red Giant while helium fuses to carbon/oxygen.",
         "Eventually the outer shells drift away as a Planetary Nebula, leaving the exposed hot carbon-oxygen White Dwarf core."],
        "Only stars above ~8 solar masses end in core-collapse supernovae.",
        "نتتبع مسار تطور النجوم الشبيهة بالشمس.",
        ["عند نفاد هيدروجين النواة يتمدد الغلاف الخارجي ويبرد فيتحول النجم إلى عملاق أحمر.",
         "ثم ينقشع الغلاف مكوناً سديماً كوكبياً وتتبقى النواة الساخنة على هيئة قزم أبيض."],
        "الانفجار كمستعر أعظم يختص بالنجوم فائقة الكتلة (> 8 كتل شمسية).",
        diagram_en=_svg_hr_diagram("Sun (1 M)", "الشمس", 0.50, 0.66, "en"),
        diagram_ar=_svg_hr_diagram("Sun (1 M)", "الشمس", 0.50, 0.66, "ar"),
    ))

    # --- MEDIUM (5..9) ---
    qs.append(make_science_concept_q(
        _qid(start_idx + 5), LEVEL, T_EARTH, _diff(5), "G9-SCI-B24",
        "Astronomers classify stars by spectral sequence O–B–A–F–G–K–M from hottest to coolest. Suppose Star 1 is spectral class B, Star 2 is G (like our Sun), and Star 3 is M. Which comparison is correct?",
        "يصنف الفلكيون النجوم طيفياً وفق الترتيب O–B–A–F–G–K–M من الأعلى حرارة إلى الأبرد. إذا كان النجم 1 من الفئة B، والنجم 2 من الفئة G (كالشمس)، والنجم 3 من الفئة M، فأي مقارنة صحيحة؟",
        [
            ("Star 1 (B) is hottest and blue-white; Star 2 (G) is intermediate yellow-white; Star 3 (M) is coolest and red", "النجم 1 (B) هو الأسخن وأزرق-أبيض؛ النجم 2 (G) متوسط أصفر-أبيض؛ النجم 3 (M) هو الأبرد وأحمر"),
            ("Star 3 (M) is hottest and blue; Star 1 (B) is coolest and red", "النجم 3 (M) هو الأسخن وأزرق؛ والنجم 1 (B) هو الأبرد وأحمر"),
            ("All three stars have the same 5,800 K surface temperature", "النجوم الثلاثة لها درجة حرارة السطح نفسها (5,800 كلفن)"),
            ("Star 2 (G) is hotter than Star 1 (B) because G lies near the end", "النجم 2 (G) أسخن من النجم 1 (B)"),
        ],
        "Memorize the standard Harvard sequence from hottest (O) to coolest (M): O-B-A-F-G-K-M.",
        "احفظ الترتيب الطيفي من الأسخن (O) إلى الأبرد (M): O-B-A-F-G-K-M.",
        "Read surface temperature downward along O -> B -> A -> F -> G -> K -> M.",
        ["Class B (~10,000–30,000 K) shines blue-white and far hotter than G (~5,800 K).",
         "Class M (~3,000 K) sits at the coolest red end of the spectrum."],
        "Notice alphabetical order was historical, not thermal — rely on OBAFGKM.",
        "نرتب الفئات الطيفية حسب التدرج الحراري O-B-A-F-G-K-M.",
        ["الفئة B قريبة من بداية السلسلة الساخنة فتكون زرقاء بيضاء (~20,000 K).",
         "تليها الفئة G الصفراء كالشمس، ثم الفئة M الأبرد والأكثر احمراراً في نهاية السلسلة."],
        "تسلسل الأحرف يمثل التبريد التدريجي من اليسار لليمين.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 6), LEVEL, T_EARTH, _diff(6), "G9-SCI-B24",
        f"Star A and Star B have the exact same surface temperature ({m('T_A = T_B')}), yet Star A radiates {m('100')} times the total luminosity of Star B (recall {m('L \\propto R^2 T^4')}). How many times larger is Star A's radius than Star B's radius?",
        f"يمتلك النجمان أ وب درجة حرارة السطح نفسها تماماً ({m('T_A = T_B')})، ولكن لمعان النجم أ يفوق لمعان النجم ب بمقدار {m('100')} مرة (حيث {m('L \\propto R^2 T^4')}). كم مرة يزيد نصف قطر النجم أ عن نصف قطر النجم ب؟",
        10, [100, 50, 20],
        "With T fixed, luminosity scales with surface area (R²): if R² increases by 100×, take √100.",
        "عند تساوي درجة الحرارة يتناسب اللمعان مع مربع نصف القطر (R²): خذ الجذر التربيعي لـ 100.",
        f"Set {m('\\frac{L_A}{L_B} = \\left(\\frac{R_A}{R_B}\\right)^2 = 100')}.",
        [f"Because {m('T_A = T_B')}, temperature factors cancel out.",
         f"Take square root: {m('\\frac{R_A}{R_B} = \\sqrt{100} = 10')}."],
        "Check: a star 10× wider has 100× the surface area and emits 100× as much light at the same temperature.",
        f"بما أن الحرارة متساوية تصبح النسبة {m('\\frac{L_A}{L_B} = \\left(\\frac{R_A}{R_B}\\right)^2 = 100')}.",
        [f"بأخذ الجذر التربيعي للطرفين: {m('\\frac{R_A}{R_B} = \\sqrt{100} = 10')} مرات."],
        "التحقق: مساحة السطح تتناسب مع R²، ومضاعفة نصف القطر 10 مرات تعطي مساحة أكبر 100 مرة.",
    ))

    d_7 = _svg_hr_diagram("O Star", "نجم O", 0.14, 0.86, "en")
    ar_7 = _svg_hr_diagram("O Star", "نجم O", 0.14, 0.86, "ar")
    qs.append(make_science_concept_q(
        _qid(start_idx + 7), LEVEL, T_EARTH, _diff(7), "G9-SCI-B24",
        "A massive blue O-type star has ~40 times the Sun's hydrogen fuel mass, yet it burns out in under 10 million years while our Sun lasts ~10 billion years and tiny red M-dwarfs last trillions of years. Why do massive stars live far shorter lives?",
        "يمتلك نجم أزرق ضخم من الفئة O كتلة هيدروجين تفوق الشمس بنحو 40 مرة، ومع ذلك ينفد وقوده في أقل من 10 ملايين سنة بينما تعيش الشمس ~10 مليارات سنة والأقزام الحمر تريليونات السنين. لماذا تعيش النجوم الضخمة أعماراً أقصر بكثير؟",
        [
            ("Extreme core pressure and temperature drive fusion luminosity thousands of times faster than fuel mass grows", "الضغط والحرارة الهائلان في نواتها يرفعان معدل الاندماج واللمعان بآلاف الأضعاف متجاوزين الزيادة في كمية الوقود"),
            ("Massive blue stars lose all hydrogen into space before fusion ever starts", "تفقد النجوم الزرقاء كل هيدروجينها إلى الفضاء قبل أن يبدأ الاندماج"),
            ("Red M-dwarfs fuse iron instead of hydrogen, lasting longer", "تدمج الأقزام الحمر الحديد بدلاً من الهيدروجين فتدوم أطول"),
            ("O-type stars have lower core temperatures so reactions freeze quickly", "النجوم الضخمة أبرَد نواةً فتتجمد تفاعلاتها سريعاً"),
        ],
        "Lifetime = Fuel Mass / Burn Rate (M / L). While mass M goes up 40×, luminosity L shoots up >100,000×!",
        "العمر النجمي = كمية الوقود ÷ معدل الاستهلاك (M/L)؛ ورغم زيادة الوقود عشرات المرات فإن معدل الاستهلاك يقفز مئات آلاف المرات.",
        "Compare fuel supply M against luminosity burn rate L.",
        ["Enormous self-gravity compresses the core of a 40-solar-mass star to extreme densities and temperatures.",
         "As a result, core fusion consumes fuel over 100,000 times faster than in the Sun, exhausting hydrogen in a few million years."],
        "In stellar astrophysics: high mass = bright, hot, and short-lived; low mass = dim, cool, and long-lived.",
        "نقارن مخزون الكتلة بمعدل استهلاكه (اللمعان).",
        ["تضغط الجاذبية الهائلة النواة فترتفع الحرارة ومعدل الاندماج النووي بشكل أُسي هائل.",
         "تستهلك النجوم الضخمة وقودها بمعدل يفوق الشمس بمئات آلاف المرات فينفد في بضعة ملايين من السنين."],
        "القاعدة الفلكية: كلما كبرت كتلة النجم زاد سطوعه وقَصُر عمره.",
        diagram_en=d_7, diagram_ar=ar_7,
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 8), LEVEL, T_EARTH, _diff(8), "G9-SCI-B24",
        f"Star A and Star B have identical intrinsic luminosity ({m('L_A = L_B')}), yet Star A is located {m('3')} times farther from Earth than Star B. Using the inverse-square brightness law ({m('b \\propto \\frac{L}{d^2}')}), how many times dimmer does Star A appear in Earth's sky compared to Star B?",
        f"يمتلك النجمان أ وب اللمعان الحقيقي نفسه ({m('L_A = L_B')})، لكن النجم أ يبعد عن الأرض مسافة تساوي {m('3')} أضعاف بعد النجم ب. وفق قانون التربيع العكسي للسطوع ({m('b \\propto \\frac{L}{d^2}')})، كم مرة يبدو النجم أ أخفت في سماء الأرض مقارنة بالنجم ب؟",
        9, [3, 6, 27],
        "Apparent brightness spreads across a sphere of surface area 4πd²; tripling d divides brightness by 3² = 9.",
        "ينتشر الضوء على مساحة كرة تتناسب مع مربع البعد d²؛ فزيادة البعد 3 مرات تقلل السطوع 3² = 9 مرات.",
        f"Evaluate {m('\\frac{b_B}{b_A} = \\left(\\frac{d_A}{d_B}\\right)^2')}.",
        [f"Substitute distance ratio {m('\\frac{d_A}{d_B} = 3')}.",
         f"Brightness ratio = {m('3^2 = 9')}, so Star A appears 9 times dimmer."],
        "Check: twice as far -> 4× dimmer; three times as far -> 9× dimmer.",
        f"نطبق قانون التربيع العكسي للسطوع {m('3^2 = 9')}.",
        [f"بما أن النسبة بين المسافتين {m('3')} واللمعان متساوٍ، فإن شدة السطوع الظاهري تقل بمقدار {m('3^2 = 9')} مرات."],
        "التحقق: مضاعفة المسافة 3 مرات تجعل السطوع الظاهري 1/9 من الأصل.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 9), LEVEL, T_EARTH, _diff(9), "G9-SCI-B24",
        "Which final fate awaits a massive star born with more than 8 solar masses after it finishes evolving into a Red Supergiant?",
        "ما المصير النهائي لنجم فائق الكتلة وُلد بكتلة تزيد عن 8 كتل شمسية بعد بلوغه مرحلة العملاق الأحمر العظيم؟",
        [
            ("A catastrophic core-collapse Supernova leaving behind a Neutron Star or Black Hole", "انفجار مستعر أعظم (Supernova) عنيف يُخلّف نجماً نيوترونياً أو ثقباً أسود"),
            ("A quiet planetary nebula leaving behind a cool Brown Dwarf", "سديم كوكبي هادئ يترك خلفه قزماً بنياً بارداً"),
            ("Gradual cooling directly into a solid rocky planet", "تبرّد تدريجي مباشر ليصبح كوكباً صخرياً صلباً"),
            ("Reversal back into a young G-type Main Sequence star", "عودة عكسية ليصبح نجماً شاباً من التسلسل الرئيسي كالشمس"),
        ],
        "Stars >8 M_Sun have enough gravity to collapse their iron cores violently, triggering a supernova.",
        "النجوم الأثقل من 8 كتل شمسية تنهار نواتها بجاذبية هائلة فتنفجر كمستعر أعظم وتترك جسماً فائق الكثافة.",
        "Distinguish high-mass stellar death (>8 M_Sun) from solar-mass death.",
        ["High-mass stars fuse elements sequentially up to iron, then undergo sudden gravitational core collapse.",
         "The rebound shockwave blasts outer layers into space (Supernova), crushing the core into a Neutron Star (~8–20 M_Sun) or Black Hole (>20 M_Sun)."],
        "Remember: Sun-like stars form White Dwarfs; massive stars form Supernovae -> Neutron Stars or Black Holes.",
        "نفرق بين مصير النجوم متوسطة الكتلة وفائقة الكتلة.",
        ["النجوم التي تفوق 8 كتل شمسية تنهار نواتها فجأة وتنفجر كمستعر أعظم مدمّر.",
         "ينضغط ما تبقى من النواة ليتحول إما إلى نجم نيوتروني أو إلى ثقب أسود تبعاً للكتلة المتبقية."],
        "هذا عكس مصير الشمس التي تنتهي كقزم أبيض دون انفجار.",
        diagram_en=_svg_hr_diagram("Massive Star", "نجم عظيم", 0.85, 0.52, "en"),
        diagram_ar=_svg_hr_diagram("Massive Star", "نجم عظيم", 0.85, 0.52, "ar"),
    ))

    # --- HARD (10..14) ---
    qs.append(make_science_math_q(
        _qid(start_idx + 10), LEVEL, T_EARTH, _diff(10), "G9-SCI-B24",
        f"By the Stefan–Boltzmann law ({m('L \\propto R^2 T^4')}), suppose Star P has the exact same radius as our Sun ({m('R_P = R_{\\odot}')}) but TWICE the Sun's absolute surface temperature ({m('T_P = 2\\,T_{\\odot}')}). How many times more luminous than the Sun is Star P?",
        f"وفق قانون ستيفان–بولتزمان ({m('L \\propto R^2 T^4')})، لنفترض أن النجم P يمتلك نصف القطر نفسه للشمس ({m('R_P = R_{\\odot}')}) لكن درجة حرارته المطلقة تساوي ضعف حرارة الشمس ({m('T_P = 2\\,T_{\\odot}')}). كم مرة يفوق لمعان النجم P لمعان الشمس؟",
        16, [2, 4, 8],
        "Temperature enters to the fourth power (T⁴): compute 2⁴ while R factor is 1² = 1.",
        "تدخل درجة الحرارة المطلقة مرفوعة للأس الرابع (T⁴): احسب 2⁴ بينما معامل نصف القطر 1² = 1.",
        f"Evaluate {m('\\frac{L_P}{L_{\\odot}} = \\left(\\frac{R_P}{R_{\\odot}}\\right)^2 \\left(\\frac{T_P}{T_{\\odot}}\\right)^4')}.",
        [f"Substitute {m('R_P / R_{\\odot} = 1')} and {m('T_P / T_{\\odot} = 2')}.",
         f"Luminosity ratio = {m('1^2 \\times 2^4 = 1 \\times 16 = 16')}."],
        "Check: temperature has a dramatic 4th-power impact on stellar radiation.",
        f"نطبق النسبة {m('1^2 \\times 2^4')}.",
        [f"مع ثبات نصف القطر يكون معامل المساحة {m('1')}.",
         f"معامل الحرارة = {m('2^4 = 16')} مرة."],
        "التحقق: مضاعفة الحرارة المطلقة تضاعف الطاقة المشعة 16 مرة.",
    ))

    qs.append(make_science_math_q(
        _qid(start_idx + 11), LEVEL, T_EARTH, _diff(11), "G9-SCI-B24",
        f"Using a scaled stellar lifetime formula {m('t_{\\text{life}} = 10 \\times \\left(\\frac{M}{L}\\right)')} billion years (where {m('M')} and {m('L')} are measured in solar masses and solar luminosities), estimate the main-sequence lifetime in billions of years of an A-type star with {m('M = 2\\,M_{\\odot}')} and {m('L = 16\\,L_{\\odot}')}.",
        f"باستخدام صيغة تقديرية لعمر النجم في التسلسل الرئيسي {m('t_{\\text{life}} = 10 \\times \\left(\\frac{M}{L}\\right)')} مليار سنة (حيث {m('M')} و{m('L')} مقيسة بوحدات الكتلة واللمعان الشمسي)، احسب عمر نجم من الفئة A كتلته {m('2\\,M_{\\odot}')} ولمعانه {m('16\\,L_{\\odot}')} بوحدة مليار سنة.",
        1.25, [80, 5, 2.5],
        "Plug M = 2 and L = 16 into 10 × (2 / 16) = 10 / 8.",
        "عوض M = 2 و L = 16 في العلاقة 10 × (2 / 16) = 10 / 8.",
        f"Evaluate {m('t_{\\text{life}} = 10 \\times \\frac{2}{16}')}.",
        [f"Compute ratio {m('\\frac{M}{L} = \\frac{2}{16} = \\frac{1}{8} = 0.125')}.",
         f"Lifetime = {m('10 \\times 0.125 = 1.25\\text{ billion years}')}."],
        f"Check: for the Sun ({m('M=1, L=1')}), formula yields {m('10\\text{ billion years}')}; Sirius A (~2 M_Sun) lives ~1 billion years.",
        f"نطبق {m('t_{\\text{life}} = 10 \\times \\frac{2}{16}')}.",
        [f"النسبة = {m('\\frac{2}{16} = 0.125')}.",
         f"العمر المقدر = {m('10 \\times 0.125 = 1.25\\text{ مليار سنة}')}."],
        "التحقق: للشمس يعطي القانون 10 مليارات سنة، والنجم بكتلة شمسين يعيش ثُمن ذلك تقريباً.",
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 12), LEVEL, T_EARTH, _diff(12), "G9-SCI-B24",
        "Inside a massive supergiant star, nuclear fusion progresses through carbon, neon, oxygen, and silicon until an iron core builds up — and then the core suddenly collapses in less than a second. Why does iron trigger catastrophic collapse?",
        "داخل نجم عملاق عظيم، يتدرج الاندماج النووي عبر الكربون والنيون والأكسجين والسيليكون حتى تتراكم نواة من الحديد — وعندئذ تنهار النواة فجأة في أقل من ثانية. لماذا يسبب الحديد هذا الانهيار الكارثي؟",
        [
            ("Fusing iron absorbs energy instead of releasing energy, cutting off the outward thermal pressure supporting the star against gravity", "اندماج الحديد يستهلك طاقة بدلاً من إطلاقها، فينقطع فجأة الضغط الحراري الداعم ضد الجاذبية"),
            ("Iron turns into liquid water that cools the core to zero degrees", "يتحول الحديد إلى ماء سائل يبرد النواة إلى الصفر"),
            ("Iron becomes strongly magnetic and pulls neighboring galaxies into the star", "يصبح الحديد مغناطيسياً قوياً يجذب المجرات المجاورة نحو النجم"),
            ("Iron evaporates silently out through the star's surface without resistance", "يتبخر الحديد بصمت عبر سطح النجم دون مقاومة"),
        ],
        "Iron-56 sits at the peak of nuclear binding stability: fusing lighter nuclei releases energy, whereas fusing iron costs energy.",
        "الحديد يقع في قمة الاستقرار النووي: اندماج ما قبله يحرر طاقة تدعم النجم، أما اندماج الحديد فيمتص طاقة.",
        "Connect nuclear binding energy limit at iron to loss of hydrostatic pressure.",
        ["Every fusion shell up to silicon produces exothermic energy that sustains core thermal pressure.",
         "Iron fusion is endothermic (absorbs energy), instantaneously starving outward pressure so gravity crushes the core inward."],
        "That core bounce drives a Type II Supernova explosion.",
        "نربط حدود الطاقة النووية عند الحديد بفقدان الاتزان الهيدروستاتيكي.",
        ["تنتج التفاعلات من الهيدروجين حتى السيليكون طاقة تحفظ توازن النجم ضد الجاذبية.",
         "اندماج الحديد ماصٌّ للطاقة لا مُنتج لها، فينهار الضغط الداعم وتنكبس النواة بجاذبيتها في أجزاء من الثانية."],
        "ارتداد الطبقات المنهارة يطلق انفجار المستعر الأعظم.",
    ))

    d_13 = _svg_hr_diagram("Red Giant", "عملاق أحمر", 0.85, 0.52, "en")
    ar_13 = _svg_hr_diagram("Red Giant", "عملاق أحمر", 0.85, 0.52, "ar")
    qs.append(make_science_math_q(
        _qid(start_idx + 13), LEVEL, T_EARTH, _diff(13), "G9-SCI-B24",
        f"In the future, our Sun will leave the Main Sequence and swell into a Red Giant whose surface temperature drops by half ({m('T = 0.5\\,T_{\\odot}')}) while its radius expands {m('40')} times ({m('R = 40\\,R_{\\odot}')}). Using {m('L \\propto R^2 T^4')}, how many times more luminous than today's Sun will the Red Giant Sun be?",
        f"مستقبلاً ستغادر شمسنا التسلسل الرئيسي وتتضخم لتصبح عملاقاً أحمر تنخفض حرارة سطحه إلى النصف ({m('T = 0.5\\,T_{\\odot}')}) بينما يتمدد نصف قطره {m('40')} مرة ({m('R = 40\\,R_{\\odot}')}). باستخدام {m('L \\propto R^2 T^4')}، كم مرة سيفوق لمعان العملاق الأحمر لمعان الشمس الحالي؟",
        100, [20, 400, 1600],
        "Compute R factor squared (40² = 1,600) multiplied by T factor to the 4th power ((0.5)⁴ = 1/16).",
        "احسب مربع عامل نصف القطر (40² = 1,600) واضربه في الأس الرابع لعامل الحرارة ((0.5)⁴ = 1/16).",
        f"Evaluate {m('\\frac{L_{\\text{RG}}}{L_{\\odot}} = 40^2 \\times (0.5)^4')}.",
        [f"Surface area multiplier: {m('40^2 = 1,600')}.",
         f"Temperature flux multiplier: {m('(0.5)^4 = \\frac{1}{16}')}.",
         f"Net luminosity ratio = {m('\\frac{1,600}{16} = 100')}."],
        "Check: even though each square meter cools and dims by 16×, the 1,600× larger surface outshines today's Sun by 100×!",
        f"نطبق {m('\\frac{L_{\\text{RG}}}{L_{\\odot}} = 40^2 \\times (0.5)^4')}.",
        [f"تتضاعف المساحة بمقدار {m('40^2 = 1,600')} مرة.",
         f"تقل شدة الإشعاع لكل وحدة مساحة إلى {m('(0.5)^4 = \\frac{1}{16}')}.",
         f"اللمعان الكلي = {m('\\frac{1,600}{16} = 100')} ضعفاً للشمس."],
        "التحقق: رغم برودة السطح يرتفع اللمعان الإجمالي مئة مرة بفضل ضخامة المساحة.",
        diagram_en=d_13, diagram_ar=ar_13,
    ))

    qs.append(make_science_concept_q(
        _qid(start_idx + 14), LEVEL, T_EARTH, _diff(14), "G9-SCI-B24",
        "Astrophysicists often summarize cosmic chemistry by dividing the periodic table by origin. Which pairing accurately identifies where hydrogen/helium, carbon–iron, and elements heavier than iron (such as gold and uranium) primarily originated?",
        "يلخص علماء الفيزياء الفلكية أصل العناصر الكيميائية في الكون حسب آلية تشكلها. أي اختيار يحدد بدقة أصل كل من: (الهيدروجين والهيليوم)، (الكربون حتى الحديد)، و(العناصر الأثقل من الحديد كالذهب واليورانيوم)؟",
        [
            ("H and He: Big Bang nucleosynthesis; C through Fe: fusion inside stars; heavier than Fe: supernovae and neutron-star mergers", "H و He: الانفجار العظيم؛ C إلى Fe: الاندماج داخل النجوم؛ الأثقل من Fe: انفجارات المستعرات العظمى واندماج النجوم النيوترونية"),
            ("All elements including gold and uranium formed during the first 3 minutes of the Big Bang", "تشكلت جميع العناصر بما فيها الذهب واليورانيوم خلال الدقائق الثلاث الأولى للانفجار العظيم"),
            ("Gold and uranium form inside Earth's crust by tectonic plate friction", "يتكون الذهب واليورانيوم في قشرة الأرض بفعل احتكاك الصفائح التكتونية"),
            ("Hydrogen and helium are manufactured exclusively inside White Dwarfs", "يتكون الهيدروجين والهيليوم حصرياً داخل الأقزام البيضاء"),
        ],
        "Standard stellar fusion stops at iron; forging gold/uranium requires extreme neutron-capture blasts.",
        "يتوقف الاندماج النجمي العادي عند الحديد؛ أما الذهب واليورانيوم فيتطلبان انفجارات كونية فائقة الطاقة وغنية بالنيوترونات.",
        "Assign Big Bang, stellar fusion, and explosive nucleosynthesis to their element ranges.",
        ["Big Bang nucleosynthesis produced ~75% hydrogen, ~25% helium, and traces of lithium.",
         "Stellar cores fuse elements up to iron (Z=26); violent supernovae and kilonova neutron-star mergers forge heavier elements like gold (Z=79) and uranium (Z=92)."],
        "That is why Earth's gold and our body's carbon and iron trace back to ancient stars.",
        "نربط كل نطاق من الجدول الدوري بمصنعه الكوني.",
        ["أنتج الانفجار العظيم الهيدروجين والهيليوم البدائيين.",
         "تصنع النجوم العناصر حتى الحديد في نواتها، بينما تنشأ العناصر الأثقل من الحديد في المستعرات العظمى وتصادمات النجوم النيوترونية."],
        "الذهب والحديد والكربون على الأرض هي إرث نجوم قديمة انفجرت قبل نشأة النظام الشمسي.",
    ))

    return qs


# ==============================================================================
# Public Bank Assembly & Verification
# ==============================================================================

def build_g9_science_bank() -> list[dict]:
    """Assemble all 360 verified Grade 9 Nafes Science MCQs (B01..B24 x 15)."""
    generators = [
        _gen_sci_b01, _gen_sci_b02, _gen_sci_b03, _gen_sci_b04, _gen_sci_b05, _gen_sci_b06,
        _gen_sci_b07, _gen_sci_b08, _gen_sci_b09, _gen_sci_b10, _gen_sci_b11, _gen_sci_b12,
        _gen_sci_b13, _gen_sci_b14, _gen_sci_b15, _gen_sci_b16, _gen_sci_b17, _gen_sci_b18,
        _gen_sci_b19, _gen_sci_b20, _gen_sci_b21, _gen_sci_b22, _gen_sci_b23, _gen_sci_b24,
    ]
    all_qs: list[dict] = []
    for k, gen in enumerate(generators):
        all_qs.extend(gen(1 + k * 15))
    return all_qs
