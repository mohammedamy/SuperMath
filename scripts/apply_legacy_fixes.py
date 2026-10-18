import json
from pathlib import Path

ROOT = Path("/Users/mohammedamy/Developer/SuperMath")

clean_replacements = {
    # 1. JEE-226: Definite integral x*e^(2x) dx from 0 to 1 = (e^2 + 1)/4
    "JEE-226": {
        "id": "JEE-226",
        "track": "jee",
        "level": "Grade 12",
        "topic": "Calculus",
        "type": "MCQ",
        "difficulty": "Hard",
        "correct_index": 2,
        "correct_answer": "\\( \\frac{e^2 + 1}{4} \\)",
        "content": {
            "en": {
                "question": "Evaluate the definite integral \\( \\int_0^1 x e^{2x} \\, dx \\).",
                "options": [
                    "\\( \\frac{e^2 - 1}{2} \\)",
                    "\\( \\frac{e^2 - 1}{4} \\)",
                    "\\( \\frac{e^2 + 1}{4} \\)",
                    "\\( \\frac{e^2 + 1}{2} \\)"
                ],
                "hint": "Use integration by parts: \\( \\int u v' dx = uv - \\int u' v dx \\) with \\( u = x \\) and \\( v' = e^{2x} \\).",
                "explanation": "Let \\( u = x \\implies du = dx \\), and \\( dv = e^{2x} dx \\implies v = \\frac{1}{2}e^{2x} \\). Then \\( \\int_0^1 x e^{2x} dx = \\left[ \\frac{x}{2}e^{2x} \\right]_0^1 - \\int_0^1 \\frac{1}{2}e^{2x} dx = \\frac{e^2}{2} - \\left[ \\frac{1}{4}e^{2x} \\right]_0^1 = \\frac{e^2}{2} - \\frac{e^2 - 1}{4} = \\frac{e^2 + 1}{4} \\)."
            },
            "ar": {
                "question": "احسب التكامل المحدد \\( \\int_0^1 x e^{2x} \\, dx \\).",
                "options": [
                    "\\( \\frac{e^2 - 1}{2} \\)",
                    "\\( \\frac{e^2 - 1}{4} \\)",
                    "\\( \\frac{e^2 + 1}{4} \\)",
                    "\\( \\frac{e^2 + 1}{2} \\)"
                ],
                "hint": "استخدم التكامل بالتجزئة: \\( u = x \\) و \\( dv = e^{2x} dx \\).",
                "explanation": "بالتكامل بالتجزئة: \\( \\left[ \\frac{x}{2}e^{2x} \\right]_0^1 - \\frac{1}{2}\\int_0^1 e^{2x}dx = \\frac{e^2}{2} - \\frac{e^2-1}{4} = \\frac{e^2 + 1}{4} \\)."
            }
        }
    },

    # 2. KAUST-F-04: Principal argument of z = -sqrt(3) + i
    "KAUST-F-04": {
        "id": "KAUST-F-04",
        "track": "kaust",
        "level": "Phase 1: Foundation Research",
        "topic": "Complex Numbers",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 1,
        "correct_answer": "\\( \\frac{5\\pi}{6} \\)",
        "content": {
            "en": {
                "question": "Find the principal argument \\( \\operatorname{Arg}(z) \\) of the complex number \\( z = -\\sqrt{3} + i \\), where \\( \\operatorname{Arg}(z) \\in (-\\pi, \\pi] \\).",
                "options": [
                    "\\( \\frac{2\\pi}{3} \\)",
                    "\\( \\frac{5\\pi}{6} \\)",
                    "\\( -\\frac{\\pi}{6} \\)",
                    "\\( \\frac{7\\pi}{6} \\)"
                ],
                "hint": "The complex number lies in the second quadrant where \\( x < 0 \\) and \\( y > 0 \\).",
                "explanation": "Here \\( x = -\\sqrt{3} \\) and \\( y = 1 \\). Since \\( z \\) is in Quadrant II, \\( \\operatorname{Arg}(z) = \\pi - \\arctan(1/\\sqrt{3}) = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6} \\)."
            },
            "ar": {
                "question": "أوجد السعة الأساسية \\( \\operatorname{Arg}(z) \\) للعدد المركب \\( z = -\\sqrt{3} + i \\)، حيث \\( \\operatorname{Arg}(z) \\in (-\\pi, \\pi] \\).",
                "options": [
                    "\\( \\frac{2\\pi}{3} \\)",
                    "\\( \\frac{5\\pi}{6} \\)",
                    "\\( -\\frac{\\pi}{6} \\)",
                    "\\( \\frac{7\\pi}{6} \\)"
                ],
                "hint": "العدد المركب يقع في الربع الثاني حيث الجزء الحقيقي سالب والتخيلي موجب.",
                "explanation": "بما أن النقطة في الربع الثاني، فإن السعة تساوي \\( \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6} \\)."
            }
        }
    },

    # 3. KAUST-003-R175: Two dice sum equals 9
    "KAUST-003-R175": {
        "id": "KAUST-003-R175",
        "track": "kaust",
        "level": "Phase 2: Advanced Analysis",
        "topic": "Probability",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 2,
        "correct_answer": "\\( \\frac{1}{9} \\)",
        "content": {
            "en": {
                "question": "Two fair standard six-sided dice are rolled simultaneously. What is the probability that the sum of the two numbers rolled is exactly 9?",
                "options": [
                    "\\( \\frac{1}{12} \\)",
                    "\\( \\frac{5}{36} \\)",
                    "\\( \\frac{1}{9} \\)",
                    "\\( \\frac{7}{36} \\)"
                ],
                "hint": "List all ordered pairs \\( (a, b) \\) with \\( 1 \\le a, b \\le 6 \\) such that \\( a + b = 9 \\).",
                "explanation": "The favorable pairs are \\( (3,6), (4,5), (5,4), (6,3) \\), giving 4 outcomes out of \\( 6 \\times 6 = 36 \\). The probability is \\( \\frac{4}{36} = \\frac{1}{9} \\)."
            },
            "ar": {
                "question": "أُلقي حجرَا نرد منتظمان وذوا 6 أوجه في آن واحد. ما احتمال أن يكون مجموع العددين الظاهرين 9 تمامًا؟",
                "options": [
                    "\\( \\frac{1}{12} \\)",
                    "\\( \\frac{5}{36} \\)",
                    "\\( \\frac{1}{9} \\)",
                    "\\( \\frac{7}{36} \\)"
                ],
                "hint": "احصر جميع الأزواج المرتبة التي مجموعها 9.",
                "explanation": "الأزواج هي \\( (3,6), (4,5), (5,4), (6,3) \\) أي 4 حالات من 36، فالاحتمال \\( \\frac{4}{36} = \\frac{1}{9} \\)."
            }
        }
    },

    # 4. NAFES-250: 15% VAT on 400 SAR
    "NAFES-250": {
        "id": "NAFES-250",
        "track": "nafes",
        "level": "Grade 6",
        "topic": "Arithmetic",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 1,
        "correct_answer": "\\( 460 \\text{ SAR} \\)",
        "content": {
            "en": {
                "question": "A tablet device costs \\( 400 \\text{ SAR} \\) before tax. If a value-added tax (VAT) of \\( 15\\% \\) is added, what is the final price of the tablet?",
                "options": [
                    "\\( 440 \\text{ SAR} \\)",
                    "\\( 460 \\text{ SAR} \\)",
                    "\\( 475 \\text{ SAR} \\)",
                    "\\( 480 \\text{ SAR} \\)"
                ],
                "hint": "Calculate 15% of 400 SAR, then add it to the original price.",
                "explanation": "Tax amount = \\( 400 \\times 0.15 = 60 \\text{ SAR} \\). Total price = \\( 400 + 60 = 460 \\text{ SAR} \\)."
            },
            "ar": {
                "question": "سعر جهاز لوحي قبل الضريبة هو \\( 400 \\text{ ريال} \\). إذا أُضيفت ضريبة القيمة المضافة بنسبة \\( 15\\% \\)، فما السعر النهائي للجهاز؟",
                "options": [
                    "\\( 440 \\text{ ريال} \\)",
                    "\\( 460 \\text{ ريال} \\)",
                    "\\( 475 \\text{ ريال} \\)",
                    "\\( 480 \\text{ ريال} \\)"
                ],
                "hint": "احسب 15% من 400 ريال ثم أضفها إلى السعر الأصلي.",
                "explanation": "قيمة الضريبة = \\( 400 \\times 0.15 = 60 \\text{ ريال} \\). السعر النهائي = \\( 400 + 60 = 460 \\text{ ريال} \\)."
            }
        }
    },

    # 5. KAN-JUN-05: units digit of 2^2025 + 6^2025
    "KAN-JUN-05": {
        "id": "KAN-JUN-05",
        "track": "kangaroo",
        "level": "Junior",
        "topic": "Number Theory",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 3,
        "correct_answer": "\\( 8 \\)",
        "content": {
            "en": {
                "question": "What is the units digit of the sum \\( 2^{2025} + 6^{2025} \\)?",
                "options": [
                    "\\( 2 \\)",
                    "\\( 4 \\)",
                    "\\( 6 \\)",
                    "\\( 8 \\)",
                    "\\( 0 \\)"
                ],
                "hint": "Powers of 2 repeat in a cycle of length 4, while powers of 6 always end in 6.",
                "explanation": "\\( 2^{2025} = 2^{4 \\times 506 + 1} \\) ends in 2. Any positive power of 6 ends in 6. Thus, the units digit of the sum is \\( 2 + 6 = 8 \\)."
            },
            "ar": {
                "question": "ما رقم آحاد المجموع \\( 2^{2025} + 6^{2025} \\)؟",
                "options": [
                    "\\( 2 \\)",
                    "\\( 4 \\)",
                    "\\( 6 \\)",
                    "\\( 8 \\)",
                    "\\( 0 \\)"
                ],
                "hint": "قوى 2 دورية بطول 4، وقوى 6 تنتهي دائمًا بالرقم 6.",
                "explanation": "\\( 2^{2025} = 2^{4 \\times 506 + 1} \\) ينتهي بالرقم 2. و \\( 6^{2025} \\) ينتهي دائمًا بالرقم 6. إذن رقم الآحاد هو \\( 2 + 6 = 8 \\)."
            }
        }
    },

    # 6. NSMO-P3-065: Largest prime factor of 2^16 - 1
    "NSMO-P3-065": {
        "id": "NSMO-P3-065",
        "track": "nsmo",
        "level": "Phase 3: Senior National Olympiad (Grades 10-12)",
        "topic": "Number Theory",
        "type": "MCQ",
        "difficulty": "Hard",
        "correct_index": 2,
        "correct_answer": "\\( 257 \\)",
        "content": {
            "en": {
                "question": "What is the largest prime factor of the integer \\( 2^{16} - 1 \\)?",
                "options": [
                    "\\( 17 \\)",
                    "\\( 67 \\)",
                    "\\( 257 \\)",
                    "\\( 641 \\)"
                ],
                "hint": "Factor \\( 2^{16} - 1 \\) as a difference of squares repeatedly: \\( (2^8+1)(2^4+1)(2^2+1)(2+1)(2-1) \\).",
                "explanation": "\\( 2^{16}-1 = (2^8+1)(2^8-1) = (257)(2^4+1)(2^4-1) = 257 \\times 17 \\times 15 = 257 \\times 17 \\times 5 \\times 3 \\). The prime 257 is a Fermat prime \\( F_3 \\), and is the largest prime factor."
            },
            "ar": {
                "question": "ما هو أكبر قاسم أولي للعدد الصحيح \\( 2^{16} - 1 \\)؟",
                "options": [
                    "\\( 17 \\)",
                    "\\( 67 \\)",
                    "\\( 257 \\)",
                    "\\( 641 \\)"
                ],
                "hint": "حلل المقدار باستخدام فرق المربعات المتكرر.",
                "explanation": "\\( 2^{16}-1 = (2^8+1)(2^8-1) = 257 \\times 17 \\times 5 \\times 3 \\). أكبر قاسم أولي هو 257."
            }
        }
    },

    # 7. OLYMPIAD-111: Prove 7 does not divide n^3 + 2
    "OLYMPIAD-111": {
        "id": "OLYMPIAD-111",
        "track": "olympiad",
        "level": "High School",
        "topic": "Number Theory",
        "type": "FRQ",
        "difficulty": "Hard",
        "assessment": "self_assessment",
        "content": {
            "en": {
                "question": "Prove that there is no positive integer \\( n \\) such that \\( n^3 + 2 \\) is divisible by \\( 7 \\). Give a complete mathematical justification.",
                "options": [],
                "hint": "Examine the possible remainders of \\( n^3 \\) modulo 7 by testing all residue classes \\( n \\equiv 0, 1, 2, 3, 4, 5, 6 \\pmod 7 \\).",
                "explanation": "For any integer \\( n \\), cubic residues modulo 7 are \\( 0^3 \\equiv 0 \\), \\( (\\pm 1)^3 \\equiv \\pm 1 \\), \\( (\\pm 2)^3 = \\pm 8 \\equiv \\pm 1 \\), and \\( (\\pm 3)^3 = \\pm 27 \\equiv \\mp 1 \\pmod 7 \\). Hence \\( n^3 \\pmod 7 \\in \\{0, 1, 6\\} \\). Adding 2 yields \\( n^3 + 2 \\pmod 7 \\in \\{2, 3, 1\\} \\), none of which is divisible by 7."
            },
            "ar": {
                "question": "أثبت أنه لا يوجد عدد صحيح موجب \\( n \\) بحيث يقبل \\( n^3 + 2 \\) القسمة على \\( 7 \\). قدّم برهانًا رياضيًا متكاملاً.",
                "options": [],
                "hint": "ادرس فئات البواقي الممكنة لـ \\( n^3 \\) بترديد 7.",
                "explanation": "بواقي المكعبات الكاملة بترديد 7 هي \\( \\{0, 1, 6\\} \\) فقط. وبإضافة 2 تصبح البواقي \\( \\{2, 3, 1\\} \\)، ولا يوجد بينها الصفر. إذن لا يمكن لـ \\( n^3 + 2 \\) أن يقبل القسمة على 7."
            }
        }
    },

    # 8. KANGAROO-247: Grid paths (0,0) to (4,3) avoiding (2,2)
    "KANGAROO-247": {
        "id": "KANGAROO-247",
        "track": "kangaroo",
        "level": "Cadet",
        "topic": "Combinatorics",
        "type": "MCQ",
        "difficulty": "Hard",
        "correct_index": 2,
        "correct_answer": "\\( 17 \\)",
        "content": {
            "en": {
                "question": "A grid has vertices from \\( (0,0) \\) to \\( (4,3) \\). A path moves only right or up along grid lines. If the intersection point \\( (2,2) \\) is blocked and cannot be visited, how many valid paths are there from \\( (0,0) \\) to \\( (4,3) \\)?",
                "options": [
                    "\\( 13 \\)",
                    "\\( 15 \\)",
                    "\\( 17 \\)",
                    "\\( 19 \\)",
                    "\\( 21 \\)"
                ],
                "hint": "Subtract the number of paths that pass through (2,2) from the total unrestricted paths.",
                "explanation": "Total unrestricted paths: \\( \\binom{4+3}{3} = \\binom{7}{3} = 35 \\). Paths passing through \\( (2,2) \\): from \\( (0,0) \\) to \\( (2,2) \\) is \\( \\binom{4}{2} = 6 \\), and from \\( (2,2) \\) to \\( (4,3) \\) is \\( \\binom{2+1}{1} = 3 \\), giving \\( 6 \\times 3 = 18 \\). Paths avoiding \\( (2,2) \\) = \\( 35 - 18 = 17 \\)."
            },
            "ar": {
                "question": "شبكة إحداثيات تمتد من \\( (0,0) \\) إلى \\( (4,3) \\). يتحرك مسار بخطوات وحدة يمينًا أو لأعلى فقط. إذا كانت النقطة \\( (2,2) \\) مغلقة ولا يمكن المرور بها، فكم مسارًا متاحًا من \\( (0,0) \\) إلى \\( (4,3) \\)؟",
                "options": [
                    "\\( 13 \\)",
                    "\\( 15 \\)",
                    "\\( 17 \\)",
                    "\\( 19 \\)",
                    "\\( 21 \\)"
                ],
                "hint": "اطرح عدد المسارات المارة بالنقطة (2,2) من إجمالي المسارات.",
                "explanation": "إجمالي المسارات = \\( \\binom{7}{3} = 35 \\). المسارات المارة بـ (2,2) = \\( \\binom{4}{2} \\times \\binom{3}{1} = 6 \\times 3 = 18 \\). المسارات المتاحة = \\( 35 - 18 = 17 \\)."
            }
        }
    },

    # 9. KANGAROO-112: Counterfeit coin balance scale
    "KANGAROO-112": {
        "id": "KANGAROO-112",
        "track": "kangaroo",
        "level": "Cadet",
        "topic": "Logic",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 1,
        "correct_answer": "\\( 3 \\)",
        "content": {
            "en": {
                "question": "You have \\( 27 \\) identical-looking gold coins, one of which is counterfeit and slightly heavier than the others. What is the minimum number of weighings on a two-pan balance scale guaranteed to identify the fake coin?",
                "options": [
                    "\\( 2 \\)",
                    "\\( 3 \\)",
                    "\\( 4 \\)",
                    "\\( 5 \\)",
                    "\\( 6 \\)"
                ],
                "hint": "Each weighing on a two-pan balance can partition the coins into 3 groups of equal size.",
                "explanation": "With a two-pan balance, each weighing divides the candidates by 3. Since \\( 3^3 = 27 \\), exactly 3 weighings suffice: 27 -> 9 -> 3 -> 1."
            },
            "ar": {
                "question": "لديك \\( 27 \\) قطعة نقدية ذهبية متطابقة في المظهر، إحداها مزيفة وأثقل وزنًا بقليل من الأخريات. ما هو الحد الأدنى لعدد مرات الوزن بميزان ذي كفتين الذي يضمن لك بالتأكيد تحديد القطعة المزيفة؟",
                "options": [
                    "\\( 2 \\)",
                    "\\( 3 \\)",
                    "\\( 4 \\)",
                    "\\( 5 \\)",
                    "\\( 6 \\)"
                ],
                "hint": "كل وزنة بميزان ذي كفتين تقسم الاحتمالات إلى 3 أجزاء متساوية لأن \\( 3^k \\ge 27 \\).",
                "explanation": "بما أن \\( 3^3 = 27 \\)، فإن 3 وزنات تكفي تمامًا بتقسيم القطع إلى ثلاث مجموعات في كل مرحلة (9، ثم 3، ثم 1)."
            }
        }
    },

    # 10. KANGAROO-171: Handshake gifts in 6-member club
    "KANGAROO-171": {
        "id": "KANGAROO-171",
        "track": "kangaroo",
        "level": "Cadet",
        "topic": "Combinatorics",
        "type": "MCQ",
        "difficulty": "Hard",
        "correct_index": 2,
        "correct_answer": "\\( 15 \\)",
        "content": {
            "en": {
                "question": "In a social club with 6 members, each member is friends with all other 5 members. If each friendship pair exchanges exactly one commemorative badge, how many badges are exchanged in total?",
                "options": [
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 15 \\)",
                    "\\( 18 \\)",
                    "\\( 30 \\)"
                ],
                "hint": "Calculate the number of edges in a complete graph with 6 vertices: \\( \\binom{6}{2} \\).",
                "explanation": "The number of unique friendship pairs in a complete graph on 6 vertices is \\( \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15 \\). Thus 15 badges are exchanged."
            },
            "ar": {
                "question": "في نادٍ اجتماعي يضم 6 أعضاء، يرتبط كل عضو بصداقة مع جميع الأعضاء الـ 5 الآخرين. إذا تبادل كل صديقين شارة تذكارية واحدة، فما إجمالي عدد الشارات المتبادلة؟",
                "options": [
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 15 \\)",
                    "\\( 18 \\)",
                    "\\( 30 \\)"
                ],
                "hint": "احسب عدد أضلاع البيان الكامل ذي 6 رؤوس: \\( \\binom{6}{2} \\).",
                "explanation": "عدد أزواج الأصدقاء هو \\( \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15 \\) شارة."
            }
        }
    },

    # 11. KANGAROO-208: Total edges of hexagonal prism
    "KANGAROO-208": {
        "id": "KANGAROO-208",
        "track": "kangaroo",
        "level": "Cadet",
        "topic": "Geometry",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 3,
        "correct_answer": "\\( 18 \\)",
        "content": {
            "en": {
                "question": "A right prism has regular hexagonal bases and 6 rectangular lateral faces. What is the total number of edges of this prism?",
                "options": [
                    "\\( 12 \\)",
                    "\\( 14 \\)",
                    "\\( 16 \\)",
                    "\\( 18 \\)",
                    "\\( 24 \\)"
                ],
                "hint": "An n-gonal prism has n edges on each of its two bases, plus n lateral edges.",
                "explanation": "For an n-gonal prism, total edges = \\( 3n \\). Since \\( n = 6 \\), total edges = \\( 3 \\times 6 = 18 \\)."
            },
            "ar": {
                "question": "منشور قائم له قاعدتان سداسيتان منتظمتان و6 أوجه جانبية مستطيلة. ما العدد الكلي لحواف (أضلاع) هذا المنشور؟",
                "options": [
                    "\\( 12 \\)",
                    "\\( 14 \\)",
                    "\\( 16 \\)",
                    "\\( 18 \\)",
                    "\\( 24 \\)"
                ],
                "hint": "المنشور ذو القاعدة ذات n أضلاع يمتلك 3n حافة.",
                "explanation": "عدد الحواف في منشور قاعدته سداسية (n = 6) هو \\( 3 \\times 6 = 18 \\) حافة."
            }
        }
    },

    # 12. NSMO-105: Solve linear fractional equation
    "NSMO-105": {
        "id": "NSMO-105",
        "track": "nsmo",
        "level": "Phase 2: Intermediate Olympiad (Grades 8-9)",
        "topic": "Algebra",
        "type": "MCQ",
        "difficulty": "Medium",
        "correct_index": 2,
        "correct_answer": "\\( 11 \\)",
        "content": {
            "en": {
                "question": "Solve for \\( x \\) in the linear equation: \\( \\frac{3x - 5}{4} = \\frac{x + 1}{2} + 1 \\).",
                "options": [
                    "\\( 9 \\)",
                    "\\( 10 \\)",
                    "\\( 11 \\)",
                    "\\( 12 \\)"
                ],
                "hint": "Multiply the entire equation by the common denominator 4 to eliminate all fractions.",
                "explanation": "Multiply by 4: \\( 3x - 5 = 2(x + 1) + 4 \\implies 3x - 5 = 2x + 6 \\implies 3x - 2x = 6 + 5 \\implies x = 11 \\)."
            },
            "ar": {
                "question": "أوجد قيمة \\( x \\) في المعادلة الخطية: \\( \\frac{3x - 5}{4} = \\frac{x + 1}{2} + 1 \\).",
                "options": [
                    "\\( 9 \\)",
                    "\\( 10 \\)",
                    "\\( 11 \\)",
                    "\\( 12 \\)"
                ],
                "hint": "اضرب المعادلة كاملة في المضاعف المشترك 4 للتخلص من المقامات.",
                "explanation": "بالضرب في 4: \\( 3x - 5 = 2(x + 1) + 4 \\implies 3x - 5 = 2x + 6 \\implies x = 11 \\)."
            }
        }
    },

    # 13. NAFES-3-107: Box of chocolates remaining
    "NAFES-3-107": {
        "id": "NAFES-3-107",
        "track": "nafes",
        "level": "Grade 3",
        "topic": "Arithmetic",
        "type": "MCQ",
        "difficulty": "Easy",
        "correct_index": 1,
        "correct_answer": "\\( 10 \\)",
        "content": {
            "en": {
                "question": "A box contains 24 pieces of chocolate. Sara eats 6 pieces, and her brother eats 8 pieces. How many pieces of chocolate remain in the box?",
                "options": [
                    "\\( 8 \\)",
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 14 \\)"
                ],
                "hint": "Add the pieces eaten by Sara and her brother, then subtract from 24.",
                "explanation": "Total eaten = \\( 6 + 8 = 14 \\). Remaining = \\( 24 - 14 = 10 \\)."
            },
            "ar": {
                "question": "صندوق يحتوي على 24 قطعة شوكولاتة. أكلت سارة 6 قطع، وأكل أخوها 8 قطع. كم قطعة شوكولاتة بقيت في الصندوق؟",
                "options": [
                    "\\( 8 \\)",
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 14 \\)"
                ],
                "hint": "اجمع القطع التي أُكلت ثم اطرحها من 24.",
                "explanation": "مجموع ما أُكل = \\( 6 + 8 = 14 \\). المتبقي = \\( 24 - 14 = 10 \\) قطع."
            }
        }
    },

    # 14. KANG-ECO-073: Distinct options for sides of a hexagon
    "KANG-ECO-073": {
        "id": "KANG-ECO-073",
        "track": "kangaroo",
        "level": "Ecolier",
        "topic": "Geometry",
        "type": "MCQ",
        "difficulty": "Easy",
        "correct_index": 1,
        "correct_answer": "\\( 6 \\)",
        "content": {
            "en": {
                "question": "How many sides does a regular hexagon have?",
                "options": [
                    "\\( 5 \\)",
                    "\\( 6 \\)",
                    "\\( 7 \\)",
                    "\\( 8 \\)",
                    "\\( 10 \\)"
                ],
                "hint": "A hexagon is a polygon with 6 vertices.",
                "explanation": "By definition, any hexagon has 6 straight sides."
            },
            "ar": {
                "question": "كم ضلعًا للمسدس (الشكل السداسي) المنتظم؟",
                "options": [
                    "\\( 5 \\)",
                    "\\( 6 \\)",
                    "\\( 7 \\)",
                    "\\( 8 \\)",
                    "\\( 10 \\)"
                ],
                "hint": "الشكل السداسي هو مضلع له 6 رؤوس.",
                "explanation": "بحسب التعريف الهندسي، الشكل السداسي له 6 أضلاع."
            }
        }
    }
}

for track in ["jee", "kaust", "nafes", "kangaroo", "nsmo", "olympiad"]:
    path = ROOT / "data" / f"{track}.json"
    data = json.loads(path.read_text())
    changed = 0
    for i, q in enumerate(data):
        qid = q["id"]
        if qid in clean_replacements:
            data[i] = clean_replacements[qid]
            changed += 1
            print(f"[{track}] Replaced legacy duplicate {qid}")
    if changed > 0:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print(f"[{track}] Saved {changed} replacements to {path.name}")
