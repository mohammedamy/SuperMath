"""ETEC Nafes National Assessment — Science Grade 6 (العلوم · الصف السادس الابتدائي) Bank: 360 Verified 4-Option MCQs."""
import re
import xml.etree.ElementTree as ET

from kmc_common import m, norm_text
from kmc_diagrams import (
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
    _esc as esc,
    wrap_svg,
)
from nafes_ext_common import (
    make_science_concept_q,
    make_science_math_q,
    svg_cell_diagram,
    svg_earth_layers,
    svg_food_chain,
    svg_force_block,
    svg_motion_graph,
    svg_moon_phases,
    svg_ohm_circuit,
    svg_ph_scale,
    svg_states_of_matter,
)

LEVEL = "Science · Grade 6"
SLATE_BG = "#f8fafc"
LINE_GRID = "#e2e8f0"
PURPLE = "#7c3aed"
TEAL = "#0f766e"

_TEXT_NODE_RE = re.compile(r"(<text\b[^>]*>)([^<]+)(</text>)")


def _svg(w: int, h: int, body: str, title: str) -> str:
    return wrap_svg(body, w=w, h=h, disp_w=min(420, max(280, w)), title=esc(title))


def _ar_svg(svg_str: str, mapping: dict[str, str], regex_rules: list[tuple[str, str]] = None) -> str:
    """Translate <text> bodies inside an XML-validated SVG to Arabic cleanly."""

    def _repl(match: re.Match) -> str:
        open_t, body, close_t = match.group(1), match.group(2), match.group(3)
        raw = body.strip()
        if raw in mapping:
            return f"{open_t}{esc(mapping[raw])}{close_t}"
        if regex_rules:
            for pat, sub in regex_rules:
                if re.fullmatch(pat, raw):
                    return f"{open_t}{esc(re.sub(pat, sub, raw))}{close_t}"
        return match.group(0)

    out = _TEXT_NODE_RE.sub(_repl, svg_str)
    ET.fromstring(out)
    return out


def _cell_svgs(cell_type: str, highlight: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_cell_diagram(cell_type, highlight, title_en)
    ar_raw = svg_cell_diagram(cell_type, highlight, title_ar)
    ar = _ar_svg(
        ar_raw,
        {
            "Cell Wall": "جدار الخلية",
            "Nucleus": "النواة",
            "Vacuole": "فجوة عصارية",
            "Chloroplast": "بلاستيدة خضراء",
            "Membrane": "غشاء خلوي",
            "Mitochondria": "ميتوكوندريا",
            "Cytoplasm": "سيتوبلازم",
        },
    )
    return en, ar


def _food_chain_svgs(steps_en: list[str], steps_ar: list[str], title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_food_chain(steps_en, title_en)
    ar_raw = svg_food_chain(steps_ar, title_ar)
    ar = _ar_svg(ar_raw, {"Producer → Consumers": "منتِج → مستهلكات"})
    return en, ar


def _states_svgs(highlight: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_states_of_matter(highlight, title_en)
    ar_raw = svg_states_of_matter(highlight, title_ar)
    ar = _ar_svg(ar_raw, {"Solid": "صلب", "Liquid": "سائل", "Gas": "غاز"})
    return en, ar


def _ph_svgs(marker_ph: float, lbl_en: str, lbl_ar: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_ph_scale(marker_ph, lbl_en, title_en)
    ar_raw = svg_ph_scale(marker_ph, lbl_en, title_ar)
    ar = _ar_svg(
        ar_raw,
        {
            "Acidic": "حمضي",
            "Neutral (7)": "متعادل (7)",
            "Basic": "قاعدي",
            f"{lbl_en} (pH {marker_ph:g})": f"{lbl_ar} (pH {marker_ph:g})",
        },
    )
    return en, ar


def _force_svgs(left_f: int, right_f: int, mass_kg: int | None, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_force_block(left_f, right_f, mass_kg, title_en)
    ar_raw = svg_force_block(left_f, right_f, mass_kg, title_ar)
    ar = _ar_svg(
        ar_raw,
        {"Object": "الجسم"},
        [(r"(\d+)\s*kg", r"\1 كجم"), (r"(\d+)\s*N", r"\1 نيوتن")],
    )
    return en, ar


def _ohm_svgs(voltage_v: int, r_vals: list[int], mode: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_ohm_circuit(voltage_v, r_vals, mode, title_en)
    ar = svg_ohm_circuit(voltage_v, r_vals, mode, title_ar)
    return en, ar


def _earth_svgs(highlight: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_earth_layers(highlight, title_en)
    ar_raw = svg_earth_layers(highlight, title_ar)
    ar = _ar_svg(
        ar_raw,
        {
            "Crust": "القشرة",
            "Mantle": "الوشاح",
            "Outer Core": "اللب الخارجي",
            "Inner Core": "اللب الداخلي",
        },
    )
    return en, ar


def _moon_svgs(phase_en: str, phase_ar: str, title_en: str, title_ar: str) -> tuple[str, str]:
    en = svg_moon_phases(phase_en, title_en)
    ar_raw = svg_moon_phases(phase_en, title_ar)
    ar = _ar_svg(ar_raw, {"Sun": "الشمس", "Earth": "الأرض", phase_en: phase_ar})
    return en, ar


# ---- Custom Clean Grade-6 Science SVG Helpers (font-size >= 11.5, title = 14) ----

def svg_data_table(headers: list[str], rows: list[list[str]], title: str, col_widths: list[int] = None) -> str:
    n_cols = len(headers)
    if col_widths is None:
        col_widths = [int(348 / n_cols)] * n_cols
    w = max(360, sum(col_widths) + 28)
    row_h = 28
    top_y = 44
    h = top_y + 30 + len(rows) * row_h + 18
    x0 = (w - sum(col_widths)) / 2.0
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="{x0:.1f}" y="{top_y}" width="{sum(col_widths)}" height="{30 + len(rows)*row_h}" rx="6" fill="#ffffff" stroke="{STROKE}" stroke-width="1.5"/>',
        f'<rect x="{x0:.1f}" y="{top_y}" width="{sum(col_widths)}" height="30" rx="6" fill="#dbeafe"/>',
        f'<line x1="{x0:.1f}" y1="{top_y+30}" x2="{x0+sum(col_widths):.1f}" y2="{top_y+30}" stroke="{STROKE}" stroke-width="1.3"/>',
    ]
    cx = x0
    for idx, (hd, cw) in enumerate(zip(headers, col_widths)):
        parts.append(f'<text x="{cx + cw/2:.1f}" y="{top_y + 20}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(hd)}</text>')
        if idx < n_cols - 1:
            parts.append(f'<line x1="{cx+cw:.1f}" y1="{top_y}" x2="{cx+cw:.1f}" y2="{top_y + 30 + len(rows)*row_h}" stroke="#cbd5e1" stroke-width="1.1"/>')
        cx += cw
    for r_idx, row in enumerate(rows):
        ry = top_y + 30 + r_idx * row_h
        if r_idx > 0:
            parts.append(f'<line x1="{x0:.1f}" y1="{ry}" x2="{x0+sum(col_widths):.1f}" y2="{ry}" stroke="{LINE_GRID}" stroke-width="1"/>')
        cx = x0
        for c_idx, (val, cw) in enumerate(zip(row, col_widths)):
            fw = "700" if c_idx == 0 else "600"
            col = BLUE if c_idx == 0 else STROKE
            parts.append(f'<text x="{cx + cw/2:.1f}" y="{ry + 19}" text-anchor="middle" font-size="11.5" font-weight="{fw}" fill="{col}">{esc(val)}</text>')
            cx += cw
    return _svg(w, h, "".join(parts), title)


def svg_bar_chart(bars: list[tuple[str, float, str]], y_label: str, title: str) -> str:
    w, h = 376, 198
    ox, oy, gw, gh = 58, 154, 292, 90
    max_v = max(v for _, v, _ in bars) or 1
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="26" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<text x="20" y="43" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(y_label)}</text>',
    ]
    for i in range(5):
        gy = oy - i * gh / 4
        parts.append(f'<line x1="{ox}" y1="{gy:.1f}" x2="{ox+gw}" y2="{gy:.1f}" stroke="{LINE_GRID}" stroke-width="1"/>')
        parts.append(f'<text x="{ox-8}" y="{gy+4:.1f}" text-anchor="end" font-size="11.5" font-weight="600" fill="{MUTED}">{max_v*i/4:g}</text>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+gw}" y2="{oy}" stroke="{STROKE}" stroke-width="1.8"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-gh}" stroke="{STROKE}" stroke-width="1.8"/>')
    n = len(bars)
    bw = min(48, (gw - 24) / max(1, n) * 0.65)
    step = gw / max(1, n)
    for i, (lbl, val, col) in enumerate(bars):
        bx = ox + i * step + (step - bw) / 2
        bh = (val / max_v) * gh
        by = oy - bh
        parts.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{col}" fill-opacity="0.22" stroke="{col}" stroke-width="1.8"/>')
        parts.append(f'<text x="{bx+bw/2:.1f}" y="{by-5:.1f}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{STROKE}">{val:g}</text>')
        parts.append(f'<text x="{bx+bw/2:.1f}" y="{oy+17}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    return _svg(w, h, "".join(parts), title)


def svg_graduated_cylinder(v1: int, v2: int, mass_g: int, cap: int, lbl_before: str, lbl_after: str, mass_lbl: str, title: str) -> str:
    w, h = 376, 195
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    for cx, v, lbl, rock in ((76, v1, lbl_before, False), (186, v2, lbl_after, True)):
        top_y, bot_y, cw = 52, 146, 44
        wh = (v / cap) * (bot_y - top_y)
        wy = bot_y - wh
        parts.append(f'<rect x="{cx}" y="{top_y}" width="{cw}" height="{bot_y-top_y}" rx="4" fill="#ffffff" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(f'<rect x="{cx+2}" y="{wy:.1f}" width="{cw-4}" height="{wh-1:.1f}" fill="{WATER}" stroke="{BLUE}" stroke-width="1.2"/>')
        if rock:
            parts.append(f'<polygon points="{cx+12},{bot_y-4} {cx+32},{bot_y-4} {cx+28},{bot_y-22} {cx+14},{bot_y-20}" fill="#94a3b8" stroke="{STROKE}" stroke-width="1.3"/>')
        for k in range(1, 5):
            ty = bot_y - k * (bot_y - top_y) / 4
            parts.append(f'<line x1="{cx}" y1="{ty:.1f}" x2="{cx+10}" y2="{ty:.1f}" stroke="{MUTED}" stroke-width="1"/>')
        parts.append(f'<text x="{cx+cw/2:.1f}" y="{wy-6:.1f}" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{v} mL</text>')
        parts.append(f'<text x="{cx+cw/2:.1f}" y="168" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(lbl)}</text>')
    # Arrow between cylinders
    parts.append(f'<line x1="132" y1="100" x2="170" y2="100" stroke="{STROKE}" stroke-width="2"/>')
    parts.append(f'<polygon points="170,95 178,100 170,105" fill="{STROKE}"/>')
    # Mass info box
    parts.append(f'<rect x="252" y="64" width="106" height="68" rx="9" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.7"/>')
    parts.append(f'<text x="305" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(mass_lbl)}</text>')
    parts.append(f'<text x="305" y="116" text-anchor="middle" font-size="13" font-weight="800" fill="{ORANGE}">{mass_g} g</text>')
    return _svg(w, h, "".join(parts), title)


def svg_process_flow(steps: list[str], footer: str, title: str) -> str:
    n = len(steps)
    max_chars = max((len(s) for s in steps), default=10)
    bw = max(88 if n == 4 else 102, int(max_chars * 7.0) + 12)
    gap = 16
    w = max(416 if n == 4 else 384, int(36 + n * bw + max(1, n - 1) * gap))
    h = 148
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="29" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
    ]
    fills = ["#dcfce7", "#dbeafe", "#fef3c7", "#f3e8ff"]
    edges = [GREEN, BLUE, ORANGE, PURPLE]
    x_start = (w - (n * bw + max(0, n - 1) * gap)) / 2.0
    for i, s in enumerate(steps):
        x = x_start + i * (bw + gap)
        parts.append(f'<rect x="{x:.1f}" y="52" width="{bw}" height="48" rx="8" fill="{fills[i%4]}" stroke="{edges[i%4]}" stroke-width="1.7"/>')
        parts.append(f'<text x="{x+bw/2:.1f}" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(s)}</text>')
        if i < n - 1:
            ax1, ax2 = x + bw + 2, x + bw + gap - 5
            parts.append(f'<line x1="{ax1:.1f}" y1="76" x2="{ax2:.1f}" y2="76" stroke="{STROKE}" stroke-width="1.8"/>')
            parts.append(f'<polygon points="{ax2:.1f},72 {ax2+5:.1f},76 {ax2:.1f},80" fill="{STROKE}"/>')
    parts.append(f'<text x="{w/2:.1f}" y="125" text-anchor="middle" font-size="11.5" font-weight="600" fill="{MUTED}">{esc(footer)}</text>')
    return _svg(w, h, "".join(parts), title)


def svg_lever_diagram(fulcrum_x: int, left_lbl: str, right_lbl: str, d1_lbl: str, d2_lbl: str, title: str) -> str:
    w, h = 368, 165
    fx = fulcrum_x  # e.g. 160 or 200
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="48" y1="88" x2="320" y2="88" stroke="{STROKE}" stroke-width="4" stroke-linecap="round"/>',
        f'<polygon points="{fx},91 {fx-16},122 {fx+16},122" fill="#fed7aa" stroke="{ORANGE}" stroke-width="1.8"/>',
        f'<rect x="44" y="60" width="38" height="26" rx="4" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.6"/>',
        f'<text x="63" y="52" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">{esc(left_lbl)}</text>',
        f'<line x1="305" y1="54" x2="305" y2="82" stroke="{RED}" stroke-width="2.6"/>',
        f'<polygon points="300,78 305,87 310,78" fill="{RED}"/>',
        f'<text x="305" y="48" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(right_lbl)}</text>',
        f'<text x="{(63+fx)/2:.1f}" y="138" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(d1_lbl)}</text>',
        f'<text x="{(fx+305)/2:.1f}" y="138" text-anchor="middle" font-size="12" font-weight="700" fill="{STROKE}">{esc(d2_lbl)}</text>',
    ]
    return _svg(w, h, "".join(parts), title)


def svg_ramp_diagram(len_lbl: str, h_lbl: str, load_lbl: str, title: str) -> str:
    w, h = 380, 168
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<polygon points="48,130 268,130 268,58" fill="#dbeafe" stroke="{STROKE}" stroke-width="2"/>',
        f'<rect x="136" y="76" width="34" height="24" rx="4" transform="rotate(-18 153 88)" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.8"/>',
        f'<text x="142" y="63" text-anchor="middle" font-size="12" font-weight="800" fill="{ORANGE}">{esc(load_lbl)}</text>',
        f'<text x="158" y="147" text-anchor="middle" font-size="12" font-weight="700" fill="{BLUE}">{esc(len_lbl)}</text>',
        f'<text x="318" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="{RED}">{esc(h_lbl)}</text>',
    ]
    return _svg(w, h, "".join(parts), title)


def svg_roller_coaster(h_vals: list[int], title: str) -> str:
    w, h = 368, 180
    # Track through A (top), B (mid valley), C (mid hill), D (low valley)
    pts = [(42, 62), (126, 134), (218, 86), (312, 134)]
    path_d = "M 42,62 Q 84,134 126,134 T 218,86 T 312,134"
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="28" y1="144" x2="340" y2="144" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4 3"/>',
        f'<path d="{path_d}" fill="none" stroke="{BLUE}" stroke-width="3"/>',
    ]
    tags = ["A", "B", "C", "D"]
    for (px, py), tg, hv in zip(pts, tags, h_vals):
        parts.append(f'<circle cx="{px}" cy="{py}" r="5.5" fill="{RED}" stroke="#ffffff" stroke-width="1.4"/>')
        parts.append(f'<text x="{px}" y="{py-11}" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{tg} ({hv}m)</text>')
    return _svg(w, h, "".join(parts), title)


def svg_light_ray(mode: str, angle_deg: int, lbl_n: str, lbl_m: str, title: str) -> str:
    w, h = 360, 175
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<line x1="180" y1="46" x2="180" y2="152" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4 3"/>',
        f'<text x="180" y="42" text-anchor="middle" font-size="11.5" font-weight="700" fill="{MUTED}">{esc(lbl_n)}</text>',
    ]
    if mode == "reflect":
        parts.append(f'<line x1="48" y1="126" x2="312" y2="126" stroke="{STROKE}" stroke-width="3"/>')
        parts.append(f'<line x1="88" y1="58" x2="180" y2="126" stroke="{RED}" stroke-width="2.4"/>')
        parts.append(f'<line x1="180" y1="126" x2="272" y2="58" stroke="{BLUE}" stroke-width="2.4"/>')
        parts.append(f'<text x="142" y="86" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{angle_deg}°</text>')
        parts.append(f'<text x="220" y="86" text-anchor="middle" font-size="12" font-weight="800" fill="{BLUE}">?</text>')
        parts.append(f'<text x="180" y="146" text-anchor="middle" font-size="11.5" font-weight="700" fill="{STROKE}">{esc(lbl_m)}</text>')
    else:
        parts.append(f'<rect x="40" y="96" width="280" height="58" rx="4" fill="{WATER}" fill-opacity="0.55" stroke="{BLUE}" stroke-width="1.2"/>')
        parts.append(f'<line x1="92" y1="52" x2="180" y2="96" stroke="{RED}" stroke-width="2.4"/>')
        parts.append(f'<line x1="180" y1="96" x2="226" y2="148" stroke="{ORANGE}" stroke-width="2.4"/>')
        parts.append(f'<text x="144" y="72" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{angle_deg}°</text>')
        parts.append(f'<text x="292" y="142" text-anchor="middle" font-size="11.5" font-weight="700" fill="{BLUE}">{esc(lbl_m)}</text>')
    return _svg(w, h, "".join(parts), title)


def svg_bulb_circuit(cfg: str, bat_lbl: str, s1_lbl: str, s2_lbl: str, title: str) -> str:
    w, h = 360, 175
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<rect x="64" y="54" width="232" height="90" rx="6" fill="none" stroke="{STROKE}" stroke-width="2.2"/>',
        f'<rect x="42" y="84" width="46" height="28" rx="5" fill="#fef3c7" stroke="{ORANGE}" stroke-width="1.8"/>',
        f'<text x="65" y="102" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(bat_lbl)}</text>',
    ]
    if cfg == "series":
        parts.append(f'<circle cx="145" cy="54" r="14" fill="#fef08a" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="145" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">B1</text>')
        parts.append(f'<circle cx="235" cy="54" r="14" fill="#fef08a" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="235" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">B2</text>')
        parts.append(f'<rect x="154" y="132" width="52" height="22" rx="4" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.5"/>')
        parts.append(f'<text x="180" y="147" text-anchor="middle" font-size="11.5" font-weight="800" fill="{STROKE}">{esc(s1_lbl)}</text>')
    else:
        parts.append(f'<line x1="64" y1="98" x2="296" y2="98" stroke="{STROKE}" stroke-width="2.2"/>')
        parts.append(f'<circle cx="150" cy="54" r="13" fill="#fef08a" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="150" y="58" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">B1</text>')
        parts.append(f'<circle cx="150" cy="98" r="13" fill="#fef08a" stroke="{ORANGE}" stroke-width="1.8"/>')
        parts.append(f'<text x="150" y="102" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">B2</text>')
        parts.append(f'<rect x="210" y="43" width="48" height="22" rx="4" fill="#dbeafe" stroke="{BLUE}" stroke-width="1.5"/>')
        parts.append(f'<text x="234" y="58" text-anchor="middle" font-size="11.5" font-weight="800" fill="{STROKE}">{esc(s1_lbl)}</text>')
        parts.append(f'<rect x="210" y="87" width="48" height="22" rx="4" fill="#dcfce7" stroke="{GREEN}" stroke-width="1.5"/>')
        parts.append(f'<text x="234" y="102" text-anchor="middle" font-size="11.5" font-weight="800" fill="{STROKE}">{esc(s2_lbl)}</text>')
    return _svg(w, h, "".join(parts), title)


def svg_tilt_seasons(sun_lbl: str, n_lbl: str, s_lbl: str, ray_lbl: str, title: str) -> str:
    w, h = 368, 175
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="68" cy="100" r="28" fill="#fde047" stroke="{ORANGE}" stroke-width="2"/>',
        f'<text x="68" y="144" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(sun_lbl)}</text>',
        f'<line x1="108" y1="84" x2="210" y2="84" stroke="{ORANGE}" stroke-width="2"/>',
        f'<polygon points="210,79 220,84 210,89" fill="{ORANGE}"/>',
        f'<line x1="108" y1="114" x2="210" y2="114" stroke="{ORANGE}" stroke-width="2"/>',
        f'<polygon points="210,109 220,114 210,119" fill="{ORANGE}"/>',
        f'<text x="158" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="{ORANGE}">{esc(ray_lbl)}</text>',
        f'<circle cx="264" cy="100" r="30" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>',
        f'<line x1="252" y1="60" x2="276" y2="140" stroke="{RED}" stroke-width="2.2"/>',
        f'<text x="272" y="54" text-anchor="middle" font-size="12" font-weight="800" fill="{RED}">{esc(n_lbl)}</text>',
        f'<text x="284" y="152" text-anchor="middle" font-size="12" font-weight="700" fill="{BLUE}">{esc(s_lbl)}</text>',
    ]
    return _svg(w, h, "".join(parts), title)


def svg_eclipse_diagram(kind: str, sun_lbl: str, mid_lbl: str, right_lbl: str, title: str) -> str:
    w, h = 368, 165
    parts = [
        f'<rect x="8" y="8" width="{w-16}" height="{h-16}" rx="12" fill="{SLATE_BG}" stroke="#cbd5e1" stroke-width="1.3"/>',
        f'<text x="{w/2:.1f}" y="28" text-anchor="middle" font-size="14" font-weight="700" fill="{STROKE}">{esc(title)}</text>',
        f'<circle cx="58" cy="92" r="24" fill="#fde047" stroke="{ORANGE}" stroke-width="2"/>',
        f'<text x="58" y="134" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(sun_lbl)}</text>',
    ]
    if kind == "solar":
        parts.append(f'<polygon points="184,81 288,89 288,95 184,103" fill="#475569" fill-opacity="0.35"/>')
        parts.append(f'<circle cx="184" cy="92" r="11" fill="#334155" stroke="{STROKE}" stroke-width="1.8"/>')
        parts.append(f'<circle cx="294" cy="92" r="20" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>')
    else:
        parts.append(f'<polygon points="184,72 296,81 296,103 184,112" fill="#475569" fill-opacity="0.35"/>')
        parts.append(f'<circle cx="184" cy="92" r="20" fill="{WATER}" stroke="{BLUE}" stroke-width="2"/>')
        parts.append(f'<circle cx="294" cy="92" r="11" fill="#fca5a5" stroke="{RED}" stroke-width="1.8"/>')
    parts.append(f'<text x="184" y="134" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(mid_lbl)}</text>')
    parts.append(f'<text x="294" y="134" text-anchor="middle" font-size="12" font-weight="800" fill="{STROKE}">{esc(right_lbl)}</text>')
    return _svg(w, h, "".join(parts), title)


class G6SciBankBuilder:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add_concept(
        self,
        topic: str,
        difficulty: str,
        blueprint: str,
        q_en: str,
        q_ar: str,
        option_pairs: list[tuple[str, str]],
        hint_en: str,
        hint_ar: str,
        idea_en: str,
        steps_en: list[str],
        check_en: str,
        idea_ar: str,
        steps_ar: list[str],
        check_ar: str,
        diagram_en: str = None,
        diagram_ar: str = None,
    ) -> None:
        qid = f"NAFS-SCI-G6-{len(self.items) + 1:03d}"
        self.items.append(
            make_science_concept_q(
                qid=qid,
                level=LEVEL,
                topic=topic,
                difficulty=difficulty,
                blueprint=blueprint,
                q_en=q_en,
                q_ar=q_ar,
                option_pairs=option_pairs,
                hint_en=hint_en,
                hint_ar=hint_ar,
                idea_en=idea_en,
                steps_en=steps_en,
                check_en=check_en,
                idea_ar=idea_ar,
                steps_ar=steps_ar,
                check_ar=check_ar,
                diagram_en=diagram_en,
                diagram_ar=diagram_ar,
            )
        )

    def add_math(
        self,
        topic: str,
        difficulty: str,
        blueprint: str,
        q_en: str,
        q_ar: str,
        correct_val,
        distractors: list,
        hint_en: str,
        hint_ar: str,
        idea_en: str,
        steps_en: list[str],
        check_en: str,
        idea_ar: str,
        steps_ar: list[str],
        check_ar: str,
        suffix: str = "",
        diagram_en: str = None,
        diagram_ar: str = None,
    ) -> None:
        qid = f"NAFS-SCI-G6-{len(self.items) + 1:03d}"
        item = make_science_math_q(
            qid=qid,
            level=LEVEL,
            topic=topic,
            difficulty=difficulty,
            blueprint=blueprint,
            q_en=q_en,
            q_ar=q_ar,
            correct_val=correct_val,
            distractors=distractors,
            hint_en=hint_en,
            hint_ar=hint_ar,
            idea_en=idea_en,
            steps_en=steps_en,
            check_en=check_en,
            idea_ar=idea_ar,
            steps_ar=steps_ar,
            check_ar=check_ar,
            suffix=suffix,
            diagram_en=diagram_en,
            diagram_ar=diagram_ar,
        )
        assert all("_" not in o for o in item["content"]["en"]["options"]), f"Fallback distractor in {qid}"
        self.items.append(item)


# ==============================================================================
# TOPIC 1: LIFE SCIENCES (G6-SCI-B01 .. G6-SCI-B06, 90 Questions)
# ==============================================================================

def _add_b01(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B01"
    # Easy (0..4): Organelle identification using svg_cell_diagram
    easy_cells = [
        (
            "plant", "Chloroplast", "Plant Leaf Cell", "الخلية النباتية",
            "A Grade 6 student examines a green spinach leaf cell under a microscope. Which highlighted organelle captures sunlight to manufacture glucose during photosynthesis?",
            "تفحص طالبة في الصف السادس خلية من ورقة السبانخ تحت المجهر. ما العضية المظللة باللون الأحمر التي تمتص ضوء الشمس لصنع الجلوكوز في عملية البناء الضوئي؟",
            [
                ("Chloroplast", "البلاستيدة الخضراء"),
                ("Nucleus", "النواة"),
                ("Cell Wall", "جدار الخلية"),
                ("Vacuole", "الفجوة العصارية"),
            ],
            "Look for the green organelle that contains chlorophyll in plant cells.",
            "ابحث عن العضية الخضراء التي تحتوي على الكلوروفيل في الخلية النباتية.",
            "Chloroplasts convert solar energy, CO₂, and water into sugar.",
            ["Identify the green oval organelle labeled Chloroplast in the plant cell diagram.", "Chlorophyll inside chloroplasts traps light energy for photosynthesis."],
            "Only plant and algal cells have chloroplasts to make food.",
            "تقوم البلاستيدة الخضراء بتحويل الطاقة الضوئية وثاني أكسيد الكربون والماء إلى غذاء.",
            ["تُظهر الرسمة البلاستيدة الخضراء المحددة باللون الأحمر.", "تحتوي على صبغة الكلوروفيل اللازمة لعملية البناء الضوئي."],
            "تختص البلاستيدات الخضراء بالخلايا النباتية والطحالب.",
        ),
        (
            "plant", "Cell Wall", "Plant Stem Cell", "خلية ساق نباتية",
            "During a lab check of a celery stem cell, which outer rigid layer shown in the diagram protects the cell and gives the plant its upright rectangular shape?",
            "أثناء فحص خلية من ساق الكرفس، ما الطبقة الخارجية الصلبة الموضحة في الشكل التي تحمي الخلية وتمنح النبات شكله المنتظم القائم؟",
            [
                ("Cell Wall", "جدار الخلية"),
                ("Cell Membrane", "الغشاء الخلوي"),
                ("Cytoplasm", "السيتوبلازم"),
                ("Mitochondria", "الميتوكوندريا"),
            ],
            "This tough cellulose barrier surrounds the outside of plant cells, outside the membrane.",
            "هذه الطبقة المصنوعة من السليلوز تحيط بالخلية النباتية من الخارج بعد الغشاء الخلوي.",
            "The cellulose cell wall provides structural rigidity.",
            ["Compare the outer thick green border with the dashed inner cell membrane.", "The outer border is the cell wall, absent in animal cells."],
            "Animal cells lack a rigid cell wall.",
            "يمنح الجدار الخلوي المصنوع من السليلوز الدعم والصلابة للخلية النباتية.",
            ["نلاحظ في الشكل طبقة خارجية سميكة تحيط بالغشاء الخلوي المتقطع.", "تُسمى هذه الطبقة جدار الخلية وهي غير موجودة في الخلية الحيوانية."],
            "الجدار الخلوي هو المسؤول عن ثبات شكل الخلية النباتية.",
        ),
        (
            "animal", "Nucleus", "Animal Cheek Cell", "الخلية الحيوانية",
            "When viewing a stained cheek cell, a student notices one large dark spherical structure controlling growth and heredity. Which organelle is highlighted?",
            "عند فحص خلية مأخوذة من باطن الخد، لاحظ طالب تركيباً كروياً واضحاً يتحكم في أنشطة الخلية والوراثة. ما هذه العضية المحددة؟",
            [
                ("Nucleus", "النواة"),
                ("Mitochondria", "الميتوكوندريا"),
                ("Cytoplasm", "السيتوبلازم"),
                ("Cell Membrane", "الغشاء الخلوي"),
            ],
            "It stores the cell's DNA and directs cellular activities like a control center.",
            "تخزن المادة الوراثية DNA وتنظم جميع أنشطة الخلية.",
            "The nucleus is the genetic control center of eukaryotic cells.",
            ["Locate the large purple central sphere in the animal cell diagram.", "It houses DNA and regulates protein synthesis and cell division."],
            "Both plant and animal cells contain a nucleus.",
            "النواة هي مركز التحكم في الخلية وتحتوي على المادة الوراثية.",
            ["تقع النواة كجسم كروي بارز في وسط الخلية الحيوانية تقريباً.", "تتحكم في النمو والانقسام والعمليات الحيوية."],
            "توجد النواة في كلٍّ من الخلية النباتية والخلية الحيوانية.",
        ),
        (
            "animal", "Mitochondria", "Animal Muscle Cell", "خلية عضلية حيوانية",
            "Active muscle cells require large amounts of usable energy from glucose and oxygen. Which highlighted organelle carries out cellular respiration to release energy?",
            "تحتاج الخلايا العضلية النشطة إلى كميات كبيرة من الطاقة من الجلوكوز والأكسجين. ما العضية المحددة التي تقوم بالتنفس الخلوي لإنتاج الطاقة؟",
            [
                ("Mitochondria", "الميتوكوندريا"),
                ("Vacuole", "الفجوة العصارية"),
                ("Cell Wall", "جدار الخلية"),
                ("Chloroplast", "البلاستيدة الخضراء"),
            ],
            "Often called the powerhouse of the cell, it breaks down sugar to release energy.",
            "تُعرف بمحطة توليد الطاقة في الخلية لأنها تحرر الطاقة من الغذاء.",
            "Mitochondria release usable energy through cellular respiration.",
            ["Find the oval organelle with folded inner membranes labeled Mitochondria.", "It converts glucose and oxygen into cellular energy (ATP), CO₂, and water."],
            "Muscle cells contain many mitochondria to power movement.",
            "تقوم الميتوكوندريا بالتنفس الخلوي لتحرير الطاقة اللازمة لنشاط الخلية.",
            ["تشير العلامة الحمراء إلى الميتوكوندريا في الخلية الحيوانية.", "تكسر السكر بوجود الأكسجين لإنتاج الطاقة."],
            "تكثر الميتوكوندريا في الخلايا العضلية كثيرة الحركة.",
        ),
        (
            "plant", "Vacuole", "Plant Parenchyma Cell", "خلية نباتية",
            "Which large fluid-filled sac highlighted inside the plant cell stores water, dissolved minerals, and wastes while keeping the stem crisp and firm?",
            "ما الكيس الكبير المملوء بالسائل والمحدد داخل الخلية النباتية، الذي يخزن الماء والأملاح والفضلات ويحافظ على امتلاء الساق ونضارتها؟",
            [
                ("Vacuole", "الفجوة العصارية"),
                ("Nucleus", "النواة"),
                ("Chloroplast", "البلاستيدة الخضراء"),
                ("Cell Wall", "جدار الخلية"),
            ],
            "In mature plant cells, one central sac can occupy more than half of the cell volume.",
            "في الخلية النباتية الناضجة، يشغل هذا الكيس مساحة كبيرة في المركز لتخزين الماء.",
            "Plant cells possess a large central vacuole for water storage and turgor pressure.",
            ["Observe the large light-blue sac inside the plant cell diagram.", "When filled with water, the central vacuole presses against the cell wall to prevent wilting."],
            "Animal cells have only small, scattered vacuoles.",
            "تحتوي الخلية النباتية على فجوة عصارية مركزية كبيرة لتخزين الماء.",
            ["يوضح الرسم فجوة زرقاء كبيرة تشغل معظم حجم الخلية.", "عند امتلائها بالماء تحافظ على انتصاب النبات."],
            "تمتاز الخلية النباتية بفجوتها الكبيرة مقارنة بالخلية الحيوانية.",
        ),
    ]
    for ct, hi, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in easy_cells:
        den, dar = _cell_svgs(ct, hi, ten, tar)
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Comparing plant/animal cells, membrane transport & levels of organization
    med_b01 = [
        (
            "A student peels the translucent white inner skin of an onion bulb (underground storage organ) and views it under a microscope. Why does this plant cell show a cell wall and large vacuole, yet lack chloroplasts?",
            "فحص طالب الغشاء الداخلي الشفاف لبصلة تنمو تحت التربة بالمجهر. لماذا تظهر في هذه الخلية النباتية فجوة كبيرة وجدار خلوي ولكنها تخلو من البلاستيدات الخضراء؟",
            [
                ("Underground bulb cells do not receive sunlight, so they store food instead of performing photosynthesis", "لأن خلايا البصلة تحت التربة لا تتعرض لضوء الشمس فتخزن الغذاء ولا تقوم بالبناء الضوئي"),
                ("Onion bulbs belong to the Fungi kingdom rather than the Plant kingdom", "لأن البصل ينتمي إلى مملكة الفطريات وليس النباتات"),
                ("Plant cells lose their chloroplasts as soon as a cell wall is formed", "لأن الخلايا النباتية تفقد بلاستيداتها بمجرد تكون الجدار الخلوي"),
                ("Chloroplasts exist only in animal cells that consume green vegetables", "لأن البلاستيدات الخضراء توجد فقط في الخلايا الحيوانية"),
            ],
            "Think about whether underground tissues can trap sunlight.",
            "فكر في إمكانية وصول ضوء الشمس إلى الأجزاء التي تنمو تحت سطح التربة.",
            "Organelles present in a cell match the cell's specific job.",
            ["Onion root and bulb cells grow underground in darkness.", "Without light, chloroplasts would be useless; instead, root and bulb cells store starch/sugars made by the green leaves."],
            "Presence of a cell wall confirms it is a plant cell even without chloroplasts.",
            "تتخصص الخلايا حسب وظيفتها ومكان وجودها في الكائن الحي.",
            ["تنمو البصلة في الظلام تحت التربة فلا تصلها أشعة الشمس.", "لذلك لا تحتاج إلى بلاستيدات خضراء بل تخزن الغذاء المصنوع في الأوراق."],
            "وجود الجدار الخلوي يثبت أنها خلية نباتية رغم غياب البلاستيدات.",
            _cell_svgs("plant", "Cell Wall", "Onion Bulb Cell", "خلية بصل تحت التربة"),
        ),
        (
            "Which sequence correctly orders the biological levels of organization in a date palm tree from the simplest living unit to the most complex?",
            "أي تسلسل مما يلي يرتب مستويات التنظيم الحيوي في شجرة النخيل ترتيباً صحيحاً من أبسط وحدة حية إلى الأكثر تعقيداً؟",
            [
                ("Cell → Tissue → Organ → Organ System → Organism", "خلية ← نسيج ← عضو ← جهاز عضوي ← كائن حي"),
                ("Tissue → Cell → Organ → Organism → Organ System", "نسيج ← خلية ← عضو ← كائن حي ← جهاز عضوي"),
                ("Organ → Tissue → Cell → Organ System → Organism", "عضو ← نسيج ← خلية ← جهاز عضوي ← كائن حي"),
                ("Cell → Organ → Tissue → Organ System → Organism", "خلية ← عضو ← نسيج ← جهاز عضوي ← كائن حي"),
            ],
            "Start with the single building block, then group similar ones together.",
            "ابدأ بأصغر وحدة بناء حية، ثم تجمّعها لتكوين المستوى التالي.",
            "Multicellular organisms are organized hierarchically from cells upward.",
            ["Similar cells form a tissue (such as vascular xylem tissue).", "Different tissues combine into an organ (leaf), organs form an organ system (shoot/root system), and systems form the whole organism."],
            "Cell is always the smallest living unit; Organism is the whole living thing.",
            "تتدرج مستويات التنظيم من الخلية حتى الكائن الحي الكامل.",
            ["الخلايا المتشابهة تكوّن نسيجاً، والأنسجة المختلفة تكوّن عضواً كالورقة.", "مجموعة الأعضاء تشكل جهازاً، والأجهزة معاً تكوّن الكائن الحي."],
            "الخلية هي أصغر وحدة بناء ووظيفة في الكائن الحي.",
            _cell_svgs("plant", "Nucleus", "Building Block: Cell", "وحدة البناء: الخلية"),
        ),
        (
            "Why is the cell membrane described as selectively permeable in both plant and animal cells?",
            "لماذا يوصف الغشاء الخلوي بأنه ذو نفاذية اختيارية في كلٍّ من الخلية النباتية والخلية الحيوانية؟",
            [
                ("It allows essential molecules like water and oxygen to enter while blocking harmful substances", "لأنه يسمح بدخول المواد الضرورية كالماء والأكسجين ويمنع مرور المواد الضارة"),
                ("It blocks every substance from entering or leaving the cytoplasm completely", "لأنه يمنع دخول أو خروج أي مادة من السيتوبلازم بشكل تام"),
                ("It converts sunlight directly into rigid cellulose fibers", "لأنه يحول ضوء الشمس مباشرة إلى ألياف سليلوز صلبة"),
                ("It pumps blood throughout the organism's circulatory vessels", "لأنه يضخ الدم عبر الأوعية الدموية في الجسم"),
            ],
            "Consider how a cell stays hydrated and fed without letting toxins inside.",
            "فكر كيف تحصل الخلية على الماء والغذاء وتمنع دخول السموم.",
            "Selective permeability controls molecular traffic across the cell boundary.",
            ["The cell membrane surrounds the cytoplasm in every cell.", "It regulates what enters (nutrients, O₂, water) and exits (wastes, CO₂) to maintain internal balance."],
            "Selectively permeable means picky: some molecules pass easily while others are controlled.",
            "النفاذية الاختيارية تعني تنظيم مرور المواد عبر الغشاء.",
            ["يسمح الغشاء البلازمي بمرور مواد معينة مثل الماء والأكسجين والغذاء.", "وفي الوقت نفسه يمنع دخول المواد غير المرغوب فيها أو الضارة."],
            "هذه الخاصية تحافظ على الاتزان الداخلي للخلية.",
            _cell_svgs("animal", "Membrane", "Cell Boundary", "غشاء الخلية"),
        ),
        (
            "What happens inside an animal cell if a toxin suddenly stops all of its mitochondria from functioning?",
            "ماذا يحدث داخل الخلية الحيوانية إذا أوقف سمٌّ عمل جميع عضيات الميتوكوندريا فجأة؟",
            [
                ("The cell cannot release usable energy from glucose and soon dies", "تتعجز الخلية عن تحرير الطاقة القابلة للاستخدام من الجلوكوز وتموت سريعاً"),
                ("The cell starts making its own food using sunlight instead", "تبدأ الخلية بصنع غذائها من ضوء الشمس بدلاً من ذلك"),
                ("The cell grows a rigid outer cellulose wall for protection", "تكوّن الخلية جداراً خلوياً صلباً من السليلوز للحماية"),
                ("Water storage in a huge central vacuole doubles immediately", "يتضاعف تخزين الماء فوراً في فجوة مركزية ضخمة"),
            ],
            "Recall the primary reaction performed inside mitochondria.",
            "تذكر العملية الحيوية الأساسية التي تحدث داخل الميتوكوندريا.",
            "Stopping mitochondria halts cellular respiration and ATP energy release.",
            ["Mitochondria combine digested glucose with oxygen to release energy.", "Without energy, active transport, movement, and protein repair stop."],
            "Animal cells have no chloroplasts and rely entirely on mitochondria for ATP.",
            "توقف الميتوكوندريا يوقف عملية التنفس الخلوي وإنتاج الطاقة.",
            ["الميتوكوندريا مسؤولة عن تحويل الجلوكوز بوجود الأكسجين إلى طاقة.", "بدون طاقة تتوقف جميع العمليات الحيوية داخل الخلية."],
            "الخلية الحيوانية تعتمد كلياً على الميتوكوندريا لتوليد الطاقة.",
            _cell_svgs("animal", "Mitochondria", "Energy Supply", "إنتاج الطاقة الخلوية"),
        ),
        (
            "A wilted mint stem is placed in a glass of fresh water for two hours and becomes firm and upright again. Which two plant cell structures work together to restore this firmness?",
            "وُضع غصن نعناع ذابل في كوب ماء عذب لمدة ساعتين فاستعاد نضارته وانتصابه. أي تركيبين في الخلية النباتية تعاونا لاستعادة هذا التصلب؟",
            [
                ("Central vacuole filling with water and pushing outward against the rigid cell wall", "امتلاء الفجوة العصارية بالماء وضغطها للخارج على جدار الخلية الصلب"),
                ("Chloroplast releasing oxygen bubbles that lift the stem upward", "إطلاق البلاستيدات الخضراء فقاعات أكسجين ترفع الساق للأعلى"),
                ("Nucleus shrinking to pull water toward the center of the leaf", "انكماش النواة لسحب الماء نحو مركز الورقة"),
                ("Mitochondria hardening the cytoplasm into solid ice crystals", "تحويل الميتوكوندريا للسيتوبلازم إلى بلورات صلبة"),
            ],
            "Think about water pressure pushing from inside against a rigid outer frame.",
            "فكر في ضغط الماء من الداخل على الإطار الخارجي الصلب للخلية.",
            "Turgor pressure results from water-filled vacuoles pressing against cell walls.",
            ["Water moves into the plant cells and fills the central vacuole.", "As the vacuole swells, it presses firmly against the inelastic cell wall, making the stem crisp."],
            "Wilting occurs when vacuoles lose water and pull away from the cell wall.",
            "يحدث الانتصاب بفضل ضغط الامتلاء داخل الخلايا النباتية.",
            ["يدخل الماء إلى الخلايا فتنتفخ الفجوة العصارية المركزية.", "يضغط امتلاء الفجوة على الجدار الخلوي الصلب فيستقيم الغصن."],
            "الذبول يحدث عندما تفقد الفجوات العصارية الماء.",
            _cell_svgs("plant", "Vacuole", "Turgor Pressure", "ضغط الامتلاء في الخلية"),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, (den, dar) in med_b01:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Microscope specimen tables & experimental cell reasoning
    spec_tbl_en = svg_data_table(
        ["Sample", "Cell Wall", "Chloroplast", "Nucleus"],
        [["W", "Yes", "Yes", "Yes"], ["X", "Yes", "No", "Yes"], ["Y", "No", "No", "Yes"], ["Z", "Yes", "No", "No"]],
        "Microscope Cell Survey",
        [72, 86, 98, 86],
    )
    spec_tbl_ar = svg_data_table(
        ["العينة", "جدار خلوي", "بلاستيدة", "نواة"],
        [["W", "نعم", "نعم", "نعم"], ["X", "نعم", "لا", "نعم"], ["Y", "لا", "لا", "نعم"], ["Z", "نعم", "لا", "لا"]],
        "مسح مجهري للعينات",
        [72, 86, 98, 86],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A biologist records four mystery samples (W, X, Y, Z) in the microscope table. Which sample is most likely a bacterial cell, and which is a plant root cell?",
        "سجّل عالم أحياء خصائص أربع عينات مجهولة (W، X، Y، Z) في الجدول الموضح. أي عينة تمثل خلية بكتيرية، وأيها تمثل خلية جذر نباتي على الترتيب؟",
        [
            ("Z is bacterial (no nucleus); X is a plant root cell (cell wall, nucleus, no chloroplasts)", "Z خلية بكتيرية (بلا نواة)، و X خلية جذر نباتي (جدار ونواة دون بلاستيدات)"),
            ("Y is bacterial (no cell wall); W is a plant root cell (has chloroplasts)", "Y خلية بكتيرية (بلا جدار)، و W خلية جذر نباتي (تحتوي بلاستيدات)"),
            ("X is bacterial; Z is a plant root cell because it lacks a nucleus", "X بكتيرية، و Z خلية جذر نباتي لأنها تفتقر للنواة"),
            ("W is bacterial; Y is a plant root cell because animals lack cell walls", "W بكتيرية، و Y خلية جذر نباتي"),
        ],
        "Prokaryotic bacteria have a cell wall but NO membrane-bound nucleus; underground plant roots lack chloroplasts.",
        "البكتيريا بدائية النواة تمتلك جداراً خلوياً دون نواة محاطة بغشاء، وجذور النبات لا تحتوي على بلاستيدات خضراء.",
        "Match each specimen's organelle profile to prokaryotic vs plant vs animal cells.",
        ["Sample Z has a cell wall and lacks a true nucleus → prokaryotic bacterium.", "Sample X has a cell wall and nucleus but no chloroplasts → underground plant root cell; W is a leaf cell; Y is an animal cell."],
        "All four features in the table fit uniquely: W=leaf, X=root, Y=animal, Z=bacterium.",
        "نطابق صفات كل عينة مع خصائص الخلايا النباتية والحيوانية والبكتيرية.",
        ["العينة Z لها جدار خلوي وتخلو من النواة الحقيقية ← بكتيريا.", "العينة X لها جدار خلوي ونواة دون بلاستيدات خضراء ← خلية جذر نباتي؛ بينما W ورقة وY خلية حيوانية."],
        "هذا التصنيف يتطابق تماماً مع جميع خانات الجدول.",
        spec_tbl_en, spec_tbl_ar,
    )

    hard_b01 = [
        (
            "A student places fresh potato strips in two beakers: Beaker A contains pure water, and Beaker B contains concentrated salt water. After 45 minutes, strips in Beaker B become limp and lighter. Why?",
            "وضع طالب شرائح بطاطس طازجة في كأسين: الكأس A فيه ماء نقي، والكأس B فيه محلول ملحي مركز. بعد 45 دقيقة أصبحت شرائح الكأس B رخوة وأخف وزناً. ما التفسير العلمي؟",
            [
                ("Water moved out of the potato cells' vacuoles into the saltier surrounding solution by osmosis", "خرج الماء من الفجوات العصارية لخلايا البطاطس نحو المحلول الملحي الأكثر تركيزاً بالخاصية الأسموزية"),
                ("Salt molecules dissolved the cellulose cell walls completely", "ذوّبت جزيئات الملح جدران الخلايا السليلوزية تماماً"),
                ("The nuclei stopped directing respiration when exposed to table salt", "توقفت النواة عن توجيه التنفس الخلوي عند ملامسة الملح"),
                ("Pure water in Beaker A destroyed the cell membranes of Beaker B", "دمّر الماء النقي في الكأس A أغشية خلايا الكأس B"),
            ],
            "Water diffuses across membranes from higher water concentration (inside cell) to lower water concentration (salty water).",
            "ينتقل الماء عبر الغشاء شبه المنفذ من المنطقة الأعلى تركيزاً بالماء إلى الأقل تركيزاً بالماء.",
            "Osmosis pulls water out of plant cells in hypertonic salt solutions.",
            ["Concentrated salt water has less free water per volume than potato cell sap.", "Water exits the vacuoles through the cell membrane, decreasing turgor pressure and mass."],
            "In Beaker A (pure water), potato strips absorb water and become crisper.",
            "الخاصية الأسموزية تسحب الماء من داخل الخلايا إلى المحلول المركز.",
            ["تركيز الماء خارج الخلية في المحلول الملحي أقل من تركيزه داخل الفجوة العصارية.", "لذلك يخرج الماء من الخلايا فينخفض ضغط الامتلاء وتصبح الشرائح رخوة وأقل كتلة."],
            "أما في الماء النقي فتمتص الخلايا الماء وتزداد صلابتها.",
            _cell_svgs("plant", "Vacuole", "Osmosis in Plant Cell", "الأسموزية في الخلية النباتية"),
        ),
        (
            "Suppose a red blood cell (an animal cell) is placed in pure distilled water, while a leaf cell is placed in the same water. The red blood cell bursts, but the leaf cell only swells firmly. Why?",
            "وُضعت خلية دم حمراء (حيوانية) في ماء مقطر نقي، بينما وُضعت خلية ورقة نباتية في الماء نفسه؛ فانفجرت خلية الدم بينما انتفخت الخلية النباتية وثبتت دون أن تنفجر. لماذا؟",
            [
                ("The leaf cell's rigid cellulose cell wall resists excessive expansion, whereas the animal cell lacks a cell wall", "لأن جدار الخلية النباتية الصلب يقاوم التمدد الزائد، بينما تفتقر الخلية الحيوانية لجدار خلوي"),
                ("Red blood cells lack a cell membrane to hold cytoplasm inside", "لأن خلايا الدم الحمراء تفتقر إلى الغشاء الخلوي"),
                ("Leaf cells pump excess distilled water out using chloroplasts", "لأن خلايا الورقة تضخ الماء الزائد باستخدام البلاستيدات الخضراء"),
                ("Animal cells absorb ten times more salt than plant cells", "لأن الخلايا الحيوانية تمتص أملاحاً أكثر بعشر مرات"),
            ],
            "Identify the structural difference between plant and animal outer boundaries.",
            "حدد التركيب الخارجي الموجود في الخلية النباتية والغائب عن الحيوانية.",
            "The rigid cell wall prevents plant cells from bursting due to water uptake.",
            ["Pure water enters both cells by osmosis.", "The animal cell only has a flexible membrane so it bursts; the plant cell pushes against its tough cell wall and stops swelling."],
            "This explains why plants thrive in fresh rainwater without exploding.",
            "يمنع الجدار الخلوي انفجار الخلية النباتية عند امتصاص الماء.",
            ["يدخل الماء النقي إلى كلتا الخليتين بالأسموزية.", "تملك الخلية الحيوانية غشاءً مرناً فقط فتنفجر، أما الخلية النباتية فيحميها جدارها الخلوي الصلب."],
            "يوضح ذلك قدرة النبات على تحمل الري بالماء العذب.",
            _cell_svgs("animal", "Membrane", "No Cell Wall Protection", "غياب الجدار الخلوي"),
        ),
        (
            "A genetic mutation disables the chlorophyll inside a seedling's leaves while leaving its roots, xylem, and mitochondria normal. Why will this white seedling survive for only a few days after using up its seed food?",
            "أدت طفرة وراثية إلى تعطيل الكلوروفيل في أوراق بادرة نباتية مع بقاء جذورها والخشب والميتوكوندريا سليمة. لماذا تعيش البادرة البيضاء أياماً معدودة فقط بعد نفاد غذاء البذرة؟",
            [
                ("Without functional chlorophyll, chloroplasts cannot make glucose, so mitochondria soon run out of fuel for energy", "لأن غياب الكلوروفيل يمنع صنع الجلوكوز في البلاستيدات، فينفد وقود الميتوكوندريا اللازم لإنتاج الطاقة"),
                ("Without chlorophyll, the plant's xylem tubes cannot pull liquid water from the soil", "لأن غياب الكلوروفيل يمنع أوعية الخشب من سحب الماء من التربة"),
                ("White leaves lose their nuclei and cannot copy DNA during growth", "لأن الأوراق البيضاء تفقد نواتها ولا تستطيع نسخ المادة الوراثية"),
                ("Mitochondria directly absorb sunlight instead of chlorophyll but produce toxic acid", "لأن الميتوكوندريا تمتص الضوء بدلاً من الكلوروفيل وتنتج حمضاً ساماً"),
            ],
            "Connect chloroplast food production to mitochondrial energy release.",
            "اربط بين صنع الغذاء في البلاستيدات واستهلاكه في الميتوكوندريا.",
            "Chloroplasts make glucose; mitochondria oxidize that glucose to power survival.",
            ["Seedlings initially grow using stored starch inside the seed.", "Once that reserve ends, an albino seedling cannot photosynthesize new glucose, starving its working mitochondria."],
            "Both organelles depend on each other in green plants.",
            "تصنع البلاستيدات الجلوكوز وتستخدمه الميتوكوندريا لإطلاق الطاقة.",
            ["تعتمد البادرة في أيامها الأولى على الغذاء المخزن في البذرة.", "بعد نفاده تعجز عن تصنيع جلوكوز جديد لعدم وجود كلوروفيل فتموت رغم سلامة الميتوكوندريا."],
            "يتكامل عمل البلاستيدة والميتوكوندريا لاستمرار حياة النبات.",
            _cell_svgs("plant", "Chloroplast", "Albino Seedling Check", "أثر غياب الكلوروفيل"),
        ),
        (
            "Four students examine an unknown slide and argue over whether it shows a multicellular plant tissue or a colony of animal cells. Which microscopic observation settles the debate in favor of plant tissue?",
            "فحص أربعة طلاب شريحة مجهولة واختلفوا هل هي نسيج نباتي أم خلايا حيوانية. أي ملاحظة مجهرية تحسم النقاش لصالح النسيج النباتي بشكل قاطع؟",
            [
                ("Box-like cells tightly joined by thick outer walls with large central fluid sacs", "خلايا منتظمة متراصة محاطة بجدران سميكة وبداخلها فجوات عصارية مركزية كبيرة"),
                ("Round cells containing both nuclei and small mitochondria in their cytoplasm", "خلايا مستديرة تحتوي على نواة وميتوكوندريا صغيرة في السيتوبلازم"),
                ("Flexible outer boundaries changing shape slightly as fluid moves", "أغشية خارجية مرنة يتغير شكلها قليلاً مع حركة السائل"),
                ("Presence of cytoplasm surrounded by a selectively permeable plasma membrane", "وجود سيتوبلازم محاط بغشاء بلازمي ذي نفاذية اختيارية"),
            ],
            "Which combination of structures is unique to plants and absent in all animal cells?",
            "ما الصفات الحصرية للخلية النباتية والغائبة في الخلية الحيوانية؟",
            "Only plant cells combine cellulose cell walls and large central vacuoles (often with chloroplasts).",
            ["Nuclei, mitochondria, cytoplasm, and cell membranes occur in BOTH plant and animal cells.", "Thick rigid box-like cell walls plus large central vacuoles uniquely confirm plant tissue."],
            "Even non-green plant cells (roots/petals) exhibit rigid walls and large central vacuoles.",
            "تتميز الخلايا النباتية بالجدار الخلوي والفجوة المركزية الكبيرة.",
            ["النواة والميتوكوندريا والسيتوبلازم والغشاء الخلوي مشتركة بين النبات والحيوان.", "وجود جدار خلوي صلب وفجوة مركزية كبيرة يحسم أن العينة نباتية."],
            "هذه السمات ثابتة في الأنسجة النباتية حتى غير الخضراء منها.",
            _cell_svgs("plant", "Cell Wall", "Plant vs Animal Clue", "تمييز النسيج النباتي"),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, (den, dar) in hard_b01:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b02(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B02"
    # Easy (0..4): Kingdoms, vertebrates & invertebrates
    easy_b02 = [
        (
            "Bread mold and mushrooms lack chlorophyll and obtain nutrients by secreting enzymes onto decaying organic matter and absorbing it. To which kingdom do they belong?",
            "يخلو عفن الخبز وفطر المشروم من الكلوروفيل، ويحصلان على غذائهما بإفراز إنزيمات على المواد العضوية المتحللة وامتصاصها. إلى أي مملكة ينتميان؟",
            [
                ("Fungi", "مملكة الفطريات"),
                ("Plants", "مملكة النباتات"),
                ("Animals", "مملكة الحيوانات"),
                ("Bacteria", "مملكة البكتيريا"),
            ],
            "They have cell walls and nuclei, cannot photosynthesize, and act as decomposers.",
            "تمتلك خلاياها نواة وجداراً خلوياً ولا تصنع غذاءها بنفسها بل تحلل البقايا.",
            "Fungi are heterotrophic absorptive decomposers without chlorophyll.",
            ["Unlike plants, fungi lack chloroplasts and cannot perform photosynthesis.", "Unlike animals, fungi do not ingest food internally; they absorb digested nutrients externally."],
            "Mushrooms, yeasts, and molds all belong to Kingdom Fungi.",
            "الفطريات كائنات غير ذاتية التغذية تمتص الغذاء من البيئة.",
            ["تفتقر الفطريات إلى الكلوروفيل لذا لا تنتمي للنباتات.", "وتهضم غذاءها خارجياً ثم تمتصه بعكس الحيوانات."],
            "المشروم والخميرة والعفن أمثلة على الفطريات.",
            None, None,
        ),
        (
            "Which group of vertebrates begins life breathing underwater through gills and later develops lungs and moist skin to live on land and in water?",
            "أي طائفة من الفقاريات تبدأ حياتها في الماء بالتنفس عبر الخياشيم ثم تطور رئتين وجلداً رطباً للعيش على اليابسة وفي الماء؟",
            [
                ("Amphibians", "البرمائيات"),
                ("Reptiles", "الزواحف"),
                ("Mammals", "الثدييات"),
                ("Birds", "الطيور"),
            ],
            "Think of frogs and salamanders undergoing metamorphosis.",
            "فكر في الضفادع والسمندل ومراحل تحولها.",
            "Amphibians lead a dual aquatic-and-terrestrial life cycle.",
            ["Tadpoles hatch from jelly-coated eggs in water with gills and tails.", "Adults grow legs and lungs and exchange extra oxygen through thin moist skin."],
            "Reptiles have dry scales and breathe only with lungs from hatching.",
            "تعيش البرمائيات جزءاً من حياتها في الماء وجزءاً على اليابسة.",
            ["تبدأ صغارها كأبي ذنيبة تتنفس بالخياشيم في الماء.", "ثم تنمو لها رئات وأطراف وتستخدم جلدها الرطب للمساعدة في التنفس."],
            "تختلف عن الزواحف التي تمتلك جلداً جافاً مغطى بالحراشف.",
            None, None,
        ),
        (
            "An invertebrate found in the Red Sea has an external skeleton (exoskeleton), jointed legs, and a segmented body. Which phylum does this organism belong to?",
            "حيوان لا فقاري في البحر الأحمر له هيكل خارجي صلب وأرجل مفصلية وجسم مقسم إلى قطع. إلى أي شعبة ينتمي هذا الحيوان؟",
            [
                ("Arthropods", "المفصليات"),
                ("Mollusks", "الرخويات"),
                ("Cnidarians", "اللاسعات"),
                ("Annelids", "الديدان الحلقية"),
            ],
            "The word literally means 'jointed feet' — like crabs, shrimp, scorpions, and locusts.",
            "اسم الشعبة مشتق من امتلاكها أرجلاً مفصلية كالسرطان والجراد والعقرب.",
            "Arthropods have segmented bodies, jointed appendages, and chitin exoskeletons.",
            ["Crabs, lobsters, insects, and spiders all share an outer exoskeleton and jointed legs.", "They make up the largest phylum in the animal kingdom."],
            "Mollusks have soft unsegmented bodies; cnidarians have stinging tentacles.",
            "تتميز المفصليات بوجود هيكل خارجي صلب وأطراف مفصلية.",
            ["تشمل القشريات البحرية كالروبيان والسلطعون إضافة إلى الحشرات والعنكبيات.", "وهي أكبر شعب المملكة الحيوانية."],
            "تختلف عن الرخويات ذات الأجسام اللينة غير المقسمة.",
            None, None,
        ),
        (
            "Why do mosses stay only a few centimeters tall and grow closely packed on damp shaded rocks?",
            "لماذا تبقى الحزازيات قصيرة جداً لا تتجاوز بضعة سنتيمترات وتنمو متقاربة على الصخور الرطبة الظليلة؟",
            [
                ("They are nonvascular plants without xylem or phloem tubes to lift water high", "لأنها نباتات لاوعائية تفتقر إلى أوعية الخشب واللحاء لرفع الماء إلى ارتفاعات عالية"),
                ("They are fungi that melt when exposed to warm morning air", "لأنها فطريات تذوب عند تعرضها لهواء الصباح الدافئ"),
                ("Their seeds are too heavy to rise above soil level", "لأن بذورها ثقيلة جداً لا ترتفع عن سطح التربة"),
                ("They lack cell walls and must lean against rocks like jellyfish", "لأنها تفتقر لجدران الخلايا فتستند على الصخور"),
            ],
            "Compare plants that have internal plumbing tubes with those that move water cell-to-cell.",
            "قارن بين النباتات التي تملك أنابيب نقل داخلية وتلك التي تنقل الماء من خلية لأخرى.",
            "Nonvascular plants rely on slow cell-to-cell osmosis and diffusion.",
            ["Mosses have no true roots, stems, or vascular xylem/phloem vessels.", "Water can only travel short distances by osmosis, keeping mosses small and tied to moist habitats."],
            "Vascular plants like date palms grow tall using xylem vessels.",
            "الحزازيات نباتات لاوعائية تنقل الماء ببطء من خلية إلى أخرى.",
            ["لا تحتوي على جذور حقيقية أو أوعية خشب ولحاء لنقل الماء لمسافات طويلة.", "لذا تبقى صغيرة الحجم وتحتاج إلى بيئة رطبة."],
            "بعكس النخيل والأشجار الوعائية التي تنمو لارتفاعات شاهقة.",
            None, None,
        ),
        (
            "Which characteristic is shared by BOTH birds and mammals, setting them apart from fish, amphibians, and reptiles?",
            "ما الصفة المشتركة بين الطيور والثدييات والتي تميزهما عن الأسماك والبرمائيات والزواحف؟",
            [
                ("Both are warm-blooded (endothermic) and keep a steady internal body temperature", "كلاهما من ذوات الدم الحار (ثابتة درجة الحرارة) وتحافظ على ثبات حرارة جسمها"),
                ("Both breathe underwater through gills throughout adulthood", "كلاهما يتنفس تحت الماء بالخياشيم طوال مرحلة البلوغ"),
                ("Both have dry scaly skin and lay soft leathery eggs on sand", "كلاهما يملك جلداً جافاً بحراشف ويضع بيضاً جلدياً على الرمل"),
                ("Both lack a vertebral column and possess an exoskeleton", "كلاهما يفتقر للعمود الفقري ويمتلك هيكلاً خارجياً"),
            ],
            "Think about how a desert falcon or camel maintains body temperature on a freezing desert night.",
            "فكر في كيفية حفاظ الصقر أو الجمل على درجة حرارة جسمه في ليالي الصحراء الباردة.",
            "Birds and mammals are endothermic vertebrates.",
            ["Endotherms generate internal metabolic heat to keep body temperature constant regardless of weather.", "Fish, amphibians, and reptiles are ectothermic (cold-blooded)."],
            "Feathers (birds) and hair/fur (mammals) insulate that internal heat.",
            "الطيور والثدييات فقاريات ثابتة درجة الحرارة.",
            ["تنتج أجسامها حرارة داخلية تحافظ على استقرار حرارة الجسم مهما تغير الجو.", "أما الأسماك والبرمائيات والزواحف فمتغيرة درجة الحرارة."],
            "يساعد الريش والفرو في عزل هذه الحرارة الداخلية.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b02:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Classifying Saudi & global organisms + card SVGs
    med_b02 = [
        (
            "The Arabian spiny-tailed lizard (Dhub) basks on desert rocks each morning before foraging, has dry overlapping scales, and lays eggs in burrows. How should scientists classify the Dhub?",
            "يتشمس الضب العربي على صخور الصحراء صباحاً قبل البحث عن غذائه، ويغطي جسمه حراشف جافة ويضع بيضه في الجحور. كيف يصنف العلماء الضب؟",
            [
                ("Cold-blooded (ectothermic) reptile", "زاحف من ذوات الدم البارد (متغير درجة الحرارة)"),
                ("Warm-blooded (endothermic) mammal", "ثديي من ذوات الدم الحار (ثابت درجة الحرارة)"),
                ("Cold-blooded amphibian", "برمائي متغير درجة الحرارة"),
                ("Jointed-legged arthropod invertebrate", "لافقاري من المفصليات"),
            ],
            "Basking in sunlight raises body temperature, and dry scales prevent desert water loss.",
            "التعرض للشمس لرفع حرارة الجسم مع جلد جاف بحراشف صفتان مميزتان.",
            "Dry scaly skin, lungs, and behavioral thermoregulation define reptiles.",
            ["Basking shows the Dhub relies on external heat (ectothermic).", "Dry scales and land eggs identify it as a reptile, not an amphibian."],
            "All lizards, snakes, turtles, and crocodiles are reptiles.",
            "الحراشف الجافة والاعتماد على حرارة الشمس من خصائص الزواحف.",
            ["تشمس الضب يدل على أنه متغير درجة الحرارة.", "جلده الجاف ذو الحراشف ووضعه البيض على اليابسة يضعانه ضمن الزواحف."],
            "السحالي والثعابين والسلاحف جميعها زواحف.",
            svg_data_table(["Organism", "Skin", "Temp", "Eggs"], [["Dhub", "Dry scales", "Varies", "On land"]], "Field Observation Card", [84, 92, 74, 84]),
            svg_data_table(["الكائن", "الجلد", "الحرارة", "البيض"], [["الضب", "حراشف جافة", "متغيرة", "على اليابسة"]], "بطاقة ملاحظة ميدانية", [84, 92, 74, 84]),
        ),
        (
            "Dolphins in the Arabian Gulf swim underwater like fish, yet biologists classify them as mammals. Which two traits prove a dolphin is a mammal rather than a fish?",
            "تسبح الدلافين في الخليج العربي مثل الأسماك، لكن العلماء يصنفونها ضمن الثدييات. ما الصفتان اللتان تثبتان أن الدلفين ثديي وليس سمكة؟",
            [
                ("It breathes air with lungs and nurses its young with milk", "يتنفس الهواء بالرئتين ويرضع صغاره الحليب"),
                ("It has fins for steering and lives in saltwater seas", "يمتلك زعانف للتوجيه ويعيش في المياه المالحة"),
                ("It has a streamlined shape and a cold-blooded metabolism", "له جسم انسيابي ودم بارد متغير الحرارة"),
                ("It breathes dissolved oxygen through gills and lays thousands of eggs", "يتنفس الأكسجين الذائب بالخياشيم ويضع آلاف البيض"),
            ],
            "Think about why dolphins surface periodically through a blowhole and care for calves.",
            "فكر لماذا يصعد الدلفين إلى سطح الماء باستمرار وكيف يغذي صغاره.",
            "Mammals breathe air via lungs, are warm-blooded, and feed young milk.",
            ["Streamlined bodies and fins are adaptations to water shared with fish, not proof of fish ancestry.", "Breathing air with lungs, steady warm body temperature, and milk glands define mammals."],
            "Whales, dolphins, and bats are all air-breathing, milk-producing mammals.",
            "تتنفس الثدييات البحرية بالرئتين وترضع صغارها الحليب.",
            ["الشكل الانسيابي والزعانف تكيف للسباحة ولا تجعله سمكة.", "صعوده للتنفس بالرئتين وإرضاعه لصغاره يثبتان أنه من الثدييات."],
            "الحيتان والدلافين والخفافيش جميعها ثدييات.",
            svg_data_table(["Trait", "Shark", "Dolphin"], [["Breathing", "Gills", "Lungs"], ["Body Temp", "Cold-blooded", "Warm-blooded"], ["Young", "Eggs/pups", "Nursed w/ milk"]], "Marine Vertebrate Check", [92, 112, 126]),
            svg_data_table(["الصفة", "القرش", "الدلفين"], [["التنفس", "خياشيم", "رئتان"], ["الحرارة", "متغيرة", "ثابتة"], ["الصغار", "لا يرضع", "يرضع حليباً"]], "مقارنة الفقاريات البحرية", [92, 112, 126]),
        ),
        (
            "A student catches a garden creature with 8 legs, two main body segments, and no antennae or wings. Which subgroup of arthropods did the student find?",
            "أمسك طالب بكائن صغير في الحديقة له 8 أرجل وجسم من جزأين رئيسيين دون قرون استشعار أو أجنحة. إلى أي مجموعة من المفصليات ينتمي؟",
            [
                ("Arachnids (such as spiders and scorpions)", "العنكبيات (مثل العناكب والعقارب)"),
                ("Insects (such as beetles and locusts)", "الحشرات (مثل الخنافس والجراد)"),
                ("Crustaceans (such as crabs and shrimp)", "القشريات (مثل السرطان والروبيان)"),
                ("Mollusks (such as snails and octopuses)", "الرخويات (مثل الحلزون والأخطبوط)"),
            ],
            "Insects always have 6 legs and 3 body parts; count the legs here carefully!",
            "للحشرات دائماً 6 أرجل و3 أقسام جسمية؛ انتبه لعدد الأرجل هنا!",
            "Leg count and body division distinguish arthropod classes.",
            ["Insects have 6 legs, 3 body parts (head, thorax, abdomen), and antennae.", "Arachnids have 8 legs, 2 body regions, and zero antennae or wings."],
            "Spiders, ticks, and scorpions are classic arachnids.",
            "تُفرّق طوائف المفصليات بعدد الأرجل وأقسام الجسم.",
            ["تمتلك الحشرات 6 أرجل وقرني استشعار و3 أجزاء جسمية.", "أما العنكبيات فلها 8 أرجل وجزءان فقط دون قرون استشعار."],
            "العناكب والعقارب والقراد من العنكبيات.",
            svg_data_table(["Group", "Legs", "Body Parts"], [["Insects", "6", "3"], ["Arachnids", "8", "2"], ["Crab", "10", "2"]], "Arthropod Key", [110, 96, 112]),
            svg_data_table(["المجموعة", "الأرجل", "أقسام الجسم"], [["الحشرات", "6", "3"], ["العنكبيات", "8", "2"], ["السرطان", "10", "2"]], "مفتاح المفصليات", [110, 96, 112]),
        ),
        (
            "A coral reef diver touches a sea star and notices spiny tube-like bumps arranged in 5 equal arms around a central disk. To which invertebrate group does the sea star belong?",
            "لاحظ غواص في البحر الأحمر وجود نجم بحر له جلد شوكي و5 أذرع متماثلة شعاعياً حول قرص مركزي. إلى أي مجموعة لا فقارية ينتمي نجم البحر؟",
            [
                ("Echinoderms (spiny-skinned radial invertebrates)", "شوكيات الجلد (لافقاريات ذات جلد شوكي وتماثل شعاعي)"),
                ("Annelids (segmented worms)", "الديدان الحلقية"),
                ("Cnidarians (jellyfish and sea anemones)", "اللاسعات"),
                ("Mammals (marine vertebrates)", "الثدييات البحرية"),
            ],
            "The prefix 'echino-' means spiny and '-derm' means skin.",
            "اسم هذه الشعبة يشير مباشرة إلى جلدها الشوكي وتماثلها الشعاعي.",
            "Sea stars, sea urchins, and brittle stars belong to Echinoderms.",
            ["Echinoderms live exclusively in saltwater oceans.", "They exhibit 5-part radial symmetry, spiny internal plates, and tube feet."],
            "Unlike jellyfish (cnidarians), sea stars have rigid spiny skin and tube feet.",
            "تنتمي نجوم البحر وقنافذ البحر إلى شوكيات الجلد.",
            ["تعيش شوكيات الجلد في البحار وتتميز بتماثل شعاعي غالباً خماسي الأذرع.", "تتحرك بواسطة الأقدام الأنبوبية ولها جلد ذو أشواك."],
            "تختلف عن اللاسعات مثل قنديل البحر التي تفتقر للجلد الشوكي.",
            None, None,
        ),
        (
            "A botanist groups wild plants into two baskets: Basket 1 contains pine trees and ferns; Basket 2 contains mosses and liverworts. What criterion divides Basket 1 from Basket 2?",
            "قسّم عالم نبات نباتات برية إلى سلتين: السلة 1 تضم الصنوبر والسراخس، والسلة 2 تضم الحزازيات وحشيشة الكبد. ما المعيار الذي يفرّق السلة 1 عن السلة 2؟",
            [
                ("Presence of vascular tissue (xylem and phloem) in Basket 1 vs. absence in Basket 2", "وجود الأنسجة الوعائية (الخشب واللحاء) في السلة 1 وغيابها في السلة 2"),
                ("Presence of flowers in Basket 1 vs. absence of chlorophyll in Basket 2", "وجود الأزهار في السلة 1 وغياب الكلوروفيل في السلة 2"),
                ("Ability to make spores in Basket 1 vs. seeds in Basket 2", "التكاثر بالأبواغ في السلة 1 وبالبذور في السلة 2"),
                ("Living in oceans in Basket 1 vs. deserts in Basket 2", "العيش في المحيطات في السلة 1 وفي الصحاري في السلة 2"),
            ],
            "Remember ferns reproduce by spores like mosses, yet ferns grow tall because they have internal transport tubes!",
            "تذكر أن السراخس تتكاثر بالأبواغ مثل الحزازيات، لكنها تنمو أطول بفضل وجود أنابيب نقل داخلية!",
            "Vascular vs. nonvascular plants is the primary division of Kingdom Plantae.",
            ["Both pine trees and ferns contain vascular xylem and phloem tubes (though ferns lack seeds and pines lack flowers).", "Mosses and liverworts are nonvascular and lack true roots, stems, and leaves."],
            "Vascular tubes explain how ferns and pines grow much taller than mosses.",
            "ينقسم عالم النبات أساساً إلى نباتات وعائية ولاوعائية.",
            ["تمتلك السراخس والصنوبر أنسجة وعائية لنقل الماء والغذاء، مع أن السراخس لا تكون بذوراً والصنوبر لا يزهر.", "تخلو الحزازيات من الأنسجة الوعائية الحقيقية."],
            "لذلك يكون التمييز الدقيق بين السلتين هو وجود الأنسجة الوعائية.",
            svg_data_table(["Basket", "Examples", "Height"], [["Basket 1", "Pine, Fern", "Tall"], ["Basket 2", "Moss, Liverwort", "Tiny"]], "Plant Grouping Check", [84, 134, 86]),
            svg_data_table(["السلة", "الأمثلة", "الارتفاع"], [["السلة 1", "صنوبر، سرخس", "طويل"], ["السلة 2", "حزاز، حشيشة الكبد", "قصير جداً"]], "تصنيف النباتات", [84, 146, 86]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b02:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Dichotomous key & organism trait tables
    key_tbl_en = svg_data_table(
        ["Creature", "Backbone", "Temp", "Breathing"],
        [["K", "Yes", "Warm", "Lungs"], ["L", "Yes", "Cold", "Gills -> Lungs"], ["M", "No", "Cold", "Spiracles"], ["N", "Yes", "Cold", "Gills only"]],
        "Field Survey Organisms",
        [82, 82, 72, 108],
    )
    key_tbl_ar = svg_data_table(
        ["الكائن", "عمود فقري", "الحرارة", "التنفس"],
        [["K", "نعم", "ثابتة", "رئتان"], ["L", "نعم", "متغيرة", "خياشيم ← رئتان"], ["M", "لا", "متغيرة", "ثغور تنفسية"], ["N", "نعم", "متغيرة", "خياشيم فقط"]],
        "جدول مسح الكائنات",
        [72, 84, 76, 114],
    )
    B.add_concept(
        tp, "Hard", bp,
        "Using the field survey table, which creature matches a fruit bat (mammal), and which matches a desert locust (insect)?",
        "بالاستعانة بجدول المسح الميداني، أي كائن يطابق خفاش الفاكهة (ثديي)، وأيهما يطابق الجراد الصحراوي (حشرة) على الترتيب؟",
        [
            ("K is the bat (vertebrate, warm-blooded, lungs); M is the locust (invertebrate, spiracles)", "K يمثل الخفاش (فقاري، ثابت الحرارة، رئتان)، و M يمثل الجراد (لافقاري بثغور تنفسية)"),
            ("L is the bat (cold-blooded); N is the locust (breathes only with gills)", "L يمثل الخفاش، و N يمثل الجراد"),
            ("M is the bat (no backbone so it can fly); K is the locust", "M يمثل الخفاش لأن الطيران بلا عمود فقري، و K يمثل الجراد"),
            ("N is the bat; L is the locust because insects transform from water", "N يمثل الخفاش، و L يمثل الجراد"),
        ],
        "Bats have internal skeletons (backbones) and nurse young; insects lack backbones and breathe via tiny air tubes (spiracles).",
        "يمتلك الخفاش عموداً فقرياً ورئتين وحرارة ثابتة، بينما الجراد لا فقاري يتنفس بالقصيبات الهوائية.",
        "Filter each creature by backbone, thermoregulation, and breathing structures.",
        ["K has a backbone, warm body temperature, and lungs → mammal (bat), NOT bird, though both K traits fit endotherms.", "M lacks a backbone and breathes air via spiracles → insect (locust), while L is an amphibian and N is a fish."],
        "Notice a bat's wings do NOT make it a bird or invertebrate.",
        "نفرز الكائنات وفق العمود الفقري وثبات الحرارة وآلية التنفس.",
        ["الكائن K فقاري ثابت الحرارة ويتنفس بالرئتين ← الخفاش (ثديي).", "الكائن M لا فقاري يتنفس عبر ثغور وقصيبات تنفسية ← الجراد (حشرة)، بينما L برمائي وN سمكة."],
        "تغطي جميع الصفات الأربع الكائنات بدقة دون تناقض.",
        key_tbl_en, key_tbl_ar,
    )

    hard_b02 = [
        (
            "A student finds a microscopic single-celled organism in pond water. Under the microscope, it has a membrane-bound nucleus and chloroplasts, AND swims using a whip-like flagellum. Why does it NOT fit cleanly into either Plants or Bacteria?",
            "وجد طالب كائناً وحيد الخلية في ماء بركة. أظهر المجهر أنه يمتلك نواة حقيقية وبلاستيدات خضراء ويتحرك بسوط. لماذا لا يُصنف مع النباتات ولا مع البكتيريا؟",
            [
                ("It has a true nucleus (so not Bacteria) and is unicellular and motile (so classified as a Protist rather than a Plant)", "لأن له نواة حقيقية (فليس بكتيريا) وهو وحيد الخلية متحرك بالسوط (فيُصنف ضمن الطلائعيات لا النباتات)"),
                ("It lacks DNA completely and only viruses have flagella", "لأنه يفتقر للحمض النووي والفيروسات وحدها تملك أسواطاً"),
                ("Bacteria are always multicellular while plants lack nuclei", "لأن البكتيريا عديدة الخلايا دائماً والنباتات بلا أنوية"),
                ("Any green organism that moves is automatically classified as a vertebrate animal", "لأن أي كائن أخضر متحرك يُعد حيواناً فقارياً"),
            ],
            "Consider Kingdom Protista (like Euglena): eukaryotic, mostly unicellular, with mixed plant-like or animal-like traits.",
            "فكر في مملكة الطلائعيات (مثل اليوجلينا): حقيقية النواة وحيدة الخلية وتجمع صفات متنوعة.",
            "Protists are eukaryotes that are neither true plants, animals, nor fungi.",
            ["Having a membrane-bound nucleus rules out prokaryotic Bacteria.", "Being unicellular and swimming actively with a flagellum rules out true multicellular Plants → Protist (e.g., Euglena)."],
            "Kingdom Protista bridges unicellular eukaryotes with diverse feeding styles.",
            "تضم الطلائعيات كائنات حقيقية النواة لا تنطبق عليها صفات النباتات أو الحيوانات أو الفطريات.",
            ["وجود نواة محاطة بغشاء يستبعد البكتيريا بدائية النواة.", "وكونه وحيد الخلية متحركاً بسوط يجعله من الطلائعيات مثل اليوجلينا وليس نباتاً متعدد الخلايا."],
            "وهذا يفسر وجود الكلوروفيل والحركة معاً في كائن مجهري.",
            svg_data_table(["Feature", "Specimen", "Match"], [["Nucleus", "Yes", "Eukaryote"], ["Cells", "Single cell", "Unicellular"], ["Energy", "Chloroplast", "Protist"]], "Pond Mystery Cell", [92, 108, 108]),
            svg_data_table(["الصفة", "العينة", "الدلالة"], [["النواة", "موجودة", "حقيقي النواة"], ["الخلايا", "خلية واحدة", "وحيد الخلية"], ["التغذية", "بلاستيدات", "طلائعيات"]], "كائن مجهري من البركة", [92, 108, 108]),
        ),
        (
            "An expedition finds four organisms on Farasan Island: (1) Squid, (2) Green Sea Turtle, (3) Dugong (sea cow), (4) Hammerhead Shark. Which two belong to different classes even though both breathe ONLY with lungs?",
            "رصد فريق بحثي في جزر فرسان أربعة كائنات: (1) الحبار، (2) السلحفاة البحرية الخضراء، (3) الأطوم (بقرة البحر)، (4) قرش أبو مطرقة. أي كائنين ينتميان لطائفتين مختلفتين رغم أن كليهما يتنفس بالرئتين فقط؟",
            [
                ("Green Sea Turtle (Reptile) and Dugong (Mammal)", "السلحفاة البحرية الخضراء (زواحف) والأطوم (ثدييات)"),
                ("Squid (Mollusk) and Hammerhead Shark (Fish)", "الحبار (رخويات) وقرش أبو مطرقة (أسماك)"),
                ("Dugong (Fish) and Hammerhead Shark (Mammal)", "الأطوم (أسماك) وقرش أبو مطرقة (ثدييات)"),
                ("Green Sea Turtle (Amphibian) and Squid (Arthropod)", "السلحفاة البحرية (برمائيات) والحبار (مفصليات)"),
            ],
            "Neither squid nor shark breathes with lungs! Check the two air-breathing marine animals.",
            "الحبار والقرش يتنفسان بالخياشيم؛ انظر إلى الكائنين اللذين يصعدان للتنفس بالرئتين.",
            "Marine reptiles (turtles) and marine mammals (dugongs) both breathe air via lungs.",
            ["Squid (mollusk) and Hammerhead Shark (cartilaginous fish) both use gills.", "Green Sea Turtle is an egg-laying, cold-blooded reptile with lungs; Dugong is a milk-nursing, warm-blooded mammal with lungs."],
            "Both surface for air, yet differ in thermoregulation and reproduction.",
            "تشترك الزواحف البحرية والثدييات البحرية في التنفس بالرئتين وتختلفان في الطائفة.",
            ["الحبار (رخويات) والقرش (أسماك) يتنفسان بالخياشيم.", "أما السلحفاة البحرية فزاحف متغير الحرارة يبيض على الشاطئ، والأطوم ثديي ثابت الحرارة يرضع صغاره."],
            "كلاهما يصعد للسطح للتنفس بالرئتين رغم اختلاف طائفتهما.",
            None, None,
        ),
        (
            "A student claims: 'A jellyfish and a tilapia fish are both fish because both swim in water and lack lungs.' Which biological correction accurately refutes this claim?",
            "يدعي طالب أن قنديل البحر وسمكة البلطي ينتميان معاً إلى طائفة الأسماك لأنهما يسبحان في الماء ولا يملكان رئتين. أي تصحيح علمي يفند هذا الادعاء بدقة؟",
            [
                ("A tilapia has a bony backbone and gills (vertebrate fish), whereas a jellyfish has no backbone and belongs to cnidarians", "سمكة البلطي فقارية ذات عمود فقري وخياشيم، بينما قنديل البحر لافقاري يفتقر للعمود الفقري وينتمي للاسعات"),
                ("A jellyfish is actually a marine mammal that nurses young underwater", "قنديل البحر ثديي بحري يرضع صغاره تحت الماء"),
                ("Tilapia fish are amphibians because they also swim in freshwater lakes", "سمكة البلطي من البرمائيات لأنها تسبح في البحيرات العذبة"),
                ("Jellyfish belong to Kingdom Fungi because their bodies are soft and gelatinous", "ينتمي قنديل البحر لمملكة الفطريات لأن جسمه هلامي"),
            ],
            "Check the presence of an internal backbone and gills.",
            "قارن بين وجود العمود الفقري والخياشيم في السمكة وغيابهما في القنديل.",
            "Habitat alone does not determine biological classification.",
            ["Fish are vertebrates with a backbone, fins, scales, and gills.", "Jellyfish are invertebrates (Cnidarians) with soft bell bodies, stinging tentacles, and no backbone or gills."],
            "Living in the same aquatic habitat causes similar movement without making them the same group.",
            "التشابه في البيئة المائية لا يعني الانتماء إلى الطائفة نفسها.",
            ["تمتلك سمكة البلطي عموداً فقرياً وزعانف وخياشيم فهي سمكة فقارية.", "أما قنديل البحر فجسمه هلامي بلا عمود فقري وله لوامس لاسعة، لذا فهو لافقاري من اللاسعات."],
            "العمود الفقري والتراكيب التشريحية هما أساس التصنيف.",
            None, None,
        ),
        (
            "In a dichotomous key, scientists separate four newly discovered land animals: (A) lays shelled eggs, dry scales; (B) lays jelly eggs in pond, smooth moist skin; (C) feathery wings, warm-blooded; (D) segmented body, 6 legs, wings. Which single YES/NO question splits them cleanly into 2 vertebrates vs. 2 invertebrates? Wait—how many of A, B, C, D are vertebrates?",
            "صنّف علماء أربعة حيوانات برية: (A) يبيض بقشرة صلبة وله حراشف جافة، (B) يبيض في البركة وله جلد أملس رطب، (C) له أجنحة بريش ودم حار، (D) جسمه مقسم وله 6 أرجل وأجنحة. كم عدد الفقاريات من بين الحيوانات الأربعة؟",
            [
                ("3 vertebrates (A reptile, B amphibian, C bird) and 1 invertebrate (D insect)", "3 فقاريات (A زاحف، B برمائي، C طائر) ولافقاري واحد (D حشرة)"),
                ("2 vertebrates (A and C) and 2 invertebrates (B and D)", "فقاريان (A و C) ولافقاريان (B و D)"),
                ("4 vertebrates because all four animals can walk or fly on land", "4 فقاريات لأن جميعها يعيش على اليابسة"),
                ("1 vertebrate (C only) and 3 invertebrates (A, B, and D)", "فقاري واحد (C فقط) و3 لافقاريات (A و B و D)"),
            ],
            "Identify the class of A, B, C, and D first, then check which classes belong to Phylum Chordata (Vertebrates).",
            "حدد طائفة كل حيوان أولاً، ثم احسب كم منها يتبع طوائف الفقاريات الخمس.",
            "Vertebrates consist of Fish, Amphibians, Reptiles, Birds, and Mammals.",
            ["A = Reptile (vertebrate), B = Amphibian (vertebrate), C = Bird (vertebrate).", "D = 6-legged Insect (Arthropod invertebrate). Total = 3 vertebrates and 1 invertebrate."],
            "Both C (bird) and D (insect) have wings, yet only C has a backbone.",
            "تشمل الفقاريات الأسماك والبرمائيات والزواحف والطيور والثدييات.",
            ["الحيوان A زاحف، و B برمائي، و C طائر ← ثلاثتها فقاريات.", "أما D فله 6 أرجل وجسم مقسم ← حشرة (مفصليات لافقارية)."],
            "إذن يوجد 3 فقاريات ولافقاري واحد فقط رغم وجود أجنحة لدى C و D.",
            svg_data_table(["Animal", "Traits", "Backbone?"], [["A", "Dry scales, land eggs", "Yes"], ["B", "Moist skin, pond eggs", "Yes"], ["C", "Feathers, warm", "Yes"], ["D", "6 legs, segmented", "No"]], "4-Animal Key Check", [74, 158, 92]),
            svg_data_table(["الحيوان", "السمات", "فقاري؟"], [["A", "حراشف جافة، بيض يابس", "نعم"], ["B", "جلد رطب، بيض بالماء", "نعم"], ["C", "ريش، دم حار", "نعم"], ["D", "6 أرجل، مقسم", "لا"]], "تحليل مفتاح التصنيف", [74, 158, 92]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b02:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b03(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B03"
    # Easy (0..4): Photosynthesis inputs/outputs, chlorophyll, stomata, xylem/phloem
    easy_b03 = [
        (
            "Which balanced word summary accurately describes the process of photosynthesis inside a green plant leaf?",
            "أي معادلة لفظية تصف بدقة نواتج ومتفاعلات عملية البناء الضوئي داخل ورقة النبات الخضراء؟",
            [
                ("Carbon dioxide + Water + Light energy → Glucose + Oxygen", "ثاني أكسيد الكربون + ماء + طاقة ضوئية ← جلوكوز + أكسجين"),
                ("Glucose + Oxygen → Carbon dioxide + Water + Heat", "جلوكوز + أكسجين ← ثاني أكسيد الكربون + ماء + حرارة"),
                ("Nitrogen + Soil minerals → Chlorophyll + Carbon dioxide", "نيتروجين + أملاح التربة ← كلوروفيل + ثاني أكسيد الكربون"),
                ("Oxygen + Water + Darkness → Starch + Nitrogen", "أكسجين + ماء + ظلام ← نشا + نيتروجين"),
            ],
            "Plants take in CO₂ from air and H₂O from soil to build sugar and release O₂.",
            "يمتص النبات ثاني أكسيد الكربون من الهواء والماء من التربة ليصنع السكر ويطلق الأكسجين.",
            "Photosynthesis converts inorganic CO₂ and H₂O into chemical sugar and O₂.",
            ["Inputs (reactants): carbon dioxide (through stomata) and water (from roots) powered by sunlight.", "Outputs (products): glucose sugar (stored/used as food) and oxygen gas released to air."],
            "Notice cellular respiration runs in the reverse chemical direction.",
            "تحوّل عملية البناء الضوئي غاز ثاني أكسيد الكربون والماء إلى سكر وأكسجين بمساعدة الضوء.",
            ["المدخلات: ثاني أكسيد الكربون عبر الثغور والماء من الجذور بوجود الضوء.", "المخرجات: سكر الجلوكوز كغذاء للنبات وغاز الأكسجين المنطلق للهواء."],
            "وهي عكس معادلة التنفس الخلوي.",
            svg_process_flow(["CO2 + H2O", "Sunlight", "Chloroplast", "Glucose + O2"], "Photosynthesis Pathway", "Photosynthesis Summary"),
            svg_process_flow(["CO2 + ماء", "ضوء الشمس", "البلاستيدة", "جلوكوز + O2"], "مسار البناء الضوئي", "ملخص البناء الضوئي"),
        ),
        (
            "Tiny microscopic pores on the underside of plant leaves open and close to let carbon dioxide enter and oxygen and water vapor exit. What are these pores called?",
            "فتحات مجهرية دقيقة على السطح السفلي لأوراق النبات تُفتح وتُغلق لتسمح بدخول ثاني أكسيد الكربون وخروج الأكسجين وبخار الماء. ما اسم هذه الفتحات؟",
            [
                ("Stomata", "الثغور"),
                ("Xylem vessels", "أوعية الخشب"),
                ("Root hairs", "الشعيرات الجذرية"),
                ("Mitochondria", "الميتوكوندريا"),
            ],
            "Each pore is flanked by two kidney-shaped guard cells.",
            "تحيط بكل فتحة خليتان حارستان تتحكمان في فتحها وإغلاقها.",
            "Stomata regulate leaf gas exchange and transpiration.",
            ["Guard cells swell to open stomata during daylight for CO₂ intake.", "They close during severe heat or drought to prevent excessive water loss."],
            "Xylem carries liquid water; stomata exchange gases.",
            "الثغور هي بوابات تبادل الغازات في الورقة.",
            ["تفتح الخلايا الحارسة الثغور نهاراً لإدخال غاز ثاني أكسيد الكربون.", "وتغلقها عند الجفاف الشديد لتقليل فقدان الماء عبر النتح."],
            "أما الخشب فينقل الماء السائل داخل الساق.",
            None, None,
        ),
        (
            "Which vascular tissue in a date palm trunk carries water and dissolved minerals upward from the roots to the fronds?",
            "أي نسيج وعائي في جذع النخلة ينقل الماء والأملاح المعدنية الذائبة من الجذور إلى أعلى نحو السعف؟",
            [
                ("Xylem", "الخشب"),
                ("Phloem", "اللحاء"),
                ("Guard cells", "الخلايا الحارسة"),
                ("Cuticle", "الطبقة الشمعية"),
            ],
            "Remember: Phloem carries 'phood' (sugars) all around; the other tube lifts water UP from soil.",
            "اللحاء ينقل الغذاء الجاهز؛ أما النسيج الآخر فيرفع الماء والأملاح للأعلى.",
            "Xylem transports water and soil minerals upward; phloem transports dissolved sugars.",
            ["Root hairs absorb water from soil and pass it into xylem vessels.", "Water moves upward to leaf chloroplasts for photosynthesis and transpiration."],
            "Phloem distributes glucose made in leaves down to roots and fruits.",
            "ينقل نسيج الخشب الماء والأملاح صعوداً من الجذور إلى الأوراق.",
            ["يمتص الجذر الماء من التربة ويدفعه عبر أنابيب الخشب للأعلى.", "بينما يوزع اللحاء السكر المصنوع في الأوراق إلى باقي أجزاء النبات."],
            "لكل نسيج وعائي اتجاه ووظيفة محددة.",
            svg_process_flow(["Root Hairs", "Xylem Tubes", "Leaf Vein", "Stomata"], "Water Transport Upward", "Plant Water Pathway"),
            svg_process_flow(["شعيرات جذرية", "أوعية الخشب", "عروق الورقة", "الثغور"], "نقل الماء للأعلى", "مسار الماء في النبات"),
        ),
        (
            "Why do most leaves appear green to the human eye?",
            "لماذا تبدو معظم أوراق النباتات باللون الأخضر للعين البشرية؟",
            [
                ("Chlorophyll absorbs red and blue light wavelengths and reflects green light", "لأن الكلوروفيل يمتص الأطوال الموجية الحمراء والزرقاء ويعكس الضوء الأخضر"),
                ("Plant leaves emit green fluorescence from inside mitochondria", "لأن أوراق النبات تصدر توهجاً أخضر من الميتوكوندريا"),
                ("Stomata trap only green-colored dust particles from air", "لأن الثغور تحبس ذرات الغبار الخضراء فقط من الهواء"),
                ("Water inside xylem tubes naturally turns bright green in air", "لأن الماء داخل أوعية الخشب يتحول للون الأخضر في الهواء"),
            ],
            "An object appears the color of the light waves it reflects rather than absorbs.",
            "يظهر الجسم باللون الذي يعكسه إلى أعيننا لا باللون الذي يمتصه.",
            "Chlorophyll pigments reflect green wavelengths while absorbing red and blue light for energy.",
            ["Sunlight contains all colors of the visible spectrum.", "Chlorophyll strongly absorbs red and blue light to power photosynthesis and reflects green wavelengths back to our eyes."],
            "Therefore, green light alone gives plants the slowest photosynthesis rate!",
            "نرى الأجسام بألوان الضوء التي تعكسها.",
            ["يمتص الكلوروفيل الضوء الأحمر والأزرق لإتمام البناء الضوئي.", "ويعكس الجزء الأخضر من الطيف فتظهر الأوراق خضراء لأعيننا."],
            "لهذا يقل البناء الضوئي لو أُضيء النبات بضوء أخضر فقط.",
            None, None,
        ),
        (
            "Which gas bubbles off the cut stem of an aquatic Elodea water plant when placed in bright sunlight?",
            "ما الغاز الذي يتصاعد على شكل فقاعات من ساق نبات مائي (إيلوديا) مقطوع عند وضعه في ضوء الشمس الساطع؟",
            [
                ("Oxygen (O₂)", "غاز الأكسجين (O₂)"),
                ("Carbon dioxide (CO₂)", "غاز ثاني أكسيد الكربون (CO₂)"),
                ("Nitrogen (N₂)", "غاز النيتروجين (N₂)"),
                ("Methane (CH₄)", "غاز الميثان (CH₄)"),
            ],
            "Light drives photosynthesis, which releases a vital gas needed by aquatic fish.",
            "يدفع الضوء عملية البناء الضوئي التي تطلق الغاز اللازم لتنفس الأسماك.",
            "Bright light triggers photosynthesis, releasing O₂ gas bubbles in water.",
            ["The submerged Elodea takes in dissolved CO₂ and water.", "Using light energy, it releases pure oxygen bubbles from the cut stem."],
            "Moving the lamp closer increases the bubble rate up to a maximum limit.",
            "ينطلق غاز الأكسجين كمنتج ثانوي لعملية البناء الضوئي.",
            ["يمتص النبات المائي ثاني أكسيد الكربون الذائب والماء.", "وبمساعدة الضوء ينتج الجلوكوز وتتصاعد فقاعات غاز الأكسجين."],
            "زيادة شدة الإضاءة تزيد معدل هذه الفقاعات حتى حد معين.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b03:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Stomata desert adaptation, respiration vs photosynthesis, experiment applications
    med_b03 = [
        (
            "On a scorching 46°C afternoon in Riyadh, a desert shrub closes most of its leaf stomata. What trade-off does the shrub immediately experience?",
            "في ظهيرة حارة تصل فيها الحرارة إلى 46°م في الرياض، تُغلق شجيرة صحراوية معظم ثغور أوراقها. ما الموازنة التي تحدث للشجيرة مباشرة؟",
            [
                ("It conserves water by slowing transpiration, but photosynthesis slows down because less CO₂ enters", "تحافظ على الماء بإبطاء النتح، لكن البناء الضوئي يتباطأ لقلة دخول ثاني أكسيد الكربون"),
                ("It absorbs extra CO₂ rapidly while evaporating twice as much water", "تمتص كمية مضاعفة من ثاني أكسيد الكربون مع مضاعفة فقدان الماء"),
                ("Its chloroplasts convert stored nitrogen directly into liquid water", "تحول البلاستيدات النيتروجين المخزن مباشرة إلى ماء سائل"),
                ("Its xylem tubes begin pumping sugars downward into the soil", "تبدأ أوعية الخشب بضخ السكر للأسفل نحو التربة"),
            ],
            "Closing a door keeps cool air/water inside, but also blocks needed gas deliveries from entering.",
            "إغلاق النوافذ يحفظ الرطوبة بالداخل، لكنه يقلل أيضاً دخول الغاز اللازم لصنع الغذاء.",
            "Closing stomata saves water at the cost of reduced CO₂ uptake.",
            ["Open stomata allow both water vapor exit (transpiration) and CO₂ entry.", "Closing stomata protects the desert plant from dehydration, temporarily lowering glucose synthesis."],
            "Desert plants open stomata mainly during cooler dawn or night hours.",
            "إغلاق الثغور يحمي النبات من الجفاف مع تقليل دخول الغاز.",
            ["تقلل الثغور المغلقة تبخر الماء (النتح) في الحر الشديد.", "لكنها تحد في الوقت نفسه من دخول غاز ثاني أكسيد الكربون اللازم للبناء الضوئي."],
            "لذلك تفتح بعض النباتات الصحراوية ثغورها ليلاً أو عند الفجر.",
            None, None,
        ),
        (
            "Do green plants perform cellular respiration, and when does it happen?",
            "هل تقوم النباتات الخضراء بعملية التنفس الخلوي، ومتى تحدث هذه العملية؟",
            [
                ("Yes, continuously day and night inside plant mitochondria to release energy for growth and transport", "نعم، باستمرار ليلاً ونهاراً داخل الميتوكوندريا لتحرير الطاقة اللازمة للنمو والنقل"),
                ("No, plants only perform photosynthesis and never use oxygen", "لا، تقوم النباتات بالبناء الضوئي فقط ولا تستهلك الأكسجين أبداً"),
                ("Yes, but only during winter months when leaves drop off", "نعم، ولكن في فصل الشتاء فقط عند تساقط الأوراق"),
                ("Only in underground roots while leaves strictly avoid respiration", "تحدث في الجذور فقط بينما تمتنع الأوراق تماماً عن التنفس"),
            ],
            "Living plant cells need usable energy 24 hours a day, even in the dark!",
            "تحتاج خلايا النبات الحية إلى طاقة مستمرة على مدار 24 ساعة حتى في الظلام!",
            "Plants carry out photosynthesis only in light, but cellular respiration continuously.",
            ["During daylight, photosynthesis produces more O₂ than respiration consumes.", "At night, photosynthesis pauses while mitochondria continue cellular respiration 24/7."],
            "Plants possess BOTH chloroplasts and mitochondria!",
            "تحتاج جميع الخلايا الحية بما فيها النباتية إلى طاقة مستمرة بالتنفس الخلوي.",
            ["البناء الضوئي يحدث بوجود الضوء فقط، أما التنفس الخلوي فيستمر ليلاً ونهاراً.", "تحرق الميتوكوندريا جزءاً من الجلوكوز المصنوع لتوفير الطاقة لنمو النبات."],
            "تمتلك الخلية النباتية بلاستيدات وميتوكوندريا معاً.",
            None, None,
        ),
        (
            "A student covers half of a green geranium leaf with black aluminum foil, leaves the plant in sunlight for 6 hours, boils the leaf in alcohol to remove green pigment, and adds brown iodine solution (which turns dark blue-black where starch is present). What will the leaf look like?",
            "غطى طالب نصف ورقة إبرة الراعي بورق ألمنيوم أسود، وترك النبات في الشمس 6 ساعات، ثم أزال اللون الأخضر بالكحول وأضاف محلول اليود البني (الذي يتحول إلى أزرق مسودّ بوجود النشا). كيف ستبدو الورقة؟",
            [
                ("The uncovered half turns dark blue-black; the foil-covered half stays yellowish-brown", "يتحول النصف المكشوف إلى أزرق مسودّ، ويبقى النصف المغطى بنياً مصفراً"),
                ("The foil-covered half turns dark blue-black because foil traps starch", "يتحول النصف المغطى إلى أزرق مسودّ لأن الألمنيوم يحبس النشا"),
                ("Both halves stay pure white because boiling destroys all leaf cells", "يبقى النصفان بلون أبيض لأن الغلي يدمر جميع الخلايا"),
                ("Both halves turn blue-black equally because sunlight passed through foil", "يتحول النصفان إلى أزرق مسودّ بالتساوي"),
            ],
            "Starch forms from glucose made during photosynthesis, which requires light.",
            "يتكوّن النشا من الجلوكوز الناتج عن البناء الضوئي الذي يتطلب ضوء الشمس.",
            "Only illuminated leaf areas produce glucose and store starch.",
            ["The uncovered half received sunlight, performed photosynthesis, and stored starch → iodine turns blue-black.", "The covered half received zero light, made no new glucose, and tests negative for starch."],
            "Covering half the same leaf acts as a built-in controlled comparison.",
            "يتكوّن النشا في الأجزاء المعرضة للضوء فقط.",
            ["صنع الجزء المكشوف الجلوكوز وخزنه كنشا فتفاعل مع اليود وأعطى لوناً أزرق مسودّاً.", "حُجب الضوء عن الجزء المغطى فلم يصنع نشا وبقي لون اليود بنياً."],
            "تثبت التجربة ضرورة الضوء لتكوين الغذاء في الورقة.",
            svg_data_table(["Leaf Half", "Light?", "Iodine Result"], [["Uncovered", "Yes", "Blue-Black"], ["Foil-covered", "No", "Yellow-Brown"]], "Starch Test Setup", [110, 82, 128]),
            svg_data_table(["نصف الورقة", "ضوء؟", "نتيجة اليود"], [["مكشوف", "نعم", "أزرق مسودّ"], ["مغطى", "لا", "بني مصفر"]], "اختبار النشا باليود", [104, 80, 132]),
        ),
        (
            "A sealed glass jar holds a healthy green mint plant and a glowing candle in dark shade. Why does the candle go out much sooner in the dark than if the jar were placed in bright sunlight?",
            "يحتوي برطمان زجاجي محكم الإغلاق على نبات نعناع سليم وشمعة مشتعلة في مكان مظلم. لماذا تنطفئ الشمعة في الظلام أسرع بكثير مقارنة بوضع البرطمان في شمس ساطعة؟",
            [
                ("In the dark, the plant only consumes O₂ for respiration instead of producing extra O₂ by photosynthesis", "في الظلام يستهلك النبات الأكسجين للتنفس ولا ينتج أكسجيناً بالبناء الضوئي"),
                ("In the dark, plant roots absorb wax vapor directly from the candle", "في الظلام تمتص الجذور بخار الشمع مباشرة"),
                ("Sunlight heats glass so carbon dioxide turns spontaneously into oxygen gas", "تسخن الشمس الزجاج فيتحول ثاني أكسيد الكربون تلقائياً لأكسجين"),
                ("In darkness, leaves release pure liquid nitrogen that extinguishes flames", "في الظلام تطلق الأوراق نيتروجيناً سائلاً يطفئ اللهب"),
            ],
            "Compare gas output of a plant in sunlight vs. in darkness.",
            "قارن بين الغازات التي يطلقها النبات في الشمس وفي الظلام.",
            "In darkness, both the plant and the flame consume O₂ and release CO₂.",
            ["Burning requires oxygen gas (O₂).", "In sunlight, photosynthesis supplies fresh O₂; in the dark, photosynthesis stops while plant respiration also uses O₂."],
            "This classic Priestley-style jar demonstrates plant-atmosphere gas exchange.",
            "يتوقف إنتاج الأكسجين في الظلام بينما يستمر استهلاكه في التنفس والاحتراق.",
            ["تحتاج الشمعة إلى الأكسجين لتبقى مشتعلة.", "في الشمس يعوّض البناء الضوئي الأكسجين، أما في الظلام فيستهلكه كلٌّ من الشمعة وتنفس النبات معاً."],
            "يوضح ذلك تكامل الغازات بين النبات والبيئة.",
            None, None,
        ),
        (
            "A student coats the underside of 5 leaves on Plant A with thick petroleum jelly (Vaseline) while leaving Plant B untreated under the same sunny window. After one week, Plant A looks stunted and yellow. Why?",
            "دهن طالب السطح السفلي لخمس أوراق في النبات A بطبقة سميكة من الفازلين وترك النبات B دون دهن عند النافذة نفسها. بعد أسبوع بدا النبات A ضعيف النمو ومصفراً. ما السبب؟",
            [
                ("The jelly clogged the underside stomata, blocking CO₂ entry needed to make glucose", "سدّ الفازلين الثغور في السطح السفلي فمنع دخول ثاني أكسيد الكربون اللازم لصنع الغذاء"),
                ("Petroleum jelly blocked xylem tubes inside the wooden stem", "سدّ الفازلين أوعية الخشب داخل الساق الخشبية"),
                ("Plant roots refused to absorb water because leaves became shiny", "امتنعت الجذور عن امتصاص الماء لأن الأوراق صارت لامعة"),
                ("Vaseline absorbed all chlorophyll molecules out of the top leaf surface", "امتص الفازلين جزيئات الكلوروفيل من السطح العلوي للورقة"),
            ],
            "Where are most leaf stomata located, and which gas must enter through them?",
            "أين تتركز معظم الثغور في الأوراق، وأي غاز يدخل عبرها؟",
            "Blocking stomata starves chloroplasts of carbon dioxide.",
            ["Most stomata lie on the cooler underside of leaves to limit evaporation.", "Clogging them prevents CO₂ diffusion into leaf cells, halting photosynthesis and growth."],
            "Plant B serves as the untreated control group.",
            "إغلاق الثغور السفلية يمنع تبادل الغازات اللازمة للبناء الضوئي.",
            ["تتركز معظم الثغور على السطح السفلي للورقة.", "سددها بالفازلين منع دخول غاز ثاني أكسيد الكربون فتوقف صنع الغذاء وضعف النبات."],
            "يمثل النبات B المجموعة الضابطة للمقارنة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b03:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Graph reasoning & experimental photosynthesis analysis
    g_pts = [(10, 40), (20, 80), (30, 120), (40, 120), (50, 120)]
    B.add_concept(
        tp, "Hard", bp,
        "A student varies light intensity on an aquatic plant while keeping water temperature (24°C) and CO₂ supply constant, recording O₂ bubbles/min in the graph. Why does the curve flatten at 120 bubbles/min above 30% light intensity?",
        "غيّر طالب شدة الإضاءة على نبات مائي مع تثبيت درجة الحرارة (24°م) وتركيز CO₂، وسجل عدد فقاعات الأكسجين في الدقيقة كما في الرسم البياني. لماذا يثبت المنحنى عند 120 فقاعة/دقيقة بعد شدة إضاءة 30%؟",
        [
            ("Another factor such as CO₂ concentration or enzyme speed becomes the limiting factor", "لأن عاملاً آخر مثل تركيز ثاني أكسيد الكربون أو سرعة الإنزيمات أصبح هو العامل المحدد"),
            ("Chlorophyll turns into mitochondria once light reaches 30%", "لأن الكلوروفيل يتحول إلى ميتوكوندريا عند شدة إضاءة 30%"),
            ("The plant runs out of oxygen molecules inside the glass beaker", "لأن النبات استنفد جميع جزيئات الأكسجين داخل الكأس"),
            ("Water stops dissolving carbon dioxide whenever bulbs shine above 30%", "لأن الماء يتوقف عن إذابة ثاني أكسيد الكربون فوق 30% إضاءة"),
        ],
        "Adding more of one ingredient cannot speed up a factory if a second ingredient is already running at maximum capacity.",
        "زيادة أحد المدخلات لا ترفع الإنتاج إذا كان مُدخل آخر مثل CO₂ قد وصل لحده الأقصى.",
        "A plateau on a rate graph signals a different limiting factor.",
        ["From 10% to 30% light, light intensity limits the rate (bubble count climbs linearly).", "Above 30%, light is abundant, so fixed CO₂ availability or temperature caps the maximum rate at 120 bubbles/min."],
        "Adding baking soda (extra CO₂) would raise the plateau higher.",
        "ثبات معدل التفاعل رغم زيادة الإضاءة يدل على وجود عامل محدد آخر.",
        ["بين 10% و30% كانت الإضاءة هي العامل المحدد فارتفع عدد الفقاعات طردياً.", "بعد 30% توافر الضوء بوفرة فأصبح تركيز CO₂ الثابت أو الحرارة هو العامل المحدد للسرعة."],
        "إضافة مصدر لزيادة CO₂ سترفع السقف الأعلى للفقاعات.",
        svg_motion_graph(g_pts, "O2/min", "Light (%)", "Photosynthesis Rate"),
        svg_motion_graph(g_pts, "فقاعة/د", "الإضاءة (%)", "معدل البناء الضوئي"),
    )

    hard_b03 = [
        (
            "An Elodea sprig produces 18 O₂ bubbles in 3 minutes when a lamp is 20 cm away. Keeping CO₂ and temperature fixed, the student moves the lamp to 10 cm and counts 24 bubbles in 1 minute. By how many bubbles per minute did the rate increase?",
            "أنتج غصن نبات مائي 18 فقاعة أكسجين خلال 3 دقائق عندما كان المصباح على بُعد 20 سم. وعند تقريب المصباح إلى 10 سم، عدّ الطالب 24 فقاعة في دقيقة واحدة. بكم فقاعة/دقيقة زاد معدل الإنتاج؟",
            18, [6, 12, 20],
            "Convert both measurements to bubbles per 1 minute first, then subtract.",
            "احسب معدل الفقاعات في الدقيقة الواحدة لكلتا الحالتين أولاً ثم اطرح.",
            "Compare rates per unit time (bubbles/min).",
            ["At 20 cm: rate = 18 ÷ 3 = 6 bubbles/min.", "At 10 cm: rate = 24 bubbles/min. Increase = 24 - 6 = 18 bubbles/min."],
            "Closer lamp gives stronger light intensity (4× intensity), sharply boosting rate.",
            "نوحد الزمن إلى دقيقة واحدة للمقارنة ثم نحسب مقدار الزيادة.",
            ["المعدل عند 20 سم = 18 ÷ 3 = 6 فقاعات/دقيقة.", "المعدل عند 10 سم = 24 فقاعة/دقيقة، والزيادة = 24 − 6 = 18 فقاعة/دقيقة."],
            "6 + 18 = 24 فقاعة/دقيقة.",
            None, None,
        ),
    ]
    for qen, qar, ans, dists, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b03:
        B.add_math(tp, "Hard", bp, qen, qar, ans, dists, hen, har, ien, sen, cen, iar, sar, car, "", den, dar)

    hard_b03_c = [
        (
            "Four identical aquatic plants are placed in tubes with BTB indicator (yellow when rich in CO₂, blue when CO₂ is low/removed). Tube 1 (plant + light), Tube 2 (plant + foil dark), Tube 3 (snail + light), Tube 4 (plant + snail + light). Which tube turns brightest BLUE after 4 hours, and which turns YELLOW?",
            "وُضعت أربعة أنابيب تحتوي كاشف BTB (يتحول للأصفر مع كثرة CO₂ وللأزرق عند نقص CO₂): أنبوب 1 (نبات + ضوء)، أنبوب 2 (نبات + ظلام)، أنبوب 3 (حلزون + ضوء)، أنبوب 4 (نبات + حلزون + ضوء). أي أنبوب يتحول إلى أزرق ساطع، وأيها إلى أصفر قوي بعد 4 ساعات؟",
            [
                ("Tube 1 turns brightest BLUE (removes CO₂); Tube 2 & Tube 3 turn YELLOW (add CO₂)", "الأنبوب 1 أزرق ساطع (يسحب CO₂)، والأنبوبان 2 و 3 أصفران (يطلقان CO₂)"),
                ("Tube 2 turns BLUE; Tube 1 turns YELLOW because photosynthesis makes CO₂", "الأنبوب 2 أزرق، والأنبوب 1 أصفر لأن البناء الضوئي ينتج CO₂"),
                ("Tube 3 turns brightest BLUE because snails inhale nitrogen and exhale oxygen", "الأنبوب 3 أزرق ساطع لأن الحلزون ينتج أكسجيناً"),
                ("All four tubes stay completely green regardless of light or organisms", "تبقى جميع الأنابيب خضراء تماماً دون تغير"),
            ],
            "Photosynthesis REMOVES CO₂ from water; respiration (by snails or plants in dark) ADDS CO₂.",
            "يسحب البناء الضوئي CO₂ من الماء، بينما يضيف التنفس (حلزون أو نبات في الظلام) CO₂ للماء.",
            "Net CO₂ removal turns BTB blue; net CO₂ release turns BTB yellow.",
            ["Tube 1 has photosynthesis removing CO₂ without a snail → lowest CO₂ → brightest blue.", "Tube 2 (dark plant respiring) and Tube 3 (snail respiring) both release CO₂ → yellow."],
            "Tube 4 balances snail respiration with plant photosynthesis, staying near green/blue.",
            "يعكس لون الكاشف تغير تركيز ثاني أكسيد الكربون في كل أنبوب.",
            ["الأنبوب 1 يستهلك CO₂ بالبناء الضوئي في الضوء دون حيوان متنفّس ← أقل تركيز CO₂ ← أزرق.", "الأنبوبان 2 (نبات بالظلام) و3 (حلزون) يطلقان CO₂ بالتنفس ← أصفر."],
            "يتكامل تنفس الحلزون وبناء النبات في الأنبوب 4.",
            svg_data_table(["Tube", "Contents", "Light?"], [["1", "Plant", "Yes"], ["2", "Plant", "No"], ["3", "Snail", "Yes"], ["4", "Plant+Snail", "Yes"]], "BTB Gas Experiment", [64, 150, 92]),
            svg_data_table(["الأنبوب", "المحتوى", "ضوء؟"], [["1", "نبات فقط", "نعم"], ["2", "نبات فقط", "لا"], ["3", "حلزون فقط", "نعم"], ["4", "نبات+حلزون", "نعم"]], "تجربة كاشف BTB", [68, 146, 92]),
        ),
        (
            "A farmer waters two identical tomato plots equally, but adds a compound that blocks root hair respiration (starving root cells of ATP energy). Soon, mineral levels inside the tomato leaves drop sharply even though the soil is rich in minerals. Why?",
            "سقى مزارع حوضي طماطم متماثلين، لكنه أضاف للحوض الثاني مادة تعيق التنفس الخلوي في الشعيرات الجذرية. سرعان ما انخفضت الأملاح المعدنية في أوراق الحوض الثاني رغم غنى التربة بها. ما التفسير؟",
            [
                ("Root hairs require ATP energy from cellular respiration to actively pump scarce soil minerals inward", "تحتاج الشعيرات الجذرية إلى طاقة من التنفس الخلوي لضخ الأملاح المعدنية من التربة عبر النقل النشط"),
                ("Roots perform photosynthesis to manufacture mineral salts from sunlight", "تصنع الجذور الأملاح المعدنية بعملية البناء الضوئي"),
                ("Minerals evaporate out through stomata whenever roots stop breathing", "تتبخر الأملاح من الثغور عند توقف تنفس الجذور"),
                ("Xylem tubes dissolve when soil contains dissolved nitrogen", "تذوب أوعية الخشب عند وجود النيتروجين في التربة"),
            ],
            "Water enters by passive osmosis, but many mineral ions require active transport powered by mitochondria.",
            "يدخل الماء بالأسموزية، لكن كثيراً من الأملاح تحتاج لطاقة الميتوكوندريا لنقلها ضد التدرج.",
            "Active mineral uptake by roots depends on cellular respiration in root cells.",
            ["Mineral concentration inside root cells is often higher than in soil water.", "Pumping minerals uphill against concentration gradients consumes ATP made by root mitochondria."],
            "Waterlogged soil lacking air pockets also suffocates roots for this same reason!",
            "يعتمد امتصاص الأملاح في الجذور على الطاقة الخلوية.",
            ["غالباً ما يكون تركيز الأملاح داخل خلايا الجذر أعلى منه في ماء التربة.", "لذلك تحتاج الشعيرات الجذرية إلى طاقة ATP من الميتوكوندريا لضخ الأملاح للداخل."],
            "غمر التربة بالماء الزائد يخنق الجذور للسبب ذاته.",
            None, None,
        ),
        (
            "Two identical potted basil plants are tested: Pot A receives red+blue LED light; Pot B receives strictly green LED light of the same brightness. After 14 days, Pot A gained 14 g in dry mass while Pot B lost 1 g. Why did Pot B lose mass?",
            "وُضع نباتا ريحان متماثلان تحت إضاءة متساوية الشدة: الحوض A تحت ضوء أحمر وأزرق، والحوض B تحت ضوء أخضر فقط. بعد 14 يوماً زادت الكتلة الجافة للنبات A بمقدار 14 جم، بينما فقد النبات B 1 جم. لماذا خسر النبات B كتلة؟",
            [
                ("Chlorophyll reflects green light rather than absorbing it, so Pot B consumed its stored food via respiration faster than it made sugar", "يعكس الكلوروفيل الضوء الأخضر ولا يمتصه، فاستهلك النبات B غذاءه المخزن بالتنفس أسرع من إنتاجه للسكر"),
                ("Green light destroys plant cell walls and turns xylem into bark", "يدمّر الضوء الأخضر جدران الخلايا ويحول الخشب إلى لحاء"),
                ("Red and blue light directly convert into solid soil inside Pot A", "يتحول الضوء الأحمر والأزرق مباشرة إلى تربة صلبة في الحوض A"),
                ("Plants under green light stop cellular respiration and exhale solid glucose", "تتوقف النباتات تحت الضوء الأخضر عن التنفس وتطرد الجلوكوز الصلب"),
            ],
            "Connect chlorophyll light reflection to the balance between photosynthesis gain and respiration loss.",
            "اربط بين انعكاس الضوء الأخضر وتوازن البناء الضوئي مع التنفس الخلوي.",
            "Photosynthesis stalls in green light while respiration continues consuming biomass.",
            ["Chlorophyll absorbs red and blue photons strongly (Pot A gains +14 g biomass).", "Under green light, almost all light reflects away, so Pot B burns stored carbohydrate via respiration (-1 g)."],
            "Green light is the least effective spectrum color for plant growth.",
            "لا يستفيد الكلوروفيل من الضوء الأخضر الذي يعكسه، بينما يستمر استهلاك الغذاء.",
            ["يمتص الكلوروفيل الضوء الأحمر والأزرق بكفاءة فينمو الحوض A.", "تحت الضوء الأخضر ينعكس معظم الضوء فيتوقف البناء الضوئي وتستمر الميتوكوندريا باستهلاك المخزون."],
            "لذلك ينمو النبات جيداً تحت الضوء الأبيض أو الأحمر والأزرق.",
            svg_bar_chart([("Red+Blue", 14, GREEN), ("Green LED", 0.5, ORANGE)], "Growth (g)", "LED Light Experiment"),
            svg_bar_chart([("أحمر+أزرق", 14, GREEN), ("أخضر فقط", 0.5, ORANGE)], "النمو (جم)", "تجربة ألوان الضوء"),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b03_c:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b04(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B04"
    # Easy (0..4): Organs and functions of digestive, respiratory, circulatory systems
    easy_b04 = [
        (
            "In which organ of the human digestive system does most chemical breakdown finish and digested nutrients pass through tiny finger-like villi into the bloodstream?",
            "في أي عضو من أعضاء الجهاز الهضمي يكتمل معظم الهضم الكيميائي وتُمتص العناصر الغذائية عبر الخملات إلى مجرى الدم؟",
            [
                ("Small intestine", "الأمعاء الدقيقة"),
                ("Esophagus", "المريء"),
                ("Stomach", "المعدة"),
                ("Large intestine", "الأمعاء الغليظة"),
            ],
            "Villi vastly increase surface area for nutrient absorption; water reabsorption occurs later in the colon.",
            "تزيد الخملات مساحة الامتصاص؛ بينما يُمتص ما تبقى من الماء في الأمعاء الغليظة.",
            "The small intestine completes chemical digestion and absorbs nutrients via villi.",
            ["Enzymes from the pancreas and small intestine break carbs, proteins, and fats into tiny molecules.", "Millions of folded villi absorb those nutrients into capillaries."],
            "Stomach mainly starts protein digestion; large intestine absorbs water.",
            "الأمعاء الدقيقة هي موقع الامتصاص الرئيس للغذاء المهضوم.",
            ["تكمل إنزيمات البنكرياس والأمعاء الدقيقة هضم النشويات والبروتينات والدهون.", "تمتص الخملات الدقيقة تلك المواد إلى الشعيرات الدموية."],
            "بينما تختص الأمعاء الغليظة بامتصاص الماء المتبقي.",
            svg_process_flow(["Mouth", "Stomach", "Small Int.", "Large Int."], "Digestive Pathway", "Human Digestive Tract"),
            svg_process_flow(["الفم", "المعدة", "الأمعاء الدقيقة", "الغليظة"], "مسار الهضم", "القناة الهضمية"),
        ),
        (
            "Inside the lungs, oxygen diffuses into tiny capillaries and carbon dioxide leaves the blood across ultra-thin, grape-like air sacs. What are these sacs called?",
            "داخل الرئتين، ينتقل الأكسجين إلى الشعيرات الدموية ويغادر ثاني أكسيد الكربون عبر أكياس هوائية رقيقة تشبه عناقيد العنب. ما اسم هذه الأكياس؟",
            [
                ("Alveoli", "الحويصلات الهوائية"),
                ("Trachea", "القصبة الهوائية"),
                ("Diaphragm", "الحجاب الحاجز"),
                ("Villi", "الخملات المعوية"),
            ],
            "Do not confuse intestinal nutrient folds (villi) with lung air sacs!",
            "لا تخلط بين خملات الأمعاء وأكياس الهواء الرقيقة في الرئتين!",
            "Alveoli are the microscopic gas-exchange sacs of the respiratory system.",
            ["Air travels down trachea → bronchi → bronchioles → alveoli.", "Each alveolus is one cell thick and wrapped in blood capillaries for rapid O₂/CO₂ diffusion."],
            "The diaphragm is the dome muscle beneath the lungs.",
            "الحويصلات الهوائية هي مكان تبادل الغازات في الرئتين.",
            ["يصل الهواء عبر القصبة والشعيبات الهوائية إلى الحويصلات.", "جدارها رقيق جداً ومحاط بشعيرات دموية لتبادل الأكسجين وثاني أكسيد الكربون."],
            "أما الحجاب الحاجز فهو العضلة التي تحرك الرئتين.",
            None, None,
        ),
        (
            "Which type of blood vessel carries blood AWAY from the heart under high pressure and therefore has thick, muscular, elastic walls?",
            "أي نوع من الأوعية الدموية ينقل الدم بعيداً عن القلب تحت ضغط مرتفع، ولذلك يمتلك جدراناً عضلية سميكة ومرنة؟",
            [
                ("Arteries", "الشرايين"),
                ("Veins", "الأوردة"),
                ("Capillaries", "الشعيرات الدموية"),
                ("Alveoli", "الحويصلات الهوائية"),
            ],
            "Remember 'A' for Arteries = Away from the heart.",
            "الشرايين تنطلق من القلب لتوزيع الدم بقوة، لذا جدرانها سميكة.",
            "Arteries transport high-pressure blood away from heart ventricles.",
            ["Thick elastic walls withstand each heartbeat surge without bursting.", "Veins return lower-pressure blood back to the heart using one-way valves."],
            "Capillaries are one-cell-thick vessels connecting arterioles and venules.",
            "الشرايين أوعية سميكة الجدار تنقل الدم بعيداً عن القلب.",
            ["يتحمل الجدار العضلي المرن ضغط الدم القوي القادم من البطينين.", "أما الأوردة فلها صمامات وجدران أرق لإعادة الدم إلى القلب."],
            "تتصل الشرايين والأوردة عبر الشعيرات الدموية الدقيقة.",
            None, None,
        ),
        (
            "Which component of human blood contains hemoglobin protein to bind and transport oxygen from the lungs to every body cell?",
            "أي مكون من مكونات الدم يحتوي على بروتين الهيموجلوبين ليرتبط بالأكسجين وينقله من الرئتين إلى خلايا الجسم؟",
            [
                ("Red blood cells", "خلايا الدم الحمراء"),
                ("White blood cells", "خلايا الدم البيضاء"),
                ("Platelets", "الصفائح الدموية"),
                ("Digestive enzymes", "الإنزيمات الهاضمة"),
            ],
            "White blood cells fight germs and platelets seal cuts; which cell carries oxygen?",
            "تقاوم الخلايا البيضاء الجراثيم وتجلّط الصفائح الدم؛ أيها يحمل الأكسجين؟",
            "Red blood cells transport O₂ via iron-rich hemoglobin.",
            ["Red blood cells lack a nucleus when mature to pack maximum hemoglobin.", "Their biconcave disc shape speeds up oxygen uptake in lung capillaries."],
            "Iron deficiency reduces hemoglobin, causing fatigue (anemia).",
            "تنقل خلايا الدم الحمراء الأكسجين بفضل احتوائها على الهيموجلوبين.",
            ["الهيموجلوبين بروتين غني بالحديد يرتبط بالأكسجين في الرئتين.", "وتحمله الخلايا الحمراء لتوزيعه على أنسجة الجسم."],
            "أما الخلايا البيضاء فللمناعة والصفائح لتخثر الدم.",
            None, None,
        ),
        (
            "What happens to the dome-shaped diaphragm muscle and rib cage when you take a deep breath IN (inhalation)?",
            "ماذا يحدث لعضلة الحجاب الحاجز والقفص الصدري عندما تأخذ نفساً عميقاً للداخل (الشهيق)؟",
            [
                ("The diaphragm contracts and flattens downward while the rib cage lifts outward, drawing air into the lungs", "ينقبض الحجاب الحاجز ويهبط للأسفل ويتسع القفص الصدري للخارج فينسحب الهواء إلى الرئتين"),
                ("The diaphragm relaxes upward while the ribs collapse inward to pull air inside", "يرتخي الحجاب الحاجز للأعلى وينكمش القفص الصدري لسحب الهواء"),
                ("The heart stops pumping temporarily so the trachea expands", "يتوقف القلب مؤقتاً لتتوسع القصبة الهوائية"),
                ("Lung alveoli push air outward into the nasal passage", "تدفع الحويصلات الهوائية الهواء للخارج نحو الأنف"),
            ],
            "Making the chest cavity larger drops air pressure inside the lungs, pulling outside air in.",
            "زيادة حجم التجويف الصدري تقلل الضغط داخل الرئتين فيندفع الهواء للداخل.",
            "Inhalation enlarges chest volume via diaphragm contraction.",
            ["When the diaphragm contracts, it flattens downward and increases chest volume.", "Lower internal air pressure pulls outside air down the trachea into the lungs."],
            "Exhalation reverses this: the diaphragm relaxes upward into a dome.",
            "يحدث الشهيق عند انقباض الحجاب الحاجز واتساع الصدر.",
            ["ينخفض الحجاب الحاجز للأسفل وترتفع الأضلاع للأعلى والخارج.", "يتسع حجم الرئتين ويقل الضغط بداخلهما فيدخل الهواء."],
            "أما الزفير فيحدث بارتخاء الحجاب الحاجز للأعلى.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b04:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Digestive enzymes, circulation path, vein valves, system coordination
    med_b04 = [
        (
            "Chewing a plain unsweetened cracker thoroughly for 45 seconds makes it start tasting slightly sweet. Why?",
            "مضغ قطعة بسكويت غير محلاة جيداً لمدة 45 ثانية يجعل طعمها يميل قليلاً للحلاوة. ما السبب العلمي؟",
            [
                ("Salivary enzymes (amylase) begin chemically breaking starch chains into simpler sugars in the mouth", "تبدأ إنزيمات اللعاب (الأميليز) في الفم بتفكيك النشا كيميائياً إلى سكريات بسيطة"),
                ("Taste buds convert salty minerals into pure glucose crystals", "تحول براعم التذوق الأملاح المعدنية إلى بلورات جلوكوز"),
                ("Stomach acid rises up the esophagus during normal chewing", "يصعد حمض المعدة عبر المريء أثناء المضغ الطبيعي"),
                ("Teeth add sugar molecules stored inside tooth enamel", "تضيف الأسنان جزيئات سكر مخزنة في طبقة المينا"),
            ],
            "Digestion begins in the mouth — both mechanically (teeth) and chemically (saliva)!",
            "يبدأ الهضم الميكانيكي والكيميائي معاً في الفم قبل البلع!",
            "Salivary amylase chemically digests complex starch into sweet simple sugars.",
            ["Teeth mechanically crush the cracker to increase surface area.", "Saliva contains amylase enzyme, which breaks long starch molecules into maltose sugars."],
            "Mechanical + chemical digestion start immediately in the oral cavity.",
            "يحتوي اللعاب على إنزيم يحول النشا إلى سكر بسيط.",
            ["تطحن الأسنان البسكويت ميكانيكياً لزيادة مساحة السطح.", "يفكك إنزيم الأميليز في اللعاب سلاسل النشا إلى سكريات حلوة المذاق."],
            "وهذا يثبت بدء الهضم الكيميائي في الفم.",
            None, None,
        ),
        (
            "Trace a drop of oxygen-poor blood returning from your leg muscles as it travels through the heart and lungs to pick up oxygen again:",
            "تتبّع مسار قطرة دم فقيرة بالأكسجين عائدة من عضلات الساق أثناء مرورها بالقلب والرئتين لتتزود بالأكسجين مجدداً:",
            [
                ("Veins → Right Heart → Lungs (alveoli) → Left Heart → Arteries to body", "الأوردة ← الجانب الأيمن من القلب ← الرئتان ← الجانب الأيسر من القلب ← الشرايين للجسم"),
                ("Arteries → Left Heart → Stomach → Right Heart → Lungs", "الشرايين ← الجانب الأيسر ← المعدة ← الجانب الأيمن ← الرئتان"),
                ("Veins → Left Heart → Kidneys → Right Heart → Brain", "الأوردة ← الجانب الأيسر ← الكليتان ← الجانب الأيمن ← الدماغ"),
                ("Capillaries → Liver → Right Heart → Left Heart without visiting lungs", "الشعيرات ← الكبد ← الجانب الأيمن ← الجانب الأيسر دون المرور بالرئتين"),
            ],
            "The right side of the heart pumps to the lungs; the left side pumps oxygenated blood out to the whole body.",
            "الجانب الأيمن من القلب يضخ للرئتين، والأيسر يضخ الدم المؤكسج لسائر الجسم.",
            "Double circulation separates oxygen-poor blood (right) from oxygen-rich blood (left).",
            ["Veins return deoxygenated blood from body tissues to the right atrium/ventricle.", "The right ventricle pumps it to lung capillaries to drop off CO₂ and pick up O₂, returning to the left side to pump through the aorta."],
            "Two separate loops prevent oxygenated and deoxygenated blood from mixing.",
            "تفصل الدورة الدموية المزدوجة الدم المؤكسج عن غير المؤكسج.",
            ["يعود الدم الفقير بالأكسجين عبر الأوردة إلى الجانب الأيمن من القلب ثم يذهب للرئتين.", "بعد التبادل الغازي يعود الدم الغني بالأكسجين للجانب الأيسر ليُضخ عبر الشرايين."],
            "يضمن هذا المسار تزويد جميع الخلايا بالأكسجين النقي.",
            svg_process_flow(["Right Heart", "Lung Alveoli", "Left Heart", "Body Cells"], "Double Blood Circulation", "Heart & Lungs Loop"),
            svg_process_flow(["الأيمن بالقلب", "الرئتان", "الأيسر بالقلب", "خلايا الجسم"], "الدورة الدموية المزدوجة", "مسار القلب والرئتين"),
        ),
        (
            "Why do veins in your arms and legs contain tiny one-way pocket valves, whereas arteries generally do not?",
            "لماذا تحتوي الأوردة في الذراعين والساقين على صمامات دقيقة أحادية الاتجاه، بينما تفتقر الشرايين عادةً إليها؟",
            [
                ("Blood in veins moves under low pressure against gravity, so valves prevent backward flow", "لأن الدم في الأوردة يسير بضغط منخفض وعكس الجاذبية أحياناً فتمنع الصمامات رجوعه للخلف"),
                ("Veins carry bright oxygen-rich blood directly out of the left ventricle", "لأن الأوردة تحمل دماً مؤكسجاً بضغط عالٍ من البطين الأيسر"),
                ("Valves in veins crush red blood cells into smaller oxygen molecules", "لأن الصمامات في الأوردة تطحن خلايا الدم الحمراء"),
                ("Arteries lack blood flow and only carry digestive bile from the liver", "لأن الشرايين لا تحمل دماً بل تنقل العصارة الصفراوية فقط"),
            ],
            "Compare pressure in arteries (pushed directly by heart beats) vs. pressure in veins returning from feet.",
            "قارن ضغط الدم المندفع من القلب في الشرايين بضغط الدم العائد ببطء من القدمين في الأوردة.",
            "One-way venous valves keep low-pressure blood flowing strictly toward the heart.",
            ["By the time blood passes through tiny capillaries into veins, blood pressure drops sharply.", "Skeletal muscles squeeze veins and one-way valves stop blood from pooling downward."],
            "Standing completely still for hours makes venous return harder.",
            "تحافظ صمامات الأوردة على اتجاه سريان الدم نحو القلب فقط.",
            ["ينخفض ضغط الدم بعد مروره بالشعيرات الدموية الدقيقة.", "لذا تمنع الصمامات ارتداد الدم للأسفل خاصة عند صعوده من الساقين نحو القلب."],
            "بينما يندفع الدم في الشرايين بضغط القلب المرتفع فلا يرتد.",
            None, None,
        ),
        (
            "What is the specific role of the large intestine (colon) compared with the small intestine after a meal?",
            "ما الوظيفة الرئيسة للأمعاء الغليظة مقارنة بالأمعاء الدقيقة بعد تناول وجبة غذائية؟",
            [
                ("The large intestine absorbs remaining water and electrolytes and forms solid waste, whereas the small intestine absorbs digested nutrients", "تمتص الأمعاء الغليظة الماء المتبقي والأملاح وتكوّن الفضلات، بينما تمتص الأمعاء الدقيقة الغذاء المهضوم"),
                ("The large intestine produces hydrochloric acid to dissolve proteins into chyme", "تفرز الأمعاء الغليظة حمض الهيدروكلوريك لهضم البروتينات"),
                ("The small intestine absorbs only liquid water and blocks all glucose", "تمتص الأمعاء الدقيقة الماء فقط وتمنع امتصاص الجلوكوز"),
                ("The large intestine pumps air bubbles into the bloodstream", "تضخ الأمعاء الغليظة فقاعات هواء داخل مجرى الدم"),
            ],
            "Think about why illness affecting the colon (diarrhea) rapidly causes dehydration!",
            "فكر لماذا تسبب اضطرابات القولون (الإسهال) جفافاً سريعاً في الجسم!",
            "Small intestine = nutrient absorption; Large intestine = water recovery.",
            ["Virtually all amino acids, simple sugars, and fatty acids enter blood/lymph in the small intestine.", "The leftover watery slurry enters the large intestine where water is reclaimed into the blood."],
            "Helpful gut bacteria in the large intestine also make vitamin K.",
            "تختص الأمعاء الدقيقة بامتصاص الغذاء المهضوم والغليظة باسترجاع الماء.",
            ["يمر معظم البروتين والسكريات والدهون المهضومة إلى الدم عبر خملات الأمعاء الدقيقة.", "تستخلص الأمعاء الغليظة الماء والأملاح من البقايا قبل طرحها."],
            "وتنتج بكتيريا الأمعاء الغليظة النافعة بعض الفيتامينات مثل فيتامين K.",
            None, None,
        ),
        (
            "Why does the inner stomach lining produce a thick layer of protective mucus alongside hydrochloric acid (HCl)?",
            "لماذا تفرز بطانة المعدة الداخلية طبقة سميكة من المخاط الواقي بالتزامن مع إفراز حمض الهيدروكلوريك القوي؟",
            [
                ("To protect the muscular stomach wall from being digested by its own strong acid and pepsin enzyme", "لحماية جدار المعدة العضلي من أن يهضمه حمضها القوي وإنزيم البيبسين"),
                ("To turn starch directly into dietary fiber inside the stomach", "لتحويل النشا مباشرة إلى ألياف غذائية داخل المعدة"),
                ("To neutralize oxygen entering through the windpipe", "لمعادلة الأكسجين الداخل عبر القصبة الهوائية"),
                ("To dissolve red blood cells before nutrients enter the esophagus", "لتحليل خلايا الدم الحمراء قبل دخول الغذاء للمريء"),
            ],
            "Acid + protein-digesting enzymes could damage living stomach cells without a shield.",
            "الحمض القوي والإنزيم الهاضم للبروتين قد يضران بخلايا المعدة نفسها لولا وجود عازل.",
            "Gastric mucus shields stomach cells from corrosive HCl and protein enzymes.",
            ["HCl kills swallowed bacteria and activates pepsin to digest meat/bean proteins.", "Alkaline mucus coats the stomach lining so the acid digests food instead of the stomach itself."],
            "Breaks in that mucus shield lead to painful stomach ulcers.",
            "يقي المخاط بطانة المعدة من التآكل بفعل الحمض القوي.",
            ["يهضم حمض المعدة وإنزيم البيبسين البروتينات ويقتلان الجراثيم.", "يشكل المخاط حاجزاً عازلاً يمنع تآكل جدار المعدة العضلي نفسه."],
            "ضعف هذه الطبقة المخاطية يسبب قرحة المعدة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b04:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Exercise physiology table & multi-system reasoning
    hr_tbl_en = svg_data_table(
        ["Activity", "Heart (bpm)", "Breaths/min"],
        [["Rest", "72", "14"], ["Brisk Walk", "105", "22"], ["Sprint", "156", "38"], ["5m Recovery", "88", "18"]],
        "Exercise Physiology Log",
        [106, 114, 114],
    )
    hr_tbl_ar = svg_data_table(
        ["النشاط", "النبض/د", "التنفس/د"],
        [["راحة", "72", "14"], ["مشي سريع", "105", "22"], ["جري سريع", "156", "38"], ["بعد 5 د", "88", "18"]],
        "سجل الجهد البدني",
        [106, 114, 114],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A Grade 6 runner logs heart rate and breathing rate across four stages in the table. Why do BOTH heart rate and breathing rate more than double during the sprint?",
        "سجّل عدّاء في الصف السادس معدل نبضات القلب ومعدل التنفس في أربع مراحل كما في الجدول. لماذا يتضاعف كلٌّ من النبض والتنفس معاً أثناء الجري السريع؟",
        [
            ("Leg muscles burn glucose rapidly for energy, demanding faster O₂ delivery and faster CO₂ removal by lungs and blood", "تحرق العضلات الجلوكوز بسرعة لإنتاج الطاقة، مما يتطلب توصيلاً أسرع للأكسجين وتخلصاً أسرع من ثاني أكسيد الكربون"),
            ("Running shakes air out of the stomach into the alveoli, forcing extra beats", "يدفع الجري الهواء من المعدة إلى الحويصلات مما يزيد النبض"),
            ("Faster breathing cools blood down so the heart beats rapidly to prevent freezing", "التنفس السريع يبرّد الدم فيتسارع القلب لمنع تجمده"),
            ("Muscles stop cellular respiration while sprinting and run solely on white blood cells", "تتوقف العضلات عن التنفس الخلوي أثناء الجري وتعتمد على الخلايا البيضاء"),
        ],
        "Connect respiratory gas exchange (O₂ in, CO₂ out) with circulatory transport to muscle mitochondria.",
        "اربط بين تبادل الغازات في الرئتين ونقل الدم للأكسجين والغذاء إلى ميتوكوندريا العضلات.",
        "Respiratory and circulatory systems accelerate together to support muscle respiration.",
        ["Active muscle mitochondria consume much more O₂ and glucose and produce extra CO₂.", "Faster breathing refreshes alveolar O₂ and vents CO₂; faster heart rate pumps oxygenated blood to muscles quickly."],
        "Notice both rates drop together during the 5-minute recovery.",
        "يتعاون الجهازان التنفسي والدوري لتلبية حاجة العضلات للطاقة.",
        ["تستهلك العضلات أثناء الجري كمية كبيرة من الأكسجين وتنتج ثاني أكسيد الكربون بكثرة.", "يسرّع التنفس إدخال O₂ وطرد CO₂، بينما يسرّع القلب ضخ الدم الحامل للأكسجين إلى العضلات."],
        "ولذلك ينخفض المعدلان معاً عند التوقف للراحة.",
        hr_tbl_en, hr_tbl_ar,
    )

    hard_b04 = [
        (
            "A medical condition flattens the microscopic finger-like villi lining a patient's small intestine into a smooth flat tube. Even though the patient eats plenty of balanced food, they become weak and lose weight. Why?",
            "تسببت حالة مرضية في تسطّح الخملات الدقيقة المبطنة للأمعاء الدقيقة لدى مريض لتصبح ملساء. ومع أن المريض يتناول طعاماً متوازناً بكثرة، فإنه يصاب بالهزال ونقص الوزن. ما السبب؟",
            [
                ("Surface area for nutrient absorption shrinks dramatically, so digested glucose and amino acids pass out unabsorbed", "تنخفض مساحة سطح الامتصاص بدرجة كبيرة فلا ينتقل الغذاء المهضوم إلى الدم ويخرج مع الفضلات"),
                ("Stomach acid stops working whenever intestinal villi flatten", "يتوقف حمض المعدة عن العمل فور تسطح الخملات"),
                ("Smooth intestines cannot push food downward by swallowing", "تعجز الأمعاء الملساء عن دفع الطعام عبر البلع"),
                ("Blood capillaries inside the lungs lose their hemoglobin", "تفقد شعيرات الرئتين بروتين الهيموجلوبين"),
            ],
            "What geometric property do millions of tiny folds and projections provide inside the small intestine?",
            "ما الميزة الهندسية التي توفرها ملايين الانثناءات والخملات الدقيقة داخل الأمعاء؟",
            "Villi maximize absorptive surface area inside the small intestine.",
            ["Healthy villi create a massive surface area (like a tennis court) touching digested food.", "Flattening villi reduces absorption surface, starving body cells despite normal eating."],
            "This matches celiac-style malabsorption biology.",
            "تزيد الخملات مساحة السطح الماص في الأمعاء الدقيقة عشرات الأضعاف.",
            ["يمر الطعام المهضوم عبر الأمعاء دون وقت أو مساحة كافية لعبور المغذيات إلى الشعيرات الدموية.", "فينتج نقص التغذية رغم وفرة الطعام المتناول."],
            "الكفاءة تعتمد على ضخامة مساحة التلامس مع الدم.",
            None, None,
        ),
        (
            "Trace the exact sequence of systems and structures a single glucose molecule follows from a date fruit you eat until it powers a contracting leg muscle cell:",
            "تتبّع المسار الدقيق الذي يسلكه جزيء جلوكوز واحد من حبة تمر أكلتها حتى يصل لتوليد الطاقة في خلية عضلية بساقك:",
            [
                ("Digestive tract → Small intestine villi → Blood capillaries & Heart → Muscle cell mitochondria", "القناة الهضمية ← خملات الأمعاء الدقيقة ← الشعيرات والقلب ← ميتوكوندريا الخلية العضلية"),
                ("Trachea → Lung alveoli → Veins → Stomach lining → Muscle nucleus", "القصبة الهوائية ← الحويصلات ← الأوردة ← بطانة المعدة ← نواة العضلة"),
                ("Large intestine → Bile duct → Bronchioles → Skin pores", "الأمعاء الغليظة ← القناة الصفراوية ← الشعيبات الهوائية ← مسام الجلد"),
                ("Esophagus → Kidney tubules → Alveoli → Muscle cell wall", "المريء ← أنابيب الكلى ← الحويصلات ← جدار الخلية العضلية"),
            ],
            "Follow absorption into blood, transport by the circulatory pump, and breakdown inside the energy organelle.",
            "اتبع امتصاصه إلى الدم ثم نقله بالدورة الدموية ثم تأكسده داخل عضية الطاقة.",
            "Digestive, circulatory, and cellular systems work sequentially.",
            ["Glucose is released in digestion and absorbed through small intestine villi into blood.", "The heart pumps blood via arteries to muscle capillaries, where glucose enters muscle mitochondria for cellular respiration."],
            "Every body cell depends on both digestive glucose and respiratory oxygen.",
            "تترابط أجهزة الهضم والدوران والتنفس الخلوي لإمداد العضلة بالطاقة.",
            ["يُمتص الجلوكوز عبر خملات الأمعاء الدقيقة إلى الدم.", "يضخه القلب عبر الشرايين ليصل إلى ميتوكوندريا الخلايا العضلية حيث يتحرر منه الطاقة."],
            "لا تصل المغذيات للعضلات دون تعاون الهضم والدوران.",
            svg_process_flow(["Small Int.", "Bloodstream", "Heart Pump", "Mitochondria"], "Multi-System Delivery", "Glucose to Energy"),
            svg_process_flow(["الأمعاء الدقيقة", "الدم", "القلب", "الميتوكوندريا"], "تكامل الأجهزة الحيوية", "من الغذاء إلى الطاقة"),
        ),
        (
            "If a person's resting heart pumps 70 mL of blood per beat at 75 beats per minute, how many milliliters of blood does the heart pump in 4 minutes of rest?",
            "إذا كان قلب شخص أثناء الراحة يضخ 70 مل من الدم في كل نبضة بمعدل 75 نبضة في الدقيقة، فكم ملليلتراً من الدم يضخ القلب خلال 4 دقائق من الراحة؟",
            (21000, [5250, 14500, 28000]),
            "First find mL per minute (70 × 75), then multiply by 4 minutes.",
            "احسب أولاً كمية الدم في الدقيقة (70 × 75)، ثم اضرب الناتج في 4 دقائق.",
            "Cardiac output over time = (volume per beat) × (beats per min) × (minutes).",
            ["Blood pumped in 1 minute = 70 × 75 = 5,250 mL/min.", "Blood pumped in 4 minutes = 5,250 × 4 = 21,000 mL (21 liters)."],
            "21,000 ÷ 4 = 5,250 and 5,250 ÷ 75 = 70.",
            "نحسب الضخ في الدقيقة الواحدة ثم نضرب في عدد الدقائق.",
            ["كمية الدم في الدقيقة = 70 × 75 = 5250 مل.", "في 4 دقائق = 5250 × 4 = 21000 مل (أي 21 لتراً)."],
            "تحقق: 70 × 300 نبضة = 21000 مل.",
            None, None,
        ),
        (
            "Cigarette smoke coats lung alveoli with sticky tar and thickens alveolar walls. Which immediate physiological effect explains why a smoker runs out of breath quickly when climbing stairs?",
            "يغلف دخان السجائر الحويصلات الهوائية بالقطران اللزج ويزيد سماكة جدرانها. أي أثر فسيولوجي مباشر يفسر سرعة انقطاع نفس المدخن عند صعود الدرج؟",
            [
                ("O₂ diffuses much more slowly across thickened walls into blood, starving working leg muscles of oxygen", "يتباطأ انتشار الأكسجين عبر الجدران السميكة إلى الدم فتعاني عضلات الساق من نقص الأكسجين"),
                ("Tar dissolves red blood cell nuclei and stops stomach acid secretion", "يذيب القطران أنوية كريات الدم الحمراء ويوقف إفراز المعدة"),
                ("Thick alveolar walls prevent the diaphragm from contracting downward", "تمنع الجدران السميكة عضلة الحجاب الحاجز من الانقباض للأسفل"),
                ("Smoke converts exhaled CO₂ into extra glucose inside the trachea", "يحول الدخان غاز CO₂ إلى جلوكوز زائد داخل القصبة الهوائية"),
            ],
            "Gas diffusion speed depends on keeping the alveolar membrane paper-thin and clean.",
            "تعتمد سرعة انتقال الغازات على بقاء جدار الحويصلات رقيقاً للغاية ونظيفاً.",
            "Thickened or tar-coated alveoli impede O₂ and CO₂ diffusion into capillaries.",
            ["Normal gas exchange needs thin, moist, unobstructed alveolar surface area.", "Tar decreases effective surface area and widens diffusion distance, reducing oxygen delivery to blood."],
            "Less blood O₂ limits aerobic ATP production in muscles during exertion.",
            "تعيق السماكة والقطران سرعة تبادل الغازات عبر جدار الحويصلات.",
            ["يتطلب الانتشار السريع للأكسجين غشاءً رقيقاً غير مغطى بالعوائق.", "تضاعف طبقة القطران وسماكة الجدار المسافة التي يقطعها الأكسجين فتقل نسبته في الدم."],
            "يظهر ذلك فوراً على شكل لهث وتعب سريع عند المجهود.",
            None, None,
        ),
    ]
    for qen, qar, item_or_pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b04:
        if isinstance(item_or_pairs, tuple):
            ans_v, dists_v = item_or_pairs
            B.add_math(tp, "Hard", bp, qen, qar, ans_v, dists_v, hen, har, ien, sen, cen, iar, sar, car, "", den, dar)
        else:
            B.add_concept(tp, "Hard", bp, qen, qar, item_or_pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b05(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B05"
    # Easy (0..4): Food chain roles & decomposers with svg_food_chain
    easy_b05 = [
        (
            ["Grass", "Gazelle", "Wolf", "Eagle"], ["عشب", "غزال", "ذئب", "نسر"],
            "Savanna Food Chain", "سلسلة غذائية برية",
            "In the desert-edge food chain shown, which organism is the producer that captures energy directly from sunlight?",
            "في السلسلة الغذائية البرية الموضحة، أي كائن يمثل المنتِج الذي يستمد طاقته مباشرة من ضوء الشمس؟",
            [("Grass", "العشب"), ("Gazelle", "الغزال"), ("Wolf", "الذئب"), ("Eagle", "النسر")],
            "Producers are plants or algae at the start of every food chain.",
            "المنتجات هي النباتات أو الطحالب التي تصنع غذاءها في بداية السلسلة.",
            "Producers convert sunlight into chemical energy for the whole ecosystem.",
            ["Arrows point in the direction energy flows.", "Grass sits at the base (left), capturing sunlight via photosynthesis."],
            "Gazelle is primary consumer; wolf and eagle are higher consumers.",
            "تبدأ السلسلة الغذائية دائماً بكائن منتِج يصنع غذاءه بنفسه.",
            ["العشب في بداية السلسلة يستخدم ضوء الشمس في البناء الضوئي.", "بينما الغزال والذئب والنسر كائنات مستهلكة."],
            "اتجاه الأسهم يدل على انتقال الطاقة من الكائن المأكول إلى الآكل.",
        ),
        (
            ["Algae", "Shrimp", "Grouper", "Shark"], ["طحالب", "روبيان", "هامور", "قرش"],
            "Red Sea Food Chain", "سلسلة بحرية بالبحر الأحمر",
            "In this Red Sea marine food chain, which organism is the primary consumer (herbivore) feeding directly on the producer?",
            "في السلسلة الغذائية البحرية بالبحر الأحمر، أي كائن يمثل المستهلك الأول الذي يتغذى مباشرة على المنتِج؟",
            [("Shrimp", "الروبيان"), ("Algae", "الطحالب"), ("Grouper", "الهامور"), ("Shark", "القرش")],
            "Follow the first arrow leaving the producer (Algae).",
            "تتبع السهم الأول الخارج من المنتِج (الطحالب).",
            "Primary consumers feed directly on photosynthetic producers.",
            ["Algae are producers.", "Shrimp eat Algae directly → primary consumer; Grouper is secondary consumer; Shark is tertiary consumer."],
            "Primary consumers occupy the second box in a chain.",
            "المستهلك الأول هو آكل الأعشاب أو الطحالب الذي يلي المنتِج مباشرة.",
            ["الطحالب هي المنتِج في بداية السلسلة.", "يتغذى الروبيان على الطحالب مباشرة فهو المستهلك الأول."],
            "أما الهامور والقرش فمستهلكان ثاني وثالث.",
        ),
        (
            ["Acacia", "Locust", "Hoopoe", "Falcon"], ["سنط", "جراد", "هدهد", "صقر"],
            "Saudi Wadi Chain", "سلسلة وادي سعودي",
            "What do the arrows pointing from Acacia → Locust → Hoopoe → Falcon represent in this wadi food chain?",
            "ماذا تمثل الأسهم المتجهة من السنط إلى الجراد ثم الهدهد فالصقر في هذه السلسلة الغذائية؟",
            [
                ("The direction in which food energy flows from one organism to its consumer", "اتجاه انتقال الطاقة الغذائية من الكائن إلى الكائن الذي يتغذى عليه"),
                ("Which animal is faster at running or flying across the valley", "أي الحيوانات أسرع جرياً أو طيراناً في الوادي"),
                ("The order in which organisms wake up each morning", "ترتيب استيقاظ الكائنات الحية في الصباح"),
                ("How water evaporates from plant roots into bird feathers", "كيفية تبخر الماء من جذور النبات إلى ريش الطيور"),
            ],
            "Think about where the energy starts and who eats whom!",
            "فكر من أين تبدأ الطاقة وإلى جسم مَن تنتقل عند الافتراس أو التغذية!",
            "Food-chain arrows show energy transfer from organism eaten → consumer.",
            ["Locusts eat Acacia leaves, transferring chemical energy from Acacia to Locust.", "Each arrow points into the mouth/consumer that gains the energy."],
            "Remember: arrows do NOT mean 'eats' in reverse; they mean 'is eaten by / passes energy to'.",
            "تشير أسهم السلسلة الغذائية إلى اتجاه تدفق الطاقة والغذاء.",
            ["عندما يأكل الجراد أوراق السنط تنتقل الطاقة من السنط إلى الجراد، وهكذا حتى الصقر.", "لذلك يشير السهم دائماً من الغذاء إلى المستهلك."],
            "نقطة البداية دائماً هي الطاقة الشمسية التي يلتقطها المنتِج.",
        ),
        (
            ["Corn", "Mouse", "Viper", "Hawk"], ["ذرة", "فأر", "أفعى", "صقر"],
            "Farmland Food Chain", "سلسلة غذائية زراعية",
            "When Corn, Mouse, Viper, or Hawk dies, which group of organisms breaks down their bodies and returns mineral nutrients to the soil for Corn?",
            "عندما يموت نبات الذرة أو الفأر أو الأفعى أو الصقر، أي مجموعة كائنات تحلل أجسامها وتعيد الأملاح المعدنية إلى التربة ليستخدمها النبات مجدداً؟",
            [
                ("Decomposers (soil bacteria and fungi)", "المحللات (بكتيريا التربة والفطريات)"),
                ("Tertiary apex predators", "المفترسات العليا الثالثة"),
                ("Herbivorous primary consumers", "المستهلكات الأولى آكلة الأعشاب"),
                ("Abiotic sandstone rocks", "الصخور الرملية غير الحية"),
            ],
            "Think of nature's recyclers working in the soil.",
            "فكر في الكائنات التي تعيد تدوير المادة العضوية في التربة.",
            "Decomposers recycle dead organic matter back into soil minerals.",
            ["Bacteria and fungi digest dead tissues and animal wastes.", "They release nitrogen, phosphorus, and minerals back to soil for plant roots."],
            "Without decomposers, dead bodies would pile up and soil nutrients would run out.",
            "تعيد المحللات العناصر الغذائية من الأجسام الميتة إلى التربة.",
            ["تقوم البكتيريا والفطريات بتفكيك بقايا الكائنات الميتة وفضلاتها.", "فتتحول إلى أملاح ومعادن خصبة تمتصها جذور الذرة من جديد."],
            "بدون المحللات تنفد خصوبة التربة وتتراكم الفضلات.",
        ),
        (
            ["Date Palm", "Beetle", "Lizard", "Fox"], ["نخلة", "خنفساء", "سحلية", "ثعلب"],
            "Oasis Ecosystem", "نظام بيئي بواحة",
            "In the oasis food chain shown, how would you classify the Lizard based on what it eats and who eats it?",
            "في السلسلة الغذائية للواحة، كيف تصنّف السحلية بناءً على غذائها ومن يتغذى عليها؟",
            [
                ("Secondary consumer (carnivore/insectivore)", "مستهلك ثانٍ (آكل لحوم / حشرات)"),
                ("Autotrophic producer", "منتِج ذاتي التغذية"),
                ("Primary consumer (herbivore)", "مستهلك أول (آكل أعشاب)"),
                ("Soil decomposer", "محلِّل في التربة"),
            ],
            "Count steps after the Date Palm: Beetle = 1st consumer, Lizard = ?",
            "عدّ الخطوات بعد النخلة: الخنفساء مستهلك أول، إذن السحلية مستهلك ...؟",
            "An organism eating a primary consumer is a secondary consumer.",
            ["Date Palm = producer.", "Beetle eats palm = primary consumer; Lizard eats beetle = secondary consumer; Fox = tertiary consumer."],
            "Because the lizard eats beetles (animals), it is a secondary consumer.",
            "آكل المستهلك الأول يُسمى مستهلكاً ثانياً.",
            ["النخلة منتِج، والخنفساء مستهلك أول لأنها تأكل النبات.", "السحلية تأكل الخنفساء فهي مستهلك ثانٍ."],
            "أما الثعلب الذي يأكل السحلية فهو مستهلك ثالث.",
        ),
    ]
    for s_en, s_ar, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in easy_b05:
        den, dar = _food_chain_svgs(s_en, s_ar, ten, tar)
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): 10% energy rule math + population shifts
    med_math_b05 = [
        (
            ["Grass", "Cricket", "Frog", "Heron"], ["عشب", "صرصور", "ضفدع", "بلشون"],
            10000, 10, [1000, 100, 3000],
            "Suppose producers (Grass) capture 10,000 J of chemical energy. If only 10% of energy passes up to each next trophic level, how many joules reach the tertiary consumer (Heron)?",
            "افترض أن العشب (المنتِج) خزّن 10,000 جول من الطاقة الكيميائية. إذا انتقل 10% فقط من الطاقة إلى كل مستوى غذائي تالٍ، فكم جولاً يصل إلى المستهلك الثالث (البلشون)؟",
        ),
        (
            ["Algae", "Snail", "Perch", "Osprey"], ["طحالب", "حلزون", "سمك", "عقاب"],
            25000, 25, [2500, 250, 7500],
            "In a coastal lagoon, Algae store 25,000 J of energy. Using the 10% energy transfer rule per trophic step, how much energy reaches the top predator (Osprey)?",
            "في بحيرة ساحلية، تخزن الطحالب 25,000 جول من الطاقة. باستخدام قاعدة انتقال 10% في كل خطوة غذائية، كم جولاً يصل إلى المفترس الأعلى (العقاب)؟",
        ),
        (
            ["Clover", "Rabbit", "Snake", "Owl"], ["برسيم", "أرنب", "أفعى", "بومة"],
            8000, 8, [800, 80, 2400],
            "Clover plants hold 8,000 J of stored food energy. Following the 10% rule at every arrow, how many joules of energy reach the Owl (4th trophic level)?",
            "تحتوي نباتات البرسيم على 8,000 جول من الطاقة المخزنة. باتباع قاعدة الـ 10% عند كل سهم، كم جولاً يصل إلى البومة (المستوى الرابع)؟",
        ),
    ]
    for s_en, s_ar, e0, e3, dists, qen, qar in med_math_b05:
        den, dar = _food_chain_svgs(s_en, s_ar, "Energy Flow (10% Rule)", "انتقال الطاقة (قاعدة 10%)")
        e1, e2 = e0 // 10, e0 // 100
        B.add_math(
            tp, "Medium", bp, qen, qar, e3, dists,
            "Divide by 10 (multiply by 0.10) across three trophic steps: Level 1 → Level 2 → Level 3 → Level 4.",
            "اقسم على 10 في كل انتقال عبر ثلاث خطوات: منتِج ← أول ← ثانٍ ← ثالث.",
            "Only ~10% of available energy transfers up each trophic link.",
            [f"Level 2 (primary consumer): {e0} ÷ 10 = {e1} J.", f"Level 3 (secondary): {e1} ÷ 10 = {e2} J. Level 4 (tertiary): {e2} ÷ 10 = {e3} J."],
            f"{e0} × 0.1 × 0.1 × 0.1 = {e3} J.",
            "ينتقل نحو 10% فقط من الطاقة من كل مستوى إلى المستوى الذي يليه.",
            [f"المستهلك الأول: {e0} ÷ 10 = {e1} جول.", f"المستهلك الثاني: {e2} جول، والمستهلك الثالث: {e2} ÷ 10 = {e3} جول."],
            f"تُفقد 90% من الطاقة تقريباً في كل خطوة كحرارة وحركة.",
            "", den, dar,
        )

    med_c_b05 = [
        (
            ["Shrub", "Hare", "Fox", "Eagle"], ["شجيرة", "أرنب بري", "ثعلب", "عقاب"],
            "If hunters suddenly remove almost all Foxes from the ecosystem shown, what immediate changes are most likely in the Hare and Shrub populations?",
            "إذا أزال الصيادون فجأة معظم الثعالب من هذا النظام البيئي، ما التغيرات الفورية المتوقعة في أعداد الأرانب البرية والشجيرات؟",
            [
                ("Hare population rises rapidly, causing Shrub population to decrease from overgrazing", "يزداد عدد الأرانب البرية سريعاً مما يسبب تناقص الشجيرات بسبب الرعي الجائر"),
                ("Hare population drops to zero immediately while Shrubs grow twice as thick", "ينعدم عدد الأرانب فوراً وتتضاعف الشجيرات"),
                ("Eagle population triples immediately because Foxes ate all the shrubs", "يتضاعف عدد العقبان فوراً لأن الثعالب كانت تأكل الشجيرات"),
                ("Decomposers turn directly into Foxes within one week", "تتحول المحللات مباشرة إلى ثعالب خلال أسبوع"),
            ],
            "Removing a predator releases its prey from predation pressure; ask what the prey eats!",
            "إزالة المفترس يزيد أعداد فريسته؛ فكر ماذا تأكل هذه الفريسة!",
            "Predator removal triggers an alternating trophic cascade.",
            ["Fewer Foxes means fewer Hares get eaten → Hare population booms.", "More Hares graze heavily on Shrubs → Shrub population declines (and Eagles also lose a food source)."],
            "Food webs transmit population ripples across linked levels.",
            "إزالة أحد المفترسات تؤثر في المستويات الأعلى والأدنى منه.",
            ["نقص الثعالب يقلل افتراس الأرانب فتتكاثر الأرانب بكثرة.", "زيادة الأرانب تزيد التهام الشجيرات فتقل كثافة الغطاء النباتي."],
            "وهذا يوضح الترابط المتوازن في السلسلة الغذائية.",
        ),
        (
            ["Plankton", "Anchovy", "Tuna", "Orca"], ["عوالق", "أنشوجة", "تونة", "أوركا"],
            "Why does an ocean ecosystem contain far greater total biomass of tiny Plankton than of large Orca whales?",
            "لماذا يحتوي النظام البيئي البحري على كتلة حيوية أكبر بكثير من العوالق الدقيقة مقارنة بحيتان الأوركا الكبيرة؟",
            [
                ("About 90% of energy is lost as heat and life processes at each trophic step, supporting fewer top predators", "لأن نحو 90% من الطاقة يُفقد كحرارة وأنشطة حيوية في كل مستوى، مما يدعم عدداً أقل من المفترسات العليا"),
                ("Orca whales refuse to eat more than once per year", "لأن حيتان الأوركا لا تتغذى إلا مرة واحدة في السنة"),
                ("Plankton do not need any energy from sunlight or food", "لأن العوالق لا تحتاج أي طاقة من الشمس أو الغذاء"),
                ("Ocean water dissolves top predators back into algae overnight", "لأن ماء البحر يذيب المفترسات العليا ويحولها إلى طحالب"),
            ],
            "Recall the ecological pyramid of energy and biomass.",
            "تذكر هرم الطاقة والكتلة الحيوية في الأنظمة البيئية.",
            "Large energy losses at each step require a massive producer base.",
            ["Producers use energy to swim, respire, and grow; much energy dissipates as heat.", "Only ~10% per step reaches the next level, so a wide base of Plankton is needed to sustain a few Orcas."],
            "That is why top predators are always rarer than producers.",
            "يتناقص مخزون الطاقة المتاحة كلما ارتفعنا نحو قمة الهرم الغذائي.",
            ["تُستهلك 90% من الطاقة تقريباً في التنفس والحرارة عند كل مستوى.", "لذلك يلزم وجود قاعدة هائلة من العوالق لإعالة عدد قليل من المفترسات العليا."],
            "وهذا يفسر ندرة المفترسات العليا مقارنة بالنباتات والطحالب.",
        ),
    ]
    for s_en, s_ar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in med_c_b05:
        den, dar = _food_chain_svgs(s_en, s_ar, "Trophic Interaction", "التفاعل الغذائي")
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Food web cascades, biomagnification, decomposer removal, max chain length
    hard_b05 = [
        (
            ["Reeds", "Mayfly", "Sunfish", "Heron"], ["قصب", "ذباب مايو", "سمك شمس", "بلشون"],
            "A harmless-looking farm pesticide enters a lake at tiny concentration (0.01 units in Reeds). Because organisms cannot excrete it, each consumer eats many prey and concentrates the toxin. Which organism carries the highest toxin level?",
            "تسرّب مبيد زراعي إلى بحيرة بتركيز ضئيل جداً (0.01 وحدة في القصب). ولأن الكائنات لا تستطيع التخلص منه، يتراكم في أنسجتها مع التغذية. أي كائن يحمل أعلى تركيز للسم؟",
            [
                ("Heron (the top tertiary consumer)", "البلشون (المستهلك الثالث في القمة)"),
                ("Reeds (the aquatic producer)", "القصب (المنتِج المائي)"),
                ("Mayfly (the herbivorous larva)", "يرقة ذباب مايو (المستهلك الأول)"),
                ("Lake water molecules only", "جزيئات ماء البحيرة فقط"),
            ],
            "This process is called biomagnification: each predator eats hundreds of lower-level prey and keeps all their toxins.",
            "يُسمى ذلك التضخم الحيوي: كل مفترس يأكل عشرات الفرائس فيجمع سمومها جميعاً في جسمه.",
            "Persistent toxins amplify up food chains (biomagnification).",
            ["One Mayfly eats many Reeds; one Sunfish eats dozens of Mayflies; one Heron eats many Sunfish.", "Because the pesticide stays stored in fat, toxin concentration multiplies at the top (Heron)."],
            "While energy drops 10× per step upward, non-degradable toxins concentrate upward!",
            "تتضاعف تراكيز السموم غير القابلة للتحلل بالصعود في السلسلة الغذائية.",
            ["يأكل البلشون العديد من الأسماك التي جمعت بدورها سموم مئات الحشرات والنباتات.", "فيتركز المبيد بأعلى نسبة في أنسجة المستهلك الأعلى (البلشون)."],
            "بينما تتناقص الطاقة للأعلى، يتصاعد تركيز السموم المتراكمة.",
        ),
        (
            ["Oats", "Field Mouse", "Rattlesnake", "Hawk"], ["شوفان", "فأر حقل", "أفعى", "صقر"],
            "Why do natural terrestrial food chains rarely contain 7 or 8 consumer levels above the producers?",
            "لماذا يندر جداً أن تحتوي السلاسل الغذائية البرية الطبيعية على 7 أو 8 مستويات استهلاكية فوق المنتِجات؟",
            [
                ("Too little energy remains after 4–5 transfers (~90% lost each step) to support a viable top predator population", "لأن الطاقة المتبقية بعد 4 إلى 5 انتقالات تكون ضئيلة جداً (لفقدان ~90% في كل خطوة) فلا تكفي لإعالة مستوى أعلى"),
                ("Predators at level 6 forget how to use cellular respiration", "لأن المفترسات في المستوى السادس تنسى كيفية التنفس الخلوي"),
                ("Sunrays cannot penetrate below 5 species in a meadow", "لأن أشعة الشمس لا تخترق أكثر من 5 أنواع في المرج"),
                ("Decomposers prevent any predator larger than a hawk from breathing oxygen", "لأن المحللات تمنع أي مفترس أكبر من الصقر من تنفس الأكسجين"),
            ],
            "Compute what fraction of 1,000,000 J survives 7 steps of 10% transfer!",
            "احسب كم يتبقى من مليون جول بعد 7 خطوات من قاعدة الـ 10%!",
            "Energy dissipation limits the maximum length of food chains.",
            ["After 4 steps (0.1⁴ = 1/10,000), only 0.01% of plant energy remains.", "By step 7 or 8, there would not be enough calories across an entire valley to keep one predator alive."],
            "Therefore, most food chains stop at 3–5 levels.",
            "فقدان الطاقة المستمر يضع سقفاً طبيعياً لطول السلاسل الغذائية.",
            ["بعد 4 مستويات لا يتبقى سوى جزء ضئيل جداً من الطاقة الأصلية للمنتِج.", "بعد 6 أو 7 خطوات تصبح الطاقة المتاحة غير كافية لبقاء جماعة حيوانية كاملة."],
            "لذلك تتوقف معظم السلاسل الغذائية عند 3 إلى 5 مستويات.",
        ),
        (
            ["Leaf Litter", "Earthworm", "Thrush", "Cat"], ["أوراق ميتة", "دودة أرض", "طائر سمنة", "قط"],
            "Suppose a chemical sterilizes a forest floor, wiping out all bacteria and fungi (decomposers) while leaving trees alive initially. What happens over the next few years?",
            "افترض أن مادة كيميائية قضت على جميع البكتيريا والفطريات (المحللات) في أرضية غابة مع بقاء الأشجار حية مؤقتاً. ما الذي سيحدث خلال السنوات التالية؟",
            [
                ("Dead leaves and carcasses accumulate without rotting, soil mineral nitrates drop, and tree growth slows and fails", "تتراكم الأوراق والجثث دون تحلل، وتنضب أملاح النيترات في التربة، فيضعف نمو الأشجار وتذبل"),
                ("Trees grow twice as fast because bacteria no longer eat their bark", "تنمو الأشجار بسرعة مضاعفة لأن البكتيريا لم تعد تأكل لحاءها"),
                ("Earthworms convert directly into photosynthetic shrubs", "تتحول ديدان الأرض مباشرة إلى شجيرات تقوم بالبناء الضوئي"),
                ("Sunlight increases by 90% so trees no longer need mineral roots", "تزداد أشعة الشمس 90% فتستغني الأشجار عن الجذور"),
            ],
            "Decomposers are the link closing the nutrient circle back to producers.",
            "المحللات هي الحلقة التي تغلق دائرة العناصر الغذائية وتعيدها للمنتِجات.",
            "Without decomposers, mineral nutrient recycling halts and soil becomes barren.",
            ["Trees need nitrogen, potassium, and phosphorus ions absorbed by roots to build proteins and chlorophyll.", "If decomposers vanish, nutrients stay locked inside unrotted dead leaves and animal bodies."],
            "Energy flows one way (Sun → heat), but matter must be recycled by decomposers!",
            "بدون المحللات ينكسر تدوير المادة في النظام البيئي.",
            ["تحتاج الأشجار إلى أملاح النيتروجين والفوسفور لصنع البروتين والكلوروفيل.", "غياب المحللات يحبس هذه العناصر داخل الأوراق المتساقطة وبقايا الكائنات فتجوع النباتات."],
            "الطاقة تتدفق في اتجاه واحد، أما المادة فتُعاد تدويرها عبر المحللات.",
        ),
        (
            ["Kelp", "Sea Urchin", "Sea Otter", "Orca"], ["عشب بحري", "قنفذ بحر", "قضاعة بحر", "أوركا"],
            "In a Pacific kelp forest, Sea Otters eat Sea Urchins, and Sea Urchins graze on giant Kelp. When Orcas shift their diet and drastically reduce the Sea Otter population, what happens to the Kelp forest?",
            "في غابة أعشاب بحرية، تأكل قضاعات البحر قنافذ البحر، وتتغذى القنافذ على الأعشاب البحرية العملاقة. عندما تلتهم حيتان الأوركا عدداً كبيراً من القضاعات، ماذا يحدث لغابة الأعشاب البحرية؟",
            [
                ("Sea Urchin numbers explode and overgraze the Kelp, creating a barren sea floor", "تتكاثر قنافذ البحر بشكل هائل وتلتهم الأعشاب البحرية حتى تتعرى أرضية البحر"),
                ("Kelp grows denser because Sea Otters used to eat giant Kelp", "تزداد كثافة الأعشاب البحرية لأن القضاعات كانت تأكلها"),
                ("Sea Urchins starve immediately even though Kelp is abundant", "تموت قنافذ البحر جوعاً فوراً رغم وفرة الأعشاب"),
                ("Orcas switch to eating Kelp directly once Sea Otters decline", "تتحول حيتان الأوركا إلى أكل الأعشاب البحرية مباشرة"),
            ],
            "Trace the 4-level cascade: Fewer Otters → what happens to Urchins → what happens to Kelp?",
            "تتبّع السلسلة الرباعية: نقص القضاعات ← أثره على القنافذ ← أثره على الأعشاب البحرية؟",
            "Top-down trophic cascades link top predators to producers two steps below.",
            ["Orcas reduce Sea Otters (secondary consumers).", "With fewer Otters eating them, Sea Urchins surge and destroy Kelp beds — a classic keystone predator effect."],
            "Every link two steps apart tends to move in the same direction (fewer Otters → less Kelp).",
            "يؤثر المفترس الأعلى بصورة غير مباشرة في المنتِجات عبر المستويات الوسطى.",
            ["نقص قضاعات البحر يحرر قنافذ البحر من الافتراس فتتزايد أعدادها.", "تهاجم القنافذ الكثيرة الأعشاب البحرية وتدمر الغابة البحرية."],
            "تسمى القضاعة هنا نوعاً مفتاحياً يحمي اتزان الغابة البحرية.",
        ),
        (
            ["Grass", "Beetle", "Lizard", "Eagle"], ["عشب", "خنفساء", "سحلية", "عقاب"],
            "In a grassland food web, Eagles eat BOTH Lizards and Field Mice, while both Lizards and Mice eat Beetles (which eat Grass). If a disease kills only Lizards, why might Field Mice actually decline soon afterward?",
            "في شبكة غذائية، يتغذى العقاب على كلٍّ من السحالي وفئران الحقل، وتأكل السحالي والفئران الخنافس التي تتغذى على العشب. إذا قضى مرض على السحالي فقط، فلماذا قد تتناقص أعداد الفئران أيضاً؟",
            [
                ("Eagles lose Lizards and switch to hunting Field Mice much more heavily", "يفقد العقاب السحالي فيركز صيده بشكل مضاعف على فئران الحقل"),
                ("Field Mice only survive by breathing oxygen released by Lizards", "تتنفس الفئران الأكسجين الذي تنتجه السحالي فقط"),
                ("Dead Lizards turn into Beetles that chase Field Mice away", "تتحول السحالي الميتة إلى خنافس تطرد الفئران"),
                ("Grass immediately stops photosynthesizing without Lizards", "يتوقف العشب عن البناء الضوئي فور موت السحالي"),
            ],
            "In a food web (unlike a single chain), a predator with two prey species shifts pressure onto the surviving prey.",
            "في الشبكة الغذائية المعقدة، إذا اختفت إحدى الفرائس يضاعف المفترس ضغطه على الفريسة الأخرى.",
            "Shared predators create indirect negative links (apparent competition) between prey.",
            ["Losing Lizards deprives Eagles of one main prey.", "Eagles intensify hunting on the remaining prey (Field Mice), driving Mouse numbers down despite more Beetles."],
            "Food webs show real-world interdependence better than single linear chains.",
            "تُظهر الشبكات الغذائية علاقات غير مباشرة بين الكائنات.",
            ["باختفاء السحالي يضطر العقاب للاعتماد كلياً على الفئران في غذائه.", "فيزداد افتراس الفئران وتنخفض أعدادها رغم توفر الخنافس."],
            "هذا يبرز أهمية الشبكة الغذائية في التنبؤ بالتغيرات البيئية.",
        ),
    ]
    for s_en, s_ar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in hard_b05:
        den, dar = _food_chain_svgs(s_en, s_ar, "Ecosystem Cascade", "التأثير المتسلسل")
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b06(B: G6SciBankBuilder) -> None:
    tp, bp = "Life Sciences", "G6-SCI-B06"
    # Easy (0..4): Adaptations & inquiry variables definitions
    easy_b06 = [
        (
            "The Fennec fox living in Arabian and Saharan sands has unusually huge ears packed with blood vessels. How does this structural adaptation help it survive desert heat?",
            "يمتلك ثعلب الفنك الذي يعيش في الصحاري أذنين كبيرتين غنيتين بالأوعية الدموية. كيف يساعده هذا التكيف التركيبي على تحمل حرارة الصحراء؟",
            [
                ("Large thin ears radiate excess body heat into the air to keep the fox cool", "تُشع الأذنان الكبيرتان الرقيقتان حرارة الجسم الزائدة إلى الهواء لتبريد الجسم"),
                ("Huge ears store drinking water for months like a camel's hump", "تخزن الأذنان الكبيرتان مياه الشرب لأشهر مثل سنام الجمل"),
                ("Large ears block sunlight so the fox can perform photosynthesis", "تحجب الأذنان ضوء الشمس ليتمكن الثعلب من البناء الضوئي"),
                ("Blood vessels in the ears freeze sand grains for drinking", "تجمّد الأوعية الدموية حبات الرمل للحصول على الماء"),
            ],
            "Large surface area exposed to air allows heat to escape quickly.",
            "المساحة السطحية الكبيرة المعرضة للهواء تسرّع التخلص من الحرارة الزائدة.",
            "Large vascular ears increase surface-area-to-volume heat dissipation.",
            ["Blood warmed by body core flows close to the thin skin of the large ears.", "Heat radiates into the cooler evening air without wasting precious body water through sweating."],
            "Arctic foxes have tiny ears to conserve heat — the exact opposite!",
            "تزيد الأذنان الكبيرتان مساحة سطح التبريد الحراري للثعلب.",
            ["يتدفق الدم الدافئ قريباً من الجلد الرقيق للأذنين الواسعتين.", "فتنتقل الحرارة للهواء دون فقدان الماء الثمين عبر التعرق."],
            "بينما يمتلك ثعلب القطب أذنين صغيرتين لحفظ الحرارة.",
            None, None,
        ),
        (
            "Why do desert cacti and thorny acacia plants grow sharp spines instead of wide flat leaves?",
            "لماذا تنمو لأشجار الصبار والطلح الصحراوية أشواك حادة بدلاً من أوراق خضراء عريضة ومسطحة؟",
            [
                ("Spines minimize surface area to cut water loss by transpiration and deter thirsty herbivores", "تقلل الأشواك مساحة السطح لتخفيض فقدان الماء بالنتح وتحمي النبات من الحيوانات العطشى"),
                ("Spines pull nitrogen gas directly into underground rocks", "تسحب الأشواك غاز النيتروجين مباشرة داخل الصخور"),
                ("Wide leaves freeze during warm desert afternoons", "تتجمد الأوراق العريضة خلال ظهيرة الصحراء الحارة"),
                ("Spines reflect 100% of water droplets back into the atmosphere", "تعكس الأشواك 100% من قطرات الماء إلى الغلاف الجوي"),
            ],
            "Wide flat leaves lose huge amounts of water through thousands of stomata.",
            "تفقد الأوراق العريضة كميات ضخمة من الماء عبر آلاف الثغور.",
            "Modified leaf spines cut transpiration water loss and defend stored water.",
            ["Cacti photosynthesize in their thick, waxy green stems while modified spines replace broad leaves.", "Spines also shade the stem slightly and protect it from grazing animals."],
            "Notice how water lilies do the exact opposite: huge flat floating leaves where water is abundant.",
            "الأشواك أوراق متحورة تحفظ الماء وتحمي النبات الصحراوي.",
            ["تقوم السيقان الخضراء السميكة المغطاة بطبقة شمعية بعملية البناء الضوئي.", "تقلل الأشواك التبخر إلى أدنى حد وتردع الحيوانات عن التهام الساق العصارية."],
            "هذا التكيف التركيبي مثالي لندرة الأمطار الصحراوية.",
            None, None,
        ),
        (
            "Which adaptation is a BEHAVIORAL adaptation rather than a structural body feature?",
            "أي تكيف مما يلي يُعد تكيفاً سلوكياً وليس تكيفاً تركيبياً في شكل الجسم؟",
            [
                ("Desert jerboas remaining inside cool underground burrows all day and foraging at night", "بقاء اليربوع الصحراوي داخل جحور باردة تحت الأرض طوال النهار وخروجه ليلاً"),
                ("A camel having wide padded two-toed hooves that keep it from sinking in soft sand", "امتلاك الجمل خفاً عريضاً مبطناً يمنع غوصه في الرمل الناعم"),
                ("A polar bear growing dense hollow fur and a thick fat layer", "نمو فراء كثيف وطبقة شحم سميكة لدى الدب القطبي"),
                ("A duck having webbed feet for paddling smoothly across ponds", "امتلاك البط أقداماً مكففة للسباحة بسهولة في البرك"),
            ],
            "Structural = physical body part; Behavioral = action or habit an organism does.",
            "التركيبي يرتبط بتركيب عضو في الجسم؛ والسلوكي يرتبط بتصرف أو عادة يفعلها الكائن.",
            "Behavioral adaptations are actions organisms perform to survive.",
            ["Hooves, fur, and webbed feet are inherited anatomical structures.", "Nocturnal burrowing (sleeping in cool burrows by day, foraging at night) is an instinctive behavior."],
            "Bird seasonal migration and hibernation are other classic behavioral adaptations.",
            "التكيف السلوكي هو تصرف يقوم به الكائن الحي استجابة لبيئته.",
            ["الخف والفراء والأقدام المكففة تراكيب جسمية (تكيفات تركيبية).", "الاختباء في الجحور نهاراً والنشاط ليلاً سلوك لتفادي حرارة الشمس."],
            "الهجرة الموسمية للطيور والبيات الشتوي أمثلة سلوكية أخرى.",
            None, None,
        ),
        (
            "In a science fair plant experiment, a student waters four pots with different amounts of water (50 mL, 100 mL, 150 mL, 200 mL) and measures plant height after 3 weeks. What is the INDEPENDENT variable?",
            "في تجربة علمية لنمو النبات، سقى طالب 4 أصص بكميات مختلفة من الماء (50 مل، 100 مل، 150 مل، 200 مل) ثم قاس طول النبات بعد 3 أسابيع. ما المتغير المستقل في هذه التجربة؟",
            [
                ("The volume of water given to each pot", "حجم الماء المضاف إلى كل أصيص"),
                ("The height of the plants after 3 weeks", "طول النباتات بعد مرور 3 أسابيع"),
                ("The pot size and soil type kept identical", "حجم الأصيص ونوع التربة المتطابقان"),
                ("The number of days in three weeks", "عدد الأيام في ثلاثة أسابيع"),
            ],
            "Independent = 'I' change it deliberately on purpose!",
            "المتغير المستقل هو العامل الوحيد الذي يتعمّد الباحث تغييره.",
            "The independent variable is the factor purposefully varied across test groups.",
            ["Water amount (50 to 200 mL) is what the student intentionally alters.", "Plant height is the dependent variable (measured outcome); soil and pot size are controlled variables."],
            "One clear independent variable ensures a fair test.",
            "المتغير المستقل هو ما يختار المجرب تغييره لاختبار أثره.",
            ["تعمّد الطالب تغيير حجم الماء بين الأصص، لذا فهو المتغير المستقل.", "أما طول النبات المقاس فهو المتغير التابع، ونوع التربة متغير ثابت."],
            "تغيير عامل واحد فقط يجعل التجربة عادلة.",
            None, None,
        ),
        (
            "In the same plant-watering experiment, what is the DEPENDENT variable?",
            "في تجربة سقاية النبات السابقة نفسها، ما المتغير التابع الذي يعتمد على كمية الماء؟",
            [
                ("The measured height of each plant after 3 weeks", "طول كل نبات المقاس بعد 3 أسابيع"),
                ("The volume of water poured into each pot", "حجم الماء المصبوب في كل أصيص"),
                ("The identical sunny windowsill location", "الموقع المتطابق عند النافذة المشمسة"),
                ("The brand of identical bean seeds planted", "نوع بذور الفاصولياء المتطابقة المزروعة"),
            ],
            "Dependent = the Data you measure because it DEPENDS on what you changed.",
            "المتغير التابع هو النتيجة التي تقيسها وتعتمد على المتغير المستقل.",
            "The dependent variable is the observed response measured by the investigator.",
            ["Plant growth (height) responds to and depends on water volume.", "Sunlight location and seed variety remain controlled (constant)."],
            "Independent → cause; Dependent → measured effect.",
            "المتغير التابع هو الأثر المقاس الناتج عن التجربة.",
            ["يتأثر نمو النبات (الطول) بكمية الماء، لذا فهو المتغير التابع.", "الضوء ونوع البذور تبقى ثابتة لضمان عدالة الاختبار."],
            "المستقل هو السبب، والتابع هو النتيجة المقاسة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b06:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Controlled fair-test variables & camel/mangrove adaptations + tables/bars
    med_b06 = [
        (
            "A student tests how fertilizer type affects radish growth across four pots shown in the bar chart. Which variables MUST be kept identical across all four pots to make it a fair test?",
            "يختبر طالب أثر نوع السماد في نمو الفجل عبر أربعة أصص كما في الرسم البياني. ما المتغيرات التي يجب تثبيتها بدقة بين الأصص الأربعة لتكون التجربة عادلة؟",
            [
                ("Seed type, soil volume, daily water amount, pot size, sunlight, and temperature", "نوع البذور، وكمية التربة، وحجم الماء اليومي، وحجم الأصيص، والإضاءة، والحرارة"),
                ("Fertilizer brand only, while varying water and sunlight freely", "نوع السماد فقط مع تغيير الماء والإضاءة بحرية"),
                ("Only the final height of the radish leaves at day 21", "طول أوراق الفجل النهائي في اليوم 21 فقط"),
                ("Keeping Pot A in a dark closet and Pot D outdoors in full sun", "وضع الأصيص A في خزانة مظلمة والأصيص D في الشمس"),
            ],
            "In a fair test, EVERY factor except fertilizer type must stay constant.",
            "في التجربة العادلة، يجب تثبيت كل الظروف الأخرى ما عدا العامل المُختبَر (نوع السماد).",
            "Controlled variables prevent outside factors from skewing experimental results.",
            ["Only fertilizer type (No fertilizer, Compost, Brand X, Brand Y) should differ.", "All water, light, temperature, pot size, and seed variety must be identical."],
            "The pot with 'None' (no fertilizer) acts as the control group.",
            "يجب تثبيت جميع المتغيرات الضابطة عدا المتغير المستقل.",
            ["نوع السماد هو المتغير المستقل الوحيد الذي نريد قياس أثره.", "تثبيت الماء والضوء والتربة ونوع البذور يضمن أن أي فرق في الطول سببه السماد وحده."],
            "الأصيص الخالي من السماد يمثل المجموعة الضابطة.",
            svg_bar_chart([("None", 8, MUTED), ("Compost", 14, GREEN), ("Brand X", 16, BLUE), ("Brand Y", 11, ORANGE)], "Height (cm)", "Fertilizer Trial (Day 21)"),
            svg_bar_chart([("بلا سماد", 8, MUTED), ("عضوي", 14, GREEN), ("سماد X", 16, BLUE), ("سماد Y", 11, ORANGE)], "الطول (سم)", "تجربة الأسمدة (يوم 21)"),
        ),
        (
            "A student designs an investigation to find out whether red bean seeds germinate faster at 15°C, 25°C, or 35°C. Which setup correctly isolates temperature as the independent variable?",
            "صمم طالب استقصاءً لمعرفة ما إذا كانت بذور الفاصولياء الحمراء تنبت أسرع عند 15°م أم 25°م أم 35°م. أي تصميم يعزل درجة الحرارة كمتغير مستقل بشكل صحيح؟",
            [
                ("Place 10 identical seeds on equally moist paper towels in three identical covered dishes kept at 15°C, 25°C, and 35°C", "وضع 10 بذور متماثلة على مناديل متساوية الرطوبة في ثلاثة أطباق مغطاة متماثلة عند 15°م و25°م و35°م"),
                ("Put dry seeds at 15°C, soaked seeds at 25°C, and soil-planted seeds at 35°C", "وضع بذور جافة عند 15°م، ومنقوعة عند 25°م، ومزروعة بتربة عند 35°م"),
                ("Use 2 seeds at 15°C, 15 seeds at 25°C, and 50 seeds at 35°C", "استخدام بذرتين عند 15°م، و15 بذرة عند 25°م، و50 بذرة عند 35°م"),
                ("Change both temperature and daily vinegar concentration in every dish", "تغيير درجة الحرارة وتركيز الخل اليومي معاً في كل طبق"),
            ],
            "Keep seed variety, sample size, moisture, and container type identical; vary ONLY temperature.",
            "ثبّت نوع البذور وعددها والرطوبة ونوع الطبق، وغيّر درجة الحرارة فقط.",
            "Valid experiments isolate one independent variable and use multiple seeds per group.",
            ["Using 10 seeds per dish averages out random individual seed differences.", "Moisture, container, and seed type are kept identical across 15°C, 25°C, and 35°C."],
            "Varying moisture or medium alongside temperature confounds the test.",
            "يتطلب التصميم السليم تغيير متغير مستقل واحد وتكرار العينة.",
            ["تثبيت الرطوبة ونوع الطبق واستخدام 10 بذور في كل درجة حرارة يعطي نتائج موثوقة.", "لو تغيرت الرطوبة أو الوسط مع الحرارة لما عرفنا سبب اختلاف الإنبات."],
            "العزل الصحيح هو أساس الاستنتاج العلمي.",
            None, None,
        ),
        (
            "Gray mangrove trees growing along the Red Sea coast tolerate salty tidal water and thick anoxic mud. Which specialized root adaptation allows their submerged roots to breathe oxygen?",
            "تنمو أشجار المانغروف (الشورى) على سواحل البحر الأحمر في مياه مالحة وطين فقير بالأكسجين. أي تكيف جذري خاص يمكّن جذورها المغمورة من تنفس الأكسجين؟",
            [
                ("Upward-growing breathing roots (pneumatophores) poking above the mud into the air", "جذور تنفسية تنمو للأعلى فوق سطح الطين والماء لاستخلاص الأكسجين من الهواء"),
                ("Deep taproots drinking pure rainwater from granite bedrock 50 m below sea level", "جذور وتدية تشرب ماء المطر النقي على عمق 50 متراً تحت البحر"),
                ("Hollow floating thorns that capture fish for nitrogen", "أشواك مجوفة تلتقط الأسماك للحصول على النيتروجين"),
                ("Replacing cell membranes with solid iron crystals", "استبدال الأغشية الخلوية ببلورات حديد صلبة"),
            ],
            "Think of snorkel tubes poking up from muddy tidewaters.",
            "فكر في أنابيب تنفس طبيعية تبرز من الطين المغمور نحو الهواء.",
            "Mangrove pneumatophores extend upward into air to supply O₂ to waterlogged roots.",
            ["Waterlogged tidal mud lacks air spaces, which would suffocate normal roots.", "Vertical breathing roots poke above low-tide mud and channel air down to underground roots (and leaves also excrete excess salt)."],
            "Another mangrove adaptation is filtering or excreting sea salt via leaves.",
            "تمتد الجذور الهوائية لأشجار الشورى للأعلى فوق الطين للتنفس.",
            ["يفتقر الطين المغمور بمياه المد إلى الأكسجين اللازم لتنفس الجذور.", "تخرج الجذور التنفسية نحو الهواء لتمرير الأكسجين إلى بقية المجموع الجذري."],
            "كما تطرد أوراقها الأملاح الزائدة للحفاظ على اتزان الماء.",
            None, None,
        ),
        (
            "In a desert-plant watering experiment, why does a student include a fourth pot that receives NO fertilizer at all while getting the exact same water, soil, and sunlight?",
            "في تجربة لاختبار أثر السماد على نبات صحراوي، لماذا يضيف الطالب أصيصاً رابعاً لا يُوضع له أي سماد بتاتاً مع إعطائه نفس الماء والتربة والشمس؟",
            [
                ("It acts as the control group baseline to prove whether the fertilizer actually changed growth", "يمثل المجموعة الضابطة التي نرجع إليها لنتأكد هل أحدث السماد فرقاً حقيقياً أم لا"),
                ("It uses up leftover sunlight so the other three pots do not overheat", "لأنه يستهلك ضوء الشمس الزائد كي لا تسخن الأصص الثلاثة الأخرى"),
                ("It turns into the dependent variable whenever seeds germinate slowly", "لأنه يتحول إلى متغير تابع عندما تنبت البذور ببطء"),
                ("It removes carbon dioxide from the soil around fertilized pots", "لأنه يزيل ثاني أكسيد الكربون من التربة حول الأصص الأخرى"),
            ],
            "Without a baseline pot with zero fertilizer, how could you tell if Brand X helped or actually harmed the plant?",
            "بدون أصيص خالٍ من السماد، كيف تعرف هل ساعد السماد النمو أم أضره؟",
            "A control group provides the baseline comparison for judging treatment effect.",
            ["Comparing fertilized pots against the unfertilized control reveals true fertilizer effect.", "If fertilized plants grow 16 cm while control grows 8 cm, the fertilizer doubled growth."],
            "If fertilized plants only reached 5 cm vs. 8 cm control, the fertilizer actually harmed them!",
            "المجموعة الضابطة هي المرجع الأساسي لقياس أثر العامل المُختبَر.",
            ["تقارن نتائج الأصص المعالجة بالسماد مع الأصيص الضابط الخالي من السماد.", "وبذلك نتحقق علمياً من فاعلية السماد إيجاباً أو سلباً."],
            "لا تكتمل التجربة المقارنة دون مجموعة ضابطة.",
            None, None,
        ),
        (
            "Which combination of adaptations helps an Arabian camel endure multi-day desert journeys without drinking water?",
            "أي مجموعة من التكيفات تساعد الجمل العربي على قطع مسافات صحراوية لأيام دون شرب الماء؟",
            [
                ("Fat stored in one localized hump (keeping rest of body uninsulated to shed heat), broad padded hooves, and double eyelashes", "تخزين الدهون في السنام وحده لتبريد بقية الجسم، وخف عريض مبطن، ورموش مزدوجة"),
                ("Liquid water stored directly inside a hollow hump and webbed swimming toes", "تخزين الماء السائل مباشرة داخل سنام مجوف وأصابع مكففة للسباحة"),
                ("Gills behind its ears and thin green skin that performs photosynthesis", "خياشيم خلف الأذنين وجلد أخضر رقيق يقوم بالبناء الضوئي"),
                ("Thick blubber covering its entire belly and short pointed needles on hooves", "طبقة شحم سميكة تغطي كامل بطنه وإبر حادة في أخفافه"),
            ],
            "Careful: a camel's hump stores FAT (not liquid water!), and keeps fat off the rest of its body so heat escapes.",
            "انتبه: سنام الجمل يخزن الدهون وليس الماء السائل، مما يترك باقي جسمه قليل العزل ليتخلص من الحرارة.",
            "Camel adaptations combine localized fat storage, heat tolerance, water conservation, and sand-walking hooves.",
            ["Storing fat in the hump provides metabolic energy without wrapping the whole body in heat-trapping blubber.", "Double eyelashes and closable nostrils keep blowing sand out; broad hooves spread weight on loose dunes."],
            "Camels can also tolerate huge drops in hydration and body temperature swings.",
            "تجمع تكيفات الجمل بين حفظ الطاقة وتقليل فقدان الماء ومقاومة الرمل.",
            ["السنام مخزن للدهون وليس للماء السائل، وتجمع الدهون فيه يمنع احتباس الحرارة في سائر الجسم.", "وتحمي الرموش المزدوجة والخف العريض الجمل من العواصف والرمال المتحركة."],
            "تلك منظومة تكيف متكاملة لبيئة الصحراء.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b06:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Diagnosing confounded trials & reading inquiry tables
    flaw_tbl_en = svg_data_table(
        ["Pot", "Soil", "Light", "Growth"],
        [["P1", "Sand", "Shade", "4 cm"], ["P2", "Loam", "Full Sun", "15 cm"], ["P3", "Clay", "Partial", "9 cm"]],
        "Student Experiment Log",
        [64, 88, 96, 86],
    )
    flaw_tbl_ar = svg_data_table(
        ["الأصيص", "التربة", "الإضاءة", "النمو"],
        [["P1", "رملية", "ظل", "4 سم"], ["P2", "طميية", "شمس كاملة", "15 سم"], ["P3", "طينية", "جزئية", "9 سم"]],
        "سجل تجربة طالب",
        [68, 88, 98, 86],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A student runs the plant experiment in the table and concludes: 'Loam soil caused P2 to grow tallest.' Why is this conclusion scientifically INVALID?",
        "أجرى طالب تجربة النبات في الجدول ثم استنتج: «التربة الطميية وحدها هي سبب نمو الأصيص P2 أكثر من غيره». لماذا يُعد هذا الاستنتاج غير صالح علمياً؟",
        [
            ("Both soil type AND sunlight intensity changed across pots, so it is impossible to isolate which variable caused the growth", "لأن نوع التربة وشدة الإضاءة تغيرا معاً بين الأصص، فيستحيل الجزم أي المتغيرين أحدث الزيادة"),
            ("Loam soil cannot support any plant growth unless placed in total darkness", "لأن التربة الطميية لا تدعم أي نمو إلا في الظلام التام"),
            ("4 cm, 9 cm, and 15 cm show that plants actually shrank over time", "لأن الأطوال 4 و9 و15 سم تثبت أن النباتات انكمشت"),
            ("Three pots cannot be measured with a metric ruler accurately", "لأن قياس ثلاثة أصص بالمسطرة المترية مستحيل"),
        ],
        "Count how many variables changed between P1, P2, and P3!",
        "عدّ كم متغيراً تغير في الوقت نفسه بين الأصص P1 وP2 وP3!",
        "Changing two independent variables simultaneously confounds an experiment.",
        ["P2 had BOTH Loam soil AND Full Sun, whereas P1 had Sand AND Shade.", "To test soil validly, all pots must sit in identical sunlight (e.g., all in full sun) with only soil differing."],
        "Never change two factors at once in a controlled investigation.",
        "تغيير عاملين مستقلين معاً يفسد الاستنتاج العلمي.",
        ["حصل الأصيص P2 على تربة طميية وإضاءة شمس كاملة في آنٍ واحد مقارنة بـ P1.", "لاختبار أثر التربة، كان يجب وضع جميع الأصص تحت الإضاءة نفسها وتغيير التربة فقط."],
        "هذه تجربة غير عادلة بسبب تداخل المتغيرات.",
        flaw_tbl_en, flaw_tbl_ar,
    )

    hard_b06 = [
        (
            "A researcher tests seed germination in four petri dishes shown in the table. Which pair of dishes proves that MOISTURE (not warmth alone) is necessary for radish seeds to sprout?",
            "اختبر باحث إنبات بذور الفجل في أربعة أطباق كما في الجدول. أي زوج من الأطباق يثبت أن الرطوبة (وليست الحرارة وحدها) ضرورية لإنبات البذور؟",
            [
                ("Dish A (25°C, Wet) vs. Dish B (25°C, Dry)", "الطبق A (25°م، رطب) مع الطبق B (25°م، جاف)"),
                ("Dish A (25°C, Wet) vs. Dish D (5°C, Dry)", "الطبق A (25°م، رطب) مع الطبق D (5°م، جاف)"),
                ("Dish B (25°C, Dry) vs. Dish D (5°C, Dry)", "الطبق B (25°م، جاف) مع الطبق D (5°م، جاف)"),
                ("Dish C (5°C, Wet) vs. Dish B (25°C, Dry)", "الطبق C (5°م، رطب) مع الطبق B (25°م، جاف)"),
            ],
            "Pick two dishes where Temperature is IDENTICAL and ONLY Moisture differs!",
            "اختر طبقين تتطابق فيهما درجة الحرارة وتختلف الرطوبة فقط!",
            "Pairwise controlled comparison isolates one variable at a time.",
            ["Between Dish A and Dish B, temperature stays fixed at 25°C while moisture switches from Wet (90%) to Dry (0%).", "Comparing A and D changes two things (temp + moisture), proving nothing alone."],
            "Similarly, Dish A vs. Dish C isolates the effect of temperature.",
            "لعزل أثر الرطوبة نختار طبقين لهما نفس الحرارة تماماً.",
            ["في الطبقين A وB تكون الحرارة ثابتة عند 25°م وتختلف الرطوبة فقط (رطب 90% مقابل جاف 0%).", "بينما مقارنة A مع D تغير الحرارة والرطوبة معاً."],
            "وبالمثل، مقارنة A مع C تعزل أثر درجة الحرارة.",
            svg_data_table(["Dish", "Temp", "Water", "Sprout %"], [["A", "25°C", "Wet", "90%"], ["B", "25°C", "Dry", "0%"], ["C", "5°C", "Wet", "5%"], ["D", "5°C", "Dry", "0%"]], "Germination Table", [74, 82, 82, 96]),
            svg_data_table(["الطبق", "الحرارة", "الماء", "الإنبات"], [["A", "25°م", "رطب", "90%"], ["B", "25°م", "جاف", "0%"], ["C", "5°م", "رطب", "5%"], ["D", "5°م", "جاف", "0%"]], "مصفوفة الإنبات", [74, 82, 82, 96]),
        ),
        (
            "Using the same germination table, a student tests ONLY 1 seed per dish instead of 20 seeds per dish. Why would scientists reject the 1-seed trial as unreliable?",
            "في تجربة الإنبات نفسها، لو وضع طالب بذرة واحدة فقط في كل طبق بدلاً من 20 بذرة، فلماذا يرفض العلماء نتائج تجربة البذرة الواحدة بوصفها غير موثوقة؟",
            [
                ("One single seed might happen to be defective or dead by chance, skewing the whole result", "لأن بذرة واحدة قد تكون تالفة أو غير صالحة بالمصادفة فتضلل النتيجة بأكملها"),
                ("Twenty seeds release carbon dioxide that freezes dry dishes", "لأن 20 بذرة تطلق غاز ثاني أكسيد الكربون الذي يجمد الأطباق"),
                ("A single seed cannot absorb liquid water through osmosis", "لأن بذرة واحدة تعجز عن امتصاص الماء السائل بالأسموزية"),
                ("Petri dishes crack unless at least 20 seeds press on the glass", "لأن الأطباق الزجاجية تنكسر ما لم تضغط عليها 20 بذرة"),
            ],
            "Think about why repeated trials and larger sample sizes matter in biology experiments.",
            "فكر لماذا يُعد تكرار المحاولات وكِبر حجم العينة ضروريين في التجارب الحيوية.",
            "Larger sample size reduces random biological variation and error.",
            ["Individual seeds vary slightly in viability.", "Testing 20 seeds per dish gives a reliable germination percentage rather than an all-or-nothing accident."],
            "Repetition and sample size build experimental confidence.",
            "يقلل حجم العينة الكبير أثر المصادفة والتباين الفردي.",
            ["قد تكون إحدى البذور مصابة أو ميتة قبل التجربة.", "استخدام 20 بذرة يعطي نسبة إنبات دقيقة وممثلة بدلاً من الاعتماد على حالة فردية."],
            "التكرار ركيزة أساسية في المنهج العلمي.",
            None, None,
        ),
        (
            "A student measures sunflower height in five daily watering levels and plots the results: 0 mL → 0 cm; 40 mL → 11 cm; 80 mL → 19 cm; 120 mL → 20 cm; 240 mL → 6 cm (rotting). Which conclusion matches ALL five data points accurately?",
            "قاس طالب طول دوار الشمس عند 5 مستويات ري يومية وسجل: 0 مل ← 0 سم؛ 40 مل ← 11 سم؛ 80 مل ← 19 سم؛ 120 مل ← 20 سم؛ 240 مل ← 6 سم (تعفّن). أي استنتاج يتطابق مع جميع النقاط الخمس بدقة؟",
            [
                ("Growth increases with watering up to an optimal range around 80–120 mL, while overwatering (240 mL) harms the plant", "يزداد النمو بزيادة الري حتى مدى أمثل حول 80–120 مل، بينما يضر الإفراط في الري (240 مل) بالنبات"),
                ("The more water you add without limit, the taller a sunflower always grows", "كلما زادت كمية الماء بلا حد ازداد طول دوار الشمس دائماً"),
                ("Sunflowers grow tallest when given 0 mL of daily water", "ينمو دوار الشمس أطول ما يمكن عند منحه 0 مل ماء يومياً"),
                ("240 mL of water doubled the height compared to 120 mL", "ضاعف الري بـ 240 مل الطول مقارنة بـ 120 مل"),
            ],
            "Check what happens at 240 mL! Waterlogged soil suffocates roots.",
            "انتبه لما حدث عند 240 مل! فالماء المفرط يخنق الجذور.",
            "Valid conclusions match the entire data range, including turning points.",
            ["Growth rises steeply from 0 → 80 mL and peaks near 120 mL (20 cm).", "At 240 mL, standing water blocks soil oxygen to roots, cutting growth back to 6 cm."],
            "Do not extrapolate 'more is always better' past the data peak.",
            "الاستنتاج الصحيح يراعي القمة والانخفاض معاً في البيانات.",
            ["يرتفع الطول حتى 80–120 مل ليبلغ 20 سم.", "عند 240 مل يغمر الماء التربة ويمنع تنفس الجذور فيتراجع الطول إلى 6 سم."],
            "إذن يوجد مدى أمثل للري والإفراط ضار كالتقصير.",
            svg_bar_chart([("0 mL", 0, MUTED), ("40 mL", 11, BLUE), ("80 mL", 19, GREEN), ("120 mL", 20, GREEN), ("240 mL", 6, RED)], "Height (cm)", "Water Volume vs Growth"),
            svg_bar_chart([("0 مل", 0, MUTED), ("40 مل", 11, BLUE), ("80 مل", 19, GREEN), ("120 مل", 20, GREEN), ("240 مل", 6, RED)], "الطول (سم)", "الماء مقابل النمو"),
        ),
        (
            "In a desert-adaptation study, two closely related fox species live in different climates: Species X lives in hot Najd dunes (weighs 1.2 kg, huge ears, pale sand coat); Species Y lives in snowy northern tundra (weighs 4.5 kg, tiny ears, thick white coat). Which statement explains BOTH pairs of traits correctly?",
            "تقارن دراسة بيئية نوعين قريبين من الثعالب: النوع X يعيش في رمال نجد الحارة (كتلته 1.2 كجم، أذنان ضخمتان، فراء رملي فاتح)، والنوع Y يعيش في التندرا الثلجية (كتلته 4.5 كجم، أذنان صغيرتان، فراء أبيض كثيف). أي عبارة تفسر الصفتين معاً بدقة؟",
            [
                ("Both colorations camouflage against predators/prey, while X's large ears shed heat and Y's compact ears and larger body retain heat", "الفراء يموه كلاً منهما في بيئته، بينما تبدد أذنا X الواسعتان الحرارة وتحفظ أذنا Y الصغيرتان وجسمه الأكبر الدفء"),
                ("Species X eats snow for water while Species Y absorbs sunlight through white fur", "يأكل النوع X الثلج للشرب بينما يمتص النوع Y الشمس بفرائه الأبيض"),
                ("White fur radiates heat faster than sand-colored fur in freezing winters", "الفراء الأبيض يشع الحرارة أسرع من الفراء الرملي في الشتاء المتجمد"),
                ("Large ears weigh down Species X so it cannot sink into deep snowdrifts", "تثقل الأذنان الكبيرتان النوع X كي لا يغوص في الجليد"),
            ],
            "Analyze both camouflage color AND surface-area heat transfer (radiating vs. conserving heat).",
            "حلّل صفتين معاً: التمويه اللوني، ومساحة السطح لفقدان الحرارة أو حفظها.",
            "Natural selection shapes both camouflage and thermal geometry to each habitat.",
            ["Pale coat blends with desert sand; white coat blends with snow (camouflage).", "Large thin ears + small body dump heat in Najd; tiny ears + compact heavy body + dense fur trap heat in the tundra."],
            "Size/ear rules (Allen's & Bergmann's principles) match thermal physics!",
            "تتوافق الصفات الظاهرية لكل نوع مع متطلبات التمويه والحرارة في موطنه.",
            ["اللون الرملي والأبيض يحققان التمويه في الصحراء والثلج على الترتيب.", "تبدد الأذن الكبيرة الحرارة في الصحراء، بينما تقلل الأذن الصغيرة والجسم المكتنز فقدان الحرارة في البرد."],
            "يمثل ذلك تكيفاً مزدوجاً للبقاء.",
            svg_data_table(["Species", "Mass", "Ears", "Coat"], [["Fox X (Najd)", "1.2 kg", "Huge", "Sand"], ["Fox Y (Arctic)", "4.5 kg", "Tiny", "White"]], "Fox Climate Study", [104, 68, 68, 76]),
            svg_data_table(["النوع", "الكتلة", "الأذن", "الفراء"], [["ثعلب X (نجد)", "1.2 كجم", "كبيرة", "رملي"], ["ثعلب Y (قطب)", "4.5 كجم", "صغيرة", "أبيض"]], "مقارنة تكيف الثعالب", [104, 72, 66, 74]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b06:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


# ==============================================================================
# TOPIC 2: CHEMISTRY & MATTER (G6-SCI-B07 .. G6-SCI-B12, 90 Questions)
# ==============================================================================

def _add_b07(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B07"
    # Easy (0..4): States of matter & phase changes
    easy_b07 = [
        (
            "Solid", "Solid State Particles", "حالة المادة الصلبة",
            "Look at the particle diagram for a solid block of iron. Why does a solid keep BOTH a definite shape and a definite volume?",
            "انظر إلى نموذج الجسيمات في كتلة حديد صلبة. لماذا تحافظ المادة الصلبة على شكل ثابت وحجم ثابت معاً؟",
            [
                ("Its particles are tightly packed in fixed positions and only vibrate in place", "لأن جسيماتها متراصة بقوة في مواضع ثابتة وتهتز في أماكنها فقط"),
                ("Its particles have zero mass and float freely across the container", "لأن جسيماتها عديمة الكتلة وتتحرك بحرية تامة"),
                ("Its particles slide rapidly past one another like flowing water", "لأن جسيماتها تنزلق فوق بعضها مثل الماء الجاري"),
                ("Its particles expand until they fill every corner of a room", "لأن جسيماتها تتمدد لتملأ الغرفة بأكملها"),
            ],
            "Compare the neat grid of touching circles in the Solid box against Liquid and Gas.",
            "قارن ترتيب الجسيمات المتراص في الصندوق الصلب مع السائل والغاز.",
            "Strong attractive forces lock solid particles in fixed positions.",
            ["Particles in solids touch closely and vibrate around fixed spots.", "Because they cannot slide around, solids retain rigid shape and fixed volume."],
            "Heating weakens those bonds until melting occurs.",
            "تحافظ الجسيمات المتقاربة والمقيدة على ثبات الشكل والحجم في الحالة الصلبة.",
            ["تهتز الجسيمات في مواضعها دون أن تغادر مواقعها.", "لذلك يظل الشكل والحجم ثابتين ما لم ترتفع الحرارة إلى درجة الانصهار."],
            "بعكس السوائل والغازات التي تتحرك جسيماتها بمرونة أكبر.",
        ),
        (
            "Liquid", "Liquid State Particles", "حالة المادة السائلة",
            "When 250 mL of milk is poured from a tall narrow bottle into a wide round bowl, its shape changes while its volume stays 250 mL. Why?",
            "عند سكب 250 مل من الحليب من قارورة طويلة إلى وعاء واسع، يتغير شكله بينما يظل حجمه 250 مل ثابتاً. ما سبب ذلك؟",
            [
                ("Liquid particles stay closely packed together (fixed volume) while sliding freely past each other (changing shape)", "تظل جسيمات السائل متقاربة (حجم ثابت) لكنها تنزلق فوق بعضها بسهولة (شكل متغير)"),
                ("Liquid particles spread miles apart to fill the whole kitchen", "تتباعد جسيمات السائل مسافات شاسعة لتملأ الغرفة كلها"),
                ("Liquid particles lock into rigid crystals whenever poured", "تتقيد جسيمات السائل في بلورات صلبة أثناء السكب"),
                ("Milk gains extra water atoms from air to keep its volume constant", "يكتسب الحليب ذرات ماء من الهواء للحفاظ على حجمه"),
            ],
            "Look at the Liquid panel: particles touch one another but are NOT locked in rows.",
            "انظر لصندوق السائل: الجسيمات متقاربة لكنها غير مقيدة في صفوف جامدة.",
            "Liquids have definite volume and indefinite shape due to mobile, closely spaced particles.",
            ["Close spacing keeps a liquid nearly incompressible with fixed volume (250 mL).", "Moderate forces let particles slide past neighbors, taking the bowl's shape."],
            "Only gases expand to change both shape and volume.",
            "تتلاصق جسيمات السائل مع قدرتها على الانزلاق والتدفق.",
            ["التقارب يحفظ الحجم ثابتاً (250 مل)، والانزلاق يسمح بأخذ شكل الإناء.", "أما الغاز فيتغير شكله وحجمه معاً."],
            "تلك هي السمة المميزة للحالة السائلة.",
        ),
        (
            "Gas", "Gas State Particles", "حالة المادة الغازية",
            "Which statement best describes the particle motion and spacing in helium gas inside a party balloon?",
            "أي عبارة تصف بدقة حركة الجسيمات والمسافات بينها في غاز الهيليوم داخل بالون؟",
            [
                ("Particles are far apart and move rapidly in all directions, colliding with each other and the balloon walls", "الجسيمات متباعدة جداً وتتحرك بسرعة عشوائية في كل الاتجاهات متصادمة مع جدران البالون"),
                ("Particles touch tightly in straight lattice rows and vibrate gently", "الجسيمات متلاصقة في صفوف منتظمة وتهتز في مكانها فقط"),
                ("Particles stick to the bottom of the balloon with zero kinetic energy", "الجسيمات مستقرة في قاع البالون بلا طاقة حركية"),
                ("Particles stay frozen in fixed pairs that never collide", "الجسيمات متجمدة في أزواج ثابتة لا تتصادم"),
            ],
            "Check the Gas box: wide empty spaces and fast free movement.",
            "لاحظ صندوق الغاز: مسافات كبيرة فارغة وحركة حرة سريعة.",
            "Gas particles move fast and randomly across wide spaces.",
            ["Weak attractions allow gas particles to separate far apart.", "Continuous high-speed collisions against the balloon's inner wall create gas pressure."],
            "Hence gases expand to fill any closed container completely.",
            "تتحرك جسيمات الغاز بسرعة وعشوائية وتملأ كامل الحيز المتاح.",
            ["تضعف قوى التجاذب بين جسيمات الغاز فتتباعد كثيراً.", "تصطدم باستمرار بجدار البالون فتسبب الضغط وتبقيه منتفخاً."],
            "لذا ليس للغاز شكل ثابت ولا حجم ثابت.",
        ),
        (
            "Liquid", "Evaporation vs Boiling", "التبخر والغليان",
            "Wet laundry dries on a clothesline in Dammam at 34°C even though water does not boil until 100°C. What phase change dries the clothes?",
            "تجف الملابس المبللة على الحبل في الدمام عند حرارة 34°م مع أن الماء لا يغلي إلا عند 100°م. ما التحول الفيزيائي الذي يجفف الملابس؟",
            [
                ("Evaporation — faster surface liquid particles escape into air as water vapor below the boiling point", "التبخر — تفلت الجسيمات الأسرع عند سطح السائل إلى الهواء كبخار ماء دون بلوغ درجة الغليان"),
                ("Condensation — water vapor freezes into solid ice crystals on cloth", "التكثف — يتحول بخار الماء إلى بلورات ثلج على القماش"),
                ("Sublimation — cotton fibers turn directly into nitrogen gas", "التسامي — تتحول ألياف القطن مباشرة إلى غاز النيتروجين"),
                ("Melting — sunlight turns liquid water into solid salt", "الانصهار — يحول ضوء الشمس الماء السائل إلى ملح صلب"),
            ],
            "Unlike boiling (bubbles throughout the liquid at 100°C), surface drying happens slowly at any warm temperature.",
            "على عكس الغليان الذي يحدث في كامل السائل عند 100°م، يحدث هذا التحول عند السطح فقط.",
            "Evaporation is surface vaporization occurring below the boiling temperature.",
            ["Individual liquid molecules near the surface absorb enough energy from warm air to break free as gas.", "Wind blows away humid vapor, speeding up drying."],
            "Boiling occurs throughout the entire volume at 100°C; evaporation happens at the surface at lower temperatures.",
            "التبخر هو تحول السائل إلى غاز من السطح فقط دون درجة الغليان.",
            ["تمتلك بعض جسيمات سطح الماء طاقة كافية للإفلات إلى الهواء عند 34°م.", "تساعد الحرارة والرياح على تسريع عملية التبخر."],
            "بينما يحدث الغليان في أعماق السائل وعند درجة حرارة محددة (100°م).",
        ),
        (
            "Solid", "Dry Ice Sublimation", "تسامي الجليد الجاف",
            "Dry ice (solid carbon dioxide) placed on a lab table shrinks and disappears into colorless CO₂ gas without ever leaving a liquid puddle. What is this direct solid-to-gas change called?",
            "وضع قطعة من الجليد الجاف (ثاني أكسيد الكربون الصلب) على طاولة المختبر يسبب اختفاءها مباشرة إلى غاز دون أن تترك بركة ماء سائلة. ما اسم هذا التحول المباشر من صلب إلى غاز؟",
            [
                ("Sublimation", "التسامي"),
                ("Condensation", "التكثف"),
                ("Freezing", "التجمد"),
                ("Deposition", "الترسب"),
            ],
            "It skips the liquid state completely going straight from solid to gas!",
            "يتخطى الحالة السائلة تماماً وينتقل مباشرة من الصلب إلى الغاز!",
            "Sublimation is the direct phase transition from solid to gas.",
            ["At normal room pressure, solid CO₂ absorbs heat and passes straight into gas.", "The reverse process (gas directly to solid frost) is deposition."],
            "Dry ice stays 'dry' because no liquid phase forms at 1 atm.",
            "التسامي تحول مباشر من الحالة الصلبة إلى الحالة الغازية دون المرور بالسائل.",
            ["يمتص الجليد الجاف الحرارة عند الضغط الجوي العادي ويتحول مباشرة إلى غاز CO₂.", "لذلك لا يترك أي أثر سائل خلفه."],
            "وعكسه هو الترسب (من غاز إلى صلب مباشرة).",
        ),
    ]
    for hi, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in easy_b07:
        den, dar = _states_svgs(hi, ten, tar)
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Diffusion, compressibility, condensation, thermal expansion, surface area
    med_b07 = [
        (
            "Gas", "Gas Diffusion", "انتشار الغازات",
            "A teacher sprays a small burst of rose perfume in one corner of a calm classroom, and within 30 seconds students in the opposite corner smell it. Which particle behavior explains this?",
            "رشّ معلم رذاذاً خفيفاً من عطر الورد في زاوية صف ساكن، وبعد 30 ثانية شمّ الطلاب في الزاوية المقابلة الرائحة. أي سلوك للجسيمات يفسر ذلك؟",
            [
                ("Gas particles move continuously in rapid random motion and diffuse through spaces between air molecules", "تتحرك جسيمات الغاز عشوائياً وبسرعة وتنتشر عبر الفراغات بين جزيئات الهواء"),
                ("Perfume particles melt the classroom air into liquid streams", "تذيب جسيمات العطر هواء الصف وتحوله إلى تيارات سائلة"),
                ("Room lights push fragrance drops horizontally with gravity", "تدفع إضاءة الصف قطرات العطر أفقياً بالجاذبية"),
                ("Sound waves carry solid perfume crystals across the ceiling", "تحمل الموجات الصوتية بلورات العطر الصلبة عبر السقف"),
            ],
            "Notice the large empty gaps between gas molecules shown in the particle model.",
            "لاحظ الفراغات الواسعة بين جزيئات الغاز التي تسمح بالتداخل والانتشار.",
            "Diffusion results from random high-speed motion of gas particles.",
            ["Perfume vapor particles collide elastically with N₂ and O₂ air molecules.", "Random thermal motion spreads the scent from high concentration toward low concentration throughout the room."],
            "Warmer rooms speed up diffusion because particles move faster.",
            "الانتشار ناتج عن الحركة العشوائية السريعة لجسيمات الغاز.",
            ["تتصادم جزيئات بخار العطر مع جزيئات الهواء وتندفع في جميع الاتجاهات.", "فتنتقل من التركيز المرتفع إلى التركيز المنخفض لتملأ الصف."],
            "كلما ارتفعت درجة الحرارة زادت سرعة الانتشار.",
            True,
        ),
        (
            "Liquid", "Compressibility Test", "قابلية الانضغاط",
            "A student seals the tip of a plastic syringe filled with 40 mL of air and easily pushes the plunger down to 20 mL. When she repeats this with 40 mL of liquid water, the plunger barely moves at all. Why?",
            "أغلقت طالبة فوهة محقن مملوء بـ 40 مل من الهواء فضغطت المكبس بسهولة إلى 20 مل، لكنها عندما ملأت المحقن بـ 40 مل ماء لم يتحرك المكبس تقريباً. لماذا؟",
            [
                ("Air particles have large empty spaces to squeeze closer, whereas water particles already touch closely", "لأن بين جسيمات الهواء فراغات واسعة يمكن تقليصها، بينما جسيمات الماء متلاصقة أصلاً"),
                ("Water molecules are made of solid iron atoms", "لأن جزيئات الماء تتكون من ذرات حديد صلبة"),
                ("Air turns into oxygen gas that leaks through solid plastic", "لأن الهواء يتحول إلى أكسجين يتسرب عبر البلاستيك"),
                ("Water has zero mass and pushes back harder than gravity", "لأن الماء بلا كتلة ويدفع للأعلى بقوة"),
            ],
            "Compare how much empty room exists between particles in a Gas vs. a Liquid!",
            "قارن مقدار الفراغ بين الجسيمات في صندوق الغاز مقابل صندوق السائل!",
            "Gases are compressible due to wide spacing; liquids and solids are virtually incompressible.",
            ["Gas molecules occupy tiny volume relative to the empty space separating them.", "Pushing the plunger compresses those gaps, whereas touching liquid particles strongly resist being forced closer."],
            "Hydraulic brakes rely on incompressible liquids!",
            "انضغاط الغازات ممكن لوجود مسافات شاسعة بين جزيئاتها.",
            ["في المحقن الهوائي تتقارب الجسيمات المتباعدة بسهولة.", "أما في الماء فالجسيمات متقاربة جداً ولا توجد فراغات كبيرة لتقليصها."],
            "تُستغل عدم انضغاطية السوائل في المكابح الهيدروليكية.",
            True,
        ),
        (
            "Liquid", "Dew Condensation", "تكثف بخار الماء",
            "On a humid afternoon in Jeddah, tiny beads of liquid water appear on the OUTSIDE surface of a sealed metal bottle filled with ice water. Where did those droplets come from?",
            "في ظهيرة رطبة بمدينة جدة، ظهرت قطرات ماء صغيرة على السطح الخارجي لقارورة معدنية مغلقة مملوءة بماء مثلج. من أين جاءت هذه القطرات؟",
            [
                ("Invisible water vapor gas in humid air cooled on contact with the cold bottle and condensed into liquid", "تكثف بخار الماء غير المرئي الموجود في الهواء الرطب عند ملامسة سطح القارورة البارد"),
                ("Liquid ice water leaked straight through solid steel walls", "تسرب الماء المثلج مباشرة عبر جدران المعدن الصلب"),
                ("Metal atoms combined with sunlight to form new water molecules", "اتحدت ذرات المعدن مع ضوء الشمس لصنع ماء جديد"),
                ("Ice inside sublimated into gas and exited through the cap", "تسامى الجليد من الداخل وخرج عبر الغطاء المغلق"),
            ],
            "The bottle is sealed! The water must come from surrounding humid air losing heat.",
            "القارورة محكمة الإغلاق! إذن الماء أتى من تبريد الهواء الرطب المحيط بها.",
            "Condensation turns gaseous water vapor into liquid water when cooled.",
            ["Warm humid air holds invisible water vapor molecules moving quickly.", "Touching the cold bottle removes thermal energy, slowing vapor molecules until attractions pull them into liquid droplets."],
            "Condensation is the exact reverse of evaporation and releases heat.",
            "التكثف هو تحول بخار الماء الغازي إلى سائل عند فقده للحرارة.",
            ["يحمل هواء جدة الرطب بخار ماء غير مرئي.", "عند ملامسته السطح البارد يفقد طاقته وتتباطأ جزيئاته لتتجمع على شكل قطرات ماء."],
            "القارورة مغلقة ولم يتسرب الماء من داخلها.",
            True,
        ),
        (
            "Solid", "Thermal Expansion", "التمدد الحراري",
            "Engineers leave narrow gaps between sections of outdoor steel bridges in Riyadh so the bridge does not buckle in 48°C summer heat. At the particle level, what actually happens inside the heated steel?",
            "يترك المهندسون فواصل ضيقة بين أجزاء الجسور الفولاذية في الرياض كي لا تلتوي في حرارة الصيف (48°م). على مستوى الجسيمات، ماذا يحدث فعلياً داخل الفولاذ الساخن؟",
            [
                ("Iron particles vibrate faster and push slightly farther apart, increasing total metal volume", "تهتز جسيمات الحديد أسرع وتبتعد قليلاً عن بعضها فيزداد الحجم الكلي للمعدن"),
                ("Individual iron atoms swell up like balloons to twice their diameter", "تنتفخ ذرات الحديد نفسها مثل البالونات ويتضاعف قطرها"),
                ("New iron atoms appear from sunlight inside the bridge girders", "تظهر ذرات حديد جديدة من ضوء الشمس داخل الجسر"),
                ("Steel particles completely melt into liquid puddles every afternoon", "تنصهر جسيمات الفولاذ وتتحول إلى برك سائلة كل ظهر"),
            ],
            "Careful: individual atoms NEVER grow bigger when heated — only the space and vibration between them increase!",
            "انتبه: حجم الذرة الواحدة لا يكبر بالحرارة، بل تتسع المسافة والاهتزاز بين الذرات!",
            "Thermal expansion increases average particle spacing via faster vibration, not particle size.",
            ["Higher temperature increases average kinetic energy (faster atomic vibrations).", "Greater vibration amplitudes push neighboring atoms slightly farther apart, lengthening the steel span."],
            "The mass and number of iron atoms stay completely constant.",
            "يزيد التسخين سرعة اهتزاز الجسيمات فتزداد المسافات البينية دون تغير حجم الذرة.",
            ["ارتفاع الحرارة يزيد الطاقة الحركية لجسيمات الفولاذ فتتسع اهتزازاتها.", "يتباعد الجيران قليلاً فيتمدد الجسر طولياً، وتستوعب فواصل التمدد هذه الزيادة."],
            "أما كتلة الجسر وعدد ذراته فيبقيان ثابتين.",
            False,
        ),
        (
            "Liquid", "Evaporation Surface Area", "مساحة السطح والتبخر",
            "A student pours 100 mL of water into a narrow test tube and another 100 mL of water into a wide shallow dinner plate, placing both side by side on a sunny table. Which container dries first and why?",
            "سكب طالب 100 مل ماء في أنبوب اختبار ضيق و100 مل ماء في طبق مسطح واسع، ووضعهما جنباً إلى جنب على طاولة مشمسة. أيهما يجف أولاً ولماذا؟",
            [
                ("The wide shallow plate dries much faster because far more water molecules are exposed at the air surface", "يجف الطبق الواسع أسرع بكثير لأن عدداً أكبر من جزيئات الماء يكون مكشوفاً على السطح للهواء"),
                ("The narrow test tube dries faster because water is squeezed deeper inside", "يجف الأنبوب الضيق أسرع لأن الماء مضغوط في العمق"),
                ("Both dry at the exact same minute because both hold 100 mL at identical temperature", "يجفان في اللحظة نفسها تماماً لتساوي الحجم والحرارة"),
                ("Neither evaporates below 100°C without an electric stove", "لا يتبخر أي منهما دون 100°م بدون موقد كهربائي"),
            ],
            "Evaporation occurs ONLY at the liquid-air surface boundary!",
            "يحدث التبخر عند السطح المعرض للهواء فقط!",
            "Greater surface area accelerates evaporation at constant temperature.",
            ["Only top-layer molecules can escape into air during evaporation.", "A wide shallow plate exposes several times more surface area than a narrow tube, boosting the escape rate."],
            "Spreading spilled water with a mop dries a floor faster for the same reason.",
            "كلما زادت مساحة السطح المعرض للهواء تسارع التبخر.",
            ["تغادر الجزيئات من السطح فقط، لا من قاع الإناء.", "يمتلك الطبق الواسع مساحة سطح أكبر بكثير من الأنبوب الضيق فتتبخر الجزيئات بمعدل أسرع."],
            "لذلك ننشر الملابس مفرودة على الحبل لتجف سريعاً.",
            False,
        ),
    ]
    for hi, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, show_svg in med_b07:
        den, dar = _states_svgs(hi, ten, tar) if show_svg else (None, None)
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Heating/cooling curves & substance melting/boiling tables
    heat_pts = [(0, -10), (2, 0), (5, 0), (8, 100), (11, 100), (13, 120)]
    B.add_concept(
        tp, "Hard", bp,
        "A block of ice at -10°C is heated steadily on a hot plate and its temperature is plotted over time. Why does the temperature stay completely flat at 0°C (minutes 2–5) and again at 100°C (minutes 8–11) even though the burner keeps adding heat?",
        "سُخّنت قطعة جليد من -10°م بمعدل ثابت ورُسم تغير درجة الحرارة مع الزمن كما في الشكل. لماذا يثبت الخط أفقياً عند 0°م (الدقائق 2–5) وعند 100°م (الدقائق 8–11) رغم استمرار التسخين؟",
        [
            ("During melting and boiling, added heat breaks particle attractions (potential energy) rather than speeding particles up (temperature)", "لأن الحرارة المضافة أثناء الانصهار والغليان تُستهلك في تفكيك قوى الترابط بين الجسيمات لا في زيادة سرعتها (حرارتها)"),
            ("The hot plate automatically switches off every time water hits 0°C or 100°C", "لأن الموقد ينطفئ تلقائياً كلما وصل الماء إلى 0°م أو 100°م"),
            ("Water molecules destroy incoming heat energy while changing state", "لأن جزيئات الماء تفني الطاقة الحرارية أثناء تغير الحالة"),
            ("Thermometers stop working whenever ice and liquid water mix together", "لأن موازين الحرارة تتعطل عند اختلاط الثلج والماء"),
        ],
        "Temperature measures average kinetic energy (speed). During a plateau, energy goes into breaking bonds instead!",
        "تقيس درجة الحرارة متوسط الطاقة الحركية للجسيمات؛ أثناء الثبات تُصرف الطاقة لفك الروابط بين الجسيمات!",
        "Phase-change plateaus absorb latent heat to break intermolecular attractions.",
        ["From min 2–5, ice melts into liquid water at constant 0°C; energy rearranges bonds rather than raising particle speed.", "From min 8–11, liquid water boils into steam at constant 100°C for the same reason."],
        "Once all molecules enter the new phase, temperature resumes climbing.",
        "ثبات الحرارة في منحنى التسخين علامة على تغير حالة المادة.",
        ["عند 0°م تنفك القيود الصلبة ليتحول الجليد إلى ماء (حرارة كامنة للانصهار).", "وعند 100°م تتغلب الجسيمات على التجاذب لتتحول إلى بخار، فتبقى الحرارة ثابتة حتى يكتمل التحول."],
        "بعد تمام التحول تعود درجة الحرارة للارتفاع مجدداً.",
        svg_motion_graph(heat_pts, "Temp (°C)", "Time (min)", "Water Heating Curve"),
        svg_motion_graph(heat_pts, "الحرارة (°م)", "الزمن (د)", "منحنى تسخين الماء"),
    )

    mp_tbl_en = svg_data_table(
        ["Substance", "Melt (°C)", "Boil (°C)"],
        [["Ethanol", "-114", "78"], ["Gallium", "30", "2400"], ["Mercury", "-39", "357"], ["Lead", "327", "1749"]],
        "Melting and Boiling Points",
        [114, 108, 108],
    )
    mp_tbl_ar = svg_data_table(
        ["المادة", "الانصهار (°م)", "الغليان (°م)"],
        [["إيثانول", "-114", "78"], ["غاليوم", "30", "2400"], ["زئبق", "-39", "357"], ["رصاص", "327", "1749"]],
        "درجات الانصهار والغليان",
        [108, 112, 112],
    )
    B.add_concept(
        tp, "Hard", bp,
        "Using the melting and boiling point table, in which state does Ethanol exist at 90°C, and in which state does Gallium exist when held in a warm 37°C hand?",
        "بالاستعانة بجدول درجات الانصهار والغليان، ما الحالة الفيزيائية للإيثانول عند 90°م، وما حالة الغاليوم عند وضعه في يد دافئة حرارتها 37°م على الترتيب؟",
        [
            ("Ethanol is a Gas at 90°C; Gallium is a Liquid at 37°C", "الإيثانول غاز عند 90°م، والغاليوم سائل عند 37°م"),
            ("Ethanol is a Liquid at 90°C; Gallium is a Solid at 37°C", "الإيثانول سائل عند 90°م، والغاليوم صلب عند 37°م"),
            ("Both Ethanol and Gallium are Solids at those temperatures", "كلاهما في الحالة الصلبة عند تينك الدرجتين"),
            ("Ethanol is a Solid at 90°C; Gallium is a Gas at 37°C", "الإيثانول صلب عند 90°م، والغاليوم غاز عند 37°م"),
        ],
        "Below melting = Solid; between melting and boiling = Liquid; above boiling = Gas!",
        "أقل من الانصهار = صلب؛ بين الانصهار والغليان = سائل؛ أعلى من الغليان = غاز!",
        "Compare the test temperature against each substance's melting and boiling thresholds.",
        ["90°C > 78°C (Ethanol's boiling point), so Ethanol has already boiled into a Gas.", "30°C < 37°C < 2400°C, so Gallium melts cleanly into a shiny Liquid in your palm!"],
        "Mercury (-39 to 357) is also liquid at 37°C, while Lead (mp 327) remains solid.",
        "نقارن درجة الحرارة المعطاة بنقطتي الانصهار والغليان في الجدول.",
        ["درجة 90°م أعلى من غليان الإيثانول (78°م) لذا يكون غازاً.", "أما 37°م فتقع بين انصهار الغاليوم (30°م) وغليانه (2400°م) فينصهر ليصبح سائلاً في راحة اليد."],
        "القاعدة: تحت الانصهار صلب، وبينهما سائل، وفوق الغليان غاز.",
        mp_tbl_en, mp_tbl_ar,
    )

    cool_pts = [(0, 85), (2, 62), (6, 62), (9, 30)]
    B.add_concept(
        tp, "Hard", bp,
        "Molten candle wax cools in a beaker and its temperature is recorded on the cooling curve. What happens to the wax particles during the horizontal plateau at 62°C (minutes 2–6)?",
        "تبرد كتلة شمع منصهر في كأس، ورُصدت حرارتها في منحنى التبريد. ماذا يحدث لجسيمات الشمع خلال الثبات الأفقي عند 62°م (الدقائق 2–6)؟",
        [
            ("Wax freezes from liquid to solid while releasing latent heat as particles lock into ordered positions", "يتجمد الشمع من سائل إلى صلب مطلقاً حرارة كامنة بينما تتقيد الجسيمات في مواضع منتظمة"),
            ("Wax boils into gas at 62°C while absorbing cooling energy", "يغلي الشمع متحولاً إلى غاز عند 62°م"),
            ("No heat leaves the beaker between minute 2 and minute 6", "لا تفقد الكأس أي حرارة بين الدقيقة 2 والدقيقة 6"),
            ("Liquid wax turns into pure water vapor at 62°C", "يتحول الشمع السائل إلى بخار ماء نقي عند 62°م"),
        ],
        "Cooling a liquid reverses melting: freezing at 62°C releases heat to the room, temporarily keeping temperature steady.",
        "تبريد السائل يعكس الانصهار: التجمد عند 62°م يحرر طاقة حرارية للغرفة فيؤخر هبوط الحرارة مؤقتاً.",
        "Freezing plateaus occur when liquid-to-solid bond formation releases latent thermal energy.",
        ["At 62°C (the freezing/melting point of wax), liquid wax solidifies.", "Bonding releases heat at the same rate the room cools the beaker, flattening the curve until all wax is solid."],
        "Melting point and freezing point of a pure substance are the exact same temperature (62°C).",
        "نقطة التجمد تساوي نقطة الانصهار للمادة النقية وتصاحبها فترة ثبات حراري.",
        ["عند 62°م تبدأ جسيمات الشمع السائل بالترابط لتكوين الحالة الصلبة.", "تطلق عملية الترابط حرارة تعوض التبريد حتى يتصلب الشمع كله عند الدقيقة 6."],
        "بعد اكتمال التجمد تستمر درجة حرارة الشمع الصلب في الانخفاض.",
        svg_motion_graph(cool_pts, "Temp (°C)", "Time (min)", "Wax Cooling Curve"),
        svg_motion_graph(cool_pts, "الحرارة (°م)", "الزمن (د)", "منحنى تبريد الشمع"),
    )

    hard_b07 = [
        (
            "In high-altitude Abha (~2,200 m above sea level), pure water boils in an open pot around 93°C instead of 100°C at Jeddah's sea-level coast. Why?",
            "في مدينة أبها المرتفعة (~2200 م فوق سطح البحر)، يغلي الماء النقي في قدر مكشوف عند نحو 93°م بدلاً من 100°م على ساحل جدة. ما السبب؟",
            [
                ("Lower atmospheric air pressure at high elevation makes it easier for vapor bubbles to push upward and boil at a lower temperature", "انخفاض الضغط الجوي في المرتفعات يسهّل تشكل فقاعات البخار وصعودها فتغلي المياه عند درجة حرارة أقل"),
                ("Mountain sunlight cools water molecules faster than coastal sunlight", "ضوء الشمس الجبلي يبرّد جزيئات الماء أسرع"),
                ("Water molecules weigh less in Abha so their mass drops to zero", "جزيئات الماء تفقد كتلتها في أبها وتقترب من الصفر"),
                ("High-altitude water lacks oxygen atoms inside H₂O", "ماء المرتفعات يفتقر لذرات الأكسجين داخل جزيء H₂O"),
            ],
            "Boiling happens when vapor pressure inside bubbles equals the surrounding air pressure pushing down on the liquid surface.",
            "يحدث الغليان عندما يتعادل ضغط البخار داخل السائل مع الضغط الجوي الضاغط على سطحه.",
            "Lower atmospheric pressure lowers a liquid's boiling point.",
            ["At sea level (1 atm), water requires 100°C for vapor bubbles to overcome air pressure.", "In Abha, thinner air exerts less downward pressure, so bubbles form and burst freely at 93°C."],
            "That is why pressure cookers raise pressure inside the pot to cook food faster above 100°C!",
            "تتأثر درجة الغليان مباشرة بالضغط الجوي المحيط.",
            ["في أبها يكون عمود الهواء فوق القدر أقل وزناً وضغطاً مقارنة بساحل جدة.", "لذا تتغلب فقاعات البخار على الضغط الجوي عند 93°م فقط."],
            "وعلى العكس، ترفع قدور الضغط درجة الغليان لتسريع الطهي.",
            None, None,
        ),
        (
            "Two identical 10 g ice cubes at 0°C are placed on two room-temperature (23°C) surfaces: one on a thick aluminum metal block and one on a wooden cutting board. After 2 minutes, the ice on aluminum has almost completely melted, while the ice on wood is barely wet. Why?",
            "وُضع مكعبان متماثلان من الجليد كتلة كل منهما 10 جم عند 0°م في غرفة حرارتها 23°م: الأول على لوح ألمنيوم سميك، والثاني على لوح خشبي. بعد دقيقتين انصهر الجليد على الألمنيوم بالكامل تقريباً بينما بالكاد ذاب على الخشب. لماذا؟",
            [
                ("Aluminum is a good thermal conductor that transfers room heat into the ice much faster than insulating wood", "الألمنيوم موصل حراري جيد ينقل الحرارة إلى الجليد أسرع بكثير من الخشب العازل"),
                ("Aluminum cools the ice below -20°C so it turns directly into water", "يبرد الألمنيوم الجليد إلى -20°م فيتحول إلى ماء"),
                ("Wood absorbs melted liquid water back inside solid wood grains instantly", "يمتص الخشب الماء الذائب فور تكونه"),
                ("The aluminum block generates chemical flames underneath the ice cube", "يولد لوح الألمنيوم تفاعلاً نارياً تحت المكعب"),
            ],
            "Both surfaces start at 23°C! Which property governs how quickly heat flows into the 0°C ice?",
            "كلا اللوحين حرارته 23°م! ما الخاصية التي تحدد سرعة تدفق الحرارة إلى الجليد؟",
            "Thermal conductivity determines how rapidly heat flows to drive melting.",
            ["Heat flows from 23°C surface into 0°C ice.", "Free electrons in metal aluminum conduct heat rapidly, supplying the latent heat of melting far sooner than wood."],
            "Even though aluminum feels colder to your hand, it actually conducts heat fastest!",
            "تعتمد سرعة الانصهار على التوصيل الحراري للسطح الملامس.",
            ["ينقل الألمنيوم (معدن) الطاقة الحرارية من الغرفة إلى الجليد بسرعة فائقة.", "أما الخشب فعازل حراري بطيء التوصيل فتأخر انصهار المكعب فوقه."],
            "تبقى درجة الجليد 0°م أثناء الانصهار في الحالتين.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b07:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b08(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B08"
    # Easy (0..4): Instruments, D=m/V basic math, displacement principle
    B.add_concept(
        tp, "Easy", bp,
        "A student needs to find the density of a small irregularly shaped quartz pebble. Which pair of laboratory tools must she use to measure its mass and volume?",
        "تريد طالبة إيجاد كثافة حصاة كوارتز صغيرة غير منتظمة الشكل. أي زوج من أدوات المختبر يلزمها لقياس كتلة الحصاة وحجمها؟",
        [
            ("A balance scale for mass (g) and a water-filled graduated cylinder for displacement volume (mL or cm³)", "ميزان لقياس الكتلة (جم) ومخبار مدرج مملوء بالماء لقياس الحجم بالإزاحة (مل أو سم³)"),
            ("A thermometer for mass and a barometer for volume", "مقياس حرارة للكتلة وبارومتر للحجم"),
            ("A ruler for mass and litmus paper for volume", "مسطرة للكتلة وورق تباع الشمس للحجم"),
            ("A stopwatch for mass and a magnet for volume", "ساعة إيقاف للكتلة ومغناطيس للحجم"),
        ],
        "Mass is measured on a balance; irregular volume is measured by water displacement.",
        "تُقاس الكتلة بالميزان، ويُقاس حجم الأجسام غير المنتظمة بإزاحة الماء في المخبار المدرج.",
        "Density D = m / V requires measuring mass and volume accurately.",
        ["Read mass in grams on a digital or triple-beam balance.", "Submerge the pebble in a graduated cylinder and subtract initial water volume from final volume (1 mL = 1 cm³)."],
        "A ruler alone only works for simple rectangular boxes, not irregular pebbles.",
        "تحتاج لحساب الكثافة إلى معرفة الكتلة والحجم.",
        ["نستخدم الميزان لقياس الكتلة بالجرام.", "ونستخدم المخبار المدرج والماء لقياس حجم الحصاة غير المنتظمة بالإزاحة (1 مل = 1 سم³)."],
        "ثم نقسم الكتلة على الحجم للحصول على الكثافة.",
        svg_graduated_cylinder(40, 65, 75, 100, "Before", "After", "Mass", "Displacement Check"),
        svg_graduated_cylinder(40, 65, 75, 100, "قبل", "بعد", "الكتلة", "قياس الحجم بالإزاحة"),
    )

    easy_math_b08 = [
        (54, 18, 3, [2, 6, 36], "aluminum sample", "عينة ألمنيوم"),
        (120, 15, 8, [5, 10, 105], "steel bolt", "برغي فولاذي"),
        (96, 12, 8, [4, 12, 84], "copper cube", "مكعب نحاسي"),
    ]
    for m_g, v_cm3, d_ans, dists, obj_en, obj_ar in easy_math_b08:
        B.add_math(
            tp, "Easy", bp,
            f"A solid {obj_en} has a mass of {m(m_g)} g and a volume of {m(v_cm3)} cm³. What is its density in g/cm³?",
            f"كتلة {obj_ar} صلب {m(m_g)} جم وحجمه {m(v_cm3)} سم³. ما كثافته بوحدة جم/سم³؟",
            d_ans, dists,
            "Use the density formula: Density = Mass ÷ Volume (D = m / V).",
            "استعمل قانون الكثافة: الكثافة = الكتلة ÷ الحجم.",
            "Density equals mass divided by volume.",
            [f"Identify values: m = {m_g} g, V = {v_cm3} cm³.", f"Divide: D = {m_g} ÷ {v_cm3} = {d_ans} g/cm³."],
            f"{d_ans} × {v_cm3} = {m_g} g.",
            "نحسب الكثافة بقسمة الكتلة على الحجم.",
            [f"الكتلة = {m_g} جم، والحجم = {v_cm3} سم³.", f"الكثافة = {m_g} ÷ {v_cm3} = {d_ans} جم/سم³."],
            f"تحقق: {d_ans} × {v_cm3} = {m_g} جم.",
        )

    B.add_math(
        tp, "Easy", bp,
        "A wooden rectangular block measures 4 cm long, 3 cm wide, and 2 cm tall, and has a mass of 48 g. What is the density of the wood in g/cm³?",
        "متوازي مستطيلات خشبي أبعاده 4 سم طولاً، و3 سم عرضاً، و2 سم ارتفاعاً، وكتلته 48 جم. ما كثافة هذا الخشب بوحدة جم/سم³؟",
        2, [4, 8, 24],
        "First find Volume = L × W × H, then compute Density = Mass ÷ Volume.",
        "احسب الحجم أولاً (الطول × العرض × الارتفاع)، ثم اقسم الكتلة على الحجم.",
        "Combine box volume V = L × W × H with density D = m / V.",
        ["Volume V = 4 × 3 × 2 = 24 cm³.", "Density D = 48 ÷ 24 = 2 g/cm³."],
        "2 × 24 = 48 g.",
        "نوجد حجم متوازي المستطيلات ثم نقسم الكتلة على الحجم.",
        ["الحجم = 4 × 3 × 2 = 24 سم³.", "الكثافة = 48 ÷ 24 = 2 جم/سم³."],
        "تحقق: 2 × 24 = 48 جم.",
    )

    # Medium (5..9): Displacement SVGs, solving for m or V, floating vs sinking table
    med_disp_b08 = [
        (35, 60, 100, 4, [2, 3, 25], "granite stone", "حجر جرانيت"),
        (42, 72, 150, 5, [3, 6, 30], "iron mineral", "عينة معدن حديد"),
    ]
    for v1, v2, mg, ans_d, dists, obj_en, obj_ar in med_disp_b08:
        dv = v2 - v1
        den = svg_graduated_cylinder(v1, v2, mg, 100, "Before", "After", "Mass", "Water Displacement")
        dar = svg_graduated_cylinder(v1, v2, mg, 100, "قبل", "بعد", "الكتلة", "الإزاحة والكتلة")
        B.add_math(
            tp, "Medium", bp,
            f"A {obj_en} of mass {mg} g is gently lowered into a graduated cylinder containing {v1} mL of water. The water level rises to {v2} mL as shown. What is the density of the {obj_en} in g/cm³?",
            f"غُمرت {obj_ar} كتلتها {mg} جم في مخبار مدرج يحتوي على {v1} مل من الماء فارتفع مستوى الماء إلى {v2} مل كما في الرسم. ما كثافة العينة بوحدة جم/سم³؟",
            ans_d, dists,
            "Find object volume first by subtracting V_initial from V_final (1 mL = 1 cm³), then divide Mass by Volume.",
            "احسب حجم الجسم أولاً بطرح الحجم الابتدائي من النهائي (1 مل = 1 سم³)، ثم اقسم الكتلة على الحجم.",
            "Water displacement yields volume V = V_final - V_initial.",
            [f"Displaced volume V = {v2} - {v1} = {dv} mL = {dv} cm³.", f"Density D = {mg} ÷ {dv} = {ans_d} g/cm³."],
            f"{ans_d} × {dv} = {mg} g.",
            "الحجم المزاح يساوي حجم الجسم المغمور تماماً.",
            [f"الحجم = {v2} − {v1} = {dv} مل = {dv} سم³.", f"الكثافة = {mg} ÷ {dv} = {ans_d} جم/سم³."],
            f"تحقق: {ans_d} × {dv} = {mg} جم.",
            "", den, dar,
        )

    B.add_math(
        tp, "Medium", bp,
        "Brass has a density of 8 g/cm³. What is the mass in grams of a solid brass ornament whose volume is 14 cm³?",
        "تبلغ كثافة النحاس الأصفر 8 جم/سم³. ما كتلة قطعة مصمتة من النحاس الأصفر حجمها 14 سم³ بوحدة الجرام؟",
        112, [22, 56, 128],
        "Rearrange D = m / V to solve for mass: m = D × V.",
        "أعد ترتيب قانون الكثافة لإيجاد الكتلة: الكتلة = الكثافة × الحجم.",
        "Mass equals density multiplied by volume.",
        ["Given D = 8 g/cm³ and V = 14 cm³.", "Mass m = 8 × 14 = 112 g."],
        "112 ÷ 14 = 8 g/cm³.",
        "نضرب الكثافة في الحجم لحساب الكتلة.",
        ["الكثافة = 8 جم/سم³، والحجم = 14 سم³.", "الكتلة = 8 × 14 = 112 جم."],
        "تحقق: 112 ÷ 14 = 8 جم/سم³.",
    )
    B.add_math(
        tp, "Medium", bp,
        "A pure silver medal has a mass of 135 g. If silver's density is roughly 9 g/cm³ (rounded for this problem), what volume in cm³ does the medal occupy?",
        "ميدالية فضية كتلتها 135 جم. إذا افترضنا أن كثافة هذا السبيكة 9 جم/سم³، فما حجم الميدالية بوحدة سم³؟",
        15, [12, 18, 126],
        "Rearrange D = m / V to solve for volume: V = m ÷ D.",
        "أعد ترتيب القانون لحساب الحجم: الحجم = الكتلة ÷ الكثافة.",
        "Volume equals mass divided by density.",
        ["Given m = 135 g and D = 9 g/cm³.", "Volume V = 135 ÷ 9 = 15 cm³."],
        "15 × 9 = 135 g.",
        "نقسم الكتلة على الكثافة لإيجاد الحجم.",
        ["الكتلة = 135 جم، والكثافة = 9 جم/سم³.", "الحجم = 135 ÷ 9 = 15 سم³."],
        "تحقق: 15 × 9 = 135 جم.",
    )

    fl_tbl_en = svg_data_table(
        ["Object", "Mass (g)", "Vol (cm³)"],
        [["Cork", "12", "48"], ["Oak", "40", "50"], ["PVC", "70", "50"], ["Slate", "130", "50"]],
        "Density Sink/Float Data",
        [96, 108, 108],
    )
    fl_tbl_ar = svg_data_table(
        ["الجسم", "الكتلة (جم)", "الحجم (سم³)"],
        [["فلين", "12", "48"], ["بلوط", "40", "50"], ["بلاستيك PVC", "70", "50"], ["أردواز", "130", "50"]],
        "بيانات الطفو والغوص",
        [108, 108, 108],
    )
    B.add_concept(
        tp, "Medium", bp,
        "Pure water has a density of 1.0 g/cm³. Based on the mass and volume table, which objects will FLOAT in pure water?",
        "تبلغ كثافة الماء النقي 1.0 جم/سم³. بناءً على جدول الكتلة والحجم الموضح، أي الأجسام ستطفو على سطح الماء النقي؟",
        [
            ("Both Cork (0.25 g/cm³) and Oak (0.80 g/cm³)", "الفلين (0.25 جم/سم³) والبلوط (0.80 جم/سم³) كلاهما يطفو"),
            ("Only Cork (0.25 g/cm³) while Oak sinks", "الفلين فقط يطفو بينما يغوص البلوط"),
            ("PVC (1.40 g/cm³) and Slate (2.60 g/cm³)", "بلاستيك PVC والأردواز كلاهما يطفو"),
            ("Only Oak because 40 g is lighter than 50 g", "البلوط فقط لأن 40 جم أخف من 50 جم"),
        ],
        "Compute D = m ÷ V for all four objects and see which densities are LESS than 1.0 g/cm³!",
        "احسب الكثافة (الكتلة ÷ الحجم) لكل جسم وحدد أيها أقل من 1.0 جم/سم³!",
        "Objects with density < 1.0 g/cm³ float in pure water; > 1.0 g/cm³ sink.",
        ["Cork = 12 ÷ 48 = 0.25 (< 1.0); Oak = 40 ÷ 50 = 0.80 (< 1.0).", "PVC = 70 ÷ 50 = 1.40 (> 1.0); Slate = 130 ÷ 50 = 2.60 (> 1.0). Thus Cork and Oak float!"],
        "Comparing mass alone without volume is a classic density trap.",
        "يطفو الجسم إذا كانت كثافته أقل من كثافة السائل (1.0 جم/سم³).",
        ["كثافة الفلين = 12 ÷ 48 = 0.25، والبلوط = 40 ÷ 50 = 0.80 (أقل من 1.0 ← يطفوان).", "كثافة PVC = 1.40 والأردواز = 2.60 (أكبر من 1.0 ← يغوصان)."],
        "الطفو يعتمد على الكثافة وليس على الكتلة وحدها.",
        fl_tbl_en, fl_tbl_ar,
    )

    # Hard (10..14): Intensive property cutting, density layers, steel ship, saltwater egg, alloy math
    B.add_math(
        tp, "Hard", bp,
        "A uniform solid metal bar has a mass of 240 g and a volume of 30 cm³ (density = 8 g/cm³). A technician saws the bar into 3 identical smaller blocks of 10 cm³ each. What is the density in g/cm³ of ONE small block?",
        "قضيب معدني منتظم صلب كتلته 240 جم وحجمه 30 سم³ (كثافته 8 جم/سم³). قصّه فني إلى 3 قطع صغيرة متطابقة حجم كل منها 10 سم³. ما كثافة القطعة الواحدة بوحدة جم/سم³؟",
        8, [2.67, 24, 80],
        "Does cutting a uniform substance change the ratio of mass to volume, or do BOTH mass and volume divide by 3?",
        "هل تقطيع مادة متجانسة يغير نسبة الكتلة إلى الحجم أم ينقسم كلٌّ من الكتلة والحجم على 3؟",
        "Density is an intensive physical property independent of sample size.",
        ["Each 10 cm³ piece gets 1/3 of the mass: m = 240 ÷ 3 = 80 g.", "Density of one piece = 80 ÷ 10 = 8 g/cm³ — identical to the original bar!"],
        "Every uniform piece of pure brass or iron shares the exact same density.",
        "الكثافة خاصية مميزة للمادة لا تتغير بتغيير حجم العينة.",
        ["تنقسم الكتلة أيضاً على 3 لتصبح كتلة القطعة 240 ÷ 3 = 80 جم.", "كثافة القطعة = 80 ÷ 10 = 8 جم/سم³ وهي مطابقة للأصل."],
        "الكتلة والحجم يتناسبان طردياً فتظل النسبة بينهما ثابتة.",
    )

    col_tbl_en = svg_data_table(
        ["Liquid", "Density (g/cm³)"],
        [["Rubbing Alcohol", "0.7"], ["Cooking Oil", "0.8"], ["Pure Water", "1.0"], ["Corn Syrup", "1.4"]],
        "4-Layer Density Column",
        [170, 148],
    )
    col_tbl_ar = svg_data_table(
        ["السائل", "الكثافة (جم/سم³)"],
        [["كحول طبي", "0.7"], ["زيت طعام", "0.8"], ["ماء نقي", "1.0"], ["شراب ذرة", "1.4"]],
        "عمود الكثافة الرباعي",
        [170, 148],
    )
    B.add_concept(
        tp, "Hard", bp,
        "Four non-mixing liquids are layered from least dense on top to most dense on bottom as shown. Where will a solid plastic bead (mass = 36 g, volume = 40 cm³) settle if dropped gently into the cylinder?",
        "صُبّت أربعة سوائل غير ممتزجة في مخبار فترتبت من الأقل كثافة بالأعلى إلى الأعلى كثافة بالأسفل. أين ستستقر خرزة بلاستيكية صلبة كتلتها 36 جم وحجمها 40 سم³ عند إسقاطها برفق؟",
        [
            ("Between Cooking Oil and Pure Water (sinks through 0.8 oil, floats atop 1.0 water)", "بين زيت الطعام والماء النقي (تغوص في الزيت 0.8 وتطفو فوق الماء 1.0)"),
            ("Floating on the very top surface of Rubbing Alcohol (0.7)", "تطفو على السطح العلوي للكحول الطبي (0.7)"),
            ("Resting on the glass bottom beneath Corn Syrup (1.4)", "تستقر في قاع المخبار تحت شراب الذرة (1.4)"),
            ("Suspended exactly between Rubbing Alcohol and Cooking Oil", "تستقر بين الكحول الطبي وزيت الطعام"),
        ],
        "Calculate bead density D = 36 ÷ 40 = 0.9 g/cm³, then bracket 0.9 between adjacent liquid densities!",
        "احسب أولاً كثافة الخرزة: 36 ÷ 40 = 0.9 جم/سم³، ثم قارنها بكثافات السوائل الأربعة!",
        "An object sinks through less-dense layers and floats on the first denser layer below.",
        ["Bead density = 36 ÷ 40 = 0.9 g/cm³.", "0.9 > 0.7 (sinks through alcohol) and 0.9 > 0.8 (sinks through oil), but 0.9 < 1.0 (floats on water!)."],
        "So it rests right at the oil–water interface!",
        "يغوص الجسم في السوائل الأقل منه كثافة ويطفو فوق السائل الأعلى منه كثافة.",
        ["كثافة الخرزة = 36 ÷ 40 = 0.9 جم/سم³.", "بما أن 0.9 أكبر من الكحول (0.7) والزيت (0.8) وأصغر من الماء (1.0)، فإنها تستقر بين الزيت والماء."],
        "أي تغوص عبر الزيت وتطفو فوق طبقة الماء.",
        col_tbl_en, col_tbl_ar,
    )

    hard_b08 = [
        (
            "Solid steel has a density of 7.8 g/cm³ and sinks rapidly in seawater (1.03 g/cm³). Why, then, does a 10,000-ton cargo ship built out of steel plates float safely on the Red Sea?",
            "تبلغ كثافة الفولاذ المصمت 7.8 جم/سم³ ويغوص فوراً في مياه البحر (1.03 جم/سم³). فلماذا تطفو سفينة شحن ضخمة مصنوعة من الفولاذ بسلام على مياه البحر الأحمر؟",
            [
                ("The hollow hull traps a huge volume of low-density air, making the ship's overall average density less than 1.03 g/cm³", "لأن الهيكل المجوف للسفينة يحجز حجماً هائلاً من الهواء قليل الكثافة فتصبح الكثافة المتوسطة للسفينة أقل من 1.03 جم/سم³"),
                ("Painting the steel hull white reduces steel's atomic density below zero", "لأن طلاء الفولاذ باللون الأبيض يقلل الكثافة الذرية للفولاذ إلى الصفر"),
                ("Saltwater freezes into solid ice beneath wide ship hulls", "لأن مياه البحر تتجمد تحت الهياكل العريضة"),
                ("Ship propellers push water upward faster than gravity pulls steel down", "لأن مراوح السفينة تدفع الماء للأعلى باستمرار لتعويمها حتى عند التوقف"),
            ],
            "Compute AVERAGE density = (steel mass + air mass) ÷ (total enclosed hull volume).",
            "فكر في متوسط الكثافة الكلي = (كتلة الفولاذ + الهواء) ÷ (الحجم الكلي للهيكل المجوف).",
            "Hollow shaping raises displaced water volume so average density drops below water's density.",
            ["A solid steel lump has tiny volume for its huge mass (7.8 g/cm³ → sinks).", "Shaping that steel into a wide hollow bowl increases total volume dramatically with mostly air inside, dropping average density well below 1.03 g/cm³."],
            "If water floods the hull and replaces the air, average density exceeds 1.03 and the ship sinks.",
            "يعتمد الطفو على متوسط كثافة الجسم الكلي مقارنة بكثافة الماء.",
            ["يحتوي جسم السفينة المجوف على حيز كبير من الهواء خفيف الكتلة.", "يرتفع الحجم الكلي للسفينة بشدة فتقل متوسط كثافتها عن 1.03 جم/سم³ وتطفو."],
            "لذلك تغرق السفينة إذا تسرّب الماء وملأ تجاويفها بدلاً من الهواء.",
            None, None,
        ),
        (
            "A fresh chicken egg (density ≈ 1.05 g/cm³) sinks to the bottom of a beaker of pure water (1.00 g/cm³). After stirring 50 g of table salt into the water until dissolved, the egg rises and floats near the surface. Why?",
            "تغوص بيضة دجاج طازجة (كثافتها 1.05 جم/سم³) إلى قاع كأس بها ماء نقي (1.00 جم/سم³). وبعد إذابة 50 جم من ملح الطعام في الماء ترتفع البيضة وتطفو. ما التفسير العلمي؟",
            [
                ("Dissolved salt increases water mass markedly with little volume change, raising solution density above 1.05 g/cm³", "تزيد ذرات الملح المذابة كتلة الماء بشكل ملحوظ مع تغير طفيف في الحجم، فترتفع كثافة المحلول فوق 1.05 جم/سم³"),
                ("Table salt dissolves inside the egg shell and turns egg white into gas", "يذيب الملح داخل القشرة بياض البيض ويحوله إلى غاز"),
                ("Salt crystals push upward physically like invisible springs under the egg", "تدفع بلورات الملح البيضة للأعلى مثل نوابض خفية"),
                ("Stirring drops the egg's mass to half its original grams", "يقلل التحريك كتلة البيضة إلى النصف"),
            ],
            "Compare solution density (mass of water + salt) / volume against egg density (1.05 g/cm³)!",
            "قارن كثافة المحلول الملحي (كتلة الماء + الملح ÷ الحجم) بكثافة البيضة (1.05 جم/سم³)!",
            "Dissolving solute raises liquid density; when liquid density exceeds object density, the object floats.",
            ["Salt ions pack into spaces between water molecules, adding 50 g of mass with tiny volume increase.", "Solution density climbs (e.g., to ~1.12 g/cm³), exceeding 1.05 g/cm³, so the egg floats!"],
            "This also explains why swimmers float so easily in the salty Dead Sea.",
            "تزداد كثافة السائل بإذابة الملح فيه مما يرفع قوة الطفو.",
            ["تملأ أيونات الملح المسافات البينية بين جزيئات الماء فتزداد الكتلة أكثر من زيادة الحجم.", "تصبح كثافة المحلول أعلى من 1.05 جم/سم³ فتطفو البيضة."],
            "وهذا نفس سبب سهولة الطفو في البحار عالية الملوحة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b08:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "A technician combines 90 g of Metal A (volume = 10 cm³) with 110 g of Metal B (volume = 15 cm³) into a composite block of total volume 25 cm³. What is the overall average density of the composite block in g/cm³?",
        "دمج فني 90 جم من المعدن A (حجمه 10 سم³) مع 110 جم من المعدن B (حجمه 15 سم³) لصنع سبيكة حجمها الكلي 25 سم³. ما متوسط كثافة السبيكة الكلية بوحدة جم/سم³؟",
        8, [7, 9, 10],
        "Add total mass (90 + 110) and divide by total volume (10 + 15). Do NOT simply average 9 and 7.33!",
        "اجمع الكتلة الكلية (90 + 110) واقسمها على الحجم الكلي (10 + 15).",
        "Average composite density = Total Mass ÷ Total Volume.",
        ["Total mass = 90 + 110 = 200 g.", "Total volume = 10 + 15 = 25 cm³. Average density = 200 ÷ 25 = 8 g/cm³."],
        "8 × 25 = 200 g.",
        "متوسط الكثافة الكلي = مجموع الكتل ÷ مجموع الحجوم.",
        ["الكتلة الكلية = 90 + 110 = 200 جم، والحجم الكلي = 10 + 15 = 25 سم³.", "متوسط الكثافة = 200 ÷ 25 = 8 جم/سم³."],
        "تحقق: 8 × 25 = 200 جم.",
    )


def _add_b09(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B09"
    # Easy (0..4): Physical vs chemical changes & conservation of mass
    easy_b09 = [
        (
            "Which everyday event is a PHYSICAL change where no new chemical substance is formed?",
            "أي حدث يومي مما يلي يمثل تغيراً فيزيائياً لا تتكون فيه مادة كيميائية جديدة؟",
            [
                ("Hammering a sheet of aluminum foil into a flat tray", "طرق صفيحة ألمنيوم لتشكيل طبق مسطح"),
                ("An iron garden gate rusting in humid coastal air", "صدأ بوابة حديدية في الهواء الساحلي الرطب"),
                ("Dry firewood burning into gray ash and smoke", "احتراق الحطب وتحوله إلى رماد ودخان"),
                ("Fresh milk turning sour after three warm days", "فساد الحليب الطازج وتغير طعمه بعد ثلاثة أيام"),
            ],
            "Shaping, cutting, bending, or melting only alters appearance or state, not molecular identity.",
            "التشكيل أو القص أو الثني أو الانصهار يغير الشكل أو الحالة فقط دون تركيب المادة.",
            "Physical changes alter form or state while keeping chemical composition identical.",
            ["Aluminum remains aluminum atoms before and after hammering.", "Rusting, burning, and souring all create brand-new chemical substances."],
            "Malleability (bending/hammering metal) is a physical property.",
            "التغير الفيزيائي يحافظ على نوع المادة الأصلية دون إنتاج مادة جديدة.",
            ["يبقى الألمنيوم ألمنيوماً بعد الطرق وتغير الشكل فقط.", "أما الصدأ والاحتراق وفساد الحليب فتغيرات كيميائية تنتج مواد جديدة."],
            "الطرق والسحب والتشكيل تغيرات فيزيائية.",
            None, None,
        ),
        (
            "When an iron nail sits outside in the rain for several weeks, reddish-brown flaky rust (iron oxide) coats its surface. Why is rusting classified as a CHEMICAL change?",
            "عند ترك مسمار حديدي في المطر أسابيع عدة تتكون عليه قشرة هشة بنية محمرة هي الصدأ (أكسيد الحديد). لماذا يُصنف الصدأ تغيراً كيميائياً؟",
            [
                ("Iron atoms chemically react with oxygen and moisture to form a brand-new compound with different properties", "لأن ذرات الحديد تتفاعل كيميائياً مع الأكسجين والرطوبة لتكوين مركب جديد له خصائص مختلفة"),
                ("Rainwater simply washes shiny silver paint off the iron nail", "لأن ماء المطر يغسل طبقة الطلاء الفضية عن الحديد فقط"),
                ("Cold air turns solid iron temporarily into brown liquid iron", "لأن الهواء البارد يحول الحديد الصلب مؤقتاً إلى سائل بني"),
                ("The iron nail breaks into smaller pure iron crumbs by hammering", "لأن المسمار يتفتت ميكانيكياً إلى فتات حديد نقي"),
            ],
            "Check whether iron oxide can simply be wiped or cooled back into shiny metallic iron.",
            "تحقق هل للصدأ نفس خواص الحديد اللامع القوي أم أنه مادة جديدة هشة غير مغناطيسية.",
            "Rusting creates iron oxide (Fe₂O₃), a new compound different from metallic iron.",
            ["Iron is strong, gray, and magnetic; flaky red rust is brittle and non-magnetic.", "New substance + new properties + irreversibility confirm a chemical change."],
            "Painting or galvanizing iron blocks oxygen and water to prevent rust.",
            "تنشأ في الصدأ مادة جديدة تختلف في خواصها عن الحديد النقي.",
            ["يتحد الحديد مع الأكسجين بوجود الرطوبة مكوناً أكسيد الحديد الهش.", "للمادة الجديدة لون وخواص مختلفة تماماً ولا يعود حديداً بالتبريد أو التجفيف."],
            "لذا يُعد الصدأ تغيراً كيميائياً واضحاً.",
            None, None,
        ),
        (
            "A student stirs 10 g of white table salt into warm water until it vanishes completely into a clear liquid. Why is dissolving salt considered a PHYSICAL change rather than a chemical reaction?",
            "أذاب طالب 10 جم من ملح الطعام الأبيض في ماء دافئ حتى اختفى تماماً في سائل شفاف. لماذا يُعد الذوبان تغيراً فيزيائياً وليس تفاعلاً كيميائياً؟",
            [
                ("Evaporating the water recovers the exact same solid white salt crystals unchanged", "لأن تبخير الماء يعيد استرجاع بلورات الملح البيضاء نفسها دون أي تغير في تركيبها"),
                ("Salt molecules melt into hydrochloric acid and sodium hydroxide", "لأن جزيئات الملح تتحول إلى أحماض وقواعد قوية"),
                ("Bubbles of flammable hydrogen gas escape while stirring", "لأن فقاعات غاز الهيدروجين تشتعل أثناء التقليب"),
                ("Dissolving permanently destroys every sodium and chloride ion", "لأن الذوبان يفني ذرات الصوديوم والكلور نهائياً"),
            ],
            "Ask: can simple physical separation (evaporation) recover the original salt?",
            "اسأل: هل يمكن استعادة الملح الأصلي بعملية فيزيائية بسيطة كالتبخير؟",
            "Dissolving disperses solute particles without altering chemical bonds.",
            ["No new substance forms; salty water still tastes salty and stays clear.", "Boiling off the water leaves behind the exact 10 g of NaCl crystals."],
            "Reversibility via physical evaporation proves dissolving salt is physical.",
            "الذوبان انتشار للجسيمات في المذيب دون تكوين مركب جديد.",
            ["يحتفظ الملح المذاب بخواصه الكيميائية ويظل طعم المحلول مالحاً.", "بتبخير الماء نستعيد بلورات الملح نفسها كاملة."],
            "التغيرات القابلة للاسترجاع بالتبخير أو التبريد تكون غالباً فيزيائية.",
            None, None,
        ),
        (
            "Which observation is NOT reliable evidence by itself that a chemical reaction has taken place?",
            "أي ملاحظة مما يلي لا تُعد وحدها دليلاً كافياً على حدوث تفاعل كيميائي؟",
            [
                ("An object changing its shape or melting into a liquid when warmed", "تغير شكل الجسم أو انصهاره إلى سائل عند تسخينه"),
                ("Two clear solutions mixing and suddenly forming a bright yellow insoluble solid precipitate", "اختلاط محلولين شفافين وتكون راسب صلب أصفر فجأة"),
                ("Vinegar and baking soda bubbling vigorously to release cool CO₂ gas", "فوران الخل مع بيكربونات الصوديوم وانطلاق غاز CO₂"),
                ("A glowing wood splint burning with light, heat, smoke, and black ash", "احتراق الخشب مع انطلاق ضوء وحرارة ودخان ورماد أسود"),
            ],
            "Remember: phase changes (melting/boiling) look dramatic yet create zero new substances!",
            "تذكر: تغيرات الحالة (كالانصهار والغليان) تغيرات فيزيائية لا تنتج مادة جديدة!",
            "Melting and reshaping alter physical state/form without changing molecular identity.",
            ["Precipitate formation, reaction gas evolution (effervescence), and combustion light/ash indicate chemical changes.", "Melting wax or reshaping clay keeps the substance chemically unchanged."],
            "Even boiling bubbles are physical steam, unlike cold vinegar + baking soda gas bubbles!",
            "تغير الشكل أو الحالة الفيزيائية لا يعني تكوّن مادة جديدة.",
            ["تكوّن الراسب والفوران الكيميائي والاحتراق دلائل قوية على تفاعل كيميائي.", "أما الانصهار وتغير الشكل فتغيرات فيزيائية تحفظ نوع المادة."],
            "نفرق دائماً بين فقاعات الغليان الفيزيائية وفقاعات التفاعل الكيميائي.",
            None, None,
        ),
        (
            "What does the Law of Conservation of Mass state about every chemical reaction inside a sealed container?",
            "ماذا ينص قانون حفظ الكتلة في أي تفاعل كيميائي يحدث داخل وعاء محكم الإغلاق؟",
            [
                ("Total mass of all products equals the exact total mass of all starting reactants because atoms are only rearranged", "الكتلة الكلية للنواتج تساوي تماماً الكتلة الكلية للمتفاعلات لأن الذرات يُعاد ترتيبها فقط ولا تفنى"),
                ("Products always weigh slightly less because chemical energy destroys atoms", "النواتج أخف دائماً لأن الطاقة الكيميائية تفني بعض الذرات"),
                ("Gases produced in reactions have negative mass and lift the scale", "الغازات الناتجة لها كتلة سالبة ترفع كفة الميزان"),
                ("Mass doubles whenever two compounds react to form a precipitate", "تتضاعف الكتلة كلما تكوّن راسب صلب"),
            ],
            "Think of LEGO bricks: snapping the same bricks into a new model keeps the exact same total brick weight!",
            "تخيل مكعبات التركيب: إعادة ترتيب نفس المكعبات لصنع شكل جديد لا يغير وزنها الكلي!",
            "Matter is conserved: total atom counts and total mass remain invariant in closed reactions.",
            ["Chemical reactions break and form bonds between existing atoms.", "No atoms appear from nowhere or vanish, so mass before = mass after in a sealed system."],
            "If an open beaker seems lighter, a gas escaped into the air.",
            "ينص قانون حفظ الكتلة على أن المادة لا تفنى ولا تستحدث من عدم.",
            ["تعيد التفاعلات ترتيب الذرات نفسها في روابط جديدة.", "لذلك تظل الكتلة قبل التفاعل مساوية تماماً للكتلة بعد التفاعل في الوعاء المغلق."],
            "وأي نقص ظاهري في وعاء مفتوح يعني هروب غاز إلى الهواء.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b09:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Sealed conservation math, boiling vs reaction bubbles, patina, baking, missing reactant math
    B.add_math(
        tp, "Medium", bp,
        "A student pours 25 g of vinegar into a flask, puts 12 g of baking soda inside a balloon stretched over the mouth (total sealed system = 37 g plus flask), and tips the soda in so the balloon inflates with CO₂ gas. Ignoring the empty flask and balloon glass/rubber mass, what is the total mass of the contents inside the sealed flask + balloon after fizzing stops?",
        "سكب طالب 25 جم من الخل في دورق ووضع 12 جم من بيكربونات الصوديوم داخل بالون مثبت بإحكام على فوهة الدورق، ثم أفرغ البيكربونات فتفاعل وانتفخ البالون بغاز CO₂. بإهمال كتلة الدورق والبالون نفسه، ما الكتلة الكلية للمواد والنواتج داخل النظام المغلق بعد توقف الفوران؟",
        37, [13, 25, 49],
        "The balloon traps every molecule of CO₂ gas inside the sealed system!",
        "يحجز البالون المحكم كل جزيئات غاز CO₂ داخل النظام المغلق فلا يهرب شيء!",
        "By conservation of mass, sealed reactants mass equals sealed products mass.",
        ["Starting contents = 25 g vinegar + 12 g baking soda = 37 g.", "Because the balloon prevents gas from escaping, total mass after reaction remains 37 g."],
        "25 + 12 = 37 g.",
        "في النظام المغلق تبقى الكتلة ثابتة تماماً مهما تكوّنت غازات.",
        ["كتلة المتفاعلات = 25 + 12 = 37 جم.", "بما أن البالون منع تسرب غاز CO₂، تظل كتلة المحتويات 37 جم بعد انتهاء التفاعل."],
        "25 + 12 = 37 جم.",
        "",
        svg_process_flow(["25 g Vinegar", "+ 12 g Soda", "Sealed Balloon", "37 g Total"], "Closed System Conservation", "Sealed Reaction Mass"),
        svg_process_flow(["25 جم خل", "+ 12 جم صودا", "بالون محكم", "37 جم كلياً"], "حفظ الكتلة في نظام مغلق", "كتلة التفاعل المغلق"),
    )

    med_b09 = [
        (
            "Both a pot of boiling water on a stove and a glass of vinegar + baking soda produce vigorous gas bubbles. How do these two bubbling processes differ fundamentally?",
            "ينتج كلٌّ من قدر ماء يغلي وكأس خل مع بيكربونات الصوديوم فقاعات غازية كثيرة. ما الفرق الجوهري بين العمليتين؟",
            [
                ("Boiling bubbles are water vapor (physical state change of H₂O); vinegar + baking soda bubbles are new CO₂ gas from a chemical reaction", "فقاعات الغليان بخار ماء (تغير فيزيائي للماء نفسه)، بينما فقاعات الخل والصودا غاز CO₂ جديد ناتج عن تفاعل كيميائي"),
                ("Boiling water destroys H₂O chemically into hydrogen and oxygen flames", "غليان الماء يفكك الماء كيميائياً إلى لهب هيدروجين وأكسجين"),
                ("Vinegar + baking soda only boils because baking soda heats vinegar to 100°C", "الخليط يغلي فقط لأن الصودا تسخن الخل إلى 100°م"),
                ("Both processes are physical changes because both produce invisible gases", "العمليتان فيزيائيتان لأن كلتيهما تطلق غازاً غير مرئي"),
            ],
            "Check whether a brand-new molecule (CO₂) formed or if liquid H₂O just became gaseous H₂O.",
            "تحقق: هل تكوّن جزيء جديد (CO₂) أم مجرد تحول ماء سائل إلى ماء غازي؟",
            "Gas bubbles can arise from either physical boiling or chemical reaction.",
            ["Cooling steam above a boiling pot condenses straight back into liquid water (H₂O).", "Cooling vinegar + baking soda bubbles cannot rebuild vinegar and soda — new CO₂, water, and sodium acetate formed."],
            "Always look at whether new chemical bonds were created, not just whether bubbles appear.",
            "رغم تشابه ظهور الفقاعات، يختلف نوع التغير في الحالتين.",
            ["تبريد بخار الغليان يعيده ماءً سائلاً (نفس المادة H₂O) فهو تغير فيزيائي.", "أما فوران الخل مع الصودا فيكوّن غاز CO₂ وملحاً وماءً، أي مواد جديدة."],
            "التمييز يعتمد على تكوّن مادة جديدة من عدمه.",
            None, None,
        ),
        (
            "Which kitchen process is an example of a CHEMICAL change?",
            "أي عملية مطبخية مما يلي تُعد مثالاً على تغير كيميائي؟",
            [
                ("Baking flatbread dough in a hot oven until it rises, browns, and develops a toasted aroma", "خبز عجينة الخبز في الفرن الساخن حتى تنتفخ وتحمر وتكتسب رائحة التحميص"),
                ("Freezing fresh mango juice into solid ice pops", "تجميد عصير المانجو الطازج ليصبح مثلجات صلبة"),
                ("Grating a solid block of cheddar cheese into thin shreds", "بشر قالب جبن شيدر صلب إلى شرائح رفيعة"),
                ("Crushing rock salt crystals with a mortar and pestle", "سحق بلورات الملح الخشن في الهاون إلى مسحوق ناعم"),
            ],
            "Look for permanent color/aroma/chemical breakdown that cannot be reversed by melting or reassembling.",
            "ابحث عن تغير دائم في اللون والرائحة والتركيب لا يمكن إرجاعه بالتسخين أو التبريد.",
            "Baking triggers irreversible chemical reactions (browning, gas expansion, protein setting).",
            ["Freezing juice, grating cheese, and crushing salt only alter state or piece size.", "Baking transforms dough proteins and starches chemically into new compounds with toasted crust color and flavor."],
            "You cannot un-bake toasted bread back into raw wet dough!",
            "ينتج الخبز بالفرن مواد جديدة ذات طعم ولون ورائحة مختلفة.",
            ["التجميد والبشر والسحق كلها تغيرات فيزيائية للشكل أو الحالة.", "أما الخَبز فيغير تركيب النشا والبروتينات كيميائياً ولا يمكن استرجاع العجين."],
            "الرائحة الجديدة واللون البني الدائم من علامات التفاعل الكيميائي.",
            None, None,
        ),
        (
            "Over decades exposed to damp air and carbon dioxide, shiny brown copper domes turn a chalky green patina coating. What type of change formed this green coating?",
            "على مدى عقود من التعرض للهواء الرطب وثاني أكسيد الكربون، تتحول قباب النحاس البنية اللامعة إلى طبقة خضراء باهتة (زنجار النحاس). ما نوع هذا التغير؟",
            [
                ("A slow chemical change forming a new copper carbonate compound", "تغير كيميائي بطيء يكوّن مركباً جديداً هو كربونات النحاس"),
                ("A physical change caused by green paint falling from clouds", "تغير فيزيائي ناتج عن تساقط طلاء أخضر من السحب"),
                ("Melting of metallic copper into green ocean algae", "انصهار النحاس المعدني وتحوله إلى طحالب بحرية خضراء"),
                ("Simple drying of rainwater on copper without any reaction", "جفاف ماء المطر على النحاس دون أي تفاعل"),
            ],
            "Does the green coating conduct electricity and shine like pure copper, or is it a new compound?",
            "هل الطبقة الخضراء تحافظ على بريق النحاس وخواصه، أم أنها مركب جديد ناتج عن تفاعل بطيء؟",
            "Slow corrosion/tarnishing is a chemical reaction with atmospheric gases.",
            ["Copper atoms react gradually with O₂, H₂O, and CO₂ in air.", "The green crust is a new compound (copper carbonate) with totally different color and texture from copper metal."],
            "Chemical changes can happen slowly over years (rust/patina) or in milliseconds (fireworks).",
            "تآكل المعادن وتكون الزنجار تفاعلات كيميائية بطيئة مع غازات الهواء.",
            ["يتفاعل النحاس مع الأكسجين والرطوبة وCO₂ فيكوّن مركباً أخضر جديداً.", "تختلف خواص هذا المركب كلياً عن فلز النحاس النقي."],
            "تحدث التفاعلات الكيميائية بسرعات متفاوتة من ثوانٍ إلى سنوات.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b09:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Medium", bp,
        "In a sealed jar filled with pure oxygen, 18 g of magnesium ribbon burns completely to produce 30 g of white magnesium oxide ash with zero leftover metal. How many grams of oxygen gas reacted with the magnesium?",
        "في إناء مغلق مملوء بالأكسجين النقي، احترق 18 جم من شريط المغنيسيوم احتراقاً كاملاً فنتج 30 جم من رماد أكسيد المغنيسيوم الأبيض دون بقاء أي معدن. كم جراماً من غاز الأكسجين تفاعل مع المغنيسيوم؟",
        12, [18, 30, 48],
        "Mass of Magnesium + Mass of Oxygen = Mass of Magnesium Oxide (30 g).",
        "كتلة المغنيسيوم + كتلة الأكسجين = كتلة أكسيد المغنيسيوم (30 جم).",
        "Subtract the known reactant mass from the total product mass.",
        ["18 g + m(O₂) = 30 g.", "m(O₂) = 30 - 18 = 12 g of oxygen reacted."],
        "18 + 12 = 30 g.",
        "بموجب حفظ الكتلة: مجموع كتل المتفاعلات يساوي كتلة الناتج.",
        ["18 جم + كتلة الأكسجين = 30 جم.", "كتلة الأكسجين المتفاعل = 30 − 18 = 12 جم."],
        "تحقق: 18 + 12 = 30 جم.",
    )

    # Hard (10..14): Open vs closed mass, steel wool mass gain, lab comparison table, precipitate mass, burning candle
    open_tbl_en = svg_data_table(
        ["Stage", "Open Beaker (g)", "Sealed Flask (g)"],
        [["Before mixing", "90", "90"], ["During fizz", "87", "90"], ["After reaction", "86", "90"]],
        "Open vs Sealed Reaction Mass",
        [114, 114, 114],
    )
    open_tbl_ar = svg_data_table(
        ["المرحلة", "كأس مفتوح (جم)", "دورق مغلق (جم)"],
        [["قبل المزج", "90", "90"], ["أثناء الفوران", "87", "90"], ["بعد التفاعل", "86", "90"]],
        "مقارنة الكتلة مفتوحاً ومغلقاً",
        [110, 114, 114],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A student mixes 30 g acid and 10 g chalk inside a 50 g container (starting total = 90 g) in an open beaker and again in a sealed flask as recorded in the table. Why did the open beaker drop by 4 g while the sealed flask stayed at 90 g?",
        "مزج طالب 30 جم حمضاً مع 10 جم طباشير في إناء كتلته 50 جم (المجموع 90 جم) مرة في كأس مفتوح ومرة في دورق مغلق كما في الجدول. لماذا نقصت قراءة الكأس المفتوح بمقدار 4 جم بينما بقي الدورق المغلق عند 90 جم؟",
        [
            ("4 g of carbon dioxide gas formed during the reaction escaped into the surrounding air from the open beaker", "لأن 4 جم من غاز ثاني أكسيد الكربون الناتج عن التفاعل تسربت إلى هواء الغرفة من الكأس المفتوح"),
            ("4 g of chalk atoms vanished out of existence inside the open beaker", "لأن 4 جم من ذرات الطباشير فنيت تماماً في الكأس المفتوح"),
            ("Sealing a flask makes chalk molecules 4 g heavier than normal", "لأن إغلاق الدورق يجعل جزيئات الطباشير أثقل بمقدار 4 جم"),
            ("The open beaker absorbed 4 g of nitrogen and became lighter", "لأن الكأس المفتوح امتص 4 جم نيتروجين فأصبح أخف"),
        ],
        "Mass is conserved in BOTH experiments! Track where the gas molecules went.",
        "الكتلة محفوظة في التجربتين معاً! تتبع أين ذهبت جزيئات الغاز المتصاعد.",
        "Apparent mass loss in open vessels equals escaped gas mass.",
        ["Chalk (CaCO₃) + acid produces CO₂ gas.", "In the open beaker, 4 g of CO₂ drifted into the room air; in the sealed flask, those 4 g remained trapped inside."],
        "90 - 86 = 4 g of escaped CO₂ gas.",
        "النقص الظاهري في القراءة يساوي كتلة الغاز المتصاعد للخارج.",
        ["ينتج تفاعل الحمض والطباشير غاز CO₂.", "في الكأس المفتوح هرب 4 جم من الغاز للهواء، أما في المغلق فبقي محبوساً عند 90 جم."],
        "الكتلة محفوظة دائماً عند حساب جميع النواتج الغازية والصلبة.",
        open_tbl_en, open_tbl_ar,
    )

    hard_b09 = [
        (
            "A student places a 2.8 g pad of dry steel wool (iron) on an open digital balance, lights it safely with a battery spark until it glows and forms dark iron oxide ash, and lets it cool. The scale now reads 4.0 g instead of 2.8 g! Why did the solid pad GAIN 1.2 g?",
            "وضع طالب ليفة فولاذية جافة كتلتها 2.8 جم على ميزان رقمي مفتوح وأشعلها بأمان حتى توهجت وتكوّن أكسيد حديد داكن، وبعد أن بردت قرأ الميزان 4.0 جم بدلاً من 2.8 جم! لماذا زادت الكتلة بمقدار 1.2 جم؟",
            [
                ("Iron chemically bonded with 1.2 g of oxygen gas pulled from the surrounding room air", "لأن الحديد اتحد كيميائياً مع 1.2 جم من غاز الأكسجين المأخوذ من الهواء المحيط"),
                ("Battery electricity injected 1.2 g of solid electrons into the steel pad", "لأن كهرباء البطارية أضافت 1.2 جم من الإلكترونات الصلبة إلى الليفة"),
                ("Heat created brand-new iron atoms from nothing inside the pan", "لأن الحرارة ولّدت ذرات حديد جديدة من العدم"),
                ("Ash always weighs more than metal even in a vacuum chamber", "لأن الرماد أثقل دائماً من المعدن حتى في الفراغ التام"),
            ],
            "In open air, oxygen gas is an invisible reactant! Does iron + oxygen weigh more than iron alone?",
            "في الهواء المفتوح، الأكسجين الغازي متفاعل غير مرئي! أليس الحديد + الأكسجين أثقل من الحديد وحده؟",
            "Combustion in open air adds atmospheric oxygen mass into solid metal oxides.",
            ["Before ignition, oxygen molecules floated freely in room air, not sitting on the scale pan.", "During glowing combustion, iron captured 1.2 g of O₂ gas into solid Fe₂O₃ on the pan (2.8 + 1.2 = 4.0 g)."],
            "Conservation of mass holds once you include atmospheric O₂ as a reactant!",
            "الأكسجين الجوي غير المرئي دخل في التفاعل وزاد كتلة المادة الصلبة على الميزان.",
            ["قبل الاحتراق لم يكن أكسجين الهواء محسوباً ضمن قراءة الميزان.", "عند التوهج ارتبط 2.8 جم حديد مع 1.2 جم أكسجين لتكوين 4.0 جم من أكسيد الحديد."],
            "لو أُجريت التجربة في دورق مغلق لما تغيرت قراءة الميزان إطلاقاً.",
            None, None,
        ),
        (
            "A student records four observations in the lab table. Which two observations definitely represent CHEMICAL changes?",
            "دوّن طالب أربع ملاحظات مختبرية في الجدول الموضح. أي عمليتين تمثلان بالتأكيد تغيرات كيميائية؟",
            [
                ("Process 2 (caramelizing white sugar into bitter black solid) and Process 4 (clear liquids forming yellow solid)", "العملية 2 (تفحم السكر الأبيض إلى صلب أسود مر) والعملية 4 (تكوّن راسب أصفر من سائلين شفافين)"),
                ("Process 1 (iodine crystals turning into purple gas) and Process 3 (salt vanishing in water)", "العملية 1 والعملية 3"),
                ("Process 1 and Process 2 only", "العملية 1 والعملية 2 فقط"),
                ("Process 3 and Process 4 only", "العملية 3 والعملية 4 فقط"),
            ],
            "Beware: Process 1 is sublimation (pure iodine solid → pure iodine gas) and Process 3 is dissolving!",
            "انتبه: العملية 1 هي تسامٍ فيزيائي لليود، والعملية 3 هي ذوبان فيزيائي!",
            "Irreversible decomposition (black carbon) and precipitation indicate chemical reactions.",
            ["Process 1 (iodine sublimation) and Process 3 (salt dissolving) are reversible physical changes.", "Process 2 decomposes sucrose chemically into carbon + steam; Process 4 creates a brand-new insoluble precipitate."],
            "Always look past dramatic color changes when a substance simply changes state!",
            "التحول اللوني الناتج عن تفكك المادة أو تكوّن راسب جديد يدل على تفاعل كيميائي.",
            ["تسامي اليود (1) وذوبان الملح (3) لا يكوّنان مواد جديدة.", "تفحم السكر (2) ينتج كربوناً جديداً، ومزج السائلين (4) يكوّن راسباً كيميائياً جديداً."],
            "إذن العمليتان 2 و4 كيميائيتان.",
            svg_data_table(["#", "Observation"], [["1", "Iodine solid -> purple gas"], ["2", "Heated sugar -> black bitter solid"], ["3", "Salt stirs clear into water"], ["4", "2 clear liquids -> yellow solid"]], "4 Lab Processes", [48, 286]),
            svg_data_table(["#", "الملاحظة"], [["1", "يود صلب ← غاز بنفسجي بالتسخين"], ["2", "تسخين سكر ← صلب أسود مر الطعم"], ["3", "اختفاء الملح في ماء دافئ"], ["4", "سائلان شفافان ← راسب أصفر"]], "أربع عمليات مختبرية", [48, 294]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b09:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "In a closed reaction flask, 42 g of clear Solution A mixes with 58 g of clear Solution B. Immediately, 14 g of solid white precipitate settles at the bottom alongside a clear remaining solution. What is the mass in grams of the remaining clear liquid inside the flask?",
        "في دورق تفاعل مغلق، مُزج 42 جم من المحلول الشفاف A مع 58 جم من المحلول الشفاف B. تكوّن فوراً راسب أبيض صلب كتلته 14 جم وبقي سائل شفاف فوقه. ما كتلة السائل الشفاف المتبقي داخل الدورق بالجرام؟",
        86, [16, 72, 100],
        "Total mass = 42 + 58 = 100 g. Subtract the 14 g solid precipitate to find the remaining liquid mass.",
        "الكتلة الكلية = 42 + 58 = 100 جم. اطرح كتلة الراسب (14 جم) لمعرفة كتلة السائل المتبقي.",
        "Sum reactant masses, then subtract solid product mass.",
        ["Total mass before and after mixing = 42 + 58 = 100 g.", "Liquid mass = 100 - 14 = 86 g."],
        "86 + 14 = 100 = 42 + 58 g.",
        "الكتلة الكلية محفوظة فتتقسم بين الراسب والسائل المتبقي.",
        ["الكتلة الكلية = 42 + 58 = 100 جم.", "كتلة السائل المتبقي = 100 − 14 = 86 جم."],
        "تحقق: 86 + 14 = 100 جم.",
    )

    B.add_concept(
        tp, "Hard", bp,
        "When a wax candle burns steadily on a birthday cake, both a physical change AND a chemical change occur simultaneously. Which statement identifies BOTH changes accurately?",
        "عندما تحترق شمعة شمعية بانتظام، يحدث تغيران أحدهما فيزيائي والآخر كيميائي في الوقت نفسه. أي عبارة تحدد كلا التغيرين بدقة؟",
        [
            ("Melting/vaporizing wax at the wick is physical; burning wax vapor with oxygen into CO₂ and water vapor is chemical", "انصهار الشمع وتبخره عند الفتيل تغير فيزيائي، واحتراق بخار الشمع بالأكسجين إلى CO₂ وبخار ماء تغير كيميائي"),
            ("Melting solid wax is chemical; burning wick smoke is physical", "انصهار الشمع الصلب كيميائي، واحتراق الفتيل فيزيائي"),
            ("Both dripping wax and glowing flame light are strictly physical phase changes", "كلٌّ من سيلان الشمع واشتعال اللهب تغير فيزيائي فقط"),
            ("Wax turns chemically into glass while oxygen freezes physically into carbon", "يتحول الشمع كيميائياً إلى زجاج بينما يتجمد الأكسجين إلى كربون"),
        ],
        "Liquid wax pooling near the wick cools right back into solid wax drips — that part is physical! The flame consumes wax vapor chemically.",
        "الشمع السائل المتقاطر يتصلب ويعود شمعاً (تغير فيزيائي)؛ أما اللهب فيحرق بخار الشمع (تغير كيميائي).",
        "A burning candle couples physical melting/evaporation with chemical combustion.",
        ["Physical: solid wax melts into liquid and climbs the wick, then vaporizes.", "Chemical: hot wax vapor reacts with O₂ in the flame, producing CO₂, H₂O vapor, heat, and light."],
        "The candle shrinks over time because chemical combustion converts wax into invisible gases.",
        "تجمع الشمعة المشتعلة بين تغيرين متزامنين فيزيائي وكيميائي.",
        ["انصهار الشمع وتبخره عند الفتيل لا يغيران تركيبه فهو تغير فيزيائي.", "تفاعل بخار الشمع مع الأكسجين في اللهب ينتج حرارة وضوءاً وCO₂ وبخار ماء فهو تغير كيميائي."],
        "لذلك تتناقص كتلة الشمعة لتحول معظم الشمع إلى غازات متصاعدة.",
    )


def _add_b10(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B10"
    # Easy (0..4): Solutions vs heterogeneous mixtures, solute/solvent, magnet, filtration, evaporation
    easy_b10 = [
        (
            "Which mixture is a homogeneous SOLUTION where particles are evenly mixed at the molecular level and do not settle on standing?",
            "أي خليط مما يلي يُعد محلولاً متجانساً تتوزع فيه الجسيمات بانتظام على المستوى الجزيئي ولا تترسب مع الزمن؟",
            [
                ("Clear apple-vinegar and water mixture (or clear saltwater)", "خليط ماء وملح صافٍ متجانس (محلول ملحي)"),
                ("Muddy puddle water with sinking clay and sand", "ماء عكر بالطين والرمل المترسب"),
                ("A bowl of mixed almonds, dates, and walnuts", "وعاء من التمر واللوز والجوز المخلوط"),
                ("Iron filings stirred into coarse beach sand", "برادة حديد مخلوطة برمل الشاطئ"),
            ],
            "In a true solution, you cannot see separate layers or solid chunks and light passes clearly.",
            "في المحلول الحقيقي لا تُرى طبقات منفصلة ولا قطع صلبة عالقة ولا يترسب شيء بالركود.",
            "Solutions are uniform homogeneous mixtures down to individual ions or molecules.",
            ["Dissolved salt ions disperse uniformly throughout water and never settle out.", "Muddy water, trail mix, and iron-sand are heterogeneous mixtures with visible parts."],
            "Clear brass and clean air are also homogeneous solutions!",
            "المحلول خليط متجانس تماماً لا تترسب مكوناته بالترك.",
            ["تتوزع دقائق الملح المذاب بالتساوي بين جزيئات الماء.", "أما الطين والمكسرات والحديد مع الرمل فمخاليط غير متجانسة يمكن تمييز أجزائها."],
            "السبائك المعدنية مثل النحاس الأصفر والهواء النقي محاليل أيضاً.",
            None, None,
        ),
        (
            "To prepare sweet mint tea, Omar dissolves 15 g of white sugar completely into 200 mL of hot water. Which substance is the SOLUTE, and which is the SOLVENT?",
            "لتحضير شاي النعناع الحلو، أذاب عمر 15 جم من السكر تماماً في 200 مل من الماء الساخن. ما المادة المذابة وما المذيب على الترتيب؟",
            [
                ("Sugar is the solute; Water is the solvent", "السكر هو المذاب، والماء هو المذيب"),
                ("Water is the solute; Sugar is the solvent", "الماء هو المذاب، والسكر هو المذيب"),
                ("Both sugar and water are insoluble precipitates", "كلا السكر والماء رواسب غير ذائبة"),
                ("Hot cup glass is the solute; Mint aroma is the solvent", "الزجاج هو المذاب، ورائحة النعناع هي المذيب"),
            ],
            "The substance present in larger amount that does the dissolving is the solvent.",
            "المادة الموجودة بكمية أكبر والتي تُذيب غيرها هي المذيب، والمادة التي تذوب هي المذاب.",
            "Solute dissolves into the solvent.",
            ["Sugar (15 g) breaks apart and disperses inside water → solute.", "Water (200 mL) dissolves the sugar → universal solvent."],
            "Remember: solvENT = dissolvEs; solUTe = gets dissolved.",
            "المذاب هو المادة القليلة التي تختفي بالذوبان في المذيب الأكبر كمية.",
            ["السكر (15 جم) هو المادة المذابة داخل الماء.", "والماء (200 مل) هو المذيب."],
            "يُلقب الماء بالمذيب العام لقدرته على إذابة مواد كثيرة.",
            None, None,
        ),
        (
            "A student accidentally spills iron filings into a jar of fine yellow sulfur powder. Which quick physical tool separates the iron filings cleanly from the sulfur?",
            "انكبت برادة حديد عن طريق الخطأ داخل وعاء يحتوي على مسحوق الكبريت الأصفر الناعم. ما الأداة الفيزيائية السريعة لفصل برادة الحديد عن الكبريت بسهولة؟",
            [
                ("A bar magnet wrapped in paper", "مغناطيس مغلف بورقة"),
                ("A kitchen flour sieve with medium holes", "منخل دقيق بفتحات متوسطة"),
                ("Filter paper and a funnel", "ورق ترشيح وقمع"),
                ("A distillation boiling flask", "دورق تقطير بالتسخين"),
            ],
            "Use the magnetic property unique to iron (Fe) compared with nonmagnetic sulfur (S).",
            "استغل الخاصية المغناطيسية التي يتميز بها الحديد دون الكبريت.",
            "Magnetism cleanly separates ferromagnetic iron/nickel/cobalt from nonmagnetic powders.",
            ["Both powders are fine solids that would pass through a sieve together.", "A magnet attracts iron filings right out of the yellow sulfur powder."],
            "Wrapping the magnet in paper makes detaching the filings effortless!",
            "يفصل المغناطيس المواد المغناطيسية كالحديد عن غيرها دون ذوبان أو تسخين.",
            ["حبيبات الحديد والكبريت دقيقة وقد تمر معاً عبر المنخل.", "يجذب المغناطيس برادة الحديد وحدها تاركاً الكبريت الأصفر نقياً."],
            "تُعد المغناطيسية من أسرع طرق فصل المخاليط الجافة.",
            None, None,
        ),
        (
            "Which mixture can be separated effectively using simple filter paper folded inside a funnel?",
            "أي خليط مما يلي يمكن فصله بفعالية باستخدام ورق الترشيح المطوي داخل قمع؟",
            [
                ("Insoluble river sand mixed in tap water", "رمل نهري غير ذائب مخلوط بماء الصنبور"),
                ("Table salt completely dissolved in clear seawater", "ملح الطعام الذائب تماماً في ماء البحر الصافي"),
                ("Liquid sugar dissolved evenly in hot tea", "سكر ذائب بانتظام في شاي ساخن"),
                ("Oxygen gas mixed with nitrogen gas in clean air", "غاز الأكسجين المختلط بالنيتروجين في الهواء"),
            ],
            "Filter paper has microscopic pores: dissolved ions pass straight through, while solid insoluble grains get trapped!",
            "يحتوي ورق الترشيح على مسام دقيقة: تمر عبرها الجزيئات الذائبة وتُحتجز الحبيبات الصلبة غير الذائبة!",
            "Filtration separates insoluble suspended solids from liquids by particle size.",
            ["Sand particles are way larger than filter paper pores and stay behind as residue.", "Dissolved salt ions and sugar molecules are tiny and pass right through filter paper with water."],
            "To separate dissolved salt from water, you need evaporation or distillation instead.",
            "يفصل الترشيح المواد الصلبة غير الذائبة عن السوائل.",
            ["تحتجز مسام ورق الترشيح حبيبات الرمل الكبيرة ويمر الماء الصافي فقط.", "أما الملح والسكر الذائبان فيمران مع الماء عبر الورقة لصغر دقائقهما."],
            "لذلك لا يصلح الترشيح لفصل محلول ملحي صافٍ.",
            svg_process_flow(["Sand+Water", "Funnel+Filter", "Sand Trapped", "Clear Filtrate"], "Filtration by Particle Size", "Filtration Separation"),
            svg_process_flow(["رمل + ماء", "قمع ترشيح", "احتجاز الرمل", "ماء راشح نقي"], "الفصل بالترشيح", "فصل الرمل عن الماء"),
        ),
        (
            "Salt ponds along the Red Sea coast trap shallow seawater under hot sunshine until dry white sea salt crystals remain. Which separation method do these salt pans use?",
            "تحجز أحواض الملح على ساحل البحر الأحمر مياه البحر الضحلة تحت الشمس الحارة حتى تتبقى بلورات الملح الأبيض الجاف. ما طريقة الفصل المستخدمة؟",
            [
                ("Evaporation", "التبخير"),
                ("Magnetism", "الفصل المغناطيسي"),
                ("Filtration", "الترشيح"),
                ("Chromatography", "الكروماتوغرافيا"),
            ],
            "Solar heat turns liquid water into escaping vapor while solid salt stays behind in the pan.",
            "تحوّل حرارة الشمس الماء السائل إلى بخار متصاعد وتترك بلورات الملح الصلبة في الحوض.",
            "Evaporation recovers a dissolved solid solute when the liquid solvent need not be saved.",
            ["Water evaporates at daytime desert temperatures.", "Salt does not evaporate and crystallizes cleanly on the pan floor."],
            "If you wanted to collect the pure freshwater too, you would condense the vapor (distillation).",
            "التبخير يفصل المذاب الصلب عن المذيب السائل عندما لا نحتاج لجمع السائل.",
            ["يتبخر ماء البحر تدريجياً بفعل حرارة الشمس والرياح.", "وتتبلور أملاح البحر في قاع الأحواض لارتفاع درجة غليانها."],
            "أما إذا أردنا الاحتفاظ بالماء العذب فنستخدم التقطير.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b10:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Distillation, oil/water funnel, chromatography, dissolution factors, % concentration
    med_b10 = [
        (
            "A desalination lab in Jubail needs to recover BOTH pure drinkable liquid water AND dry salt crystals from seawater. Why is DISTILLATION chosen instead of simple open-pan evaporation?",
            "يحتاج مختبر تحلية في الجبيل إلى استخلاص الماء العذب الصالح للشرب وبلورات الملح معاً من ماء البحر. لماذا يُختار التقطير بدلاً من التبخير المكشوف؟",
            [
                ("Distillation boils water and then cools and condenses the steam back into pure liquid water inside a separate flask", "لأن التقطير يغلي الماء ثم يبرّد البخار ويكثّفه إلى ماء سائل نقي يُجمع في وعاء منفصل مع بقاء الملح"),
                ("Distillation passes seawater through a paper magnet that traps salt ions", "لأن التقطير يمرر ماء البحر عبر مغناطيس ورقي"),
                ("Open evaporation freezes seawater into salty snow blocks", "لأن التبخير المكشوف يجمد ماء البحر إلى ثلج مالح"),
                ("Distillation melts salt first at 30°C while water stays solid", "لأن التقطير يصهر الملح أولاً عند 30°م"),
            ],
            "Simple evaporation lets the pure water vapor blow away into the sky; distillation adds a condenser!",
            "التبخير المفتوح يضيّع بخار الماء في الهواء؛ أما التقطير فيضيف مكثفاً لاستعادة الماء النقي!",
            "Distillation couples vaporization and condensation to separate miscible solutions by boiling point.",
            ["Water boils at 100°C and rises as pure steam into a cooled condenser tube.", "Steam condenses into pure distilled liquid water while salt stays behind in the boiling flask."],
            "Thermal desalination plants work on this exact principle.",
            "يجمع التقطير بين التبخير والتكثيف لاسترداد المذيب والمذاب معاً.",
            ["يتصاعد بخار الماء النقي عند الغليان تاركاً الملح في الدورق.", "يمر البخار عبر مكثف بارد فيتكثف إلى ماء عذب مقطّر."],
            "بهذه الطريقة لا يضيع الماء العذب في الغلاف الجوي.",
            svg_process_flow(["Saltwater", "Boil (100°C)", "Cool Condenser", "Pure Water"], "Vaporization + Condensation", "Distillation Steps"),
            svg_process_flow(["ماء مالح", "غليان 100°م", "مكثف بارد", "ماء عذب نقي"], "تبخير ثم تكثيف", "خطوات التقطير"),
        ),
        (
            "Cooking oil and vinegar do not dissolve in each other and settle into two distinct liquid layers inside a jar. Which method best separates pure oil from pure vinegar cleanly?",
            "لا يمتزج زيت الطبخ مع الخل، بل ينفصلان في برطمان إلى طبقتين سائلتين واضحتين. ما الطريقة الأنسب لفصل الزيت النقي عن الخل النقي؟",
            [
                ("Use a separatory funnel (or careful decanting) based on their density difference", "استخدام قمع الفصل (أو الترويق/الصب الحذر) اعتماداً على اختلاف الكثافة بينهما"),
                ("Pour the jar through coarse filter paper", "سكب الخليط عبر ورق ترشيح خشن"),
                ("Sweep a bar magnet across the jar lid", "تمرير مغناطيس على غطاء البرطمان"),
                ("Stir vigorously until both layers vanish forever", "التقليب السريع حتى يختفي الانفصال للأبد"),
            ],
            "Both are liquids that pass straight through filter paper! How does a funnel with a bottom valve drain the denser bottom layer?",
            "كلاهما سائلان يمران عبر ورق الترشيح! كيف يفصل قمع بصنبور سفلي الطبقة الأثقل بالأسفل؟",
            "Immiscible liquids separate by density using a separatory funnel or decanting.",
            ["Less-dense oil floats atop denser water-based vinegar.", "Opening the stopcock drains the bottom vinegar layer cleanly, leaving pure oil inside the funnel."],
            "Both liquids pass right through filter paper, so filtration fails here.",
            "تنفصل السوائل غير الممتزجة باختلاف الكثافة عبر قمع الفصل.",
            ["يطفو الزيت الأقل كثافة فوق الخل الأعلى كثافة.", "بفتح صنبور قمع الفصل تخرج الطبقة السفلية أولاً ثم يُغلق الصنبور ليبقى الزيت نقياً."],
            "لا ينجح الترشيح لأن كلا المكونين سائل.",
            None, None,
        ),
        (
            "A student draws a black ink dot near the bottom of a strip of absorbent filter paper and dips only the bottom edge into water. Soon blue, yellow, and red bands climb to different heights up the paper. What separation technique is this?",
            "رسم طالب نقطة حبر أسود قرب أسفل شريط ورق امتصاص وغمر طرفه السفلي فقط في الماء، فصعدت أحزمة لونية زرقاء وصفراء وحمراء إلى ارتفاعات مختلفة. ما اسم هذه الطريقة؟",
            [
                ("Paper chromatography", "الكروماتوغرافيا الورقية (التحليل الكروماتوغرافي)"),
                ("Fractional crystallization", "التبلور التجزيئي"),
                ("Magnetic extraction", "الفصل المغناطيسي"),
                ("Centrifugal sieving", "الغربلة المركزية"),
            ],
            "Different ink dyes dissolve and cling to paper fibers differently as water wicks upward.",
            "تختلف سرعة انجراف كل صبغة مع الماء الصاعد عبر ألياف الورقة فتظهر منفصلة.",
            "Chromatography separates dissolved mixtures (dyes/pigments) by differential travel speed.",
            ["Water rises through paper pores by capillary action.", "Highly water-soluble dyes travel near the top while less-soluble dyes lag behind, revealing hidden colors inside black ink."],
            "Chemists use chromatography to check food dyes and plant pigments too.",
            "تفصل الكروماتوغرافيا الأصباغ والمكونات الذائبة حسب تفاوت سرعة حركتها.",
            ["يرتفع الماء بالخاصية الشعرية حاملاً أصباغ الحبر الأسود.", "تصل الأصباغ الأكثر ذوباناً في الماء إلى ارتفاع أكبر فتنفصل الألوان المكونة للحبر."],
            "تُستخدم هذه التقنية في فصل صبغات النبات ومختبرات الكيمياء.",
            None, None,
        ),
        (
            "Which set of actions will dissolve a 10 g cube of sugar into a glass of water in the SHORTEST amount of time?",
            "أي مجموعة إجراءات تُذيب مكعب سكر كتلته 10 جم في كوب ماء بأقصر زمن ممكن؟",
            [
                ("Crush the sugar cube into fine powder, use hot water (70°C), and stir steadily", "سحق المكعب إلى مسحوق ناعم، واستخدام ماء ساخن (70°م)، مع التحريك المستمر"),
                ("Keep the cube whole, use ice water (2°C), and leave it untouched", "ترك المكعب كاملاً، واستخدام ماء مثلج (2°م)، دون تحريك"),
                ("Crush the cube, use ice water (2°C), and place the cup in a freezer", "سحق المكعب في ماء مثلج ووضعه في المجمد"),
                ("Keep the cube whole in hot water without ever stirring", "ترك المكعب كاملاً في ماء ساخن دون تحريك"),
            ],
            "Three factors speed up solid dissolving: surface area (crushing), particle speed (heat), and fresh solvent contact (stirring).",
            "تسرّع ثلاثة عوامل ذوبان المواد الصلبة: زيادة مساحة السطح (السحق)، التسخين، والتحريك.",
            "Crushing, heating, and stirring maximize solid dissolution rate.",
            ["Crushing exposes far more sugar surface to water molecules.", "Heating speeds up molecular collisions; stirring sweeps concentrated syrup away from crystals."],
            "Doing all three together minimizes dissolving time.",
            "يزيد السحق والتسخين والتحريك معدل تصادم جزيئات المذيب بالمذاب.",
            ["السحق يضاعف مساحة سطح التماس، والحرارة تسرّع حركة الجزيئات.", "والتحريك يجدد الماء المحيط بالسكر فيختفي بسرعة قياسية."],
            "اجتماع العوامل الثلاثة يحقق أسرع ذوبان.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b10:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Medium", bp,
        "A student dissolves 20 g of table salt completely in 80 g of pure water to form 100 g of saltwater solution. What is the percentage concentration of salt by mass in this solution?",
        "أذاب طالب 20 جم من ملح الطعام تماماً في 80 جم من الماء النقي لتكوين 100 جم من المحلول الملحي. ما النسبة المئوية الكتلية للملح في المحلول؟",
        20, [16, 25, 80],
        "Mass % = (Mass of Solute ÷ Total Mass of Solution) × 100%. Be sure to divide by 20 + 80 = 100 g, not 80 g!",
        "النسبة المئوية = (كتلة المذاب ÷ الكتلة الكلية للمحلول) × 100%. تذكّر القسمة على 100 جم وليس 80 جم!",
        "Percent by mass uses total solution mass (solute + solvent) in the denominator.",
        ["Total solution mass = 20 + 80 = 100 g.", "Concentration = (20 ÷ 100) × 100% = 20%."],
        "20 g out of 100 g total = 20%.",
        "النسبة الكتلية تقسم كتلة المذاب على كتلة المحلول الكلية (المذاب + المذيب).",
        ["كتلة المحلول = 20 + 80 = 100 جم.", "التركيز = (20 ÷ 100) × 100% = 20%."],
        "تحقق: 20% من 100 جم = 20 جم ملح.",
        suffix="\\%",
    )

    # Hard (10..14): 4-step separation protocol, saturation table, gas vs solid solubility, concentration comparison, solar still
    B.add_concept(
        tp, "Hard", bp,
        "A laboratory jar contains a dry mixture of four ingredients: Iron filings, Gravel pebbles, Fine sand, and Table salt. Which step-by-step sequence recovers ALL four dry substances cleanly?",
        "يحتوي وعاء مختبر على خليط جاف من أربع مواد: برادة حديد، وحصى كبير، ورمل ناعم، وملح طعام. أي تسلسل خطوات يسترجع المواد الأربع نقية ومنفصلة؟",
        [
            ("Magnet (iron) → Coarse sieve (gravel) → Add water & filter (sand) → Evaporate filtrate (salt)", "مغناطيس (حديد) ← منخل (حصى) ← إضافة ماء وترشيح (رمل) ← تبخير الراشح (ملح)"),
            ("Add water first → Magnet → Boil sand → Sieve iron", "إضافة الماء أولاً ← مغناطيس ← غلي الرمل ← نخل الحديد"),
            ("Filter dry powder → Freeze salt → Magnet → Sieve water", "ترشيح الخليط الجاف ← تجميد الملح ← مغناطيس ← نخل الماء"),
            ("Evaporate dry sand → Dissolve gravel → Filter iron → Magnet", "تبخير الرمل الجاف ← إذابة الحصى ← ترشيح الحديد ← مغناطيس"),
        ],
        "Pull out magnetic iron and big gravel while dry BEFORE adding water, because wet sand sticks to iron and gravel!",
        "افصل الحديد والحصى والخليط جاف تماماً قبل إضافة الماء، لأن الرمل المبلل يلتصق بالحديد والحصى!",
        "Multi-step separation sequences leverage each component's unique physical property in optimal order.",
        ["Step 1: Magnet removes iron filings cleanly while dry. Step 2: Sieve catches large gravel while sand+salt fall through.", "Step 3: Add water so salt dissolves while sand stays solid; filter traps sand. Step 4: Evaporate clear saltwater to recover dry salt."],
        "Only this order isolates all 4 pure dry components.",
        "نستغل الخصائص الفيزيائية بالترتيب الأنسب لتجنب تلوث المكونات.",
        ["الخطوة 1: المغناطيس يجذب برادة الحديد. الخطوة 2: المنخل يحجز الحصى الكبير.", "الخطوة 3: إذابة الملح بالماء ثم الترشيح يحجز الرمل. الخطوة 4: تبخير الراشح يستعيد الملح."],
        "إضافة الماء مبكراً تعيق حركة المغناطيس وتجعل الرمل يلتصق بالحصى.",
        svg_process_flow(["Magnet: Iron", "Sieve: Gravel", "Filter: Sand", "Evaporate: Salt"], "4-Step Protocol", "Separating 4 Solids"),
        svg_process_flow(["مغناطيس: حديد", "منخل: حصى", "ترشيح: رمل", "تبخير: ملح"], "بروتوكول فصل رباعي", "فصل 4 مواد صلبة"),
    )

    sat_tbl_en = svg_data_table(
        ["Temp (°C)", "Salt (g/100g)", "Sugar (g/100g)"],
        [["20", "36", "204"], ["60", "37", "287"], ["90", "39", "415"]],
        "Solubility Limits Table",
        [86, 128, 128],
    )
    sat_tbl_ar = svg_data_table(
        ["الحرارة (°م)", "الملح (جم/100جم)", "السكر (جم/100جم)"],
        [["20", "36", "204"], ["60", "37", "287"], ["90", "39", "415"]],
        "جدول حدود الذائبية",
        [86, 132, 132],
    )
    B.add_math(
        tp, "Hard", bp,
        "According to the solubility table, a maximum of 36 g of salt can dissolve in 100 g of water at 20°C. A student pours 50 g of salt into 100 g of water at 20°C and stirs for 10 minutes. How many grams of undissolved salt settle at the bottom?",
        "وفقاً لجدول الذائبية، يذوب حد أقصى قدره 36 جم من الملح في 100 جم ماء عند 20°م. أضاف طالب 50 جم من الملح إلى 100 جم ماء عند 20°م وحركها لمدة 10 دقائق. كم جراماً من الملح سيبقى مترسباً في القاع دون ذوبان؟",
        14, [10, 36, 86],
        "Once 36 g dissolves, the solution is saturated; subtract 36 g from the 50 g added.",
        "بعد ذوبان 36 جم يصبح المحلول مشبعاً؛ اطرح 36 جم من الـ 50 جم المضافة.",
        "Undissolved excess = Added solute − Saturation limit.",
        ["At 20°C, 100 g water saturates at 36 g dissolved salt.", "Leftover solid at bottom = 50 - 36 = 14 g."],
        "36 g dissolved + 14 g solid = 50 g total salt.",
        "يستوعب المحلول حد الإشباع فقط ويترسب الفائض في القاع.",
        ["يذوب أقصى حد عند 20°م وهو 36 جم من الملح.", "المتبقي غير المذاب = 50 − 36 = 14 جم."],
        "تحقق: 36 + 14 = 50 جم.",
        "", sat_tbl_en, sat_tbl_ar,
    )

    hard_b10 = [
        (
            "A student leaves one cold bottle of sparkling water in the fridge (4°C) and an identical bottle on a sunny patio (38°C) with loose caps. Why does the warm bottle lose its fizz (CO₂ gas) much faster than the cold bottle?",
            "ترك طالب زجاجة ماء فوار باردة في الثلاجة (4°م) وأخرى مماثلة في فناء مشمس (38°م) بغطاءين غير محكمين. لماذا تفقد الزجاجة الدافئة غازها (CO₂) أسرع بكثير من الباردة؟",
            [
                ("Unlike most solid solutes, gas solubility in water DECREASES as water temperature rises, driving CO₂ bubbles out", "على عكس معظم المواد الصلبة، تقل ذائبية الغازات في الماء كلما ارتفعت حرارته فينطلق غاز CO₂ سريعاً"),
                ("Warm water chemically converts CO₂ gas into solid table sugar", "يحول الماء الدافئ غاز CO₂ كيميائياً إلى سكر مائدة صلب"),
                ("Sunlight increases gravity inside the warm bottle, pulling gas upward", "يزيد ضوء الشمس الجاذبية داخل الزجاجة الدافئة"),
                ("Cold water molecules turn into carbon dioxide inside the fridge", "تتحول جزيئات الماء البارد إلى ثاني أكسيد الكربون في الثلاجة"),
            ],
            "Compare solid solubility (increases with temperature) vs. gas solubility (decreases with temperature!).",
            "قارن بين ذائبية الصلب (تزيد بالتسخين) وذائبية الغاز (تقل بالتسخين!).",
            "Gas solubility drops at higher temperatures because fast-moving gas molecules escape liquid more easily.",
            ["Heating water speeds up dissolved CO₂ molecules so they overcome weak attractions and bubble out.", "Warm lakes also hold less dissolved O₂ for fish than cold mountain streams!"],
            "Remember the rule: Solids dissolve better hot; Gases stay dissolved better cold!",
            "تتصرف الغازات بعكس المواد الصلبة عند تسخين المحلول.",
            ["تمنح الحرارة جزيئات الغاز المذاب طاقة حركية تجعلها تفلت من السائل إلى الجو.", "لهذا تفقد المشروبات الغازية غازها في الجو الحار وتقل نسبة الأكسجين في المياه الدافئة."],
            "القاعدة: الصلب يذوب أكثر في الساخن، والغاز يذوب أكثر في البارد.",
            None, None,
        ),
        (
            "Beaker X contains 15 g of sugar dissolved in 60 mL of water. Beaker Y contains 25 g of sugar dissolved in 125 mL of water. Which beaker is MORE concentrated (sweeter per milliliter)?",
            "تحتوي الكأس X على 15 جم سكر مذابة في 60 مل ماء، وتحتوي الكأس Y على 25 جم سكر مذابة في 125 مل ماء. أي الكأسين أعلى تركيزاً (أكثر حلاوة لكل ملليلتر)؟",
            [
                ("Beaker X (0.25 g/mL) is more concentrated than Beaker Y (0.20 g/mL)", "الكأس X (0.25 جم/مل) أعلى تركيزاً من الكأس Y (0.20 جم/مل)"),
                ("Beaker Y is more concentrated because 25 g is greater than 15 g", "الكأس Y أعلى تركيزاً لأن 25 جم أكبر من 15 جم"),
                ("Both beakers have the exact same concentration", "الكأسان لهما التركيز نفسه تماماً"),
                ("Beaker Y has twice the concentration of Beaker X", "الكأس Y ضعف تركيز الكأس X"),
            ],
            "Divide solute grams by water mL for BOTH beakers to compare concentration fairly!",
            "اقسم جرامات السكر على ملليلترات الماء في كل كأس للمقارنة العادلة!",
            "Concentration equals solute mass per unit volume (ratio), not total solute alone.",
            ["Beaker X ratio = 15 ÷ 60 = 0.25 g/mL.", "Beaker Y ratio = 25 ÷ 125 = 0.20 g/mL. Since 0.25 > 0.20, Beaker X is more concentrated!"],
            "Equivalently, scaling Beaker X to 125 mL would contain 31.25 g > 25 g.",
            "التركيز هو نسبة المذاب إلى حجم المذيب وليس كمية المذاب وحدها.",
            ["تركيز X = 15 ÷ 60 = 0.25 جم/مل.", "تركيز Y = 25 ÷ 125 = 0.20 جم/مل؛ وبما أن 0.25 > 0.20 فالكأس X أشد حلاوة."],
            "المقارنة بالنسب تمنع الانخداع بكبر الرقم 25.",
            svg_bar_chart([("Beaker X", 0.25, BLUE), ("Beaker Y", 0.20, ORANGE)], "g / mL", "Sugar Concentration Check"),
            svg_bar_chart([("الكأس X", 0.25, BLUE), ("الكأس Y", 0.20, ORANGE)], "جم / مل", "مقارنة تركيز السكر"),
        ),
        (
            "In a desert survival kit, campers dig a shallow pit filled with muddy salty water, set a clean empty cup in the center, cover the pit tightly with clear plastic wrap, and place a small pebble in the middle of the plastic right above the cup. How does this solar still produce clean fresh water inside the cup?",
            "في حقيبة نجاة صحراوية، حفر رحالة حفرة فيها ماء طيني مالح، ووضعوا كوباً فارغاً في وسطها، وغطوا الحفرة بإحكام بغلاف بلاستيكي شفاف مع وضع حصاة صغيرة فوق الغلاف تماماً فوق الكوب. كيف يجمع هذا المقطّر الشمسي ماءً عذباً داخل الكوب؟",
            [
                ("Sunlight evaporates pure water vapor (leaving salt and mud behind), which condenses on the underside of the plastic and drips down the pebble cone into the cup", "تبخّر الشمس ماءً نقياً (تاركة الملح والطين بالأسفل)، فيتكثف البخار على السطح الداخلي للبلاستيك ويتجمع عند الحصاة ليقطر داخل الكوب"),
                ("The pebble squeezes salty mud upward through solid plastic pores", "تضغط الحصاة الطين المالح للأعلى عبر مسام البلاستيك"),
                ("Clear plastic filters saltwater directly into oxygen and hydrogen crystals", "يرشح البلاستيك الماء المالح ليحوله إلى بلورات أكسجين"),
                ("Nighttime freezing melts mud into freshwater inside the pit walls", "يجمد البرد الليلي الطين ويحوله لماء عذب"),
            ],
            "This solar still mimics both steps of distillation (evaporation + condensation) plus the water cycle!",
            "يحاكي هذا الجهاز خطوتي التقطير (تبخير + تكثيف) ودورة الماء في الطبيعة!",
            "Solar stills combine evaporation and condensation to purify contaminated/salty water.",
            ["Solar energy heats the salty mud water → pure H₂O evaporates while salt and dirt cannot vaporize.", "Vapor hits the cooler plastic film, condenses into freshwater droplets, and slides down the low point weighted by the pebble straight into the cup."],
            "Pure evaporation leaves dissolved minerals and microbes completely behind.",
            "يعتمد المقطّر الشمسي على تبخير الماء النقي ثم تكثيفه داخل الحفرة المغطاة.",
            ["ترفع الشمس حرارة الماء فيتبخر الماء النقي دون الملح والطين.", "يتكثف البخار تحت البلاستيك وتوجه الحصاة القطرات العذبة للسقوط مباشرة في الكوب."],
            "يمثل هذا تطبيقاً عملياً ذكياً لعمليات الفصل.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b10:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b11(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B11"
    # Easy (0..4): Elements vs compounds, metals, nonmetals, metalloids, conductors/insulators
    easy_b11 = [
        (
            "Which substance is a pure ELEMENT made of only one kind of atom rather than a compound?",
            "أي مادة مما يلي تُعد عنصراً نقياً يتكون من نوع واحد فقط من الذرات وليس مركباً؟",
            [
                ("Copper wire (Cu)", "سلك النحاس النقي (Cu)"),
                ("Pure table salt (NaCl)", "ملح الطعام النقي (NaCl)"),
                ("Carbon dioxide gas (CO₂)", "غاز ثاني أكسيد الكربون (CO₂)"),
                ("Distilled liquid water (H₂O)", "الماء المقطر النقي (H₂O)"),
            ],
            "Look for a single chemical symbol with only one capital letter!",
            "ابحث عن رمز كيميائي واحد يمثل نوعاً واحداً فقط من الذرات!",
            "Elements contain one type of atom; compounds chemically combine two or more elements.",
            ["Cu represents purely copper atoms.", "NaCl (Na + Cl), CO₂ (C + O), and H₂O (H + O) are compounds built from 2 elements."],
            "Even diatomic O₂ gas is an element because both atoms are oxygen.",
            "العنصر مادة نقية لا تتجزأ كيميائياً وتتكون من نوع واحد من الذرات.",
            ["النحاس (Cu) يتكون من ذرات النحاس وحدها.", "بينما الملح وCO₂ والماء مركبات تضم أكثر من عنصر مرتبطين كيميائياً."],
            "كثرة الذرات من النوع نفسه (مثل O₂) تبقى عنصراً.",
            None, None,
        ),
        (
            "A craftsman pounds a gold nugget flat into wafer-thin foil without cracking or shattering it. Which metallic property does this demonstrate?",
            "طرق صائغ قطعة ذهب وحوّلها إلى رقاقة رفيعة جداً دون أن تتشقق أو تنكسر. ما الخاصية الفلزية التي يظهرها الذهب هنا؟",
            [
                ("Malleability (ability to be hammered into thin sheets)", "القابلية للطرق والتشكيل إلى صفائح رقيقة"),
                ("Brittleness (shattering easily when struck)", "الهشاشة والانكسار عند الطرق"),
                ("Thermal insulation (blocking heat transfer)", "العزل الحراري ومنع انتقال الحرارة"),
                ("Acidic reactivity (turning blue litmus red)", "الحمضية وتحويل تباع الشمس للأحمر"),
            ],
            "Metals bend and flatten into sheets (malleable) and pull into wires (ductile), unlike brittle nonmetals!",
            "تتمدد الفلزات إلى صفائح بالطرق وتسحب لأسلاك دون كسر، بعكس اللافلزات الهشة!",
            "Malleability is a defining physical property of metals.",
            ["Metallic bonding allows layers of metal atoms to slide past one another without snapping.", "Gold is the most malleable metal known."],
            "Nonmetals like solid sulfur shatter into dust when tapped with a hammer.",
            "تتميز الفلزات بقابليتها للطرق والسحب واللمعان والتوصيل.",
            ["تنزلق طبقات ذرات الذهب بمرونة عند الطرق فتنفرد إلى رقائق رفيعة دون تكسر.", "أما اللافلزات الصلبة كالكبريت فتتحطم فوراً."],
            "القابلية للطرق تعني التشكيل على هيئة صفائح، والسحب يعني صنع أسلاك.",
            None, None,
        ),
        (
            "Which set of physical properties belongs to typical NONMETALS such as solid sulfur or phosphorus?",
            "أي مجموعة خصائص فيزيائية تنطبق على اللافلزات الصلبة النموذجية مثل الكبريت أو الفوسفور؟",
            [
                ("Dull appearance, brittle when hammered, and poor conductor of heat and electricity", "مظهر معتم غير لامع، هشة تنكسر عند الطرق، ورديئة التوصيل للحرارة والكهرباء"),
                ("Bright metallic luster, high ductility, and strong electrical conduction", "بريق معدني لامع، قابلة للسحب، وموصلة ممتازة للكهرباء"),
                ("Magnetic attraction toward steel and flexible bending without cracking", "تنجذب للمغناطيس وتنثني بمرونة دون تكسر"),
                ("Always liquid at room temperature and silvery gray", "تكون سائلة دائماً في حرارة الغرفة ورمادية لامعة"),
            ],
            "Nonmetals sit on the upper-right of the periodic table and have properties opposite to metals.",
            "تقع اللافلزات يمين الجدول الدوري وتعاكس الفلزات في معظم خواصها الفيزيائية.",
            "Solid nonmetals are generally dull, brittle, thermal/electrical insulators.",
            ["Carbon (charcoal), sulfur, and phosphorus lack metallic shine and crumble when struck.", "They are insulators rather than conductors (except graphite form of carbon)."],
            "Many nonmetals (O₂, N₂, Cl₂, Ne) are gases at room temperature.",
            "تتصف اللافلزات الصلبة بالعتامة والهشاشة ورداءة التوصيل.",
            ["الكبريت والفوسفور لا يلمعان مثل الفلزات ويتفتتان بضربة المطرقة.", "كما أنهما لا يوصلان التيار الكهربائي أو الحرارة بكفاءة."],
            "تُستخدم بعض اللافلزات والمركبات غير الفلزية كعوازل.",
            None, None,
        ),
        (
            "Silicon (Si) has a shiny metallic-looking surface like a metal, yet shatters like a brittle crystal and conducts electricity only moderately depending on temperature. How is silicon classified?",
            "يمتلك عنصر السيليكون (Si) بريقاً يشبه الفلزات، لكنه هش يتكسر كالبلورات ويوصل الكهرباء بدرجة متوسطة تتأثر بالحرارة. كيف يُصنف السيليكون؟",
            [
                ("A metalloid (semiconductor)", "شبه فلز (شبه موصل)"),
                ("An alkali metal", "فلز قلوي لين"),
                ("A noble gas nonmetal", "غاز خامل لا فلزي"),
                ("A liquid ionic compound", "مركب أيوني سائل"),
            ],
            "Sitting along the staircase border between metals and nonmetals gives it intermediate properties — ideal for computer chips!",
            "يقع على الخط المتدرج بين الفلزات واللافلزات ويجمع صفات وسطى — وهو أساس الشرائح الإلكترونية!",
            "Metalloids combine metal-like luster with brittle semiconductor behavior.",
            ["Silicon shines like a metal but cannot be hammered into wires.", "Its controlled semiconductivity powers solar cells and modern computer processors."],
            "Boron, silicon, germanium, and arsenic are classic metalloids.",
            "أشباه الفلزات جسر بين الفلزات واللافلزات في الجدول الدوري.",
            ["يمتلك السيليكون لمعاناً فلزياً وهشاشة لا فلزية وتوصيلاً كهربائياً متوسطاً قابل للتحكم.", "لذلك يُصنف شبه فلز ويُستخدم في الألواح الشمسية والمعالجات."],
            "التحكم في توصيله أساس الإلكترونيات الحديثة.",
            None, None,
        ),
        (
            "Why do electricians use copper inside household power cords and wrap the outside in flexible plastic?",
            "لماذا يستخدم الكهربائيون معدن النحاس داخل أسلاك الكهرباء المنزلية ويغلفونها من الخارج بالبلاستيك المرن؟",
            [
                ("Copper is a low-resistance metallic conductor that carries current easily, while plastic is an insulator preventing electric shock", "النحاس موصل فلزي ممتاز ينقل التيار بسهولة، بينما البلاستيك عازل يمنع الصعق الكهربائي"),
                ("Plastic conducts electricity faster while copper blocks voltage leaks", "البلاستيك يوصل الكهرباء أسرع والنحاس يمنع تسرب الجهد"),
                ("Copper turns electrical energy into solid plastic when cooled", "يحول النحاس الكهرباء إلى بلاستيك صلب عند التبريد"),
                ("Plastic melts into magnetic wires whenever switches turn on", "ينصهر البلاستيك ليصبح أسلاكاً مغناطيسية عند التشغيل"),
            ],
            "Distinguish an electrical conductor (core) from a protective electrical insulator (jacket).",
            "فرّق بين الموصل الكهربائي الذي يمرر التيار بالداخل والعازل الذي يحمي اليد بالخارج.",
            "Conductive metals carry electric current; nonmetallic polymers insulate safely.",
            ["Copper has free-moving electrons and high ductility to draw into long wires.", "Plastic nonmetallic coatings trap electrons inside, keeping users safe."],
            "The same logic pairs metal frying pans (conduct heat) with plastic/wooden handles (insulate heat).",
            "يجمع السلك الكهربائي بين قلب معدني موصل وغلاف عازل.",
            ["النحاس فلز سحوب وموصل ممتاز للتيار الكهربائي.", "البلاستيك عازل يمنع انتقال التيار إلى أيدينا عند لمس السلك."],
            "الأسلوب نفسه في أواني الطبخ: قاعدة معدنية موصلة ومقبض عازل.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b11:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Atom counts, Na+Cl2 -> NaCl contrast, steel alloy vs iron
    med_math_b11 = [
        (
            "A molecule of glucose sugar produced during photosynthesis has the chemical formula C₆H₁₂O₆. How many TOTAL atoms are bonded inside ONE molecule of glucose?",
            "صيغة جزيء سكر الجلوكوز الناتج عن البناء الضوئي هي C₆H₁₂O₆. كم مجموع الذرات المرتبطة داخل جزيء واحد فقط من الجلوكوز؟",
            24, [3, 18, 36],
            "Add the three subscripts: 6 carbon + 12 hydrogen + 6 oxygen.",
            "اجمع الأرقام السفلية للذرات الثلاث: 6 كربون + 12 هيدروجين + 6 أكسجين.",
            "Total atoms in a formula = sum of all element subscripts.",
            ["Count each element: C = 6, H = 12, O = 6.", "Total = 6 + 12 + 6 = 24 atoms (made of 3 different elements)."],
            "Do not confuse element count (3) with atom count (24)!",
            "مجموع الذرات في الجزيء يساوي مجموع أرقام الذرات لكل العناصر.",
            ["عدد ذرات الكربون = 6، والهيدروجين = 12، والأكسجين = 6.", "المجموع الكلي للذرات = 6 + 12 + 6 = 24 ذرة (تنتمي لـ 3 عناصر)."],
            "تحقق: 6 + 12 + 6 = 24 ذرة.",
        ),
        (
            "How many TOTAL atoms are present across THREE separate molecules of carbon dioxide (3 CO₂)?",
            "كم مجموع الذرات الكلي في ثلاثة جزيئات منفصلة من غاز ثاني أكسيد الكربون (3 CO₂)؟",
            9, [3, 6, 12],
            "One CO₂ molecule has 1 carbon + 2 oxygen = 3 atoms; multiply by 3 molecules.",
            "الجزيء الواحد من CO₂ يحتوي ذرة كربون + ذرتي أكسجين = 3 ذرات؛ اضرب في 3 جزيئات.",
            "Multiply atoms per molecule by the coefficient (number of molecules).",
            ["In 1 CO₂ molecule: 1 C + 2 O = 3 atoms.", "Across 3 molecules: 3 × 3 = 9 total atoms."],
            "3 C atoms + 6 O atoms = 9 atoms total.",
            "نحسب عدد الذرات في جزيء واحد ثم نضربه في المعامل (عدد الجزيئات).",
            ["في جزيء CO₂ واحد: 1 كربون + 2 أكسجين = 3 ذرات.", "في 3 جزيئات: 3 × 3 = 9 ذرات."],
            "تحقق: 3 كربون + 6 أكسجين = 9 ذرات.",
        ),
    ]
    for qen, qar, ans, dists, hen, har, ien, sen, cen, iar, sar, car in med_math_b11:
        B.add_math(tp, "Medium", bp, qen, qar, ans, dists, hen, har, ien, sen, cen, iar, sar, car)

    med_b11 = [
        (
            "Baking soda has the chemical formula NaHCO₃. How many DIFFERENT ELEMENTS and how many TOTAL ATOMS are in one unit of NaHCO₃?",
            "الصيغة الكيميائية لبيكربونات الصوديوم هي NaHCO₃. كم عدد العناصر المختلفة وكم مجموع الذرات في وحدة واحدة من NaHCO₃ على الترتيب؟",
            [
                ("4 different elements and 6 total atoms", "4 عناصر مختلفة و6 ذرات كلياً"),
                ("3 different elements and 5 total atoms", "3 عناصر مختلفة و5 ذرات كلياً"),
                ("5 different elements and 6 total atoms", "5 عناصر مختلفة و6 ذرات كلياً"),
                ("4 different elements and 4 total atoms", "4 عناصر مختلفة و4 ذرات كلياً"),
            ],
            "Count each capital letter to get elements (Na counts as 1 element!), and add implied 1s + 3.",
            "عدّ كل رمز يبدأ بحرف كبير لمعرفة العناصر (Na عنصر واحد!)، واجمع الأرقام لحساب الذرات.",
            "Capital-letter starts identify distinct elements; subscripts sum to total atoms.",
            ["Elements: Na (sodium), H (hydrogen), C (carbon), O (oxygen) = 4 elements.", "Atoms: 1 Na + 1 H + 1 C + 3 O = 6 atoms."],
            "Remember a lowercase second letter like 'a' in Na belongs to the same element symbol!",
            "الحرف الكبير يحدد بداية رمز عنصر جديد، والأرقام السفلية تعطي عدد ذراته.",
            ["العناصر هي: Na (صوديوم)، H (هيدروجين)، C (كربون)، O (أكسجين) = 4 عناصر.", "الذرات = 1 + 1 + 1 + 3 = 6 ذرات."],
            "لاحظ أن Na رمز واحد وليس عنصرين.",
            None, None,
        ),
        (
            "Pure sodium (Na) is a soft metal that bursts into flame in water, and chlorine (Cl₂) is a toxic greenish gas. Yet when they react chemically to form table salt (NaCl), it safely flavors food. Why?",
            "الصوديوم النقي (Na) فلز يشتعل بشدة في الماء، والكلور (Cl₂) غاز سام، لكن اتحادهما كيميائياً ينتج ملح الطعام (NaCl) الآمن في غذائنا. ما التفسير العلمي؟",
            [
                ("A chemical compound has completely new physical and chemical properties different from its constituent elements", "لأن المركب الكيميائي يكتسب خصائص فيزيائية وكيميائية جديدة تختلف تماماً عن خصائص عناصره المكونة له"),
                ("Sodium and chlorine simply hide inside salt crystals without forming any chemical bonds", "لأن الصوديوم والكلور يختبئان في الملح دون أي رابطة كيميائية"),
                ("Table salt is a physical mixture where boiling easily separates Na metal from Cl₂ gas", "لأن الملح خليط فيزيائي ينفصل فيه الصوديوم عن الكلور بالغليان"),
                ("Salt turns sodium into pure water inside the human mouth", "لأن الملح يحول الصوديوم إلى ماء نقي داخل الفم"),
            ],
            "Chemical bonding creates an entirely new substance with its own properties — unlike a physical mixture!",
            "الروابط الكيميائية تنتج مادة جديدة كلياً بخواص مختلفة عن عناصرها، على عكس المخاليط!",
            "Compounds possess emergent properties unrelated to the unbonded elements.",
            ["In a mixture, components keep their original properties (iron filings stay magnetic).", "In compound NaCl, electron transfer forms stable Na⁺ and Cl⁻ ions with safe salty taste and high melting point."],
            "Never assume a compound behaves like the average of its elements!",
            "تختلف خواص المركب الكيميائي جذرياً عن خواص العناصر التي دخلت في تكوينه.",
            ["في الخليط تحتفظ المواد بخواصها؛ أما في المركب فتتغير الخواص بالارتباط الكيميائي.", "لذلك يكون كلوريد الصوديوم NaCl آمناً ومستقراً بعكس خطورة الصوديوم والكلور منفردين."],
            "لا يعادل المركب مجرد مزج خواص عناصره.",
            None, None,
        ),
        (
            "Engineers make construction steel by blending mostly iron (Fe) with a tiny amount (~1%) of carbon (C) and sometimes chromium. Why is steel classified as an ALLOY MIXTURE rather than a pure element?",
            "يصنع المهندسون الفولاذ (الصلب) بمزج الحديد (Fe) بنسبة عالية مع نسبة ضئيلة (~1%) من الكربون (C) وأحياناً الكروم. لماذا يُصنف الفولاذ كسبيكة (خليط) وليس عنصراً نقياً؟",
            [
                ("It blends multiple elements physically in variable proportions rather than consisting of one atom type", "لأنه يمزج عدة عناصر معاً بنسب متفاوتة ولا يتكون من نوع واحد فقط من الذرات"),
                ("Steel dissolves instantly into gas whenever exposed to magnet poles", "لأن الفولاذ يتحول إلى غاز فوراً عند تقريب المغناطيس"),
                ("Carbon turns iron atoms into nonmetallic sulfur crystals", "لأن الكربون يحول ذرات الحديد إلى كبريت لا فلزي"),
                ("Alloys cannot be melted or reshaped once cooled", "لأن السبائك لا يمكن صهرها أو تشكيلها بعد التبريد"),
            ],
            "An element contains 1 kind of atom; an alloy is a solid solution of metals/nonmetals with customizable ratios.",
            "العنصر يحوي نوعاً واحداً من الذرات؛ أما السبيكة فمحلول صلب يمزج فلزات وعناصر أخرى بنسب مرنة.",
            "Alloys are solid homogeneous metallic mixtures with tunable compositions.",
            ["Pure iron is too soft for skyscrapers.", "Mixing small variable percentages of carbon (0.2%–2%) forms steel alloys much stronger than pure iron."],
            "Bronze (copper + tin) and brass (copper + zinc) are other common alloys.",
            "السبيكة محلول صلب متجانس يدمج عنصرين أو أكثر لتحسين المتانة ومقاومة الصدأ.",
            ["يضم الفولاذ ذرات الحديد وذرات الكربون معاً، وتختلف نسبتها حسب الاستخدام.", "إذن ليس عنصراً نقياً بل خليط معدني متجانس (سبيكة)."],
            "تشبهه سبيكة النحاس الأصفر والبرونز.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b11:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Mystery sample property table, H2+O2 vs H2O, atom count balance, material selection matrix, fixed ratio vs mixture
    el_tbl_en = svg_data_table(
        ["Sample", "Luster", "Hammer Test", "Bulb Lit?"],
        [["X", "Shiny", "Flattens", "Bright"], ["Y", "Dull yellow", "Shatters", "Off"], ["Z", "Shiny gray", "Cracks", "Dim"]],
        "Unknown Element Lab Tests",
        [68, 92, 92, 86],
    )
    el_tbl_ar = svg_data_table(
        ["العينة", "البريق", "الطرق", "المصباح؟"],
        [["X", "لامع", "يتصفح", "قوي"], ["Y", "أصفر باهت", "يتفتت", "مطفأ"], ["Z", "رمادي لامع", "يتشقق", "خافت"]],
        "اختبار عناصر مجهولة",
        [68, 92, 92, 86],
    )
    B.add_concept(
        tp, "Hard", bp,
        "Students test three mystery elements (X, Y, Z) in the lab table. Which classification correctly matches X, Y, and Z?",
        "اختبر طلاب ثلاثة عناصر مجهولة (X، Y، Z) وسجلوا النتائج في الجدول. أي تصنيف يطابق X وY وZ على الترتيب؟",
        [
            ("X = Metal, Y = Nonmetal, Z = Metalloid", "X فلز، و Y لا فلز، و Z شبه فلز"),
            ("X = Nonmetal, Y = Metal, Z = Metalloid", "X لا فلز، و Y فلز، و Z شبه فلز"),
            ("X = Metalloid, Y = Nonmetal, Z = Metal", "X شبه فلز، و Y لا فلز، و Z فلز"),
            ("X = Metal, Y = Metalloid, Z = Nonmetal", "X فلز، و Y شبه فلز، و Z لا فلز"),
        ],
        "Shiny + malleable + bright bulb = Metal; dull + brittle + off = Nonmetal; mixed intermediate traits = Metalloid!",
        "لامع وقابل للطرق وموصل قوي = فلز؛ باهت وهش وعازل = لا فلز؛ وصفات متوسطة = شبه فلز!",
        "Combine luster, mechanical behavior, and conductivity to classify elements.",
        ["X flattens (malleable) and conducts brightly → Metal (e.g., aluminum).", "Y is dull, shatters, and insulates → Nonmetal (sulfur). Z shines yet cracks and conducts dimly → Metalloid (silicon)."],
        "Every column in the test table lines up cleanly.",
        "نجمع بين البريق والقابلية للطرق والتوصيل الكهربائي لتصنيف العنصر.",
        ["العينة X لامعة وتتصفح وتضيء المصباح بقوة ← فلز.", "العينة Y باهتة وتتفتت ولا توصل ← لافلز، بينما تجمع Z بين اللمعان والتشقق والتوصيل الخافت ← شبه فلز."],
        "الاختبارات الثلاثة تحسم التصنيف دون لبس.",
        el_tbl_en, el_tbl_ar,
    )

    hard_b11 = [
        (
            "Hydrogen (H₂) is an explosive gas that burns rapidly, and oxygen (O₂) is a gas that feeds fires fiercely. Yet liquid water (H₂O) formed by burning H₂ in O₂ is used by firefighters to extinguish fires! Which statement best explains this contrast?",
            "الهيدروجين (H₂) غاز شديد الاشتعال، والأكسجين (O₂) غاز يساعد على الاشتعال بقوة؛ ومع ذلك يستخدم رجال الإطفاء الماء السائل (H₂O) المتكون من اتحادهما لإخماد الحرائق! أي عبارة تفسر هذا التناقض الظاهري؟",
            [
                ("Bonding H and O chemically forms a stable new compound (H₂O) whose energy and properties differ completely from H₂ and O₂", "الارتباط الكيميائي بين الهيدروجين والأكسجين يكوّن مركباً جديداً مستقراً (H₂O) تختلف طاقته وخواصه كلياً عن الغازين الأصليين"),
                ("Water molecules keep fire away only because water freezes fire into ice", "تطفئ جزيئات الماء النار لأنها تجمد اللهب إلى جليد"),
                ("In water, hydrogen and oxygen separate back into pure non-burning helium", "ينفصل الهيدروجين والأكسجين داخل الماء ويتحولان إلى هيليوم"),
                ("Oxygen loses all its protons as soon as it cools below 100°C", "يفقد الأكسجين بروتوناته بمجرد تبريده دون 100°م"),
            ],
            "Think about how chemical reactions rearrange electrons into a much lower-energy, stable molecule.",
            "فكر كيف تعيد التفاعلات الكيميائية ترتيب الإلكترونات لتكوين جزيء مستقر منخفض الطاقة.",
            "Chemical bonding turns reactive elements into low-energy stable compounds.",
            ["Burning H₂ with O₂ already released the combustion energy!", "The product H₂O is already fully oxidized, stable, and absorbs huge heat when sprayed on flames."],
            "Compounds never share the hazards of their free unreacted elements.",
            "تكوّن الروابط الكيميائية مادة جديدة بخصائص مختلفة ومستقرة.",
            ["احتراق الهيدروجين بالأكسجين يطلق طاقة التفاعل، وما ينتج (H₂O) مادة مستقرة خامدة أمام النار.", "يمتص الماء السائل الحرارة ويعزل الأكسجين عن الوقود المشتعل."],
            "فخواص المركب مستقلة عن خواص العناصر الحرة قبل التفاعل.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b11:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "In the balanced chemical equation 2 H₂ + O₂ → 2 H₂O, how many TOTAL atoms (hydrogen + oxygen combined) exist on the right-hand product side?",
        "في المعادلة الكيميائية الموزونة: 2 H₂ + O₂ → 2 H₂O، كم مجموع الذرات الكلي (هيدروجين + أكسجين معاً) في طرف النواتج الأيمن؟",
        6, [3, 4, 8],
        "Each H₂O molecule contains 3 atoms (2 H + 1 O). Multiply by the 2 molecules of water produced!",
        "يحتوي جزيء الماء الواحد H₂O على 3 ذرات (2 هيدروجين + 1 أكسجين). اضرب في 2 جزيء!",
        "Sum conserved atoms across reactant and product sides.",
        ["On reactant side: 2 H₂ (4 H atoms) + 1 O₂ (2 O atoms) = 6 atoms.", "On product side: 2 H₂O = 2 × (2 H + 1 O) = 4 H + 2 O = 6 total atoms."],
        "Conservation of atoms keeps both sides equal to 6.",
        "الذرات محفوظة في المعادلة الموزونة بين المتفاعلات والنواتج.",
        ["جزيء H₂O الواحد فيه 3 ذرات.", "في جزيئين 2 H₂O: 4 ذرات هيدروجين + 2 ذرة أكسجين = 6 ذرات."],
        "تحقق: طرف المتفاعلات أيضاً 4 + 2 = 6 ذرات.",
    )

    mat_tbl_en = svg_data_table(
        ["Material", "Melt (°C)", "Conduct Heat", "Bend?"],
        [["M1", "1085", "Very High", "Bends"], ["M2", "180", "Very Low", "Bends"], ["M3", "115", "Very Low", "Brittle"]],
        "Cookware Material Table",
        [76, 86, 102, 76],
    )
    mat_tbl_ar = svg_data_table(
        ["المادة", "الانصهار (°م)", "التوصيل", "التشكل"],
        [["M1", "1085", "عالٍ جداً", "ينثني"], ["M2", "180", "ضعيف جداً", "ينثني"], ["M3", "115", "ضعيف جداً", "هش ينكسر"]],
        "مصفوفة اختيار مواد الطهي",
        [68, 92, 92, 92],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A cookware designer reads the material properties table to pick one material for the frying pan BASE (touching the 300°C burner) and one for the HANDLE (held safely by hand without cracking if dropped). Which pairing works best?",
        "يراجع مصمم أواني الطهي الجدول لاختيار مادة لقاعدة المقلاة (تلامس شعلة 300°م) ومادة للمقبض (تُمسك باليد بأمان ولا تنكسر عند السقوط). أي اختيار هو الأنسب؟",
        [
            ("M1 (metal) for the pan base; M2 (tough polymer) for the handle", "المادة M1 (فلز) لقاعدة المقلاة، والمادة M2 (بوليمر متين) للمقبض"),
            ("M2 for the pan base; M1 for the handle", "المادة M2 للقاعدة، و M1 للمقبض"),
            ("M3 for both base and handle", "المادة M3 لكلٍّ من القاعدة والمقبض"),
            ("M1 for both base and handle so the handle melts bread faster", "المادة M1 لكلٍّ منهما"),
        ],
        "The base needs high melting point + high heat conduction; the handle needs thermal insulation + toughness (not brittle!).",
        "القاعدة تحتاج توصيلاً حرارياً عالياً وانصهاراً مرتفعاً؛ والمقبض يحتاج عزلاً حرارياً ومتانة لا هشاشة!",
        "Engineering design matches material properties (melting point, conductivity, ductility) to function.",
        ["M1 conducts heat rapidly and withstands 1085°C (copper) → ideal pan base.", "M2 insulates hand from heat and bends rather than shattering if dropped → ideal handle (whereas M3 is brittle and melts near 115°C)."],
        "Checking all three columns rules out M2 for base and M3 for handle.",
        "يعتمد اختيار المواد الهندسي على موازنة التوصيل والانصهار والمتانة.",
        ["المادة M1 توصل الحرارة بكفاءة وتتحمل حتى 1085°م فتصلح للقاعدة.", "المادة M2 رديئة التوصيل للحرارة ولا تنكسر بسهولة عند السقوط فتصلح للمقبض، بينما M3 هشة تنكسر."],
        "وهكذا نوفّق بين السلامة والكفاءة.",
        mat_tbl_en, mat_tbl_ar,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Pure liquid water (H₂O) ALWAYS contains 8 g of oxygen for every 1 g of hydrogen, whether sampled from Taif rainwater or Arctic ice. By contrast, saltwater from the Red Sea and saltwater from a kitchen cup can have very different salt percentages. Why?",
        "يحتوي الماء النقي (H₂O) دائماً على 8 جم أكسجين لكل 1 جم هيدروجين سواء أُخذ من أمطار الطائف أم من جليد القطبين، بينما تختلف نسبة الملح في ماء البحر الأحمر عنها في كوب ماء مالح بالمطبخ. ما السبب؟",
        [
            ("Water is a compound with a fixed chemical formula (2 H : 1 O), whereas saltwater is a physical mixture whose components can vary freely", "لأن الماء مركب كيميائي له صيغة ونسبة ثابتة (2 هيدروجين : 1 أكسجين)، بينما الماء المالح مخلوط فيزيائي تتغير نسب مكوناته بحرية"),
            ("Saltwater undergoes nuclear fusion whenever stirred in a kitchen cup", "لأن الماء المالح يخضع لتفاعل نووي عند تقليبه في الكوب"),
            ("Water molecules are physically mixed mixtures of gas bubbles that freeze at 8:1", "لأن الماء النقي مخلوط غازي يتجمد بنسبة 8:1"),
            ("Red Sea fish absorb all hydrogen atoms from ocean waves", "لأن أسماك البحر الأحمر تمتص ذرات الهيدروجين من الأمواج"),
        ],
        "Recall the fundamental difference between a pure compound (fixed atomic ratio) and a mixture/solution (variable recipe).",
        "تذكر الفرق الأساسي بين المركب النقي (نسب ذرية ثابتة) والمخلوط أو المحلول (نسب متغيرة).",
        "Definite fixed composition distinguishes pure compounds from variable mixtures.",
        ["Every water molecule is strictly H₂O (fixed 2:1 atom ratio, fixed 8:1 O-to-H mass ratio).", "Adding one spoon or five spoons of salt to water still yields a valid saltwater mixture (solution)."],
        "This law of definite proportions defines every true chemical compound.",
        "يتميز المركب النقي بثبات نسب عناصره دائماً، بعكس المخلوط.",
        ["كل جزيء ماء يتكون دائماً من ذرتي هيدروجين وذرة أكسجين لا تتغير نسبتهما.", "أما المحلول الملحي فيمكن تحضيره بملعقة ملح أو بخمس ملاعق دون تغير صفته كمخلوط."],
        "وهذا يوضح الفارق الدقيق بين المركبات والمخاليط.",
    )


def _add_b12(B: G6SciBankBuilder) -> None:
    tp, bp = "Chemistry & Matter", "G6-SCI-B12"
    # Easy (0..4): Reading pH scale & litmus rules with svg_ph_scale
    easy_ph = [
        (
            2, "Lemon", "ليمون", "Acidic Sample", "عينة حمضية",
            "Based on the pH scale diagram, lemon juice registers around pH 2. How is lemon juice classified?",
            "استناداً إلى مقياس الرقم الهيدروجيني pH الموضح، يسجل عصير الليمون قيمة قريبة من pH 2. كيف يُصنف عصير الليمون؟",
            [("Acidic (acid)", "حمضي (حمض)"), ("Neutral", "متعادل"), ("Basic (alkaline)", "قاعدي (قلوي)"), ("Pure distilled salt", "ملح مقطر نقي")],
            "Values below 7 on the 0–14 scale are acidic; 7 is neutral; above 7 are basic.",
            "القيم الأقل من 7 على المقياس (0–14) حمضية، و7 متعادلة، والأكبر من 7 قاعدية.",
            "A pH below 7 indicates an acidic solution.",
            ["Locate pH 2 on the left (red/orange) side of the pH scale.", "Since 2 < 7, lemon juice is an acid (citric acid)."],
            "Common food acids like citrus and vinegar have pH values between 2 and 4.",
            "تشير قيمة pH الأصغر من 7 إلى أن المحلول حمضي.",
            ["تقع القيمة pH 2 في المنطقة الحمراء/البرتقالية يسار المقياس.", "بما أن 2 أقل من 7، فعصير الليمون مادة حمضية."],
            "تتميز الأحماض الغذائية بمذاقها اللاذع.",
        ),
        (
            7, "Water", "ماء نقي", "Neutral Sample", "عينة متعادلة",
            "Pure distilled water sits squarely at pH 7 on the pH scale. What does pH 7 signify?",
            "يقع الماء المقطر النقي تماماً عند pH 7 على مقياس الرقم الهيدروجيني. علامَ تدل القيمة pH 7؟",
            [("Neutral — neither acidic nor basic", "متعادل — ليس حمضياً ولا قاعدياً"), ("Extremely strong corrosive acid", "حمض قوي جداً شديد التآكل"), ("Concentrated strong base", "قاعدة قوية مركزة"), ("Insoluble solid metal oxide", "أكسيد فلزي صلب غير ذائب")],
            "Look right at the green midpoint labeled 7 on the pH strip.",
            "انظر إلى المنتصف الأخضر المرقم بـ 7 على المقياس.",
            "pH 7 marks the exact neutral midpoint between acids and bases.",
            ["Acids run from 0 up to < 7; bases run from > 7 up to 14.", "Pure water at 25°C balances H⁺ and OH⁻ equally at pH 7 (neutral)."],
            "Pure water leaves both red and blue litmus paper unchanged.",
            "يمثل الرقم 7 نقطة التعادل الدقيقة بين الأحماض والقواعد.",
            ["تتراوح الأحماض من 0 إلى أقل من 7، والقواعد من فوق 7 إلى 14.", "الماء النقي متعادل تماماً عند 7 ولا يغير لون ورق تباع الشمس."],
            "أي محلول عند 7 يكون متعادلاً.",
        ),
        (
            9, "Soda", "صودا الخبز", "Basic Sample", "عينة قاعدية",
            "Dissolved baking soda sits near pH 9 as marked on the pH scale. How do chemists classify this solution?",
            "يسجل محلول بيكربونات الصوديوم (صودا الخبز) قيمة قريبة من pH 9 كما يظهر في المقياس. كيف يصنف الكيميائيون هذا المحلول؟",
            [("Basic / alkaline (weak base)", "قاعدي / قلوي (قاعدة ضعيفة)"), ("Strong mineral acid", "حمض معدني قوي"), ("Neutral pure water", "ماء نقي متعادل"), ("Organic solid lipid", "دهن عضوي صلب")],
            "Values greater than 7 up to 14 belong to the Basic (alkaline) side.",
            "القيم الأكبر من 7 حتى 14 تنتمي إلى الجانب القاعدي (القلوي).",
            "A pH above 7 indicates a basic (alkaline) solution.",
            ["pH 9 lies to the right of neutral 7 in the blue/teal basic region.", "Baking soda is a mild base often used to neutralize acid odors or stings."],
            "Stronger household cleaners like bleach reach pH 12–13.",
            "تشير قيمة pH الأكبر من 7 إلى محلول قاعدي.",
            ["تقع القيمة 9 يمين نقطة التعادل 7 في المنطقة الزرقاء القاعدية.", "بيكربونات الصوديوم قاعدة خفيفة آمنة الاستخدام."],
            "أما المنظفات القوية كالمبيضات فتقترب من pH 12–13.",
        ),
        (
            3, "Vinegar", "خل", "Litmus Acid Test", "اختبار الحمض بالتباع",
            "A student dips both a strip of BLUE litmus paper and a strip of RED litmus paper into white kitchen vinegar (pH 3). What color change occurs?",
            "غمست طالبة شريط تباع شمس أزرق وشريطاً آخر أحمر في خل أبيض (pH 3). ما تغير اللون الذي تلاحظه؟",
            [
                ("Blue litmus turns RED; red litmus stays RED", "يتحول ورق تباع الشمس الأزرق إلى أحمر، ويبقى الورق الأحمر أحمر كما هو"),
                ("Red litmus turns BLUE; blue litmus stays BLUE", "يتحول الورق الأحمر إلى أزرق، ويبقى الأزرق أزرق"),
                ("Both strips turn bright green immediately", "يتحول الشريطان فوراً إلى اللون الأخضر الساطع"),
                ("Both strips turn colorless white like bleach", "يصبح الشريطان أبيضين بلا لون"),
            ],
            "Remember the simple memory trick: Acid = Red! Acids turn blue litmus red.",
            "تذكّر القاعدة البسيطة: الأحماض تُحمّر ورقة تباع الشمس الزرقاء!",
            "Acids turn blue litmus red while leaving red litmus unchanged.",
            ["Vinegar contains acetic acid (pH 3 < 7).", "Acids shift blue litmus paper to red and leave red litmus red."],
            "Bases do the exact reverse: turn red litmus blue.",
            "الأحماض تحوّل ورقة تباع الشمس الزرقاء إلى اللون الأحمر.",
            ["الخل محلول حمضي رقم هيدروجيني 3.", "عند غمس الورقتين تصبح الزرقاء حمراء بينما لا يتغير لون الحمراء."],
            "أما القواعد فتزرّق ورقة تباع الشمس الحمراء.",
        ),
        (
            10, "Soap", "صابون", "Litmus Base Test", "اختبار القاعدة بالتباع",
            "Liquid hand soap feels slippery between fingers and has a pH around 10. What happens when RED litmus paper is dipped into soapy water?",
            "يتميز سائل غسل اليدين بملمس زلق ورقم هيدروجيني نحو 10. ماذا يحدث عند غمس ورقة تباع شمس حمراء في ماء الصابون؟",
            [
                ("Red litmus paper turns BLUE", "يتحول لون ورقة تباع الشمس الحمراء إلى أزرق"),
                ("Red litmus paper turns bright yellow", "يتحول لون الورقة الحمراء إلى أصفر"),
                ("Red litmus paper stays dark red without change", "تبقى الورقة الحمراء حمراء دون أي تغير"),
                ("Red litmus dissolves completely into soap bubbles", "تذوب الورقة الحمراء تماماً داخل رغوة الصابون"),
            ],
            "Remember: Base = Blue! Slippery feel and pH > 7 are hallmarks of bases.",
            "تذكّر: القاعدة تُزرّق ورقة تباع الشمس الحمراء، وتمتاز بملمس زلق وpH أكبر من 7.",
            "Bases turn red litmus blue.",
            ["Soap solution is alkaline (pH 10 > 7).", "Basic solutions convert red litmus dye into blue while leaving blue litmus blue."],
            "Never taste unknown lab chemicals — always use pH indicators!",
            "القواعد تحول ورقة تباع الشمس الحمراء إلى اللون الأزرق.",
            ["محلول الصابون قاعدي (pH = 10 > 7).", "لذلك يغيّر لون تباع الشمس الأحمر إلى أزرق."],
            "الملمس الزلق من الصفات المميزة للقواعد الآمنة المخففة.",
        ),
    ]
    for ph_v, len_s, lar_s, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in easy_ph:
        den, dar = _ph_svgs(ph_v, len_s, lar_s, ten, tar)
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Relative pH strength, neutralization, antacid, red cabbage table
    med_ph = [
        (
            2, "Acid A", "حمض A", "Acid Strength Check", "مقارنة قوة الأحماض",
            "Sample A is tomato juice (pH 4) and Sample B is lemon juice (pH 2). Which sample is the STRONGER acid, and what happens to acidity as pH moves from 4 down toward 0?",
            "العينة A هي عصير طماطم (pH 4) والعينة B هي عصير ليمون (pH 2). أيهما الحمض الأقوى، وماذا يحدث لقوة الحموضة كلما هبطت القيمة من 4 نحو 0؟",
            [
                ("Lemon juice (pH 2) is stronger; acidity increases sharply as pH decreases toward 0", "عصير الليمون (pH 2) أقوى حمضية؛ إذ تزداد الحموضة بقوة كلما اقتربنا من 0"),
                ("Tomato juice (pH 4) is stronger because 4 is bigger than 2", "عصير الطماطم (pH 4) أقوى لأن العدد 4 أكبر من 2"),
                ("Both have identical acid strength because both are below 7", "كلاهما متساوي القوة تماماً لمجرد أنهما أقل من 7"),
                ("Acidity drops to zero below pH 3", "تنعدم الحموضة تماماً تحت pH 3"),
            ],
            "On the pH scale, extreme edges (0 and 14) are the strongest; 7 in the middle is weakest/neutral.",
            "الأطراف البعيدة عن 7 (أي قرب 0 للأحماض وقرب 14 للقواعد) هي الأقوى تأثيراً!",
            "Lower pH values represent exponentially stronger acidity (10× per pH unit).",
            ["7 is neutral; moving left toward 0 raises acid strength.", "pH 2 is 2 steps closer to 0 than pH 4 — actually 10 × 10 = 100 times more acidic!"],
            "Similarly, pH 13 is a much stronger base than pH 8.",
            "تزداد قوة الحمض كلما ابتعدنا عن 7 نحو الصفر.",
            ["يقع pH 2 أقرب إلى الصفر من pH 4 بمقدار وحدتين.", "لذلك فإن عصير الليمون أقوى حمضية بنحو مئة ضعف من عصير الطماطم."],
            "كل درجة على مقياس pH تمثل تغيراً بمقدار 10 أضعاف.",
        ),
        (
            12, "Bleach", "مبيض", "Base Strength Check", "مقارنة قوة القواعد",
            "Household bleach has a pH of 12, while seawater has a pH of 8. Which statement correctly compares these two alkaline liquids?",
            "الرقم الهيدروجيني لمبيض الغسيل المنزلي هو 12، بينما لماء البحر نحو 8. أي عبارة تقارن بين هذين السائلين القاعديين بدقة؟",
            [
                ("Bleach (pH 12) is a much stronger, corrosive base than mild seawater (pH 8)", "المبيض (pH 12) قاعدة أقوى بكثير وأكثر كاوية من ماء البحر الخفيف (pH 8)"),
                ("Seawater (pH 8) is stronger because it sits closer to neutral water", "ماء البحر (pH 8) أقوى لأنه أقرب للماء المتعادل"),
                ("Bleach at pH 12 is actually an acid stronger than vinegar", "المبيض عند pH 12 يُعد حمضاً أقوى من الخل"),
                ("Both pH 8 and pH 12 neutralize red litmus back to colorless", "كلاهما يحوّل ورق تباع الشمس إلى شفاف"),
            ],
            "The farther above 7 toward 14, the stronger the base!",
            "كلما ارتفعت القيمة فوق 7 باتجاه 14، زادت قوة القاعدة!",
            "Higher pH above 7 corresponds to stronger alkalinity.",
            ["pH 8 sits just slightly past neutral 7 (mildly basic).", "pH 12 lies near the far basic edge (14), meaning bleach is strongly alkaline and requires gloves."],
            "Distance from 7 measures strength on BOTH sides of the pH scale.",
            "تزداد قوة القلوية كلما اقترب الرقم الهيدروجيني من 14.",
            ["ماء البحر (pH 8) قريب جداً من التعادل فهو قاعدة خفيفة جداً.", "أما المبيض (pH 12) فبعيد عن 7 وقريب من 14 لذا هو قاعدة قوية."],
            "درجة الخطورة تزيد عند طرفي المقياس قرب 0 و14.",
        ),
        (
            7, "Salt+H2O", "ملح+ماء", "Neutralization", "تفاعل التعادل",
            "When an acid such as hydrochloric acid (HCl) reacts completely with a matching base such as sodium hydroxide (NaOH) in balanced amounts, what two neutral products are formed?",
            "عند تفاعل حمض مثل حمض الهيدروكلوريك (HCl) مع كمية مكافئة من قاعدة مثل هيدروكسيد الصوديوم (NaOH)، ما الناتجان المتعادلان من هذا التفاعل؟",
            [
                ("A salt (NaCl) and water (H₂O)", "ملح (كلوريد الصوديوم NaCl) وماء (H₂O)"),
                ("Pure oxygen gas and solid charcoal", "غاز أكسجين نقي وفحم صلب"),
                ("A stronger acid and liquid mercury", "حمض أقوى وزئبق سائل"),
                ("Nitrogen gas and glucose sugar", "غاز نيتروجين وسكر جلوكوز"),
            ],
            "Acid + Base → Salt + Water (neutralization!).",
            "حمض + قاعدة ← ملح + ماء (تفاعل التعادل!).",
            "Neutralization reacts an acid and a base to yield water and an ionic salt.",
            ["H⁺ from the acid pairs with OH⁻ from the base to make neutral H₂O.", "The remaining ions (Na⁺ and Cl⁻) pair into dissolved table salt (NaCl), bringing pH near 7."],
            "General rule: Acid + Base → Salt + Water.",
            "يُلغي الحمض والقاعدة أثر بعضهما في تفاعل التعادل.",
            ["يتحد أيون الهيدروجين من الحمض مع الهيدروكسيد من القاعدة لتكوين الماء المتعادل.", "وتتحد الأيونات المتبقية لتكوين الملح (NaCl) ويقترب pH من 7."],
            "المعادلة العامة: حمض + قاعدة ← ملح + ماء.",
        ),
        (
            2, "Stomach", "المعدة", "Antacid Action", "عمل مضاد الحموضة",
            "A person experiencing acid indigestion takes a chewable antacid tablet containing milk of magnesia (a mild base, pH ~10). How does the tablet soothe the stomach?",
            "شخص يعاني من حرقة المعدة تناول قرصاً مضاداً للحموضة يحتوي على هيدروكسيد المغنيسيوم (قاعدة خفيفة، pH ~10). كيف يخفف القرص آلام المعدة؟",
            [
                ("The mild base neutralizes excess stomach hydrochloric acid, raising pH closer to comfort", "تعادل القاعدة الخفيفة حمض الهيدروكلوريك الزائد في المعدة فترفع الرقم الهيدروجيني نحو التوازن"),
                ("The tablet adds extra concentrated sulfuric acid to speed digestion", "يضيف القرص حمضاً قوياً إضافياً لتسريع الهضم"),
                ("The base freezes stomach liquid below 0°C", "تجمد القاعدة سائل المعدة تحت الصفر المئوي"),
                ("The tablet turns stomach lining directly into cellulose wall", "يحول القرص جدار المعدة إلى سليلوز صلب"),
            ],
            "What neutralizes an excess acid safely? A mild base!",
            "ما المادة التي تعادل الحمض الزائد بأمان؟ قاعدة خفيفة!",
            "Antacids use safe weak bases to neutralize excess gastric acid.",
            ["Stomach acid has a very low pH (~1.5–2).", "An alkaline antacid reacts with excess acid (neutralization), forming mild magnesium salt and water and reducing irritation."],
            "That is also why baking soda paste calms acidic bee stings!",
            "تُستعمل القواعد الخفيفة طبياً لمعادلة الحموضة الزائدة.",
            ["يسبب زيادة حمض المعدة (pH نحو 2) تهيجاً وألماً.", "يتفاعل مضاد الحموضة القاعدي مع الحمض الزائد لتكوين ملح وماء وتهدئة الحموضة."],
            "وللمبدأ نفسه تُعالج لسعة النحلة الحمضية بقاعدة خفيفة كصودا الخبز.",
        ),
    ]
    for ph_v, len_s, lar_s, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in med_ph:
        den, dar = _ph_svgs(ph_v, len_s, lar_s, ten, tar)
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    cab_tbl_en = svg_data_table(
        ["Solution", "Red Cabbage Color", "pH Range"],
        [["Drain cleaner", "Yellow-Green", "12–13"], ["Rainwater", "Purple", "6.5–7"], ["Citrus juice", "Bright Pink", "2–3"]],
        "Red Cabbage Indicator",
        [114, 134, 92],
    )
    cab_tbl_ar = svg_data_table(
        ["المحلول", "لون الملفوف", "مدى pH"],
        [["منظف مصارف", "أخضر مصفر", "12–13"], ["ماء مطر نقي", "بنفسجي", "6.5–7"], ["عصير حمضيات", "وردي ساطع", "2–3"]],
        "كاشف الملفوف الأحمر",
        [112, 118, 92],
    )
    B.add_concept(
        tp, "Medium", bp,
        "Red cabbage juice acts as a natural pH indicator as shown in the table. When a student drops cabbage juice into an unknown clear window cleaner, it turns bright green-yellow. What must the window cleaner be?",
        "يعمل عصير الملفوف الأحمر ككاشف طبيعي للرقم الهيدروجيني كما في الجدول. عندما أضافت طالبة عصير الملفوف إلى منظف زجاج شفاف تحول إلى أخضر مصفر. ما طبيعة المنظف؟",
        [
            ("A strong base (alkaline solution around pH 11–13)", "قاعدة قوية (محلول قلوي بين pH 11–13)"),
            ("A strong acid (around pH 1–2)", "حمض قوي (حول pH 1–2)"),
            ("Neutral distilled water (pH 7)", "ماء مقطر متعادل (pH 7)"),
            ("A non-dissolving mixture of sand and oil", "خليط رمل وزيت غير ذائب"),
        ],
        "Match green-yellow against the Red Cabbage Indicator reference chart.",
        "طابق اللون الأخضر المصفر مع جدول كاشف الملفوف الأحمر المرجعي.",
        "Universal/natural indicators map distinct colors across acidic, neutral, and basic pH ranges.",
        ["Bright pink = acidic (pH 2–3); purple = near neutral (pH 7).", "Yellow-green matches the strongly basic row (pH 12–13), typical of ammonia window cleaners."],
        "Natural pigments like anthocyanins in red cabbage work just like synthetic indicators.",
        "يتغير لون كاشف الملفوف الأحمر حسب درجة الحموضة والقاعدية.",
        ["الوردي يدل على الحمض، والبنفسجي على التعادل.", "الأخضر المصفر يطابق المحاليل القاعدية القوية (11–13) كمنظفات الزجاج والأمونيا."],
        "الصبغات الطبيعية في الملفوف والشاي تغير لونها وفق pH.",
        cab_tbl_en, cab_tbl_ar,
    )

    # Hard (10..14): 4-solution lab table, dilution limit, soil remediation, acid rain marble, unequal neutralization
    ph_tbl_en = svg_data_table(
        ["Liquid", "Blue Litmus", "Red Litmus", "Baking Soda"],
        [["P", "Turns Red", "Stays Red", "Fizzes CO2"], ["Q", "Stays Blue", "Turns Blue", "No fizz"], ["R", "Stays Blue", "Stays Red", "No fizz"]],
        "Unknown Solution Lab",
        [64, 96, 96, 96],
    )
    ph_tbl_ar = svg_data_table(
        ["السائل", "تباع أزرق", "تباع أحمر", "صودا الخبز"],
        [["P", "يصير أحمر", "يبقى أحمر", "فوران CO2"], ["Q", "يبقى أزرق", "يصير أزرق", "لا فوران"], ["R", "يبقى أزرق", "يبقى أحمر", "لا فوران"]],
        "مختبر السوائل المجهولة",
        [62, 96, 96, 98],
    )
    B.add_concept(
        tp, "Hard", bp,
        "A student tests three colorless liquids (P, Q, R) in the table. Which row identifies P, Q, and R correctly?",
        "اختبر طالب ثلاثة سوائل شفافة (P، Q، R) في الجدول المرفق. أي خيار يصنف السوائل P وQ وR بدقة على الترتيب؟",
        [
            ("P = Acid, Q = Base, R = Neutral (e.g., water or salt solution)", "P حمض، و Q قاعدة، و R متعادل (مثل الماء أو محلول الملح)"),
            ("P = Base, Q = Acid, R = Strong Acid", "P قاعدة، و Q حمض، و R حمض قوي"),
            ("P = Neutral, Q = Base, R = Acid", "P متعادل، و Q قاعدة، و R حمض"),
            ("P = Acid, Q = Neutral, R = Base", "P حمض، و Q متعادل، و R قاعدة"),
        ],
        "Notice R leaves BOTH blue and red litmus unchanged! And acids fizz with carbonate baking soda.",
        "لاحظ أن السائل R لا يغيّر أياً من ورقتي تباع الشمس! والأحماض تفور مع بيكربونات الصوديوم.",
        "Combine litmus transitions and carbonate fizz reactivity to identify solutions.",
        ["P turns blue litmus red AND fizzes with baking soda → Acid.", "Q turns red litmus blue → Base. R changes neither litmus strip → Neutral."],
        "All three chemical clues cross-verify cleanly.",
        "يجمع الجدول دلالات تباع الشمس وتفاعل الفوران مع البيكربونات.",
        ["السائل P يحمّر الورق الأزرق ويفور مطلقاً غاز CO₂ ← حمض.", "السائل Q يزرّق الورق الأحمر ← قاعدة، و R لا يغير أي ورقة ← متعادل."],
        "الاختبار المزدوج لورقتي تباع الشمس يؤكد التعادل تماماً.",
        ph_tbl_en, ph_tbl_ar,
    )

    hard_b12 = [
        (
            2, "HCl Acid", "حمض", "Diluting an Acid", "تخفيف الحمض بالماء",
            "Suppose a beaker holds 50 mL of dilute hydrochloric acid at pH 2. If you pour 500 mL of pure distilled water (pH 7) into the acid beaker, what happens to the pH of the mixture?",
            "تحتوي كأس على 50 مل من حمض مخفف عند pH 2. إذا أضفت إليه 500 مل من الماء المقطر النقي (pH 7)، ماذا يحدث لقيمة pH الخليط؟",
            [
                ("The pH rises closer to 7 (around pH 3–4), but never goes above 7 because adding neutral water cannot make an acid basic", "ترتفع قيمة pH مقتربة من 7 (نحو 3–4)، ولكنها لا تتجاوز 7 أبداً لأن إضافة ماء متعادل لا تحوّل الحمض إلى قاعدة"),
                ("The pH jumps from 2 all the way up to pH 12 basic", "تقفز قيمة pH من 2 لتصبح قاعدة قوية عند 12"),
                ("The pH drops down to pH 0 because water makes acid stronger", "تنخفض قيمة pH إلى 0 لأن الماء يجعل الحمض أقوى"),
                ("The pH freezes permanently at exactly 2.00 no matter how much water is added", "تبقى ثابتة تماماً عند 2.00 مهما أضفت من ماء"),
            ],
            "Diluting lemon juice with water makes it less sour (closer to pH 7), NEVER soapy/basic (> 7)!",
            "تخفيف عصير الليمون بالماء يقلل حموضته ليقترب من 7، لكنه لا يصبح صابوناً قاعدياً أبداً!",
            "Dilution weakens acid/base concentration toward neutral 7 without crossing 7.",
            ["Adding pure water spreads acid particles over a larger volume, weakening acidity so pH moves upward toward 7.", "Because water itself is pH 7 (not a base), the mixture remains slightly acidic (< 7)."],
            "Similarly, diluting a pH 12 base with pure water lowers its pH toward 7 without ever dropping below 7.",
            "التخفيف بالماء يقرب الحمض والقاعدة من نقطة التعادل 7 دون أن يتخطاها.",
            ["تقل نسبة تركيز الحمض في الحجم الكبير فترتفع قيمة pH قليلاً نحو 7.", "وبما أن الماء المضاف متعادل (7) فلا توجد أي قاعدة تدفع الرقم فوق 7."],
            "بالمثل، تخفيف قاعدة (pH 12) بالماء يخفض pH نحو 7 فقط.",
        ),
        (
            4, "Acid Rain", "مطر حمضي", "Acid Rain on Marble", "أثر المطر الحمضي",
            "Outdoor marble statues made of calcium carbonate (CaCO₃) slowly pit and crumble in cities exposed to industrial acid rain (pH 4). Why does acid rain damage limestone and marble far faster than clean rainwater?",
            "تتآكل التماثيل والأبنية المصنوعة من الرخام والحجر الجيري (كربونات الكالسيوم CaCO₃) ببطء في المدن المعرضة للمطر الحمضي (pH 4). لماذا يتلف المطر الحمضي الرخام أسرع بكثير من المطر النقي؟",
            [
                ("Acid reacts chemically with calcium carbonate, dissolving it into soluble salts, water, and CO₂ gas", "يتفاعل الحمض كيميائياً مع كربونات الكالسيوم فيذيبها محولاً إياها إلى أملاح ذائبة وماء وغاز CO₂"),
                ("Acid rain turns solid marble physically into shiny liquid mercury", "يحوّل المطر الحمضي الرخام فيزيائياً إلى زئبق سائل"),
                ("Acids increase marble crystal hardness from Mohs 3 to Mohs 10", "تزيد الأحماض صلادة الرخام من 3 إلى 10 على مقياس موهس"),
                ("Rainwater at pH 4 is frozen dry ice that shatters statues", "المطر عند pH 4 عبارة عن ثلج جاف يكسر التماثيل"),
            ],
            "Recall how vinegar (acid) reacts with chalk or baking soda (carbonates)!",
            "تذكر كيف يتفاعل الخل (الحمض) مع الطباشير والرخام (الكربونات)!",
            "Acids chemically corrode carbonate minerals (CaCO₃), forming soluble salts + H₂O + CO₂.",
            ["Rainwater polluted by sulfur/nitrogen oxides drops from ~5.6 down to pH 4.", "When pH 4 rain wets CaCO₃ marble or limestone, chemical weathering eats away the stone surface."],
            "Granite statues (silicate quartz/feldspar) resist acid rain much better than marble!",
            "تتفاعل الأحماض كيميائياً مع معادن الكربونات فتسبب تجوية كيميائية سريعة.",
            ["تحتوي أمطار المصانع الملوثة على أحماض تخفض الرقم الهيدروجيني نحو 4.", "عند سقوطها على الرخام أو الحجر الجيري يتفاعل الحمض مع CaCO₃ وينطلق CO₂ ويتآكل الصخر."],
            "أما الجرانيت فمقاوم أكثر للأمطار الحمضية.",
        ),
    ]
    for ph_v, len_s, lar_s, ten, tar, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car in hard_b12:
        den, dar = _ph_svgs(ph_v, len_s, lar_s, ten, tar)
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_concept(
        tp, "Hard", bp,
        "A farmer tests soil from a neglected field and measures pH 4.5, whereas his crops need neutral soil around pH 7.0. Which soil amendment should he spread to raise the soil pH toward 7.0?",
        "فحص مزارع تربة حقل مهمل فوجد رقمها الهيدروجيني pH 4.5، بينما تحتاج محاصيله إلى تربة متعادلة حول pH 7.0. أي مادة يجب أن يضيفها إلى التربة لرفع رقمها الهيدروجيني نحو 7.0؟",
        [
            ("Crushed agricultural limestone (calcium carbonate, a mild base)", "مسحوق الحجر الجيري الزراعي (كربونات الكالسيوم — قاعدة خفيفة)"),
            ("Concentrated lemon juice or vinegar (acids)", "عصير الليمون المركز أو الخل (أحماض)"),
            ("Pure hydrochloric acid solution", "محلول حمض الهيدروكلوريك"),
            ("Pure table sugar crystals (neutral non-electrolyte)", "بلورات سكر المائدة النقي"),
        ],
        "Soil at pH 4.5 is too ACIDIC. What neutralizes excess acid and pushes pH up toward 7?",
        "التربة عند pH 4.5 شديدة الحموضة! أي مادة تعادل الحموضة الزائدة وترفع pH نحو 7؟",
        "Basic soil amendments (agricultural lime) neutralize acidic soils safely.",
        ["Adding vinegar or HCl would lower pH even further below 4.5.", "Crushed limestone (CaCO₃) reacts with soil acids (neutralization), steadily raising pH toward 7.0."],
        "Agronomists routinely 'lime' overly acidic farmland.",
        "تُعالج التربة الحمضية بإضافة مادة قاعدية خفيفة لمعادلتها.",
        ["الرقم 4.5 يعني تربة حمضية؛ إضافة أحماض أخرى يزيد المشكلة سوءاً.", "مسحوق الحجر الجيري قاعدة آمنة تعادل أحماض التربة وترفع pH تدريجياً إلى 7.0."],
        "يمثل هذا تطبيقاً زراعياً مباشراً لتفاعلات التعادل.",
        _ph_svgs(4.5, "Soil", "التربة", "Acidic Soil Check", "فحص حموضة التربة")[0],
        _ph_svgs(4.5, "Soil", "التربة", "Acidic Soil Check", "فحص حموضة التربة")[1],
    )

    B.add_concept(
        tp, "Hard", bp,
        "In a titration experiment, exactly 25 mL of Acid X completely neutralizes 25 mL of Base Y to reach pH 7.0. What happens if a student accidentally mixes 25 mL of Acid X with ONLY 10 mL of Base Y?",
        "في تجربة معايرة، تعادل 25 مل من الحمض X تماماً 25 مل من القاعدة Y لتصل النتيجة إلى pH 7.0. ماذا يحدث لو مزج طالب بالخطأ 25 مل من الحمض X مع 10 مل فقط من القاعدة Y؟",
        [
            ("Excess unreacted Acid X remains, so the mixture stays acidic (pH < 7) and turns blue litmus red", "يتبقى فائض من الحمض X غير المتعادل فيبقى الخليط حمضياً (pH < 7) ويحمّر ورق تباع الشمس الأزرق"),
            ("The mixture becomes strongly basic (pH > 11) and turns red litmus blue", "يصبح الخليط قاعدياً قوياً (pH > 11) ويزرّق الورق الأحمر"),
            ("Any mixing of acid and base ALWAYS stops precisely at pH 7.0 regardless of volume", "يصل أي مزج بين حمض وقاعدة دائماً إلى pH 7.0 بغض النظر عن الكميات"),
            ("The excess 15 mL of acid evaporates into solid salt instantly", "يتبخر الفائض (15 مل من الحمض) فوراً إلى ملح صلب"),
        ],
        "10 mL of Base Y can only neutralize 10 mL of Acid X — leaving 15 mL of Acid X leftover!",
        "الـ 10 مل من القاعدة Y تعادل 10 مل فقط من الحمض X — فيتبقى 15 مل من الحمض X!",
        "Incomplete neutralization leaves the excess reactant controlling final pH.",
        ["Since X and Y react in a 1:1 volume ratio, 10 mL of Base Y consumes 10 mL of Acid X.", "The remaining 15 mL of un-neutralized Acid X keeps the beaker below pH 7 (acidic)."],
        "Adding 15 mL more Base Y would finish bringing the flask to pH 7.0.",
        "التعادل التام يتطلب نسباً متكافئة، وأي فائض يحدد صفة المحلول النهائي.",
        ["تتفاعل 10 مل من القاعدة مع 10 مل فقط من الحمض.", "يتبقى 15 مل من الحمض X حراً في الإناء، فيظل المحلول حمضياً (pH < 7) ويحمّر تباع الشمس الأزرق."],
        "يلزم إضافة 15 مل أخرى من القاعدة للوصول إلى التعادل التام.",
    )


# ==============================================================================
# TOPIC 3: PHYSICS — FORCES & ENERGY (G6-SCI-B13 .. G6-SCI-B18, 90 Questions)
# ==============================================================================

def _add_b13(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B13"
    # Easy (0..4): Force unit, balanced forces, mass vs weight, friction direction, simple unbalanced force
    easy_b13 = [
        (
            "What SI unit do scientists use to measure the magnitude of a force such as a push, pull, or weight on a spring scale?",
            "ما الوحدة الدولية التي يستخدمها العلماء لقياس مقدار القوة مثل الدفع أو السحب أو الوزن بالميزان النابضي؟",
            [("Newton (N)", "نيوتن (N)"), ("Kilogram (kg)", "كيلوجرام (kg)"), ("Cubic centimeter (cm³)", "سنتيمتر مكعب (cm³)"), ("Degree Celsius (°C)", "درجة مئوية (°C)")],
            "Kilogram measures mass; this unit is named after Sir Isaac Newton.",
            "الكيلوجرام يقيس الكتلة؛ أما وحدة القوة فسميت على اسم العالم إسحاق نيوتن.",
            "Force is measured in newtons (N) using a spring scale.",
            ["Mass is measured in kilograms (kg), volume in cm³.", "Force (push, pull, gravity weight) is measured in newtons (N)."],
            "1 kg of mass weighs roughly 9.8 N (about 10 N) on Earth.",
            "تُقاس القوة بوحدة النيوتن (N) باستخدام الميزان النابضي.",
            ["يقاس الوزن والقوة بالنيوتن لأن الوزن قوة جذب الأرض للجسم.", "أما الكتلة فتقاس بالكيلوجرام أو الجرام."],
            "النيوتن هو الوحدة القياسية للقوة.",
            None, None,
        ),
        (
            "Look at the force diagram showing a 5 kg wooden crate pulled with 25 N to the left and 25 N to the right on a smooth table. What is the net force on the crate, and what happens to its motion if it starts at rest?",
            "انظر لمخطط القوى لصندوق خشبي كتلته 5 كجم يُسحب بقوة 25 نيوتن يساراً و25 نيوتن يميناً على طاولة ملساء. ما القوة المحصلة، وماذا يحدث لحركة الصندوق إذا بدأ من السكون؟",
            [
                ("Net force = 0 N (balanced forces); the crate stays at rest", "القوة المحصلة = 0 نيوتن (قوى متزنة)؛ يبقى الصندوق ساكناً"),
                ("Net force = 50 N right; the crate accelerates rapidly right", "القوة المحصلة = 50 نيوتن يميناً؛ يتسارع الصندوق يميناً"),
                ("Net force = 50 N left; the crate spins vertically upward", "القوة المحصلة = 50 نيوتن يساراً؛ يدور الصندوق للأعلى"),
                ("Net force = 5 N; the crate jumps off the table", "القوة المحصلة = 5 نيوتن؛ يقفز الصندوق عن الطاولة"),
            ],
            "Opposite equal forces cancel each other out: 25 N - 25 N = ?",
            "القوتان المتساويتان المتعاكستان تلغي إحداهما الأخرى: 25 − 25 = ؟",
            "Equal opposite forces produce zero net force (balanced equilibrium).",
            ["Left pull = 25 N, Right pull = 25 N.", "Net force = 25 - 25 = 0 N → balanced forces cause no change in motion, so a stationary crate stays still."],
            "Zero net force never changes an object's velocity.",
            "القوى المتزنة محصلتها صفر ولا تغير حالة الحركة.",
            ["تؤثر قوة 25 نيوتن يميناً و25 نيوتن يساراً فتلغي كل قوة الأخرى.", "المحصلة = 0 نيوتن فيبقى الصندوق الساكن ساكناً."],
            "تتزن القوى عند تساوي المقدار وتعاكس الاتجاه.",
            _force_svgs(25, 25, 5, "Balanced Pulls", "قوى متزنة")[0],
            _force_svgs(25, 25, 5, "Balanced Pulls", "قوى متزنة")[1],
        ),
        (
            "How does an astronaut's MASS compare with her WEIGHT when she travels from Earth's surface to the International Space Station or the Moon?",
            "كيف تتغير كتلة رائدة فضاء مقارنة بوزنها عند انتقالها من سطح الأرض إلى القمر؟",
            [
                ("Her mass stays identical everywhere (amount of matter), while her weight decreases because gravity is weaker", "تبقى كتلتها ثابتة في كل مكان (مقدار المادة)، بينما يقل وزنها لأن الجاذبية أضعف"),
                ("Her weight stays identical everywhere, while her mass drops to zero in space", "يبقى وزنها ثابتاً في كل مكان وتنعدم كتلتها في الفضاء"),
                ("Both mass and weight double on the Moon due to lack of air", "يتضاعف كلٌّ من الكتلة والوزن على القمر لانعدام الهواء"),
                ("Mass is measured in newtons and changes whenever she climbs stairs", "تُقاس الكتلة بالنيوتن وتتغير عند صعود الدرج"),
            ],
            "Mass = how much matter (atoms) make up your body; Weight = gravitational pull on that matter.",
            "الكتلة هي مقدار ما يحتويه الجسم من مادة؛ والوزن هو قوة جذب الكوكب لهذه المادة.",
            "Mass (kg) is invariant; weight (N) scales directly with local gravity.",
            ["Traveling to the Moon removes zero atoms from the astronaut, so mass (kg) stays unchanged.", "Moon gravity is 1/6 of Earth's, so weight (N) drops to 1/6."],
            "Never confuse mass (kg) with gravitational force weight (N)!",
            "الكتلة خاصية ثابتة للجسم، بينما يتغير الوزن بتغير قوة الجاذبية.",
            ["لا تفقد رائدة الفضاء أي مادة من جسمها على القمر، فتبقى كتلتها بالكيلوجرام ثابتة.", "ولأن جاذبية القمر سدس جاذبية الأرض، يقل وزنها بالنيوتن إلى السدس."],
            "يُقاس الوزن بالميزان النابضي والكتلة بالميزان ذي الكفتين.",
            None, None,
        ),
        (
            "A soccer ball rolls eastward across thick grass and gradually slows down until it stops. In which direction does the friction force act on the rolling ball?",
            "تتدحرج كرة قدم شرقاً فوق عشب كثيف وتتباطأ تدريجياً حتى تتوقف. في أي اتجاه تؤثر قوة الاحتكاك على الكرة المتدحرجة؟",
            [
                ("Westward (directly opposite the ball's motion)", "غرباً (بعكس اتجاه حركة الكرة تماماً)"),
                ("Eastward (pushing the ball even faster forward)", "شرقاً (تدفع الكرة للأمام أسرع)"),
                ("Straight upward into the sky", "عمودياً للأعلى نحو السماء"),
                ("Friction acts with zero direction only when the ball stops", "ليس للاحتكاك اتجاه ويظهر فقط بعد التوقف"),
            ],
            "Friction always resists relative sliding/rolling motion between touching surfaces.",
            "قوة الاحتكاك تقاوم دائماً حركة الأجسام المتلامسة وتعاكس اتجاه حركتها.",
            "Friction opposes motion and converts kinetic energy into thermal energy.",
            ["The ball moves East; grass blades rub against it to oppose that motion.", "Therefore, friction pushes West, slowing the ball down."],
            "Rough grass exerts stronger friction than smooth polished wood.",
            "تؤثر قوة الاحتكاك دائماً في اتجاه معاكس لاتجاه الحركة.",
            ["تتحرك الكرة نحو الشرق فيقاوم العشب حركتها بقوة احتكاك متجهة نحو الغرب.", "تؤدي هذه القوة المعاكسة إلى إبطاء الكرة حتى تتوقف."],
            "ويتحول جزء من طاقتها الحركية إلى حرارة.",
            None, None,
        ),
        (
            "In the force diagram shown, a 4 kg sled is pulled with 15 N to the left and 35 N to the right on frictionless ice. What is the net force acting on the sled?",
            "في المخطط الموضح، يُسحب زلاج كتلته 4 كجم بقوة 15 نيوتن يساراً و35 نيوتن يميناً على جليد أملس عديم الاحتكاك. ما القوة المحصلة المؤثرة على الزلاج؟",
            [
                ("20 N to the right (unbalanced)", "20 نيوتن نحو اليمين (قوى غير متزنة)"),
                ("20 N to the left", "20 نيوتن نحو اليسار"),
                ("50 N to the right", "50 نيوتن نحو اليمين"),
                ("0 N (balanced forces)", "0 نيوتن (قوى متزنة)"),
            ],
            "When two forces pull in opposite directions, subtract the smaller force from the larger force and keep the stronger direction.",
            "عندما تكون القوتان متعاكستين، اطرح الصغرى من الكبرى وخُذ اتجاه القوة الأكبر.",
            "Opposing collinear forces subtract; net direction follows the larger force.",
            ["Right force = 35 N, Left force = 15 N.", "Net force = 35 - 15 = 20 N toward the right (larger arrow)."],
            "Because net force ≠ 0, the sled accelerates rightward!",
            "القوتان في اتجاهين متعاكسين فنطرحهما ونختار جهة الأكبر.",
            ["القوة يميناً 35 نيوتن والقوة يساراً 15 نيوتن.", "المحصلة = 35 − 15 = 20 نيوتن نحو اليمين."],
            "القوة المحصلة غير متزنة فتُكسب الزلاج تسارعاً يميناً.",
            _force_svgs(15, 35, 4, "Unbalanced Forces", "قوى غير متزنة")[0],
            _force_svgs(15, 35, 4, "Unbalanced Forces", "قوى غير متزنة")[1],
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b13:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Net force math, opposite direction concept, surface friction table, streamlining, constant velocity = balanced
    B.add_math(
        tp, "Medium", bp,
        "A 6 kg laboratory cart is pulled left with 18 N and simultaneously pulled right with 42 N as shown. What is the magnitude of the net unbalanced force in newtons (N)?",
        "تُسحب عربة مختبر كتلتها 6 كجم بقوة 18 نيوتن نحو اليسار وبقوة 42 نيوتن نحو اليمين في الوقت نفسه كما بالرسم. ما مقدار القوة المحصلة بوحدة النيوتن (N)؟",
        24, [18, 30, 60],
        "Subtract the opposing left force (18 N) from the right force (42 N).",
        "اطرح القوة اليسرى المعاكسة (18 نيوتن) من القوة اليمنى (42 نيوتن).",
        "Net force magnitude for opposite forces = |F_right - F_left|.",
        ["Identify forces: 42 N right and 18 N left.", "Net force = 42 - 18 = 24 N (to the right)."],
        "24 + 18 = 42 N.",
        "لحساب محصلة قوتين متعاكستين نطرح الصغرى من الكبرى.",
        ["القوة يميناً = 42 نيوتن، ويساراً = 18 نيوتن.", "المحصلة = 42 − 18 = 24 نيوتن."],
        "تحقق: 24 + 18 = 42 نيوتن.",
        "",
        _force_svgs(18, 42, 6, "Net Force Calculation", "حساب القوة المحصلة")[0],
        _force_svgs(18, 42, 6, "Net Force Calculation", "حساب القوة المحصلة")[1],
    )

    med_b13 = [
        (
            "In the diagram, a 3 kg wooden box experiences 30 N pulling left and 12 N pulling right. Which arrow describes the box's net force and direction of acceleration?",
            "في المخطط المرفق، يتأثر صندوق كتلته 3 كجم بقوة 30 نيوتن يساراً و12 نيوتن يميناً. ما مقدار واتجاه القوة المحصلة وتسارع الصندوق؟",
            [
                ("18 N to the left", "18 نيوتن نحو اليسار"),
                ("18 N to the right", "18 نيوتن نحو اليمين"),
                ("42 N to the left", "42 نيوتن نحو اليسار"),
                ("0 N (remains stationary)", "0 نيوتن (يبقى ساكناً)"),
            ],
            "Compare 30 N left against 12 N right — which side wins?",
            "قارن 30 نيوتن يساراً مع 12 نيوتن يميناً — أي جهة هي الأقوى؟",
            "Unbalanced forces accelerate an object in the direction of the stronger net force.",
            ["Left pull (30 N) is stronger than right pull (12 N).", "Net force = 30 - 12 = 18 N leftward."],
            "Check: 18 + 12 = 30.",
            "تتجه القوة المحصلة والتسارع في اتجاه القوة الكبرى.",
            ["القوة اليسرى (30 نيوتن) أكبر من اليمنى (12 نيوتن).", "المحصلة = 30 − 12 = 18 نيوتن نحو اليسار."],
            "تحقق: 18 + 12 = 30 نيوتن.",
            _force_svgs(30, 12, 3, "Left vs Right Pull", "سحب يساراً أم يميناً")[0],
            _force_svgs(30, 12, 3, "Left vs Right Pull", "سحب يساراً أم يميناً")[1],
        ),
        (
            "A student uses a spring scale to pull the same 2 kg wooden block across four flat surfaces at a steady speed and logs the pulling force needed in the table. Which surface creates the GREATEST friction, and why do mountain hikers choose deep-treaded rubber boots?",
            "سحب طالب كتلة خشبية وزنها 2 كجم بميزان نابضي بسرعة ثابتة على أربعة أسطح مختلفة وسجل القوة اللازمة في الجدول. أي سطح يُنتج أكبر احتكاك، ولماذا يختار متسلقو الجبال أحذية مطاطية ذات نتوءات خشنة؟",
            [
                ("Sandpaper (11 N); rough deep rubber treads boost friction to prevent slipping on steep rocks", "ورق الصنفرة (11 نيوتن)؛ النتوءات الخشنة تزيد الاحتكاك لمنع الانزلاق على الصخور"),
                ("Polished Ice (1 N); treads eliminate friction completely so boots glide like skates", "الجليد المصقول (1 نيوتن)؛ النتوءات تلغي الاحتكاك تماماً"),
                ("Glass Tile (3 N); smooth rubber reduces air drag on mountain trails", "البلاط الزجاجي (3 نيوتن)؛ المطاط الناعم يقلل مقاومة الهواء"),
                ("Dry Wood (6 N); friction always stops all forward walking on mountains", "الخشب الجاف (6 نيوتن)؛ الاحتكاك يمنع المشي نهائياً"),
            ],
            "More pulling force needed at steady speed = greater opposing friction! Hikers want grip (high friction).",
            "زيادة قوة السحب اللازمة للتحريك تعني احتكاكاً أكبر! ومتسلق الجبال يحتاج إلى تماسك عالٍ لمنع السقوط.",
            "Rougher microscopic surface interlock increases friction force.",
            ["Sandpaper requires the largest force (11 N) because rough grit interlocks strongly with wood.", "Deep rubber boot treads mimic rough grit, increasing traction on slippery rock slopes."],
            "Without friction, neither walking nor car tires could push forward!",
            "تزداد قوة الاحتكاك كلما زادت خشونة السطحين المتلامسين.",
            ["احتاج السحب فوق ورق الصنفرة لأعلى قوة (11 نيوتن) لشدة خشونته.", "كذلك تزيد نتوءات الحذاء الخشن الاحتكاك مع الصخور فتمنع الانزلاق."],
            "الاحتكاك قد يكون مفيداً (في المشي والمكابح) أو ضاراً (في تآكل الآلات).",
            svg_data_table(["Surface", "Pull Force"], [["Polished Ice", "1 N"], ["Glass Tile", "3 N"], ["Dry Wood", "6 N"], ["Sandpaper", "11 N"]], "Surface Friction Lab", [166, 150]),
            svg_data_table(["السطح", "قوة السحب"], [["جليد مصقول", "1 نيوتن"], ["بلاط زجاجي", "3 نيوتن"], ["خشب جاف", "6 نيوتن"], ["ورق صنفرة", "11 نيوتن"]], "مختبر قوة الاحتكاك", [160, 156]),
        ),
        (
            "Why do engineers design the nose of the Haramain High-Speed Rail train in a smooth, tapered bullet shape instead of a flat square wall?",
            "لماذا يصمم المهندسون مقدمة قطار الحرمين السريع بشكل انسيابي مدبب بدلاً من واجهة مربعة مسطحة؟",
            [
                ("To slice smoothly through air molecules, cutting fluid friction (air resistance) and saving energy", "لشق الهواء بسلاسة مما يقلل الاحتكاك المائع (مقاومة الهواء) ويوفر الطاقة"),
                ("To increase air drag so the train stops instantly at every bridge", "لزيادة مقاومة الهواء كي يتوقف القطار عند كل جسر"),
                ("To turn air nitrogen into liquid fuel inside the front windshield", "لتحويل نيتروجين الهواء إلى وقود سائل عند الزجاج الأمامي"),
                ("To raise the train's total mass by adding heavy nose weight", "لزيادة الكتلة الكلية للقطار وإبطاء سرعته"),
            ],
            "Streamlined shapes reduce fluid drag (air and water friction) at high speeds.",
            "الأشكال الانسيابية تقلل مقاومة الموائع (الهواء والماء) عند السرعات العالية.",
            "Aerodynamic streamlining minimizes fluid drag force.",
            ["A blunt flat front slams directly into air, creating high pressure and turbulent drag.", "A sleek tapered nose guides air smoothly past the train body, allowing 300 km/h cruising efficiently."],
            "Dolphins, sharks, and diving peregrine falcons share similar streamlined profiles!",
            "يقلل الشكل الانسيابي من قوة مقاومة الهواء للأجسام سريعة الحركة.",
            ["الواجهة المسطحة تصطدم بكمية كبيرة من الهواء وتبدد طاقة المحرك.", "التصميم الانسيابي يقلل الدوامات والاحتكاك بالهواء فيحقق سرعة عالية باستهلاك أقل."],
            "تحاكي هذه التصاميم شكل الطيور الغواصة والدلافين.",
            None, None,
        ),
        (
            "A 1,200 kg car cruises east along a straight highway at a COMPLETELY CONSTANT speed of 100 km/h. Its engine pushes forward with 400 N while air resistance and tire drag push backward with 400 N. What is the net force on the moving car?",
            "تسير سيارة كتلتها 1200 كجم شرقاً على طريق مستقيم بسرعة ثابتة تماماً قدرها 100 كم/س. يدفع المحرك للأمام بقوة 400 نيوتن وتقاوم الرياح والاحتكاك للخلف بقوة 400 نيوتن. ما القوة المحصلة على السيارة؟",
            [
                ("0 N (balanced forces maintain constant speed in a straight line)", "0 نيوتن (القوى المتزنة تحافظ على سرعة ثابتة في خط مستقيم)"),
                ("800 N eastward", "800 نيوتن شرقاً"),
                ("400 N eastward", "400 نيوتن شرقاً"),
                ("100 N westward", "100 نيوتن غرباً"),
            ],
            "Constant speed in a straight line means ZERO acceleration → forces MUST be balanced!",
            "السرعة الثابتة في خط مستقيم تعني انعدام التسارع ← القوى متزنة ومجموعها صفر!",
            "Balanced forces (F_net = 0) apply equally to rest AND constant-velocity motion.",
            ["Forward drive = 400 N East; backward drag = 400 N West.", "Net force = 400 - 400 = 0 N → no change in speed or direction (steady 100 km/h)."],
            "Common misconception: moving objects do NOT need an unbalanced net force just to keep moving steadily!",
            "لا تعني الحركة المستمرة دائماً وجود قوة محصلة، فالسرعة الثابتة تعني اتزان القوى.",
            ["قوة الدفع 400 نيوتن تساوي تماماً قوة المقاومة 400 نيوتن وتعاكسها.", "المحصلة = 400 − 400 = 0 نيوتن فتستمر السيارة بالسرعة نفسها (100 كم/س) دون زيادة أو نقصان."],
            "تتغير السرعة فقط عندما تصبح القوى غير متزنة.",
            _force_svgs(400, 400, 1200, "Constant Speed Forces", "قوى السرعة الثابتة")[0],
            _force_svgs(400, 400, 1200, "Constant Speed Forces", "قوى السرعة الثابتة")[1],
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b13:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Steady push friction math, Moon/Earth mass & weight table, 3-force equilibrium math, stopping bar chart, seatbelt inertia
    B.add_math(
        tp, "Hard", bp,
        "A student pushes a heavy 10 kg wooden crate steadily to the right across a warehouse floor using a constant 55 N push, and the crate slides at an UNCHANGING steady speed of 1.5 m/s. How many newtons of sliding friction push back to the left?",
        "يدفع طالب صندوقاً خشبياً كتلته 10 كجم نحو اليمين بقوة ثابتة قدرها 55 نيوتن، فينزلق الصندوق على أرضية المستودع بسرعة ثابتة تماماً لا تتغير (1.5 م/ث). كم نيوتن تبلغ قوة الاحتكاك التي تدفع نحو اليسار؟",
        55, [10, 45, 110],
        "Steady constant speed = zero acceleration = balanced horizontal forces (Push = Friction)!",
        "سرعة ثابتة لا تتغير = تسارع صفر = القوى الأفقية متزنة (قوة الدفع = قوة الاحتكاك)!",
        "During constant-velocity sliding, opposing kinetic friction exactly equals applied push.",
        ["Because speed stays constant at 1.5 m/s, net force must be 0 N.", "Therefore, leftward friction = rightward push = 55 N."],
        "55 N right − 55 N left = 0 N net force.",
        "بما أن السرعة ثابتة في خط مستقيم، فإن القوى متزنة ومحصّلتها صفر.",
        ["قوة الدفع لليمين = 55 نيوتن ولا يوجد تسارع.", "إذن قوة الاحتكاك لليسار = 55 نيوتن لتتوازن معها."],
        "تحقق: 55 − 55 = 0 نيوتن.",
        "",
        _force_svgs(0, 55, 10, "Steady Sliding Crate", "انزلاق بسرعة ثابتة")[0],
        _force_svgs(0, 55, 10, "Steady Sliding Crate", "انزلاق بسرعة ثابتة")[1],
    )

    mw_tbl_en = svg_data_table(["Location", "Gravity (N/kg)", "Mass (kg)", "Weight (N)"], [["Earth", "10.0", "60", "600"], ["Moon", "1.6", "?", "?"]], "Earth vs Moon Gravity", [90, 96, 80, 80])
    mw_tbl_ar = svg_data_table(["الموقع", "الجاذبية (N/kg)", "الكتلة (kg)", "الوزن (N)"], [["الأرض", "10.0", "60", "600"], ["القمر", "1.6", "؟", "؟"]], "مقارنة الأرض والقمر", [84, 100, 82, 82])
    B.add_concept(
        tp, "Hard", bp,
        "Using the gravity table (where Earth g ≈ 10 N/kg and Moon g ≈ 1.6 N/kg), what are the astronaut's MASS and WEIGHT on the Moon?",
        "بالاستعانة بجدول الجاذبية (حيث جاذبية الأرض ≈ 10 نيوتن/كجم والقمر ≈ 1.6 نيوتن/كجم)، ما كتلة رائدة الفضاء وما وزنها على سطح القمر على الترتيب؟",
        [
            ("Mass = 60 kg; Weight = 96 N", "الكتلة = 60 كجم؛ والوزن = 96 نيوتن"),
            ("Mass = 9.6 kg; Weight = 600 N", "الكتلة = 9.6 كجم؛ والوزن = 600 نيوتن"),
            ("Mass = 60 kg; Weight = 600 N", "الكتلة = 60 كجم؛ والوزن = 600 نيوتن"),
            ("Mass = 10 kg; Weight = 96 N", "الكتلة = 10 كجم؛ والوزن = 96 نيوتن"),
        ],
        "Mass stays 60 kg! Multiply 60 kg × 1.6 N/kg to get Moon weight in newtons.",
        "الكتلة تبقى 60 كجم! اضرب 60 × 1.6 نيوتن/كجم لإيجاد الوزن على القمر.",
        "Weight = Mass × gravitational field strength (W = m × g).",
        ["Mass never depends on location → remains 60 kg on the Moon.", "Moon weight = 60 × 1.6 = 96 N (about 1/6 of 600 N)."],
        "60 × 1 = 60 and 60 × 0.6 = 36; 60 + 36 = 96 N.",
        "تظل الكتلة ثابتة بينما يُضرب مقدارها في تسارع جاذبية القمر لحساب الوزن.",
        ["الكتلة على القمر = 60 كجم دون نقصان.", "الوزن على القمر = 60 × 1.6 = 96 نيوتن."],
        "60 + 36 = 96 نيوتن.",
        mw_tbl_en, mw_tbl_ar,
    )

    B.add_math(
        tp, "Hard", bp,
        "Three students pull on a heavy equipment box simultaneously: Student A pulls 18 N left, Student B pulls 14 N left, and Student C pulls 50 N right. How many newtons of force must a fourth student pull to the LEFT so the box stays completely balanced (net force = 0 N)?",
        "يسحب ثلاثة طلاب صندوق معدات ثقيلاً معاً: الطالب A يسحب 18 نيوتن يساراً، و B يسحب 14 نيوتن يساراً، و C يسحب 50 نيوتن يميناً. كم نيوتن يجب أن يسحب طالب رابع نحو اليسار لتصبح القوة المحصلة صفراً؟",
        18, [14, 32, 82],
        "Add existing left pulls (18 + 14 = 32 N) and find how much more left pull is needed to match 50 N right.",
        "اجمع قوتي اليسار الحاليتين (18 + 14 = 32 نيوتن) واحسب المتبقي لتساوي 50 نيوتن يميناً.",
        "For static equilibrium, sum of left forces must equal sum of right forces.",
        ["Current left pull = 18 + 14 = 32 N.", "Missing left pull = 50 - 32 = 18 N."],
        "18 + 14 + 18 = 50 N left vs. 50 N right → 0 N net.",
        "عند الاتزان يجب أن يتساوى مجموع القوى يساراً مع مجموع القوى يميناً.",
        ["مجموع القوى يساراً حالياً = 18 + 14 = 32 نيوتن.", "القوة الناقصة يساراً = 50 − 32 = 18 نيوتن."],
        "تحقق: 32 + 18 = 50 نيوتن.",
    )

    hard_b13 = [
        (
            "A student rolls the exact same toy car down the same ramp onto four flat floor surfaces and records how far it glides before stopping in the bar chart. Why did the car roll 4.2 m on oiled vinyl yet only 0.6 m on gravel?",
            "دحرجت طالبة سيارة لعبة من المنحدر نفسه إلى أربعة أسطح مستوية مختلفة وسجلت المسافة التي قطعتها قبل التوقف في الرسم البياني. لماذا انزلقت السيارة مسافة 4.2 م على البلاط المدهون بالزيت مقابل 0.6 م فقط على الحصى؟",
            [
                ("Oil lubrication sharply reduced sliding friction so kinetic energy lasted over a longer distance, whereas rough gravel dissipated kinetic energy rapidly", "قلّل الزيت الاحتكاك بشدة فاستمرت الطاقة الحركية لمسافة أطول، بينما بدّد الحصى الخشن الطاقة الحركية بسرعة"),
                ("Gravity pulled downward ten times harder on gravel than on vinyl", "سحبت الجاذبية السيارة بقوة أكبر عشر مرات فوق الحصى"),
                ("Oiled vinyl added magnetic thrust to the plastic toy wheels", "أضاف الزيت دفعاً مغناطيسياً لعجلات اللعبة البلاستيكية"),
                ("The car weighed less than zero grams once it rolled onto vinyl", "أصبحت كتلة السيارة سالبة فور وصولها إلى البلاط المدهون"),
            ],
            "All runs released from the same ramp height start with the SAME initial speed and kinetic energy!",
            "انطلقت السيارة في كل المحاولات من الارتفاع نفسه أي بنفس السرعة والطاقة الحركية الابتدائية!",
            "Lower friction allows an object to travel farther before work by friction stops it.",
            ["Same ramp height gives identical starting kinetic energy.", "Oiled vinyl exerts tiny opposing friction so stopping takes 4.2 m; gravel exerts huge friction stopping the car in just 0.6 m."],
            "Lubricants (oil/grease) separate surface peaks to reduce wear and heat.",
            "الاحتكاك الصغير يحتاج مسافة طويلة لإيقاف الجسم المتحرك، والاحتكاك الكبير يوقفه سريعاً.",
            ["بدأت السيارة بنفس الطاقة الحركية من نفس المنحدر.", "قللت طبقة الزيت الاحتكاك فواصلت السيارة 4.2 م، أما الحصى الخشن فأوقفها خلال 0.6 م."],
            "تُستخدم الزيوت التشحيمية في المحركات لتقليل الاحتكاك والحرارة.",
            svg_bar_chart([("Gravel", 0.6, RED), ("Carpet", 1.1, ORANGE), ("Wood", 2.4, BLUE), ("Oiled Tile", 4.2, GREEN)], "Glide (m)", "Surface vs Stopping Distance"),
            svg_bar_chart([("حصى", 0.6, RED), ("سجاد", 1.1, ORANGE), ("خشب", 2.4, BLUE), ("بلاط مزيت", 4.2, GREEN)], "المسافة (م)", "السطح مقابل مسافة التوقف"),
        ),
        (
            "When a school bus moving at 60 km/h suddenly slams on its brakes, an unbuckled backpack on the floor slides forward toward the front windshield. Why does the backpack move forward even though the brakes pushed backward?",
            "عندما يضغط سائق حافلة تسير بسرعة 60 كم/س على المكابح فجأة، تنزلق حقيبة غير مثبتة على الأرضية نحو الزجاج الأمامي. لماذا تندفع الحقيبة للأمام رغم أن المكابح أبطأت الحافلة؟",
            [
                ("By inertia, the backpack keeps moving forward at 60 km/h until friction or a seatback exerts an unbalanced backward force on it", "بسبب القصور الذاتي، تحافظ الحقيبة على حركتها للأمام بسرعة 60 كم/س حتى توقفها قوة احتكاك أو حاجز"),
                ("Brakes generate a mysterious forward magnetic wind inside the bus aisle", "تولد المكابح رياحاً مغناطيسية تدفع الحقائب للأمام"),
                ("Gravity suddenly switches from downward to horizontal toward the front", "تتجه الجاذبية الأرضية فجأة إلى الأمام بدلاً من الأسفل"),
                ("Air inside the bus pushes heavier bags backward and light bags forward", "يدفع الهواء الحقائب الخفيفة للأمام عند الفرملة"),
            ],
            "Think about Newton's First Law (inertia): objects in motion tend to keep moving at the same speed and direction!",
            "تذكّر قانون نيوتن الأول (القصور الذاتي): الجسم المتحرك يميل للاستمرار في حركته بالسرعة والاتجاه نفسهما!",
            "Inertia keeps unrestrained passengers/objects moving forward when a vehicle decelerates.",
            ["Before braking, both the bus and backpack moved at 60 km/h.", "Brakes stop the bus wheels/floor first, while inertia carries the unbuckled bag forward until it hits a seat or friction stops it."],
            "That is exactly why seatbelts apply a safe backward force directly to passengers!",
            "القصور الذاتي هو مقاومة الجسم لتغير حالته الحركية.",
            ["كانت الحافلة والحقيبة تتحركان معاً بسرعة 60 كم/س.", "توقفت الحافلة بالمكابح، فاستمرت الحقيبة للأمام بقصورها الذاتي حتى يصطدم مسارها بحاجز."],
            "ولهذا السبب تنقذ أحزمة الأمان الركاب بتوفير قوة إيقاف متدرجة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b13:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b14(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B14"
    # Easy (0..4): Direct v=d/t, distance-time graph slope & stationary line
    B.add_math(
        tp, "Easy", bp,
        "A remote-controlled solar rover travels 180 m across flat sand in 15 seconds. What is its average speed in meters per second (m/s)?",
        "قطعت مركبة روبوت شمسية مسافة 180 متراً على رمل مستوٍ خلال 15 ثانية. ما سرعتها المتوسطة بوحدة متر/ثانية (م/ث)؟",
        12, [10, 15, 165],
        "Use the speed formula: Speed = Distance ÷ Time (v = d / t).",
        "استخدم قانون السرعة: السرعة = المسافة ÷ الزمن.",
        "Average speed equals total distance divided by elapsed time.",
        ["Distance d = 180 m, Time t = 15 s.", "Speed v = 180 ÷ 15 = 12 m/s."],
        "12 × 15 = 180 m.",
        "نحسب السرعة المتوسطة بقسمة المسافة على الزمن.",
        ["المسافة = 180 م، والزمن = 15 ث.", "السرعة = 180 ÷ 15 = 12 م/ث."],
        "تحقق: 12 × 15 = 180 م.",
    )
    B.add_math(
        tp, "Easy", bp,
        "A family drives 240 km from Riyadh toward Qassim in exactly 3 hours. What was the car's average speed in km/h?",
        "قطعت عائلة مسافة 240 كم بالسيارة من الرياض باتجاه القصيم في 3 ساعات تماماً. ما السرعة المتوسطة للسيارة بوحدة كم/ساعة؟",
        80, [60, 90, 237],
        "Divide total kilometers (240) by total hours (3).",
        "اقسم المسافة الكلية بالكيلومترات (240) على عدد الساعات (3).",
        "Speed = Distance ÷ Time.",
        ["d = 240 km, t = 3 h.", "v = 240 ÷ 3 = 80 km/h."],
        "80 × 3 = 240 km.",
        "نقسم المسافة الكلية على الزمن الكلي.",
        ["المسافة = 240 كم، والزمن = 3 ساعات.", "السرعة = 240 ÷ 3 = 80 كم/ساعة."],
        "تحقق: 80 × 3 = 240 كم.",
    )

    g_const = [(0, 0), (2, 12), (4, 24), (6, 36)]
    B.add_math(
        tp, "Easy", bp,
        "Look at the distance-versus-time graph for a sprinter jogging along a straight track. What is the sprinter's constant speed in m/s?",
        "انظر إلى منحنى المسافة مقابل الزمن لعدّاء يهرول في مضمار مستقيم. ما السرعة الثابتة للعدّاء بوحدة م/ث؟",
        6, [3, 12, 36],
        "Pick any point on the straight line (for example t = 6 s, d = 36 m) and compute d ÷ t.",
        "اختر أي نقطة على الخط المستقيم (مثلاً الزمن 6 ث، المسافة 36 م) واقسم المسافة على الزمن.",
        "On a distance-time graph, constant speed equals the slope (change in distance ÷ change in time).",
        ["At t = 6 s, distance d = 36 m (starting from 0 m at t = 0).", "Speed v = 36 ÷ 6 = 6 m/s (check at t = 2 s: 12 ÷ 2 = 6 m/s)."],
        "Every 2 seconds the sprinter covers 12 meters → 6 m/s.",
        "ميل الخط المستقيم في منحنى (المسافة - الزمن) يساوي السرعة.",
        ["عند الزمن 6 ث بلغت المسافة 36 م.", "السرعة = 36 ÷ 6 = 6 م/ث."],
        "تحقق عند 2 ث: 12 ÷ 2 = 6 م/ث.",
        "",
        svg_motion_graph(g_const, "Dist (m)", "Time (s)", "Sprinter Motion Graph"),
        svg_motion_graph(g_const, "المسافة (م)", "الزمن (ث)", "منحنى حركة العدّاء"),
    )

    g_rest = [(0, 0), (2, 20), (5, 20), (7, 40)]
    B.add_concept(
        tp, "Easy", bp,
        "In the distance-versus-time graph of a delivery scooter, what was the scooter doing between t = 2 minutes and t = 5 minutes (where the line is flat and horizontal at 200 m)?",
        "في منحنى المسافة مقابل الزمن لدراجة توصيل، ماذا كانت تفعل الدراجة بين الدقيقة t = 2 والدقيقة t = 5 (حيث الخط أفقي تماماً)؟",
        [
            ("Stopped / completely stationary (speed = 0)", "متوقفة / ساكنة تماماً (السرعة = 0)"),
            ("Coasting downhill at constant high speed", "تنحدر بسرعة عالية ثابتة"),
            ("Accelerating faster every second", "تتسارع باستمرار كل ثانية"),
            ("Driving backward toward the starting store", "ترجع للخلف نحو نقطة الانطلاق"),
        ],
        "Notice distance did NOT change at all between t = 2 and t = 5!",
        "لاحظ أن المسافة لم تتغير مطلقاً بين الزمن 2 والزمن 5!",
        "A horizontal segment on a distance-time graph signifies zero speed (at rest).",
        ["At t = 2, distance = 20; at t = 5, distance is STILL 20.", "Zero distance covered over 3 time units means speed = 0 (resting)."],
        "Remember: horizontal on a distance graph = stopped; horizontal on a speed graph = constant speed!",
        "الخط الأفقي في منحنى المسافة-الزمن يعني ثبات الموقع أي التوقف التام.",
        ["لم تتغير المسافة بين t = 2 و t = 5 بل بقيت عند القيمة نفسها.", "إذن المسافة المقطوعة خلال هذه الفترة = 0 والسرعة = 0."],
        "انتبه: هذا في منحنى المسافة-الزمن وليس السرعة-الزمن.",
        svg_motion_graph(g_rest, "Dist (10m)", "Time (min)", "Delivery Scooter Trip"),
        svg_motion_graph(g_rest, "المسافة (×10م)", "الزمن (د)", "رحلة دراجة التوصيل"),
    )

    sl_tbl_en = svg_data_table(["Cyclist", "t = 0 s", "t = 4 s", "t = 8 s"], [["Nora", "0 m", "16 m", "32 m"], ["Lina", "0 m", "28 m", "56 m"]], "Distance vs Time Table", [84, 78, 78, 78])
    sl_tbl_ar = svg_data_table(["المتسابقة", "0 ث", "4 ث", "8 ث"], [["نورة", "0 م", "16 م", "32 م"], ["لينا", "0 م", "28 م", "56 م"]], "جدول المسافة والزمن", [84, 76, 76, 76])
    B.add_concept(
        tp, "Easy", bp,
        "Look at the cycling data table for Nora and Lina. If both motions were drawn on the same distance-time graph, whose line would be STEEPER and how much faster is she?",
        "انظر لجدول سباق الدراجات بين نورة ولينا. لو رُسمت حركتاهما على منحنى المسافة والزمن نفسه، أيّهما يكون خطها أشد انحداراً وكم تزيد سرعتها؟",
        [
            ("Lina's line is steeper (7 m/s vs. Nora's 4 m/s — 3 m/s faster)", "خط لينا أشد انحداراً (7 م/ث مقابل 4 م/ث لنورة — أسرع بـ 3 م/ث)"),
            ("Nora's line is steeper (4 m/s vs. Lina's 2 m/s)", "خط نورة أشد انحداراً (4 م/ث مقابل 2 م/ث)"),
            ("Both lines have identical steepness", "كلا الخطين لهما الانحدار نفسه"),
            ("Lina's line stays flat at 0 m/s because she started at 0 m", "خط لينا أفقي عند 0 م/ث"),
        ],
        "Compute each cyclist's speed at 8 seconds: distance ÷ 8!",
        "احسب سرعة كل متسابقة عند 8 ثوانٍ: المسافة ÷ 8!",
        "Steeper distance-time slopes represent higher speeds.",
        ["Nora speed = 32 ÷ 8 = 4 m/s.", "Lina speed = 56 ÷ 8 = 7 m/s → Lina travels 3 m/s faster and has the steeper slope."],
        "7 - 4 = 3 m/s difference.",
        "كلما زادت السرعة زاد ميل الخط المستقيم على محور الزمن.",
        ["سرعة نورة = 32 ÷ 8 = 4 م/ث.", "سرعة لينا = 56 ÷ 8 = 7 م/ث، لذا خط لينا أشد ميلاً وتتفوق بـ 3 م/ث."],
        "7 − 4 = 3 م/ث.",
        sl_tbl_en, sl_tbl_ar,
    )

    # Medium (5..9): Solve d=vt, t=d/v, min->hour conversion, segment speed from graph, speed vs velocity
    B.add_math(
        tp, "Medium", bp,
        "A Peregrine falcon dives toward prey at a steady speed of 42 m/s for 8 seconds. How many meters does the falcon travel during those 8 seconds?",
        "ينقضّ صقر الشاهين في السماء بسرعة ثابتة قدرها 42 م/ث لمدة 8 ثوانٍ. ما المسافة التي يقطعها الصقر بالأمتار خلال هذه الثواني الثماني؟",
        336, [50, 294, 420],
        "Rearrange v = d / t to solve for distance: d = v × t.",
        "استعمل قانون المسافة: المسافة = السرعة × الزمن.",
        "Distance = Speed × Time.",
        ["Given v = 42 m/s and t = 8 s.", "Distance d = 42 × 8 = 336 m."],
        "336 ÷ 8 = 42 m/s.",
        "لحساب المسافة نضرب السرعة في الزمن.",
        ["السرعة = 42 م/ث، والزمن = 8 ث.", "المسافة = 42 × 8 = 336 متراً."],
        "تحقق: 336 ÷ 8 = 42 م/ث.",
    )
    B.add_math(
        tp, "Medium", bp,
        "A passenger train travels at an average speed of 180 km/h along a straight desert rail line. How many hours will it take to travel 540 km without stopping?",
        "يسير قطار ركاب بسرعة متوسطة 180 كم/ساعة على خط سكة مستقيم. كم ساعة يستغرق لقطع مسافة 540 كم دون توقف؟",
        3, [2, 4, 360],
        "Solve for time: t = Distance ÷ Speed.",
        "احسب الزمن بقسمة المسافة على السرعة: الزمن = المسافة ÷ السرعة.",
        "Time = Distance ÷ Speed.",
        ["Given d = 540 km and v = 180 km/h.", "Time t = 540 ÷ 180 = 3 hours."],
        "180 × 3 = 540 km.",
        "نقسم المسافة الكلية على السرعة المتوسطة.",
        ["المسافة = 540 كم، والسرعة = 180 كم/ساعة.", "الزمن = 540 ÷ 180 = 3 ساعات."],
        "تحقق: 180 × 3 = 540 كم.",
    )
    B.add_math(
        tp, "Medium", bp,
        "A cyclist rides 6 km along a Corniche bike path in exactly 15 minutes. What is her average speed in kilometers per hour (km/h)?",
        "قطعت راكبة دراجة مسافة 6 كم على مسار الكورنيش في 15 دقيقة تماماً. ما سرعتها المتوسطة بوحدة كم/ساعة؟",
        24, [12, 18, 90],
        "Convert 15 minutes into hours first (15 min = 1/4 hour = 0.25 h), then divide 6 km by 0.25 h!",
        "حوّل 15 دقيقة إلى ساعات أولاً (15 دقيقة = ربع ساعة = 0.25 ساعة)، ثم اقسم 6 كم على 0.25!",
        "Consistent units require converting minutes to hours before computing km/h.",
        ["15 minutes = 15 ÷ 60 = 0.25 h (one-quarter hour).", "Speed = 6 ÷ 0.25 = 6 × 4 = 24 km/h."],
        "6 km every 15 min × 4 quarters per hour = 24 km/h.",
        "نحول الدقائق إلى ساعات أولاً لتتطابق مع وحدة كم/ساعة.",
        ["15 دقيقة = 1/4 ساعة (0.25 ساعة).", "السرعة = 6 ÷ 0.25 = 6 × 4 = 24 كم/ساعة."],
        "كل ربع ساعة تقطع 6 كم، إذن في الساعة الكاملة 24 كم.",
    )

    g_seg = [(0, 0), (2, 16), (4, 16), (6, 40)]
    B.add_math(
        tp, "Medium", bp,
        "Based on the motion graph of a toy train, what was the train's speed in m/s ONLY during the final segment from t = 4 s to t = 6 s?",
        "اعتماداً على منحنى حركة القطار اللعبة، ما سرعة القطار بوحدة م/ث خلال المرحلة الأخيرة فقط من الزمن t = 4 ث إلى t = 6 ث؟",
        12, [6.7, 10, 24],
        "Find distance gained ONLY during t = 4 to t = 6 (40 - 16 = 24 m) and divide by elapsed time (6 - 4 = 2 s).",
        "احسب المسافة المقطوعة خلال هذه الفترة فقط (40 − 16 = 24 م) واقسمها على فرق الزمن (6 − 4 = 2 ث).",
        "Interval speed = (d_end - d_start) ÷ (t_end - t_start).",
        ["Distance gained = 40 - 16 = 24 m.", "Time interval = 6 - 4 = 2 s. Speed = 24 ÷ 2 = 12 m/s."],
        "Segment 1 was 16/2 = 8 m/s; Segment 2 was rest (0); Segment 3 is 12 m/s.",
        "نحسب السرعة في فترة محددة بقسمة التغير في المسافة على التغير في الزمن.",
        ["التغير في المسافة = 40 − 16 = 24 م.", "التغير في الزمن = 6 − 4 = 2 ث ← السرعة = 24 ÷ 2 = 12 م/ث."],
        "المرحلة الأخيرة هي الأسرع في الرسم.",
        "",
        svg_motion_graph(g_seg, "Dist (m)", "Time (s)", "3-Stage Train Trip"),
        svg_motion_graph(g_seg, "المسافة (م)", "الزمن (ث)", "رحلة القطار الثلاثية"),
    )

    B.add_concept(
        tp, "Medium", bp,
        "Car A drives North at 70 km/h and Car B drives East at 70 km/h on intersecting highways. How do their SPEEDS and VELOCITIES compare?",
        "تسير السيارة A شمالاً بسرعة 70 كم/ساعة وتسير السيارة B شرقاً بسرعة 70 كم/ساعة على طريقين متعامدين. كيف نقارن بين سرعتيهما القياسيتين وسرعتيهما المتجهتين؟",
        [
            ("They have the SAME speed (70 km/h) but DIFFERENT velocities (North vs. East)", "لهما نفس مقدار السرعة (70 كم/ساعة) ولكن سرعتيهما المتجهتين مختلفتان (شمال مقابل شرق)"),
            ("They have identical velocities and different speeds", "سرعتاهما المتجهتان متطابقتان ومقدارهما مختلف"),
            ("Neither speed nor velocity depends on direction", "لا تعتمد السرعة القياسية ولا المتجهة على الاتجاه"),
            ("Car A has double the velocity of Car B because North points upward", "للسيارة A ضعف السرعة المتجهة لأن الشمال يشير للأعلى"),
        ],
        "Speed = how fast (scalar); Velocity = speed PLUS direction (vector)!",
        "السرعة القياسية هي المقدار فقط؛ أما السرعة المتجهة فتجمع المقدار + الاتجاه!",
        "Velocity specifies both speed magnitude and motion direction.",
        ["Both cars cover 70 km per hour → equal speeds.", "Because Car A heads North and Car B heads East, their velocities differ."],
        "Changing direction (turning a corner) changes velocity even at steady speedometer reading!",
        "تختلف السرعة المتجهة باختلاف الاتجاه ولو تساوى المقدار.",
        ["تقطع السيارتان 70 كم كل ساعة فمقدار السرعة متساوٍ.", "لكن إحداهما تتجه شمالاً والأخرى شرقاً فسرعتهما المتجهة مختلفة."],
        "تغيّر الاتجاه يغير السرعة المتجهة وينتج تسارعاً.",
        None, None,
    )

    # Hard (10..14): Two-stage harmonic trap, average speed incl rest, overtake catch-up, 4-segment graph analysis, circular motion velocity
    B.add_math(
        tp, "Hard", bp,
        "A car drives 120 km at 60 km/h and then drives another 120 km at 40 km/h. What is the car's TRUE average speed in km/h for the entire 240 km trip?",
        "قطعت سيارة 120 كم بسرعة 60 كم/ساعة ثم قطعت 120 كم أخرى بسرعة 40 كم/ساعة. ما السرعة المتوسطة الحقيقية للسيارة بوحدة كم/ساعة لكامل الرحلة (240 كم)؟",
        48, [45, 50, 52],
        "Do NOT average 60 and 40 to get 50! Find the time for EACH leg first, then divide total distance (240 km) by total time.",
        "احذر من أخذ المتوسط الحسابي (50)! احسب زمن كل مرحلة أولاً ثم اقسم المسافة الكلية (240 كم) على الزمن الكلي.",
        "Average speed always equals Total Distance ÷ Total Time.",
        ["Leg 1 time = 120 ÷ 60 = 2 h. Leg 2 time = 120 ÷ 40 = 3 h.", "Total time = 2 + 3 = 5 h. Average speed = 240 ÷ 5 = 48 km/h!"],
        "Notice the car spent more time (3 h vs. 2 h) driving slowly, pulling the average below 50!",
        "السرعة المتوسطة للرحلة الكاملة = المسافة الكلية ÷ الزمن الكلي.",
        ["زمن المرحلة الأولى = 120 ÷ 60 = ساعتان؛ زمن الثانية = 120 ÷ 40 = 3 ساعات.", "الزمن الكلي = 5 ساعات ← السرعة المتوسطة = 240 ÷ 5 = 48 كم/ساعة."],
        "لأن السيارة قضت زمناً أطول في السرعة الأبطأ (40)، انخفض المتوسط عن 50.",
    )

    g_avg = [(0, 0), (2, 40), (4, 40), (6, 120)]
    B.add_math(
        tp, "Hard", bp,
        "Look at the motion graph of a bike messenger who rides 40 m in 2 s, rests for 2 s, then rides from 40 m to 120 m in the final 2 s. Including the 2-second rest stop, what was the messenger's overall average speed in m/s for the full 6-second trip?",
        "انظر لمنحنى حركة ساعي دراجة قطع 40 م في ثانيتين، ثم توقف ثانيتين، ثم واصل من 40 م إلى 120 م في الثانيتين الأخيرتين. بحساب زمن التوقف، ما السرعة المتوسطة الكلية بوحدة م/ث للرحلة كلها (6 ثوانٍ)؟",
        20, [25, 30, 40],
        "Total distance at t = 6 s is 120 m; total elapsed time INCLUDING rest is 6 s!",
        "المسافة الكلية عند 6 ثوانٍ هي 120 متراً، والزمن الكلي شاملاً التوقف هو 6 ثوانٍ!",
        "Overall average speed divides total distance by total elapsed time (including stops).",
        ["Total distance = 120 m.", "Total time = 6 s → Overall average speed = 120 ÷ 6 = 20 m/s."],
        "Resting lowers overall average speed even though active speeds were 20 m/s and 40 m/s.",
        "السرعة المتوسطة الكلية تشمل فترات التوقف ضمن الزمن الكلي.",
        ["المسافة الإجمالية المقطوعة = 120 م، والزمن الإجمالي = 6 ث.", "السرعة المتوسطة الكلية = 120 ÷ 6 = 20 م/ث."],
        "تحقق: 20 × 6 = 120 م.",
        "",
        svg_motion_graph(g_avg, "Dist (m)", "Time (s)", "Trip With Rest Stop"),
        svg_motion_graph(g_avg, "المسافة (م)", "الزمن (ث)", "رحلة مع توقف"),
    )

    B.add_math(
        tp, "Hard", bp,
        "During a track drill, Runner A starts 30 m ahead on the straight track and jogs steadily at 5 m/s. At the exact same moment, Runner B starts from the 0 m line and sprints steadily at 8 m/s in the same direction. How many seconds does it take Runner B to catch up to Runner A?",
        "في تمرين جري، يبدأ المتسابق A متقدماً بمقدار 30 متراً ويجري بسرعة ثابتة 5 م/ث. في اللحظة نفسها يبدأ المتسابق B من نقطة الصفر ويجري في الاتجاه نفسه بسرعة 8 م/ث. بعد كم ثانية يلحق المتسابق B بالمتسابق A؟",
        10, [6, 15, 30],
        "Each second, Runner B closes the 30 m gap by (8 - 5) = 3 meters! Divide 30 m by 3 m/s.",
        "يُغلق المتسابق B الفارق (30 متراً) بمعدل (8 − 5) = 3 أمتار كل ثانية! اقسم 30 على 3.",
        "Catch-up time = Initial gap ÷ Relative closing speed.",
        ["Closing speed = 8 - 5 = 3 m/s.", "Time to close 30 m = 30 ÷ 3 = 10 s."],
        "Check at t = 10 s: A is at 30 + 5(10) = 80 m; B is at 8(10) = 80 m!",
        "نستخدم السرعة النسبية لإغلاق الفارق الابتدائي بين المتسابقين.",
        ["سرعة الاقتراب = 8 − 5 = 3 م/ث.", "زمن اللحاق = 30 ÷ 3 = 10 ثوانٍ."],
        "التحقق عند 10 ث: موقع A = 30 + 50 = 80 م، وموقع B = 80 م.",
    )

    g_4seg = [(0, 0), (2, 10), (5, 10), (7, 50), (8, 50)]
    B.add_concept(
        tp, "Hard", bp,
        "Analyze the 4-part motion graph of an automated warehouse cart. How many TOTAL seconds did the cart spend stopped, and what was its fastest moving speed?",
        "حلّل منحنى الحركة رباعي المراحل لعربة مستودع آلية. كم مجموع الثواني التي توقفت خلالها العربة كلياً، وما أقصى سرعة بلغتها أثناء الحركة؟",
        [
            ("Stopped for 4 seconds total (3 s + 1 s); fastest speed = 20 m/s (from t = 5 to 7 s)", "توقفت 4 ثوانٍ إجمالاً (3 ث + 1 ث)؛ وأقصى سرعة = 20 م/ث (من t = 5 إلى 7 ث)"),
            ("Stopped for 3 seconds total; fastest speed = 50 m/s", "توقفت 3 ثوانٍ إجمالاً؛ وأقصى سرعة = 50 م/ث"),
            ("Stopped for 2 seconds total; fastest speed = 10 m/s", "توقفت ثانيتين إجمالاً؛ وأقصى سرعة = 10 م/ث"),
            ("Never stopped; fastest speed = 5 m/s", "لم تتوقف أبداً؛ وأقصى سرعة = 5 م/ث"),
        ],
        "Count BOTH horizontal flat sections (t = 2..5 and t = 7..8), and compute slope (50 - 10) ÷ (7 - 5)!",
        "احسب فترتي الخط الأفقي معاً (من 2 إلى 5، ومن 7 إلى 8)، واحسب ميل القطعة الأشد انحداراً (50 − 10) ÷ (7 − 5)!",
        "Identify multiple rest intervals and steepest slope on a multi-stage distance-time graph.",
        ["Flat rest segments: (5 - 2) = 3 s AND (8 - 7) = 1 s → 3 + 1 = 4 s stopped.", "Steepest moving interval t = 5..7 s covers (50 - 10) = 40 m in 2 s → 20 m/s (vs. 5 m/s in t = 0..2)."],
        "Notice total distance at t = 8 s is 50 m.",
        "الخطوط الأفقية تمثل التوقف، والقطعة الأكثر انحداراً تمثل أعلى سرعة.",
        ["فترات التوقف: من 2 إلى 5 (3 ث) + من 7 إلى 8 (1 ث) = 4 ثوانٍ.", "أشد ميل من 5 إلى 7 ث: (50 − 10) ÷ (7 − 5) = 40 ÷ 2 = 20 م/ث."],
        "تم جمع فترتي التوقف مع حساب ميل المرحلة الثالثة بدقة.",
        svg_motion_graph(g_4seg, "Dist (m)", "Time (s)", "Warehouse Cart Log"),
        svg_motion_graph(g_4seg, "المسافة (م)", "الزمن (ث)", "سجل عربة المستودع"),
    )

    B.add_concept(
        tp, "Hard", bp,
        "A go-kart races around a circular track while its speedometer stays locked at an exact steady 15 m/s. Why do physicists say the go-kart's velocity is changing and an unbalanced inward force MUST act on it?",
        "تدور سيارة سباق صغيرة في مضمار دائري مع ثبات قراءة عداد السرعة تماماً عند 15 م/ث. لماذا يؤكد الفيزيائيون أن سرعتها المتجهة تتغير وأن قوة غير متزنة للداخل تؤثر عليها؟",
        [
            ("Because velocity includes direction, and turning in a circle continuously changes the go-kart's direction via inward friction", "لأن السرعة المتجهة تشمل الاتجاه، والدوران يغيّر اتجاه الحركة باستمرار بفعل قوة احتكاك متجهة لمركز الدائرة"),
            ("Because circular motion makes mass drop to zero every half lap", "لأن الحركة الدائرية تجعل الكتلة تساوي صفراً كل نصف دورة"),
            ("Because speedometers always lag 15 m/s behind gravity", "لأن عدادات السرعة تتأخر بمقدار 15 م/ث عن الجاذبية"),
            ("Because turning in circles creates balanced 0 N net force automatically", "لأن الدوران يخلق توازناً تلقائياً للقوى عند 0 نيوتن"),
        ],
        "Velocity = speed + direction! What happens to direction every instant on a circular loop?",
        "السرعة المتجهة = مقدار + اتجاه! ماذا يحدث للاتجاه في كل لحظة على المسار الدائري؟",
        "Uniform circular motion constantly changes velocity direction via inward centripetal force.",
        ["Even at steady 15 m/s speed, the kart turns from North → West → South → East.", "Changing direction means velocity changes (acceleration), requiring an unbalanced inward force (tire friction toward center)."],
        "If tires hit slick oil (zero inward friction), inertia sends the kart straight off the tangent!",
        "تغير الاتجاه المستمر يعني تغير السرعة المتجهة ووجود تسارع.",
        ["رغم ثبات المقدار (15 م/ث)، يتغير اتجاه السيارة في كل نقطة على الدائرة.", "يلزم قوة غير متزنة نحو مركز الدائرة (احتكاك الإطارات) لإجبارها على الدوران."],
        "لو زال هذا الاحتكاك لانزلقت السيارة في خط مستقيم بالقصور الذاتي.",
        None, None,
    )


def _add_b15(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B15"
    # Easy (0..4): Lever parts, Class 2 lever, inclined plane, fixed pulley, wedge/screw
    easy_b15 = [
        (
            "In a playground seesaw or crowbar lever, what is the fixed pivot point around which the rigid bar turns?",
            "في الأرجوحة التوازنية (السي سو) أو العتلة، ما النقطة الثابتة التي يرتكز عليها القضيب الصلب ويدور حولها؟",
            [("Fulcrum", "نقطة الارتكاز"), ("Load arm", "ذراع المقاومة"), ("Inclined plane", "المستوى المائل"), ("Pulley wheel", "بكرة الرفع")],
            "A lever has three key parts: Load (resistance), Effort (applied push/pull), and the pivot triangle!",
            "تتكون الرافعة من ثلاثة عناصر: المقاومة، والقوة المبذولة، ونقطة الدوران المثلثة!",
            "The fulcrum is the pivot point supporting a lever.",
            ["A lever pivots around its fulcrum.", "Changing where the fulcrum sits alters effort force vs. distance moved."],
            "Triangle symbol in lever diagrams always marks the fulcrum.",
            "نقطة الارتكاز هي المحور الثابت الذي تدور حوله الرافعة.",
            ["تربط نقطة الارتكاز ذراعي القوة والمقاومة.", "تغيّر موضعها يحدد الفائدة الآلية للرافعة."],
            "يمثل المثلث تحت العارضة في الرسم نقطة الارتكاز.",
            svg_lever_diagram(150, "Load", "Effort", "Load Arm", "Effort Arm", "Parts of a Lever"),
            svg_lever_diagram(150, "مقاومة", "قوة", "ذراع المقاومة", "ذراع القوة", "أجزاء الرافعة"),
        ),
        (
            "Why does pushing a heavy refrigerator up a 4 m wooden ramp into a delivery truck require far less pushing force than lifting it straight vertically up 1 m?",
            "لماذا يتطلب دفع ثلاجة ثقيلة فوق منحدر خشبي طوله 4 م إلى شاحنة قوةً أقل بكثير من رفعها رأسياً مباشرة لمسافة 1 م؟",
            [
                ("An inclined plane spreads the same lifting work over a longer distance, reducing the required push force", "لأن المستوى المائل يوزع الشغل نفسه على مسافة أطول فيقلل القوة اللازمة للدفع"),
                ("The wooden ramp reduces the refrigerator's mass to one-fourth", "لأن المنحدر الخشبي يقلل كتلة الثلاجة إلى الربع"),
                ("Gravity disappears completely on slanted wooden boards", "لأن الجاذبية تنعدم تماماً فوق الألواح المائلة"),
                ("An inclined plane creates extra electrical energy inside the truck", "لأن المستوى المائل يولد طاقة كهربائية إضافية"),
            ],
            "Remember: Work = Force × Distance. Longer distance means smaller force!",
            "تذكر: الشغل = القوة × المسافة؛ زيادة المسافة تقلل القوة اللازمة!",
            "Inclined planes trade greater push distance for smaller effort force.",
            ["Raising the fridge 1 m requires a fixed gravitational potential energy gain.", "Pushing along 4 m instead of lifting 1 m cuts ideal force to 1/4 while increasing travel distance 4×."],
            "Simple machines NEVER reduce ideal work — they make work easier by lowering force!",
            "المستوى المائل آلة بسيطة تقلل القوة المطلوبة بزيادة المسافة.",
            ["رفع الثلاجة رأسياً يتطلب قوة كبيرة لمسافة قصيرة (1 م).", "دفعها على المنحدر (4 م) يقلل القوة إلى الربع تقريباً لأن الشغل يتوزع على مسافة أطول."],
            "الآلة البسيطة تغير القوة أو المسافة ولا تختصر الشغل المثالي.",
            svg_ramp_diagram("Ramp: 4 m", "H: 1 m", "Fridge", "Inclined Plane Ramp"),
            svg_ramp_diagram("طول: 4 م", "ارتفاع: 1 م", "ثلاجة", "المستوى المائل"),
        ),
        (
            "A school flagpole has a single FIXED pulley mounted at the top of the pole. When a student pulls the rope downward with 25 N to lift a 25 N flag upward, what advantage does this fixed pulley provide?",
            "يوجد أعلى سارية المدرسة بكرة مفردة ثابتة. عندما يسحب طالب الحبل للأسفل بقوة 25 نيوتن لرفع علم وزنه 25 نيوتن للأعلى، ما الفائدة التي تقدمها البكرة الثابتة؟",
            [
                ("It changes the direction of the pull (pulling comfortably downward instead of climbing up), with mechanical advantage = 1", "تغيّر اتجاه القوة (السحب المريح للأسفل بدلاً من الصعود للأعلى) بفائدة آلية تساوي 1"),
                ("It cuts the flag's weight in half to 12.5 N", "تقلل وزن العلم إلى النصف ليصبح 12.5 نيوتن"),
                ("It multiplies force by 4 while keeping rope distance equal", "تضاعف القوة أربع مرات"),
                ("It eliminates gravity from the cotton flag fabric", "تلغي الجاذبية عن قماش العلم"),
            ],
            "Does pulling 1 m of rope down raise the flag 1 m up? Then force stays 25 N, only direction reverses!",
            "إذا سحبت متراً من الحبل للأسفل يرتفع العلم متراً للأعلى — أي القوة نفسها مع تغيير مريح للاتجاه!",
            "A single fixed pulley has MA = 1 and works solely by reversing force direction.",
            ["One rope segment supports the flag directly, so Effort = Load = 25 N.", "Pulling downward lets gravity and body weight assist you comfortably from the ground."],
            "To actually halve the force (MA = 2), you need a MOVABLE pulley riding with the load.",
            "البكرة الثابتة المفردة فائدتها الآلية 1 وتغير اتجاه السحب فقط.",
            ["تحمل البكرة الثابتة الحبل بفرع واحد فتساوي القوة المبذولة وزن العلم (25 نيوتن).", "لكنها تجعل السحب للأسفل أسهل وأكثر أماناً من الرفع للأعلى."],
            "أما البكرة المتحركة فتضاعف القوة (فائدة آلية = 2).",
            None, None,
        ),
        (
            "In a wheelbarrow used by a gardener, the wheel axle at the front is the fulcrum, the heavy soil sits inside the bucket in the middle (load), and the gardener lifts the handles at the back (effort). Which class of lever is a wheelbarrow?",
            "في عربة اليد الزراعية، يقع محور العجلة (نقطة الارتكاز) في الأمام، والتراب الثقيل (المقاومة) في المنتصف، ويدفع البستاني المقابض (القوة) من الخلف. أي نوع من الروافع تمثل عربة اليد؟",
            [
                ("Class 2 lever (load in the middle, always giving mechanical advantage > 1)", "رافعة من النوع الثاني (المقاومة في المنتصف، وتضاعف القوة دائماً)"),
                ("Class 1 lever (fulcrum in the middle like a seesaw)", "رافعة من النوع الأول (الارتكاز في المنتصف كالأرجوحة)"),
                ("Class 3 lever (effort in the middle like tweezers)", "رافعة من النوع الثالث (القوة في المنتصف كالملقط)"),
                ("Fixed pulley system with zero fulcrum", "نظام بكرة ثابتة بلا نقطة ارتكاز"),
            ],
            "Use the middle-item memory rule 'FLE 1-2-3': Fulcrum middle = Class 1; Load middle = Class 2; Effort middle = Class 3!",
            "تذكّر موقع العنصر الأوسط: الارتكاز بالوسط = أول؛ المقاومة بالوسط = ثانٍ؛ القوة بالوسط = ثالث!",
            "Class 2 levers place the load between fulcrum and effort, ensuring effort arm > load arm.",
            ["In a wheelbarrow (and nutcracker), the Load lies between Fulcrum (wheel) and Effort (handles).", "Because effort is always farther from the wheel than the load, MA > 1 always multiplies force."],
            "Class 2 levers make heavy lifting far easier!",
            "في رافعة النوع الثاني تقع المقاومة بين نقطة الارتكاز والقوة المبذولة.",
            ["تقع التربة (المقاومة) في حوض العربة بين العجلة (الارتكاز) والمقابض (القوة).", "يكون ذراع القوة أطول دائماً من ذراع المقاومة فتضاعف العربة القوة."],
            "تعد كسارة البندق وعربة اليد أشهر أمثلة النوع الثاني.",
            None, None,
        ),
        (
            "A kitchen knife blade, a wood-splitting axe, and a metal jar-lid thread are everyday simple machines. How are a knife blade and jar-lid threads classified?",
            "تُعد شفرة سكين المطبخ وفأس تقطيع الخشب وسنّ غطاء البرطمان الحلزوني آلات بسيطة يومية. كيف يُصنف كلٌّ من شفرة السكين وسنّ الغطاء الحلزوني؟",
            [
                ("Knife blade = Wedge; jar-lid thread = Screw (wrapped inclined plane)", "شفرة السكين إسفين، وسنّ الغطاء برغي (مستوى مائل ملتف)"),
                ("Knife blade = Pulley; jar-lid thread = Class 1 lever", "شفرة السكين بكرة، وسنّ الغطاء رافعة أولى"),
                ("Both are strictly wheel-and-axle gears", "كلاهما عجلة ومحور فقط"),
                ("Knife blade = Screw; jar-lid thread = Fixed fulcrum", "شفرة السكين برغي، وسنّ الغطاء نقطة ارتكاز"),
            ],
            "Both wedges and screws belong to the inclined-plane family!",
            "كلٌّ من الإسفين والبرغي ينتمي لعائلة المستوى المائل!",
            "Wedges are moving inclined planes; screws are inclined planes wrapped around a cylinder.",
            ["A sharp knife or axe concentrates force sideways to split materials apart → wedge.", "Spiral jar-lid threads turn rotation over a long spiral ramp into tight clamping force → screw."],
            "That completes the 6 simple machines: lever, pulley, wheel & axle, inclined plane, wedge, screw.",
            "الإسفين مستوى مائل متحرك للفصل والقطع، والبرغي مستوى مائل ملتف حول أسطوانة.",
            ["تركز شفرة السكين والفأس القوة لقطع المواد أو شقها (إسفين).", "تحوّل لوالب الغطاء الدوران لمسافة طويلة إلى قوة إغلاق محكمة (برغي)."],
            "جميعها تندرج ضمن الآلات البسيطة الست.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b15:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Lever MA math, ramp MA math, Class 3 trade-off, movable pulley math, wheel & axle
    B.add_math(
        tp, "Medium", bp,
        "Workers use a sturdy crowbar lever to lift a 120 N rock. The rock sits 1 m from the fulcrum, while the worker pushes down 4 m from the fulcrum as shown. Ignoring bar weight, how many newtons of downward effort force are needed to lift the rock?",
        "يستخدم عمال عتلة متينة لرفع صخرة وزنها 120 نيوتن. تبعد الصخرة 1 م عن نقطة الارتكاز بينما يضغط العامل للأسفل على بُعد 4 م من الارتكاز كما في الرسم. كم نيوتن من القوة يحتاج العامل لرفع الصخرة؟",
        30, [40, 120, 480],
        "Mechanical advantage MA = Effort Arm ÷ Load Arm = 4 ÷ 1 = 4. Divide load (120 N) by MA!",
        "الفائدة الآلية = ذراع القوة ÷ ذراع المقاومة = 4 ÷ 1 = 4. اقسم وزن الصخرة (120 نيوتن) على 4!",
        "Lever mechanical advantage equals Effort Arm ÷ Load Arm.",
        ["MA = 4 m ÷ 1 m = 4.", "Required Effort = Load ÷ MA = 120 ÷ 4 = 30 N."],
        "Torque check: 120 N × 1 m = 30 N × 4 m = 120 N·m.",
        "تساوي الفائدة الآلية للرافعة نسبة ذراع القوة إلى ذراع المقاومة.",
        ["الفائدة الآلية = 4 م ÷ 1 م = 4.", "القوة اللازمة = المقاومة ÷ الفائدة الآلية = 120 ÷ 4 = 30 نيوتن."],
        "تحقق من التوازن: 120 × 1 = 30 × 4.",
        "",
        svg_lever_diagram(112, "120 N", "Effort ?", "1 m", "4 m", "Crowbar Lever MA"),
        svg_lever_diagram(112, "120 نيوتن", "قوة ؟", "1 م", "4 م", "حساب فائدة العتلة"),
    )

    B.add_math(
        tp, "Medium", bp,
        "A mover pushes a 300 N piano up a smooth frictionless ramp that is 6 m long and rises 2 m high into a stage. What is the ideal effort force in newtons needed along the ramp?",
        "يدفع عامل بيانو وزنه 300 نيوتن صعوداً على منحدر أملس عديم الاحتكاك طوله 6 م وارتفاعه 2 م نحو مسرح. ما القوة المثالية اللازمة لدفع البيانو على طول المنحدر بالنيوتن؟",
        100, [50, 150, 600],
        "Ramp MA = Length ÷ Height = 6 ÷ 2 = 3. Divide Load (300 N) by 3!",
        "الفائدة الآلية للمنحدر = الطول ÷ الارتفاع = 6 ÷ 2 = 3. اقسم الوزن (300 نيوتن) على 3!",
        "Inclined plane ideal MA = Ramp Length ÷ Vertical Height.",
        ["MA = 6 m ÷ 2 m = 3.", "Effort force = 300 ÷ 3 = 100 N."],
        "Ideal work check: 100 N × 6 m = 300 N × 2 m = 600 J.",
        "الفائدة الآلية للمستوى المائل = طول المنحدر ÷ ارتفاعه الرأسي.",
        ["الفائدة الآلية = 6 ÷ 2 = 3.", "القوة المثالية = 300 ÷ 3 = 100 نيوتن."],
        "تحقق الشغل: 100 × 6 = 300 × 2 = 600 جول.",
        "",
        svg_ramp_diagram("Length: 6 m", "Height: 2 m", "300 N", "Ramp Advantage"),
        svg_ramp_diagram("الطول: 6 م", "الارتفاع: 2 م", "300 نيوتن", "فائدة المستوى المائل"),
    )

    med_b15 = [
        (
            "Kitchen tongs, tweezers, and a baseball bat are Class 3 levers where the effort is applied between the fulcrum and the load (giving MA < 1, requiring MORE effort force than the load weight). Why are Class 3 levers still so useful?",
            "تُعد الملاقط الطبية ومضرب البيسبول والذراع البشرية روافع من النوع الثالث حيث تقع القوة في المنتصف فتكون فائدتها الآلية أقل من 1 (تحتاج قوة أكبر من المقاومة). فلماذا تظل هذه الروافع شديدة الفائدة؟",
            [
                ("They multiply distance and speed at the output tip, allowing quick wide sweeps or delicate precision", "لأنها تضاعف المسافة والسرعة عند الطرف المتحرك فتمنح حركة سريعة واسعة أو دقة عالية"),
                ("They create infinite electrical energy without muscle work", "لأنها تنتج طاقة كهربائية لا نهائية دون جهد عضلي"),
                ("They reduce the mass of any grasped object by 90%", "لأنها تقلل كتلة الأجسام الممسوكة بنسبة 90%"),
                ("They allow lifting 10-ton boulders using a single finger", "لأنها تتيح رفع صخور تزن 10 أطنان بإصبع واحد"),
            ],
            "Think about why your forearm moves 5 cm near the elbow while your hand swings 40 cm rapidly to throw a ball!",
            "فكر كيف تتحرك عضلة الذراع بضعة سنتيمترات لتقطع اليد مسافة سريعة وواسعة عند رمي كرة!",
            "Class 3 levers sacrifice force advantage to amplify output speed and range of motion.",
            ["When effort arm < load arm, you pull harder than the load weight.", "In exchange, the far tip moves much farther and faster — ideal for brooms, fishing rods, and human arms."],
            "Force × Distance stays balanced either way!",
            "تضحي روافع النوع الثالث بمضاعفة القوة مقابل زيادة السرعة ومدى الحركة.",
            ["عندما يكون ذراع القوة أقصر من ذراع المقاومة، نبذل قوة أكبر.", "في المقابل يتحرك الطرف البعيد بسرعة أكبر ولمسافة أوسع كما في المكنسة وسنارة الصيد."],
            "وهكذا تناسب المهام السريعة والدقيقة.",
            svg_lever_diagram(56, "Fulcrum", "Load", "Effort", "Long Arm", "Class 3 Lever"),
            svg_lever_diagram(56, "الارتكاز", "المقاومة", "القوة", "ذراع طويل", "رافعة النوع الثالث"),
        ),
        (
            "Why is turning a round doorknob far easier than gripping and twisting the thin inner metal spindle directly with your fingers?",
            "لماذا يكون تدوير مقبض الباب المستدير العريض أسهل بكثير من الإمساك بالعمود المعدني الرفيع الداخلي وتدويره مباشرة بأصابعك؟",
            [
                ("The wide knob acts as a wheel-and-axle where a larger outer radius multiplies turning force onto the small axle", "لأن المقبض العريض يعمل كعجلة ومحور حيث يضاعف نصف القطر الكبير قوة التدوير على المحور الصغير"),
                ("The doorknob acts as a spring scale that removes door friction", "لأن المقبض يعمل كميزان نابضي يزيل احتكاك الباب"),
                ("Touching steel directly blocks air pressure around the door", "لأن لمس الفولاذ مباشرة يحجب الضغط الجوي"),
                ("Wide knobs store static electricity that unlocks latches automatically", "لأن المقابض العريضة تخزن كهرباء ساكنة تفتح الباب"),
            ],
            "Compare the large circle traced by the outer wheel rim against the tiny circle of the inner axle shaft!",
            "قارن الدائرة الكبيرة التي تدور بها حافة العجلة الخارجية بالدائرة الصغيرة للمحور الداخلي!",
            "Wheel-and-axle multiplies effort force by the ratio of wheel radius to axle radius.",
            ["Turning the large outer doorknob requires less force applied over a longer circular path.", "The inner shaft rotates with multiplied force to retract the latch."],
            "Steering wheels and screwdrivers apply this exact same wheel-and-axle advantage.",
            "العجلة والمحور رافعة دائرية تضاعف القوة بنسبة نصف قطر العجلة إلى نصف قطر المحور.",
            ["تدور يدك على محيط كبير حول المقبض بقوة صغيرة.", "فينقل المحور الداخلي الرفيع عزماً مضاعفاً يفتح المزلاج بسهولة."],
            "المفك ومقود السيارة يعتمدان على المبدأ نفسه.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b15:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Medium", bp,
        "A mechanic uses a single MOVABLE pulley (supported by 2 vertical rope segments, MA = 2) to lift a 180 N motorcycle wheel smoothly. What ideal upward pulling force in newtons must the mechanic exert on the rope?",
        "يستخدم ميكانيكي بكرة متحركة واحدة (تحملها قطعتا حبل عموديتان، الفائدة الآلية = 2) لرفع عجلة دراجة وزنها 180 نيوتن. ما مقدار قوة السحب المثالية للأعلى التي يجب أن يبذلها الميكانيكي بالنيوتن؟",
        90, [45, 180, 360],
        "With 2 supporting strands sharing the 180 N load equally (MA = 2), divide 180 N by 2.",
        "بتوزيع الوزن (180 نيوتن) بالتساوي على فرعي الحبل الحاملين (MA = 2)، اقسم 180 على 2.",
        "Movable pulley effort = Load ÷ number of supporting rope strands.",
        ["Two rope strands share the 180 N load equally.", "Ideal effort = 180 ÷ 2 = 90 N (while pulling twice the rope length)."],
        "2 strands × 90 N = 180 N.",
        "في البكرة المتحركة تتقاسم قطع الحبل الحاملة وزن المقاومة.",
        ["يحمل العجلة فرعا حبل متساويان (MA = 2).", "القوة اللازمة = 180 ÷ 2 = 90 نيوتن."],
        "تحقق: 90 × 2 = 180 نيوتن.",
    )

    # Hard (10..14): Torque seesaw balance math, work/efficiency on rough ramp, ramp comparison table, 4-strand pulley distance, compound scissors
    B.add_math(
        tp, "Hard", bp,
        "A 400 N child sits 1.5 m to the left of a seesaw's central fulcrum. How many meters to the RIGHT of the fulcrum must a 300 N friend sit so the seesaw balances horizontally?",
        "يجلس طفل وزنه 400 نيوتن على بُعد 1.5 م يسار نقطة ارتكاز أرجوحة توازنية. على بُعد كم متراً يمين نقطة الارتكاز يجب أن يجلس صديقه الذي وزنه 300 نيوتن كي تتزن الأرجوحة أفقياً؟",
        2, [1.5, 3, 4],
        "Balance turning torques: Left Weight × Left Distance = Right Weight × Right Distance (400 × 1.5 = 300 × d).",
        "ساوِ العزمين: الوزن الأيسر × بعده = الوزن الأيمن × بعده (400 × 1.5 = 300 × البعد).",
        "Rotational lever equilibrium requires F₁ × d₁ = F₂ × d₂.",
        ["Left product = 400 × 1.5 = 600 N·m.", "Solve 300 × d₂ = 600 → d₂ = 600 ÷ 300 = 2 m."],
        "Heavier child sits closer (1.5 m); lighter friend sits farther (2 m) so 400×1.5 = 300×2 = 600.",
        "يتحقق توازن الرافعة عند تساوي حاصل ضرب القوة في ذراعها على الجانبين.",
        ["العزم الأيسر = 400 × 1.5 = 600.", "للاتزان: 300 × المسافة = 600 ← المسافة = 600 ÷ 300 = 2 م."],
        "الأثقل يجلس أقرب للارتكاز والأخف يجلس أبعد.",
        "",
        svg_lever_diagram(184, "400 N", "300 N", "1.5 m", "? m", "Balanced Seesaw"),
        svg_lever_diagram(184, "400 نيوتن", "300 نيوتن", "1.5 م", "؟ م", "توازن الأرجوحة"),
    )

    hard_b15 = [
        (
            "Lifting a 200 N crate straight up 2 m requires 400 J of useful work. A student instead drags the crate up a rough 8 m ramp using 75 N of pull (75 × 8 = 600 J of input work). Where did the extra 200 J go, and why can NO real machine ever require less than 400 J of input work?",
            "رفع صندوق وزنه 200 نيوتن رأسياً مسافة 2 م يتطلب 400 جول من الشغل المفيد. سحب طالب الصندوق على منحدر خشن طوله 8 م بقوة 75 نيوتن (بذل 75 × 8 = 600 جول). أين ذهبت الـ 200 جول الإضافية، ولماذا لا تستطيع أي آلة حقيقية تقليل الشغل المبذول عن 400 جول؟",
            [
                ("Friction between crate and rough ramp turned 200 J into thermal heat; conservation of energy forbids machines from multiplying work output above input", "تحولت 200 جول إلى حرارة بسبب الاحتكاك على المنحدر، وقانون حفظ الطاقة يمنع أي آلة من إنتاج شغل يفوق الشغل المبذول"),
                ("The 200 J vanished out of the universe because wood absorbs joules", "تلاشت الـ 200 جول من الكون لأن الخشب يمتص الجولات"),
                ("Gravity decreased the crate's mass to 100 N halfway up the ramp", "قلّلت الجاذبية وزن الصندوق إلى 100 نيوتن في منتصف المنحدر"),
                ("Ideal simple machines reduce work below 400 J only when oiled with water", "الآلات المثالية تقلل الشغل عن 400 جول عند تبليلها بالماء"),
            ],
            "Compare Useful Output Work (400 J) with Total Input Work (600 J): 600 − 400 = 200 J!",
            "قارن الشغل المفيد الناتج (400 جول) بالشغل الكلي المبذول (600 جول): 600 − 400 = 200 جول!",
            "Friction wastes part of input work as heat, keeping efficiency below 100%.",
            ["Output useful work = 200 N × 2 m = 400 J.", "Input work = 75 N × 8 m = 600 J. Difference (200 J) went into heat via sliding friction. Efficiency = 400/600 = 67%."],
            "Simple machines lower FORCE by raising distance, never lowering total required work.",
            "لا تصنع الآلات شغلًا إضافياً؛ بل تضيع نسبة من الشغل المبذول كحرارة بالاحتكاك.",
            ["الشغل المفيد لرفع الصندوق = 200 × 2 = 400 جول.", "الشغل المبذول = 75 × 8 = 600 جول؛ والفرق (200 جول) تبدد كحرارة احتكاك."],
            "الآلة البسيطة تسهل العمل بتقليل القوة لا بتقليل الطاقة المطلوبة.",
            svg_ramp_diagram("Rough: 8 m (75 N)", "H: 2 m", "200 N", "Work & Friction on Ramp"),
            svg_ramp_diagram("خشن 8م (75 نيوتن)", "2 م", "200 نيوتن", "الشغل والاحتكاك بالمنحدر"),
        ),
        (
            "Four loading ramps lift identical 240 N barrels onto a 1.5 m-high platform as listed in the table. Neglecting friction, which ramp gives the GREATEST mechanical advantage and needs the smallest pushing force?",
            "ترفع أربعة منحدرات براميل متطابقة وزنها 240 نيوتن إلى منصة ارتفاعها 1.5 م كما في الجدول. بإهمال الاحتكاك، أي منحدر يعطي أكبر فائدة آلية ويتطلب أقل قوة دفع؟",
            [
                ("Ramp D (length 6.0 m, MA = 4, effort = 60 N)", "المنحدر D (طوله 6.0 م، فائدته الآلية 4، القوة 60 نيوتن)"),
                ("Ramp A (length 3.0 m, MA = 2, effort = 120 N)", "المنحدر A (طوله 3.0 م، فائدته الآلية 2، القوة 120 نيوتن)"),
                ("Ramp B (length 4.5 m, MA = 3, effort = 80 N)", "المنحدر B (طوله 4.5 م، فائدته الآلية 3، القوة 80 نيوتن)"),
                ("All four ramps need 240 N because the platform height is 1.5 m for all", "جميع المنحدرات الأربعة تحتاج 240 نيوتن لتساوي الارتفاع"),
            ],
            "For equal height (1.5 m), longer gentler ramp = higher MA = smaller push force!",
            "مع ثبات الارتفاع (1.5 م)، المنحدر الأطول الأقل ميلاً يعطي أكبر فائدة آلية وأقل قوة دفع!",
            "Longer ramp length at fixed height increases MA = L / H.",
            ["Compute MA = L ÷ 1.5: A = 2, B = 3, C = 1.5, D = 4.", "Ramp D yields highest MA (4), cutting push force to 240 ÷ 4 = 60 N."],
            "Gentler ramps require less force over a longer path.",
            "يزداد مقدار الفائدة الآلية كلما زاد طول المنحدر لنفس الارتفاع.",
            ["الفائدة الآلية للمنحدر D = 6.0 ÷ 1.5 = 4 (الأكبر).", "تقل قوة الدفع اللازمة إلى 240 ÷ 4 = 60 نيوتن."],
            "المنحدر الألطف انحداراً يتطلب جهداً أقل.",
            svg_data_table(["Ramp", "Height (m)", "Length (m)"], [["A", "1.5", "3.0"], ["B", "1.5", "4.5"], ["C", "1.5", "2.25"], ["D", "1.5", "6.0"]], "4 Ramp Options", [84, 114, 114]),
            svg_data_table(["المنحدر", "الارتفاع (م)", "الطول (م)"], [["A", "1.5", "3.0"], ["B", "1.5", "4.5"], ["C", "1.5", "2.25"], ["D", "1.5", "6.0"]], "مقارنة أربعة منحدرات", [84, 114, 114]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b15:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "A car engine hoist uses a 4-strand pulley block-and-tackle (MA = 4) so a mechanic pulls with only 1/4 of the engine's weight. To lift the engine 3 meters vertically upward, how many meters of rope must the mechanic pull through the pulleys?",
        "تستخدم رافعة محركات نظام بكرات رباعي الحبال (الفائدة الآلية = 4) بحيث يبذل الميكانيكي ربع وزن المحرك فقط. إذا أراد رفع المحرك مسافة 3 أمتار للأعلى، فكم متراً من الحبل يجب أن يسحب؟",
        12, [0.75, 4, 7],
        "Force divides by 4, so rope pull distance must MULTIPLY by 4 (3 m × 4)!",
        "تقل القوة إلى الربع (÷ 4)، لذا تتضاعف مسافة الحبل المسحوبة (× 4)!",
        "Ideal pulley trade-off: Rope Distance = Load Lift Distance × MA.",
        ["With MA = 4, four rope sections each shorten by 3 m.", "Total rope pulled = 4 × 3 = 12 m."],
        "Check work: (W/4) × 12 = 3W = W × 3.",
        "الفائدة الآلية تعني مضاعفة القوة على حساب سحب مسافة حبل أطول بنفس النسبة.",
        ["تقصر كل قطعة من الحبال الأربعة بمقدار 3 أمتار.", "إجمالي طول الحبل المسحوب = 4 × 3 = 12 متراً."],
        "تحقق: (1/4 القوة) × (4 × المسافة) = نفس الشغل.",
    )

    B.add_concept(
        tp, "Hard", bp,
        "A pair of heavy garden shears is a COMPOUND machine built from two joined parts. Which two simple machines combine inside garden shears to slice thick twigs cleanly?",
        "تُعد مقصات التقليم الثقيلة آلة مركبة تجمع أكثر من آلة بسيطة. أي آلتين بسيطتين تندمجان معاً داخل مقص التقليم لقص الأغصان السميكة بسهولة؟",
        [
            ("Two Class 1 levers (joined at the central screw fulcrum) plus two sharp wedges (the beveled cutting blades)", "رافعتان من النوع الأول (متصلتان عند مسمار الارتكاز الأوسط) مدمجتان مع إسفينين حادين (حافتي القص)"),
            ("A fixed flagpole pulley plus an inclined ramp", "بكرة ثابتة مع مستوى مائل"),
            ("Two Class 3 levers plus a magnetic gear train", "رافعتان من النوع الثالث مع تروس مغناطيسية"),
            ("A single wheel-and-axle with zero blades", "عجلة ومحور واحد دون شفرات"),
        ],
        "Look at the central pivot bolt between handles and blades, and check the tapered V-edge of each blade!",
        "انظر إلى المسمار المحوري بين المقابض والشفرات، وإلى الحافة المشطوفة الحادة لكل شفرة!",
        "Compound machines combine two or more simple machines working in sequence.",
        ["Handles (effort) pivot on the center bolt (fulcrum) to pinch blades (load) → twin Class 1 levers.", "Each blade tapers to a sharp V-edge to wedge apart plant fibers → twin wedges."],
        "Bicycles, wheelbarrows (lever + wheel/axle), and can openers are other compound machines.",
        "الآلة المركبة تتكون من آلتين بسيطتين أو أكثر تعملان معاً.",
        ["يدور المقبضان والشفرتان حول نقطة ارتكاز وسطى (رافعتان من النوع الأول).", "وتنتهي الشفرتان بحافة حادة مائلة تخترق الغصن وتشقه (إسفينان)."],
        "الجمع بينهما يضاعف قوة الضغط ويقطع بسهولة.",
        None, None,
    )


def _add_b16(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B16"
    # Easy (0..4): Roller coaster PE/KE, elastic PE, chemical energy, renewable vs nonrenewable, conservation
    easy_b16 = [
        (
            "A roller coaster car pauses momentarily at the highest peak A (40 m) before plunging down the track. Which type of mechanical energy is at its MAXIMUM at peak A?",
            "تتوقف عربة أفعوانية لحظياً عند أعلى قمة A (بارتفاع 40 م) قبل انحدارها للأسفل. أي نوع من الطاقة الميكانيكية يكون في أعلى قيمة له عند القمة A؟",
            [
                ("Gravitational potential energy", "طاقة الوضع الجاذبية"),
                ("Kinetic energy of rapid motion", "الطاقة الحركية"),
                ("Elastic spring energy", "طاقة الوضع المرونية"),
                ("Chemical battery energy", "الطاقة الكيميائية"),
            ],
            "Height determines gravitational potential energy; speed determines kinetic energy!",
            "الارتفاع يحدد طاقة الوضع الجاذبية، والسرعة تحدد الطاقة الحركية!",
            "Gravitational potential energy increases directly with height above ground.",
            ["Peak A is the highest point (40 m) where the car pauses briefly.", "Therefore gravitational PE is maximum and KE is near zero."],
            "At the lowest valley B (0 m), PE drops and converts into maximum KE!",
            "تبلغ طاقة الوضع الجاذبية أقصاها عند أعلى ارتفاع.",
            ["النقطة A هي أعلى موضع على المسار (40 م) والسرعة عندها شبه صفرية.", "لذا تتخزن معظم الطاقة على شكل طاقة وضع جاذبية."],
            "وعند الهبوط تتحول طاقة الوضع إلى طاقة حركية.",
            svg_roller_coaster([40, 0, 20, 0], "Roller Coaster Energy"),
            svg_roller_coaster([40, 0, 20, 0], "طاقة الأفعوانية"),
        ),
        (
            "When an archer pulls back a bowstring firmly before releasing the arrow, what form of energy is stored inside the bent wooden bow limbs?",
            "عندما يسحب الرامي وتر القوس بقوة للخلف قبل إطلاق السهم، ما شكل الطاقة المخزنة داخل ذراعي القوس المثنيين؟",
            [
                ("Elastic potential energy", "طاقة الوضع المرونية"),
                ("Nuclear fission energy", "طاقة نووية"),
                ("Gravitational potential energy from altitude", "طاقة وضع جاذبية"),
                ("Sound wave energy", "طاقة صوتية"),
            ],
            "Stretched rubber bands, compressed springs, and bent bows all store energy due to deformation.",
            "الأشرطة المطاطية المشدودة والنوابض المضغوطة والأقواس المثنية تخزن طاقة بسبب تغير شكلها.",
            "Elastic potential energy is stored when objects are stretched or compressed.",
            ["Pulling the bow bends elastic wood/fiberglass limbs.", "Releasing transforms that elastic PE rapidly into arrow kinetic energy."],
            "Slingshots and pogo-stick springs store elastic PE the same way.",
            "تُخزن طاقة الوضع المرونية في الأجسام المرنة عند شدها أو ثنيها أو ضغطها.",
            ["يخزن القوس المثني طاقة مرونية تتحرر عند ترك الوتر.", "فتتحول بسرعة إلى طاقة حركية تدفع السهم للأمام."],
            "نفس الطاقة توجد في النابض المضغوط والمطاط المشدود.",
            None, None,
        ),
        (
            "Which object primarily stores CHEMICAL energy ready to be transformed when used?",
            "أي مما يلي يختزن طاقةً كيميائيةً جاهزة للتحول عند استخدامها؟",
            [
                ("An AA dry-cell battery and a plate of rice and dates", "بطارية جافة ووجبة من التمر والأرز"),
                ("A spinning wind turbine rotor at the top of a hill", "مروحة توربين رياح دوّارة فوق تل"),
                ("A rock perched on a cliff ledge", "صخرة مستقرة على حافة جرف مرتفع"),
                ("Sunlight rays beaming onto a solar rooftop", "أشعة شمس ساطعة على سقف منزل"),
            ],
            "Chemical energy is stored inside molecular bonds of food, batteries, and fuels.",
            "تُخزن الطاقة الكيميائية في الروابط الجزيئية داخل الغذاء والبطاريات والوقود.",
            "Food, fuels, and batteries store chemical potential energy.",
            ["Eating food and discharging a battery break chemical bonds to release usable energy.", "Spinning turbines hold kinetic energy; perched rocks hold gravitational PE; sunlight is radiant energy."],
            "Even gasoline and wood store chemical energy from ancient photosynthesis!",
            "تُعد الأغذية والوقود والبطاريات مخازن للطاقة الكيميائية.",
            ["تختزن البطارية والطعام الطاقة في روابطهما الكيميائية.", "أما التوربين الدوار فحركية، والصخرة المرتفعة فوضع جاذبية، وضوء الشمس فإشعاعية."],
            "تتحول الطاقة الكيميائية في الجسم إلى حرارة وحركة.",
            None, None,
        ),
        (
            "Saudi Arabia's Sakaka solar plant and Dumat Al-Jandal wind farm generate electricity using which category of energy resources?",
            "تولّد محطة سكاكا للطاقة الشمسية ومزرعة دومة الجندل لطاقة الرياح في المملكة الكهرباء باستخدام أي فئة من مصادر الطاقة؟",
            [
                ("Renewable energy resources that replenish naturally without running out", "مصادر طاقة متجددة تتجدد طبيعياً ولا تنضب"),
                ("Nonrenewable fossil fuels formed over millions of years", "وقود أحفوري غير متجدد تكوّن عبر ملايين السنين"),
                ("Nuclear uranium fuel rods", "وقود اليورانيوم النووي"),
                ("Underground coal seams", "طبقات الفحم الحجري الجوفية"),
            ],
            "Sunlight and wind refill day after day naturally, unlike finite coal, oil, and natural gas.",
            "أشعة الشمس والرياح تتجدد يومياً بشكل طبيعي بعكس النفط والفحم والغاز الطبيعي القابلة للنفاد.",
            "Solar, wind, hydro, and geothermal are renewable; fossil fuels are nonrenewable.",
            ["Solar panels and wind turbines harvest continuous natural sunlight and atmospheric wind.", "Coal, petroleum, and natural gas take millions of years to form and are nonrenewable."],
            "Renewable sources also produce zero greenhouse gas emissions during operation.",
            "الشمس والرياح والمياه الجارية مصادر طاقة متجددة.",
            ["تتجدد الطاقة الشمسية والرياح باستمرار في الطبيعة دون أن تنفد.", "بينما يُعد النفط والفحم والغاز مصادر غير متجددة."],
            "تتميز المتجددة بنظافتها واستدامتها البيئية.",
            None, None,
        ),
        (
            "What does the Law of Conservation of Energy state whenever energy changes from one form to another in a closed system?",
            "ماذا ينص قانون حفظ الطاقة كلما تحولت الطاقة من شكل إلى آخر داخل نظام مغلق؟",
            [
                ("Energy cannot be created or destroyed; it only transforms from one form to another with constant total energy", "الطاقة لا تفنى ولا تُستحدث من العدم، وإنما تتحول من شكل إلى آخر مع بقاء مجموعها ثابتاً"),
                ("Half of the energy vanishes permanently whenever machines heat up", "يفنى نصف الطاقة نهائياً كلما سخنت الآلات"),
                ("Batteries create brand-new energy from nothing when switches close", "تنشئ البطاريات طاقة جديدة من العدم عند إغلاق الدائرة"),
                ("Potential energy can never turn into kinetic energy", "لا يمكن لطاقة الوضع أن تتحول إلى طاقة حركية أبداً"),
            ],
            "Just like mass in a closed jar, total energy is strictly accounted for across every conversion!",
            "كما تُحفظ الكتلة في الإناء المغلق، يظل مجموع الطاقة الكلي ثابتاً في جميع التحولات!",
            "Total energy in an isolated system remains strictly conserved.",
            ["When energy 'appears lost' (like friction heat), it actually transformed into thermal/sound energy.", "Adding useful output + heat/sound output always equals initial energy input."],
            "Conservation of energy is one of physics' most fundamental laws.",
            "قانون حفظ الطاقة يؤكد ثبات الكمية الكلية للطاقة في الكون.",
            ["الطاقة تتحول فقط بين صور مختلفة كالكهربائية والضوئية والحرارية والحركية.", "وما يُسمى 'فقدان الطاقة' يعني تحولها إلى صورة غير مرغوبة كالحرارة الضائعة لا فناؤها."],
            "مجموع الطاقات الناتجة يساوي دائماً الطاقة الداخلة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b16:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Transformation chains (flashlight, dam), solar/photosynthesis, truck vs car KE table, roller coaster PE->KE
    med_b16 = [
        (
            "Which sequence accurately traces the main energy transformations inside a handheld battery-powered LED flashlight once you slide the switch ON?",
            "أي تسلسل يتتبع بدقة تحولات الطاقة الرئيسة داخل مصباح يدوي يعمل بالبطارية عند تشغيله؟",
            [
                ("Chemical energy (battery) → Electrical energy (wires) → Light + Thermal energy (LED)", "طاقة كيميائية (البطارية) ← طاقة كهربائية (الأسلاك) ← طاقة ضوئية وحرارية (المصباح)"),
                ("Electrical energy → Nuclear energy → Chemical energy", "طاقة كهربائية ← طاقة نووية ← طاقة كيميائية"),
                ("Gravitational potential → Elastic energy → Sound energy", "طاقة وضع جاذبية ← طاقة مرونية ← طاقة صوتية"),
                ("Light energy → Chemical energy → Mechanical energy", "طاقة ضوئية ← طاقة كيميائية ← طاقة ميكانيكية"),
            ],
            "Start with what sits stored inside the battery, trace what travels through the copper circuit, and end with what exits the bulb!",
            "ابدأ بما هو مخزن في البطارية، ثم ما يسري في الأسلاك، وانتهِ بما يخرج من المصباح!",
            "Flashlights transform chemical → electrical → light and thermal energy.",
            ["A battery stores chemical energy.", "Closing the switch sends electric current to the LED, emitting visible light plus a bit of warmth."],
            "Notice thermal energy always accompanies real conversions!",
            "تتحول الطاقة في المصباح عبر ثلاث مراحل متتابعة.",
            ["تبدأ الطاقة كيميائية مخزنة داخل البطارية.", "تسري كهربائياً في الدائرة فتضيء المصباح مع تولد قدر يسير من الحرارة."],
            "دائماً ما يصاحب التحولات قدر من الطاقة الحرارية.",
            svg_process_flow(["Chemical", "Electrical", "Light + Heat"], "Flashlight Chain", "Energy Transformations"),
            svg_process_flow(["كيميائية", "كهربائية", "ضوء + حرارة"], "سلسلة تحول المصباح", "تحولات الطاقة"),
        ),
        (
            "How does a hydroelectric dam generate household electricity from river water stored high behind the dam wall?",
            "كيف يولّد السد الكهرومائي الكهرباء للمنازل من مياه النهر المحتجزة على ارتفاع عالٍ خلف جدار السد؟",
            [
                ("Gravitational potential energy (high water) → Kinetic energy (falling flow) → Mechanical turbine rotation → Electrical energy (generator)", "طاقة وضع جاذبية (الماء المرتفع) ← طاقة حركية (اندفاع الماء) ← طاقة ميكانيكية (التوربين) ← طاقة كهربائية (المولد)"),
                ("Chemical energy (water) → Light energy → Gravitational energy", "طاقة كيميائية ← ضوئية ← جاذبية"),
                ("Thermal magma heat → Nuclear energy → Chemical energy", "حرارية ← نووية ← كيميائية"),
                ("Sound energy → Elastic energy → Potential energy", "صوتية ← مرونية ← وضع"),
            ],
            "Water sits high in the reservoir, drops fast through tunnels, spins blades, and turns a wire-and-magnet generator.",
            "يخزن الماء عالياً في البحيرة، ثم يندفع ساقطاً ليدير شفرات التوربين والمولد الكهربائي.",
            "Hydroelectric dams convert gravitational PE of elevated water into electrical energy.",
            ["Elevated reservoir water holds large gravitational PE.", "Falling water accelerates (KE), spins turbine blades (mechanical), and rotates coils past magnets inside the generator (electrical)."],
            "No fuel combustion occurs at a hydroelectric dam.",
            "تُستغل طاقة وضع المياه الساقطة لتدوير التوربينات وتوليد الكهرباء.",
            ["يمتلك الماء خلف السد طاقة وضع جاذبية كبيرة بسبب ارتفاعه.", "عند تدفقه للأسفل تتحول لحركية تدير التوربين ثم إلى طاقة كهربائية عبر المولد."],
            "يعد هذا من مصادر الطاقة المتجددة النظيفة.",
            svg_process_flow(["High Water PE", "Falling KE", "Spin Turbine", "Electricity"], "Hydroelectric Dam", "Water to Electricity"),
            svg_process_flow(["وضع (ماء عالٍ)", "حركة السقوط", "دوران التوربين", "كهرباء"], "محطة كهرومائية", "من الماء إلى الكهرباء"),
        ),
        (
            "Look at the highway vehicle data table. Both the sedan and the delivery truck cruise at 20 m/s, yet the truck has twice the kinetic energy. Why?",
            "انظر لجدول المركبات على الطريق. تسير السيارة الصغيرة وشاحنة التوصيل بالسرعة نفسها (20 م/ث)، ومع ذلك تمتلك الشاحنة ضعف الطاقة الحركية. ما السبب؟",
            [
                ("Kinetic energy increases directly with mass, and the truck has double the car's mass (2,400 kg vs. 1,200 kg)", "لأن الطاقة الحركية تتناسب طردياً مع الكتلة، وكتلة الشاحنة ضعف كتلة السيارة (2400 كجم مقابل 1200 كجم)"),
                ("Truck tires are taller so gravity stops affecting them", "لأن إطارات الشاحنة أكبر فلا تؤثر عليها الجاذبية"),
                ("The truck moves at twice the speed even though both read 20 m/s", "لأن الشاحنة تتحرك بضعف السرعة رغم قراءة 20 م/ث"),
                ("Kinetic energy depends solely on vehicle paint color", "لأن الطاقة الحركية تعتمد على لون المركبة فقط"),
            ],
            "Kinetic energy depends on TWO factors: mass and speed! Here speed is identical, so check mass!",
            "تعتمد الطاقة الحركية على عاملين: الكتلة والسرعة! السرعة هنا متساوية، فانظر إلى الكتلة!",
            "At equal speeds, kinetic energy is directly proportional to mass.",
            ["Car mass = 1,200 kg; Truck mass = 2,400 kg (2× heavier).", "At identical 20 m/s speed, doubling mass doubles kinetic energy (and requires twice the braking distance!)."],
            "That is why loaded trucks require far longer braking room than small cars.",
            "عند تساوي السرعة، تتضاعف الطاقة الحركية بتضاعف الكتلة.",
            ["تبلغ كتلة الشاحنة (2400 كجم) ضعفي كتلة السيارة (1200 كجم).", "إذن طاقتها الحركية ضعف طاقة السيارة تماماً عند السرعة نفسها."],
            "لهذا تحتاج الشاحنات المحملة إلى مسافة كبح أطول.",
            svg_data_table(["Vehicle", "Mass (kg)", "Speed (m/s)"], [["Sedan", "1,200", "20"], ["Truck", "2,400", "20"]], "Highway KE Comparison", [104, 112, 112]),
            svg_data_table(["المركبة", "الكتلة (كجم)", "السرعة (م/ث)"], [["سيارة صغيرة", "1200", "20"], ["شاحنة", "2400", "20"]], "مقارنة الطاقة الحركية", [104, 112, 112]),
        ),
        (
            "In the roller coaster diagram (assuming negligible friction), at which point is the coaster car moving at its GREATEST speed?",
            "في مخطط الأفعوانية المرفق (بإهمال الاحتكاك)، عند أي نقطة تتحرك العربة بأقصى سرعة ممكنة؟",
            [
                ("At valley B (and valley D, height 0 m), where all gravitational PE has converted into kinetic energy", "عند الوادي B (والوادي D بارتفاع 0 م)، حيث تحولت كامل طاقة الوضع إلى طاقة حركية"),
                ("At peak A (height 40 m), right before descending", "عند القمة A (40 م) قبل بدء الهبوط"),
                ("At mid-hill C (height 20 m)", "عند التل المتوسط C (20 م)"),
                ("Speed stays identical at A, B, C, and D", "تبقى السرعة متطابقة تماماً عند جميع النقاط"),
            ],
            "Lowest elevation = minimum PE = maximum KE = highest speed!",
            "أدنى ارتفاع = أقل طاقة وضع = أعلى طاقة حركية = أقصى سرعة!",
            "Maximum speed on a frictionless track occurs at the lowest elevation.",
            ["Total mechanical energy PE + KE remains constant.", "At height 0 m (valleys B and D), PE = 0 and KE is maximum, giving top speed."],
            "Climbing back to hill C (20 m) slows the car back down as KE converts back into PE.",
            "أعلى سرعة على المسار تكون عند أخفض نقطة لتمام تحول طاقة الوضع إلى حركة.",
            ["مجموع طاقتي الوضع والحركة ثابت.", "عند القاع (0 م) تبلغ الطاقة الحركية قمتها وتصل العربة لأعلى سرعة."],
            "وعند الصعود نحو C تتباطأ العربة مجدداً.",
            svg_roller_coaster([40, 0, 20, 0], "Track Speed Points"),
            svg_roller_coaster([40, 0, 20, 0], "نقاط سرعة المسار"),
        ),
        (
            "How does a rooftop solar photovoltaic panel differ from a green plant leaf in what it produces from sunlight?",
            "بماذا يختلف اللوح الشمسي الكهروضوئي فوق سطح المنزل عن ورقة النبات الخضراء فيما ينتجه كلٌّ منهما من ضوء الشمس؟",
            [
                ("A solar panel converts sunlight directly into electrical energy, whereas a leaf converts sunlight into stored chemical energy (glucose)", "يحوّل اللوح الشمسي الضوء مباشرة إلى طاقة كهربائية، بينما تحوّله الورقة إلى طاقة كيميائية مخزنة (جلوكوز)"),
                ("Both convert sunlight directly into liquid gasoline inside tubes", "كلاهما يحوّل الضوء إلى وقود سائل"),
                ("A leaf produces electrical current while a solar panel makes sugar", "تنتج الورقة تياراً كهربائياً ويصنع اللوح الشمسي سكراً"),
                ("Neither uses sunlight; both rely on geothermal underground steam", "لا يستخدم أي منهما الشمس بل البخار الجوفي"),
            ],
            "Compare the final energy form generated by photovoltaic silicon cells vs. green chloroplasts.",
            "قارن بين الصورة النهائية للطاقة التي ينتجها اللوح السيليكوني وتلك التي تنتجها البلاستيدة الخضراء.",
            "Solar panels output electrical energy; chloroplasts output chemical sugar energy.",
            ["Silicon photovoltaic cells knock electrons into motion → direct electric current.", "Chloroplasts capture light to bond CO₂ and water → chemical bonds in glucose."],
            "Both harvest renewable solar energy without fossil fuels.",
            "كلاهما يستثمر ضوء الشمس لكن بمخرج مختلف تماماً.",
            ["يولّد اللوح الشمسي تياراً كهربائياً فورياً دون وقود.", "وتحوّل الورقة الطاقة الضوئية إلى طاقة كيميائية داخل سكر الجلوكوز."],
            "يستمد الغلاف الحيوي والتقنية الحديثة طاقتهما أساساً من الشمس.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b16:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Frictionless roller coaster math, doubling speed = 4x KE, bouncing ball dissipation, efficiency %, power plant vs wind
    B.add_math(
        tp, "Hard", bp,
        "Starting from rest at Peak A (40 m high) on the frictionless roller coaster, a cart possesses 800 J of gravitational potential energy and 0 J of kinetic energy. When the cart reaches the top of Hill C (20 m high, half the height of A), how many joules of KINETIC energy does it have?",
        "بدأت عربة من السكون عند القمة A (ارتفاع 40 م) على مسار أملس عديم الاحتكاك بطاقة وضع قدرها 800 جول وطاقة حركية 0 جول. عندما تصل العربة إلى قمة التل C (ارتفاع 20 م، أي نصف الارتفاع)، كم جولاً تبلغ طاقتها الحركية؟",
        400, [200, 600, 800],
        "Total energy is 800 J everywhere. At half the height (20 m), PE is half (400 J) — so the remaining energy must be KE!",
        "الطاقة الكلية ثابتة عند 800 جول. عند نصف الارتفاع (20 م) تصبح طاقة الوضع نصفها (400 جول)، إذن الباقي هو الطاقة الحركية!",
        "Total mechanical energy E = PE + KE stays constant without friction.",
        ["At Peak A (40 m): E_total = 800 + 0 = 800 J.", "At Hill C (20 m = half of 40 m): PE = 400 J. Therefore KE = 800 - 400 = 400 J."],
        "400 J PE + 400 J KE = 800 J conserved total.",
        "بإهمال الاحتكاك، مجموع طاقتي الوضع والحركة يساوي 800 جول في كل نقطة.",
        ["عند الارتفاع 20 م (نصف 40 م) تنخفض طاقة الوضع إلى نصف قيمتها أي 400 جول.", "الطاقة الحركية عند C = 800 − 400 = 400 جول."],
        "تحقق: 400 + 400 = 800 جول.",
        "",
        svg_roller_coaster([40, 0, 20, 0], "Mechanical Energy Split"),
        svg_roller_coaster([40, 0, 20, 0], "توزيع الطاقة الميكانيكية"),
    )

    hard_b16 = [
        (
            "A cyclist pedals along a flat track at 5 m/s with 300 J of kinetic energy. She sprints and DOUBLES her speed to 10 m/s (with her total mass unchanged). What happens to her kinetic energy?",
            "يتحرك راكب دراجة على مضمار مستوٍ بسرعة 5 م/ث وطاقة حركية قدرها 300 جول. إذا ضاعف سرعته لتصبح 10 م/ث (مع ثبات كتلته)، فماذا يحدث لطاقته الحركية؟",
            [
                ("It quadruples (4× larger) to 1,200 J because kinetic energy scales with the SQUARE of speed", "تتضاعف أربع مرات (4×) لتصل إلى 1200 جول لأن الطاقة الحركية تتناسب مع مربع السرعة"),
                ("It doubles (2× larger) to 600 J because speed doubled", "تتضاعف مرتين فقط إلى 600 جول"),
                ("It stays 300 J because total bicycle mass stayed identical", "تبقى 300 جول لثبات الكتلة"),
                ("It drops in half to 150 J as wind pushes backward", "تقل إلى النصف (150 جول)"),
            ],
            "Watch out! KE depends on speed SQUARED (v²): doubling speed multiplies KE by 2² = 4!",
            "انتبه! الطاقة الحركية تعتمد على مربع السرعة (v²): مضاعفة السرعة تضرب الطاقة الحركية في 2² = 4!",
            "Kinetic energy scales linearly with mass (m) and quadratically with speed (v²).",
            ["Doubling speed (2v) multiplies v² by 2² = 4.", "Thus KE rises from 300 J to 300 × 4 = 1,200 J (which is why doubling car speed needs 4× stopping distance!)."],
            "That speed-squared factor explains why highway speeding is so dangerous.",
            "تتناسب الطاقة الحركية طردياً مع مربع السرعة، فتأثير السرعة مضاعف.",
            ["عند مضاعفة السرعة مرتين (من 5 إلى 10 م/ث)، يزداد مربع السرعة 2 × 2 = 4 أضعاف.", "إذن الطاقة الحركية الجديدة = 300 × 4 = 1200 جول."],
            "ولهذا تضاعف السرعة الزائدة مسافة الفرملة أربع مرات.",
            svg_bar_chart([("5 m/s", 300, BLUE), ("10 m/s", 1200, RED)], "KE (J)", "Speed Doubling vs KE"),
            svg_bar_chart([("5 م/ث", 300, BLUE), ("10 م/ث", 1200, RED)], "الطاقة (جول)", "تأثير مضاعفة السرعة"),
        ),
        (
            "A student drops a rubber ball from a height of 2.0 m onto a tile floor, and it bounces back up to only 1.4 m on the first bounce. Why does it NOT reach 2.0 m again?",
            "أسقطت طالبة كرة مطاطية من ارتفاع 2.0 م على بلاط الأرضية، فارتدت في القفزة الأولى إلى ارتفاع 1.4 م فقط. لماذا لم تعد الكرة إلى ارتفاع 2.0 م؟",
            [
                ("Part of the mechanical energy converted into thermal heat and sound waves during the bounce and air drag, while total energy remained conserved", "لأن جزءاً من الطاقة الميكانيكية تحول إلى حرارة وصوت أثناء الارتطام ومقاومة الهواء مع بقاء الطاقة الكلية محفوظة"),
                ("Half of the rubber atoms disappeared inside the floor tiles", "لأن نصف ذرات المطاط فُقدت داخل بلاط الأرضية"),
                ("Energy conservation stops working whenever objects bounce upward", "لأن قانون حفظ الطاقة يتوقف عند ارتداد الكرات للأعلى"),
                ("Gravity doubled on the bounce back up", "لأن الجاذبية تضاعفت أثناء الارتداد للأعلى"),
            ],
            "Check what happens when you touch a squash ball after several rallies — it feels warm and makes a 'thump' sound!",
            "تلمّس كرة الاسكواش بعد عدة ضربات: ستجدها دافئة وقد أصدرت صوت ارتطام!",
            "Real bounces dissipate some mechanical energy as thermal energy and sound.",
            ["At 2.0 m drop, the ball starts with 100% gravitational PE.", "Hitting the floor compresses rubber and air, turning ~30% into heat and sound, leaving ~70% to climb to 1.4 m."],
            "Total universe energy (1.4 m PE + heat + sound) still equals original 2.0 m PE!",
            "قانون حفظ الطاقة متحقق؛ التحول إلى حرارة وصوت يفسر نقص الارتفاع.",
            ["تفقد الكرة جزءاً من طاقتها الميكانيكية عند اصطدامها بالأرض على هيئة طاقة حرارية وصوت.", "لذا لا تكفي الطاقة الميكانيكية المتبقية للوصول إلا لارتفاع 1.4 م."],
            "مجموع (الطاقة المتبقية + الحرارة + الصوت) يساوي الطاقة الابتدائية.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b16:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "A modern LED desk lamp draws 20 J of electrical energy each second and outputs 18 J of bright visible light plus 2 J of warmth. What is the percentage energy efficiency of this LED lamp?",
        "يستهلك مصباح مكتب حديث من نوع LED طاقة كهربائية مقدارها 20 جولاً كل ثانية، وينتج 18 جولاً من الضوء الساطع و2 جول من الحرارة. ما نسبة الكفاءة الطاقية لهذا المصباح (%)؟",
        90, [10, 20, 80],
        "Efficiency % = (Useful Light Output ÷ Total Electrical Input) × 100%.",
        "الكفاءة (%) = (الطاقة الضوئية المفيدة ÷ الطاقة الكهربائية الكلية الداخلة) × 100%.",
        "Energy efficiency equals useful output divided by total energy input.",
        ["Useful light = 18 J; total input = 20 J.", "Efficiency = (18 ÷ 20) × 100% = 0.90 × 100% = 90%."],
        "Remaining 2/20 = 10% became wasted heat.",
        "تقيس الكفاءة نسبة الطاقة المحولة للشكل المرغوب مقارنة بإجمالي الطاقة المستهلكة.",
        ["الضوء المفيد = 18 جول، والطاقة الكلية = 20 جول.", "الكفاءة = (18 ÷ 20) × 100% = 90%."],
        "والـ 10% الباقية (2 جول) تحولت إلى حرارة.",
        suffix="\\%",
        diagram_en=svg_bar_chart([("Input", 20, BLUE), ("Light", 18, GREEN), ("Heat", 2, ORANGE)], "Energy (J/s)", "LED Energy Efficiency"),
        diagram_ar=svg_bar_chart([("داخلة", 20, BLUE), ("ضوء مفيد", 18, GREEN), ("حرارة", 2, ORANGE)], "الطاقة (جول/ث)", "كفاءة مصباح LED"),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Compare a coal-fired steam power plant with a coastal wind turbine. Both spin a copper-coil generator to send electricity onto the grid, yet the coal plant involves extra intermediate steps. Which extra energy step occurs in the coal plant but NOT in the wind turbine?",
        "قارن بين محطة كهرباء بخارية تعمل بالفحم وتوربين رياح ساحلي: كلاهما يدير مولداً كهربائياً لإمداد الشبكة، لكن محطة الفحم تمر بخطوة وسيطة إضافية. ما الخطوة الطاقية الإضافية الموجودة في محطة الفحم وغير الموجودة في توربين الرياح؟",
            [
                ("Chemical energy burns into intense thermal energy (heat) to boil high-pressure steam before spinning the turbine", "تحترق الطاقة الكيميائية لتوليد طاقة حرارية هائلة تغلي الماء إلى بخار مضغوط قبل تدوير التوربين"),
                ("Wind turbines burn nitrogen gas into thermal steam before spinning blades", "يحرق توربين الرياح غاز النيتروجين لصنع بخار"),
                ("Coal plants use solar radiation directly inside silicon solar panels", "تستخدم محطة الفحم الإشعاع الشمسي مباشرة في ألواح سيليكون"),
                ("Wind turbines convert gravitational energy directly into chemical coal", "يحول توربين الرياح الجاذبية مباشرة إلى فحم كيميائي"),
            ],
            "Wind already carries kinetic energy straight onto the rotor blades! Coal starts as chemical fuel needing fire + steam.",
            "تحمل الرياح طاقة حركية جاهزة تدير الشفرات مباشرة! أما الفحم فيحتاج حرقاً وحرارة وغليان بخار أولاً.",
            "Thermal fossil plants add chemical → thermal combustion stages before turbine rotation.",
            ["Wind farm: Kinetic air → Mechanical blades → Electrical.", "Coal plant: Chemical fuel → Thermal heat → Kinetic steam → Mechanical turbine → Electrical."],
            "Skipping combustion avoids CO₂ emissions and heat losses.",
            "تتجاوز طاقة الرياح مرحلتي الاحتراق الكيميائي والتسخين الحراري.",
            ["توربين الرياح يحول طاقة حركة الهواء مباشرة لدوران التوربين ثم الكهرباء.", "محطة الفحم تحول الطاقة الكيميائية إلى حرارة تغلي الماء لبخار ثم تدير التوربين."],
            "تقليل مراحل التحول يحد من التلوث والفواقد الحرارية.",
            None, None,
    )


def _add_b17(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B17"
    # Easy (0..4): Conduction, convection, radiation, reflection angle, sound pitch vs volume
    easy_b17 = [
        (
            "A steel spoon left sitting inside a mug of steaming hot tea soon feels hot all the way up to its handle. By which heat transfer method did thermal energy travel through the solid metal spoon?",
            "ملعقة فولاذية تُركت داخل كوب شاي ساخن فسرعان ما أصبح مقبضها ساخناً. بأي طريقة من طرق انتقال الحرارة وصلت الطاقة الحرارية عبر الملعقة المعدنية الصلبة؟",
            [("Conduction (particle-to-particle collisions through solid metal)", "التوصيل الحراري (انتقال الاهتزاز من جسيم لآخر عبر المعدن الصلب)"), ("Convection (rising fluid currents)", "الحمل الحراري (تيارات السوائل الصاعدة)"), ("Radiation (electromagnetic waves through vacuum)", "الإشعاع الحراري (موجات عبر الفراغ)"), ("Refraction (bending light rays)", "انكسار الضوء")],
            "Particles in solid metal stay in place and pass rapid vibrations along directly from neighbor to neighbor!",
            "تبقى ذرات المعدن في مواضعها وتنقل الاهتزاز الحراري بالتلامس المباشر من ذرة لأخرى!",
            "Conduction transfers heat via direct particle collisions in solids.",
            ["Hot tea speeds up vibrations at the submerged spoon tip.", "Those vibrations and free electrons pass thermal energy atom-by-atom up to the handle."],
            "Wooden or plastic spoons conduct much more slowly (insulators).",
            "التوصيل هو انتقال الحرارة عبر المواد الصلبة دون انتقال الجسيمات نفسها.",
            ["تكتسب ذرات طرف الملعقة المغمور طاقة اهتزازية وتنقلها عبر التصادمات المتتالية إلى المقبض.", "الفلزات ممتازة في التوصيل الحراري."],
            "الملاعق الخشبية لا تسخن بالسرعة نفسها لأنها عوازل.",
            None, None,
        ),
        (
            "When a pot of water heats on a stove burner, warm water at the bottom expands, becomes less dense, rises to the top, cools, and sinks back down in a continuous loop. What is this heat transfer method called?",
            "عند تسخين قدر ماء على الموقد، يتمدد الماء الدافئ في القاع فتقل كثافته ويصعد للأعلى، ثم يبرد ويهبط في حلقة مستمرة. ما اسم طريقة انتقال الحرارة هذه؟",
            [("Convection", "الحمل الحراري"), ("Conduction", "التوصيل الحراري"), ("Radiation", "الإشعاع الحراري"), ("Reflection", "الانعكاس")],
            "Fluids (liquids and gases) transfer heat by bulk rising and sinking circulation loops!",
            "تنقل الموائع (السوائل والغازات) الحرارة عبر صعود الأدفأ الأقل كثافة وهبوط الأبرد!",
            "Convection transfers heat through moving currents in liquids and gases.",
            ["Warm fluid expands → lower density → rises upward.", "Cooler denser fluid sinks to take its place, circulating thermal energy throughout the pot."],
            "Sea breezes and home heater airflow also rely on convection currents.",
            "الحمل الحراري ينقل الحرارة عبر تيارات صاعدة وهابطة في السوائل والغازات.",
            ["يسخن الماء بالأسفل فتقل كثافته ويرتفع للأعلى، ويحل محله ماء أبرد من الأعلى.", "تستمر هذه الدورة لتسخين كامل الماء في القدر."],
            "النسيم البحري وتيارات الطقس أمثلة طبيعية على الحمل الحراري.",
            None, None,
        ),
        (
            "Earth sits 150 million kilometers from the Sun separated by the nearly empty vacuum of outer space. How does solar thermal energy reach Earth across that vacuum?",
            "تبعد الأرض نحو 150 مليون كيلومتر عن الشمس ويفصل بينهما فضاء فراغ شبه تام. كيف تصل الطاقة الحرارية الشمسية إلى الأرض عبر هذا الفراغ؟",
            [
                ("By thermal radiation (electromagnetic waves requiring no matter medium)", "بالإشعاع الحراري (موجات كهرومغناطيسية لا تحتاج لوسط مادي)"),
                ("By solid conduction through invisible copper wires in space", "بالتوصيل عبر أسلاك فضائية غير مرئية"),
                ("By air convection currents flowing directly from Sun to Earth", "بتيارات الحمل الهوائية من الشمس للأرض"),
                ("By sound waves carrying heat across space", "بموجات صوتية تنقل الحرارة عبر الفراغ"),
            ],
            "Conduction and convection BOTH require matter particles! Only one method crosses empty vacuum.",
            "التوصيل والحمل كلاهما يحتاج لجسيمات مادية! طريقة واحدة فقط تعبر الفراغ التام.",
            "Radiation transfers energy as electromagnetic waves through empty space.",
            ["Outer space lacks solids, liquids, or dense gases needed for conduction or convection.", "Sunlight (infrared + visible waves) radiates across the vacuum at 300,000 km/s."],
            "Campfire warmth felt across cool air from the side also travels mostly by radiation!",
            "ينتقل الإشعاع الحراري عبر الفراغ دون الحاجة إلى جسيمات مادة.",
            ["لا يوجد هواء أو صلب بين الشمس والأرض لنقل الحرارة بالتوصيل أو الحمل.", "تصل حرارة الشمس وضوؤها إلينا على هيئة موجات إشعاع كهرومغناطيسي."],
            "الدفاية الكهربائية تشع الدفء نحو يديك بالإشعاع أيضاً.",
            None, None,
        ),
        (
            "A narrow laser ray strikes a flat mirror at an angle of 35° from the vertical dashed normal line as shown. At what angle (measured from the normal) will the reflected ray bounce away?",
            "يسقط شعاع ضوئي ضيق على مرآة مستوية بزاوية 35° مع العمود المقام المتقطع كما في الشكل. ما مقدار زاوية الانعكاس المقاسة مع العمود المقام؟",
            [("35°", "35°"), ("55°", "55°"), ("70°", "70°"), ("90°", "90°")],
            "Recall the Law of Reflection: Angle of Incidence = Angle of Reflection!",
            "تذكّر قانون الانعكاس: زاوية السقوط = زاوية الانعكاس!",
            "Specular reflection keeps incidence and reflection angles strictly equal.",
            ["Both angles are measured from the perpendicular normal line.", "Angle of reflection = Angle of incidence = 35°."],
            "If the ray hit straight down along the normal (0°), it would bounce straight back at 0°.",
            "ينص قانون الانعكاس على تساوي زاوية السقوط وزاوية الانعكاس.",
            ["زاوية السقوط المحددة مع العمود المقام هي 35°.", "لذلك تساويها زاوية الانعكاس تماماً فتبلغ 35°."],
            "الانعكاس المنتظم على المرآة يحافظ على تساوي الزاويتين.",
            svg_light_ray("reflect", 35, "Normal", "Flat Mirror", "Law of Reflection"),
            svg_light_ray("reflect", 35, "العمود المقام", "مرآة مستوية", "قانون الانعكاس"),
        ),
        (
            "A violinist plucks a string gently and then plucks the EXACT same string much harder (making larger side-to-side vibrations without changing how many times it vibrates per second). How does the sound change?",
            "نقر عازف على وتر كمان برفق، ثم نقر الوتر نفسه بقوة أكبر (مُحدثاً اهتزازاً أوسع دون تغيير عدد الاهتزازات في الثانية). كيف يتغير الصوت؟",
            [
                ("The sound becomes LOUDER (larger amplitude), while its pitch (frequency) stays the same", "يزداد علوّ الصوت (تزداد السعة)، بينما تبقى درجة حدّته (التردد) كما هي"),
                ("The sound becomes higher-pitched (higher frequency) and softer", "تزداد حدّة الصوت ويصبح أخفت"),
                ("Both loudness and pitch drop to zero", "ينعدم الصوت وتختفي الحدة"),
                ("The sound turns into light rays inside the violin", "يتحول الصوت إلى أشعة ضوء"),
            ],
            "Amplitude controls loudness (volume); Frequency controls pitch (high vs. low note)!",
            "السعة تتحكم في شدة الصوت (العلوّ)، والتردد يتحكم في درجة الصوت (الحِدة والغلظة)!",
            "Wave amplitude governs volume; frequency governs pitch.",
            ["Plucking harder supplies more energy → wider amplitude → louder sound.", "Same string length/tension keeps vibration frequency identical → unchanged pitch."],
            "Tightening or shortening a string raises frequency → higher pitch.",
            "زيادة سعة الاهتزاز ترفع شدة الصوت دون تغيير تردده أو درجته.",
            ["النقر الأقوى يوسع مسافة اهتزاز الوتر (زيادة السعة) فيعلو الصوت.", "بقاء طول الوتر وشده ثابتين يحفظ التردد نفسه فتظل النغمة ثابتة."],
            "السعة ↔ العلوّ؛ التردد ↔ الحِدة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b17:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Thermos vacuum flask, refraction air->water, translucent/opaque, sound in space, sound speed in solids/liquids/gases
    med_b17 = [
        (
            "A vacuum thermos flask keeps hot Arabic coffee piping hot for hours using a double-walled glass container with ALL air pumped out between the walls and shiny silver mirror coatings inside. How do the vacuum gap and silver coating reduce heat loss?",
            "تحفظ حافظة القهوة (الترمس) القهوة العربية ساخنة لساعات عبر جدار زجاجي مزدوج مفرّغ تماماً من الهواء بين جداريه ومطلي بالفضة اللامعة. كيف يمنع الفراغ والطلاء الفضي فقدان الحرارة؟",
            [
                ("The airless vacuum blocks conduction and convection, while shiny silver walls reflect thermal radiation back inward", "يمنع الفراغ التوصيل والحمل الحراري لانعدام المادة، ويعكس الطلاء الفضي اللامع الإشعاع الحراري للداخل"),
                ("The silver mirror creates electric sparks that boil coffee continuously", "يولد الطلاء الفضي شرارات تغلي القهوة باستمرار"),
                ("Vacuum speeds up convection currents tenfold around the coffee", "يسرّع الفراغ تيارات الحمل عشر مرات"),
                ("Glass conducts heat rapidly out of the flask to warm the room", "يوصل الزجاج الحرارة بسرعة لتدفئة الغرفة"),
            ],
            "Check all THREE heat transfer paths: Conduction, Convection (both need matter!) and Radiation (blocked/reflected by mirrors).",
            "تحقق من الطرق الثلاث: التوصيل والحمل (يحتاجان لمادة فيمنعهما الفراغ) والإشعاع (يعكسه السطح اللامع).",
            "Thermos flasks defeat all three modes: vacuum stops conduction/convection; silver stops radiation.",
            ["No air molecules between glass walls → neither conduction nor convection can cross the gap.", "Shiny reflective silver coating reflects infrared thermal radiation back into the coffee."],
            "For the exact same reason, the thermos keeps ice water cold for hours too!",
            "تُصمم الحافظة الحرارية لعزل طرق انتقال الحرارة الثلاث معاً.",
            ["تفريغ الهواء بين الجدارين يمنع التوصيل والحمل لغياب الجزيئات الناقلة.", "السطح الفضي اللامع يعكس الأشعة الحرارية عائدة للقهوة فلا تتسرب للخارج."],
            "كما تحفظ المشروبات المثلجة باردة بالآلية العكسية نفسها.",
            None, None,
        ),
        (
            "A student places a straight plastic straw into a glass of water and notices the submerged half looks broken or bent sharply at the water surface. Which wave behavior causes this visual illusion?",
            "وضع طالب مصاصة عصير مستقيمة داخل كوب ماء فلاحظ أن الجزء المغمور يبدو مكسوراً أو منحنياً عند سطح الماء. أي ظاهرة ضوئية تسبب هذا المنظر؟",
            [
                ("Refraction — light rays change speed and bend when crossing between water and air", "انكسار الضوء — تتغير سرعة الضوء وينحني مساره عند عبوره بين الماء والهواء"),
                ("Total absorption — water dissolves straight plastic straws temporarily", "الامتصاص الكامل للضوء — الماء يذيب المصاصة مؤقتاً"),
                ("Sound interference — room echoes bend plastic shapes", "تداخل الصوت — الصدى يثني الأجسام"),
                ("Thermal conduction — cold water melts light straight downward", "التوصيل الحراري"),
            ],
            "Light travels slower in water than in air, bending the rays heading toward your eyes!",
            "يسير الضوء في الماء أبطأ منه في الهواء، فينكسر مساره عند السطح الفاصل!",
            "Refraction bends light due to speed change across transparent media.",
            ["Light travels faster in air (~300,000 km/s) than in water (~225,000 km/s).", "When rays leaving the submerged straw exit into air, they bend away from the normal, making the straw appear shifted."],
            "Eyeglasses and magnifying lenses also rely on refraction!",
            "ينكسر الضوء عند انتقاله مائلاً بين وسطين شفافين مختلفي الكثافة الضوئية.",
            ["تتباطأ سرعة الضوء في الماء مقارنة بالهواء فتنحرف الأشعة عند سطح الماء.", "يفسر دماغنا الأشعة القادمة في خطوط مستقيمة فتبدو المصاصة مكسورة."],
            "العدسات والنظارات تعمل بمبدأ الانكسار نفسه.",
            svg_light_ray("refract", 40, "Normal", "Water", "Light Refraction"),
            svg_light_ray("refract", 40, "العمود المقام", "ماء", "انكسار الضوء"),
        ),
        (
            "Frosted bathroom window glass lets bright daylight enter a room, yet you cannot see sharp shapes of trees outside through it. How is frosted glass classified optically?",
            "يسمح زجاج النوافذ المُغبّش (المصنفر) بمرور ضوء النهار الساطع للداخل، لكنك لا تستطيع رؤية تفاصيل الأشجار بالخارج بوضوح عبره. كيف يُصنف هذا الزجاج بصرياً؟",
            [
                ("Translucent (transmits light while scattering rays)", "شبه شفاف (يسمح بمرور الضوء ولكنه يشتت الأشعة)"),
                ("Completely transparent (like clear air)", "شفاف تماماً مثل الزجاج الصافي"),
                ("Completely opaque (like solid brick wall)", "معتم تماماً مثل الجدار الطوبي"),
                ("Self-luminous plasma", "مضيء ذاتياً"),
            ],
            "Transparent = clear sharp image; Translucent = light passes blurry/scattered; Opaque = zero light passes.",
            "الشفاف = صورة واضحة؛ شبه الشفاف = يمر الضوء متشتتاً بلا تفاصيل واضحة؛ المعتم = يحجب الضوء كلياً.",
            "Translucent materials transmit light diffusely without preserving crisp images.",
            ["Clear window glass is transparent; wooden doors are opaque (casting crisp dark shadows).", "Frosted glass scatters incoming rays in many directions → translucent."],
            "Tissue paper and wax paper are also translucent.",
            "الأجسام شبه الشفافة تنفذ جزءاً من الضوء مع تشتيته.",
            ["يمر الضوء من الزجاج المصنفر فيضيء الغرفة.", "لكن سطحه الخشن يبعثر الأشعة فلا تتكون صورة واضحة للأشجار."],
            "أما الورق المشمع والضباب الخفيف فأمثلة أخرى شبه شفافة.",
            None, None,
        ),
        (
            "In a science-fiction movie, an astronaut watching from outside a space station sees a distant asteroid explode in a bright flash AND hears a deafening boom. What scientific error did the movie make?",
            "في فيلم خيال علمي، شاهد رائد فضاء خارج محطة الفضاء انفجار كويكب بعيد بوميض ساطع وسمع في اللحظة نفسها دوي انفجار يصم الآذان. ما الخطأ العلمي الذي وقع فيه الفيلم؟",
            [
                ("Light travels easily across the space vacuum, whereas sound CANNOT travel through empty space because it needs matter particles", "الضوء ينتقل عبر فراغ الفضاء، بينما الصوت لا ينتقل إطلاقاً في الفراغ لاحتياجه إلى وسط مادي"),
                ("Neither light nor sound can travel through space, so the flash is impossible too", "لا الضوء ولا الصوت ينتقلان في الفضاء"),
                ("Sound travels ten times faster than light in outer space", "الصوت أسرع من الضوء عشر مرات في الفضاء"),
                ("Asteroids freeze sound waves into bright flashes", "الكويكبات تجمد الصوت وتحوله لوميض"),
            ],
            "Sound is a mechanical vibration of atoms/molecules; electromagnetic light waves need zero medium!",
            "الصوت موجة ميكانيكية تتطلب اهتزاز جزيئات المادة؛ أما الضوء فموجة كهرومغناطيسية لا تحتاج لوسط!",
            "Light propagates through vacuum; mechanical sound waves require a medium.",
            ["Electromagnetic light crosses vacuum from stars and explosions.", "Without air molecules to push against one another, space is completely silent."],
            "Astronauts talk in space using radio waves (light-family waves) inside helmets!",
            "ينعدم الصوت في الفضاء الخارجي تماماً رغم انتشار الضوء.",
            ["يتكوّن الصوت من تضاغطات وتخلخلات في جسيمات المادة، ولا مادة في الفراغ تنقله.", "أما الضوء فينتقل عبر الفراغ ليصل لعين الرائد بصمت تام."],
            "لذلك يتواصل رواد الفضاء بموجات الراديو الكهرومغناطيسية.",
            None, None,
        ),
        (
            "Sound travels at about 340 m/s in air, 1,500 m/s in seawater, and nearly 5,900 m/s in solid steel. Why does sound travel FASTEST through solid steel?",
            "تبلغ سرعة الصوت في الهواء نحو 340 م/ث، وفي ماء البحر نحو 1500 م/ث، وفي الفولاذ الصلب نحو 5900 م/ث. لماذا ينتقل الصوت بأقصى سرعة له عبر الفولاذ الصلب؟",
            [
                ("Solid particles are tightly packed with strong elastic bonds, passing vibrations instantly from atom to atom", "لأن جسيمات المادة الصلبة متراصة جداً ومترابطة بقوة فتنتقل الاهتزازات فوراً من ذرة لأخرى"),
                ("Solid steel contains huge empty gaps for echoes to sprint through", "لأن الفولاذ يحتوي على فراغات شاسعة تجري فيها الموجات"),
                ("Air molecules absorb sound waves chemically into nitrogen", "لأن جزيئات الهواء تحلل الموجات الصوتية كيميائياً"),
                ("Sound moves fastest wherever temperature drops below freezing", "لأن الصوت يتسارع كلما انخفضت الحرارة تحت الصفر"),
            ],
            "Imagine dominoes lined up millimeter-apart (solid) vs. meters apart (gas)!",
            "تخيل قطع الدومينو متلاصقة تماماً (صلب) مقابل متباعدة جداً (غاز)!",
            "Sound speed increases with tighter particle spacing and stiffness: Solid > Liquid > Gas.",
            ["In gases, widely spaced molecules must travel across gaps to bump neighbors (slowest: 340 m/s).", "In rigid solids, tightly linked iron atoms transmit vibrations instantaneously (5,900 m/s)."],
            "That is why pressing an ear to a railroad rail detects an approaching train long before hearing it through air!",
            "يزداد سرعة انتقال الاهتزازات الصوتية كلما تقاربت الجسيمات وتماسكت روابطها.",
            ["الصلب متراص الجسيمات فتصل الدفعة الاهتزازية لجيرانها بلا تأخير (5900 م/ث).", "السائل متوسط التقارب (1500 م/ث)، والغاز متباعد الجسيمات فهو الأبطأ (340 م/ث)."],
            "لذلك تسمع اقتراب القطار عبر القضبان قبل سماعه في الهواء.",
            svg_bar_chart([("Air", 340, BLUE), ("Water", 1500, GREEN), ("Steel", 5900, ORANGE)], "Speed (m/s)", "Sound Speed by Medium"),
            svg_bar_chart([("الهواء", 340, BLUE), ("الماء", 1500, GREEN), ("الفولاذ", 5900, ORANGE)], "السرعة (م/ث)", "سرعة الصوت في الأوساط"),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b17:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Cooling radiation/insulation table, echo distance math, colored light reflection, string pitch, mirror surface-angle trick
    cool_tbl_en = svg_data_table(["Can Wrap", "Start (°C)", "After 15m (°C)"], [["Matte Black", "80", "51"], ["Shiny Silver", "80", "64"], ["Thick Foam", "80", "73"]], "Hot Water Cooling Test", [112, 100, 120])
    cool_tbl_ar = svg_data_table(["غلاف العلبة", "البداية (°م)", "بعد 15 د (°م)"], [["أسود مطفي", "80", "51"], ["فضي لامع", "80", "64"], ["فوم سميك", "80", "73"]], "تجربة تبريد الماء الساخن", [110, 102, 120])
    B.add_concept(
        tp, "Hard", bp,
        "Three identical metal cans filled with 80°C water sit in a 22°C room for 15 minutes as recorded in the table. Why did the Matte Black can cool down fastest (to 51°C), while Shiny Silver stayed warmer (64°C) than Matte Black?",
        "ملئت ثلاث علب معدنية متطابقة بماء حرارته 80°م وتُركت في غرفة حرارتها 22°م لمدة 15 دقيقة كما في الجدول. لماذا بردت العلبة السوداء المطفية أسرع ما يمكن (إلى 51°م)، بينما بقيت الفضية اللامعة أدفأ منها (64°م)؟",
        [
            ("Dark matte surfaces are strong emitters of thermal radiation (losing heat rapidly), whereas shiny silver reflects radiation inward", "الأسطح الداكنة المطفية باعثة قوية للإشعاع الحراري (فتفقد الحرارة سريعاً)، بينما تعكس الفضية اللامعة الإشعاع للداخل"),
            ("Black color slows down conduction inside metal atoms", "اللون الأسود يبطئ التوصيل داخل ذرات المعدن"),
            ("Silver foil attracts warm air currents to heat the can up", "الورق الفضي يجذب هواء الغرفة لتسخين العلبة"),
            ("Foam absorbs 100% of radiant light to boil water up to 73°C", "الفوم يمتص الإشعاع ليغلي الماء إلى 73°م"),
        ],
        "Dark matte surfaces absorb AND radiate thermal energy best; shiny surfaces reflect radiation best! Foam insulates conduction.",
        "الأسطح السوداء المطفية ممتازة في امتصاص وإشعاع الحرارة، والفضية اللامعة تعكسها؛ والفوم يمنع التوصيل.",
        "Good absorbers of thermal radiation are also strong emitters.",
        ["Both Matte Black and Shiny Silver are bare metal walls, differing only in surface radiation.", "Matte Black radiated heat out fastest (-29°C drop); Shiny Silver reflected heat back inside (-16°C); Foam blocked conduction (-7°C)."],
        "That is why space blankets are shiny silver, while solar water heaters are painted matte black!",
        "كلما كان السطح داكناً ومطفياً زادت قدرته على إشعاع الحرارة وامتصاصها.",
        ["انخفضت السوداء 29°م لأن السطح الأسود يبعث الأشعة تحت الحمراء بكفاءة عالية.", "انخفضت الفضية 16°م فقط لأنها تعكس الإشعاع للداخل، وحافظ الفوم العازل على أعلى حرارة (73°م)."],
        "لذلك تُطلى مجمعات السخانات الشمسية بالأسود لتمتص أكبر طاقة.",
        cool_tbl_en, cool_tbl_ar,
    )

    B.add_math(
        tp, "Hard", bp,
        "A hiker standing near a canyon wall in Al-Ula shouts and hears her clear echo return exactly 4 seconds later. If sound travels through desert air at 340 m/s, how many meters away is the canyon cliff?",
        "وقف متنزّه قرب جدار وادٍ صخري في العلا وصرخ، فسمع صدى صوته عائداً بوضوح بعد 4 ثوانٍ تماماً. إذا كانت سرعة الصوت في الهواء 340 م/ث، فكم متراً يبعد الجدار الصخري عنه؟",
        680, [85, 340, 1360],
        "Careful! In 4 seconds, the sound traveled THERE AND BACK (twice the cliff distance)! Divide total distance by 2.",
        "انتبه! خلال 4 ثوانٍ قطع الصوت المسافة ذهاباً وإياباً (ضعف البعد)! اقسم المسافة الكلية على 2.",
        "Echo cliff distance = (speed × round-trip echo time) ÷ 2.",
        ["Round-trip sound distance = 340 × 4 = 1,360 m.", "One-way cliff distance = 1,360 ÷ 2 = 680 m."],
        "2 s to reach the wall (680 m) + 2 s to bounce back (680 m) = 4 s.",
        "زمن الصدى يشمل رحلة الذهاب إلى الحاجز ورحلة العودة إلى الأذن.",
        ["المسافة الكلية ذهاباً وإياباً = 340 × 4 = 1360 متراً.", "بُعد الجدار الصخري = 1360 ÷ 2 = 680 متراً."],
        "تحقق: ثانيتان للوصول (680 م) + ثانيتان للارتداد = 4 ثوانٍ.",
    )

    hard_b17 = [
        (
            "In a dark theater, an actor wears a pure BLUE jersey under white stage lights. Suddenly the stage technician turns off white lights and shines ONLY pure RED light onto the jersey. What color does the blue jersey now appear to the audience?",
            "في مسرح مظلم، يرتدي ممثل قميصاً أزرق نقياً تحت إضاءة بيضاء. فجأة أطفأ الفني الإضاءة البيضاء وسلّط على القميص ضوءاً أحمر نقياً فقط. بأي لون يبدو القميص الأزرق للجمهور الآن؟",
            [
                ("Almost completely BLACK (dark) because blue pigment absorbs red light and has zero blue light to reflect", "أسود تقريباً (داكن) لأن صبغة اللون الأزرق تمتص الضوء الأحمر ولا تجد ضوءاً أزرق لتعكسه"),
                ("Bright glowing PURPLE because red and blue pigments mix into light", "بنفسجي متوهج لأن الصبغة تمزج الأحمر بالأزرق"),
                ("Bright WHITE because blue shirts mirror every colored spotlight", "أبيض ساطع لأن القميص الأزرق يعكس كل الأضواء"),
                ("Bright GREEN because blue plus red cancels to green", "أخضر ساطع"),
            ],
            "An object looks blue under white light because it reflects ONLY blue and absorbs red and green. What happens when zero blue arrives?",
            "يبدو القميص أزرق تحت الضوء الأبيض لأنه يعكس الأزرق فقط ويمتص الأحمر والأخضر؛ فماذا يعكس إذا سقط عليه أحمر فقط؟",
            "Opaque pigments reflect only their matching wavelengths and absorb all others.",
            ["Pure blue dye reflects blue light and absorbs red and green wavelengths.", "Under pure red light, the red light gets absorbed and nothing reflects to viewers' eyes → appears black!"],
            "Only under white light (which contains red + green + blue) can a blue shirt reflect blue.",
            "نرى الأجسام المعتمة بألوان الضوء الذي تعكسه نحو أعيننا فقط.",
            ["يمتص القميص الأزرق اللون الأحمر الساقط عليه تماماً.", "وبعدم وجود ضوء أزرق ليعكسه، لا يصل للعين أي ضوء فيظهر القميص أسود."],
            "يوضح ذلك كيفية امتصاص الأصباغ وانعكاس الألوان.",
            None, None,
        ),
        (
            "A student builds a guitar using four strings of different lengths and tensions and wants string #1 to produce the HIGHEST pitch (highest frequency). Which combination produces the highest musical pitch?",
            "صنعت طالبة آلة وترية بأربعة أوتار مختلفة الأطوال والشد، وتريد أن يُصدر الوتر رقم 1 أعلى حدة صوت (أعلى تردد). أي مواصفات للوتر تُصدر أعلى صوت حدةً؟",
            [
                ("Shortest length, thinnest diameter, and tightest tension", "أقصر طولاً، وأرفع سُمكاً، وأشدّ توتراً (شداً)"),
                ("Longest length, thickest diameter, and loosest tension", "أطول طولاً، وأسمك قطراً، وأقل شداً"),
                ("Longest length and tightest tension, plucked very gently", "أطول طولاً وأقل شداً"),
                ("Thickest diameter and shortest length with zero tension", "أسمك قطراً وأقصر طولاً بلا شد"),
            ],
            "Faster vibration = higher frequency = higher pitch! Short, thin, tight strings vibrate fastest.",
            "الاهتزاز الأسرع = تردد أعلى = صوت أحدّ! الوتر القصير الرفيع المشدود يهتز بأقصى سرعة.",
            "Higher frequency (shorter, thinner, tighter string) yields higher pitch.",
            ["Short length reduces wavelength.", "Thin light mass and high tension snap back rapidly, raising vibration frequency and pitch."],
            "Long, thick, loose bass strings vibrate slowly for deep low-pitched notes.",
            "تزداد حدة الصوت (التردد) كلما قصر الوتر وقلّ سمكه وزاد شَدّه.",
            ["القصر والرفع والشد القوي كلها تسرّع عودة الوتر في كل ذبذبة.", "يرتفع التردد فينتج صوت حاد مرتفع الدرجة."],
            "أما الأوتار الطويلة السميكة المرتخية فتنتج أصواتاً غليظة منخفضة التردد.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b17:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    B.add_math(
        tp, "Hard", bp,
        "A beam of sunlight hits a flat glass mirror at an angle of 25° measured from the FLAT MIRROR SURFACE (NOT from the perpendicular normal!). What is the angle of reflection measured from the perpendicular normal line?",
        "يسقط شعاع شمس على مرآة مستوية بزاوية 25° مقاسة مع سطح المرآة نفسه (وليس مع العمود المقام!). ما مقدار زاوية الانعكاس المقاسة مع العمود المقام على المرآة؟",
        65, [25, 50, 115],
        "The normal line makes 90° with the mirror surface! Subtract 25° from 90° first to get the angle of incidence from the normal.",
        "يصنع العمود المقام زاوية 90° مع سطح المرآة! اطرح 25° من 90° أولاً لإيجاد زاوية السقوط.",
        "Angle of incidence is always measured from the surface normal (90° − grazing angle).",
        ["Angle from normal = 90° - 25° = 65° (angle of incidence).", "By Law of Reflection, angle of reflection from the normal = 65°."],
        "65° + 25° = 90°.",
        "الزاوية المعتمدة في قانون الانعكاس هي المحصورة بين الشعاع والعمود المقام.",
        ["بما أن الزاوية مع السطح 25°، فزاوية السقوط مع العمود المقام = 90° − 25° = 65°.", "وبالتالي تساوي زاوية الانعكاس 65°."],
        "تحقق: 65° + 25° = 90°.",
        "",
        svg_light_ray("reflect", 65, "Normal", "25° to surface", "Grazing Ray Check"),
        svg_light_ray("reflect", 65, "العمود المقام", "25° مع السطح", "زاوية السقوط الفعلية"),
    )


def _add_b18(B: G6SciBankBuilder) -> None:
    tp, bp = "Physics: Forces & Energy", "G6-SCI-B18"
    # Easy (0..4): Circuit essentials, identify series diagram, open loop effect, parallel bulb failure, electromagnet parts
    easy_b18 = [
        (
            "In a simple electric circuit powering a flashlight bulb, what role do the battery and copper wires play?",
            "في دائرة كهربائية بسيطة تضيء مصباحاً، ما وظيفة كلٍّ من البطارية وأسلاك النحاس؟",
            [
                ("The battery provides electrical energy (voltage push); copper wires provide a closed conducting path for charges", "توفر البطارية الطاقة الكهربائية (الجهد الدافع)، وتوفر أسلاك النحاس مساراً موصلاً مغلقاً لسريان الشحنات"),
                ("Copper wires generate electricity while the battery insulates electrons", "تولد أسلاك النحاس الكهرباء وتعزل البطارية الشحنات"),
                ("The battery absorbs light while wires store heat inside switches", "تمتص البطارية الضوء وتخزن الأسلاك الحرارة"),
                ("Both act as high-resistance insulators to block electric current", "يعمل كلاهما كعوازل لمنع مرور التيار"),
            ],
            "Every working circuit needs an energy source, a closed conducting loop, and a load (plus an optional switch).",
            "كل دائرة تعمل تحتاج إلى مصدر طاقة ومسار موصل مغلق وحمل كهربائي (ومفتاح اختياري).",
            "Batteries drive electrical potential; metallic conductors carry current around a closed loop.",
            ["Chemical reactions inside the battery push electrons around the circuit.", "Ductile copper wires connect battery → switch → bulb → back to battery."],
            "If any gap opens the loop, current stops everywhere immediately.",
            "تضخ البطارية الطاقة وتنقل الأسلاك المعدنية التيار في مسار مغلق.",
            ["توفر البطارية فرق الجهد الذي يحرك الشحنات في الدائرة.", "تشكل أسلاك النحاس مساراً منخفض المقاومة بين البطارية والمصباح."],
            "انقطاع المسار في أي نقطة يفتح الدائرة ويوقف التيار.",
            svg_bulb_circuit("series", "6 V", "Switch", "Switch", "Simple Loop Circuit"),
            svg_bulb_circuit("series", "6 V", "مفتاح", "مفتاح", "الدائرة المغلقة البسيطة"),
        ),
        (
            "Look at the circuit diagram containing a 12 V battery and two resistors (4 Ω and 4 Ω) wired one right after another in a single rectangular loop. How are these two loads connected?",
            "انظر إلى مخطط الدائرة الذي يضم بطارية 12 فولت ومقاومتين (4 أوم و4 أوم) موصولتين تلو الأخرى في حلقة واحدة مستطيلة. كيف وُصلت المقاومتان؟",
            [("In series (single continuous path)", "على التوالي (مسار واحد متواصل)"), ("In parallel (two independent branches)", "على التوازي (فرعان مستقلان)"), ("As an open broken circuit", "كدائرة مفتوحة منقطعة"), ("Inside an iron electromagnet coil", "داخل ملف مغناطيس كهربائي")],
            "Trace from the battery's positive terminal back to negative: how many distinct pathways exist?",
            "تتبع المسار من البطارية وعُد إليها: كم مساراً مختلفاً يمكن للتيار أن يسلكه؟",
            "Series circuits provide exactly one single current pathway through all components.",
            ["All electric current leaves the 12 V source, passes through the first 4 Ω load, then the second 4 Ω load, and returns.", "Only one closed loop exists → series connection."],
            "Parallel circuits split wires at junctions into 2 or more branches.",
            "التوصيل على التوالي يعني وجود مسار واحد فقط يسلكه التيار عبر جميع المكونات.",
            ["يمر التيار نفسه في المقاومة الأولى ثم الثانية دون أي تفرع.", "إذن التوصيل على التوالي."],
            "لو وجدت نقطتا تفرع متوازيتان لكان التوصيل على التوازي.",
            _ohm_svgs(12, [4, 4], "series", "Single-Loop Circuit", "دائرة مسار واحد")[0],
            _ohm_svgs(12, [4, 4], "series", "Single-Loop Circuit", "دائرة مسار واحد")[1],
        ),
        (
            "In a string of older holiday lights wired in SERIES (B1 and B2 in one single loop as shown), what happens to bulb B2 if bulb B1's filament burns out and snaps?",
            "في سلسلة مصابيح زينة موصولة على التوالي (المصباحان B1 و B2 في حلقة واحدة كما بالرسم)، ماذا يحدث للمصباح B2 إذا احترق فتيل المصباح B1 وانقطع؟",
            [
                ("Bulb B2 goes completely OFF too because the single path is now open", "ينطفئ المصباح B2 تماماً أيضاً لأن المسار الوحيد قد انقطع وأصبح مفتوحاً"),
                ("Bulb B2 shines twice as brightly as before", "يزداد توهج المصباح B2 للضعف"),
                ("Bulb B2 stays lit at normal brightness unaffected", "يبقى المصباح B2 مضيئاً بالإضاءة نفسها"),
                ("The battery instantaneously rewires itself into parallel", "تتحول البطارية تلقائياً لتوصيل التوازي"),
            ],
            "In a series loop, one broken bulb acts just like opening a switch!",
            "في دائرة التوالي، تلف مصباح واحد يشبه فتح المفتاح الكهربائي تماماً!",
            "Breaking any component in a series circuit halts current everywhere in the loop.",
            ["Current must pass through B1 to reach B2.", "Once B1 snaps, an air gap stops electron flow through the whole loop, turning B2 off."],
            "Parallel wiring solves this frustrating problem!",
            "انقطاع أي جزء في دائرة التوالي يوقف التيار عن جميع الأجزاء.",
            ["المسار متصل واحد، فاحتراق B1 يفتح الدائرة الكهربائية.", "يتوقف مرور التيار فينطفئ المصباح B2 فوراً."],
            "تلك هي أبرز عيوب التوصيل على التوالي.",
            svg_bulb_circuit("series", "9 V", "Closed", "Closed", "Series Break Impact"),
            svg_bulb_circuit("series", "9 V", "مغلق", "مغلق", "أثر انقطاع التوالي"),
        ),
        (
            "Now inspect the PARALLEL circuit diagram showing two separate branches (6 Ω and 6 Ω) connected across the same 12 V battery. If the top branch is disconnected or burns out, what happens to the lower 6 Ω branch?",
            "تأمل الآن مخطط الدائرة على التوازي بفرعين مستقلين (6 أوم و6 أوم) متصلين بالبطارية نفسها (12 فولت). إذا انقطع الفرع العلوي، فماذا يحدث للفرع السفلي؟",
            [
                ("The lower branch stays completely ON and keeps working normally", "يبقى الفرع السفلي متصلاً ومضيئاً ويعمل بشكل طبيعي تماماً"),
                ("Both branches shut off immediately like a series string", "ينطفئ الفرعان فوراً مثل التوالي"),
                ("Voltage across the lower branch drops to 0 V", "يهبط الجهد في الفرع السفلي إلى صفر فولت"),
                ("The battery turns into a wooden insulator", "تتحول البطارية إلى عازل خشبي"),
            ],
            "Trace the lower rectangular loop back to the 12 V battery — is it still a closed loop?",
            "تتبع الحلقة السفلية إلى البطارية — هل ما زالت حلقة مغلقة مكتملة؟",
            "In parallel circuits, each branch maintains an independent closed loop to the source.",
            ["Top and bottom loads lie on separate parallel branches.", "Cutting the top branch leaves the bottom branch's loop intact across the full 12 V battery."],
            "That is why homes and schools wire lamps and outlets in parallel!",
            "في التوازي يمتلك كل فرع مساراً مستقلاً نحو المصدر فلا يتأثر بتعطل الآخر.",
            ["الفرع السفلي ما زال يشكّل دائرة مغلقة مكتملة مع البطارية 12 فولت.", "لذا يستمر عمله بانتظام عند فصل الفرع العلوي."],
            "هذا سبب اعتماد التوصيل على التوازي في المباني.",
            _ohm_svgs(12, [6, 6], "parallel", "Parallel Branches", "دائرة التوازي")[0],
            _ohm_svgs(12, [6, 6], "parallel", "Parallel Branches", "دائرة التوازي")[1],
        ),
        (
            "A student wraps 30 turns of insulated copper wire tightly around a large soft iron nail and connects both bare wire ends to a fresh 1.5 V D-cell battery. When she touches the nail tip to metal paperclips, it picks up 8 clips. What device did she build?",
            "لفّت طالبة 30 لفة من سلك نحاسي معزول بإحكام حول مسمار حديدي كبير ووصلت طرفيه ببطارية 1.5 فولت، فجذب رأس المسمار 8 مشابك ورق معدنية. ما الجهاز الذي صنعته؟",
            [
                ("An electromagnet (a temporary magnet controlled by electric current)", "مغناطيس كهربائي (مغناطيس مؤقت يتحكم فيه التيار الكهربائي)"),
                ("A solar photovoltaic panel", "خلية شمسية كهروضوئية"),
                ("A permanent bar magnet that stays strong forever without batteries", "مغناطيس دائم يبقى قوياً للأبد دون بطارية"),
                ("A gravitational spring balance", "ميزان نابضي للجاذبية"),
            ],
            "Electric current flowing through a coil generates a magnetic field concentrated by the iron core!",
            "مرور التيار الكهربائي في ملف سلكي يولد مجالاً مغناطيسياً يقوّيه قلب الحديد!",
            "Electromagnets convert electrical current into a switchable magnetic field.",
            ["Current spiraling through insulated copper turns produces a magnetic field.", "The soft iron nail concentrates that field; disconnecting the battery turns magnetism right back off!"],
            "Scrapyard cranes use huge electromagnets to lift and drop steel cars on command.",
            "المغناطيس الكهربائي ينشأ عن سريان تيار في ملف حول قلب حديدي، ويزول بزوال التيار.",
            ["ينتج التيار في اللفات مجالاً مغناطيسياً يتمغنط به المسمار الحديدي مؤقتاً.", "وعند فصل البطارية يفقد المسمار مغناطيسيته وتسقط المشابك."],
            "تُستخدم هذه الميزة في الأجراس الكهربائية ورافعات الخردة.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b18:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Total series resistance math, series vs parallel brightness, house parallel wiring, electromagnet booster table, short circuit
    B.add_math(
        tp, "Medium", bp,
        "Two resistors of 5 Ω and 7 Ω are connected end-to-end in SERIES across a 12 V battery as shown. What is the TOTAL electrical resistance of the series circuit in ohms (Ω)?",
        "وُصلت مقاومتان قيمتهما 5 أوم و7 أوم على التوالي مع بطارية 12 فولت كما في المخطط. ما المقاومة الكهربائية الكلية للدائرة بوحدة الأوم (Ω)؟",
        12, [2, 6, 35],
        "In a series circuit, total resistance equals the sum of individual resistances: R_total = R1 + R2.",
        "في التوصيل على التوالي، المقاومة الكلية تساوي مجموع المقاومات: R_total = R1 + R2.",
        "Series resistances add directly because current passes through every load sequentially.",
        ["Identify resistors: R₁ = 5 Ω and R₂ = 7 Ω.", "Total series resistance = 5 + 7 = 12 Ω."],
        "5 + 7 = 12 Ω.",
        "في التوالي يواجه التيار المقاومتين الواحدة تلو الأخرى فتُجمع قيمتاهما.",
        ["المقاومة الأولى = 5 أوم والثانية = 7 أوم.", "المقاومة الكلية = 5 + 7 = 12 أوم."],
        "تحقق: 5 + 7 = 12 أوم.",
        "",
        _ohm_svgs(12, [5, 7], "series", "Series Resistors", "مقاومات على التوالي")[0],
        _ohm_svgs(12, [5, 7], "series", "Series Resistors", "مقاومات على التوالي")[1],
    )

    med_b18 = [
        (
            "A student connects ONE bulb to a 9 V battery and notes its bright glow. She then adds a SECOND identical bulb in SERIES into the same single loop. What happens to the brightness of both bulbs?",
            "وصلت طالبة مصباحاً واحداً ببطارية 9 فولت فلاحظت سطوعه القوي، ثم أضافت مصباحاً ثانياً مماثلاً على التوالي في الحلقة نفسها. ماذا يحدث لإضاءة المصباحين؟",
            [
                ("Both bulbs glow noticeably DIMMER because total circuit resistance doubled and cut the current in half", "يصبح توهج المصباحين أضعف بوضوح لأن المقاومة الكلية تضاعفت فنقص التيار إلى النصف"),
                ("Both bulbs shine twice as brightly because two bulbs multiply voltage", "يتوهج كلاهما للضعف"),
                ("The first bulb stays bright while the second bulb stays completely dark", "يظل الأول ساطعاً وينطفئ الثاني"),
                ("Both bulbs stay at full brightness because 9 V pushes unlimited current", "يبقى السطوع كاملاً"),
            ],
            "More bulbs in one single series line = more resistance slowing down the shared current!",
            "إضافة مصابيح في مسار توالٍ واحد يزيد المقاومة الكلية فيقل التيار المار بالجميع!",
            "Adding loads in series increases total resistance and dims each bulb.",
            ["One bulb gets the full 9 V push.", "Two series bulbs share the 9 V (4.5 V each) and double resistance, halving current → dimmer glow."],
            "By contrast, adding a second bulb in PARALLEL keeps both at full brightness!",
            "التوصيل على التوالي يقسّم الجهد ويزيد المقاومة فتضعف الإضاءة.",
            ["يتشارك المصباحان جهد البطارية (9 فولت) فتقل حصة كل مصباح.", "كما تتضاعف المقاومة فيقل التيار المار عبرهما وتخفت الإضاءة."],
            "أما في التوازي فيحصل كل مصباح على الجهد الكامل ويحتفظ بسطوعه.",
            _ohm_svgs(9, [3, 3], "series", "2 Bulbs in Series", "مصباحان على التوالي")[0],
            _ohm_svgs(9, [3, 3], "series", "2 Bulbs in Series", "مصباحان على التوالي")[1],
        ),
        (
            "Why are electrical wall outlets and ceiling lights inside Saudi homes ALWAYS wired in parallel circuits rather than one giant series loop?",
            "لماذا تُوصّل مقابس الكهرباء وإضاءة الأسقف في المنازل دائماً على التوازي وليس في حلقة توالٍ واحدة؟",
            [
                ("Each appliance receives full line voltage independently and can be turned ON/OFF without shutting off the whole house", "ليحصل كل جهاز على الجهد الكامل بشكل مستقل ويمكن تشغيله أو إطفاؤه دون فصل باقي أجهزة المنزل"),
                ("Parallel wiring raises total resistance so refrigerators draw zero current", "لأن التوازي يرفع المقاومة فتتوقف الثلاجات عن سحب التيار"),
                ("Series wiring prevents television screens from working with batteries", "لأن التوالي يمنع التلفاز من العمل بالبطاريات"),
                ("Parallel wires use wood instead of copper to save energy", "لأن أسلاك التوازي تصنع من الخشب بدلاً من النحاس"),
            ],
            "Imagine having to keep your oven, AC, and bedroom lamp ALL switched on at once just so the fridge stays cold!",
            "تخيل لو اضطررت لتشغيل الفرن والمكيف والمصباح معاً كي لا تنطفئ الثلاجة!",
            "Parallel household wiring provides independent switching and constant full voltage.",
            ["If wired in series, switching off one bedroom light would cut power to the kitchen refrigerator!", "In parallel, every branch gets equal voltage and independent switches."],
            "Circuit breakers protect parallel branches against overloading too many appliances.",
            "يتيح التوصيل على التوازي استقلالية كل جهاز وثبات الجهد عبره.",
            ["في التوازي، إطفاء مصباح غرفة لا يقطع الكهرباء عن الغرف أو الثلاجة.", "ويحصل كل جهاز على الجهد القياسي الكامل للمنزل."],
            "تحمي القواطع الكهربائية الفروع المتوازية من التحميل الزائد.",
            None, None,
        ),
        (
            "A student wants her homemade nail electromagnet to lift 30 steel tacks instead of only 10. Based on electromagnet physics, which change will FAIL to strengthen the magnet?",
            "تريد طالبة تقوية مغناطيسها الكهربائي المصنوع من مسمار ليرفع 30 دبوساً فولاذياً بدلاً من 10 فقط. أي تعديل مما يلي سيفشل ولن يقوّي المغناطيس؟",
            [
                ("Replacing the iron nail core with a dry wooden dowel of the same size", "استبدال قلب المسمار الحديدي بقضيب خشبي جاف من الحجم نفسه"),
                ("Wrapping 90 coils of wire neatly instead of 30 coils", "زيادة عدد اللفات إلى 90 لفة بدلاً من 30 لفة"),
                ("Connecting two 1.5 V batteries in series (3.0 V) instead of one", "توصيل بطاريتين على التوالي (3 فولت) بدلاً من بطارية واحدة"),
                ("Using thicker low-resistance copper wire to increase electric current", "استخدام سلك نحاسي أقل مقاومة لزيادة شدة التيار"),
            ],
            "More coils + stronger current + ferromagnetic IRON core boost strength! What happens if you swap iron for nonmagnetic wood?",
            "زيادة اللفات + زيادة التيار + قلب حديدي تقوّي المغناطيس! ماذا لو بدّلنا الحديد بالخشب غير المغناطيسي؟",
            "Electromagnet strength depends on coil turns, current, and ferromagnetic core permeability.",
            ["More wire turns, higher battery voltage/current, and soft iron cores all amplify magnetic field.", "Wood is non-ferromagnetic and adds zero magnetic amplification, severely weakening the magnet!"],
            "Soft iron loses its magnetism cleanly once current shuts off — unlike steel which may stay slightly magnetized.",
            "يعتمد المغناطيس الكهربائي على التيار وعدد اللفات ونفاذية القلب الحديدي.",
            ["زيادة اللفات وزيادة الجهد/التيار ترفع شدة المجال المغناطيسي.", "أما الخشب فلا يتمغنط ولا يركز خطوط المجال فيضعف المغناطيس بشدة."],
            "الحديد المطاوع هو أفضل قلب للمغناطيس الكهربائي المؤقت.",
            None, None,
        ),
        (
            "While building a bulb circuit, a student accidentally touches a bare copper jumper wire directly across both terminals of the 9 V battery, bypassing the light bulb completely. Within seconds the wire and battery grow dangerously hot and the bulb goes out. What happened?",
            "أثناء تركيب دائرة مصباح، لمس طالب سلكاً نحاسياً عارياً مباشرة بين قطبي بطارية 9 فولت متجاوزاً المصباح تماماً. خلال ثوانٍ سَخِن السلك والبطارية بشدة وانطفأ المصباح. ما الذي حدث؟",
            [
                ("A short circuit occurred: huge current surged through the tiny-resistance wire bypass instead of the bulb", "حدث تماس كهربائي (دائرة قصر): تدفق تيار هائل عبر السلك قليل المقاومة متجاوزاً المصباح"),
                ("The light bulb converted copper into dry plastic", "حوّل المصباح النحاس إلى بلاستيك جاف"),
                ("Current reversed direction and froze electrons inside the bulb", "انعكس اتجاه التيار وتجمدت الإلكترونات داخل المصباح"),
                ("Gravity pulled voltage downward out of the copper wire", "سحبت الجاذبية الجهد للأسفل خارج السلك"),
            ],
            "Current always prefers the path of almost ZERO resistance — creating dangerous overheating!",
            "يفضل التيار دائماً المسار ذا المقاومة الضئيلة جداً — مما يسبب حرارة عالية خطيرة!",
            "Short circuits bypass load resistance, causing excessive current and thermal hazard.",
            ["Bare copper wire has nearly 0 Ω resistance compared with the bulb filament.", "Almost all current rushed through the shortcut wire, generating rapid heat and draining/damaging the battery."],
            "Fuses and circuit breakers melt or trip during short circuits to prevent electrical fires!",
            "دائرة القصر مسار جانبي منخفض المقاومة يمتص تياراً خطيراً.",
            ["تجاوز التيار المصباح ومر عبر السلك العاري ذي المقاومة شبه المعدومة.", "أدى ارتفاع شدة التيار المفاجئ إلى سخونة شديدة وانطفاء المصباح."],
            "المنصهرات والقواطع تفصل الدائرة تلقائياً عند حدوث قصر للحماية من الحرائق.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b18:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): 2-switch parallel logic, electromagnet data table, Ohm's law series current math, static vs current, circuit troubleshooting
    B.add_concept(
        tp, "Hard", bp,
        "Inspect the two-branch parallel circuit with Bulb B1 + Switch S1 on the top branch and Bulb B2 + Switch S2 on the bottom branch. If Switch S1 is left OPEN while Switch S2 is CLOSED, which bulbs light up?",
        "تأمل الدائرة المتوازية المكونة من فرعين: الفرع العلوي فيه المصباح B1 والمفتاح S1، والفرع السفلي فيه المصباح B2 والمفتاح S2. إذا تُرك المفتاح S1 مفتوحاً وأُغلق المفتاح S2، فأي المصابيح يضيء؟",
        [
            ("Only Bulb B2 lights up; Bulb B1 stays off", "يضيء المصباح B2 فقط، ويبقى المصباح B1 مطفأً"),
            ("Both B1 and B2 light up brightly", "يضيء كلٌّ من B1 و B2 معاً"),
            ("Neither B1 nor B2 lights up because S1 is open", "لا يضيء أي منهما لأن S1 مفتوح"),
            ("Only Bulb B1 lights up; Bulb B2 stays off", "يضيء المصباح B1 فقط"),
        ],
        "Closed switch = complete path! Open switch = broken gap! Trace each parallel branch separately.",
        "مفتاح مغلق = مسار مكتمل! مفتاح مفتوح = مسار مقطوع! تتبّع كل فرع على حدة.",
        "Independent switches in parallel branches control each branch individually.",
        ["Top branch has S1 OPEN → no complete path through B1 → B1 stays off.", "Bottom branch has S2 CLOSED → complete closed loop from 12 V battery through B2 → B2 lights up!"],
        "That is how one wall switch controls kitchen lights while another controls hallway lights.",
        "يتحكم كل مفتاح في فرعه المستقل في التوصيل على التوازي.",
        ["الفرع العلوي مفتوح عند S1 فلا يمر تيار في المصباح B1.", "الفرع السفلي مغلق عند S2 فتكتمل دورته مع البطارية ويضيء المصباح B2 وحده."],
        "إغلاق الدائرة يعني تمام التوصيل ومرور التيار.",
        svg_bulb_circuit("parallel", "12 V", "S1 OPEN", "S2 CLOSED", "Parallel Switch Control"),
        svg_bulb_circuit("parallel", "12 V", "S1 مفتوح", "S2 مغلق", "التحكم بمفاتيح التوازي"),
    )

    em_tbl_en = svg_data_table(["Trial", "Coils", "Batteries", "Clips Lifted"], [["1", "20", "1", "6"], ["2", "40", "1", "12"], ["3", "40", "2", "24"], ["4", "60", "2", "?"]], "Electromagnet Lab Data", [62, 68, 92, 102])
    em_tbl_ar = svg_data_table(["المحاولة", "اللفات", "البطاريات", "المشابك"], [["1", "20", "1", "6"], ["2", "40", "1", "12"], ["3", "40", "2", "24"], ["4", "60", "2", "؟"]], "بيانات المغناطيس الكهربائي", [66, 68, 92, 96])
    B.add_math(
        tp, "Hard", bp,
        "A student records how many paperclips an electromagnet lifts when varying coil turns and batteries in the data table. Following the exact proportional pattern shown in Trials 1–3, how many paperclips should Trial 4 (60 coils, 2 batteries) lift?",
        "سجل طالب عدد مشابك الورق التي يرفعها مغناطيس كهربائي عند تغيير عدد اللفات والبطاريات في الجدول المرفق. باتباع النمط التناسبي نفسه في المحاولات 1–3، كم مشبكاً يُتوقع أن ترفع المحاولة 4 (60 لفة، بطاريتان)؟",
        36, [18, 28, 48],
        "Look at Trials 1 → 2 (1 battery: 20 coils = 6 clips, 40 coils = 12 clips → 0.3 clips per coil). With 2 batteries (Trial 3), 40 coils lifted 24 clips (0.6 clips per coil). Now multiply 60 × 0.6!",
        "في بطارية واحدة: كل 20 لفة ترفع 6 مشابك (40 لفة = 12). مع بطاريتين يتضاعف الناتج: 40 لفة ترفع 24 مشبكاً (0.6 لكل لفة). اضرب 60 × 0.6!",
        "Magnetic strength scales proportionally with (coil turns) × (voltage/current).",
        ["At 2 batteries, 40 coils lifts 24 clips → rate = 24 ÷ 40 = 0.6 clips/coil (or 12 clips per 20 coils).", "For 60 coils (= 3 × 20 coils) at 2 batteries: 3 × 12 = 36 clips!"],
        "Check: Trial 3 had 40 coils (24 clips); adding 50% more coils (60) adds 50% more clips (24 + 12 = 36).",
        "تزداد قوة المغناطيس طردياً مع كلٍّ من عدد اللفات وعدد البطاريات.",
        ["عند بطاريتين: كل 20 لفة ترفع 12 مشبكاً (40 لفة رفعت 24 مشبكاً).", "إذن 60 لفة (ثلاثة أضعاف الـ 20 لفة) ترفع 3 × 12 = 36 مشبكاً."],
        "تحقق: زيادة اللفات من 40 إلى 60 بنسبة 50% ترفع 24 بنسبة 50% إلى 36.",
        "", em_tbl_en, em_tbl_ar,
    )

    B.add_math(
        tp, "Hard", bp,
        "In the series circuit diagram, a 12 V battery drives current through a 2 Ω resistor and a 4 Ω resistor in series (total resistance = 6 Ω). Using Ohm's relation I = V ÷ R_total, what electric current in amperes (A) flows through the loop?",
        "في مخطط الدائرة على التوالي، تدفع بطارية 12 فولت تياراً عبر مقاومتين قيمتاهما 2 أوم و4 أوم (المقاومة الكلية = 6 أوم). باستخدام علاقة أوم (التيار = الجهد ÷ المقاومة الكلية)، كم أمبيراً (A) يمر في الدائرة؟",
        2, [3, 6, 18],
        "First add series resistors: R_total = 2 + 4 = 6 Ω. Then compute I = 12 V ÷ 6 Ω!",
        "اجمع المقاومتين على التوالي أولاً: 2 + 4 = 6 أوم، ثم اقسم 12 فولت ÷ 6 أوم!",
        "Series current equals battery voltage divided by summed series resistance.",
        ["Total resistance R = 2 + 4 = 6 Ω.", "Current I = V ÷ R = 12 ÷ 6 = 2 A throughout the entire loop."],
        "2 A × 6 Ω = 12 V.",
        "في التوصيل على التوالي نجمع المقاومات ثم نقسم الجهد الكلي على المجموع.",
        ["المقاومة الكلية = 2 + 4 = 6 أوم.", "شدة التيار = 12 ÷ 6 = 2 أمبير في كل أجزاء الحلقة."],
        "تحقق: 2 × (2 + 4) = 12 فولت.",
        "",
        _ohm_svgs(12, [2, 4], "series", "Ohm Series Check", "حساب التيار بالتوالي")[0],
        _ohm_svgs(12, [2, 4], "series", "Ohm Series Check", "حساب التيار بالتوالي")[1],
    )

    hard_b18 = [
        (
            "After rubbing a rubber balloon briskly on a wool sweater, the balloon sticks to a wall without any wires or batteries. How does STATIC electricity in that balloon differ fundamentally from CURRENT electricity in a classroom lamp?",
            "بعد دلك بالون مطاطي بسترة صوفية، التصق البالون بالجدار دون أسلاك أو بطاريات. كيف تختلف الكهرباء الساكنة في البالون جذرياً عن الكهرباء المتحركة (التيار) في مصباح الصف؟",
            [
                ("Static electricity is an imbalance of stationary surface charges built up by friction, whereas current electricity is a continuous flow of charges around a closed loop", "الكهرباء الساكنة شحنات متجمعة مستقرة على السطح بفعل الاحتكاك، بينما التيار الكهربائي تدفق مستمر للشحنات في مسار مغلق"),
                ("Static electricity contains protons moving at 100 km/h through air, while lamps use zero electrons", "تتحرك البروتونات في الساكنة عبر الهواء والمصباح بلا إلكترونات"),
                ("Static charges stay inside copper metals forever without ever discharging", "تبقى الشحنات الساكنة داخل النحاس للأبد دون تفريغ"),
                ("Current electricity comes strictly from rubbing plastic combs in dry winters", "يأتي التيار الكهربائي من دلك الأمشاط البلاستيكية في الشتاء"),
            ],
            "Static = 'staying put' charges on insulators; Current = steadily flowing charges in closed conductors!",
            "الساكنة = شحنات متراكمة في موضعها على العوازل؛ والتيار = سيل مستمر من الشحنات في الموصلات المغلقة!",
            "Static electricity stores localized surface charges; current electricity flows continuously.",
            ["Rubbing transfers electrons from wool onto rubber, leaving a stationary negative static charge.", "A power grid or battery pushes electrons continuously around a closed circuit to run bulbs and motors."],
            "A sudden static spark or lightning bolt is just a brief discharge, not sustained current.",
            "الكهرباء الساكنة شحنات محلية متراكمة، والتيار حركة متواصلة للشحنات.",
            ["دلك البالون بالصوف ينقل إلكترونات تبقى ساكنة على سطح البالون المطاطي العازل.", "أما تيار المصباح فحركة متصلة للشحنات عبر الأسلاك المغلقة بفضل الجهد."],
            "الصدمة الساكنة الخفيفة عند لمس مقبض الباب تفريغ لحظي لتلك الشحنات.",
            None, None,
        ),
        (
            "A mystery circuit board has three bulbs (A, B, and C) behind a wooden cover with only the bulbs visible. When a student unscrews Bulb A, Bulb B ALSO goes out immediately, while Bulb C stays brightly lit. When A is screwed back in and Bulb C is unscrewed, BOTH A and B stay lit. Which wiring layout matches all observations?",
            "تحتوي لوحة كهربائية مغطاة على ثلاثة مصابيح ظاهرة (A و B و C). عندما فكّت طالبة المصباح A، انطفأ المصباح B فوراً مع بقاء المصباح C مضيئاً؛ وعندما أعادت A وفكّت المصباح C بقي كلٌّ من A و B مضيئين. أي توصيل يطابق هذه المشاهدات بدقة؟",
            [
                ("Bulbs A and B are wired in SERIES with each other on one branch, which is wired in PARALLEL with Bulb C", "المصباحان A و B موصولان معاً على التوالي في فرع واحد، وهذا الفرع موصول على التوازي مع المصباح C"),
                ("All three bulbs (A, B, and C) are wired in a single series line", "جميع المصابيح الثلاثة موصولة في مسار توالٍ واحد"),
                ("All three bulbs (A, B, and C) are wired in three completely separate parallel branches", "جميع المصابيح الثلاثة في ثلاثة فروع متوازية منفصلة تماماً"),
                ("Bulbs B and C are in series while A is disconnected completely", "المصباحان B و C على التوالي والمصباح A غير موصول"),
            ],
            "If unscrewing A kills B → A and B share ONE path (series)! If C works completely independently → C sits on a separate parallel branch!",
            "تعطّل A أطفأ B ← إذن A و B في مسار توالٍ واحد! وبقاء C مستقلاً ← إذن C في فرع متوازٍ منفصل!",
            "Series sub-branches fail together while parallel branches remain independent.",
            ["Unscrewing A opens the path shared with B → A and B are in series.", "C is unaffected by A/B, and A/B are unaffected by C → Branch(A+B) is parallel to Branch(C)."],
            "Hybrid series-parallel logic solves every circuit deduction puzzle!",
            "نستنتج التوصيل من اعتمادية المصابيح على بعضها عند فك أحدها.",
            ["بما أن فك A أطفأ B، فهما على مسار توالٍ مشترك.", "وبما أن C لم يتأثر بفك A وأن A و B لم يتأثرا بفك C، فالفرعان (A+B) و(C) متوازيان."],
            "الدوائر المركبة تجمع خصائص التوالي والتوازي معاً.",
            svg_data_table(["Unscrewed", "A", "B", "C"], [["Bulb A", "Off", "Off", "ON"], ["Bulb C", "ON", "ON", "Off"]], "Mystery Board Tests", [88, 72, 72, 72]),
            svg_data_table(["المفكوك", "A", "B", "C"], [["المصباح A", "مطفأ", "مطفأ", "مضيء"], ["المصباح C", "مضيء", "مضيء", "مطفأ"]], "اختبار اللوحة المغطاة", [88, 72, 72, 72]),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b18:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)



# ==============================================================================
# TOPIC 4 — Earth & Space Sciences (B19..B24, 90 Qs)
# ==============================================================================

def _add_b19(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B19"

    # Easy (0..4): Earth internal layers + Mohs scale basics
    easy_b19 = [
        (
            "In the cross-section of Earth's interior, which outermost, thinnest solid rock layer supports all continents and ocean basins?",
            "في المقطع العرضي لباطن الأرض، ما الطبقة الصخرية الخارجية الأرق التي ترتكز عليها القارات وقيعان المحيطات؟",
            [
                ("Crust", "القشرة الأرضية"),
                ("Mantle", "الوشاح"),
                ("Outer Core", "اللب الخارجي"),
                ("Inner Core", "اللب الداخلي"),
            ],
            "It is the thin brittle skin on the very outside of Earth.",
            "هي الطبقة الرقيقة الهشة على السطح الخارجي للأرض.",
            "Earth is layered by composition and density from surface to center.",
            ["Crust is the thin rocky surface layer (5 to 70 km thick).", "Mantle, outer core, and inner core lie progressively deeper beneath it."],
            "All rocks we quarry and walk on belong to Earth's crust.",
            "تتدرج طبقات الأرض من الخارج إلى المركز تبعاً للتركيب والكثافة.",
            ["القشرة الأرضية هي الطبقة الصخرية السطحية الأرق سمكاً (من 5 إلى 70 كم تقريباً).", "يليها إلى الداخل الوشاح ثم اللب الخارجي فالدّاخلي."],
            "كل القارات والبحار تقع فوق القشرة الأرضية.",
            *_earth_svgs("Crust", "Earth Interior Layers", "طبقات الأرض الداخلية"),
        ),
        (
            "Which thick Earth layer lies directly below the crust and circulates slowly by thermal convection, driving lithospheric plate motion?",
            "ما الطبقة السميكة التي تقع أسفل القشرة مباشرة وتدور فيها تيارات الحمل الحراري البطيئة المحرّكة للصفائح الأرضية؟",
            [
                ("Mantle", "الوشاح (الستار)"),
                ("Inner Core", "اللب الداخلي"),
                ("Crust", "القشرة الأرضية"),
                ("Outer Core", "اللب الخارجي"),
            ],
            "Think of the thickest middle layer making up over 80% of Earth's volume.",
            "تذكّر الطبقة الوسطى الأسمك التي تشكّل معظم حجم الأرض.",
            "Thermal convection in the upper mantle moves tectonic plates at centimeters per year.",
            ["Hot rock rises toward the base of the crust, spreads sideways, cools, and sinks.", "This slow flow in the mantle drags tectonic plates across Earth's surface."],
            "Mantle = thick middle layer driving plate movement.",
            "تحرّك تيارات الحمل في الوشاح الصفائح التكتونية ببطء مستمر.",
            ["ترتفع الصخور الساخنة في الوشاح للأعلى ثم تبرد وتهبط دافعةً الصفائح فوقها.", "يشكّل الوشاح الطبقة الوسطى الأضخم حجماً تحت القشرة."],
            "الوشاح هو المحرّك الرئيسي لحركة الصفائح.",
            *_earth_svgs("Mantle", "Convecting Middle Layer", "الطبقة الوسطى ذات تيارات الحمل"),
        ),
        (
            "Which layer of Earth's interior is composed of molten liquid iron and nickel and generates Earth's protective magnetic field?",
            "أي طبقة من طبقات الأرض تتكون من الحديد والنيكل في حالة سائلة منصهرة وتولّد المجال المغناطيسي الواقي للأرض؟",
            [
                ("Outer Core", "اللب الخارجي"),
                ("Crust", "القشرة الأرضية"),
                ("Inner Core", "اللب الداخلي"),
                ("Upper Mantle", "الوشاح العلوي"),
            ],
            "Electric currents swirl through this LIQUID metal shell around the solid center.",
            "تتحرك تيارات كهربائية في هذا الغلاف المعدني السائل المحيط بالمركز الصلب.",
            "Earth's outer core is liquid metal whose swirling convection acts as a geodynamo.",
            ["Liquid iron and nickel conduct electricity and flow because of Earth's rotation and heat.", "The inner core is solid iron-nickel, while the outer core is liquid."],
            "Liquid metal layer = Outer Core.",
            "يتكوّن اللب الخارجي من معادن منصهرة سائلة تولّد المغناطيسية الأرضية.",
            ["حركة الحديد والنيكل السائلين في اللب الخارجي تولّد المجال المغناطيسي للأرض.", "اللب الداخلي صلب بينما اللب الخارجي هو الطبقة السائلة."],
            "المعدن السائل في باطن الأرض يقع في اللب الخارجي.",
            *_earth_svgs("Outer Core", "Liquid Metal Shell", "الغلاف المعدني السائل"),
        ),
        (
            "At the very center of Earth lies the Inner Core. In what physical state are the iron and nickel atoms there?",
            "في قلب الأرض تماماً يقع اللب الداخلي. في أي حالة فيزيائية توجد ذرات الحديد والنيكل هناك؟",
            [
                ("Solid", "صلبة"),
                ("Gaseous", "غازية"),
                ("Liquid", "سائلة"),
                ("Plasma vapor", "بخار بلازما"),
            ],
            "Immense crushing weight of all overlying layers packs the atoms tightly together!",
            "الضغط الهائل من وزن جميع الطبقات العليا يضغط الذرات ويرصّها معاً!",
            "Extreme pressure at Earth's center prevents iron and nickel from melting despite extreme heat.",
            ["Temperatures reach ~5,500 °C, but pressure exceeds 3 million atmospheres.", "High pressure forces atoms into a dense solid crystal lattice."],
            "Outer Core is liquid; Inner Core is solid.",
            "يمنع الضغط الهائل في مركز الأرض انصهار الحديد والنيكل رغم الحرارة الشديدة.",
            ["تصل الحرارة إلى نحو 5500 درجة مئوية، لكن الضغط يفوق ثلاثة ملايين ضغط جوي.", "يرصّ هذا الضغط الذرات معاً في حالة صلبة متماسكة."],
            "اللب الخارجي سائل، أما اللب الداخلي فصلب.",
            *_earth_svgs("Inner Core", "Deepest Central Layer", "أعمق طبقة في المركز"),
        ),
        (
            "On the 1-to-10 Mohs hardness scale used by geologists, which mineral pair correctly represents the softest (1) and hardest (10) common natural standards?",
            "على مقياس موهس لقساوة المعادن من 1 إلى 10، أي زوج يمثّل المعدن الألين (1) والأصلب (10) بالترتيب؟",
            [
                ("Talc (1) and Diamond (10)", "التلك (1) والألماس (10)"),
                ("Gypsum (1) and Quartz (10)", "الجبس (1) والكوارتز (10)"),
                ("Calcite (1) and Topaz (10)", "الكالسيت (1) والتوباز (10)"),
                ("Talc (1) and Corundum (10)", "التلك (1) والكورندوم (10)"),
            ],
            "Talcum powder comes from the softest mineral (1), and drill-tip diamond sits at the top (10).",
            "مسحوق التلك يُستخرج من ألين معدن (1)، والألماس الذي يقطع الصخور في القمة (10).",
            "Mohs scale ranks minerals from Talc (1) up to Diamond (10) by scratch resistance.",
            ["1 = Talc, 2 = Gypsum, 3 = Calcite, 4 = Fluorite, 5 = Apatite, 6 = Feldspar, 7 = Quartz, 8 = Topaz, 9 = Corundum, 10 = Diamond.", "Harder minerals scratch softer ones."],
            "1 = Talc, 10 = Diamond.",
            "يرتب مقياس موهس المعادن من التلك (1) إلى الألماس (10) حسب مقاومة الخدش.",
            ["يخدش المعدن الأعلى قساوةً المعدن الأقل قساوةً دائماً.", "التلك في المرتبة 1، والكوارتز 7، والألماس في المرتبة القصوى 10."],
            "الألين: التلك (1)، والأصلب: الألماس (10).",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b19:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Mohs table, Red Sea rift, Convergent, Transform, Streak vs Color
    med_b19 = [
        (
            "A geologist tests an unknown mineral sample X. Based on the scratch table shown, what is the Mohs hardness of Sample X?",
            "اختبرت جيولوجية عينة معدن مجهول X. بناءً على جدول الخدش الموضّح، كم تبلغ قساوة العينة X على مقياس موهس تقريباً؟",
            [
                ("About 5 (between Fluorite and Feldspar)", "نحو 5 (بين الفلوريت والفلسبار)"),
                ("About 2 (softer than a copper coin)", "نحو 2 (ألين من العملة النحاسية)"),
                ("About 8 (harder than quartz)", "نحو 8 (أصلب من الكوارتز)"),
                ("10 (equal to diamond)", "10 (تساوي قساوة الألماس)"),
            ],
            "A mineral is harder than what it scratches, and softer than what scratches it!",
            "المعدن أصلب من الشيء الذي يخدشه، وألين من الشيء الذي يترك فيه خدشاً!",
            "Bracket unknown Mohs hardness between the hardest object scratched and softest object that scratches it.",
            ["Sample X scratches Fluorite (4), so its hardness > 4.", "Feldspar (6) scratches Sample X, so its hardness < 6 → hardness is 5 (Apatite)."],
            "4 < 5 < 6 matches every test result in the table.",
            "نحصر قساوة المعدن بين أصلب معدن خدشه وألين معدن خدش العينة.",
            ["العينة X تخدش الفلوريت (4) ← فقساوتها أكبر من 4.", "والفلسبار (6) يخدش العينة X ← فقساوتها أقل من 6، أي نحو 5 (الأباتيت)."],
            "القيمة 5 تقع تماماً بين 4 و 6.",
            svg_data_table(["Test Object", "Mohs", "Result with X"], [["Fingernail", "2.5", "X scratches it"], ["Fluorite", "4.0", "X scratches it"], ["Feldspar", "6.0", "Scratches X"], ["Quartz", "7.0", "Scratches X"]], "Mohs Scratch Tests", [108, 66, 134]),
            svg_data_table(["أداة الاختبار", "موهس", "النتيجة مع X"], [["الظفر", "2.5", "X تخدشه"], ["الفلوريت", "4.0", "X تخدشه"], ["الفلسبار", "6.0", "يخدش X"], ["الكوارتز", "7.0", "يخدش X"]], "نتائج اختبار موهس للخدش", [108, 66, 134]),
        ),
        (
            "The Red Sea along Saudi Arabia's western coast is gradually widening each year as the Arabian Plate pulls away from the African Plate. What kind of tectonic boundary is this?",
            "يتسع البحر الأحمر غرب المملكة العربية السعودية تدريجياً كل عام مع ابتعاد الصفيحة العربية عن الصفيحة الأفريقية. ما نوع الحدّ الصفائحي هنا؟",
            [
                ("Divergent boundary", "حدّ تباعدي"),
                ("Convergent collision boundary", "حدّ تقاربي تصادمي"),
                ("Transform sliding boundary", "حدّ تحويلي (انزلاقي)"),
                ("Subduction trench boundary", "حدّ اندساس قاري"),
            ],
            "Two plates pulling APART (diverging) allow magma to rise and create new seafloor crust.",
            "ابتعاد الصفيحتين عن بعضهما (تباعد) يسمح بصعود الصهارة وتكوين قشرة محيطية جديدة.",
            "Divergent boundaries form rift valleys and widening oceans like the Red Sea.",
            ["As the Arabian and African plates separate, magma wells up along the central rift.", "This builds new oceanic crust and slowly widens the Red Sea."],
            "Pulling apart = Divergent boundary.",
            "تتكوّن الأخاديد والبحار المتسعة كالبحر الأحمر عند الحدود التباعدية.",
            ["تتباعد الصفيحة العربية عن الصفيحة الأفريقية، فتصعد الصهارة لتكوين قاع بحر جديد.", "التباعد يعني حركة الصفائح في اتجاهين متعاكسين مبتعدين."],
            "الابتعاد = حدّ تباعدي.",
            svg_process_flow(["Plates Part", "Magma Rises", "New Crust", "Sea Widens"], "Arabian & African Plates", "Red Sea Tectonic Rift"),
            svg_process_flow(["تبتعد الصفيحتان", "تصعد الصهارة", "قشرة جديدة", "يتسع البحر"], "الصفيحة العربية والأفريقية", "الأخدود التكتوني للبحر الأحمر"),
        ),
        (
            "Where two continental tectonic plates push directly toward each other and crumple upward without sinking deep into the mantle, what major landform typically builds up?",
            "عندما تندفع صفيحتان قاريتان نحو بعضهما وتتجعد الصخور وترتفع للأعلى دون أن تغوص إحداهما في الوشاح، أي تضاريس رئيسية تتكون غالباً؟",
            [
                ("Tall folded mountain ranges (like the Himalayas)", "سلاسل جبلية التوائية شاهقة (مثل جبال الهيمالايا)"),
                ("A widening mid-ocean rift valley", "صدع محيطي يتسع في قاع البحر"),
                ("A chain of desert sand dunes", "كثبان رملية صحراوية متنقلة"),
                ("A horizontal fault with no vertical uplift", "صدع أفقي دون أي ارتفاع عمودي"),
            ],
            "Think of two thick carpets colliding head-on: neither slides under, so both buckle upward!",
            "تخيل سجادتين سميكتين تصطدمان وجهاً لوجه: تتجعدان وترتفعان للأعلى!",
            "Continental-continental convergent boundaries buckle thick light crust into tall mountain belts.",
            ["Because continental granite crust is too buoyant to subduct easily, colliding edges thicken and fold upward.", "This produces towering folded mountains such as the Himalayas."],
            "Colliding continental plates crumple into mountain ranges.",
            "تؤدي الحدود التقاربية بين صفيحتين قاريتين إلى انثناء القشرة وبناء الجبال الشاهقة.",
            ["القشرة القارية خفيفة الكثافة فلا تغوص بسهولة في الوشاح.", "لذلك تنثني الحواف المتصادمة وترتفع مكونةً جبالاً التوائية ضخمة."],
            "تصادم القارات يبني السلاسل الجبلية.",
            None, None,
        ),
        (
            "At a transform boundary (such as California's San Andreas Fault), two plates grind horizontally past each other without pulling apart or colliding. Which hazard is most characteristic of transform boundaries?",
            "عند الحد التحويلي (الانزلاقي) تنزلق صفيحتان أفقياً بمحاذاة بعضهما دون تباعد أو تصادم مباشر. ما الظاهرة الأكثر تمييزاً لهذه الحدود؟",
            [
                ("Frequent strong earthquakes caused by stuck rock suddenly slipping", "زلازل قوية متكررة نتيجة انزلاق الصخور المحبوسة فجأة"),
                ("Continuous growth of giant shield volcanoes", "تشكّل مستمر لبراكين درعية عملاقة"),
                ("Rapid widening of a new ocean basin", "اتساع سريع لحوض محيطي جديد"),
                ("Creation of deep oceanic subduction trenches", "حفر خنادق محيطية شديدة العمق"),
            ],
            "Friction locks the jagged rock edges together until stress snaps them forward in an earthquake.",
            "الاحتكاك يثبّت حواف الصخور حتى يتراكم الإجهاد فتنزلق فجأة مسببةً زلزالاً.",
            "Transform boundaries conserve crust while generating major shallow earthquakes.",
            ["Unlike divergent rifts or subduction zones, little magma forms at pure transform faults.", "Built-up elastic strain releases suddenly as seismic waves (earthquakes)."],
            "Side-by-side grinding plates = transform earthquakes.",
            "الحدود التحويلية لا تبني قشرة ولا تدمرها، لكنها تسبب زلازل عنيفة.",
            ["تتشابك الصخور بالاحتكاك أثناء الانزلاق الجانبي فيتراكم الإجهاد.", "عند تحرره فجأة تنطلق موجات زلزالية قوية."],
            "الاحتكاك الجانبي يولد زلازل متكررة.",
            None, None,
        ),
        (
            "Two quartz specimens look pink and purple because of trace impurities, yet both leave a white powder mark on an unglazed porcelain tile. Why do mineralogists rely on STREAK more than outer color?",
            "يظهر معدنان من الكوارتز بألوان وردية وبنفسجية بسبب شوائب طفيفة، لكن كليهما يترك مسحوقاً أبيض على قطعة خزف غير مصقول. لماذا يعتمد العلماء على المخدش أكثر من اللون الظاهري؟",
            [
                ("Tiny trace impurities often change surface color, whereas powdered streak stays consistent for a mineral", "الشوائب القليلة تغير اللون الخارجي كثيراً، بينما يظل لون مسحوق المخدش ثابتاً للمعدن الواحد"),
                ("Streak measures the exact density in grams per cubic centimeter", "المخدش يقيس الكثافة بدقة بوحدة جم/سم³"),
                ("Only metallic minerals have any outer surface color", "المعادن الفلزية وحدها لها لون سطحي خارجي"),
                ("Streak tells whether a mineral formed from magma or wind erosion", "المخدش يحدد إن كان المعدن تكوّن من الصهارة أم من الرياح"),
            ],
            "Pyrite ('fool's gold') looks brass-yellow on the outside like gold, yet its streak is greenish-black instead of yellow!",
            "البيريت (الذهب الكاذب) يشبه الذهب في لونه الخارجي الأصفر، لكن مخدشه أسود مخضر وليس أصفر!",
            "Streak (powder color) eliminates misleading lighting and trace-impurity surface tint.",
            ["Amethyst, rose quartz, and smoky quartz share identical white streaks because all are SiO2.", "Surface color alone frequently misleads field identification."],
            "Consistent mineral powder color = Streak.",
            "لون المسحوق (المخدش) أدق في تمييز المعادن من اللون الخارجي المتأثر بالشوائب.",
            ["أنواع الكوارتز المختلفة الألوان تعطي جميعها مخدشاً أبيض لأنها نفس المعدن.", "كما يفرّق المخدش بسهولة بين الذهب الحقيقي والبيريت."],
            "المخدش صفة تشخيصية أكثر ثباتاً من اللون السطحي.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b19:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Mohs ranking puzzle, S-waves/liquid outer core, Inner core pressure paradox, seafloor spreading ages, field ID reasoning
    hard_b19 = [
        (
            "Four minerals (P, Q, R, and S) are tested against one another as shown in the table. Which order ranks them correctly from SOFTEST to HARDEST?",
            "اختُبرت أربعة معادن (P و Q و R و S) بخدش بعضها كما في الجدول. أي ترتيب يضعها صحيحاً من الألين إلى الأصلب؟",
            [
                ("R, P, Q, S", "R ثم P ثم Q ثم S"),
                ("P, R, S, Q", "P ثم R ثم S ثم Q"),
                ("S, Q, P, R", "S ثم Q ثم P ثم R"),
                ("Q, P, R, S", "Q ثم P ثم R ثم S"),
            ],
            "Count how many minerals each sample scratches, or build the inequality chain step by step!",
            "رتّب السلسلة خطوة بخطوة: إذا خدش X المعدن Y فإن X > Y.",
            "Transitive scratch comparisons uniquely order Mohs hardness from lowest to highest.",
            ["Q scratches P and R → Q > P and Q > R.", "S scratches Q → S > Q (so S is hardest).", "P scratches R → P > R (so R is softest): R < P < Q < S."],
            "Check: S(4) > Q(3) > P(2) > R(1) fits every row!",
            "تحويل نتائج الخدش إلى متباينات يحدد الترتيب الدقيق للقساوة.",
            ["Q يخدش P و R ← إذن Q أصلب منهما.", "S يخدش Q ← إذن S هو الأصلب، وبما أن P يخدش R فإن R هو الألين: R < P < Q < S."],
            "التحقق من كل سطر يؤكد الترتيب من الألين إلى الأصلب.",
            svg_data_table(["Comparison Pair", "Observation"], [["Q vs P", "Q scratches P"], ["Q vs R", "Q scratches R"], ["S vs Q", "S scratches Q"], ["P vs R", "P scratches R"]], "Mineral Scratch Trials", [144, 160]),
            svg_data_table(["المقارنة", "الملاحظة"], [["Q مع P", "Q يخدش P"], ["Q مع R", "Q يخدش R"], ["S مع Q", "S يخدش Q"], ["P مع R", "P يخدش R"]], "تجارب خدش المعادن", [144, 160]),
        ),
        (
            "No drill has ever reached deeper than ~12 km into Earth, yet scientists know the Outer Core is liquid while the Mantle and Inner Core are solid. What direct evidence revealed that the Outer Core is liquid?",
            "لم يصل أي حفر أعمق من نحو 12 كم داخل الأرض، ومع ذلك يتيقّن العلماء أن اللب الخارجي سائل بينما الوشاح واللب الداخلي صلبان. ما الدليل المباشر الذي كشف سيولة اللب الخارجي؟",
            [
                ("Transverse earthquake waves (S-waves), which cannot travel through liquids, vanish when reaching the Outer Core", "الموجات الزلزالية المستعرضة (S) التي لا تمر عبر السوائل تختفي عند وصولها إلى اللب الخارجي"),
                ("Volcanoes erupt liquid iron metal straight up from the outer core", "البراكين تقذف حديداً سائلاً من اللب الخارجي مباشرة للسطح"),
                ("Ocean currents sink vertically 3,000 km into the outer core", "تيارات المحيطات تغوص عمودياً 3000 كم نحو اللب الخارجي"),
                ("Astronauts photographed the glowing outer core from space", "صوّر رواد الفضاء اللب الخارجي المتوهج من الفضاء"),
            ],
            "Think about seismic waves from major earthquakes passing through the planet to distant seismographs.",
            "فكر في الموجات الزلزالية المنطلقة من الزلازل الكبيرة عبر باطن الأرض إلى أجهزة الرصد البعيدة.",
            "Seismic wave behavior reveals phase state: S-waves require shear stiffness (solids only) and stop in liquids.",
            ["P-waves travel through both solids and liquids (refracting at boundaries).", "S-waves travel only through solids, creating an S-wave shadow zone opposite Earth from an earthquake due to the liquid outer core."],
            "S-wave blockage proves the Outer Core is liquid.",
            "تحليل الموجات الزلزالية يكشف الحالة الفيزيائية لطبقات الأرض العميقة.",
            ["تنتقل الموجات الأولية P في الصلب والسائل، أما الموجات الثانوية S فتمر في الأجسام الصلبة فقط.", "اختفاء الموجات S في المنطقة المقابلة للزلزال يثبت وجود نطاق سائل هو اللب الخارجي."],
            "توقف الموجات المستعرضة S دليل قاطع على سيولة اللب الخارجي.",
            None, None,
        ),
        (
            "Pure iron melts at about 1,538 °C on Earth's surface, yet Earth's Inner Core is roughly 5,500 °C and remains completely SOLID. Which physical explanation resolves this apparent contradiction?",
            "ينصهر الحديد النقي عند 1538 درجة مئوية تقريباً على سطح الأرض، لكن حرارة اللب الداخلي تبلغ نحو 5500 درجة مئوية ومع ذلك يبقى صلباً تماماً. ما التفسير الفيزيائي لهذا؟",
            [
                ("Colossal pressure at Earth's center squeezes iron atoms together so tightly that melting requires an even higher temperature", "الضغط الهائل في مركز الأرض يضغط ذرات الحديد بقوة فتحتاج إلى حرارة أعلى بكثير لتنصهر"),
                ("The inner core is cooled continuously by groundwater seeping down from oceans", "تبرد المياه الجوفية المتسربة من المحيطات اللب الداخلي باستمرار"),
                ("Iron mixed with helium gas loses all ability to melt at any temperature", "اختلاط الحديد بغاز الهيليوم يفقده القدرة على الانصهار"),
                ("High gravity turns solid iron into hollow foam crystals", "الجاذبية العالية تحول الحديد الصلب إلى بلورات جوفاء"),
            ],
            "Melting happens when thermal vibration breaks atoms free; squeezing atoms from outside raises the melting point!",
            "الانصهار يعني تحرر الذرات بالاهتزاز، لكن الضغط الخارجي الشديد يقيدها ويرفع درجة الانصهار!",
            "Increasing pressure elevates the melting temperature of iron above the actual core temperature.",
            ["Under 3.6 million atmospheres of pressure, iron's melting point jumps well past 6,000 °C.", "Because 5,500 °C < compressed melting point, the inner core stays solid."],
            "Pressure beats heat in the Inner Core.",
            "يرفع الضغط الهائل درجة انصهار الحديد إلى أعلى من حرارة اللب الداخلي نفسها.",
            ["الضغط في المركز يتجاوز 3.6 مليون ضغط جوي مما يرفع نقطة انصهار الحديد فوق 6000 °م.", "لذا يبقى اللب الداخلي صلباً رغم تجاوز حرارته 5500 °م."],
            "الضغط الساحق يغلب الحرارة في اللب الداخلي.",
            None, None,
        ),
        (
            "Scientists drilled basalt cores at four distances east of an active mid-ocean divergent ridge and plotted their ages in the table. Which core proves the seafloor is spreading outward from the ridge?",
            "استخرج العلماء عينات بازلت على أربع مسافات شرق أخدود وسطي محيطي متباعد وقاسوا أعمارها في الجدول. كيف تثبت هذه الأعمار أن قاع المحيط يتمدد مبتعداً عن الأخدود؟",
            [
                ("Age increases steadily with distance from the ridge (Core A is youngest at 0.4 Myr; Core D is oldest at 18.0 Myr)", "يزداد عمر الصخور بانتظام كلما ابتعدنا عن الأخدود (العينة A أحدث عند 0.4 مليون سنة، والعينة D أقدم عند 18 مليون سنة)"),
                ("All four cores have the exact same age, showing crust never moves", "للعينات الأربع العمر نفسه، مما يثبت ثبات القاع"),
                ("Core D closest to the coast is youngest, showing magma enters at beaches", "العينة D الأقرب للساحل هي الأحدث، مما يعني خروج الصهارة من الشواطئ"),
                ("Magnetic stripes disappear completely past 10 km", "الأشرطة المغناطيسية تختفي تماماً بعد مسافة 10 كم"),
            ],
            "Look down the 'Rock Age' column as distance grows from 5 km to 220 km!",
            "تتبع عمود (عمر الصخر) مع ازدياد المسافة من 5 كم إلى 220 كم!",
            "Seafloor spreading forms brand-new basalt at the ridge crest and pushes older crust outward.",
            ["At 5 km (Core A) rock is only 0.4 million years old.", "At 220 km (Core D) rock has traveled outward for 18.0 million years."],
            "Youngest at ridge crest, progressively older away = seafloor spreading!",
            "تبرد الصهارة الجديدة عند الأخدود وتندفع الصخور الأقدم نحو الخارج بمرور الزمن.",
            ["الصخور القريبة من الأخدود (5 كم) عمرها 0.4 مليون سنة فقط، والبعيدة (220 كم) عمرها 18 مليون سنة.", "التدرج المنتظم في العمر يثبت تمدد قاع المحيط."],
            "الأحدث عند الأخدود والأقدم بعيداً عنه = دليل تمدد القاع.",
            svg_data_table(["Core", "From Ridge", "Basalt Age"], [["A", "5 km", "0.4 Myr"], ["B", "40 km", "3.3 Myr"], ["C", "110 km", "9.0 Myr"], ["D", "220 km", "18.0 Myr"]], "Ocean Crust Core Ages", [76, 114, 118]),
            svg_data_table(["العينة", "البعد عن الأخدود", "عمر البازلت"], [["A", "5 كم", "0.4 م.س"], ["B", "40 كم", "3.3 م.س"], ["C", "110 كم", "9.0 م.س"], ["D", "220 كم", "18.0 م.س"]], "أعمار صخور قاع المحيط", [72, 126, 112]),
        ),
        (
            "A student receives a pale glassy rock specimen in the field. It scratches a steel knife blade (5.5) and window glass (5.5), cannot be scratched by a quartz crystal (7.0) WAIT—it IS scratched by quartz (7.0) and shows curved shell-like fractures rather than flat cleavage planes. What additional test best confirms whether it is Orthoclase Feldspar (6) versus Apatite (5)?",
            "حصل طالب على عينة معدن فاتح اللون في رحلة ميدانية؛ خدش المعدن نصل سكين فولاذي (5.5) ولوح زجاج (5.5)، لكنه انخدش ببلورة كوارتز (7.0) وأظهر مكسراً منحنياً. أي اختبار إضافي يحسم بدقة إن كان فلسباراً (6) أم أباتيتاً (5)؟",
            [
                ("Test whether the unknown mineral scratches an Orthoclase Feldspar (6) reference crystal or only scratches glass (5.5) — wait: Apatite (5) CANNOT scratch glass (5.5), so having already scratched glass (5.5) proves hardness > 5.5, matching Orthoclase (6)!", "بما أن العينة خدشت الزجاج (5.5) فهذا وحده يثبت أن قساوتها أكبر من 5.5، ما يستبعد الأباتيت (5) ويرجح الفلسبار (6)؛ ويفصل اختبار الخدش المتبادل مع عينة فلسبار قياسية نهائياً!"),
                ("Weigh the rock in air alone without measuring volume", "وزن الصخرة في الهواء فقط دون قياس الحجم"),
                ("Hold the rock in sunlight for 10 seconds to test its smell", "تعريض الصخرة للشمس عشر ثوانٍ لاختبار رائحتها"),
                ("Mix it with pure distilled water to see if it floats like ice", "وضعها في ماء مقطر لمعرفة هل تطفو كالثلج"),
            ],
            "Compare the mineral's glass test (5.5) against Apatite's Mohs value of 5!",
            "قارن نتيجة خدش الزجاج (5.5) بقساوة الأباتيت التي تساوي 5 فقط!",
            "Reference hardness benchmarks (fingernail 2.5, penny 3.5, glass 5.5, quartz 7) bracket unknown minerals accurately.",
            ["Apatite has Mohs hardness 5.0, so it fails to scratch glass (5.5).", "Scratching glass (5.5) while failing against quartz (7.0) places hardness in (5.5, 7.0), matching Orthoclase (6), and mutual scratching with a known Feldspar checks exact equality."],
            "Scratching glass (5.5) already rules out hardness 5 (Apatite).",
            "المعايير المرجعية كالزجاج (5.5) والكوارتز (7) تحصر القساوة بدقة.",
            ["قساوة الأباتيت 5 فقط لذا لا يستطيع خدش الزجاج (5.5).", "نجاح العينة في خدش الزجاج وفشلها أمام الكوارتز يضعها فوق 5.5 (كالفلسبار 6)."],
            "خدش الزجاج يستبعد الأباتيت (5) فوراً.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b19:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b20(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B20"

    # Easy (0..4): Igneous, Sedimentary, Metamorphic, Weathering->Erosion->Deposition, Desert wind erosion
    easy_b20 = [
        (
            "Which rock group forms when molten magma beneath the ground or hot lava at the surface cools and hardens into solid rock?",
            "أي نوع من الصخور يتكون عندما تبرد الصهارة في باطن الأرض أو الحمم على السطح وتتصلّب؟",
            [
                ("Igneous rocks", "الصخور النارية"),
                ("Sedimentary rocks", "الصخور الرسوبية"),
                ("Metamorphic rocks", "الصخور المتحولة"),
                ("Evaporite soils", "التربة المتبخرة"),
            ],
            "Think of fire ('ignis' = fire): melted magma/lava cooling down!",
            "صهارة وحمم ملتهبة تبرد وتتجمد = صخور نارية!",
            "Igneous rocks crystallize directly from molten magma or lava.",
            ["Slow cooling underground forms intrusive granite; fast cooling at surface forms basalt or obsidian.", "Sedimentary comes from compacted fragments; metamorphic from heat+pressure without full melting."],
            "Molten magma/lava cooling = Igneous rock.",
            "تتكون الصخور النارية مباشرة من تبريد وتصلّب الصهارة أو اللابة المنصهرة.",
            ["التبريد البطيء في الباطن يكوّن الجرانيت، والسريع على السطح يكوّن البازلت.", "لا تتكون من طبقات رسوبية ولا من ضغط دون انصهار."],
            "تبريد الصهارة = صخر ناري.",
            None, None,
        ),
        (
            "Which main rock type builds up from layers of sand, silt, or shell fragments that get squeezed (compacted) and glued (cemented) together, and most commonly preserves fossils?",
            "أي نوع رئيسي من الصخور يتكون من تراكم طبقات الرمل أو الطمي أو الأصداف ثم انضغاطها وتلاحمها معاً، ويحفظ الأحافير غالباً؟",
            [
                ("Sedimentary rocks", "الصخور الرسوبية"),
                ("Igneous rocks", "الصخور النارية"),
                ("Metamorphic rocks", "الصخور المتحولة"),
                ("Basaltic lava rocks", "صخور اللابة البازلتية"),
            ],
            "Sediments settle in layers gently enough to bury shells and bones without melting them!",
            "تستقر الرسوبيات في طبقات هادئة تدفن الأصداف دون أن تصهرها!",
            "Compaction and cementation of sediments create sedimentary rocks where fossils survive.",
            ["Gentle deposition in seas, rivers, or deserts buries organic remains in layers.", "Dissolved minerals cement grains into limestone, sandstone, or shale."],
            "Layers + cementing + fossils = Sedimentary rock.",
            "تترسب الفتاتات في طبقات متتالية ثم تتماسك بالضغط والتلاحم لتكوّن صخوراً رسوبية.",
            ["الترسيب الهادئ في البحار والأنهار يسمح بحفظ بقايا الكائنات كأحافير.", "على عكس الحرارة الصاهرة التي تدمر الأحافير في الصخور النارية."],
            "طبقات + تلاحم + أحافير = صخور رسوبية.",
            None, None,
        ),
        (
            "Deep underground, intense heat and crushing pressure reshape existing limestone or shale into harder marble or slate WITHOUT completely melting the rock. What type of rock forms?",
            "في أعماق الأرض، تغير الحرارة العالية والضغط الهائل الحجر الجيري أو الطيني إلى رخام أو أردواز أصلب دون أن ينصهر الصخر تماماً. ما نوع الصخر المتكوّن؟",
            [
                ("Metamorphic rock", "الصخر المتحول"),
                ("Igneous rock", "الصخر الناري"),
                ("Sedimentary rock", "الصخر الرسوبى"),
                ("Loose alluvial sand", "رمل نهري مفكك"),
            ],
            "Morph means 'change form' — transformed solid rock!",
            "تغيّر الصخر في الباطن دون انصهار كامل يعني صخراً متحولاً!",
            "Metamorphic rocks form when heat, pressure, or hot fluids recrystallize solid rock without melting.",
            ["If the rock melted fully first, cooling would create an igneous rock instead.", "Staying solid under heat + pressure creates metamorphic rocks like marble and gneiss."],
            "Heat + Pressure (no melting) = Metamorphic.",
            "تنشأ الصخور المتحولة عند تغيّر صخر قديم بالحرارة والضغط دون بلوغ الانصهار الكامل.",
            ["لو انصهر الصخر كلياً لأصبح صهارتُه عند التبريد صخراً نارياً لا متحولاً.", "الحجر الجيري يتحول إلى رخام، والطفل يتحول إلى أردواز."],
            "حرارة + ضغط دون انصهار = صخر متحول.",
            None, None,
        ),
        (
            "Follow the four-step surface sequence shown in the diagram. Which process specifically means the TRANSPORT (movement) of broken rock bits from place to place by wind, water, or ice?",
            "تتبع التسلسل الرباعي على سطح الأرض في المخطط. أي عملية تعني تحديداً نقل فتات الصخور من مكان لآخر بفعل الرياح أو الماء أو الجليد؟",
            [
                ("Erosion", "التعرية"),
                ("Weathering", "التجوية"),
                ("Deposition", "الترسيب"),
                ("Cementation", "التلاحم"),
            ],
            "Weathering BREAKS rock in place; Erosion MOVES it away; Deposition DROPS it!",
            "التجوية تفتّت في المكان؛ التعرية تنقل الفتات؛ الترسيب يُلقي الفتات!",
            "Surface shaping separates into breaking (weathering), transport (erosion), and settling (deposition).",
            ["Step 1 (Weathering) cracks rock without moving it far.", "Step 2 (Erosion) carries loose fragments away via rivers, wind, or glaciers; Step 3 (Deposition) drops them."],
            "Moving sediment = Erosion.",
            "تتكامل عمليات تشكيل السطح: التجوية ثم التعرية ثم الترسيب.",
            ["التجوية تفتت الصخر في موضعه، ثم تأتي التعرية لتنقله بالماء أو الرياح أو الجليد.", "وعندما تتوقف حركة العامل الناقل يحدث الترسيب."],
            "النقل = التعرية.",
            svg_process_flow(["1. Weathering", "2. Erosion", "3. Deposition", "4. Cementation"], "Breaking → Moving → Settling → Rock", "Sediment Shaping Sequence"),
            svg_process_flow(["1. التجوية", "2. التعرية", "3. الترسيب", "4. التلاحم"], "تفتيت ← نقل ← استقرار ← صخر", "تسلسل تشكيل الصخور السطحية"),
        ),
        (
            "In Saudi Arabia's Rub' al Khali (Empty Quarter), crescent-shaped barchan sand dunes slowly march across desert plains. Which natural agent drives both the movement and sculpting of these dunes?",
            "في صحراء الربع الخالي بالمملكة، تتحرك الكثبان الرملية الهلالية ببطء عبر السهول الصحراوية. ما العامل الطبيعي الذي يحرّك هذه الكثبان وينحت شكلها؟",
            [
                ("Wind erosion and deposition", "تعرية الرياح وترسيبها"),
                ("Moving valley glaciers", "زحف الأنهار الجليدية"),
                ("Deep ocean tidal currents", "تيارات المدّ البحري العميقة"),
                ("Subsurface volcanic lava tubes", "أنابيب اللابة البركانية الباطنية"),
            ],
            "No ice or sea covers the Empty Quarter — gusts lift fine sand grains up one slope and drop them down the other!",
            "لا جليد ولا محيط في الربع الخالي؛ الهبات الهوائية ترفع حبات الرمل وتسقطها في الجهة المقابلة!",
            "Wind acts as a major agent of arid-region erosion and dune deposition.",
            ["Wind lifts sand grains in short hops (saltation) up the windward slope.", "When wind drops speed past the crest, sand deposits on the slip face, advancing the dune."],
            "Desert sand dunes are shaped by wind.",
            "تؤدي الرياح دوراً أساسياً في التعرية والترسيب داخل البيئات الصحراوية الجافة.",
            ["تحمل الرياح حبيبات الرمل بالقفز صعوداً على الوجه المواجه للريح ثم ترسبها خلف القمة.", "هذا النقل والترسيب المستمر يحرك الكثبان الهلالية."],
            "الكثبان الصحراوية من عمل الرياح.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b20:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Intrusive vs Extrusive cooling table, Mech vs Chem weathering, Law of Superposition table, Dune wind direction, Soil humus
    med_b20 = [
        (
            "Examine the igneous rock table comparing Granite and Obsidian. Why does Granite grow large interlocking crystals whereas Obsidian turns smooth and glassy with no visible crystals?",
            "تأمّل جدول الصخور النارية الذي يقارن بين الجرانيت والأوبسيديان. لماذا ينمو في الجرانيت بلورات كبيرة متشابكة بينما يصبح الأوبسيديان زجاجياً أملس بلا بلورات مرئية؟",
            [
                ("Granite cooled slowly deep underground giving atoms plenty of time to lock into big crystals; Obsidian froze almost instantly at the surface", "تبرد صهارة الجرانيت ببطء شديد في باطن الأرض فتجد الذرات وقتاً لتكوين بلورات كبيرة، بينما تجمدت حمم الأوبسيديان فجأة على السطح"),
                ("Granite is actually a compacted sandstone whereas Obsidian is frozen ocean water", "الجرانيت حجر رملي متلاحم، والأوبسيديان مياه محيط متجمدة"),
                ("Underground rocks absorb sunlight through cracks to grow big crystals", "تمتص الصخور الباطنية ضوء الشمس عبر الشقوق لتنمو بلوراتها"),
                ("Granite contains air bubbles that turn into shiny quartz cubes", "يحتوي الجرانيت على فقاعات هوائية تتحول إلى مكعبات كوارتز لامعة"),
            ],
            "Compare 'Cooling Location' and 'Cooling Rate' in the table — crystal size tracks cooling duration!",
            "اربط بين مكان التبريد وسرعته: كلما طال وقت التبريد كبرت البلورات!",
            "Crystal size in igneous rocks reflects magma cooling rate.",
            ["Intrusive magma surrounded by warm rock cools over thousands of years → large visible crystals (Granite).", "Extrusive lava quenched by cold air or water cools in seconds/hours → glassy texture (Obsidian)."],
            "Slow cooling = large crystals; Fast cooling = tiny/no crystals.",
            "يتناسب حجم البلورات في الصخور النارية طردياً مع بطء التبريد.",
            ["التبريد البطيء داخل القشرة يمنح الذرات وقتاً كافياً للترتّب في بلورات واضحة كما في الجرانيت.", "التبريد المفاجئ للحمم على السطح يمنع نمو البلورات فيتكون نسيج زجاجي كالأوبسيديان."],
            "بطء التبريد = بلورات كبيرة؛ سرعة التبريد = نسيج زجاجي أو دقيق.",
            svg_data_table(["Igneous Rock", "Where Cooled", "Rate", "Texture"], [["Granite", "Deep crust", "Slow", "Large crystals"], ["Basalt", "Surface lava", "Fast", "Fine grains"], ["Obsidian", "Surface lava", "Instant", "Glassy"]], "Cooling Rate & Crystals", [88, 92, 66, 98]),
            svg_data_table(["الصخر الناري", "مكان التبريد", "السرعة", "النسيج"], [["الجرانيت", "باطن القشرة", "بطيء", "بلورات كبيرة"], ["البازلت", "حمم سطحية", "سريع", "حبيبات دقيقة"], ["الأوبسيديان", "حمم سطحية", "فوري", "زجاجي أملس"]], "سرعة التبريد وحجم البلورات", [88, 92, 66, 98]),
        ),
        (
            "Rainwater mixes with carbon dioxide in soil to form weak carbonic acid that dissolves underground limestone, carving vast caves like Saudi Arabia's Dahl Hit cavern. Which weathering process creates these caves?",
            "يذيب ماء المطر المختلط بثاني أكسيد الكربون الحجر الجيري تحت سطح الأرض تدريجياً ليحفر كهوفاً واسعة مثل كهف دحل هيت في المملكة. ما نوع التجوية هنا؟",
            [
                ("Chemical weathering (dissolution)", "التجوية الكيميائية (الإذابة)"),
                ("Physical ice wedging", "التجوية الفيزيائية بتمدد الجليد"),
                ("Wind abrasion only", "حتّ الرياح الميكانيكي فقط"),
                ("Tectonic folding uplift", "الرفع الجبلي الالتوائي"),
            ],
            "Does acid change the rock's chemical composition by dissolving minerals, or merely smash it mechanically?",
            "هل يغيّر الحمض التركيب الكيميائي للمعدن بإذابته، أم يفتته ميكانيكياً فقط؟",
            "Chemical weathering alters minerals through reactions such as acid dissolution or oxidation.",
            ["Carbonic acid reacts with calcium carbonate in limestone and carries dissolved ions away in groundwater.", "Mechanical weathering splits rock without altering mineral chemistry."],
            "Acid dissolving limestone = Chemical weathering.",
            "التجوية الكيميائية تغيّر التركيب المعدني للصخر كما يحدث عند ذوبان الحجر الجيري بالماء الحمضي.",
            ["يتفاعل حمض الكربونيك مع كربونات الكالسيوم في الحجر الجيري فيذيبه ويحفر الكهوف.", "التجوية الميكانيكية تكسر الصخر دون تغيير تركيبه الكيميائي."],
            "إذابة الحجر الجيري بحمض الكربونيك = تجوية كيميائية.",
            None, None,
        ),
        (
            "A canyon wall exposes four horizontal, undisturbed sedimentary rock layers stacked from top to bottom as listed in the table. According to the Law of Superposition, which rock layer is the OLDEST?",
            "يكشف جدار وادٍ عميق عن أربع طبقات رسوبية أفقية غير مضطربة مرتبة من الأعلى إلى الأسفل كما في الجدول. وفق مبدأ تعاقب الطبقات، أي طبقة هي الأقدم عمراً؟",
            [
                ("Conglomerate (Layer 4 at the bottom)", "الكونجلوميرات (الطبقة 4 في الأسفل)"),
                ("Shale (Layer 1 at the top)", "الطفل (الطبقة 1 في الأعلى)"),
                ("Limestone (Layer 2)", "الحجر الجيري (الطبقة 2)"),
                ("All four layers formed at the exact same minute", "تكوّنت الطبقات الأربع في اللحظة نفسها"),
            ],
            "Think of stacking newspapers day by day: Monday's paper lies under Tuesday's, and today's lies on top!",
            "تخيل تكديس الصحف يوماً بعد يوم: صحيفة أول يوم تكون في الأسفل تماماً وصحيفة اليوم في الأعلى!",
            "Law of Superposition: in undisturbed strata, deeper layers are older and upper layers are younger.",
            ["Sediment must deposit onto an existing surface below it.", "Therefore Layer 4 deposited first (oldest), then 3, then 2, and Layer 1 last (youngest)."],
            "Bottom undisturbed layer = Oldest.",
            "ينص مبدأ التعاقب الطبقي على أن الطبقة السفلى في التتابع غير المضطرب هي الأقدم.",
            ["لا يمكن أن تترسب طبقة جديدة إلا فوق سطح قديم موجود تحتها.", "إذن الطبقة 4 (الكونجلوميرات) ترسبت أولاً فهي الأقدم، والطبقة 1 هي الأحدث."],
            "الطبقة السفلى = الأقدم؛ الطبقة العليا = الأحدث.",
            svg_data_table(["Position", "Layer", "Rock Type"], [["Top", "Layer 1", "Shale"], ["Upper-Mid", "Layer 2", "Limestone"], ["Lower-Mid", "Layer 3", "Sandstone"], ["Bottom", "Layer 4", "Conglomerate"]], "Undisturbed Canyon Strata", [96, 86, 120]),
            svg_data_table(["الموضع", "الطبقة", "نوع الصخر"], [["الأعلى", "الطبقة 1", "صخر طيني"], ["الأوسط العلوي", "الطبقة 2", "حجر جيري"], ["الأوسط السفلي", "الطبقة 3", "حجر رملي"], ["الأسفل", "الطبقة 4", "كونجلوميرات"]], "طبقات الوادي المتعاقبة", [102, 82, 118]),
        ),
        (
            "A desert sand dune has a long, gentle slope on its western side and a short, steep slip face on its eastern side. Which direction is the prevailing wind blowing?",
            "لأحد الكثبان الرملية الصحراوية منحدر طويل لطيف الانحدار في جهته الغربية، ووجه قصير شديد الانحدار في جهته الشرقية. في أي اتجاه تهب الرياح السائدة؟",
            [
                ("From West to East", "من الغرب نحو الشرق"),
                ("From East to West", "من الشرق نحو الغرب"),
                ("Straight upward from underground", "عمودياً من باطن الأرض للأعلى"),
                ("From North to South only", "من الشمال إلى الجنوب فقط"),
            ],
            "Sand grains get pushed gently UP the windward ramp and avalanche down the steep sheltered slip face!",
            "تدفع الرياح الرمل صعوداً فوق المنحدر اللطيف ثم يسقط خلف القمة على الوجه الشديد الانحدار!",
            "Dune asymmetry records wind direction: wind blows up the gentle windward slope toward the steep slip face.",
            ["Gentle western slope = windward side facing incoming wind.", "Steep eastern slip face = sheltered leeward side where sand avalanches forward toward the east."],
            "Wind blows from gentle side → steep slip face (West → East).",
            "يكشف شكل الكثيب اتجاه الرياح: الوجه اللطيف يواجه الريح، والوجه شديد الانحدار في الجهة المعاكسة.",
            ["ترتقي حبات الرمل المنحدر الغربي اللطيف مدفوعةً بالرياح، ثم تتساقط على الحافة الشرقية الحادة.", "إذن الرياح تهب من الغرب متجهةً نحو الشرق."],
            "من المنحدر اللطيف نحو الحاد = من الغرب إلى الشرق.",
            None, None,
        ),
        (
            "A farmer compares dark, crumbly topsoil (Horizon A) from a river valley with pale, rocky subsoil beneath it (Horizon C). What dark organic material enriches Horizon A and helps hold moisture and nutrients for crops?",
            "يقارن مزارع بين تربة سطحية داكنة مفككة (النطاق A) من وادٍ نهري، وتربة تحتية فاتحة صخرية أسفلها (النطاق C). ما المادة العضوية الداكنة التي تغني النطاق A وتحتفظ بالماء والمغذيات؟",
            [
                ("Humus (decomposed plant and animal remains)", "الدُّبال (بقايا النباتات والحيوانات المتحللة)"),
                ("Unweathered solid granite bedrock", "صخر الأساس الجرانيتي غير المتجوي"),
                ("Pure crushed quartz table salt", "ملح الطعام المطحون النقي"),
                ("Molten volcanic ash droplets", "قطرات الرماد البركاني المنصهرة"),
            ],
            "Microorganisms and earthworms break down dead leaves and roots into rich dark soil nutrients.",
            "تحلل الكائنات الدقيقة أوراق الشجر والجذور الميتة إلى مادة داكنة خصبة.",
            "Humus provides topsoil's dark color, sponge-like water retention, and slow-release nutrients.",
            ["Decomposers convert organic litter into humus in Horizon A.", "Rocky Horizon C consists mostly of partially weathered parent rock with very little humus."],
            "Organic topsoil layer = Humus.",
            "الدُّبال مادة عضوية ناتجة عن تحلل بقايا المخلوقات الحية في التربة السطحية.",
            ["يرفع الدبال قدرة التربة على الاحتفاظ بالماء ويزود النباتات بالأملاح المعدنية اللازمة لنموها.", "النطاق C أفقر بالمواد العضوية وأكثر احتواءً على شظايا الصخر الأم."],
            "الدُّبال هو سر خصوبة النطاق السطحي الداكن.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b20:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Multi-step rock cycle, Cross-cutting magma dike puzzle, River delta sorting, Chemical surface area experiment, Tuwaiq marine fossils
    hard_b20 = [
        (
            "Trace the rock cycle path shown: Limestone (sedimentary) is buried deep beneath colliding continents, squeezed without melting into Marble, then subducted deeper until it melts completely into magma, and finally cools slowly underground. What final rock type forms at Step 4?",
            "تتبع مسار دورة الصخور في المخطط: يُدفن الحجر الجيري (رسوبي) تحت قارتين متصادمتين فينضغط دون انصهار متحولاً إلى رخام، ثم يندسّ أعمق فينصهر تماماً إلى صهارة، وأخيراً يبرد ببطء في باطن الأرض. ما نوع الصخر النهائي في الخطوة 4؟",
            [
                ("An intrusive igneous rock with large visible crystals", "صخر ناري جوفي ذو بلورات كبيرة واضحة"),
                ("A fossil-rich layered sedimentary rock", "صخر رسوبي طبقي غني بالأحافير"),
                ("A glassy extrusive lava rock with zero crystals", "صخر بركاني سطحي زجاجي بلا بلورات"),
                ("Uncompacted river silt and clay", "طمي نهري مفكك غير متماسك"),
            ],
            "Melting resets everything back to magma! Then check WHERE and HOW FAST the magma cools.",
            "الانصهار الكامل يعيد الصخر إلى صهارة! ثم تحقّق أين وبأي سرعة بردت الصهارة.",
            "Any rock melted completely into magma forms igneous rock on cooling; slow underground cooling yields coarse intrusive rock.",
            ["Marble (metamorphic) erased fossils and recrystallized, then complete melting destroyed all crystals.", "Slow cooling deep underground allows large crystals to grow → coarse intrusive igneous rock."],
            "Melt + slow underground cooling = coarse intrusive igneous rock.",
            "يمحو الانصهار الكامل البنية السابقة، ويتحدد الصخر الناتج بسرعة ومكان تبريد الصهارة.",
            ["بما أن الرخام انصهر تماماً فالناتج بعد التبريد صخر ناري حتماً.", "وبما أن التبريد كان بطيئاً في باطن الأرض تتشكل بلورات كبيرة واضحة (ناري جوفي)."],
            "انصهار + تبريد بطيء في الباطن = صخر ناري جوفي خشن.",
            svg_process_flow(["Limestone", "Heat & Pressure", "Full Melting", "Slow Deep Cool"], "Marble → Magma → ?", "Multi-Step Rock Cycle"),
            svg_process_flow(["حجر جيري", "حرارة وضغط", "انصهار كامل", "تبريد باطني بطيء"], "رخام ← صهارة ← ؟", "مسار متعدد الخطوات في دورة الصخور"),
        ),
        (
            "A rock cliff contains horizontal layers 4 (bottom), 3, 2, and 1 (top). A narrow vertical dike of dark igneous basalt cuts upward through Layers 4, 3, and 2, stopping cleanly right below Layer 1. Using cross-cutting relationships, what is the correct chronological order from OLDEST to NEWEST?",
            "يحتوي جرف صخري على طبقات أفقية من الأسفل للأعلى: 4 ثم 3 ثم 2 ثم 1. يقطع قاطع ناري عمودي من البازلت الطبقات 4 و 3 و 2 ويتوقف تماماً أسفل الطبقة 1 مباشرة. وفق مبدأ القاطع والمقطوع، ما الترتيب الزمني الصحيح من الأقدم إلى الأحدث؟",
            [
                ("Layer 4 → Layer 3 → Layer 2 → Basalt Dike → Layer 1", "الطبقة 4 ← الطبقة 3 ← الطبقة 2 ← القاطع البازلتي ← الطبقة 1"),
                ("Basalt Dike → Layer 4 → Layer 3 → Layer 2 → Layer 1", "القاطع البازلتي ← الطبقة 4 ← الطبقة 3 ← الطبقة 2 ← الطبقة 1"),
                ("Layer 1 → Layer 2 → Layer 3 → Layer 4 → Basalt Dike", "الطبقة 1 ← الطبقة 2 ← الطبقة 3 ← الطبقة 4 ← القاطع البازلتي"),
                ("Layer 4 → Layer 3 → Basalt Dike → Layer 2 → Layer 1", "الطبقة 4 ← الطبقة 3 ← القاطع البازلتي ← الطبقة 2 ← الطبقة 1"),
            ],
            "Whatever gets cut MUST already exist before the cutter! And whatever rests uncut on top came AFTER!",
            "المقطوع يجب أن يكون موجوداً قبل القاطع! وما لم يُقطع في الأعلى ترسّب بعده!",
            "Cross-cutting principle: an igneous intrusion or fault is younger than all layers it cuts, and older than undisturbed layers above it.",
            ["The basalt dike cuts through Layers 4, 3, and 2 → those three layers existed before the dike.", "The dike stops below Layer 1 without cutting it → Layer 1 deposited AFTER the dike cooled and eroded flat."],
            "Cut layers (4, 3, 2) < Dike < Overlying uncut Layer 1.",
            "القاطع أحدث من كل الطبقات التي يخترقها، وأقدم من أي طبقة تعلوه دون أن يقطعها.",
            ["بما أن البازلت قطع الطبقات 4 و 3 و 2 فلا بد أنها تكونت قبله.", "وبما أن الطبقة 1 لم تُقطع وتغطي القاطع فقد ترسّبت بعده (هي الأحدث)."],
            "4 ← 3 ← 2 ← القاطع ← 1.",
            None, None,
        ),
        (
            "A fast mountain river carrying boulders, gravel, coarse sand, and fine clay slows down sharply as it enters a calm flat sea, building a triangle-shaped delta. In what order from shoreline OUT into deep water do these sediments settle by size?",
            "يحمل نهر جبلي سريع جلاميدَ وحصى ورملاً خشناً وطيناً ناعماً، ثم يتباطأ فجأة عند التقائه ببحر هادئ مكوناً دلتا مثلثية. بأي ترتيب تتدرج الرسوبيات من الشاطئ نحو المياه الأعمق؟",
            [
                ("Heavy gravel and coarse sand drop near the shore first, while fine silt and clay carry farthest out into deep water", "يسقط الحصى والرمل الخشن قرب الشاطئ أولاً، بينما يحمل التيار الضعيف الطمي والطين الناعم أبعد نحو المياه العميقة"),
                ("Fine clay drops immediately at the beach while giant boulders float farthest out to sea", "يترسب الطين الناعم أولاً عند الشاطئ بينما تطفو الجلاميد أبعد نحو عمق البحر"),
                ("All particle sizes drop mixed together at the exact same kilometer regardless of speed", "تترسب جميع الأحجام مختلطة في الكيلومتر نفسه مهما تغيرت السرعة"),
                ("Sediments dissolve into pure water and settle only when frozen", "تذوب الرسوبيات تماماً ولا تستقر إلا عند تجمد البحر"),
            ],
            "As water slows down, which particles become too heavy for the weaker current to carry first?",
            "عندما تضعف سرعة الماء، أي حبيبات يعجز التيار الضعيف عن حملها فتسقط أولاً؟",
            "River deposition sorts sediment by particle weight and size as current velocity falls.",
            ["Heaviest gravel needs fast flow, so it drops immediately where velocity slows near the river mouth.", "Lightest clay stays suspended longest and settles farthest offshore in calm water."],
            "Heaviest drops first; lightest settles farthest out.",
            "تفرز التعرية والترسيب الرسوبيات حسب الحجم والوزن كلما تباطأت سرعة التيار.",
            ["الحصى الثقيل يحتاج لتيار قوي فيسقط فوراً عند تباطؤ النهر عند المصب.", "أما حبيبات الطين الدقيقة الخفيفة فتبقى معلّقة وتترسب بعيداً في المياه الهادئة."],
            "الأثقل يترسب أولاً قرب المصب، والأخف يبتعد إلى العمق.",
            svg_process_flow(["Fast Stream", "Calm Sea", "Gravel Drops", "Clay Far Out"], "Velocity drops → Particle sorting", "Delta Sediment Sorting"),
            svg_process_flow(["تيار سريع", "بحر هادئ", "ترسب الحصى", "ابتعاد الطين"], "تباطؤ السرعة ← فرز الحبيبات", "تدرّج الرسوبيات في الدلتا"),
        ),
        (
            "A student places equal 20 g samples of solid marble chip, marble pebbles, and powdered marble into three identical beakers of warm vinegar and records CO2 gas released in 2 minutes as shown. Why did powdered marble react fastest?",
            "وضع طالب 20 جم من قطعة رخام واحدة، و20 جم من حصى رخام، و20 جم من مسحوق رخام في ثلاثة كؤوس متماثلة من الخل الدافئ وسجّل حجم غاز CO2 المنطلق خلال دقيقتين كما في الرسم. لماذا تفاعل مسحوق الرخام أسرع؟",
            [
                ("Crushing into powder vastly increases exposed surface area touching the acid at once", "الطحن إلى مسحوق يضاعف مساحة السطح المعرّضة للتلامس مع الحمض في اللحظة نفسها"),
                ("Crushing increases the mass of the 20 g marble sample to 80 g", "الطحن يزيد كتلة العينة من 20 جم إلى 80 جم"),
                ("Crushing changes calcium carbonate chemically into sodium metal", "الطحن يحول كربونات الكالسيوم كيميائياً إلى معدن الصوديوم"),
                ("Powder absorbs extra heat from the classroom ceiling lights", "يمتص المسحوق حرارة إضافية من إضاءة الغرفة"),
            ],
            "Acid attacks only the outside faces of solid grains — compare total exposed faces in 1 big block vs 10,000 tiny grains!",
            "الحمض يتلامس مع السطح الخارجي فقط — قارن مساحة سطح كتلة واحدة بمساحة أسطح آلاف الحبيبات الدقيقة!",
            "Mechanical fracturing accelerates chemical weathering by increasing reactive surface area per unit mass.",
            ["All three flasks held identical mass (20 g) and identical acid.", "Splitting one lump into powder exposes countless new inner surfaces simultaneously, speeding chemical reaction."],
            "Smaller pieces = greater surface area = faster chemical weathering.",
            "التجوية الميكانيكية تسرّع التجوية الكيميائية بزيادة مساحة السطح المعرّض للتفاعل.",
            ["الكتلة في الكؤوس الثلاثة متساوية (20 جم)، لكن التفتيت يكشف أسطحاً جديدة كثيرة أمام الحمض.", "كلما زادت مساحة السطح المتلامس تسارعت التفاعلات الكيميائية."],
            "الطحن يرفع مساحة السطح لا الكتلة.",
            svg_bar_chart([("1 Block", 18, "#2563eb"), ("Pebbles", 46, "#ea580c"), ("Powder", 110, "#16a34a")], "CO2 (mL)", "Surface Area & Acid Reaction"),
            svg_bar_chart([("كتلة واحدة", 18, "#2563eb"), ("حصى صغيرة", 46, "#ea580c"), ("مسحوق", 110, "#16a34a")], "CO2 (مل)", "مساحة السطح وتفاعل الحمض"),
        ),
        (
            "Geologists hiking high along the dry rocky cliffs of Saudi Arabia's Tuwaiq Escarpment discover abundant fossilized marine sea shells and Jurassic ammonites embedded inside limestone beds. Which scientific conclusion is strongly supported?",
            "عثر جيولوجيون أثناء تسلّق جروف جبل طويق الصخرية الجافة في وسط المملكة على أحافير وفيرة لأصداف بحرية وأمونيتات جورية داخل طبقات الحجر الجيري. ما الاستنتاج العلمي المدعوم بقوة؟",
            [
                ("Hundreds of millions of years ago, that desert region lay submerged beneath an ancient shallow sea that later uplifted", "قبل مئات ملايين السنين كانت هذه المنطقة الصحراوية مغمورة تحت بحر ضحل قديم ثم ارتفعت قشرتها لاحقاً"),
                ("Ancient desert camels carried marine ammonites thousands of kilometers uphill to store them in wet mud", "حملت الجمال القديمة تلك الأمونيتات البحرية آلاف الكيلومترات لتدفنها في الطين"),
                ("Marine sea creatures evolved to swim freely inside dry desert limestone rock", "تكيفت الأصداف البحرية للسباحة داخل الصخور الجيرية الجافة"),
                ("Wind blew heavy fossilized limestone cliffs upward from coastal reefs yesterday", "رفعت الرياح الجروف الجيرية الثقيلة من الشواطئ حديثاً"),
            ],
            "Remember what environment living ammonites and thick limestone reefs require, and remember plates uplift landmasses over geological time!",
            "في أي بيئة تعيش الأمونيتات البحرية ويتكون الحجر الجيري، وكيف ترتفع قيعان البحار عبر العصور الجيولوجية؟",
            "Fossils preserve past environmental conditions and record dramatic geologic sea-level and tectonic changes.",
            ["Marine organisms live in ocean water, and limestone typically deposits on warm shallow marine shelves.", "Finding marine fossils high in today's dry mountains proves ancient sea coverage followed by tectonic uplift and sea retreat."],
            "Marine fossils on dry mountains = ancient ocean + later uplift.",
            "تُعدّ الأحافير سجلاً تاريخياً يكشف البيئات القديمة وتغيرات القشرة الأرضية.",
            ["الأمونيتات كائنات بحرية منقرضة والحجر الجيري يترسب غالباً في البحار الضحلة الدافئة.", "وجودها اليوم في مرتفعات جافة يثبت أنها كانت قاع بحر قديم ثم ارتفعت القشرة."],
            "أحافير بحرية فوق جبل جاف = بحر قديم ثم رفع تكتوني.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in hard_b20:
        B.add_concept(tp, "Hard", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)


def _add_b21(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B21"

    # Easy (0..4): Water cycle flow, Evaporation vs Transpiration, Infiltration/Aquifer, Sun+Gravity drivers, Freshwater share bar chart
    easy_b21 = [
        (
            "In the water cycle diagram, warm water vapor rises high into cooler air and turns into tiny liquid droplets clustering into clouds. Which process is occurring at Step 2?",
            "في مخطط دورة الماء، يرتفع بخار الماء الدافئ إلى الهواء الأبرد في الأعلى ليتحوّل إلى قطيرات سائلة دقيقة تشكّل السحب. ما العملية التي تحدث في الخطوة 2؟",
            [
                ("Condensation", "التكثف"),
                ("Evaporation", "التبخر"),
                ("Precipitation", "الهطول"),
                ("Infiltration", "التسرب الجوفي"),
            ],
            "Gas cooling back into liquid droplets = Condensation!",
            "تحوّل الغاز بالتبريد إلى قطيرات سائلة = التكثف!",
            "Condensation transforms rising water vapor into cloud droplets or ice crystals as air cools.",
            ["Step 1 (Evaporation) turns liquid sea water into vapor gas.", "Step 2 (Condensation) cools vapor back into visible cloud droplets."],
            "Vapor gas → liquid cloud droplets = Condensation.",
            "التكثف يحوّل بخار الماء الغازي عند برودته إلى قطيرات سحابية مرئية.",
            ["في التبخر يتحول السائل إلى غاز، وفي التكثف يعود الغاز البارد قطيرات ماء.", "من تلك القطيرات المتجمعة تتكوّن الغيوم قبل الهطول."],
            "بخار ← قطيرات سحب = تكثف.",
            svg_process_flow(["1. Evaporate", "2. Condense", "3. Precipitate", "4. Runoff"], "Solar Energy + Gravity", "Water Cycle Stages"),
            svg_process_flow(["1. التبخر", "2. التكثف", "3. الهطول", "4. الجريان"], "طاقة الشمس + الجاذبية", "مراحل دورة الماء"),
        ),
        (
            "Besides evaporation from oceans and rivers, green forests also release huge amounts of water vapor into the atmosphere through tiny leaf stomata. What is this plant-driven step called?",
            "إلى جانب التبخر من البحار والأنهار، تطلق الغابات الخضراء كميات كبيرة من بخار الماء إلى الجو عبر ثغور الأوراق. ماذا تسمى هذه العملية النباتية؟",
            [
                ("Transpiration", "النتح"),
                ("Sublimation", "التسامي"),
                ("Sedimentation", "الترسيب"),
                ("Freezing", "التجمد"),
            ],
            "Plants 'transpire' water drawn up from roots out through leaf pores!",
            "تفقد النباتات الماء عبر ثغور أوراقها بعملية تُسمى النتح!",
            "Transpiration is water evaporation from inside living plants through leaf stomata.",
            ["Roots absorb soil moisture, xylem lifts it to leaves, and stomata release vapor into the air.", "Together, evaporation and transpiration supply atmospheric moisture."],
            "Water vapor released by plant leaves = Transpiration.",
            "النتح هو تبخر الماء وخروجه على شكل بخار من ثغور أوراق النباتات.",
            ["تمتص الجذور الماء ويرفعه الخشب للأوراق حيث يخرج جزء منه كبخار عبر الثغور.", "يسهم النتح مع التبخر في تغذية الغلاف الجوي بالرطوبة."],
            "تبخر الماء عبر أوراق النبات = النتح.",
            None, None,
        ),
        (
            "After heavy desert rain falls in a wadi, some water soaks downward through loose gravel and porous sandstone into deep underground water-bearing rock layers. What are the downward soaking process and the underground storage layer called?",
            "بعد هطول أمطار غزيرة في أحد الأودية، يتغلغل جزء من الماء إلى أسفل عبر الحصى والحجر الرملي المسامي ليستقر في طبقات صخرية حاملة للمياه. ما اسم عملية التغلغل وما اسم الخزان الصخري الباطني؟",
            [
                ("Infiltration into an aquifer", "الرشح (التسرب) إلى خزان جوفي"),
                ("Condensation into a glacier", "التكثف إلى نهر جليدي"),
                ("Transpiration into a cumulonimbus cloud", "النتح إلى سحابة ركامية"),
                ("Evaporation into solid bedrock", "التبخر داخل صخر الأساس"),
            ],
            "Water filters down ('infiltrates') into porous rock ('aquifer') holding groundwater.",
            "يتسرب الماء للأسفل إلى طبقة مسامية تخزن المياه الجوفية (خزان جوفي)!",
            "Infiltration recharges aquifers, which store Earth's accessible liquid freshwater underground.",
            ["Porous sandstone and sand let gravity pull water downward into pores.", "Saturated permeable rock storing extractable water is an aquifer."],
            "Soaking down = Infiltration; Rock storage = Aquifer.",
            "يدخل الماء الباطن عبر عملية الرشح (التسرب) ويتجمع في الخزان الجوفي.",
            ["تسمح المسامات المتصلة في الرمل والحجر الرملي بمرور الماء للأسفل وتخزينه.", "تُعدّ الخزانات الجوفية مصدراً أساسياً للمياه العذبة في المناطق الجافة."],
            "التغلغل = الرشح؛ الطبقة المخزّنة = الخزان الجوفي.",
            None, None,
        ),
        (
            "What two natural drivers power the continuous movement of water through Earth's water cycle without needing pumps?",
            "ما العاملان الطبيعيان الرئيسيان اللذان يمدّان دورة الماء باستمرار الحركة دون مضخات؟",
            [
                ("Solar energy (evaporation/rising air) and Earth's gravity (precipitation/runoff/infiltration)", "طاقة الشمس (للتبخر وصعود البخار) والجاذبية الأرضية (للهطول والجريان والرشح)"),
                ("Ocean fish swimming and wind turbines", "سباحة الأسماك وتوربينات الرياح"),
                ("Moonlight reflection and soil magnetism", "انعكاس ضوء القمر ومغناطيسية التربة"),
                ("Earth's inner core solid iron alone", "الحديد الصلب في اللب الداخلي فقط"),
            ],
            "One heats liquid water to lift it UP into the sky; the other pulls heavy raindrops and rivers DOWN!",
            "أحدهما يسخّن الماء ليرفعه للأعلى، والآخر يجذب المطر والأنهار نحو الأسفل!",
            "Solar radiation provides thermal lifting energy while gravity drives downward precipitation, runoff, and infiltration.",
            ["Sun warms ocean surfaces and drives evaporation + atmospheric winds.", "Gravity pulls rain/snow down and steers streams downhill back to oceans."],
            "UP = Solar heat; DOWN = Gravity.",
            "تتكامل طاقة الشمس والجاذبية الأرضية لإدارة دورة الماء المستمرة.",
            ["تسخّن طاقة الشمس المسطحات المائية فيصعد البخار الدافئ في الجو.", "تسحب الجاذبية قطرات المطر والأنهار والمياه الجوفية عائدةً إلى الأسفل."],
            "للأعلى: حرارة الشمس؛ للأسفل: الجاذبية.",
            None, None,
        ),
        (
            "The bar chart summarizes Earth's total water supply. Roughly 97% is salty ocean water. Of the tiny ~3% that is freshwater, where is MOST of it locked away?",
            "يلخّص الرسم البياني توزيع المياه على كوكب الأرض؛ نحو 97% منها مياه مالحة في البحار والمحيطات. من النسبة الصغيرة للمياه العذبة (~3%)، أين يوجد معظمها؟",
            [
                ("Frozen in glaciers and polar ice caps (plus deep groundwater)", "متجمداً في الأنهار الجليدية والقمم القطبية (يليه المياه الجوفية)"),
                ("Flowing inside freshwater rivers and backyard lakes", "جارياً في الأنهار والبحيرات العذبة السطحية"),
                ("Floating as invisible water vapor clouds only", "معلقاً كبخار ماء وغيوم في الجو فقط"),
                ("Stored inside green desert cactus stems", "مختزناً داخل سيقان نباتات الصبار الصحراوية"),
            ],
            "Rivers and lakes are visible, yet hold under 1% of Earth's freshwater! Think of Antarctica and Greenland.",
            "الأنهار والبحيرات واضحة للعين لكنها أقل من 1% من الماء العذب! فكّر في القطبين والجبال الجليدية.",
            "Over two-thirds of Earth's freshwater is frozen in glaciers and ice sheets, leaving < 1% easily accessible liquid surface freshwater.",
            ["Saltwater = ~97%; Total Freshwater = ~3%.", "Within that 3%: ~69% is polar ice/glaciers, ~30% groundwater, and only ~0.3% in rivers and lakes."],
            "Most freshwater is frozen in ice sheets and glaciers!",
            "معظم المياه العذبة على الأرض مخزّن في صورة جليد قطبي وأنهار جليدية.",
            ["نحو 97% من مياه الأرض مالحة و3% فقط عذبة.", "نحو ثلثي المياه العذبة متجمد في القطبين، ونحو ثلثها مياه جوفية، وأقل من 1% في الأنهار والبحيرات السطحية."],
            "الأنهار والبحيرات لا تضم إلا حصة ضئيلة جداً من عذوبة الأرض.",
            svg_bar_chart([("Oceans", 97, "#2563eb"), ("Ice/Glacier", 2.1, "#0284c7"), ("Ground/Surf", 0.9, "#16a34a")], "Share (%)", "Earth Water Reservoirs"),
            svg_bar_chart([("المحيطات", 97, "#2563eb"), ("الجليد", 2.1, "#0284c7"), ("جوفي/سطحي", 0.9, "#16a34a")], "النسبة (%)", "مخازن المياه على الأرض"),
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b21:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Permeability table, 3 math water budget / runoff / savings Qs, Invisible gas vs visible cloud droplets
    B.add_concept(
        tp, "Medium", bp,
        "A drilling team records four underground rock layers in the table. Which layer works BEST as a natural underground AQUIFER holding water that wells can pump easily, and which acts as a SEAL trapping water below it?",
        "سجّل فريق حفر خصائص أربع طبقات صخرية في الجدول. أي طبقة تصلح أفضل خزان جوفي طبيعي يسهل ضخ الماء منه، وأي طبقة تعمل كطبقة حاجزة مانعة لتسرب الماء؟",
        [
            ("Best aquifer: Coarse Sandstone (Layer B); Best seal: Dense Clay/Shale (Layer C)", "أفضل خزان جوفي: الحجر الرملي الخشن (الطبقة B)؛ وأفضل حاجز مانع: الطين/الطفل الكثيف (الطبقة C)"),
            ("Best aquifer: Dense Clay (Layer C); Best seal: Coarse Sandstone (Layer B)", "أفضل خزان جوفي: الطين الكثيف (الطبقة C)؛ وأفضل حاجز: الحجر الرملي (الطبقة B)"),
            ("Best aquifer: Solid Granite (Layer D); Best seal: Loose Gravel (Layer A)", "أفضل خزان جوفي: الجرانيت المصمت (D)؛ وأفضل حاجز: الحصى المفكك (A)"),
            ("Both Granite (Layer D) and Clay (Layer C) pump faster than Coarse Sandstone", "كلٌّ من الجرانيت والطين يضخ الماء أسرع من الحجر الرملي الخشن"),
        ],
        "An aquifer needs BOTH open spaces (high porosity) AND connected paths for water to flow (high permeability)!",
        "الخزان الجوفي الجيد يحتاج مسامات متسعة (مسامية عالية) وممرات متصلة تسمح بالجريان (نفاذية عالية)!",
        "Aquifers require high porosity and high permeability; aquicludes (seals) have near-zero permeability.",
        ["Coarse Sandstone has high porosity (26%) AND high permeability so groundwater flows readily to wells.", "Dense Clay traps pores tightly with nearly zero permeability, acting as an impermeable cap/seal."],
        "Connected pores = Aquifer (B); Impermeable barrier = Clay (C).",
        "يجمع الخزان الجوفي الفعّال بين المسامية العالية والنفاذية العالية، بينما تمنع الطبقة الكتيمة التسرب.",
        ["الحجر الرملي الخشن يتيح تخزين الماء (26% مسامية) وجريانه بحرية نحو الآبار (نفاذية عالية).", "الطفل الكثيف شبه عديم النفاذية فيعمل غطاءً عازلاً يحجز الماء."],
        "الحجر الرملي = خزان؛ الطفل الكثيف = طبقة حاجزة.",
        svg_data_table(["Layer", "Material", "Porosity", "Permeability"], [["A", "Loose Gravel", "30%", "Very High"], ["B", "Sandstone", "26%", "High"], ["C", "Dense Clay", "42%*", "Almost Zero"], ["D", "Granite", "1%", "Almost Zero"]], "Rock Permeability Data", [56, 102, 76, 98]),
        svg_data_table(["الطبقة", "الصخر", "المسامية", "النفاذية"], [["A", "حصى مفكك", "30%", "عالية جداً"], ["B", "حجر رملي", "26%", "عالية"], ["C", "طين كثيف", "42%", "شبه معدومة"], ["D", "جرانيت صلد", "1%", "شبه معدومة"]], "بيانات مسامية الصخور ونفاذيتها", [58, 100, 74, 102]),
    )

    B.add_math(
        tp, "Medium", bp,
        "During a spring rainstorm, a desert wadi receives 120 mm of total precipitation. Measurements show 45 mm evaporates or transpires and 32 mm flows away over the surface as wadi runoff. Assuming no water is stored on leaves, how many millimeters of rainwater infiltrate underground into the aquifer?",
        "خلال عاصفة مطرية ربيعية استقبل أحد الأودية 120 ملم من الأمطار. أظهرت القياسات تبخر ونتح 45 ملم، وجريان 32 ملم على السطح كسيول. كم مليمتراً من المطر يترشّح إلى الخزان الجوفي في باطن الأرض؟",
        43, [75, 77, 13],
        "Conservation of water budget: Total Rain = Evaporation/Transpiration + Runoff + Infiltration.",
        "حفظ ميزانية الماء: المطر الكلي = التبخر/النتح + الجريان السطحي + الرشح الجوفي.",
        "Watershed precipitation splits into evapotranspiration, surface runoff, and groundwater infiltration.",
        ["Combined surface loss and flow = 45 + 32 = 77 mm.", "Remaining infiltrated water = 120 - 77 = 43 mm."],
        "Check: 45 + 32 + 43 = 120 mm total.",
        "تتوزع كمية الأمطار الساقطة بين التبخر والجريان السطحي والرشح في التربة.",
        ["مجموع الفاقد بالتبخر والجريان = 45 + 32 = 77 ملم.", "الرشح الجوفي = 120 - 77 = 43 ملم."],
        "تحقق: 45 + 32 + 43 = 120 ملم.",
        suffix="",
    )

    B.add_math(
        tp, "Medium", bp,
        "A 40 mm rainstorm falls equally on an unpaved grassy park (where 65% infiltrates into soil) and an adjacent paved asphalt parking lot (where only 10% infiltrates). Neglecting evaporation during the brief storm, how many MORE millimeters of surface runoff leave the paved lot than the grassy park?",
        "هطلت أمطار مقدارها 40 ملم بالتساوي على حديقة عشبية (يترشح فيها 65% من الماء للتربة) وموقف سيارات إسفلتي مجاور (يترشح فيه 10% فقط). بإهمال التبخر أثناء العاصفة، بكم ملم يزيد الجريان السطحي من الموقف الإسفلتي عن الحديقة؟",
        22, [14, 26, 36],
        "Find runoff (%) for each surface (100% - infiltration %), then multiply by 40 mm and subtract!",
        "احسب نسبة الجريان السطحي لكل سطح (100% - نسبة الرشح)، ثم اضرب في 40 ملم واطرح!",
        "Impermeable urban pavement sharply increases surface runoff compared with permeable soil.",
        ["Grassy park runoff = (100% - 65%) × 40 mm = 35% × 40 = 14 mm.", "Paved lot runoff = (100% - 10%) × 40 mm = 90% × 40 = 36 mm.", "Extra runoff = 36 - 14 = 22 mm."],
        "Check: (90% - 35%) × 40 = 55% × 40 = 22 mm.",
        "الأسطح الإسفلتية الكتيمة تقلّل الرشح وتزيد السيول السطحية بشكل كبير.",
        ["جريان الحديقة = 35% × 40 = 14 ملم؛ جريان الإسفلت = 90% × 40 = 36 ملم.", "الزيادة في الجريان = 36 - 14 = 22 ملم."],
        "تحقق: 55% × 40 ملم = 22 ملم زيادة.",
        suffix="",
    )

    B.add_concept(
        tp, "Medium", bp,
        "Looking up on a humid summer day, a student sees puffy white cumulus clouds surrounded by clear blue sky. Which statement accurately explains the physical difference between invisible water vapor and visible clouds?",
        "نظر طالب إلى السماء في يوم صيفي رطب فرأى سحباً ركامية بيضاء يحيط بها صفاء أزرق. أي عبارة تفسّر بدقة الفرق الفيزيائي بين بخار الماء غير المرئي والسحب المرئية؟",
        [
            ("Water vapor is an invisible gas mixed in the clear air, whereas clouds are visible millions of tiny LIQUID water droplets or ice crystals that condensed", "بخار الماء غاز شفاف غير مرئي مختلط بالهواء، أما السحب فتتكون من ملايين قطيرات الماء السائل أو بلورات الجليد المتكثفة المرئية"),
            ("Water vapor is solid blue ice dust, whereas clouds are dry smoke from factories", "بخار الماء غبار جليدي أزرق صلب، والسحب دخان جاف من المصانع"),
            ("Water vapor exists only inside oceans while clouds are giant sheets of frozen liquid nitrogen", "بخار الماء لا يوجد في الهواء، والسحب ألواح من النيتروجين السائل"),
            ("Both clouds and clear air contain zero water molecules unless rain is already falling", "تخلو السحب والهواء الصافي من جزيئات الماء ما لم ينزل المطر فعلاً"),
        ],
        "Remember: real water vapor gas is completely transparent (invisible), just like oxygen and nitrogen!",
        "تذكّر: بخار الماء الحقيقي غاز شفاف تماماً لا يُرى بالعين المجردة مثل الأكسجين والنيتروجين!",
        "Clouds become visible only after invisible water vapor gas cools and condenses into liquid droplets or ice crystals.",
        ["Even clear desert air contains invisible gaseous water vapor molecules.", "When rising air cools to its dew point, vapor condenses around tiny dust particles into visible cloud droplets that scatter sunlight."],
        "Gas = invisible vapor; Liquid droplets/ice crystals = visible clouds (and steam mist!).",
        "السحب مرئية لأنها قطيرات سائلة أو بلورات ثلجية تشتت الضوء، بينما بخار الماء غاز شفاف.",
        ["يحتوي الهواء الصافي على بخار ماء غير مرئي تماماً.", "عند تبرد الهواء الصاعد يتكثف البخار حول دقائق الغبار إلى قطيرات مرئية تشكّل الغيوم."],
        "البخار غاز خفي، والسحاب قطيرات متكثفة مرئية.",
        None, None,
    )

    B.add_math(
        tp, "Medium", bp,
        "A date-palm farm replaces old flood channels (using 1,500 L of water per day) with subsurface drip irrigation that supplies the trees with enough moisture using only 900 L per day. Over a 7-day week, how many liters of water are saved?",
        "استبدلت مزرعة نخيل قنوات الري بالغمر القديمة (التي تستهلك 1500 لتر يومياً) بشبكة ري بالتنقيط تحت السطحية تروي النخيل بكفاءة باستخدام 900 لتر فقط يومياً. كم لتراً من الماء يُوفَّر خلال أسبوع واحد (7 أيام)؟",
        4200, [600, 6300, 10500],
        "First find liters saved per day (1500 - 900), then multiply by 7 days!",
        "احسب ما يتم توفيره في اليوم الواحد أولاً (1500 - 900)، ثم اضرب في 7 أيام!",
        "Subsurface drip irrigation prevents direct surface evaporation and runoff losses.",
        ["Daily savings = 1500 - 900 = 600 L/day.", "Weekly savings = 600 × 7 = 4,200 L."],
        "Check: (1500 × 7) - (900 × 7) = 10,500 - 6,300 = 4,200 L.",
        "يمنع الري بالتنقيط الفقد الكبير بالتبخر السطحي والجريان غير المستفاد منه.",
        ["التوفير اليومي = 1500 - 900 = 600 لتر/يوم.", "التوفير الأسبوعي = 600 × 7 = 4200 لتر."],
        "تحقق: 10500 - 6300 = 4200 لتر.",
        suffix="",
    )

    # Hard (10..14): Urban paving hydrograph bar chart, Coastal saltwater intrusion, Closed terrarium conservation, Snowpack timing, Sustainable city water math
    B.add_concept(
        tp, "Hard", bp,
        "A town replaces its grassy hillside with asphalt parking lots and storm drains. Looking at the rainfall-response bar chart, why does the nearby wadi suffer sharper FLASH FLOODS right after storms yet hold LOWER groundwater levels in dry months?",
        "استبدلت بلدة تلاً عشبياً بمواقف إسفلتية ومصارف مطر. بالرجوع إلى الرسم البياني قبل البناء وبعده، لماذا يزداد خطر السيول المفاجئة أثناء المطر بينما تنخفض المياه الجوفية في شهور الجفاف؟",
        [
            ("Asphalt blocks soil infiltration, sending almost all rainwater straight into rapid surface storm runoff instead of soaking down to recharge aquifers", "يمنع الإسفلت رشح الماء في التربة، فيتدفق معظمه سريعاً كجريان سطحي مسبب للسيول بدلاً من تغذية الخزانات الجوفية"),
            ("Asphalt evaporates water underground before rain reaches the soil", "يبخر الإسفلت المياه الجوفية العميقة قبل هطول المطر"),
            ("Asphalt attracts twice as many storm clouds directly over parking lots", "يجذب الإسفلت ضعف كمية السحب الممطرة فوق المواقف"),
            ("Grassland absorbs stormwater forever and destroys it", "يمتص العشب مياه الأمطار ويفنيها إلى الأبد"),
        ],
        "Notice how Runoff bars shoot UP while Infiltration bars plummet after paving!",
        "لاحظ كيف ارتفع عمود الجريان السطحي وهبط عمود الرشح الجوفي بعد التبليط!",
        "Impermeable paving converts slow groundwater recharge into fast flash-flood surface runoff.",
        ["Before paving: 60% soaked into soil (recharging aquifers slowly) and only 25% ran off.", "After paving: infiltration plunges to 10%, forcing 80% rapidly into streams → peak flood surge + depleted dry-season groundwater."],
        "Blocked infiltration = flood spikes + dry wells.",
        "تحوّل الأسطح الكتيمة التغذية البطيئة للمياه الجوفية إلى سيول سطحية مفاجئة.",
        ["قبل الإسفلت كان 60% من المطر يترشح ليغذي الآبار، و25% فقط يجري على السطح.", "بعد الإسفلت هبط الرشح إلى 10% وارتفع الجريان إلى 80% مما يضاعف الفيضانات ويقلل المخزون الجوفي."],
        "منع الرشح يسبب السيول وجفاف الآبار معاً.",
        svg_bar_chart([("Grass Run", 25, "#2563eb"), ("Paved Run", 80, "#dc2626"), ("Grass Infil", 60, "#16a34a"), ("Paved Infil", 10, "#ea580c")], "Rain (%)", "Before vs After Paving"),
        svg_bar_chart([("جريان عشب", 25, "#2563eb"), ("جريان إسفلت", 80, "#dc2626"), ("رشح عشب", 60, "#16a34a"), ("رشح إسفلت", 10, "#ea580c")], "المطر (%)", "أثر التبليط على الجريان والرشح"),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Along a sandy coastline, farmers pump freshwater from wells faster than winter rainfall can replenish the aquifer. Over several years, irrigation water from those same wells turns noticeably salty. What happened underground?",
        "على ساحل رملي، ضخّ مزارعون المياه العذبة من الآبار أسرع من تعويض الأمطار للخزان الجوفي. بعد عدة سنوات تحوّل ماء تلك الآبار إلى ماء مالح. ما الذي حدث في باطن الأرض؟",
        [
            ("Over-pumping lowered the freshwater table, allowing denser salty seawater to push inland into the aquifer (saltwater intrusion)", "أدى الضخ المفرط إلى هبوط مستوى الماء العذب، فاندفعت مياه البحر المالحة الأثقل إلى داخل الخزان الجوفي (تداخل مياه البحر)"),
            ("Pumping motors boiled freshwater until only pure sea salt remained underground", "أغلت مضخات الآبار الماء العذب حتى بقي الملح وحده"),
            ("Coastal air condensed directly into ocean salt inside pump pipes", "تكثف هواء الساحل إلى ملح بحري داخل أنابيب المضخة"),
            ("Earth's inner core injected salt water upward from 6,000 km deep", "دفع اللب الداخلي ماءً مالحاً للأعلى من عمق 6000 كم"),
        ],
        "Freshwater pushing seaward keeps salty ocean water back — if freshwater pressure drops, ocean water flows inland!",
        "ضغط الماء العذب المتجه للبحر كان يصدّ البحر المالح — فعندما ضعف ضغط الماء العذب اندفع ماء البحر للداخل!",
        "Aquifer depletion near oceans causes saltwater intrusion into coastal wells.",
        ["Normally, inland freshwater pressure pushes toward the coast and balances seawater pressure.", "Excessive extraction drops the water table, pulling salty seawater horizontally inland into well cones."],
        "Over-pumping coastal aquifers causes saltwater intrusion.",
        "يؤدي الاستنزاف الجائر للخزانات الجوفية الساحلية إلى تداخل مياه البحر المالحة.",
        ["في الحالة الطبيعية يدفع ضغط المياه العذبة الأعلى مياه البحر المالحة خارج اليابسة.", "عند انخفاض منسوب الماء العذب بالضخ المفرط، تتوغل المياه المالحة داخل المسام وتلوّث الآبار."],
        "ضخ مفرط على الساحل = تداخل المياه المالحة.",
        svg_process_flow(["Over-Pumping", "Fresh Drops", "Sea Intrudes", "Salty Wells"], "Coastline Aquifer Imbalance", "Saltwater Intrusion"),
        svg_process_flow(["ضخ مفرط", "هبوط العذب", "تقدم المالح", "ملوحة الآبار"], "اختلال توازن الخزان الساحلي", "تداخل مياه البحر"),
    )

    B.add_concept(
        tp, "Hard", bp,
        "A student seals damp soil, pebbles, and a small fern inside a clear airtight glass jar (a terrarium) and sets it near a sunny window. Every day droplets condense inside the lid and drip back onto the fern, keeping it thriving for months with no added water. What happens to the TOTAL MASS of the sealed jar (assuming healthy plant growth)?",
        "أغلقت طالبة تربة رطبة وحصى ونبتة سرخس صغيرة داخل مرطبان زجاجي محكم الإغلاق ووضعته قرب نافذة مشمسة. تتكثف قطيرات ماء يومياً تحت الغطاء وتتساقط على التربة لشهور دون إضافة ماء. ماذا يحدث للكتلة الكلية للمرطبان المغلق؟",
        [
            ("Total mass stays constant because water and gases continuously cycle inside without matter escaping or entering", "تبقى الكتلة الكلية ثابتة لأن الماء والغازات تدور باستمرار داخل النظام المغلق دون دخول مادة أو خروجها"),
            ("Total mass doubles every month because sunlight adds kilograms of pure liquid water", "تتضاعف الكتلة كل شهر لأن ضوء الشمس يضيف كيلوجرامات من الماء"),
            ("Total mass drops to half because evaporation destroys water molecules inside glass", "تنخفض الكتلة إلى النصف لأن التبخر يفني جزيئات الماء"),
            ("Total mass drops to zero as soon as condensation forms clouds", "تصبح الكتلة صفراً فور تكوّن القطيرات المتكثفة"),
        ],
        "Energy (light/heat) passes through clear glass, NOT water or gas atoms! Remember conservation of matter.",
        "الطاقة (الضوء والحرارة) تعبر الزجاج، أما ذرات الماء والغازات فلا تخرج ولا تدخل! تذكر قانون حفظ المادة.",
        "In a closed system like a sealed terrarium (and largely Earth's water budget), energy flows through while matter recycles with constant mass.",
        ["Sunlight supplies energy to power evaporation, transpiration, and photosynthesis.", "No atoms cross the airtight seal, so evaporation + transpiration = condensation + dripping → constant total mass."],
        "Closed matter cycle + external sunlight energy = constant mass.",
        "في النظام المغلق للتراريوم تتدفق الطاقة الضوئية والحرارية عبر الزجاج بينما تبقى المادة محفوظة في دورة مغلقة.",
        ["يحرّك ضوء الشمس عمليتي البناء الضوئي والتبخر داخل الوعاء دون إضافة مادة من الخارج.", "وبما أن الغطاء محكم لا يسمح بتسرب الغاز أو الماء، تظل الكتلة الكلية ثابتة."],
        "دورة مادة مغلقة = كتلة كلية ثابتة.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Two neighboring river valleys both receive 600 mm of precipitation each year. Valley X gets winter snow on high peaks that melts slowly in late spring and summer, whereas Valley Y warms slightly so winter precipitation falls as rain instead of snow. Even though total annual rainfall stays 600 mm, why does Valley Y face summer farm droughts?",
        "يتلقى واديان مجاوران 600 ملم من الهطول سنوياً. يتلقى الوادي X ثلوجاً شتوية على القمم تذوب ببطء في الربيع والصيف، بينما ارتفعت حرارة الوادي Y قليلاً فسقط هطوله الشتوي مطراً بدلاً من الثلج. رغم ثبات مجموع المطر (600 ملم)، لماذا يعاني الوادي Y من جفاف المزارع صيفاً؟",
        [
            ("Winter rain runs straight off into the sea immediately in winter instead of staying stored as slow-melting mountain snowpack for summer crops", "يجري المطر الشتوي مباشرة نحو البحر في الشتاء بدلاً من أن يُختزن كثلوج جبلية تذوب تدريجياً لري المحاصيل الصيفية"),
            ("Rainwater freezes harder than snow and refuses to enter irrigation pipes", "ماء المطر يتجمد أصلب من الثلج ولا يدخل أنابيب الري"),
            ("Summer farms need 0 mm of water when winter snow disappears", "لا تحتاج المزارع الصيفية أي ماء عند غياب الثلج"),
            ("Turning snow into winter rain destroys 80% of H2O molecules permanently", "تحوّل الثلج إلى مطر يفني 80% من جزيئات الماء للأبد"),
        ],
        "Think about TIMING of release: mountain snowpack acts like a natural delayed-release water reservoir!",
        "فكّر في توقيت الإمداد المائي: الغطاء الثلجي الجبلي يعمل كخزان مؤجَّل يطلق الماء ببطء عند الحاجة صيفاً!",
        "Snowpack stores winter precipitation as solid water and releases it gradually during dry growing seasons.",
        ["In Valley X, cold storage delays runoff until warm summer months when crops need irrigation.", "In Valley Y, winter liquid rain surges downhill right away in winter floods, leaving dry riverbeds by summer."],
        "Timing matters as much as annual total!",
        "لا يعتمد توافر الماء على المجموع السنوي فقط، بل على توقيت تخزينه وإطلاقه أيضاً.",
        ["تخزن الثلوج الجبلية مياه الشتاء وتذوب تدريجياً في الأشهر الحارة عندما تزداد حاجة المزارع.", "أما المطر الشتوي فيجري سريعاً في الأودية خلال الشتاء ويترك الأنهار شحيحة صيفاً."],
        "الثلج الجبلي خزان طبيعي ينظّم توقيت توفر الماء.",
        None, None,
    )

    B.add_math(
        tp, "Hard", bp,
        "A coastal desert city needs 12,000 m³ of water every day. Desalination plants supply 7,500 m³ per day, and recycled treated wastewater supplies 2,100 m³ per day for parks. If groundwater pumping must NOT exceed 1,800 m³/day to keep wells sustainable, how many cubic meters per day must citizens save through conservation?",
        "تحتاج مدينة ساحلية صحراوية إلى 12,000 م³ من المياه يومياً. توفر محطات التحلية 7,500 م³ يومياً، وتوفر المياه المعاد تدويرها 2,100 م³ يومياً لري الحدائق. إذا وجب ألا يتجاوز الضخ الجوفي 1,800 م³ يومياً لحماية الآبار من النضوب، فكم متراً مكعباً يومياً يجب توفيره عبر الترشيد؟",
        600, [1800, 2400, 4500],
        "Add the maximum sustainable supply (7,500 + 2,100 + 1,800) and subtract from the 12,000 m³ demand!",
        "اجمع أقصى إمداد مستدام (7500 + 2100 + 1800) ثم اطرحه من حاجة المدينة الكلية (12000)!",
        "Sustainable water planning balances demand against safe renewable/desalinated supply.",
        ["Total safe daily supply = 7,500 + 2,100 + 1,800 = 11,400 m³/day.", "Required conservation savings = 12,000 - 11,400 = 600 m³/day."],
        "Check: 7,500 + 2,100 + 1,800 + 600 = 12,000 m³/day.",
        "التخطيط المائي المستدام يوازن الاستهلاك مع مصادر الإمداد الآمنة دون استنزاف الآبار.",
        ["مجموع الإمداد الآمن = 7500 + 2100 + 1800 = 11400 م³/يوم.", "العجز الواجب توفيره بالترشيد = 12000 - 11400 = 600 م³/يوم."],
        "تحقق: 7500 + 2100 + 1800 + 600 = 12000 م³/يوم.",
        suffix="",
    )


def _add_b22(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B22"

    # Easy (0..4): Barometer, Weather tools table, Weather vs Climate, High vs Low pressure skies, Greenhouse gases
    easy_b22 = [
        (
            "A meteorologist watches a barometer needle drop steadily from 1018 hPa to 996 hPa over several hours. What property does a barometer measure, and what weather usually follows a sharp pressure drop?",
            "يراقب راصد جوي مؤشر البارومتر وهو يهبط بثبات من 1018 هكتوباسكال إلى 996 هكتوباسكال خلال عدة ساعات. ماذا يقيس البارومتر، وما الطقس المتوقع عند هبوط الضغط بشدة؟",
            [
                ("Atmospheric air pressure; rising moist air often brings clouds, wind, or rain", "الضغط الجوي؛ وغالباً يتبعه هواء صاعد وسحب ورياح أو أمطار"),
                ("Relative soil humidity; permanent cloudless heat waves", "رطوبة التربة النسبية؛ وموجات جفاف دائمة بلا سحب"),
                ("Ocean wave speed; gentle morning frost only", "سرعة أمواج المحيط؛ وصقيع صباحي هادئ فقط"),
                ("Earthquake magnitude; clear sunny high-pressure calm", "شدة الزلازل؛ وصفاء مشمس وهدوء تام"),
            ],
            "Baro = weight/pressure! Low pressure lets air rise, cool, and condense into clouds.",
            "يقيس البارومتر وزن عمود الهواء (الضغط الجوي)! والضغط المنخفض يسمح بصعود الهواء وتكوّن الغيوم.",
            "Barometers measure atmospheric pressure; falling pressure signals an approaching low-pressure storm system.",
            ["Air pushes downward with measurable pressure (hectopascals, hPa).", "Falling barometric pressure means air is rising ahead of fronts or storms, forming clouds and rain."],
            "Dropping barometer = Low pressure approaching = clouds/rain likely.",
            "يقيس البارومتر الضغط الجوي، ويشير انخفاضه التدريجي إلى اقتراب منخفض جوي مصحوب بسحب وأمطار.",
            ["في المنخفض الجوي يصعد الهواء الرطب للأعلى فيبرد ويتكثف مكوناً الغيوم.", "أما ارتفاع الضغط فيرتبط غالباً باستقرار وصفاء السماء."],
            "انخفاض البارومتر = ضغط منخفض = سحب وأمطار محتملة.",
            None, None,
        ),
        (
            "Check the weather-station instrument table. Which pair matches the instrument that measures WIND SPEED and the instrument that measures RELATIVE HUMIDITY?",
            "تأمّل جدول أدوات محطة الرصد الجوي. أي زوج يطابق الأداة التي تقيس سرعة الرياح والأداة التي تقيس الرطوبة النسبية بالترتيب؟",
            [
                ("Anemometer (wind speed) and Hygrometer (relative humidity)", "الأنيمومتر (سرعة الرياح) والهيجرومتر (الرطوبة النسبية)"),
                ("Wind Vane (wind speed) and Rain Gauge (relative humidity)", "دوارة الرياح (سرعة الرياح) ومقياس المطر (الرطوبة النسبية)"),
                ("Thermometer (wind speed) and Barometer (relative humidity)", "الترمومتر (سرعة الرياح) والبارومتر (الرطوبة النسبية)"),
                ("Barometer (wind speed) and Anemometer (relative humidity)", "البارومتر (سرعة الرياح) والأنيمومتر (الرطوبة النسبية)"),
            ],
            "Spinning cups count how fast wind blows (anemometer); wind vane only points which direction wind comes from!",
            "الأكواب الدوارة تقيس سرعة الرياح (الأنيمومتر)، بينما دوارة الرياح تحدد الاتجاه فقط!",
            "Each weather sensor isolates a single atmospheric variable.",
            ["Anemometer = spinning cups for wind speed; Wind Vane = arrow for wind direction.", "Hygrometer = moisture percentage in air (relative humidity); Rain Gauge = precipitation depth."],
            "Speed = Anemometer; Humidity = Hygrometer.",
            "تتخصص كل أداة رصد بقياس متغير جوي محدد.",
            ["الأنيمومتر يقيس سرعة الرياح، أما دوارة الرياح فتحدد اتجاه هبوبها.", "والهيجرومتر يقيس نسبة الرطوبة في الهواء، ومقياس المطر يقيس كمية الهطول."],
            "سرعة الرياح: أنيمومتر؛ الرطوبة: هيجرومتر.",
            svg_data_table(["Instrument", "What It Measures"], [["Thermometer", "Air Temperature"], ["Anemometer", "Wind Speed"], ["Wind Vane", "Wind Direction"], ["Hygrometer", "Relative Humidity"]], "Weather Station Sensors", [118, 166]),
            svg_data_table(["الأداة", "الخاصية المقاسة"], [["الترمومتر", "درجة حرارة الهواء"], ["الأنيمومتر", "سرعة الرياح"], ["دوارة الرياح", "اتجاه الرياح"], ["الهيجرومتر", "الرطوبة النسبية"]], "أجهزة محطة الرصد الجوي", [118, 166]),
        ),
        (
            "A student reads: 'Today Tabuk has 14 °C temperatures with light rain, whereas Tabuk averages cool winters and hot dry summers over 30 years.' Which pair correctly labels these two statements?",
            "قرأت طالبة: (اليوم تشهد تبوك حرارة 14°م مع أمطار خفيفة، بينما تمتاز تبوك بشتاء بارد وصيف حار جاف خلال ثلاثين عاماً). أي وصف يميّز الجملتين بالترتيب؟",
            [
                ("First is Weather (short-term daily condition); second is Climate (long-term average pattern)", "الأولى تصف الطقس (حالة الجو اليومية القصيرة)، والثانية تصف المناخ (المعدل السائد طويل الأمد)"),
                ("First is Climate; second is Weather", "الأولى تصف المناخ، والثانية تصف الطقس"),
                ("Both statements describe only the water table depth", "الجملتان تصفان عمق المياه الجوفية فقط"),
                ("Both statements describe sudden hourly weather fronts", "الجملتان تصفان جبهات جوية ساعية مفاجئة فقط"),
            ],
            "Weather is what coat you wear today; Climate is what clothes fill your whole closet for the year!",
            "الطقس هو ما تلبسه اليوم؛ أما المناخ فهو نوع الملابس في خزانتك على مدار السنوات!",
            "Weather describes atmospheric state at a given hour/day; climate is multi-decade statistical averages.",
            ["'Today, 14 °C, light rain' is a temporary daily weather report.", "'Over 30 years: cool winters, hot dry summers' summarizes regional climate."],
            "Short-term = Weather; 30-year average = Climate.",
            "يصف الطقس حالة الغلاف الجوي الراهنة، بينما يلخّص المناخ المتوسطات طويلة المدى.",
            ["قولنا (اليوم 14°م وأمطار خفيفة) حالة يومية قصيرة المدى ← الطقس.", "أما متوسط 30 عاماً للشتاء والصيف في المنطقة ← المناخ."],
            "قصير المدى = الطقس؛ طويل المدى = المناخ.",
            None, None,
        ),
        (
            "Why do High-pressure weather zones typically bring clear blue skies and calm dry weather, whereas Low-pressure centers favor cloud formation and storms?",
            "لماذا ترتبط مناطق الضغط الجوي المرتفع غالباً بسماء صافية وطقس مستقر، بينما يكثر تشكّل السحب والعواصف في مراكز الضغط المنخفض؟",
            [
                ("In a High, cool air sinks and warms so clouds evaporate away; in a Low, warm moist air rises, cools, and condenses into clouds", "في الضغط المرتفع يهبط الهواء البارد ويدفأ فتتبخر السحب؛ أما في المنخفض فيصعد الهواء الدافئ الرطب ويبرد فيتكثف سحباً"),
                ("High pressure destroys all oxygen molecules above clouds", "يدمر الضغط المرتفع جزيئات الأكسجين فوق السحب"),
                ("Low pressure pulls ocean ice cubes directly into mountain rivers", "يسحب الضغط المنخفض مكعبات الجليد إلى أنهار الجبال"),
                ("Air never moves vertically inside any high or low pressure system", "لا يتحرك الهواء عمودياً أبداً في أنظمة الضغط الجوي"),
            ],
            "Remember what cooling air does (condensation) vs warming sinking air (evaporation)!",
            "تذكّر: الهواء الصاعد يبرد ويتكثف (سحب)، والهواء الهابط ينضغط ويدفأ فتتبدد السحب!",
            "Vertical motion links pressure systems directly to sky cover: rising = cooling/condensing; sinking = warming/drying.",
            ["Air flows into a surface Low and rises upward, expanding and cooling past its dew point to form clouds.", "Air sinks down in a High, compressing and warming, which prevents cloud droplets from persisting."],
            "Sinking air (High) = clear skies; Rising air (Low) = clouds/storms.",
            "ترتبط حركة الهواء العمودية مباشرة بتشكل السحب والصفاء الجوي.",
            ["تجميع الهواء في مركز الضغط المنخفض يدفعه للصعود حيث يبرد ويتكثف غيوماً.", "وهبوط الهواء في المرتفع الجوي يرفع حرارته ويمنع التكثف فتبقى السماء صافية."],
            "ضغط مرتفع = هبوط وصفاء؛ ضغط منخفض = صعود وتكثف.",
            None, None,
        ),
        (
            "Which trace atmospheric gases trap part of the infrared heat radiating outward from Earth's surface, naturally keeping our planet warm enough for liquid oceans (the greenhouse effect)?",
            "أي غازات أثرية في الغلاف الجوي تحبس جزءاً من الحرارة تحت الحمراء المنبعثة من سطح الأرض لتحافظ على دفء الكوكب وبقاء المحيطات سائلة (ظاهرة الاحتباس الحراري الطبيعية)؟",
            [
                ("Carbon dioxide (CO2), water vapor (H2O), and methane (CH4)", "ثاني أكسيد الكربون وبخار الماء والميثان"),
                ("Argon and pure liquid iron droplets", "الأرجون وقطرات الحديد السائل"),
                ("Pure nitrogen (N2) and neon lights", "النيتروجين النقي وغاز النيون"),
                ("Helium gas and solid quartz sand", "غاز الهيليوم ورمل الكوارتز الصلب"),
            ],
            "Nitrogen (78%) and oxygen (21%) let infrared heat pass straight through; multi-atom gases like CO2, H2O, and CH4 trap it!",
            "النيتروجين والأكسجين يمرران الحرارة، أما غازات مثل ثاني أكسيد الكربون وبخار الماء والميثان فتحبسها!",
            "Greenhouse gases absorb and re-emit outgoing thermal infrared radiation, moderating Earth's surface temperature.",
            ["Without natural greenhouse gases (H2O vapor, CO2, CH4), Earth's average temperature would drop below -18 °C.", "Adding excess CO2 from burning fossil fuels amplifies this heat trapping."],
            "CO2 + H2O vapor + CH4 = primary greenhouse gases.",
            "تمتص غازات الدفيئة الإشعاع الحراري الصادر من الأرض وتعيد إشعاعه للحفاظ على دفء الكوكب.",
            ["يسمح النيتروجين والأكسجين بمرور ضوء الشمس والحرارة بسهولة.", "أما ثاني أكسيد الكربون وبخار الماء والميثان فتمتص الحرارة المرتدة وتمنع تجمد المحيطات."],
            "غازات الدفيئة الرئيسية: CO2 وبخار الماء والميثان.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b22:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Sea breeze, Cold front table, Elevation (Abha vs Jeddah), Rain shadow (Asir mountains), Ocean specific heat
    med_b22 = [
        (
            "On a sunny afternoon in Jeddah along the Red Sea coast, sand and city streets warm rapidly while ocean water stays noticeably cooler. Following the flow diagram, which breeze blows along the beach at 2:00 PM?",
            "في ظهيرة يوم مشمس على ساحل جدة، تسخن الرمال والشوارع بسرعة بينما يظل ماء البحر أبرد نسبياً. بناءً على تسلسل المخطط، أي نسيم يهبّ على الشاطئ الساعة 2:00 ظهراً؟",
            [
                ("A cool sea breeze blowing onshore from the Sea toward Land", "نسيم بحر لطيف يهب من البحر نحو اليابسة"),
                ("A hot land breeze blowing offshore from Land toward Sea", "نسيم برّ حار يهب من اليابسة نحو البحر"),
                ("A freezing arctic blast blowing straight downward", "تيار قطبي متجمد يهبط عمودياً من القمم"),
                ("Complete stillness because land and sea always hold the same temperature", "سكون تام لتساوي حرارة البر والبحر دائماً"),
            ],
            "Warm air over hot sand rises upward (low pressure); denser cooler air over the sea rushes inward to replace it!",
            "الهواء الساخن فوق الرمال يصعد للأعلى، فيندفع الهواء الأبرد من فوق البحر ليحل محله نحو الشاطئ!",
            "Differential heating of land and sea drives coastal sea breezes by day and land breezes by night.",
            ["Daytime: land heats faster → warm air rises over land → cooler higher-pressure sea air flows onshore = Sea Breeze.", "Nighttime: land cools faster than water, reversing flow = Land Breeze."],
            "Daytime onshore cool air = Sea Breeze.",
            "يؤدي اختلاف سرعة تسخين اليابسة والماء إلى نشوء نسيم البحر نهاراً ونسيم البر ليلاً.",
            ["نهاراً تسخن اليابسة أسرع فيرتفع هواؤها، ويندفع الهواء البارد الكثيف من فوق البحر نحو اليابسة (نسيم البحر).", "ليلاً يبرد البر أسرع فينعكس الاتجاه إلى نسيم البر."],
            "من البحر إلى اليابسة نهاراً = نسيم البحر.",
            svg_process_flow(["Land Heats", "Warm Rises", "Low Pressure", "Sea Wind In"], "Afternoon Coastal Circulation", "Daytime Sea Breeze"),
            svg_process_flow(["تسخن الأرض", "يصعد الدافئ", "ضغط منخفض", "هواء البحر"], "الدوران الهوائي الساحلي ظهراً", "نسيم البحر نهاراً"),
        ),
        (
            "A weather station in northern Saudi Arabia records the readings shown in the table between 9:00 AM and 3:00 PM. Which atmospheric event passed across the station around midday?",
            "سجّلت محطة رصد شمالي المملكة القراءات الموضحة في الجدول بين 9:00 صباحاً و3:00 عصراً. أي ظاهرة جوية عبرت المحطة قرابة منتصف النهار؟",
            [
                ("A cold front (sudden temperature drop, wind shift, pressure trough, and thunderstorm rain)", "جبهة هوائية باردة (هبوط حاد في الحرارة، وتغيّر اتجاه الرياح، وأمطار رعدية)"),
                ("A warm summer heat wave with calm high pressure", "موجة حر صيفية مع ضغط مرتفع مستقر"),
                ("A permanent desert drought lasting 10 years", "جفاف صحراوي مستمر لعشر سنوات"),
                ("A local sea breeze from a calm indoor pool", "نسيم بحر محلي من مسبح مغلق"),
            ],
            "Compare 12:00 PM vs 3:00 PM: temperature plunged 11 °C, wind flipped from South to Northwest, and heavy rain hit!",
            "قارن 12:00 ظهراً بـ 3:00 عصراً: هبطت الحرارة 11 درجة مئوية وانقلب اتجاه الرياح من جنوبية إلى شمالية غربية مع أمطار!",
            "Cold fronts drive dense cold air underneath warm moist air, creating sharp temperature drops, wind shifts, and storms.",
            ["Between 12 PM and 3 PM temperature dropped from 28 °C to 17 °C while pressure rebounded after a trough.", "Abrupt cooling + wind reversal + brief heavy rain is the classic signature of a passing cold front."],
            "Sharp cooling + wind shift + rain = Cold Front.",
            "تندفع الكتلة الباردة الكثيفة أسفل الهواء الدافئ في الجبهة الباردة فتهطل أمطار وتنخفض الحرارة سريعاً.",
            ["انخفضت الحرارة 11°م دفعة واحدة وتبدّل اتجاه الرياح من الجنوب إلى الشمال الغربي مع عاصفة مطرية.", "هذه العلامات تميز عبور جبهة باردة نشطة."],
            "هبوط حرارة + تبدل رياح + مطر = جبهة باردة.",
            svg_data_table(["Time", "Temp", "Pressure", "Wind / Sky"], [["9:00 AM", "26 °C", "1012 hPa", "S / Sunny"], ["12:00 PM", "28 °C", "1006 hPa", "S / Clouds"], ["3:00 PM", "17 °C", "1015 hPa", "NW / Heavy Rain"]], "Midday Weather Changes", [76, 62, 78, 126]),
            svg_data_table(["الوقت", "الحرارة", "الضغط", "الرياح / السماء"], [["9:00 ص", "26 °م", "1012 هـ.ب", "جنوبية / مشمس"], ["12:00 م", "28 °م", "1006 هـ.ب", "جنوبية / غائم"], ["3:00 م", "17 °م", "1015 هـ.ب", "شمال غرب / مطر"]], "تغيرات الطقس في المحطة", [72, 62, 82, 130]),
        ),
        (
            "Abha (at ~2,200 m elevation in the Asir Mountains) and Jazan (near sea level on the coast) sit at nearly the same southern latitude (~17–18° N). Why does Abha enjoy mild ~22 °C summer highs while Jazan frequently tops 38 °C?",
            "تقع مدينة أبها (على ارتفاع ~2200 م في جبال عسير) ومدينة جازان (عند مستوى سطح البحر) على خط عرض متقارب تقريباً (~17–18° شمالاً). لماذا تنعم أبها بصيف لطيف (~22°م) بينما تتجاوز جازان 38°م غالباً؟",
            [
                ("Higher altitude means thinner, lower-pressure air that expands and holds far less warmth", "زيادة الارتفاع تعني هواءً أقل ضغطاً وأرق كثافةً يبرد بالتمدد ويحتفظ بحرارة أقل"),
                ("Abha sits thousands of kilometers closer to the North Pole than Jazan", "تقع أبها أقرب إلى القطب الشمالي بآلاف الكيلومترات من جازان"),
                ("Sunlight completely misses mountaintops above 2,000 meters", "لا يصل ضوء الشمس إلى قمم الجبال فوق 2000 متر"),
                ("Abha has zero carbon dioxide gas in its air", "يخلو هواء أبها تماماً من غاز ثاني أكسيد الكربون"),
            ],
            "Even at the equator, towering mountain peaks hold snow! Temperature falls ~6.5 °C for every 1,000 m gained in elevation.",
            "حتى عند خط الاستواء تتكلل القمم العالية بالثلوج! فكلما ارتفعنا نحو 1000 م تنخفض الحرارة بنحو 6.5°م.",
            "Altitude strongly cools regional climate because air temperature decreases upward through the troposphere.",
            ["Same latitude gives nearly identical incoming solar angles.", "Abha's ~2,200 m elevation lowers average air temperature by roughly 14 °C compared with coastal sea level."],
            "Higher altitude = cooler climate at the same latitude.",
            "يُخفض الارتفاع عن سطح البحر درجات الحرارة بوضوح حتى عند تساوي دوائر العرض.",
            ["بما أن أبها وجازان متقاربتان في خط العرض فزاوية الشمس متقاربة لهما.", "لكن ارتفاع أبها (~2200 م) يجعل هواءها أرقّ وأبرد بنحو 14°م مقارنة بساحل جازان."],
            "الارتفاع العالي = مناخ أبرد.",
            None, None,
        ),
        (
            "Moist winds blowing eastward off the Red Sea climb the steep western slopes of the Asir Mountains, dropping lush rain on western terraced farms while leaving the far eastern leeward side arid desert. What climate pattern is illustrated?",
            "تصعد الرياح الرطبة القادمة من البحر الأحمر المنحدرات الغربية الحادة لجبال عسير فتسقط أمطاراً غزيرة على المدرجات الزراعية، ثم تهبط جافة نحو الصحراء شرق الجبال. ما اسم هذه الظاهرة المناخية؟",
            [
                ("The rain shadow effect", "ظاهرة ظلّ المطر"),
                ("The Coriolis ocean whirlpool effect", "دوامات كوريوليس المحيطية"),
                ("Polar midnight sun heating", "تسخين شمس منتصف الليل القطبية"),
                ("Tidal spring bulge cooling", "تبريد المدّ القمري"),
            ],
            "Moist air rises and cools (raining out on the windward side), leaving a dry 'shadow' on the opposite side!",
            "يصعد الهواء الرطب ويمطر في الجهة المقابلة للبحر، فيسقط خلف الجبل هواءً جافاً يخلق (ظل مطر)!",
            "Mountains wring moisture out of rising windward air, creating wet windward slopes and an arid leeward rain shadow.",
            ["Climbing air expands, cools, condenses, and precipitates along the western mountain face.", "Descending on the eastern side, dry air warms by compression and inhibits clouds → rain shadow."],
            "Wet windward mountain side + dry leeward side = Rain shadow.",
            "تجبر الجبال الهواء الرطب على الصعود والتكثف على جانب وتكوّن منطقة جافة خلفها (ظل المطر).",
            ["يفقد الهواء رطوبته مطراً عند صعوده المنحدر الغربي للجبل.", "عندما يهبط الهواء على السفح الشرقي يكون جافاً ويسخن بالانضغاط فيمنع تكوّن السحب."],
            "مطر في المواجهة وجفاف خلف الجبل = ظل المطر.",
            svg_process_flow(["Moist Wind", "Climbs Peak", "West Rain", "Dry East"], "Orographic Uplift Pattern", "Mountain Rain Shadow"),
            svg_process_flow(["رياح رطبة", "صعود الجبل", "مطر غربي", "جفاف شرقي"], "أثر التضاريس على الهطول", "ظاهرة ظل المطر الجبلية"),
        ),
        (
            "Coastal cities like Dammam or Yanbu experience milder winter nights and slightly lower peak afternoon swings than deep inland desert cities like Hail or Riyadh at comparable latitudes. Why does the nearby sea moderate coastal temperatures?",
            "تشهد المدن الساحلية كالدمام وينبع لياليَ شتوية أدفأ وتقلبات حرارية يومية أقل من المدن الصحراوية الداخلية كحائل والرياض على دوائر عرض متقاربة. لماذا يلطف البحر حرارة السواحل؟",
            [
                ("Water absorbs and releases huge amounts of heat slowly (high specific heat capacity), warming and cooling far more slowly than desert sand and rock", "يمتص الماء ويطلق كميات ضخمة من الحرارة ببطء (سعة حرارية نوعية عالية)، فيسخن ويبرد أبطأ بكثير من رمال الصحراء وصخورها"),
                ("Sea water completely stops sunlight from hitting beaches within 200 km", "يمنع ماء البحر وصول ضوء الشمس تماماً إلى مسافة 200 كم"),
                ("Fish swimming near the coast generate 90% of city heat by friction", "تولّد الأسماك السابحة قرب الشاطئ معظم حرارة المدن بالاحتكاك"),
                ("Desert rock holds 10 times more water than the Arabian Gulf", "تحتفظ صخور الصحراء بكمية ماء أكبر بعشر مرات من الخليج"),
            ],
            "Compare stepping barefoot on hot beach sand vs cool ocean water at noon — sand heats fast and cools fast; water buffers temperature!",
            "قارن حرارة رمل الشاطئ الملتهب ظهراً بماء البحر المعتدل — الرمل يسخن سريعاً ويبرد سريعاً بينما يقاوم الماء التغير المفاجئ!",
            "Oceans stabilize nearby coastal temperatures because liquid water has a very high heat capacity.",
            ["Water takes much more thermal energy per degree of warming than rock or sand, and mixes heat deeply.", "Thus seas release stored warmth on winter nights and absorb heat during hot afternoons."],
            "High heat capacity of ocean water moderates coastal climates.",
            "يعمل البحر كمنظّم حراري للسواحل بفضل السعة الحرارية العالية جداً للماء.",
            ["يحتاج الماء إلى طاقة حرارية أكبر بكثير لترتفع حرارته مقارنة بالصخر والرمل.", "لذا يخزن البحر الحرارة نهاراً وصيفاً ويطلقها ببطء ليلاً وشتاءً ملطفاً جو الساحل."],
            "السعة الحرارية العالية للماء تلطف مناخ السواحل.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in med_b22:
        B.add_concept(tp, "Medium", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Hard (10..14): Pressure gradient wind table, Dew point / Relative humidity math, Weather vs climate reasoning, Station biome matching, Urban heat island chart
    B.add_concept(
        tp, "Hard", bp,
        "A regional forecast table compares surface air pressures between four pairs of towns separated by the exact same 100 km distance. Which town pair will experience the FASTEST winds, and in which direction?",
        "يقارن جدول النشرة الجوية قيم الضغط السطحي بين أربعة أزواج من البلدات تفصل بين كل زوج مسافة 100 كم بالضبط. أي زوج سيشهد أسرع رياح، وفي أي اتجاه ستهب؟",
            [
                ("Pair 3: from Town E (1024 hPa) toward Town F (998 hPa)", "الزوج 3: من البلدة E (1024) نحو البلدة F (998)"),
                ("Pair 3: from Town F (998 hPa) toward Town E (1024 hPa)", "الزوج 3: من البلدة F (998) نحو البلدة E (1024)"),
                ("Pair 1: from Town A (1014 hPa) toward Town B (1012 hPa)", "الزوج 1: من البلدة A (1014) نحو البلدة B (1012)"),
                ("Pair 4: from Town G (1008 hPa) toward Town H (1008 hPa)", "الزوج 4: من البلدة G (1008) نحو البلدة H (1008)"),
            ],
            "Wind ALWAYS blows from HIGH pressure toward LOW pressure, and the BIGGEST pressure difference over 100 km creates the fastest gale!",
            "تهب الرياح دائماً من الضغط المرتفع إلى المنخفض، وأكبر فرق ضغط خلال 100 كم يولد أسرع رياح!",
            "Wind speed scales with the horizontal pressure gradient, flowing from higher to lower pressure.",
            ["Compute pressure drops across 100 km: Pair 1 = 2 hPa, Pair 2 = 6 hPa, Pair 3 = 1024 - 998 = 26 hPa, Pair 4 = 0 hPa.", "Steepest drop (26 hPa) drives strongest wind from High (1024 at E) to Low (998 at F)."],
            "Biggest ΔP (26 hPa) + High→Low = Pair 3 (E → F).",
            "تتناسب سرعة الرياح طردياً مع شدة انحدار الضغط، وتتحرك من الضغط المرتفع إلى المنخفض.",
            ["نحسب فرق الضغط: الزوج 1 = 2، الزوج 2 = 6، الزوج 3 = 1024 - 998 = 26، الزوج 4 = 0.", "الفرق الأكبر (26 هكتوباسكال) يعطي أسرع رياح متجهة من المرتفع E إلى المنخفض F."],
            "أكبر فرق ضغط + من المرتفع للمنخفض = الزوج 3 (من E إلى F).",
            svg_data_table(["Pair", "Town 1 (hPa)", "Town 2 (hPa)", "Drop"], [["1", "A: 1014", "B: 1012", "2 hPa"], ["2", "C: 1018", "D: 1012", "6 hPa"], ["3", "E: 1024", "F: 998", "26 hPa"], ["4", "G: 1008", "H: 1008", "0 hPa"]], "100 km Pressure Gradients", [48, 92, 92, 68]),
            svg_data_table(["الزوج", "البلدة 1", "البلدة 2", "الفرق"], [["1", "A: 1014", "B: 1012", "2 هـ.ب"], ["2", "C: 1018", "D: 1012", "6 هـ.ب"], ["3", "E: 1024", "F: 998", "26 هـ.ب"], ["4", "G: 1008", "H: 1008", "0 هـ.ب"]], "تدرّج الضغط عبر 100 كم", [48, 92, 92, 68]),
    )

    B.add_math(
        tp, "Hard", bp,
        "At 30 °C, one cubic meter of warm air can hold up to 30 g of water vapor at saturation, and currently contains 15 g (50% relative humidity). When night falls and the air cools to 18 °C without losing any water, its maximum capacity drops to 15 g per cubic meter. What does the relative humidity (%) become at 18 °C (when dew or fog starts to form)?",
        "عند 30°م يستوعب المتر المكعب من الهواء الدافئ حتى 30 جم من بخار الماء كحد أقصى، ويحمل حالياً 15 جم فقط (رطوبة نسبية 50%). وعند حلول الليل يبرد الهواء إلى 18°م دون فقد أي ماء، فتنخفض قدرته الاستيعابية القصوى إلى 15 جم/م³. كم تصبح الرطوبة النسبية (%) عند 18°م حيث يبدأ تشكل الندى أو الضباب؟",
        100, [50, 75, 25],
        "Relative Humidity (%) = (Actual water vapor ÷ Maximum capacity at current temperature) × 100%.",
        "الرطوبة النسبية (%) = (كمية البخار الفعلية ÷ أقصى استيعاب عند الحرارة الجديدة) × 100%.",
        "Cooling air at constant moisture raises relative humidity until 100% saturation (dew point) triggers condensation.",
        ["Actual vapor stays 15 g/m³.", "At 18 °C, capacity = 15 g/m³ → RH = (15 ÷ 15) × 100% = 100% (saturated air)."],
        "Check: 15/15 = 1 = 100% saturation → dew/fog condenses.",
        "يبرد الهواء الليلي فتقل سعته لبخار الماء حتى يبلغ نقطة التشبع (100%) فيتكثف الندى.",
        ["الكمية الفعلية للبخار بقيت 15 جم/م³، وسعة الهواء عند 18°م أصبحت 15 جم/م³.", "الرطوبة النسبية = (15 ÷ 15) × 100% = 100%."],
        "تحقق: التشبع التام = 100%.",
        suffix="\\%",
    )

    B.add_concept(
        tp, "Hard", bp,
        "After one unusually snowy week in January, someone claims: 'This cold week proves global long-term warming is completely false.' Which scientific explanation accurately addresses this claim?",
        "بعد أسبوع مثلج غير معتاد في شهر يناير، قال شخص: (هذا الأسبوع البارد يثبت أن الاحترار العالمي طويل الأمد غير صحيح تماماً). ما التفسير العلمي الدقيق الذي يعالج هذا الادعاء؟",
        [
            ("One cold week is local short-term WEATHER, whereas global climate trends are measured by 30+ year planetary temperature averages", "أسبوع بارد واحد يمثّل طقساً محلياً قصير الأمد، أما اتجاهات المناخ فتُقاس بمتوسطات الحرارة العالمية لعشرات السنين"),
            ("One snowy week anywhere automatically lowers Earth's average temperature for the entire century", "أسبوع مثلج واحد في أي مكان يخفض متوسط حرارة الكوكب للقرن كله تلقائياً"),
            ("Snow falls only when greenhouse carbon dioxide completely vanishes from Earth", "لا يتساقط الثلج إلا إذا اختفى ثاني أكسيد الكربون كلياً من الغلاف الجوي"),
            ("Thermometers stop recording climate data below 5 °C", "تتوقف موازين الحرارة عن العمل دون 5 درجات مئوية"),
        ],
        "Distinguish short-term local fluctuations (Weather) from multi-decade global averages (Climate).",
        "فرّق بين التقلب الجوي المحلي القصير (الطقس) والمتوسط الكوكبي عبر العقود (المناخ).",
        "Individual extreme cold or hot days reflect weather variability and cannot confirm or refute multi-decade global climate shifts.",
        ["Even in a warming global climate, cold air outbreaks still occur locally in winter.", "Climate trend evidence relies on thousands of stations averaged over decades worldwide."],
        "One cold snap = Weather; 30-year global record = Climate.",
        "الخلط بين الطقس اليومي والمناخ طويل الأمد يسبّب استنتاجات خاطئة.",
        ["موجات البرد الأسبوعية ظاهرة طقسية عابرة في منطقة محدودة.", "تقييم تغير المناخ يتطلب رصد متوسطات درجات الحرارة في الكوكب كله على مدى 30 عاماً فأكثر."],
        "أسبوع واحد = طقس؛ عقود كوكبية = مناخ.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Four climate stations (W, X, Y, Z) record long-term annual averages in the table. Which station most accurately represents a TROPICAL RAINFOREST climate near the equator?",
        "يسجّل الجدول المتوسطات السنوية طويلة الأمد لأربع محطات مناخية (W و X و Y و Z). أي محطة تمثّل بدقة مناخ الغابات الاستوائية المطيرة قرب خط الاستواء؟",
        [
            ("Station X (high year-round 27 °C warmth and very heavy ~2,450 mm annual rainfall)", "المحطة X (حرارة عالية مستقرة ~27°م طوال العام وأمطار غزيرة جداً ~2450 ملم)"),
            ("Station W (26 °C average, only ~95 mm rain)", "المحطة W (حرارة ~26°م وأمطار شحيحة ~95 ملم)"),
            ("Station Y (-14 °C average, ~180 mm snow/rain)", "المحطة Y (حرارة متجمدة -14°م وأمطار ~180 ملم)"),
            ("Station Z (13 °C cool average, ~780 mm rain)", "المحطة Z (معدل معتدل 13°م وأمطار ~780 ملم)"),
        ],
        "Tropical rainforests need BOTH high year-round warmth (~25–28 °C) AND abundant rainfall (>2,000 mm)!",
        "الغابة الاستوائية المطيرة تجمع بين الدفء الدائم (~25–28°م) والهطول الغزير جداً (>2000 ملم)!",
        "Climate zones combine multi-year temperature and precipitation regimes.",
        ["Station W is a hot arid desert (high temp, ~95 mm rain); Station Y is polar tundra/ice.", "Station X combines constant equatorial warmth (27 °C) with 2,450 mm rainfall → tropical rainforest."],
        "Hot + Wet year-round = Station X.",
        "تُحدَّد الأقاليم المناخية بالجمع بين نمطي الحرارة والأمطار طوال السنة.",
        ["المحطة W حارة وجافة جداً (صحراوي)، والمحطة Y شديدة البرودة (قطبي)، و Z معتدلة.", "المحطة X وحدها تجمع الحرارة الاستوائية المرتفعة (27°م) مع الهطول الكثيف (2450 ملم)."],
        "دفء دائم + أمطار غزيرة = المحطة X.",
        svg_data_table(["Station", "Mean Temp", "Annual Rain"], [["W", "26 °C", "95 mm"], ["X", "27 °C", "2,450 mm"], ["Y", "-14 °C", "180 mm"], ["Z", "13 °C", "780 mm"]], "30-Year Climate Stations", [76, 102, 114]),
        svg_data_table(["المحطة", "متوسط الحرارة", "المطر السنوي"], [["W", "26 °م", "95 ملم"], ["X", "27 °م", "2450 ملم"], ["Y", "-14 °م", "180 ملم"], ["Z", "13 °م", "780 ملم"]], "بيانات مناخية لـ 30 عاماً", [76, 106, 116]),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Urban planners measured midday summer surface temperatures across four parts of a city (see bar chart). Which urban design pair best cools neighborhoods and cuts summer air-conditioning electricity demand?",
        "قاس مخططو المدن درجات حرارة الأسطح في ظهيرة صيف حار عبر أربعة مواقع بالمدينة (كما في الرسم). أي تصميم حضري يخفض حرارة الأحياء ويقلل استهلاك مكيفات الهواء صيفاً على النحو الأفضل؟",
        [
            ("Planting shaded tree parks and coating rooftops with bright white reflective paint (high albedo)", "تشجير المتنزهات المظللة وطلاء الأسقف باللون الأبيض العاكس للحرارة"),
            ("Covering every park with black asphalt and dark tar roofs", "تغطية المتنزهات بالإسفلت الأسود والأسقف بالقطران الداكن"),
            ("Removing shade trees and widening dark stone parking lots", "إزالة الأشجار المظللة وتوسيع مواقف الحجارة الداكنة"),
            ("Replacing white roofs with dark matte iron sheets", "استبدال الأسقف البيضاء بألواح حديدية داكنة"),
        ],
        "Compare Shaded Park (33 °C) and White Roof (37 °C) against Dark Asphalt (58 °C)!",
        "قارن حرارة الحديقة المظللة (33°م) والسقف الأبيض (37°م) بالإسفلت الأسود (58°م)!",
        "High-albedo reflective surfaces and plant shade/transpiration counteract the Urban Heat Island effect.",
        ["Dark asphalt absorbs sunlight and heats to 58 °C, radiating heat into streets all evening.", "Tree shade + transpiration cools parks to 33 °C, while reflective white roofs stay 17 °C cooler than dark tar roofs."],
        "Shade trees + reflective light roofs cool urban heat islands.",
        "يحدّ الغطاء النباتي والأسطح الفاتحة العاكسة من ظاهرة الجزر الحرارية الحضرية.",
        ["يمتص الإسفلت الداكن ضوء الشمس فيلتهب حتى 58°م ويسخّن الأحياء المجاورة.", "أما الأشجار فتظلل وتبرّد الهواء بالنتح (33°م)، والأسطح البيضاء تعكس الإشعاع الشمسي (37°م)."],
        "التشجير + الألوان الفاتحة العاكسة يبردان المدينة.",
        svg_bar_chart([("Asphalt", 58, "#dc2626"), ("Dark Roof", 54, "#ea580c"), ("White Roof", 37, "#0284c7"), ("Tree Park", 33, "#16a34a")], "Temp (°C)", "Urban Surface Heat"),
        svg_bar_chart([("إسفلت", 58, "#dc2626"), ("سقف داكن", 54, "#ea580c"), ("سقف أبيض", 37, "#0284c7"), ("حديقة شجر", 33, "#16a34a")], "الحرارة (°م)", "حرارة أسطح المدينة ظهراً"),
    )


def _add_b23(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B23"

    # Easy (0..4): Rotation vs Day/Night, Revolution 365.25d, 23.5 deg tilt seasons diagram, Shortest shadow noon chart, Opposite hemispheres
    easy_b23 = [
        (
            "What motion of Earth makes the Sun appear to rise in the east, arc across the sky, and set in the west, producing the daily cycle of day and night?",
            "أي حركة للأرض تجعل الشمس تبدو وكأنها تشرق من الشرق وتعبر السماء ثم تغرب في الغرب، مسببةً تعاقب الليل والنهار؟",
            [
                ("Earth's rotation (spinning) on its axis once every 24 hours from west to east", "دوران الأرض حول محورها دورة كاملة كل 24 ساعة من الغرب إلى الشرق"),
                ("Earth's yearly revolution around the Sun in 365 days", "دوران الأرض السنوي حول الشمس خلال 365 يوماً"),
                ("The Moon revolving around Earth every 29.5 days", "دوران القمر حول الأرض كل 29.5 يوماً"),
                ("Earth's axis changing direction every afternoon", "تغير اتجاه محور الأرض كل عصر"),
            ],
            "Spinning like a top from west to east makes the stationary Sun appear to move east to west!",
            "دوران الأرض حول نفسها من الغرب إلى الشرق يجعل الشمس الساكنة تبدو متحركة من الشرق للغرب!",
            "Earth's 24-hour west-to-east axial rotation produces day, night, and apparent solar motion.",
            ["At any moment, the half facing the Sun experiences daytime and the opposite half experiences night.", "Because Earth spins eastward, horizons sweep toward sunrise in the east."],
            "24 h axis spin = Day and Night.",
            "ينتج تعاقب الليل والنهار والحركة الظاهرية للشمس عن دوران الأرض المحوري خلال 24 ساعة.",
            ["يواجه نصف الأرض المضيء الشمس فيكون نهاراً، بينما يغرق النصف الآخر في الليل.", "ولأن الأرض تدور من الغرب إلى الشرق نرى الشمس تشرق من الشرق وتغرب في الغرب."],
            "الدوران المحوري اليومي (24 ساعة) = الليل والنهار.",
            None, None,
        ),
        (
            "Roughly how long does it take Earth to complete ONE full revolution (orbit) around the Sun?",
            "كم تستغرق الأرض تقريباً لتكمل دورة مدارية واحدة كاملة حول الشمس؟",
            [
                ("About 365.25 days (one Earth year)", "نحو 365.25 يوماً (سنة أرضية واحدة)"),
                ("24 hours (one day)", "24 ساعة (يوم واحد)"),
                ("29.5 days (one lunar month)", "29.5 يوماً (شهر قمري واحد)"),
                ("12 hours (half a rotation)", "12 ساعة (نصف دورة)"),
            ],
            "Every 4 years those extra 0.25 days add up to 1 full day (February 29, leap day)!",
            "كل 4 سنوات تتجمع الأرباع الزائدة (0.25 × 4) لتضيف يوماً كاملاً في السنة الكبيسة!",
            "Earth's orbital revolution around the Sun takes ~365.25 days, defining one calendar year.",
            ["Rotation (spinning on axis) = 24 hours.", "Revolution (orbiting the Sun) = 365.25 days."],
            "1 orbit around Sun = 1 year ≈ 365.25 days.",
            "تستغرق دورة الأرض الكاملة في مدارها حول الشمس نحو 365.25 يوماً وتعرّف السنة الشمسية.",
            ["الدوران حول المحور يوم (24 ساعة)، أما الدوران في المدار حول الشمس فسنة (365.25 يوماً).", "ويعالج ربع اليوم الإضافي بإضافة يوم كل أربع سنوات (السنة الكبيسة)."],
            "الدورة المدارية = سنة ≈ 365.25 يوماً.",
            None, None,
        ),
        (
            "As illustrated in the diagram, Earth's rotational axis leans at about 23.5° relative to its orbit as it revolves around the Sun. What fundamental cycle does this constant tilt plus revolution produce?",
            "كما يظهر في الشكل، يميل محور دوران الأرض بنحو 23.5° عن العمودي أثناء دورانها حول الشمس. ما الدورة الأساسية التي يسببها هذا الميلان الثابت مع الحركة المدارية؟",
            [
                ("The four seasons (Spring, Summer, Autumn, Winter)", "الفصول الأربعة (الربيع والصيف والخريف والشتاء)"),
                ("The 24-hour alternation of sunrise and sunset alone", "تعاقب الشروق والغروب كل 24 ساعة وحده"),
                ("Sudden high and low ocean waves every hour", "الأمواج البحرية اليومية كل ساعة"),
                ("Earthquakes along the Red Sea rift", "الزلازل على امتداد صدع البحر الأحمر"),
            ],
            "Look at the two hemispheres: one leans into direct solar rays while the other gets slanted rays!",
            "انظر إلى نصفي الكرة الأرضية: أحدهما يميل نحو الأشعة العمودية المباشرة والآخر يتلقى أشعة مائلة!",
            "Earth's 23.5° axial tilt combined with revolution causes seasonal changes in sun angle and day length.",
            ["Without axial tilt, every day of the year would have nearly constant sunlight angle.", "With a 23.5° tilt, each hemisphere alternates leaning toward (summer) and away from (winter) the Sun."],
            "23.5° Tilt + Orbit = Four Seasons.",
            "يسبب ميل محور الأرض الثابت (23.5°) مع دورانها حول الشمس تعاقب الفصول الأربعة.",
            ["يتبدّل ميل نصفي الكرة نحو الشمس أو بعيداً عنها عبر مدار السنة.", "يغير ذلك زاوية سقوط الأشعة وطول النهار فتتوالى الفصول الأربعة."],
            "الميلان 23.5° + المدار السنوي = الفصول الأربعة.",
            svg_tilt_seasons("Sun", "N: Away (Winter)", "S: Toward (Sum)", "Sunlight", "Earth's 23.5° Axial Tilt"),
            svg_tilt_seasons("الشمس", "الشمال: يميل بعيداً", "الجنوب: نحو الشمس", "أشعة الشمس", "ميل محور الأرض 23.5°"),
        ),
        (
            "Students measured the length of a 1.5 m flagpole's shadow in a schoolyard on a sunny day and graphed the results. At which time was the Sun HIGHEST in the sky, producing the shortest shadow?",
            "قاس طلاب طول ظل سارية علم ارتفاعها 1.5 م في ساحة المدرسة خلال يوم مشمس ورسموا النتائج. في أي وقت كانت الشمس في أعلى ارتفاع لها بالسماء فأنتجت أقصر ظل؟",
            [
                ("12:15 PM (Solar Noon)", "12:15 ظهراً (الزوال الشمسي)"),
                ("7:00 AM (Early Morning)", "7:00 صباحاً (الصباح الباكر)"),
                ("4:30 PM (Late Afternoon)", "4:30 عصراً (قبل الغروب)"),
                ("Midnight (12:00 AM)", "12:00 منتصف الليل"),
            ],
            "Think of a flashlight shining nearly straight down vs shining low from the side!",
            "تخيّل مصباحاً يضيء عمودياً من الأعلى مقارنة بإضاءة منخفضة من الجانب!",
            "Shadow length varies inversely with Sun altitude: low morning/evening sun casts long shadows; high noon sun casts short shadows.",
            ["At 7:00 AM and 4:30 PM the low Sun throws long shadows (3.8 m and 3.4 m).", "Near solar noon (12:15 PM) the overhead Sun produces the shortest shadow (0.4 m)."],
            "Highest Sun = Shortest Shadow (Noon).",
            "يتناسب طول الظل عكسياً مع ارتفاع الشمس في السماء.",
            ["عند الصباح الباكر والعصر تكون الشمس منخفضة قريبة من الأفق فيمتد الظل طويلاً.", "عند الظهر ترتفع الشمس إلى أقصى نقطة فيكون الظل أقصر ما يمكن (0.4 م)."],
            "أعلى ارتفاع للشمس = أقصر ظل (الظهيرة).",
            svg_bar_chart([("7:00 AM", 3.8, "#ea580c"), ("12:15 PM", 0.4, "#16a34a"), ("4:30 PM", 3.4, "#2563eb")], "Shadow (m)", "Flagpole Shadow Length"),
            svg_bar_chart([("7:00 ص", 3.8, "#ea580c"), ("12:15 م", 0.4, "#16a34a"), ("4:30 م", 3.4, "#2563eb")], "الظل (م)", "طول ظل السارية خلال اليوم"),
        ),
        (
            "In late June, students in Riyadh (Northern Hemisphere) experience long sunny summer days around 43 °C. At the exact same date in June, what season are students experiencing in Sydney, Australia (Southern Hemisphere)?",
            "في أواخر شهر يونيو يعيش طلاب الرياض (في نصف الكرة الشمالي) أيام صيف طويلة وحرارة نحو 43°م. في التاريخ نفسه من شهر يونيو، أي فصل يعيشه طلاب مدينة سيدني في أستراليا (في نصف الكرة الجنوبي)؟",
            [
                ("Winter", "الشتاء"),
                ("Summer", "الصيف"),
                ("Autumn transition from September", "خريف سبتمبر"),
                ("Equinox spring heat", "ربيع الاعتدال"),
            ],
            "When Earth's North Pole tilts TOWARD the Sun in June, the South Pole must tilt AWAY from the Sun!",
            "عندما يميل القطب الشمالي نحو الشمس في يونيو، فإن القطب الجنوبي يميل مبتعداً عنها في الوقت نفسه!",
            "Northern and Southern Hemispheres always experience opposite seasons.",
            ["In June, Northern Hemisphere receives direct rays and long daylight (Summer).", "Simultaneously, Southern Hemisphere leans away receiving slanted rays and short days (Winter)."],
            "North Summer = South Winter.",
            "يتعاكس الفصلان بين نصفي الكرة الأرضية الشمالي والجنوبي دائماً.",
            ["في يونيو يتجه النصف الشمالي نحو الشمس فتسود أجواء الصيف في المملكة.", "وفي اللحظة نفسها يميل النصف الجنوبي بعيداً عن الشمس فتعيش أستراليا فصل الشتاء."],
            "صيف الشمال = شتاء الجنوب.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b23:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): Perihelion/Aphelion distance misconception table, Tilt seasons diagram reading, Rotation degrees math, Riyadh shadow direction, Latitude daylight table
    B.add_concept(
        tp, "Medium", bp,
        "Astronomical data in the table shows that Earth is actually CLOSEST to the Sun (~147 million km) in early January and FARTHEST (~152 million km) in early July! How does this table refute the common misconception that 'summer happens when Earth moves closer to the Sun'?",
        "تُظهر بيانات الفلك في الجدول أن الأرض تكون في أقرب مسافة من الشمس (~147 مليون كم) في أوائل يناير، وفي أبعد مسافة (~152 مليون كم) في أوائل يوليو! كيف تدحض هذه الأرقام الفكرة الخاطئة القائلة بأن (الصيف يحدث لاقتراب الأرض من الشمس)؟",
        [
            ("In January Earth is closest to the Sun yet the Northern Hemisphere has cold winter, and in July Earth is farthest yet has hot summer — proving axial tilt, not distance, causes seasons", "في يناير تكون الأرض أقرب ما يمكن للشمس ومع ذلك يسود شتاء بارد في النصف الشمالي، وفي يوليو تكون أبعد ويسود الصيف — ما يثبت أن الميل المحوري هو السبب لا المسافة"),
            ("In January sunlight takes 10 years to reach Earth so winter arrives slowly", "يستغرق ضوء الشمس عشر سنوات للوصول في يناير"),
            ("The Sun shrinks to half its heat energy every July", "تنكمش حرارة الشمس إلى النصف في شهر يوليو"),
            ("Both hemispheres always have summer in January when Earth is closest", "يشهد نصفا الكرة الصيف معاً في يناير بسبب القرب من الشمس"),
        ],
        "Compare the distance row and Riyadh season row for January vs July!",
        "قارن بين المسافة وفصل الرياض في يناير مقابل يوليو!",
        "Orbital eccentricity (~3%) is too small to drive seasons; axial tilt controls solar concentration and day length.",
        ["If distance controlled seasons, January would be Earth-wide summer and both hemispheres would have identical seasons.", "Actually January = closest to Sun AND Northern winter (tilt away), proving tilt governs seasons."],
        "Closest in Jan (Northern winter) disproves the distance myth!",
        "تثبت القياسات الفلكية أن المسافة ليست سبب الفصول، بل ميل المحور البالغ 23.5°.",
        ["لو كان القرب من الشمس سبب الصيف لكان يناير حاراً في الرياض ولكان الفصل واحداً في نصفي الأرض.", "الواقع أن الأرض أقرب في يناير وقت شتاء الشمال، وأبعد في يوليو وقت صيفه الحار."],
        "القرب في يناير يدحض خرافة المسافة.",
        svg_data_table(["Date", "Sun Distance", "Riyadh Season"], [["Jan 4", "147 M km (Closest)", "Winter"], ["Jul 4", "152 M km (Farthest)", "Summer"]], "Earth Orbit Distance Data", [68, 146, 98]),
        svg_data_table(["التاريخ", "البعد عن الشمس", "فصل الرياض"], [["4 يناير", "147 م.كم (الأقرب)", "شتاء"], ["4 يوليو", "152 م.كم (الأبعد)", "صيف"]], "بيانات بعد الأرض عن الشمس", [72, 144, 96]),
    )

    B.add_concept(
        tp, "Medium", bp,
        "In the tilted Earth diagram shown, the Northern Hemisphere leans TOWARD the Sun while the Southern Hemisphere leans AWAY. Which two conditions accurately describe the Northern Hemisphere on that day?",
        "في رسم الأرض المائلة الموضح، يميل نصف الكرة الشمالي نحو الشمس بينما يميل النصف الجنوبي بعيداً عنها. أي وصفين ينطبقان بدقة على نصف الكرة الشمالي في ذلك اليوم؟",
        [
            ("More direct concentrated sunlight and MORE than 12 hours of daylight (Summer)", "أشعة شمس مباشرة أكثر تركيزاً ونهار أطول من 12 ساعة (الصيف)"),
            ("Very slanted spread-out sunlight and LESS than 12 hours of daylight (Winter)", "أشعة مائلة متفرقة ونهار أقصر من 12 ساعة (الشتاء)"),
            ("Complete 24-hour darkness across all latitudes", "ظلام تام لمدة 24 ساعة في كل خطوط العرض"),
            ("Equal 12-hour daylight and 12-hour night at every pole", "تساوي 12 ساعة نهاراً و12 ساعة ليلاً عند القطبين"),
        ],
        "When a hemisphere tilts toward the Sun, the Sun rises higher in the sky and stays above the horizon longer!",
        "عندما يميل النصف نحو الشمس ترتفع الشمس عالياً وتبقى فوق الأفق ساعات أطول!",
        "Tilting toward the Sun yields steeper sunlight angles (high heating per m²) and extended daylight duration.",
        ["Direct rays concentrate energy over a smaller ground area.", "The illuminated arc spans more than half the latitude circle → >12 hours of daylight (Summer Solstice)."],
        "Toward Sun = high sun angle + long days = Summer.",
        "الميل نحو الشمس يجمع عاملين للصيف: أشعة مركزة ونهاراً طويلاً.",
        ["تسقط الأشعة بزاوية قريبة من العمودية فتتركز طاقتها على مساحة أصغر.", "كما يقطع النهار أكثر من نصف دائرة العرض فيتجاوز 12 ساعة."],
        "نحو الشمس = أشعة مركزة + نهار طويل = الصيف.",
        svg_tilt_seasons("Sun", "N: Toward Sun", "S: Away", "Direct Rays", "June Solstice Alignment"),
        svg_tilt_seasons("الشمس", "الشمال: نحو الشمس", "الجنوب: بعيداً", "أشعة مباشرة", "وضع الانقلاب الصيفي"),
    )

    B.add_math(
        tp, "Medium", bp,
        "Earth rotates one full 360° circle on its axis every 24 hours (15° per hour). If Riyadh's solar noon occurs 3 hours earlier than London's solar noon due to Earth spinning eastward, how many degrees of longitude roughly separate Riyadh and London?",
        "تدور الأرض دورة كاملة مقدارها 360° حول محورها كل 24 ساعة (أي 15° في الساعة). إذا سبق وقت الظهر الشمسي في الرياض نظيره في لندن بنحو 3 ساعات بسبب دوران الأرض نحو الشرق، فبكم درجة طول جغرافية تقريباً تفصل بين الرياض ولندن؟",
        45, [15, 30, 90],
        "Multiply Earth's rotation rate (15° per hour) by the 3-hour difference!",
        "اضرب سرعة دوران الأرض (15° لكل ساعة) في فرق الساعات (3 ساعات)!",
        "Time zones trace Earth's uniform 15°/hour rotation speed.",
        ["Rotation speed = 360° ÷ 24 h = 15°/h.", "3 hours × 15°/h = 45° longitude difference (London ~0°, Riyadh ~46.7° E)."],
        "Check: 45° ÷ 15°/h = 3 hours.",
        "تقابل كل ساعة زمنية بين المدن تغيراً مقداره 15 درجة على خطوط الطول.",
        ["معدل الدوران = 360° ÷ 24 ساعة = 15°/ساعة.", "فرق 3 ساعات × 15° = 45° طول (لندن ~0°، الرياض ~46.7° شرقاً)."],
        "تحقق: 45° ÷ 15° = 3 ساعات.",
        suffix="^{\\circ}",
    )

    B.add_concept(
        tp, "Medium", bp,
        "At 8:00 AM on a clear autumn morning in Riyadh, the Sun shines low from the East-Southeast. Toward which general compass direction does a student's shadow point on the schoolyard ground?",
        "في الساعة 8:00 من صباح خريف صافٍ في الرياض، تشرق الشمس منخفضة من جهة الشرق المائل للجنوب. نحو أي اتجاه عام يمتد ظل الطالبة على ساحة المدرسة؟",
        [
            ("West (slightly Northwest), directly opposite the Sun", "نحو الغرب (الشمال الغربي قليلاً)، في الاتجاه المعاكس لموقع الشمس تماماً"),
            ("East, pointing straight toward the rising Sun", "نحو الشرق، مشيراً مباشرة نحو الشمس الصاعدة"),
            ("Straight upward into outer space", "عمودياً للأعلى نحو الفضاء"),
            ("Shadows vanish completely before 9:00 AM", "تختفي الظلال تماماً قبل التاسعة صباحاً"),
        ],
        "An opaque person blocks light traveling FROM the Sun — so the shadow falls AWAY from the Sun!",
        "الجسم المعتم يحجب الضوء الآتي من الشمس — لذا يقع الظل دائماً في الجهة المقابلة للشمس!",
        "Shadows always extend away from the light source along the line of incoming rays.",
        ["At 8:00 AM, sunlight travels from East-Southeast toward West-Northwest.", "Blocking those rays casts a long morning shadow toward the West / Northwest."],
        "Morning Sun in East → Shadow points West.",
        "يمتد الظل دائماً على امتداد الأشعة المحجوبة في الاتجاه المعاكس لمصدر الضوء.",
        ["تأتي أشعة الشمس صباحاً من الشرق نحو الغرب.", "وبذلك يمتد ظل الأجسام طويلاً نحو الغرب والشمال الغربي."],
        "الشمس شرقاً ← الظل غرباً.",
        None, None,
    )

    B.add_concept(
        tp, "Medium", bp,
        "The table records December 21 daylight hours at four Northern and Equatorial latitudes. Why does Quito (at the Equator, 0°) stay near 12 hours of daylight even in December, whereas Tromsø (69° N) drops to 0 hours?",
        "يسجل الجدول ساعات النهار في 21 ديسمبر عند أربع دوائر عرض. لماذا تبقى ساعات النهار في كيتو (عند خط الاستواء 0°) قريبة من 12 ساعة في ديسمبر، بينما تهبط في ترومسو (69° شمالاً) إلى صفر ساعة؟",
        [
            ("Earth's day-night boundary always bisects the Equator into equal halves all year, whereas in December the tilted North Polar circle stays entirely inside Earth's dark shadow", "خط الفاصل بين الليل والنهار ينصّف خط الاستواء بالتساوي طوال السنة، بينما تبقى الدائرة القطبية الشمالية المائلة بعيداً غارقة في ظل الأرض في ديسمبر"),
            ("Quito floats 50 km closer to Mars during winter", "تطفو مدينة كيتو أقرب إلى المريخ بـ 50 كم شتاءً"),
            ("Tromsø turns off all ocean reflections every winter", "تطفئ ترومسو انعكاسات المحيط في الشتاء"),
            ("Earth stops spinning north of 60° N every December", "تتوقف الأرض عن الدوران شمال خط 60° في ديسمبر"),
        ],
        "Notice how daylight drops steadily as latitude increases from 0° to 69° N in winter!",
        "لاحظ تناقص ساعات النهار تدريجياً كلما اتجهنا شمالاً من 0° إلى 69° شمالاً في الشتاء!",
        "Equatorial latitude experiences uniform ~12 h day/night year-round while polar daylight varies from 0 h to 24 h.",
        ["Any great circle (the day-night terminator) cuts the Equator (another great circle) strictly in half (12 h day, 12 h night).", "Far north latitudes above 66.5° N miss the sunlit side completely during December solstice (Polar Night)."],
        "Equator = ~12 h always; Polar Circle = 0 h in midwinter / 24 h in midsummer.",
        "ينصّف خط الليل والنهار خطَّ الاستواء دائماً (12 ساعة نهار)، بينما يغيب النهار تماماً داخل الدائرة القطبية في ذروة الشتاء.",
        ["في 21 ديسمبر يميل القطب الشمالي مبتعداً عن الشمس، فتدور المناطق شمال 66.5° بالكامل في الظل (0 ساعة نهار).", "أما خط الاستواء فيقسمه حد الإضاءة نصفين متساويين في كل الفصول."],
        "خط الاستواء: ~12 ساعة دائماً؛ القطب في ديسمبر: 0 ساعة.",
        svg_data_table(["City", "Latitude", "Dec 21 Daylight"], [["Quito", "0° Equator", "12.1 hrs"], ["Riyadh", "25° N", "10.6 hrs"], ["Oslo", "60° N", "5.9 hrs"], ["Tromsø", "69° N", "0.0 hrs"]], "Dec 21 Daylight by Latitude", [76, 100, 126]),
        svg_data_table(["المدينة", "دائرة العرض", "نهار 21 ديسمبر"], [["كيتو", "0° الاستواء", "12.1 ساعة"], ["الرياض", "25° شمالاً", "10.6 ساعة"], ["أوسلو", "60° شمالاً", "5.9 ساعة"], ["ترومسو", "69° شمالاً", "0.0 ساعة"]], "ساعات النهار حسب دائرة العرض", [74, 108, 124]),
    )

    # Hard (10..14): Flashlight beam angle experiment, Zero tilt hypothetical, Rotation proof (Foucault/star trails), Equinox geometry, Solar panel tilt chart
    B.add_concept(
        tp, "Hard", bp,
        "A student shines an identical flashlight beam from 30 cm away onto graph paper at two angles (see table). At 90° (overhead) the light illuminates 4 squares brightly; at 30° (slanted) the SAME beam spreads across 8 squares. How does this experiment explain cold polar winters?",
        "وجّهت طالبة حزمة مصباح يدوي متماثلة من مسافة 30 سم على ورق مربعات بزاويتين مختلفتين (انظر الجدول). عند 90° أضاءت 4 مربعات بسطوع، وعند 30° انتشرت الحزمة نفسها على 8 مربعات. كيف تشرح هذه التجربة برودة الشتاء والقطبين؟",
        [
            ("Slanted sunlight spreads identical energy over a wider ground area, giving each square meter far less heat", "تنتشر الأشعة المائلة فتوزع كمية الطاقة نفسها على مساحة أرض أوسع، فيأخذ كل متر مربع حرارة أقل بكثير"),
            ("Slanted light turns into cold snow waves before hitting the paper", "تتحول الأشعة المائلة إلى موجات ثلجية باردة قبل ملامسة الورق"),
            ("At 30° the flashlight battery loses 90% of its electricity instantly", "تفقد بطارية المصباح 90% من كهربائها عند إمالته 30°"),
            ("Overhead 90° light leaves twice as much area dark on the table", "تترك الأشعة العمودية 90° مساحة مظلمة أكبر تحت المصباح"),
        ],
        "Total beam power is fixed: spreading 100 units across 8 squares leaves only 12.5 per square instead of 25!",
        "طاقة الشعاع ثابتة: توزيع 100 وحدة على 8 مربعات يعطي كل مربع نصف النصيب فقط مقارنة بـ 4 مربعات!",
        "Lower solar elevation angles dilute solar flux across larger surface areas, reducing warming per square meter.",
        ["At 90°: 100% power ÷ 4 squares = 25% power per square.", "At 30°: 100% power ÷ 8 squares = 12.5% power per square → half the warming intensity."],
        "Wider area = diluted solar intensity = cooler climate.",
        "كلما مالت زاوية سقوط الأشعة تقلصت الطاقة الواصلة لكل وحدة مساحة من السطح.",
        ["الكمية الكلية لضوء المصباح لم تتغير، لكنها عند الميل 30° توزعت على ضعف المساحة (8 مربعات بدل 4).", "ينطبق المبدأ نفسه على أشعة الشمس المائلة شتاءً وعند القطبين."],
        "اتساع المساحة يقلل تركيز الحرارة لكل متر مربع.",
        svg_data_table(["Beam Angle", "Lit Squares", "Energy / Square"], [["90° (Direct)", "4", "High (25 units)"], ["30° (Slanted)", "8", "Half (12.5 units)"]], "Light Angle Investigation", [102, 86, 124]),
        svg_data_table(["زاوية الشعاع", "المربعات المضاءة", "الطاقة لكل مربع"], [["90° (عمودي)", "4", "عالية (25 وحدة)"], ["30° (مائل)", "8", "النصف (12.5 وحدة)"]], "استقصاء زاوية سقوط الضوء", [102, 92, 124]),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Imagine a hypothetical planet like Earth whose axis has ZERO degrees (0°) tilt relative to its orbit around the Sun, while still spinning every 24 hours and orbiting in 365 days. How would day/night and seasons work on that world?",
        "تخيّل كوكباً شبيهاً بالأرض لكن ميل محوره يساوي صفراً (0°) دون أي انحراف، مع استمرار دورانه اليومي كل 24 ساعة ومداره السنوي في 365 يوماً. كيف سيكون الليل والنهار والفصول على هذا الكوكب؟",
        [
            ("Day and night would still alternate every 24 hours and the equator would stay warmer than the poles, but seasonal shifts and changing day lengths would disappear everywhere", "سيتعاقب الليل والنهار كل 24 ساعة ويبقى الاستواء أدفأ من القطبين، لكن تعاقب الفصول وتغير طول النهار سيختفيان في كل مكان"),
            ("One side of the planet would stay permanently frozen in midnight darkness forever", "سيبقى نصف الكوكب متجمداً في ظلام منتصف الليل إلى الأبد"),
            ("Every latitude from equator to poles would have identical 50 °C summer heat", "ستتساوى حرارة الصيف عند القطبين والاستواء عند 50°م"),
            ("Years would become only 24 hours long", "ستصبح السنة الواحدة 24 ساعة فقط"),
        ],
        "Ask separately: Does 0° tilt stop the 24h spin? NO! Does curved planet still slant light near poles? YES! Does sun angle change from January to July? NO!",
        "اسأل كل جزء على حدة: هل يوقف الميل 0° الدوران اليومي؟ لا! هل يغير انحناء الكوكب عند القطبين؟ لا! هل تتبدل الفصول من يناير ليوليو؟ لا!",
        "Axial rotation creates day/night; planetary curvature creates latitude heat zones; axial tilt creates seasons.",
        ["Because the planet still spins every 24 h, day (~12 h) and night (~12 h) continue daily everywhere.", "Because Earth stays curved, Equator (90°) stays hot and poles (~0°) stay cold, YET neither pole ever tilts closer/farther from January to July → zero seasons!"],
        "0° tilt = still day/night and hot equator/cold poles, NO seasons.",
        "انعدام الميل المحوري يلغي الفصول الأربعة وتغير طول النهار مع بقاء الليل والنهار والمناخ المتدرج من الاستواء للقطبين.",
        ["الدوران اليومي يبقي تعاقب الليل والنهار، وكروية الكوكب تُبقي الاستواء حاراً والقطبين باردين.", "لكن مع انعدام الميلان يظل ارتفاع الشمس ثابتاً طوال السنة في أي مدينة فلا تتعاقب الفصول."],
        "ميل 0° = ليل ونهار دون فصول سنوية.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "A museum suspends a heavy brass Foucault pendulum from a tall dome ceiling and sets it swinging straight North–South. Over 6 hours, visitors watch its swing trace slowly drift across a floor dial, AND at night time-lapse cameras show northern stars tracing circles around Polaris (the North Star). What do BOTH observations prove?",
        "علّق متحف رقاص فوكو ثقيلاً من سقف قبة مرتفعة ودفعه ليتأرجح في اتجاه شمال–جنوب. بعد 6 ساعات لاحظ الزوار انحراف مسار تأرجحه تدريجياً على القرص الأرضي، كما التقطت الكاميرات ليلاً دوران النجوم حول النجم القطبي. ماذا يثبت كلا الرصدين معاً؟",
        [
            ("Earth itself is physically rotating underneath the swinging pendulum and under our sky", "الأرض نفسها تدور فعلياً حول محورها تحت الرقاص المتأرجح وتحت قبة السماء"),
            ("Earth stands completely motionless while the Sun pulls brass pendulums magnetically", "الأرض ساكنة تماماً بينما تجذب الشمس الرقاصات مغناطيسياً"),
            ("Only Polaris moves in tiny circles while stars stand still", "النجم القطبي وحده يدور في دوائر صغيرة بينما تظل الأرض ثابتة"),
            ("Earth orbits the Moon once every 6 hours", "تدور الأرض حول القمر مرة كل 6 ساعات"),
        ],
        "A freely hanging pendulum keeps swinging in its true plane in space while the floor beneath it turns with Earth!",
        "يحتفظ الرقاص الحر بمستوى تأرجحه في الفضاء بينما تدور أرضية المتحف تحته مع دوران الأرض!",
        "Foucault's pendulum and circumpolar star trails provide direct mechanical and astronomical proof of Earth's rotation.",
        ["By inertia, the swinging pendulum plane stays fixed relative to distant space while Earth turns beneath it.", "Equally, Earth's axial spin aimed near Polaris makes night stars appear to wheel steadily around it."],
        "Both prove Earth's axial rotation directly.",
        "يوفر رقاص فوكو ومسارات النجوم الدائرية دليلاً تجريبياً وفلكياً مباشراً على دوران الأرض حول نفسها.",
        ["يحافظ الرقاص بالقصور الذاتي على اتجاه تأرجحه، لكن دوران الأرض تحته يظهر انحرافاً تدريجياً للمسار.", "وبالمثل يسبب دوران المحور الموجه نحو النجم القطبي التفاف النجوم ظاهرياً حوله ليلاً."],
        "كلاهما برهان مباشر على دوران الأرض حول محورها.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Twice each year — on the Vernal Equinox (around March 20) and Autumnal Equinox (around September 22) — what is true about Earth's axial tilt relative to the Sun and daylight across the globe?",
        "مرتين في العام — عند الاعتدال الربيعي (نحو 20 مارس) والاعتدال الخريفي (نحو 22 سبتمبر) — ما الذي يتحقق لميل محور الأرض بالنسبة للشمس وساعات النهار حول العالم؟",
        [
            ("Neither pole tilts toward nor away from the Sun, placing the Sun directly overhead at the Equator and giving roughly 12 hours of daylight everywhere", "لا يميل أي من القطبين نحو الشمس ولا بعيداً عنها، فتتعامد الشمس على خط الاستواء ويتساوى الليل والنهار بنحو 12 ساعة في كل مكان"),
            ("The North Pole tilts 23.5° straight toward the Sun giving 24-hour summer", "يميل القطب الشمالي 23.5° نحو الشمس فيسود نهار 24 ساعة"),
            ("The South Pole gets zero sunlight for 48 hours straight", "تنقطع الشمس عن القطب الجنوبي 48 ساعة متواصلة"),
            ("Earth slows its orbital speed to zero for one full day", "تتوقف الأرض في مدارها يوماً كاملاً"),
        ],
        "Equi-nox literally means 'Equal Night' (~12 h day, ~12 h night everywhere on Earth)!",
        "كلمة الاعتدال تعني تساوي الليل والنهار (~12 ساعة نهار و~12 ساعة ليل في كل بقاع الأرض)!",
        "At equinoxes Earth's tilt leans sideways relative to the Earth–Sun line, distributing sunlight equally to both hemispheres.",
        ["Both hemispheres receive identical solar energy on an equinox.", "Sun shines straight down onto 0° Equator, yielding ~12 h day and ~12 h night at all non-polar latitudes."],
        "Equinox = equal ~12 h day/night + Sun overhead at Equator.",
        "في الاعتدالين يكون اتجاه ميل المحور جانبياً بالنسبة لخط الشمس والأرض، فتتساوى حصة نصفي الكرة.",
        ["تتعامد الشمس على خط الاستواء 0°، وينقسم الكوكب بالعدل بين النهار (~12 ساعة) والليل (~12 ساعة).", "يحدث ذلك حول 20 مارس و22 سبتمبر سنوياً."],
        "الاعتدال = 12 ساعة نهار/ليل وتعامد على الاستواء.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Engineers tested three fixed tilt angles for rooftop solar panels in Riyadh (latitude 24.7° N) across an entire year and recorded annual energy output in the chart. Why did the 25° South-facing tilt outperform both flat (0°) and steep (65°) mounts?",
        "اختبر مهندسون ثلاث زوايا ميل ثابتة لألواح شمسية فوق سطح في الرياض (دائرة عرض 24.7° شمالاً) طوال سنة كاملة ورسموا الإنتاج السنوي. لماذا تفوّق الميل 25° المتجه جنوباً على الوضع الأفقي (0°) والمائل بشدة (65°)؟",
        [
            ("Matching panel tilt roughly to local latitude (25°) faces the average annual Sun elevation straight-on, maximizing concentrated energy over the year", "مواءمة زاوية اللوح مع خط العرض (~25°) تجعله عمودياً تقريباً على متوسط ارتفاع الشمس السنوي، مما يعظّم تركيز الطاقة طوال العام"),
            ("Tilting at 25° blocks all afternoon sunlight so panels stay cooler at 0 °C", "الميل 25° يحجب شمس العصر فتبرد الألواح إلى الصفر"),
            ("A 25° tilt captures moonlight energy at 2:00 AM", "يلتقط الميل 25° طاقة ضوء القمر في الثانية فجراً"),
            ("Flat 0° panels slide off solar photons completely", "تنزلق فوتونات الشمس عن الألواح الأفقية 0° ولا تدخلها"),
        ],
        "Because Riyadh is 24.7° north of the Equator, the average midday Sun sits ~25° south of directly overhead!",
        "لأن الرياض تقع على عرض 24.7° شمال الاستواء، فإن متوسط ارتفاع الشمس السنوي يميل جنوباً بنحو 25°!",
        "Optimal fixed solar collector tilt approximates local latitude facing toward the equator (south in Northern Hemisphere).",
        ["At 24.7° N, tilting a panel 25° toward the southern sky minimizes average solar incidence angle over winter and summer.", "0° loses winter noon energy; 65° loses summer overhead energy → 25° achieves peak annual output."],
        "Best year-round fixed solar tilt ≈ local latitude (~25°).",
        "تقارب أفضل زاوية ميل سنوية ثابتة للألواح الشمسية قيمة خط عرض المدينة باتجاه الجنوب في النصف الشمالي.",
        ["في الرياض (24.7° شمالاً) يقلّل الميل 25° جنوباً خسارة زاوية السقوط خلال الصيف والشتاء معاً.", "الوضع المسطح يخسر شتاءً والحاد 65° يخسر صيفاً، فيحقق الميل 25° أعلى إنتاج سنوي (2150 ك.و.س)."],
        "أفضل ميل سنوي ثابت ≈ خط العرض (~25°).",
        svg_bar_chart([("0° Flat", 1920, "#ea580c"), ("25° South", 2150, "#16a34a"), ("65° Steep", 1680, "#2563eb")], "kWh / yr", "Riyadh Solar Panel Output"),
        svg_bar_chart([("0° أفقي", 1920, "#ea580c"), ("25° جنوباً", 2150, "#16a34a"), ("65° حاد", 1680, "#2563eb")], "ك.و.س/سنة", "إنتاج الألواح الشمسية بالرياض"),
    )


def _add_b24(B: G6SciBankBuilder) -> None:
    tp, bp = "Earth & Space Sciences", "G6-SCI-B24"

    # Easy (0..4): Why Moon has phases, Full Moon diagram, New Moon diagram, Solar eclipse diagram, Inner rocky vs Outer giant planets
    easy_b24 = [
        (
            "Why does the Moon shine in the night sky and appear to change shape from crescent to full circle over about a month?",
            "لماذا يضيء القمر في سماء الليل ويبدو شكله متغيراً من هلال إلى بدر كامل خلال شهر تقريباً؟",
            [
                ("The Moon reflects sunlight, and as it orbits Earth we see different fractions of its sunlit half", "يعكس القمر ضوء الشمس، ومع دورانه حول الأرض نرى أجزاءً متغيرة من نصفه المضاء بالشمس"),
                ("The Moon burns nuclear hydrogen gas like a smaller green star", "يحرق القمر غاز الهيدروجين النووي مثل نجم صغير مضيء بذاته"),
                ("Earth's shadow covers part of the Moon every single night of the month", "يغطي ظل الأرض جزءاً من القمر في كل ليلة من ليالي الشهر"),
                ("Clouds floating in space hide half of the Moon until summer", "تحجب سحب فضائية نصف القمر حتى حلول الصيف"),
            ],
            "Moonlight is reflected sunlight! Half the Moon is ALWAYS sunlit; only our viewing angle from Earth changes as the Moon orbits.",
            "نور القمر انعكاس لضوء الشمس! فنصفه مضاء دائماً، وما يتغير أثناء دورانه حولنا هو زاوية رؤيتنا لذلك النصف المضاء.",
            "Lunar phases arise from changing viewing geometry of the Moon's sunlit hemisphere along its orbit.",
            ["Always 50% of the Moon faces the Sun and glows.", "Depending on where the Moon sits around Earth, Earth observers see 0% (New), 50% (Quarter), or 100% (Full) of that lit side."],
            "Reflected sunlight + orbital viewing angle = Lunar phases.",
            "لا يولّد القمر ضوءاً ذاتياً بل يعكس ضوء الشمس، وتنشأ أطواره من تغيّر موضعه بالنسبة للأرض والشمس.",
            ["نصف القمر المواجه للشمس مضاء دائماً، بينما تتغير الزاوية التي نراه بها من الأرض خلال الشهر.", "لا يسبب ظل الأرض الأطوار العادية؛ بل يسبب الخسوف النادر فقط."],
            "ضوء منعكس + دوران حول الأرض = أطوار القمر.",
            None, None,
        ),
        (
            "Look at the highlighted position in the lunar phase diagram where Earth sits between the Sun and the Moon, allowing us to see the entire sunlit face. What is this phase called?",
            "انظر إلى الموضع المظلّل بالأزرق في مخطط أطوار القمر حيث تقع الأرض بين الشمس والقمر فنرى كامل الوجه المضاء للقمر. ماذا يُسمى هذا الطور؟",
            [
                ("Full Moon", "البدر الكامل"),
                ("New Moon", "المحاق"),
                ("First Quarter", "التربيع الأول"),
                ("Waning Crescent", "الهلال المتناقص (الأخير)"),
            ],
            "Wait: the entire sunlit half faces straight back toward Earth like a bright round disc!",
            "النصف المضاء كله يواجه الأرض فيبدو قرصاً مضيئاً مستديراً بالكامل!",
            "Full Moon occurs when the Moon is opposite the Sun in Earth's sky, showing 100% of its lit near side.",
            ["Sun → Earth → Moon puts the sunlit face squarely toward nighttime Earth.", "Therefore observers see a bright round Full Moon rising near sunset."],
            "Opposite the Sun = Full Moon.",
            "يحدث طور البدر الكامل عندما يكون القمر في الجهة المقابلة للشمس بالنسبة للأرض.",
            ["يواجه الوجه المضيء للقمر الأرضَ بكامله في هذه الوضعية.", "نرى حينها قرصاً مضاءً كاملاً يشرق قرابة الغروب."],
            "مقابل الشمس = بدر كامل.",
            *_moon_svgs("Full Moon", "بدر كامل", "Lunar Orbit Position", "موقع القمر في مداره"),
        ),
        (
            "In the highlighted orbital position directly BETWEEN Earth and the Sun, the Moon's lit side faces away toward the Sun while its dark side faces Earth. What phase is this?",
            "في الموضع المظلّل مباشرةً بين الأرض والشمس، يتجه الوجه المضاء من القمر نحو الشمس بينما يواجه وجهه المظلم الأرضَ. ما هذا الطور؟",
            [
                ("New Moon", "المحاق"),
                ("Full Moon", "البدر الكامل"),
                ("Third Quarter", "التربيع الأخير"),
                ("Waxing Gibbous", "الأحدب المتزايد"),
            ],
            "When the unlit half faces us in the daytime sky, the Moon is nearly invisible — the start of a new lunar month!",
            "عندما يواجهنا النصف المظلم يختفي القمر تقريباً في بداية الشهر القمري الجديد!",
            "New Moon occurs between Sun and Earth when the unlit lunar hemisphere faces Earth.",
            ["Sun illuminates the far side facing away from Earth.", "A thin waxing crescent appears a day or two later as the Moon moves onward."],
            "Between Sun and Earth = New Moon.",
            "يقع طور المحاق عندما يكون القمر بين الشمس والأرض فلا يرى المشاهد وجهه المضاء.",
            ["تضيء الشمس الجانب البعيد من القمر المواجه لها، بينما يتجه الجانب المظلم نحونا.", "بعد يوم أو يومين يبدأ الهلال الجديد بالظهور."],
            "بين الشمس والأرض = المحاق.",
            *_moon_svgs("New Moon", "محاق", "Start of Lunar Cycle", "بداية الدورة القمرية"),
        ),
        (
            "Examine the alignment diagram showing Sun → Moon → Earth in one straight line so the Moon casts its dark shadow onto Earth's surface. Which rare celestial event is depicted?",
            "تأمّل مخطط الاصطفاف الذي يظهر فيه اصطفاف الشمس ← القمر ← الأرض على خط مستقيم بحيث يلقي القمر بظله على سطح الأرض. ما الظاهرة الفلكية النادرة الممثلة هنا؟",
            [
                ("A solar eclipse (can occur only at New Moon)", "كسوف الشمس (ويحدث في طور المحاق فقط)"),
                ("A lunar eclipse (Earth blocking sunlight from the Moon)", "خسوف القمر (حجب الأرض ضوء الشمس عن القمر)"),
                ("A meteor shower burning in Earth's upper sky", "زخة شهب تحترق في أعلى الغلاف الجوي"),
                ("Earth's daily sunset at 6:00 PM", "غروب الشمس اليومي عند السادسة مساءً"),
            ],
            "Which object blocks the Sun? Notice the small gray Moon is in the MIDDLE casting shadow onto Earth!",
            "أي جرم يحجب الشمس هنا؟ لاحظ أن القمر الرمادي الصغير في الوسط يلقي ظله على الأرض!",
            "A solar eclipse occurs when the New Moon crosses directly between Sun and Earth, blocking the Sun briefly.",
            ["Middle body = Moon; Shadow falls on Earth.", "People inside that shadow see the Moon cover the Sun (Solar Eclipse)."],
            "Sun → Moon → Earth = Solar Eclipse.",
            "يحدث كسوف الشمس عند وقوع القمر في الوسط تماماً بين الشمس والأرض خلال المحاق.",
            ["يحجب القمر ضوء الشمس ويلقي مخروط ظله على بقعة ضيقة من سطح الأرض.", "عند وقوع الأرض في الوسط يكون الحدث خسوفاً للقمر لا كسوفاً للشمس."],
            "القمر في الوسط = كسوف الشمس.",
            svg_eclipse_diagram("solar", "Sun", "Moon", "Earth", "Solar Alignment Diagram"),
            svg_eclipse_diagram("solar", "الشمس", "القمر", "الأرض", "مخطط اصطفاف الكسوف"),
        ),
        (
            "In our solar system, the four inner planets (Mercury, Venus, Earth, Mars) differ sharply from the four outer planets (Jupiter, Saturn, Uranus, Neptune). Which pair accurately describes each group?",
            "تختلف الكواكب الأربعة الداخلية (عطارد والزهرة والأرض والمريخ) اختلافاً كبيراً عن الكواكب الأربعة الخارجية (المشتري وزحل وأورانوس ونبتون). أي وصف يميّز المجموعتين بدقة؟",
            [
                ("Inner planets are small, dense, and rocky; outer planets are huge, low-density gas and ice giants with rings", "الكواكب الداخلية صغيرة وكثيفة وصخرية؛ والخارجية عملاقة قليلة الكثافة غازية وجليدية ولها حلقات"),
                ("Inner planets are made entirely of frozen methane gas; outer planets are tiny iron rocks", "الداخلية مكونة من غاز الميثان المتجمد؛ والخارجية صخور حديدية صغيرة"),
                ("Only the four inner planets possess bright ring systems", "تمتلك الكواكب الداخلية وحدها أنظمة حلقات ساطعة"),
                ("Outer planets orbit faster around the Sun than Mercury", "تدور الكواكب الخارجية حول الشمس أسرع من عطارد"),
            ],
            "Close to the hot young Sun, only heavy rock and iron could condense; far out past the frost line, giant icy/gaseous worlds formed!",
            "قرب الشمس الساخنة بقيت الصخور والمعادن الثقيلة لتصنع الكواكب الصخرية، وبعيداً في البرودة تجمعت الغازات والثلوج لصنع العمالقة!",
            "Solar-system formation sorted terrestrial rocky inner planets from massive gas/ice outer giants.",
            ["Inner terrestrial: Mercury, Venus, Earth, Mars — solid rocky crusts, few/no moons, no rings.", "Outer Jovian: Jupiter, Saturn, Uranus, Neptune — giant H/He/ice worlds, many moons, ring systems."],
            "Inner = Small Rocky; Outer = Huge Gas/Ice Giants.",
            "تنقسم كواكب المجموعة الشمسية إلى داخلية صخرية وخارجية عملاقة غازية وجليدية.",
            ["الكواكب الداخلية صغيرة ذات سطح صلب وكثافة عالية وأقمار قليلة أو معدومة.", "الكواكب الخارجية ضخمة غازية/جليدية وتدور حولها عشرات الأقمار والحلقات."],
            "الداخلية = صخرية صغيرة؛ الخارجية = عمالقة غازية وجليدية.",
            None, None,
        ),
    ]
    for qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar in easy_b24:
        B.add_concept(tp, "Easy", bp, qen, qar, pairs, hen, har, ien, sen, cen, iar, sar, car, den, dar)

    # Medium (5..9): First Quarter diagram, Lunar eclipse red moon diagram, Lunar 28-day math, Venus greenhouse table, Spring vs Neap tides
    B.add_concept(
        tp, "Medium", bp,
        "About one week after New Moon, the Moon sits at a 90° angle relative to the Earth–Sun line (highlighted in the diagram). Viewed from the Northern Hemisphere, half its disc is illuminated on the right side. Which phase is this?",
        "بعد نحو أسبوع واحد من المحاق يصنع القمر زاوية قائمة 90° مع خط الشمس–الأرض (كما هو مظلّل في الشكل)، فيبدو نصف قرصه الأيمن مضاءً في نصف الكرة الشمالي. ما اسم هذا الطور؟",
        [
            ("First Quarter", "التربيع الأول"),
            ("Third (Last) Quarter", "التربيع الأخير"),
            ("Full Moon", "البدر الكامل"),
            ("New Moon", "المحاق"),
        ],
        "It has completed ONE-QUARTER of its orbit around Earth and is waxing (growing) toward Full Moon!",
        "قطع القمر ربع مداره الأول حول الأرض وهو في مرحلة التزايد متجهاً نحو البدر!",
        "First Quarter appears one-quarter way through the lunar orbit (~7 days post-New Moon), 50% sunlit.",
        ["At top position (counterclockwise orbit from New Moon), the lit half is waxing toward Full Moon.", "This 90° geometry ~7 days after New Moon is called First Quarter."],
        "1 week after New Moon (90° waxing) = First Quarter.",
        "يظهر التربيع الأول بعد نحو سبعة أيام من المحاق عند إتمام ربع الدورة المدارية.",
        ["في هذه الوضعية نرى نصف النصف المضاء أي ربع القمر الكلي مضيئاً ومتزايداً.", "تكتمل نصف الدورة لاحقاً عند البدر، ثم ثلاثة أرباعها عند التربيع الأخير."],
        "ربع الدورة الأول المتزايد = التربيع الأول.",
        *_moon_svgs("First Quarter", "التربيع الأول", "One Quarter Orbit", "ربع المدار القمري"),
    )

    B.add_concept(
        tp, "Medium", bp,
        "During the lunar eclipse alignment shown (Sun → Earth → Moon), Earth blocks direct sunlight, yet the Moon often glows a faint coppery-red instead of turning pitch black. Why does red light still reach the Moon?",
        "خلال اصطفاف خسوف القمر الموضح (الشمس ← الأرض ← القمر) تحجب الأرض ضوء الشمس المباشر، ومع ذلك يميل لون القمر غالباً إلى النحاسي المحمر بدلاً من السواد التام. لماذا يصل الضوء الأحمر إلى القمر؟",
        [
            ("Earth's atmosphere scatters short blue light away and bends (refracts) long red sunlight wavelengths inward onto the Moon", "الغلاف الجوي للأرض يشتّت الضوء الأزرق القصير ويكسر الأشعة الحمراء الطويلة نحو القمر"),
            ("The Moon activates volcanic lava fountains on its entire surface during eclipses", "تثور البراكين على كامل سطح القمر وقت الخسوف فجأة"),
            ("Solar flares turn Earth into a giant red mirror at midnight", "تحول التوهجات الشمسية الأرض إلى مرآة حمراء منتصف الليل"),
            ("Red light travels 10 times faster than blue light so it overtakes Earth's shadow", "يسير الضوء الأحمر أسرع بعشر مرات من الأزرق فيسبق ظل الأرض"),
        ],
        "Think of red sunsets on Earth! Sunlight skims around the rim of Earth's atmosphere into the shadow cone.",
        "تذكّر لون الشفق الأحمر عند الغروب! تمر أشعة الشمس عبر حافة الغلاف الجوي للأرض وتنكسر نحو ظل القمر.",
        "Atmospheric scattering removes blue light while refraction bends sunset-red wavelengths into Earth's umbra.",
        ["Sunlight passing through the rim of Earth's atmosphere loses blue wavelengths by scattering (making sky blue).", "Remaining longer red rays refract around Earth's edge onto the eclipsed Moon, turning it copper-red."],
        "Refracted sunset light through Earth's air = coppery eclipsed Moon.",
        "تسبب ظاهرة انكسار وتشتت الضوء في الغلاف الجوي للأرض توهج القمر باللون النحاسي وقت الخسوف الكلي.",
        ["عند مرور أشعة الشمس بحافة جو الأرض تتشتت الأشعة الزرقاء، بينما تنكسر الأشعة الحمراء الطويلة نحو القمر.", "كأن القمر يشاهد شروق وغروب الشمس على كامل محيط الأرض دفعة واحدة."],
        "تشتت الأزرق + انكسار الأحمر في جو الأرض = القمر النحاسي.",
        svg_eclipse_diagram("lunar", "Sun", "Earth", "Moon", "Lunar Eclipse Alignment"),
        svg_eclipse_diagram("lunar", "الشمس", "الأرض", "القمر", "مخطط اصطفاف الخسوف"),
    )

    B.add_math(
        tp, "Medium", bp,
        "Using a simplified 28-day lunar cycle model (exactly 7 days between New Moon → First Quarter → Full Moon → Third Quarter → next New Moon), if a New Moon occurs on Day 2 of a month, on what day of that same month will the THIRD QUARTER Moon appear?",
        "باستخدام نموذج مبسّط للدورة القمرية مدته 28 يوماً (7 أيام بالضبط بين كل طور رئيسي: المحاق ← التربيع الأول ← البدر ← التربيع الأخير ← المحاق التالي)، إذا حدث المحاق في اليوم 2 من الشهر، ففي أي يوم من الشهر نفسه يظهر التربيع الأخير؟",
        23, [9, 16, 30],
        "Count how many 7-day quarter steps lie from New Moon to Third Quarter (3 steps = 21 days) and add to Day 2!",
        "احسب عدد الفترات من المحاق إلى التربيع الأخير (3 فترات × 7 أيام = 21 يوماً) ثم أضفها إلى اليوم 2!",
        "Each primary quarter phase spans roughly one-fourth of the ~28–29.5 day synodic lunar cycle.",
        ["Day 2 + 7 = Day 9 (First Quarter).", "Day 9 + 7 = Day 16 (Full Moon).", "Day 16 + 7 = Day 23 (Third Quarter)."],
        "Check: 2 + 3 × 7 = 23.",
        "يمثل كل طور رئيسي ربع الدورة القمرية تقريباً (نحو 7 أيام في النموذج المبسط).",
        ["اليوم 2 (محاق) + 7 = 9 (تربيع أول) + 7 = 16 (بدر).", "16 + 7 = 23 (التربيع الأخير)."],
        "تحقق: 2 + (3 × 7) = 23.",
        suffix="",
    )

    B.add_concept(
        tp, "Medium", bp,
        "Study the rocky-planet data table. Although Mercury orbits almost TWICE as close to the Sun (0.39 AU) as Venus (0.72 AU), why is Venus hotter day and night (464 °C average) than Mercury (167 °C average)?",
        "ادرس جدول الكواكب الصخرية. رغم أن عطارد يدور حول الشمس على مسافة تقارب نصف بعد الزهرة (0.39 مقابل 0.72 وحدة فلكية)، فلماذا تبلغ حرارة الزهرة 464°م ليلاً ونهاراً متجاوزةً عطارد (167°م)؟",
        [
            ("Venus has a crushing, super-thick carbon dioxide (CO2) atmosphere creating an extreme runaway greenhouse effect that traps heat", "يمتلك الزهرة غلافاً جوياً كثيفاً جداً من ثاني أكسيد الكربون يولّد احتباساً حرارياً جامحاً يحبس الحرارة باستمرار"),
            ("Venus has a solid inner glacier burning with oxygen fires", "يحتوي الزهرة على جليد صلب يشتعل بالأكسجين"),
            ("Mercury orbits inside dark clouds that block all sunlight forever", "يدور عطارد داخل سحب سوداء تحجب الشمس للأبد"),
            ("Venus orbits closer to the Sun than Mercury does", "يدور الزهرة أقرب للشمس من عطارد"),
        ],
        "Look at the 'Atmosphere' column: Mercury has virtually none to hold night warmth; Venus is wrapped in ~90 atm of CO2!",
        "انظر إلى عمود الغلاف الجوي: يكاد عطارد يخلو منه، بينما يلفّ الزهرة غلاف كثيف جداً من CO2 يحبس الحرارة!",
        "Atmospheric composition and greenhouse trapping can outweigh solar distance in setting planetary surface temperature.",
        ["Mercury's thin exosphere lets its night side plunge to -180 °C, lowering its average temperature.", "Venus's dense 96% CO2 atmosphere traps infrared thermal energy globally at ~464 °C."],
        "Runaway CO2 greenhouse makes Venus hottest of all planets.",
        "قد يغلب أثر الغلاف الجوي والاحتباس الحراري عاملَ القرب من الشمس في تحديد حرارة الكوكب.",
        ["بلا غلاف جوي يبرد ليل عطارد بشدة فينخفض متوسط حرارته إلى 167°م.", "أما غلاف الزهرة الكثيف من CO2 فيحبس الحرارة ليلاً ونهاراً رافعاً حرارته إلى 464°م (الأشد حرارة بين الكواكب)."],
        "الاحتباس الحراري الهائل لغاز CO2 يجعل الزهرة الكوكب الأشد حرارة.",
        svg_data_table(["Planet", "Distance", "Atmosphere", "Mean Temp"], [["Mercury", "0.39 AU", "Near None", "167 °C"], ["Venus", "0.72 AU", "Thick CO2", "464 °C"], ["Earth", "1.00 AU", "N2 + O2", "15 °C"], ["Mars", "1.52 AU", "Thin CO2", "-65 °C"]], "Inner Planet Temperatures", [72, 74, 86, 82]),
        svg_data_table(["الكوكب", "البعد", "الغلاف الجوي", "متوسط الحرارة"], [["عطارد", "0.39 و.ف", "شبه معدوم", "167 °م"], ["الزهرة", "0.72 و.ف", "CO2 كثيف", "464 °م"], ["الأرض", "1.00 و.ف", "N2 + O2", "15 °م"], ["المريخ", "1.52 و.ف", "CO2 رقيق", "-65 °م"]], "حرارة الكواكب الداخلية", [68, 76, 88, 86]),
    )

    B.add_concept(
        tp, "Medium", bp,
        "During which two lunar phases do the gravitational pulls of BOTH the Sun and the Moon pull along the SAME straight line to create extra-high and extra-low OCEAN TIDES (Spring tides)?",
        "في أي طورين من أطوار القمر تجتمع قوتا جاذبية الشمس والقمر معاً على خط مستقيم واحد لتصنعا أعلى مدّ وأدنى جزر في المحيطات (المدّ الربيعي / الأعظمي)؟",
        [
            ("New Moon and Full Moon", "المحاق والبدر الكامل"),
            ("First Quarter and Third Quarter only", "التربيع الأول والتربيع الأخير فقط"),
            ("Only during the March 20 Equinox regardless of phase", "في الاعتدال الربيعي فقط مهما كان طور القمر"),
            ("Only when Mars aligns behind Saturn", "عند اصطفاف المريخ خلف زحل فقط"),
        ],
        "When Sun–Earth–Moon form a 180° straight line, solar and lunar tidal bulges reinforce each other!",
        "عندما تصطف الشمس والأرض والقمر على خط مستقيم تتضاعف موجتا المد الشمسي والقمري معاً!",
        "Spring tides occur twice a month at New and Full Moons (aligned gravities); weaker Neap tides occur at Quarter phases (90° offset).",
        ["At New Moon and Full Moon, Moon and Sun align along the same axis → reinforcing tidal bulges (Spring tide).", "At 90° First/Third Quarter, pulls partially cancel → moderate Neap tide."],
        "Straight line (New & Full) = Spring tides; 90° (Quarters) = Neap tides.",
        "يحدث المدّ الأعظمي مرتين شهرياً عند اصطفاف الأجرام الثلاثة في طوري المحاق والبدر.",
        ["في المحاق والبدر تجتمع جاذبية الشمس والقمر على محور واحد فتعظم حركة المد والجزر.", "أما في التربيعين فتكون الزاوية قائمة 90° فتقل سعة المد (المدّ الأصغري)."],
        "استقامة (محاق وبدر) = مدّ أعظمي؛ تعامد 90° (تربيعان) = مدّ أصغري.",
        None, None,
    )

    # Hard (10..14): 5-degree tilted moon orbit & eclipse rarity, Kepler orbital period table, Venus rotation > year puzzle, Solar vs Lunar eclipse visibility width, Airless moon thermal swings
    B.add_concept(
        tp, "Hard", bp,
        "If a New Moon passes between Sun and Earth every month and a Full Moon lies opposite the Sun every month, why do we NOT experience a solar eclipse and a lunar eclipse every single month?",
        "إذا كان القمر يمر بين الشمس والأرض كل شهر في المحاق، ويقف في الجهة المقابلة كل شهر في البدر، فلماذا لا يحدث كسوف للشمس وخسوف للقمر كل شهر؟",
        [
            ("The Moon's orbital plane is tilted by about 5° relative to Earth's orbit around the Sun, so shadows usually pass just above or below Earth and Moon", "يميل مستوى مدار القمر بنحو 5° عن مستوى مدار الأرض حول الشمس، لذا يمر الظل غالباً فوق الأرض أو القمر أو تحتهما"),
            ("Earth's shadow disappears completely for 11 months every year", "يختفي ظل الأرض تماماً لمدة 11 شهراً في السنة"),
            ("Sunlight curves vertically through empty vacuum to dodge the Moon", "ينحني ضوء الشمس في الفراغ ليتجنب الاصطدام بالقمر"),
            ("The Moon stops orbiting around Earth every odd-numbered month", "يتوقف القمر عن الدوران حول الأرض في الأشهر الفردية"),
        ],
        "Think in 3D instead of a flat 2D sheet! If two tilted hoops cross at only two nodes, shadows line up only during 'eclipse seasons'.",
        "فكّر في الفضاء ثلاثي الأبعاد لا على ورقة مسطحة! ميلان مدار القمر بـ 5° يجعل ظله يخطئ الأرض في معظم الشهور.",
        "Eclipses require BOTH New/Full phase AND crossing an orbital node due to the Moon's 5° orbital tilt.",
        ["Most months, the New Moon sits slightly above or below the Sun-Earth line → shadow misses Earth.", "Only roughly twice per year when New or Full Moon occurs near the intersection nodes can eclipses happen."],
        "5° tilted Moon orbit explains why eclipses are rare!",
        "يميل مدار القمر بنحو 5° عن مدار الأرض حول الشمس، فلا تصطف الأجرام الثلاثة بدقة إلا نادراً.",
        ["في أغلب الشهور يمر القمر عند المحاق أعلى أو أسفل الخط الواصل بين الشمس والأرض فلا يقع ظله علينا.", "لا يحدث الكسوف أو الخسوف إلا عند تزامن المحاق أو البدر مع نقطة تقاطع المدارين (العقدتين)."],
        "ميل المدار القمري 5° هو سر ندرة الكسوف والخسوف.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Observe the planetary orbit data table. As distance from the Sun grows from 0.39 AU (Mercury) to 9.5 AU (Saturn), orbital period leaps from 0.24 years to 29.5 years! What TWO physical reasons explain why outer planets take vastly longer to orbit?",
        "تأمّل جدول مدارات الكواكب. مع ازدياد البعد عن الشمس من 0.39 وحدة فلكية (عطارد) إلى 9.5 (زحل)، تقفز مدة السنة المدارية من 0.24 سنة إلى 29.5 سنة! ما السببان الفيزيائيان اللذان يفسران طول سنوات الكواكب البعيدة؟",
        [
            ("Outer planets travel a much LONGER circular circumference AND move SLOWER because solar gravity weakens with distance", "تقطع الكواكب البعيدة مداراً أطول بكثير، وتتحرك بسرعة أبطأ لأن جاذبية الشمس تضعف مع البعد"),
            ("Outer planets travel faster than Mercury but make 50 vertical loops around Jupiter", "تتحرك الكواكب البعيدة أسرع من عطارد لكنها تلف 50 دورة حول المشتري"),
            ("Saturn stops orbiting for 6 months every time it crosses winter", "يتوقف زحل عن الدوران ستة أشهر كل شتاء"),
            ("Orbital circumference shrinks outward while solar gravity grows stronger", "يتقلص محيط المدار كلما ابتعدنا وتزداد جاذبية الشمس"),
        ],
        "Period = Distance ÷ Speed: the numerator (circumference) gets huge AND the denominator (speed) gets smaller!",
        "الزمن = المسافة ÷ السرعة: المسافة (المحيط) تكبر جداً، والسرعة تقل بضعف الجاذبية!",
        "Kepler's 3rd Law reflects both expanding orbital path length and diminishing orbital speed at greater solar distances.",
        ["Mercury travels at ~47 km/s around a small 0.39 AU circle → 88 days.", "Saturn travels at only ~9.7 km/s around a giant 9.5 AU circle → 29.5 Earth years!"],
        "Longer track + weaker gravity (slower speed) = much longer year.",
        "يزداد زمن الدورة المدارية بعاملين متآزرين: طول المسار وضعف سرعة الجذب.",
        ["المسار الأبعد أكبر محيطاً بكثير (المسافة = 2πr).", "كما تضعف جاذبية الشمس مع البعد فتقل السرعة المدارية للكوكب، مما يضاعف زمن إتمام الدورة."],
        "مدار أطول + حركة أبطأ = سنة أطول بكثير.",
        svg_data_table(["Planet", "Distance", "Speed", "Orbit Period"], [["Mercury", "0.39 AU", "47 km/s", "0.24 yr"], ["Earth", "1.00 AU", "30 km/s", "1.00 yr"], ["Jupiter", "5.20 AU", "13 km/s", "11.9 yr"], ["Saturn", "9.54 AU", "9.7 km/s", "29.5 yr"]], "Solar Orbit Speed & Period", [74, 72, 74, 86]),
        svg_data_table(["الكوكب", "البعد", "السرعة", "مدة الدورة"], [["عطارد", "0.39 و.ف", "47 كم/ث", "0.24 سنة"], ["الأرض", "1.00 و.ف", "30 كم/ث", "1.00 سنة"], ["المشتري", "5.20 و.ف", "13 كم/ث", "11.9 سنة"], ["زحل", "9.54 و.ف", "9.7 كم/ث", "29.5 سنة"]], "سرعة المدار ومدة السنة", [72, 72, 74, 88]),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Astronomical measurements show that Venus takes 225 Earth days to complete ONE orbit around the Sun, yet takes 243 Earth days to spin ONCE on its axis (retrograde!). What astonishing calendar fact follows directly from the table?",
        "تُظهر القياسات الفلكية أن كوكب الزهرة يكمل دورة واحدة حول الشمس في 225 يوماً أرضياً، بينما يستغرق دورانه المحوري الواحد 243 يوماً أرضياً! ما النتيجة المدهشة المترتبة مباشرة على ذلك؟",
        [
            ("One axial spin (sidereal day) on Venus lasts LONGER than Venus's entire orbital year!", "الدورة المحورية الواحدة للزهرة أطول من سنته المدارية الكاملة حول الشمس!"),
            ("Venus has 365 sunrises every single Earth hour", "تشرق الشمس على الزهرة 365 مرة كل ساعة أرضية"),
            ("Venus completes 10 orbits before spinning even 1 degree", "يكمل الزهرة 10 مدارات قبل أن يدور درجة واحدة"),
            ("A year on Venus lasts longer than Jupiter's 12-year orbit", "سنة الزهرة أطول من سنة المشتري البالغة 12 عاماً"),
        ],
        "Compare 243 days (1 spin on axis = sidereal day) vs 225 days (1 orbit around Sun = year)!",
        "قارن بين 243 يوماً (دورة حول المحور) و225 يوماً (دورة حول الشمس = السنة)!",
        "Rotation period (day) and orbital period (year) are completely independent motions.",
        ["On Earth: day (1 d) << year (365.25 d).", "On Venus: spin period (243 Earth days) > orbital year (225 Earth days) → spin takes longer than a Venusian year!"],
        "243 > 225 → Venus's spin period exceeds its orbital year.",
        "حركة الكوكب حول نفسه وحركته حول الشمس مستقلتان عن بعضهما.",
        ["يتم الزهرة دورته حول الشمس في 225 يوماً أرضياً (سنته)، بينما يستغرق دورانه حول محوره 243 يوماً أرضياً.", "إذن يدور حول الشمس أسرع مما يدور حول محوره."],
        "243 > 225 ← الدوران المحوري للزهرة أطول من سنته.",
        svg_data_table(["Planet", "1 Axis Spin", "1 Solar Orbit"], [["Earth", "1.0 Earth day", "365.25 days"], ["Mars", "1.03 Earth days", "687 days"], ["Venus", "243 Earth days", "225 days"], ["Jupiter", "0.41 Earth days", "4,333 days"]], "Planetary Day vs Year", [74, 114, 114]),
        svg_data_table(["الكوكب", "دورة محورية", "سنة مدارية"], [["الأرض", "1.0 يوم أرضي", "365.25 يوماً"], ["المريخ", "1.03 يوم أرضي", "687 يوماً"], ["الزهرة", "243 يوماً أرضياً", "225 يوماً"], ["المشتري", "0.41 يوم أرضي", "4333 يوماً"]], "اليوم المحوري مقابل السنة", [74, 116, 112]),
    )

    B.add_concept(
        tp, "Hard", bp,
        "Why can an ENTIRE half of Earth watch a total lunar eclipse for over an hour, whereas a total SOLAR eclipse is visible only along a narrow ~100 km ribbon on Earth for just a few minutes?",
        "لماذا يستطيع نصف الكرة الأرضية بالكامل مشاهدة خسوف القمر الكلي لأكثر من ساعة، بينما لا يُرى الكسوف الكلي للشمس إلا ضمن شريط ضيق عرضه نحو 100 كم لبضع دقائق فقط؟",
        [
            ("Earth is about 4× wider than the Moon, casting a huge shadow that swallows the whole Moon, whereas the small Moon casts only a tiny pinhole shadow tip onto Earth", "قطر الأرض أكبر بنحو 4 مرات من قطر القمر فتُلقي ظلاً ضخماً يبتلع القمر كله، بينما لا يلقي القمر الصغير سوى طرف ظل ضيق جداً على الأرض"),
            ("The Moon moves 1,000 times faster during solar eclipses than during lunar eclipses", "يتحرك القمر أسرع بألف مرة أثناء الكسوف مقارنة بالخسوف"),
            ("Oceans absorb solar eclipses everywhere except deserts", "تمتص المحيطات كسوف الشمس في كل مكان عدا الصحاري"),
            ("Lunar eclipses actually happen inside Earth's atmosphere at 50 km height", "يحدث خسوف القمر فعلياً داخل الغلاف الجوي على ارتفاع 50 كم"),
        ],
        "Compare the size of the shadow-caster in each event: tiny Moon (3,474 km wide) vs huge Earth (12,742 km wide)!",
        "قارن حجم الجسم المُسبّب للظل في الحالتين: القمر الصغير (3474 كم) مقابل الأرض الكبيرة (12742 كم)!",
        "Relative sizes of Earth and Moon govern umbra footprint size and eclipse duration.",
        ["Lunar eclipse: giant Earth shadow easily covers the entire Moon, so everyone on Earth's night side sees it at once.", "Solar eclipse: Moon's tapering umbra touches Earth as a narrow moving spot (~100 km wide) sweeping fast."],
        "Earth ~4× Moon width → huge lunar-eclipse shadow vs tiny solar-eclipse spot.",
        "يتحكم الفرق الكبير بين قطري الأرض والقمر في اتساع منطقة المشاهدة ومدتها.",
        ["يغمر ظل الأرض الواسع القمر بأكمله فيراه كل من هم في النصف الليلي للأرض في الوقت نفسه.", "أما مخروط ظل القمر الصغير فيلامس الأرض كبقعة ضيقة (~100 كم) تعبر سطح الأرض بسرعة خلال دقائق."],
        "ظل الأرض كبير للخسوف؛ وظل القمر نقطة صغيرة للكسوف.",
        None, None,
    )

    B.add_concept(
        tp, "Hard", bp,
        "Astronauts' equipment on the Moon endures blistering +120 °C heat during lunar daytime and plunging -170 °C cold at lunar night — a nearly 300 °C temperature swing! Why are temperature swings so extreme on the Moon compared with Earth?",
        "تواجه معدات رواد الفضاء على سطح القمر حرارة حارقة تبلغ +120°م في نهار القمر وبرداً قارساً يصل إلى -170°م في ليله — أي فارق يقارب 300°م! لماذا تتطرف الحرارة على القمر مقارنةً بالأرض؟",
        [
            ("The Moon has virtually NO atmosphere to scatter daytime heat or trap outgoing infrared heat at night (plus each lunar day and night lasts ~14 Earth days)", "يكاد القمر يخلو تماماً من أي غلاف جوي يشتّت حرارة النهار أو يحبس الإشعاع الحراري ليلاً (إضافةً لطول نهار القمر وليله لنحو 14 يوماً أرضياً)"),
            ("The Moon orbits twice as close to the Sun as Mercury at noon", "يدور القمر أقرب إلى الشمس بمرتين من عطارد عند الظهيرة"),
            ("Deep frozen lunar oceans freeze astronaut suits instantaneously", "تجمد محيطات القمر المتجمدة بدلات الرواد فوراً"),
            ("Astronaut headlamps emit 99% of daytime heat", "تُصدر مصابيح الرواد 99% من حرارة النهار"),
        ],
        "Remember our own atmosphere's greenhouse insulation + ocean heat buffer + fast 24-hour spin!",
        "تذكّر دور الغلاف الجوي الأرضي في العزل والاعتدال الحراري، بالإضافة إلى سرعة دوران الأرض اليومية!",
        "Lack of an insulating atmosphere and slow ~29.5-day rotation expose lunar surfaces to extreme radiative heating and cooling.",
        ["With no air, nothing blocks direct midday sunlight (+120 °C) and nothing traps warmth after sunset (-170 °C).", "Earth's atmosphere, greenhouse gases, oceans, and fast 24-hour rotation keep daily swings modest."],
        "No atmosphere + ~14-day night = extreme ±150 °C lunar swings.",
        "انعدام الغلاف الجوي وطول اليوم القمري يجعلان سطح القمر بلا درع حراري.",
        ["عدم وجود هواء يعني وصول أشعة الشمس كاملة نهاراً (+120°م) وهروب الحرارة بلا عائق ليلاً (-170°م).", "على الأرض يعتدل المناخ بفضل الغلاف الجوي والاحتباس الحراري والمحيطات ودورة الـ 24 ساعة."],
        "بلا غلاف جوي = تقلب حراري متطرف على القمر.",
        None, None,
    )


def build_g6_science_bank() -> list[dict]:
    """Build and verify the 360-item ETEC Nafes Science Grade 6 question bank."""
    B = G6SciBankBuilder()
    builders = [
        _add_b01, _add_b02, _add_b03, _add_b04, _add_b05, _add_b06,
        _add_b07, _add_b08, _add_b09, _add_b10, _add_b11, _add_b12,
        _add_b13, _add_b14, _add_b15, _add_b16, _add_b17, _add_b18,
        _add_b19, _add_b20, _add_b21, _add_b22, _add_b23, _add_b24,
    ]
    for fn in builders:
        fn(B)

    items = B.items
    assert len(items) == 360, f"Expected 360 items, got {len(items)}"
    assert len({q["id"] for q in items}) == 360
    assert len({norm_text(q["content"]["en"]["question"]) for q in items}) == 360

    topic_counts = {}
    diff_counts = {}
    bp_counts = {}
    diag_count = 0
    for q in items:
        topic_counts[q["topic"]] = topic_counts.get(q["topic"], 0) + 1
        diff_counts[q["difficulty"]] = diff_counts.get(q["difficulty"], 0) + 1
        bp_key = q["nafes_science_blueprint"]
        bp_counts[bp_key] = bp_counts.get(bp_key, 0) + 1
        if q["content"]["en"].get("diagram"):
            diag_count += 1

    assert len(topic_counts) == 4 and all(v == 90 for v in topic_counts.values()), topic_counts
    assert diff_counts == {"Easy": 120, "Medium": 120, "Hard": 120}, diff_counts
    assert len(bp_counts) == 24 and all(v == 15 for v in bp_counts.values()), bp_counts
    assert diag_count >= 150, f"Expected >= 150 diagrams, got {diag_count}"
    return items
