"""Bilingual 4-card Quick Formula & Strategy Cheat-Sheets for all 36 Kangaroo Math lessons (KANG-L0-01..KANG-L5-06)."""


import re


def _extract_main_formula(en_txt: str) -> str:
    spans = re.findall(r"\\\(.*?\\\)", en_txt)
    assert spans, f"Expected inline math formula in cheat_sheet entry: {en_txt}"
    best = max(spans, key=len)
    inner = best[2:-2].strip()
    if inner.startswith("="):
        inner = inner[1:].strip()
    return rf"\({inner}\)"


def _cs(en_items: list[tuple[str, str]], ar_items: list[tuple[str, str]]) -> dict:
    assert len(en_items) == 4 and len(ar_items) == 4
    en_out = []
    ar_out = []
    for (lbl_en, txt_en), (lbl_ar, txt_ar) in zip(en_items, ar_items):
        fml = _extract_main_formula(txt_en)
        en_out.append({"title": lbl_en, "formula": fml, "note": txt_en})
        ar_out.append({"title": lbl_ar, "formula": fml, "note": txt_ar})
    return {"en": en_out, "ar": ar_out}


KANGAROO_CHEAT_SHEETS: dict[str, dict] = {
    # ── PreEcolier (Grades 1–2): KANG-L0-01 .. KANG-L0-06 ──
    "KANG-L0-01": _cs(
        [
            ("Skip-Counting Hops", r"After \( k \) equal hops of \( d \) from \( a \): \(\text{Land} = a + k \times d\)"),
            ("Two-Digit Place Cards", r"Tens card \( T \) and ones card \( U \) make \( 10T + U \) (\( T \neq 0 \))"),
            ("3-Row Brick Pyramid", r"Each top brick equals the sum below: \(\text{Top} = a + 2b + c\)"),
            ("Pairing Socks & Gloves", r"Number of complete pairs from \( n \) items \(= \lfloor n / 2 \rfloor\); leftover \(= n \bmod 2\)"),
        ],
        [
            ("قفزات العدّ القفزي", r"بعد \( k \) قفزات متساوية طولها \( d \) من \( a \): \(\text{الموقع} = a + k \times d\)"),
            ("بطاقات العشرات والآحاد", r"بطاقة عشرات \( T \) وآحاد \( U \) تكوّن \( 10T + U \) بشرط \( T \neq 0 \)"),
            ("هرم الطوب ذو 3 صفوف", r"كل طوبة علوية تساوي مجموع الطوبتين تحتها: \(\text{القمة} = a + 2b + c\)"),
            ("تزويج الجوارب والقفازات", r"عدد الأزواج الكاملة من \( n \) قطعة \(= \lfloor n / 2 \rfloor\) والباقي \(= n \bmod 2\)"),
        ],
    ),
    "KANG-L0-02": _cs(
        [
            ("Pan Balance Trading", r"If \( 1\text{ melon} = 2\text{ apples} \) and \( 1\text{ apple} = 3\text{ plums} \), then \( 1\text{ melon} = 6\text{ plums} \)"),
            ("Identical Picture Sum", r"If \( \bigstar + \bigstar + \bigstar = 15 \), then one icon \( \bigstar = 15 \div 3 = 5 \)"),
            ("Repeating Bead Train", r"For a pattern block of length \( L \), bead \( N \) matches position \( ((N - 1) \bmod L) + 1 \)"),
            ("Rewinding a Rule Box", r"Work backwards from output: undo \( +a \) with \( -a \), and undo \( \times k \) with \( \div k \)"),
        ],
        [
            ("استبدال كفّتي الميزان", r"إذا كانت \( 1\text{ بطيخة} = 2\text{ تفاحة} \) و\( 1\text{ تفاحة} = 3\text{ خوخات} \) فإن \( 1\text{ بطيخة} = 6\text{ خوخات} \)"),
            ("جمع الرموز المتماثلة", r"إذا كان \( \bigstar + \bigstar + \bigstar = 15 \) فإن قيمة الرمز الواحد \( \bigstar = 15 \div 3 = 5 \)"),
            ("قطار الخرز المتكرر", r"لدورة طولها \( L \)، الخرزة رقم \( N \) تطابق الموضع \( ((N - 1) \bmod L) + 1 \)"),
            ("عكس صندوق القاعدة", r"اعمل عكسياً من المخرج: اعكس \( +a \) بـ \( -a \) واعكس \( \times k \) بـ \( \div k \)"),
        ],
    ),
    "KANG-L0-03": _cs(
        [
            ("Polygon Sides & Corners", r"Triangle \(= 3\), Quadrilateral \(= 4\), Pentagon \(= 5\), Hexagon \(= 6\) straight sides"),
            ("Missing Wall Tiles", r"Missing tiles \(= (\text{Rows} \times \text{Columns}) - \text{Visible Tiles}\)"),
            ("Quarter-Turn Cycle", r"Four \( 90^\circ \) turns bring a stamp back; two \( 90^\circ \) turns flip top-to-bottom and left-to-right"),
            ("3D Cube Stack Columns", r"Count tower heights on the floor plan and add: \(\text{Total} = \sum h_{i,j}\)"),
        ],
        [
            ("أضلاع وزوايا المضلعات", r"مثلث \(= 3\)، رباعي \(= 4\)، خماسي \(= 5\)، سداسي \(= 6\) أضلاع مستقيمة"),
            ("البلاطات المفقودة في الجدار", r"البلاطات المفقودة \(= (\text{الصفوف} \times \text{الأعمدة}) - \text{البلاطات الظاهرة}\)"),
            ("دورة ربع الدورة", r"أربع دورات \( 90^\circ \) تعيد الختم لمكانه؛ ودورتان \( 90^\circ \) تقلبانه رأساً على عقب"),
            ("أعمدة المكعبات المتراصة", r"اكتب ارتفاع كل عمود على مخطط القاعدة واجمع: \(\text{المجموع} = \sum h_{i,j}\)"),
        ],
    ),
    "KANG-L0-04": _cs(
        [
            ("Fencepost Tree Gaps", r"\( N \) trees in a straight row create \( N - 1 \) gaps: \(\text{Length} = (N - 1) \times d\)"),
            ("Grid Step Counting", r"Count unit segments between corners (not dots!): \(\text{Steps} = \Delta x + \Delta y\)"),
            ("Folded Ribbon Cuts", r"One straight cut across \( F \) layers adds \( F \) cuts \(\implies\) pieces \(= 1 + \text{total cuts}\)"),
            ("Opposite Die Faces", r"Standard die opposite faces always sum to \( 7 \): \((1,6),\; (2,5),\; (3,4)\)"),
        ],
        [
            ("المسافات بين الأشجار", r"\( N \) شجرة في صف مستقيم تصنع \( N - 1 \) مسافة: \(\text{الطول} = (N - 1) \times d\)"),
            ("عدّ خطوات الشبكة", r"عُدّ القطع بين التقاطعات (لا النقاط!): \(\text{الخطوات} = \Delta x + \Delta y\)"),
            ("قص الشريط المطوي", r"قصّة واحدة عبر \( F \) طبقات تصنع \( F \) قصّات \(\implies\) عدد القطع \(= 1 + \text{مجموع القصّات}\)"),
            ("الأوجه المتقابلة في النرد", r"مجموع أي وجهين متقابلين في النرد القياسي يساوي \( 7 \): \((1,6),\; (2,5),\; (3,4)\)"),
        ],
    ),
    "KANG-L0-05": _cs(
        [
            ("Queue Line Formula", r"\( a \) ahead and \( b \) behind \(\implies \text{Total} = a + b + 1\); \( m \)-th from front & \( n \)-th from back \(\implies m + n - 1\)"),
            ("Coin Purse Totals", r"Group largest coins first, then smaller coins: \(\text{Value} = \sum (\text{count}_i \times \text{coin}_i)\)"),
            ("Matching Choice Pairs", r"With \( A \) flavors and \( B \) cones, total different treats \(= A \times B\)"),
            ("Magic 5-Cell Cross", r"\(\text{Row Sum} + \text{Column Sum} = (\text{Sum of all } 5 \text{ numbers}) + \text{Center}\)"),
        ],
        [
            ("قانون الطابور", r"\( a \) أمامك و\( b \) خلفك \(\implies a + b + 1\)؛ والترتيب \( m \) من الأمام و\( n \) من الخلف \(\implies m + n - 1\)"),
            ("مجموع النقود المعدنية", r"اجمع الفئات الأكبر أولاً ثم الأصغر: \(\text{القيمة} = \sum (\text{العدد}_i \times \text{الفئة}_i)\)"),
            ("أزواج الاختيارات", r"مع \( A \) نكهات و\( B \) أقماع يكون عدد الخيارات المختلفة \(= A \times B\)"),
            ("صليب الأعداد السحري", r"\(\text{مجموع الصف} + \text{مجموع العمود} = (\text{مجموع الأعداد الخمسة}) + \text{المركز}\)"),
        ],
    ),
    "KANG-L0-06": _cs(
        [
            ("Whole & Half Hours", r"Minute hand at \( 12 \implies :00 \); minute hand at \( 6 \implies :30 \) (30 minutes)"),
            ("Bar Chart Difference", r"\"How many more \( A \) than \( B \)?\" means subtract heights: \( h_A - h_B \)"),
            ("Worst-Case Marble Draw", r"To guarantee \( 1 \) red when \( N_{\text{other}} \) non-red exist, draw \( N_{\text{other}} + 1 \)"),
            ("Most-Likely Spinner Color", r"The color with the largest central angle \( \theta_{\max} \) (or most equal slices) has highest \( P = \frac{\theta}{360^\circ} \)"),
        ],
        [
            ("الساعة الكاملة والنصف", r"عقرب الدقائق عند \( 12 \implies :00 \)؛ وعند \( 6 \implies :30 \) (30 دقيقة)"),
            ("الفرق في الأعمدة البيانية", r"«بكم يزيد \( A \) على \( B \)؟» يعني طرح الارتفاعين: \( h_A - h_B \)"),
            ("أسوأ حالة لسحب الكرات", r"لضمان كرة حمراء واحدة مع وجود \( N_{\text{أخرى}} \) غير حمراء، اسحب \( N_{\text{أخرى}} + 1 \)"),
            ("اللون الأكثر احتمالاً في القرص", r"اللون ذو المساحة الأكبر أو عدد القطاعات المتساوية الأكثر هو الأرجح"),
        ],
    ),
    # ── Ecolier (Grades 3–4): KANG-L1-01 .. KANG-L1-06 ──
    "KANG-L1-01": _cs(
        [
            ("Brick Pyramid Top Rule", r"In a 3-row brick pyramid with base \( a, b, c \): \(\text{Top} = a + 2b + c\)"),
            ("Kangaroo Fencepost Hops", r"\( N \) posts have \( N - 1 \) gaps; \( k \) hops reach post \( 1 + k \)"),
            ("Smallest Multi-Digit Number", r"Put smallest non-zero digit first, then \( 0 \), then remaining digits in ascending order"),
            ("Largest Multi-Digit Number", r"Place available digits in descending order \( d_1 \ge d_2 \ge \dots \ge d_k \) from left to right"),
        ],
        [
            ("قاعدة قمة هرم الطوب", r"في هرم طوب من 3 صفوف قاعدته \( a, b, c \): \(\text{القمة} = a + 2b + c\)"),
            ("قفزات الكنغر والأعمدة", r"\( N \) عموداً بينها \( N - 1 \) فجوة؛ و\( k \) قفزات توصل إلى العمود \( 1 + k \)"),
            ("أصغر عدد من البطاقات", r"ضع أصغر رقم غير صفري في اليسار، ثم \( 0 \)، ثم بقية الأرقام تصاعدياً"),
            ("أكبر عدد من البطاقات", r"رتّب الأرقام المتاحة تنازلياً من الأكبر إلى الأصغر من اليسار لليمين"),
        ],
    ),
    "KANG-L1-02": _cs(
        [
            ("Equal Pan Removal", r"Removing identical weights \( c \) from both pans preserves balance: \( A + c = B + c \implies A = B \)"),
            ("Shared Cross Center", r"Two lines of sum \( S \) sharing center \( c \) satisfy \( 2S = (\text{total sum}) + c \)"),
            ("Cycle Remainder Rule", r"Item \( N \) in a repeating cycle of length \( L \) matches item \( r = N \bmod L \) (or \( L \) if \( r = 0 \))"),
            ("Inverse Mystery Machine", r"Reverse order and invert each step: \(\xrightarrow{+a}\xrightarrow{\times b}\) rewinds as \(\xleftarrow{-a}\xleftarrow{\div b}\)"),
        ],
        [
            ("حذف الأوزان المتساوية", r"إزالة عناصر متطابقة من كفّتي الميزان تحافظ على التوازن"),
            ("المركز المشترك في الصليب", r"خطّان مجموع كل منهما \( S \) يشتركان في المركز \( c \) يحققان \( 2S = (\text{المجموع الكلي}) + c \)"),
            ("قاعدة باقي الدورة", r"العنصر رقم \( N \) في دورة طولها \( L \) يطابق العنصر \( r = N \bmod L \) (أو \( L \) عند \( r = 0 \))"),
            ("عكس آلة الأعداد", r"اعكس الترتيب وكل عملية: \(\xrightarrow{+a}\xrightarrow{\times b}\) تُعكس بـ \(\xleftarrow{-a}\xleftarrow{\div b}\)"),
        ],
    ),
    "KANG-L1-03": _cs(
        [
            ("Staircase Perimeter Push", r"Any monotonic \( W \times H \) staircase has perimeter \( P = 2(W + H) \)"),
            ("Tiled Floor Area", r"Full rectangle of \( R \) rows by \( C \) columns contains \( R \times C \) unit tiles"),
            ("Overlapping Cards Area", r"\(\text{Combined Area} = \text{Area}_1 + \text{Area}_2 - \text{Overlap}\)"),
            ("Row of Matchstick Squares", r"\( n \) squares in a straight row use \( 3n + 1 \) matchsticks (each new square adds \( 3 \))"),
        ],
        [
            ("محيط الشكل الدرجي", r"أي مضلع درجي رتيب داخل مستطيل \( W \times H \) محيطه \( P = 2(W + H) \)"),
            ("مساحة الأرضية المبلّطة", r"المستطيل المكون من \( R \) صفوف و\( C \) أعمدة يحوي \( R \times C \) بلاطة"),
            ("مساحة البطاقات المتداخلة", r"\(\text{المساحة الكلية} = \text{مساحة}_1 + \text{مساحة}_2 - \text{التداخل}\)"),
            ("صف مربعات أعواد الثقاب", r"\( n \) مربعات متجاورة في صف تستهلك \( 3n + 1 \) عوداً (كل مربع إضافي يضيف \( 3 \))"),
        ],
    ),
    "KANG-L1-04": _cs(
        [
            ("Hidden Cubes in a Stack", r"Sum column heights across the base grid: \(\text{Missing to } n^3 = n^3 - \text{Present}\)"),
            ("Opposite Faces on Dice", r"Opposite faces on a standard die sum to \( 7 \) and never share an edge or corner"),
            ("Cube Net Leapfrog", r"On a straight strip of \( 3 \) squares in a cube net, the \( 1\text{st} \) and \( 3\text{rd} \) fold opposite"),
            ("Transparent Card Flip/Turn", r"Rotation (\( 90^\circ, 180^\circ, 270^\circ \)) preserves orientation; flipping over creates a mirror reflection"),
        ],
        [
            ("المكعبات المخفية في البرج", r"اجمع ارتفاعات الأعمدة؛ والمفقود لإكمال مكعب \( n^3 \) هو \( n^3 - \text{الموجود} \)"),
            ("الأوجه المتقابلة في النرد", r"الأوجه المتقابلة في النرد القياسي مجموعها \( 7 \) ولا تتجاور أبداً"),
            ("قاعدة القفز في شبكة المكعب", r"في صف من \( 3 \) مربعات بشبكة المكعب ينطوي الأول والثالث متقابلين"),
            ("تدوير وقلب البطاقة الشفافة", r"الدوران يحفظ الاتجاه، أما القلب فيعكس الشكل كصورة مرآة"),
        ],
    ),
    "KANG-L1-05": _cs(
        [
            ("Double-End Queue Rank", r"\( m \)-th from front and \( n \)-th from back \(\implies \text{Total} = m + n - 1\)"),
            ("Folded Ribbon Pieces", r"Fold \( k \) times in half (\( 2^k \) layers), make \( c \) transverse cuts \(\implies c \cdot 2^k + 1 \) pieces"),
            ("Outfit Multiplication Rule", r"\( a \) shirts \(\times\; b \) pants \(\times\; c \) hats \(= a \cdot b \cdot c \) distinct outfits"),
            ("4×4 Mini-Sudoku Rule", r"Every row, column, and \( 2 \times 2 \) box contains \( \{1, 2, 3, 4\} \) exactly once (sum \(= 10\))"),
        ],
        [
            ("الترتيب من طرفي الطابور", r"الترتيب \( m \) من الأمام و\( n \) من الخلف \(\implies \text{العدد الكلي} = m + n - 1\)"),
            ("قطع الشريط المطوي", r"طيّ الشريط \( k \) مرات بالنصف (\( 2^k \) طبقة) مع \( c \) قصّات يعطي \( c \cdot 2^k + 1 \) قطعة"),
            ("قاعدة ضرب الأزياء", r"\( a \) قمصان \(\times\; b \) بناطيل \(\times\; c \) قبعات \(= a \cdot b \cdot c \) زياً مختلفاً"),
            ("قاعدة سودوكو 4×4 المصغّر", r"كل صف وعمود ومربع \( 2 \times 2 \) يحوي \( \{1, 2, 3, 4\} \) مرة واحدة (المجموع \(= 10\))"),
        ],
    ),
    "KANG-L1-06": _cs(
        [
            ("Whole-Hour Clock Bridge", r"Count minutes up to the next whole hour (\( 60 - m_1 \)), then add remaining hours & minutes"),
            ("Missing Bar from Total", r"\(\text{Missing Bar} = \text{Total Surveyed} - \sum (\text{Known Bars})\)"),
            ("Pigeonhole Pair Guarantee", r"With \( C \) colors in a bag, drawing \( C + 1 \) marbles guarantees at least \( 2 \) of the same color"),
            ("Grid Arrow Walk", r"Track \( (\text{East} - \text{West}, \text{North} - \text{South}) \) net steps from the start cell"),
        ],
        [
            ("جسر الساعة الكاملة", r"احسب الدقائق حتى الساعة الكاملة التالية (\( 60 - m_1 \)) ثم أضف الساعات والدقائق المتبقية"),
            ("العمود المفقود من المجموع", r"\(\text{العمود المفقود} = \text{المجموع الكلي} - \sum (\text{الأعمدة المعلومة})\)"),
            ("ضمان زوج متماثل اللون", r"مع وجود \( C \) ألوان في الكيس، سحب \( C + 1 \) كرات يضمن كرتين على الأقل من اللون نفسه"),
            ("مسار الأسهم على الشبكة", r"احسب صافي الخطوات \( (\text{شرق} - \text{غرب}، \text{شمال} - \text{جنوب}) \) من نقطة البداية"),
        ],
    ),
    # ── Benjamin (Grades 5–6): KANG-L2-01 .. KANG-L2-06 ──
    "KANG-L2-01": _cs(
        [
            ("Divisibility by 3, 4, 9", r"By \( 3/9 \): digit sum \(\div 3/9\); by \( 4 \): last two digits \(\div 4\)"),
            ("LCM Cycle Synchronization", r"Periods \( a \) and \( b \) align every \(\operatorname{LCM}(a, b) = \frac{a \cdot b}{\gcd(a, b)}\)"),
            ("7-Segment Matchstick Counts", r"Segment counts \( 0\text{–}9 \): \( 1\to 2,\; 7\to 3,\; 4\to 4,\; \{2,3,5\}\to 5,\; \{0,6,9\}\to 6,\; 8\to 7 \)"),
            ("Column Cryptarithm Carries", r"Adding two digits (+ carry) gives a carry into the next column of at most \( 1 \)"),
        ],
        [
            ("قابلية القسمة على 3 و4 و9", r"على \( 3 \) أو \( 9 \): مجموع الأرقام؛ وعلى \( 4 \): آخر رقمين يقبلان القسمة على \( 4 \)"),
            ("تزامن الدورات بـ م.م.أ", r"دورتان طولاهما \( a, b \) تلتقيان كل \(\operatorname{LCM}(a, b) = \frac{a \cdot b}{\gcd(a, b)}\)"),
            ("أعواد الأرقام الرقمية", r"عدد القطع: \( 1\leftarrow 2،\; 7\leftarrow 3،\; 4\leftarrow 4،\; \{2,3,5\}\leftarrow 5،\; \{0,6,9\}\leftarrow 6،\; 8\leftarrow 7 \)"),
            ("الحمل في الجمع العمودي", r"جمع رقمين (مع الحمل السابق) يعطي حملاً للعمود التالي مقداره \( 0 \) أو \( 1 \) فقط"),
        ],
    ),
    "KANG-L2-02": _cs(
        [
            ("Fraction of the Remainder", r"Take \( \frac{a}{b} \) then \( \frac{c}{d} \) of remainder \(\implies \text{Left} = \left(1 - \frac{a}{b}\right)\!\left(1 - \frac{c}{d}\right)\)"),
            ("Work-Backwards Machine", r"Invert in reverse order: \( y = a x + b \implies x = \frac{y - b}{a} \)"),
            ("3×3 Magic Square Center", r"Magic constant \( M = 3 \times c \) and total sum of all \( 9 \) cells \(= 9 \times c \)"),
            ("Twin Scale Substitution", r"Scale equations combine linearly: if \( 2A = 3B \) and \( B = 4C \), then \( A = 6C \)"),
        ],
        [
            ("كسر المتبقي", r"أخذ \( \frac{a}{b} \) ثم \( \frac{c}{d} \) من المتبقي يترك \(\left(1 - \frac{a}{b}\right)\!\left(1 - \frac{c}{d}\right)\)"),
            ("الحل العكسي لآلة الأعداد", r"ابدأ من المخرج النهائي وطبّق العمليات العكسية بترتيب معكوس"),
            ("مركز المربع السحري 3×3", r"الثابت السحري للخط \( M = 3c \) ومجموع الخلايا التسع \(= 9c \) حيث \( c \) المركز"),
            ("التعويض بين ميزانين", r"ضاعف إحدى معادلتي التوازن أو اطرحهما لعزل وزن شكل واحد"),
        ],
    ),
    "KANG-L2-03": _cs(
        [
            ("Overlapping Shapes Union", r"\(\text{Total Covered Area} = A_1 + A_2 - A_{\text{overlap}}\); Uncovered \(= A_{\text{table}} - A_{\text{union}}\)"),
            ("Corner Cut Perimeter", r"Cutting an outer rectangular corner keeps \( P = 2(W + H) \); an inward notch adds \( 2d \)"),
            ("Triangle Across Rectangle", r"A triangle with base on one side of an \( L \times W \) rectangle and apex opposite has area \( \frac{1}{2}LW \)"),
            ("Paper-Fold Angle Twin", r"The crease bisects the fold: folded angle \( = \) original ghost angle, so straight line \(= 180^\circ = 2\alpha + \beta\)"),
        ],
        [
            ("اتحاد المستطيلات المتداخلة", r"\(\text{المساحة المغطاة} = A_1 + A_2 - A_{\text{التداخل}}\)"),
            ("محيط قصّ الأركان", r"قصّ ركن خارجي يحفظ المحيط \( 2(W + H) \)؛ أما الشقّ الداخلي عمقه \( d \) فيضيف \( 2d \)"),
            ("مثلث داخل مستطيل", r"مثلث قاعدته ضلع مستطيل \( L \times W \) ورأسه على الضلع المقابل مساحته \( \frac{1}{2}LW \)"),
            ("تطابق زاوية الطيّ الورقي", r"خط الطيّ ينصّف الزاوية المطوية؛ وعلى المستقيم \( 180^\circ = 2\alpha + \beta \)"),
        ],
    ),
    "KANG-L2-04": _cs(
        [
            ("Painted n × n × n Cube", r"3 faces: \( 8 \); 2 faces: \( 12(n - 2) \); 1 face: \( 6(n - 2)^2 \); 0 faces: \( (n - 2)^3 \)"),
            ("Cube Net Opposite Faces", r"Opposite faces are separated by \( 1 \) square in line or sit at Z-ends (never touch)"),
            ("Polyomino Area Divisibility", r"Tiling a grid of \( N \) cells with \( k \)-ominoes requires \( k \mid N \) plus corner/color fit"),
            ("Interlocking Gear Chain", r"Odd number of meshing gears \(\implies\) same rotation; even \(\implies\) opposite; \( T_1 \omega_1 = T_k \omega_k \)"),
        ],
        [
            ("المكعب المطلي n×n×n", r"3 أوجه: \( 8 \)؛ وجهان: \( 12(n - 2) \)؛ وجه واحد: \( 6(n - 2)^2 \)؛ بدون طلاء: \( (n - 2)^3 \)"),
            ("الأوجه المتقابلة في الشبكة", r"الأوجه المتقابلة يفصلها مربع واحد على استقامة أو تقع في طرفي حرف Z"),
            ("تبليط متعددات المربعات", r"تبليط منطقة من \( N \) خلية بقطع حجمها \( k \) يشترط أولاً \( k \mid N \)"),
            ("سلسلة التروس المتشابكة", r"عدد فردي من التروس \(\implies\) نفس الاتجاه؛ زوجي \(\implies\) عكسه؛ و\( T_1 \omega_1 = T_k \omega_k \)"),
        ],
    ),
    "KANG-L2-05": _cs(
        [
            ("2-Set Venn Formula", r"\(|A \cup B| = |A| + |B| - |A \cap B|\) — always fill the overlap \( |A \cap B| \) first!"),
            ("Worst-Case k-of-a-Kind", r"To guarantee \( k \) of one color across \( c \) colors: \( 1 + \sum_{i=1}^{c} \min(n_i, k - 1) \)"),
            ("Handshakes & Diagonals", r"Handshakes among \( n \): \( \frac{n(n - 1)}{2} \); diagonals of an \( n \)-gon: \( \frac{n(n - 3)}{2} \)"),
            ("Circular Spacing", r"Around a circle, \( N \) items create \( N \) gaps (not \( N - 1 \)!); opposite seat shift \(= N / 2\)"),
        ],
        [
            ("مخطط فن لمجموعتين", r"\(|A \cup B| = |A| + |B| - |A \cap B|\) — ابدأ دائماً بملء التقاطع أولاً!"),
            ("أسوأ حالة لضمان k من لون", r"لضمان \( k \) من لون واحد عبر \( c \) ألوان: \( 1 + \sum_{i=1}^{c} \min(n_i, k - 1) \)"),
            ("المصافحات والأقطار", r"مصافحات \( n \) أشخاص: \( \frac{n(n - 1)}{2} \)؛ وأقطار مضلع \( n \)-ي: \( \frac{n(n - 3)}{2} \)"),
            ("الترتيب الدائري", r"حول الدائرة تصنع \( N \) عناصر \( N \) فجوات تماماً؛ والمقعد المقابل يبعد \( N / 2 \)"),
        ],
    ),
    "KANG-L2-06": _cs(
        [
            ("Target Mean Sum Bridge", r"\(\text{Total Sum} = \text{Mean} \times \text{Count}\); new score \(= (n + 1)\mu_{\text{new}} - n\mu_{\text{old}}\)"),
            ("Spinner Angle Probability", r"\( P(\text{Event}) = \frac{\text{Winning Central Angle}}{360^\circ} = \frac{\text{Winning Equal Sectors}}{\text{Total Equal Sectors}} \)"),
            ("24-Hour Clock Palindromes", r"Hours `00`–`05`, `10`–`15`, `20`–`23` each have exactly \( 1 \) valid reversed minute (`ab:ba`) \(\implies 16\)/day"),
            ("Shortest Map Path", r"Relax cumulative distances node-by-node: \( D(v) = \min_{u \to v} \{D(u) + w(u, v)\} \)"),
        ],
        [
            ("جسر المجموع للمتوسط", r"\(\text{المجموع} = \text{المتوسط} \times \text{العدد}\)؛ الدرجة الجديدة \(= (n + 1)\mu_{\text{جديد}} - n\mu_{\text{قديم}}\)"),
            ("احتمال زاوية القرص الدوار", r"\( P(\text{الحدث}) = \frac{\text{مجموع الزوايا الرابحة}}{360^\circ} \)"),
            ("متناظرات الساعة الرقمية 24h", r"الساعات `00`–`05` و`10`–`15` و`20`–`23` تعطي دقيقة عكسية صالحة `ab:ba` (\( 16 \) مرة يومياً)"),
            ("أقصر مسار على الخريطة", r"احسب المسافة التراكمية الأقل عقدةً بعقدة من البداية حتى النهاية"),
        ],
    ),
    # ── Cadet (Grades 7–8): KANG-L3-01 .. KANG-L3-06 ──
    "KANG-L3-01": _cs(
        [
            ("Divisors & Perfect Squares", r"For \( n = \prod p_i^{e_i} \), \( \tau(n) = \prod(e_i + 1) \); \( n \) is a square iff every \( e_i \) is even"),
            ("Coprime GCD–LCM Parametrization", r"Write \( a = gx, b = gy \) with \( \gcd(x, y) = 1 \); then \( \operatorname{LCM}(a, b) = gxy \)"),
            ("Digit-Reversal Identities", r"\(\overline{ab} - \overline{ba} = 9(a - b)\), \(\overline{abc} - \overline{cba} = 99(a - c)\)"),
            ("Units-Digit Power Cycle", r"Reduce base mod \( 10 \) and exponent mod \( 4 \) (using \( 4 \) when exponent \(\equiv 0 \pmod 4\))"),
        ],
        [
            ("عدد القواسم والمربعات الكاملة", r"للعدد \( n = \prod p_i^{e_i} \) يكون \( \tau(n) = \prod(e_i + 1) \)؛ وهو مربع كامل إذا كانت كل \( e_i \) زوجية"),
            ("تمثيل القاسم والمضاعف المشترك", r"ضع \( a = gx,\; b = gy \) مع \( \gcd(x, y) = 1 \)؛ فيكون \( \operatorname{LCM}(a, b) = gxy \)"),
            ("متطابقات عكس الأرقام", r"\(\overline{ab} - \overline{ba} = 9(a - b)\) و\(\overline{abc} - \overline{cba} = 99(a - c)\)"),
            ("دورة آحاد القوى الكبرى", r"اختزل الأساس mod \( 10 \) والأس mod \( 4 \) (واستخدم الأس \( 4 \) إذا قبل القسمة على \( 4 \))"),
        ],
    ),
    "KANG-L3-02": _cs(
        [
            ("Mixture Invariant Anchor", r"Adding water keeps solute mass \( C \cdot V \) constant: \( C_1 V_1 = C_2 V_2 \)"),
            ("Equal-Distance Harmonic Speed", r"Out at \( v_1 \), back at \( v_2 \) \(\implies v_{\text{avg}} = \frac{2v_1 v_2}{v_1 + v_2} \) (never \( \frac{v_1 + v_2}{2} \)!)"),
            ("Constant Age Difference", r"Age gap \( D = A - B \) stays fixed; when \( A = kB \), smaller age \( B = \frac{D}{k - 1} \)"),
            ("Telescoping Sum & Product", r"\(\sum \frac{1}{k(k+1)} = \frac{1}{a} - \frac{1}{b+1}\); \(\prod \left(1 - \frac{1}{k^2}\right) = \frac{n + 1}{2n}\)"),
        ],
        [
            ("ثابت المذاب في الخليط", r"عند إضافة الماء تبقى كمية المذاب ثابتة: \( C_1 V_1 = C_2 V_2 \)"),
            ("متوسط السرعة ذهاباً وإياباً", r"ذهاباً بـ \( v_1 \) وإياباً بـ \( v_2 \): \( v_{\text{avg}} = \frac{2v_1 v_2}{v_1 + v_2} \)"),
            ("ثبات فرق العمر", r"الفرق \( D = A - B \) ثابت دائماً؛ وعندما \( A = kB \) يكون الأصغر \( B = \frac{D}{k - 1} \)"),
            ("المجاميع والجداءات المتداخلة", r"\(\sum \frac{1}{k(k+1)} = \frac{1}{a} - \frac{1}{b+1}\) و\(\prod \left(1 - \frac{1}{k^2}\right) = \frac{n + 1}{2n}\)"),
        ],
    ),
    "KANG-L3-03": _cs(
        [
            ("Parallel Zigzag Sum Rule", r"Between parallel lines: \(\sum (\text{Left-pointing bends}) = \sum (\text{Right-pointing bends})\)"),
            ("2×2 Subdivided Rectangle", r"Parallel splits: \( A_{11} A_{22} = A_{12} A_{21} \); interior point to corners: \( S_1 + S_3 = S_2 + S_4 \)"),
            ("Midpoint Square Half-Area", r"Joining midpoints of a square (or any quadrilateral) encloses exactly \( \frac{1}{2} \) the outer area"),
            ("Square-Circle Corner Cutouts", r"Four quarter-circles of radius \( r = s/2 \) inside a side-\( s \) square equal \( 1 \) full circle \( \pi (s/2)^2 \)"),
        ],
        [
            ("قاعدة الخط المتعرج بين متوازيين", r"بين مستقيمين متوازيين: \(\sum (\text{الزوايا المتجهة يساراً}) = \sum (\text{الزوايا المتجهة يميناً})\)"),
            ("المستطيل المقسم 2×2", r"بمستقيمين موازيين: \( A_{11} A_{22} = A_{12} A_{21} \)؛ ومن نقطة داخلية للأركان: \( S_1 + S_3 = S_2 + S_4 \)"),
            ("مربع منتصفات الأضلاع", r"وصل منتصفات أضلاع مربع (أو أي رباعي محدب) يحصر تماماً \( \frac{1}{2} \) المساحة الكلية"),
            ("أرباع الدوائر في المربع", r"أربعة أرباع دوائر نصف قطرها \( s/2 \) داخل مربع ضلعه \( s \) تكوّن دائرة كاملة مساحتها \( \pi (s/2)^2 \)"),
        ],
    ),
    "KANG-L3-04": _cs(
        [
            ("Painted a × b × c Block", r"0 faces: \((a-2)(b-2)(c-2)\); 2 faces: \(4[(a-2)+(b-2)+(c-2)]\); 3 faces: \(8\)"),
            ("Rolling Die State Tracking", r"Track \((\text{Top}, \text{Front}, \text{Right})\) using \( \text{Opp} = 7 - x \); rolling forward sends \((\text{T},\text{F}) \to (7-\text{F},\text{T})\)"),
            ("Unfolded Box Shortest Path", r"Flatten the faces crossed by the ant into a rectangle: \( d_{\min} = \sqrt{(\Delta X)^2 + (\Delta Y)^2} \)"),
            ("3-View Exposed Surface", r"Convex stack surface area \(= 2(A_{\text{top}} + A_{\text{front}} + A_{\text{right}})\)"),
        ],
        [
            ("متوازي المستطيلات المطلي a×b×c", r"بدون طلاء: \((a-2)(b-2)(c-2)\)؛ وجهان: \(4[(a-2)+(b-2)+(c-2)]\)؛ 3 أوجه: \(8\)"),
            ("تتبّع دحرجة النرد", r"تتبّع \((\text{أعلى}, \text{أمام}, \text{يمين})\) مع المقابل \( 7 - x \)؛ الدحرجة للأمام تعطي \((7-\text{أمام}, \text{أعلى})\)"),
            ("أقصر مسار على سطح الصندوق", r"افرد الوجهين على مستوى واحد ثم احسب الوتر: \( d_{\min} = \sqrt{(\Delta X)^2 + (\Delta Y)^2} \)"),
            ("المساحة السطحية من المساقط", r"لمجسم مكعبات محدب: \(\text{السطح} = 2(A_{\text{علوي}} + A_{\text{أمامي}} + A_{\text{جانبي}})\)"),
        ],
    ),
    "KANG-L3-05": _cs(
        [
            ("Knights & Liars Parity", r"\"My two neighbors are different\" around an \( N \)-circle forces alternating clusters; test 1 period!"),
            ("Checkerboard Domino Invariant", r"Every \( 1 \times 2 \) domino covers \( 1 \) black + \( 1 \) white cell; equal colors are required to tile"),
            ("Blocked Grid DP Addition", r"At each intersection: \(\text{Ways}(x, y) = \text{Ways}(x - 1, y) + \text{Ways}(x, y - 1)\) (\( 0 \) if blocked)"),
            ("Round-Robin Total Points", r"\( n \) players play \( \binom{n}{2} \) games; with \( (2, 1, 0) \) scoring every game adds \( 2 \implies \text{Total} = n(n - 1) \)"),
        ],
        [
            ("دائرة الفرسان والكاذبين", r"افترض هوية شخص واحد وتتبّع السلسلة حول الدائرة لاستخراج النمط الدوري الصالح"),
            ("ثابت تلوين رقعة الشطرنج", r"كل دومينو \( 1 \times 2 \) يغطي خلية سوداء وأخرى بيضاء؛ التبليط يشترط تساوي اللونين"),
            ("الجمع الديناميكي لمسارات الشبكة", r"عند كل تقاطع: \(\text{الطرق}(x, y) = \text{الطرق}(x - 1, y) + \text{الطرق}(x, y - 1)\) (\( 0 \) للمغلق)"),
            ("مجموع نقاط الدوري الكامل", r"\( n \) لاعبين يلعبون \( \binom{n}{2} \) مباراة؛ بنظام \( (2, 1, 0) \) كل مباراة تضيف \( 2 \implies n(n - 1) \)"),
        ],
    ),
    "KANG-L3-06": _cs(
        [
            ("Weighted Group Mean", r"\(\bar{x} = \frac{n_1 \mu_1 + n_2 \mu_2}{n_1 + n_2}\); deviations from \( \bar{x} \) balance: \( n_1(\mu_1 - \bar{x}) = n_2(\bar{x} - \mu_2) \)"),
            ("Two-Draw Without Replacement", r"\( P(\text{same color}) = \frac{R(R - 1) + B(B - 1)}{N(N - 1)} \); \( P(\text{different}) = \frac{2RB}{N(N - 1)} \)"),
            ("3-Set Venn Inclusion–Exclusion", r"\(|A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C|\)"),
            ("Switch-Toggle Parity", r"Bulb ends ON (from OFF) iff toggled an odd number of times; weights \( 1, 2, 4, \dots, 2^{k-1} \) span \( 0..2^k - 1 \)"),
        ],
        [
            ("المتوسط المرجّح للمجموعات", r"\(\bar{x} = \frac{n_1 \mu_1 + n_2 \mu_2}{n_1 + n_2}\)؛ وتوازن الانحرافات: \( n_1(\mu_1 - \bar{x}) = n_2(\bar{x} - \mu_2) \)"),
            ("السحب المتتالي دون إرجاع", r"\( P(\text{نفس اللون}) = \frac{R(R - 1) + B(B - 1)}{N(N - 1)} \)؛ \( P(\text{مختلفان}) = \frac{2RB}{N(N - 1)} \)"),
            ("التضمين والإقصاء لثلاث مجموعات", r"\(|A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C|\)"),
            ("زوجية تبديل المفاتيح والقوى الثنائية", r"يضيء المصباح إذا بُدّل عدداً فردياً؛ والأوزان \( 1, 2, 4, \dots, 2^{k-1} \) تمثل حتى \( 2^k - 1 \)"),
        ],
    ),
    # ── Junior (Grades 9–10): KANG-L4-01 .. KANG-L4-06 ──
    "KANG-L4-01": _cs(
        [
            ("Simon's Factoring Trick", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("Constrained Divisor Count", r"Factor out required divisor \( d \) first: divisors of \( N \) divisible by \( d \) equal \( \tau(N / d) \)"),
            ("Trailing Zeros of n!", r"\( Z(n!) = v_5(n!) = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots \)"),
            ("Modular Arithmetic Rules", r"\( (a \cdot b) \bmod m = ((a \bmod m)(b \bmod m)) \bmod m \); track periodic cycles of \( a^k \bmod m \)"),
        ],
        [
            ("حيلة سايمون للتحليل", r"\( xy + ax + by = c \iff (x + b)(y + a) = c + ab \)"),
            ("عدّ القواسم المشروطة", r"اسحب القاسم المطلوب \( d \) أولاً: عدد قواسم \( N \) القابلة للقسمة على \( d \) يساوي \( \tau(N / d) \)"),
            ("الأصفار الطرفية للمضروب n!", r"\( Z(n!) = v_5(n!) = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots \)"),
            ("قواعد الحساب المعياري", r"\( (a \cdot b) \bmod m = ((a \bmod m)(b \bmod m)) \bmod m \)؛ تتبّع دورة بواقي \( a^k \bmod m \)"),
        ],
    ),
    "KANG-L4-02": _cs(
        [
            ("Midpoint Radical Shortcut", r"\( \sqrt{(m - d)(m + d) + d^2} = \sqrt{m^2 - d^2 + d^2} = m \)"),
            ("Quadratic Vieta's Formulas", r"For \( ax^2 + bx + c = 0 \): \( r_1 + r_2 = -\frac{b}{a} \), \( r_1 r_2 = \frac{c}{a} \), \( r_1^2 + r_2^2 = (r_1 + r_2)^2 - 2r_1 r_2 \)"),
            ("Reciprocal Power Climb", r"If \( x + \frac{1}{x} = k \): \( x^2 + \frac{1}{x^2} = k^2 - 2 \) and \( x^3 + \frac{1}{x^3} = k^3 - 3k \) (if \( x - \frac{1}{x} = k \), \( x^2 + \frac{1}{x^2} = k^2 + 2 \))"),
            ("Floor-Block Counting", r"\( \lfloor \sqrt{k} \rfloor = m \) holds for \( k \in [m^2, (m + 1)^2 - 1] \), giving \( 2m + 1 \) integers"),
        ],
        [
            ("اختصار الجذر بالمنتصف", r"\( \sqrt{(m - d)(m + d) + d^2} = \sqrt{m^2 - d^2 + d^2} = m \)"),
            ("علاقات فييت التربيعية", r"للمعادلة \( ax^2 + bx + c = 0 \): \( r_1 + r_2 = -\frac{b}{a} \)، \( r_1 r_2 = \frac{c}{a} \)، \( r_1^2 + r_2^2 = (r_1 + r_2)^2 - 2r_1 r_2 \)"),
            ("سلّم القوى المقلوبة", r"إذا كان \( x + \frac{1}{x} = k \) فإن \( x^2 + \frac{1}{x^2} = k^2 - 2 \)؛ وإذا \( x - \frac{1}{x} = k \) فإن \( x^2 + \frac{1}{x^2} = k^2 + 2 \)"),
            ("كتل دالة الجزء الصحيح", r"\( \lfloor \sqrt{k} \rfloor = m \) تتحقق لقيم \( k \in [m^2, (m + 1)^2 - 1] \) وعددها \( 2m + 1 \) عدداً"),
        ],
    ),
    "KANG-L4-03": _cs(
        [
            ("Thales & Cyclic Angles", r"Angle in a semicircle \(= 90^\circ\); opposite angles of a cyclic quadrilateral sum to \( 180^\circ \)"),
            ("Similar-Triangle Area Ratio", r"Linear scale factor \( k \implies \text{Perimeter ratio} = k \) and \(\text{Area ratio} = k^2\)"),
            ("Power of a Point", r"Intersecting chords: \( PA \cdot PB = PC \cdot PD \); tangent-secant: \( PT^2 = PA \cdot PB \)"),
            ("Right-Triangle Inradius", r"For legs \( a, b \) and hypotenuse \( c \): \( r = \frac{a + b - c}{2} \) and \( R = \frac{c}{2} \)"),
        ],
        [
            ("مبرهنة طاليس والرباعي الدائري", r"الزاوية المحيطية في نصف دائرة \(= 90^\circ\)؛ والمتقابلتان في الرباعي الدائري مجموعهما \( 180^\circ \)"),
            ("نسبة مساحات المثلثات المتشابهة", r"معامل التشابه الخطي \( k \implies \text{نسبة المحيطات} = k \) و\(\text{نسبة المساحات} = k^2\)"),
            ("قوة نقطة بالنسبة لدائرة", r"الأوتار المتقاطعة: \( PA \cdot PB = PC \cdot PD \)؛ المماس والقاطع: \( PT^2 = PA \cdot PB \)"),
            ("نصف قطر الدائرة الداخلة للقائم", r"لساقين \( a, b \) ووتر \( c \): \( r = \frac{a + b - c}{2} \) ونصف قطر الخارجة \( R = \frac{c}{2} \)"),
        ],
    ),
    "KANG-L4-04": _cs(
        [
            ("Isosceles Trapezoid Split", r"Dropping both altitudes splits \( b_2 \) into \( \frac{b_2 - b_1}{2} + b_1 + \frac{b_2 - b_1}{2} \)"),
            ("Euler's Polyhedron Formula", r"\( V - E + F = 2 \); slicing a degree-\( d \) corner changes \( (V, E, F) \) by \( +(d - 1, d, 1) \)"),
            ("3D Inscribed Diagonals", r"Cube of side \( s \) inscribed in sphere of diameter \( 2R \): \( s\sqrt{3} = 2R \)"),
            ("Manhattan Diamond Area", r"\( |x| + |y| \le R \) is a tilted square with diagonals \( 2R \): \(\text{Area} = 2R^2\), lattice points \(= 2R^2 + 2R + 1\)"),
        ],
        [
            ("إسقاط ارتفاعي شبه المنحرف المتساوي الساقين", r"إسقاط الارتفاعين يقسم القاعدة الكبرى \( b_2 \) إلى \( \frac{b_2 - b_1}{2} + b_1 + \frac{b_2 - b_1}{2} \)"),
            ("صيغة أويلر لكثيرات الوجوه", r"\( V - E + F = 2 \)؛ قطع رأس درجته \( d \) يغيّر \( (V, E, F) \) بمقدار \( +(d - 1, d, 1) \)"),
            ("قطر المكعب المحاط بكرة", r"مكعب طول حرفه \( s \) داخل كرة قطرها \( 2R \) يحقق \( s\sqrt{3} = 2R \)"),
            ("معين مسافة مانهاتن", r"\( |x| + |y| \le R \) مربع مائل مساحته \( 2R^2 \) وعدد نقاطه الصحيحة \( 2R^2 + 2R + 1 \)"),
        ],
    ),
    "KANG-L4-05": _cs(
        [
            ("Zero-Split Digit Counting", r"Never let \( 0 \) lead; for even/divisible-by-5 numbers, split into Case 1 (ends in \( 0 \)) + Case 2 (ends in non-zero)"),
            ("Stars and Bars Bijection", r"\( x_1 + \dots + x_k = n \) has \( \binom{n + k - 1}{k - 1} \) non-negative solutions and \( \binom{n - 1}{k - 1} \) positive solutions"),
            ("Take-Away Game Modulo Rule", r"Removing \( 1..m \) pebbles (last wins): multiples of \( m + 1 \) are losing positions; take \( N \bmod (m + 1) \) first!"),
            ("Coloring Parity Invariant", r"Compare alternating cell sums or \( (x + y) \bmod 2 \) before vs. after every legal move"),
        ],
        [
            ("فصل حالة الصفر في التباديل", r"لا تضع \( 0 \) في اليسار؛ وللأعداد الزوجية افصل الحالة المنتهية بـ \( 0 \) عن غيرها"),
            ("النجوم والفواصل (Stars & Bars)", r"للمعادلة \( x_1 + \dots + x_k = n \) يوجد \( \binom{n + k - 1}{k - 1} \) حلاً غير سالب و\( \binom{n - 1}{k - 1} \) حلاً موجباً"),
            ("قاعدة الباقي في ألعاب السحب", r"عند سحب \( 1..m \) حصى (الرابح آخر من يسحب): مضاعفات \( m + 1 \) خاسرة؛ اسحب \( N \bmod (m + 1) \)!"),
            ("ثابت التلوين والزوجية", r"قارن مجموع الخلايا الملونة أو زوجية المقدار قبل الحركة القانونية وبعدها"),
        ],
    ),
    "KANG-L4-06": _cs(
        [
            ("Urn Transfer Mean Fraction", r"Moving a random ball from Bag A (fraction \( p_A \) red) to Bag B shifts expected red count in B by \( +p_A \)"),
            ("Geometric Area Probability", r"\( P(E) = \frac{\text{Area}(E)}{\text{Area}(\Omega)} \); for \( |x - y| \le c \) on \( [0, T]^2 \): \( P = 1 - \left(1 - \frac{c}{T}\right)^2 \)"),
            ("Mean vs Median Bounds", r"With fixed sum \( S = n\bar{x} \) and median \( M \), maximize \( x_n \) by minimizing \( x_1, \dots, x_{n-1} \)"),
            ("Signed Pipe-Tank Rate", r"Net fill fraction per hour \(= \frac{1}{t_{\text{in}}} - \frac{1}{t_{\text{out}}}\); time to fill \(= \frac{1}{r_{\text{net}}}\)"),
        ],
        [
            ("احتمال النقل بين الكيسين", r"نقل كرة عشوائية من كيس نسبة الحمر فيه \( p_A \) يضيف في المتوسط \( +p_A \) كرة حمراء للكيس الثاني"),
            ("الاحتمال الهندسي بالمساحات", r"\( P(E) = \frac{\text{مساحة}(E)}{\text{مساحة}(\Omega)} \)؛ وللشرط \( |x - y| \le c \) على \( [0, T]^2 \): \( P = 1 - \left(1 - \frac{c}{T}\right)^2 \)"),
            ("الحدود القصوى للمتوسط والوسيط", r"لتعظيم عنصر مع ثبات المتوسط والوسيط، اجعل بقية العناصر عند أدنى قيمها المسموحة"),
            ("معدل الملء والتفريغ الصافي", r"المعدل الصافي في الساعة \(= \frac{1}{t_{\text{ملء}}} - \frac{1}{t_{\text{تفريغ}}}\)؛ والزمن \(= \frac{1}{r_{\text{صافي}}}\)"),
        ],
    ),
    # ── Student (Grades 11–12): KANG-L5-01 .. KANG-L5-06 ──
    "KANG-L5-01": _cs(
        [
            ("Euler's Totient Function", r"\( \varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right) \), and \( a^{\varphi(n)} \equiv 1 \pmod n \) when \( \gcd(a, n) = 1 \)"),
            ("Frobenius Coin Formula", r"For coprime \( a, b > 1 \): largest unattainable \(= ab - a - b\); unattainable count \(= \frac{(a - 1)(b - 1)}{2} \)"),
            ("Parity Factoring of x² − y² = N", r"\( (x - y)(x + y) = N \) requires same-parity factors \( d_1, d_2 \) (\( N \equiv 2 \pmod 4 \) has NO solutions!)"),
            ("Base-b Place Expansion", r"\( (d_k \dots d_1 d_0)_b = \sum_{i=0}^{k} d_i b^i \) with digits \( 0 \le d_i < b \)"),
        ],
        [
            ("دالة أويلر ومبرهنة أويلر", r"\( \varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right) \)، و\( a^{\varphi(n)} \equiv 1 \pmod n \) عند \( \gcd(a, n) = 1 \)"),
            ("مبرهنة فروبينيوس للطوابع", r"لعددين أوليين نسبياً \( a, b > 1 \): أكبر مبلغ مستحيل \(= ab - a - b\) وعدد المبالغ المستحيلة \(= \frac{(a - 1)(b - 1)}{2} \)"),
            ("زوجية عوامل فرق المربعين", r"\( (x - y)(x + y) = N \) تتطلب عاملين من نفس الزوجية (\( N \equiv 2 \pmod 4 \) ليس لها حل صحيح!)"),
            ("التحليل المكاني في الأساس b", r"\( (d_k \dots d_1 d_0)_b = \sum_{i=0}^{k} d_i b^i \) بشرط \( 0 \le d_i < b \)"),
        ],
    ),
    "KANG-L5-02": _cs(
        [
            ("Cubic Vieta & Newton Sums", r"For \( x^3 - s_1 x^2 + s_2 x - s_3 = 0 \): \( \sum r_i^2 = s_1^2 - 2s_2 \) and \( \sum r_i^3 = s_1^3 - 3s_1 s_2 + 3s_3 \)"),
            ("Auxiliary Polynomial Trick", r"If \( P(k) = g(k) \) for \( k = 1..d \) on monic degree-\( d \) \( P - g \), then \( P(x) - g(x) = \prod_{k=1}^{d} (x - k) \)"),
            ("Involution Substitution", r"For \( a f(x) + b f(T(x)) = h(x) \) where \( T(T(x)) = x \), plug in \( T(x) \) and solve the \( 2 \times 2 \) linear system"),
            ("Balanced AM-GM Optimization", r"Split terms into equal pieces so their product is constant (e.g., \( x + \frac{a}{x^2} = \frac{x}{2} + \frac{x}{2} + \frac{a}{x^2} \ge 3\sqrt[3]{\frac{a}{4}} \))"),
        ],
        [
            ("علاقات فييت التكعيبية ومجاميع نيوتن", r"للمعادلة \( x^3 - s_1 x^2 + s_2 x - s_3 = 0 \): \( \sum r_i^2 = s_1^2 - 2s_2 \) و\( \sum r_i^3 = s_1^3 - 3s_1 s_2 + 3s_3 \)"),
            ("حيلة كثيرة الحدود المساعدة", r"إذا تحققت \( P(k) = g(k) \) لعدد \( d \) من الجذور وكانت \( P - g \) واحدية من الدرجة \( d \): \( P(x) - g(x) = \prod_{k=1}^{d} (x - k) \)"),
            ("تعويض الدوال الالتفافية", r"إذا كان \( T(T(x)) = x \) في \( a f(x) + b f(T(x)) = h(x) \)، عوّض \( T(x) \) وحل نظام المعادلتين"),
            ("موازنة الحدود في AM-GM", r"قسّم المتغير إلى أجزاء متساوية لثبات الجداء: \( \frac{x}{2} + \frac{x}{2} + \frac{a}{x^2} \ge 3\sqrt[3]{\frac{a}{4}} \)"),
        ],
    ),
    "KANG-L5-03": _cs(
        [
            ("Ceva & Menelaus Ratios", r"Ceva (concurrent) & Menelaus (collinear): \( \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1 \)"),
            ("Common External Tangent", r"Between circles of radii \( R, r \) at center distance \( d \): \( L_{\text{ext}} = \sqrt{d^2 - (R - r)^2} \) (touching: \( 2\sqrt{Rr} \))"),
            ("Pitot's Tangential Quad", r"A convex quadrilateral \( ABCD \) has an incircle iff \( AB + CD = BC + DA \), with \( [ABCD] = r \cdot s \)"),
            ("Apollonius & Angle Bisector", r"Median: \( m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4} \); Bisector: \( \frac{BD}{DC} = \frac{c}{b} \) and \( \ell_a^2 = bc - BD \cdot DC \)"),
        ],
        [
            ("مبرهنتا سيفا ومنيلاوس", r"سيفا (تلاقي) ومنيلاوس (استقامة): \( \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1 \)"),
            ("طول المماس المشترك الخارجي", r"لدائرتين نصفا قطريهما \( R, r \) والبعد \( d \): \( L_{\text{ext}} = \sqrt{d^2 - (R - r)^2} \) (وعند التماس \( 2\sqrt{Rr} \))"),
            ("مبرهنة بيتو للرباعي المماسي", r"يقبل الرباعي دائرة داخلة إذا وفقط إذا كان \( AB + CD = BC + DA \)، ومساحته \( r \cdot s \)"),
            ("أبولونيوس ومنصّف الزاوية", r"المتوسط: \( m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4} \)؛ المنصف: \( \frac{BD}{DC} = \frac{c}{b} \) و\( \ell_a^2 = bc - BD \cdot DC \)"),
        ],
    ),
    "KANG-L5-04": _cs(
        [
            ("Archimedes 2 : 3 Sphere Law", r"Sphere in cylinder (\( h = 2r \)): \( V_{\text{sph}} : V_{\text{cyl}} = \frac{4}{3}\pi r^3 : 2\pi r^3 = 2 : 3 \) (and total surface \( 2 : 3 \)!)"),
            ("Cone & Frustum Cubic Scaling", r"Slicing at height ratio \( k \): \( V_{\text{top}} = k^3 V \); frustum \( V = \frac{1}{3}\pi h(R^2 + Rr + r^2) \)"),
            ("Right-Corner Tetrahedron Slice", r"Orthogonal corner legs \( a, b, c \): \( V = \frac{abc}{6} \) and de Gua face law \( [ABC]^2 = \frac{a^2b^2 + b^2c^2 + c^2a^2}{4} \)"),
            ("Reflections & Pick's Theorem", r"Reflect target across each mirror for shortest path; lattice polygon area \( A = I + \frac{B}{2} - 1 \)"),
        ],
        [
            ("قانون أرخميدس 2 : 3 للكرة والأسطوانة", r"كرة محاطة بأسطوانة (\( h = 2r \)): نسبة الحجمين ونسبة المساحتين الكليتين تساويان \( 2 : 3 \)"),
            ("التشابه التكعيبي للمخروط والناقص", r"القطع بنسبة ارتفاع \( k \) يعطي \( V_{\text{علوي}} = k^3 V \)؛ وحجم الجذع \( \frac{1}{3}\pi h(R^2 + Rr + r^2) \)"),
            ("رباعي الوجوه القائم الركن", r"لأحرف متعامدة \( a, b, c \): الحجم \( V = \frac{abc}{6} \) ومبرهنة دي غوا \( [ABC]^2 = \frac{a^2b^2 + b^2c^2 + c^2a^2}{4} \)"),
            ("الانعكاس ومبرهنة بيك", r"اعكس الهدف عبر المرايا لأقصر مسار؛ ومساحة المضلع الشبكي \( A = I + \frac{B}{2} - 1 \)"),
        ],
    ),
    "KANG-L5-05": _cs(
        [
            ("Catalan & Ballot Numbers", r"\( C_n = \frac{1}{n + 1}\binom{2n}{n} \) (\( 1, 1, 2, 5, 14, 42 \)); strict ballot lead: \( \frac{p - q}{p + q}\binom{p + q}{p} \)"),
            ("Derangements (No Fixed Point)", r"\( D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} \implies D_1 = 0,\; D_2 = 1,\; D_3 = 2,\; D_4 = 9,\; D_5 = 44 \)"),
            ("Chromatic Polynomial of Cycles", r"Tree on \( n \) vertices: \( k(k - 1)^{n - 1} \); cycle \( C_n \): \( (k - 1)^n + (-1)^n(k - 1) \)"),
            ("Linear Tiling Recurrences", r"Condition on the first block placed: \( 2 \times n \) domino tiling satisfies \( a_n = a_{n - 1} + a_{n - 2} \)"),
        ],
        [
            ("أعداد كاتالان ومسارات الاقتراع", r"\( C_n = \frac{1}{n + 1}\binom{2n}{n} \) (\( 1, 1, 2, 5, 14, 42 \))؛ وتقدّم الاقتراع الصارم \( \frac{p - q}{p + q}\binom{p + q}{p} \)"),
            ("التشويشات الكاملة (بلا نقاط ثابتة)", r"\( D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} \implies D_1 = 0,\; D_2 = 1,\; D_3 = 2,\; D_4 = 9,\; D_5 = 44 \)"),
            ("تلوين الأشجار والدورات البيانية", r"شجرة من \( n \) رؤوس بـ \( k \) ألوان: \( k(k - 1)^{n - 1} \)؛ ودورة \( C_n \): \( (k - 1)^n + (-1)^n(k - 1) \)"),
            ("العلاقات التراجعية للتبليط", r"افصل حسب أول قطعة توضع: تبليط شريط \( 2 \times n \) يحقق \( a_n = a_{n - 1} + a_{n - 2} \)"),
        ],
    ),
    "KANG-L5-06": _cs(
        [
            ("Bayes' Posterior Ratio", r"\( P(A_i \mid E) = \frac{P(A_i) P(E \mid A_i)}{\sum_j P(A_j) P(E \mid A_j)} \)"),
            ("Linearity of Expectation", r"\( E\!\left[\sum X_i\right] = \sum E[X_i] \) ALWAYS (even for dependent indicators!); fixed points of random \( \pi \): \( E = 1 \)"),
            ("Geometric Meeting Square", r"Arrivals \( X, Y \in [0, T] \) meet within wait \( w \): \( P(|X - Y| \le w) = 1 - \left(1 - \frac{w}{T}\right)^2 \)"),
            ("1D Symmetric Random Walk", r"On \( \{0, \dots, N\} \) starting at \( k \): \( P(\text{hit } N \text{ before } 0) = \frac{k}{N} \) and \( E[\text{steps}] = k(N - k) \)"),
        ],
        [
            ("قانون بايز للاحتمال الشرطي", r"\( P(A_i \mid E) = \frac{P(A_i) P(E \mid A_i)}{\sum_j P(A_j) P(E \mid A_j)} \)"),
            ("خطية التوقع الرياضي", r"\( E\!\left[\sum X_i\right] = \sum E[X_i] \) دائماً حتى دون استقلال! وتوقع النقاط الثابتة لتبديل عشوائي \(= 1\)"),
            ("مربع الالتقاء الهندسي", r"وصول عشوائي في \( [0, T] \) مع انتظار \( w \): \( P(|X - Y| \le w) = 1 - \left(1 - \frac{w}{T}\right)^2 \)"),
            ("المشي العشوائي المتماثل", r"على \( \{0, \dots, N\} \) بدءاً من \( k \): احتمال بلوغ \( N \) قبل \( 0 \) هو \( \frac{k}{N} \) وتوقع الخطوات \( k(N - k) \)"),
        ],
    ),
}
