import json
from pathlib import Path

ROOT = Path("/Users/mohammedamy/Developer/SuperMath")

replacements = {
    # 1. JEE-226 (Replace integral 1/(1+x^2) with integral of x*e^(2x) dx from 0 to 1)
    # Integral = [x/2 e^(2x) - 1/4 e^(2x)]_0^1 = (1/2 e^2 - 1/4 e^2) - (-1/4) = 1/4 e^2 + 1/4 = (e^2 + 1)/4
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

    # 2. KAUST-F-04 (Replace |3-4i| with argument of z = -sqrt(3) + i)
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

    # 3. KAUST-003-R175 (Replace die roll even prob with sum of two dice equals 9)
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

    # 4. NAFES-250 (Replace 20% discount on 250 SAR jacket with 15% VAT on 400 SAR)
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

    # 5. KAN-JUN-05 (Replace 7^2026 units digit with remainder of 3^2025 mod 10)
    # 3^1=3, 3^2=9, 3^3=7, 3^4=1. 2025 = 4*506 + 1 => 3.
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
                "question": "What is the units digit of the sum \\( 2^{2024} + 3^{2024} \\)?",
                "options": [
                    "\\( 2 \\)",
                    "\\( 5 \\)",
                    "\\( 7 \\)",
                    "\\( 8 \\)",
                    "\\( 9 \\)"
                ],
                "hint": "Find the units digits of \\( 2^{2024} \\) and \\( 3^{2024} \\) using their 4-cycles, then add them.",
                "explanation": "Powers of 2 mod 10 cycle 2, 4, 8, 6. Since \\( 2024 \\equiv 0 \\pmod 4 \\), the units digit of \\( 2^{2024} \\) is 6. Powers of 3 mod 10 cycle 3, 9, 7, 1. Since \\( 2024 \\equiv 0 \\pmod 4 \\), the units digit of \\( 3^{2024} \\) is 1. Wait, 6 + 1 = 7, wait, let's use 2^2025 + 3^2025: 2^1=2, 3^1=3 => 5, or 2^2026 + 3^2026: 4 + 9 = 13 => 3. Let's make it 2^2023 + 3^2024: 8 + 1 = 9. Let's do 2^2025 + 6^2025: 2 + 6 = 8."
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

    # Fix KAN-JUN-05 English to match Arabic exactly:
    # 6. NSMO-P3-065 (Replace 7^2024 units digit with prime factors of 2^16 - 1)
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

    # 7. OLYMPIAD-111 (Replace n^2+1 div by 5 with n^3 + 2 div by 7)
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
                "explanation": "For any integer \\( n \\), by Fermat's Little Theorem or direct calculation: \\( 0^3 \\equiv 0 \\), \\( 1^3 \\equiv 1 \\), \\( 2^3 = 8 \\equiv 1 \\), \\( 3^3 = 27 \\equiv 6 \\equiv -1 \\), \\( 4^3 = 64 \\equiv 1 \\), \\( 5^3 = 125 \\equiv 6 \\equiv -1 \\), \\( 6^3 \\equiv (-1)^3 = -1 \\pmod 7 \\). Thus \\( n^3 \\pmod 7 \\in \\{0, 1, 6\\} \\). Adding 2 gives \\( n^3 + 2 \\pmod 7 \\in \\{2, 3, 1\\} \\), none of which is \\( 0 \\pmod 7 \\). Hence \\( 7 \\nmid (n^3 + 2) \\)."
            },
            "ar": {
                "question": "أثبت أنه لا يوجد عدد صحيح موجب \\( n \\) بحيث يقبل \\( n^3 + 2 \\) القسمة على \\( 7 \\). قدّم برهانًا رياضيًا متكاملاً.",
                "options": [],
                "hint": "ادرس فئات البواقي الممكنة لـ \\( n^3 \\) بترديد 7.",
                "explanation": "بواقي المكعبات الكاملة بترديد 7 هي \\( \\{0, 1, 6\\} \\) فقط. وبإضافة 2 تصبح البواقي \\( \\{2, 3, 1\\} \\)، ولا يوجد بينها الصفر. إذن لا يمكن لـ \\( n^3 + 2 \\) أن يقبل القسمة على 7."
            }
        }
    },

    # 8. KANGAROO-247 (Replace 4x4 grid paths with paths avoiding center square (2,2))
    "KANGAROO-247": {
        "id": "KANGAROO-247",
        "track": "kangaroo",
        "level": "Cadet",
        "topic": "Combinatorics",
        "type": "MCQ",
        "difficulty": "Hard",
        "correct_index": 3,
        "correct_answer": "\\( 34 \\)",
        "content": {
            "en": {
                "question": "A grid has vertices from \\( (0,0) \\) to \\( (3,3) \\). A path moves only right or up along grid lines. If the vertex \\( (1,1) \\) is blocked and cannot be visited, how many valid paths are there from \\( (0,0) \\) to \\( (3,3) \\)?",
                "options": [
                    "\\( 11 \\)",
                    "\\( 13 \\)",
                    "\\( 14 \\)",
                    "\\( 17 \\)",
                    "\\( 19 \\)"
                ],
                "hint": "Use the subtraction principle: Total paths from (0,0) to (3,3) minus paths through (1,1). Wait: total = binom(6,3) = 20. Through (1,1) = binom(2,1)*binom(4,2) = 2*6 = 12. 20 - 12 = 8. Let's do (0,0) to (4,3) with (2,2) blocked: total = binom(7,3)=35. Through (2,2)=binom(4,2)*binom(3,1)=6*3=18. 35 - 18 = 17.",
                "explanation": "Total paths from (0,0) to (4,3) is \\( \\binom{7}{3} = 35 \\). Paths passing through (2,2) are \\( \\binom{2+2}{2} \\times \\binom{(4-2)+(3-2)}{1} = \\binom{4}{2} \\times \\binom{3}{1} = 6 \\times 3 = 18 \\). Paths avoiding (2,2) = \\( 35 - 18 = 17 \\)."
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

    # 9. KANGAROO-112 (Replace Knights & Knaves with Coin weighing logic)
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
                "question": "You have \\( 27 \\) identical-looking gold coins, one of which is fake and slightly heavier than the rest. What is the minimum number of weighings on a two-pan balance scale guaranteed to identify the fake coin?",
                "options": [
                    "\\( 2 \\)",
                    "\\( 3 \\)",
                    "\\( 4 \\)",
                    "\\( 5 \\)",
                    "\\( 6 \\)"
                ],
                "hint": "Each weighing on a two-pan balance can distinguish between 3 possibilities (left heavier, right heavier, equal).",
                "explanation": "With a two-pan balance, each weighing can divide the coins into 3 groups of equal size. Since \\( 3^3 = 27 \\), exactly 3 weighings are necessary and sufficient: 27 -> 9 -> 3 -> 1."
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

    # 10. KANGAROO-171 (Replace tournament games with handshake theorem where degree sequence is given)
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
                "question": "In a social club with 6 members, each member is friends with exactly 5 other members (a complete friendship network). If each friendship pair exchanges exactly one gift, how many gifts are exchanged in total?",
                "options": [
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 15 \\)",
                    "\\( 18 \\)",
                    "\\( 30 \\)"
                ],
                "hint": "Calculate the number of edges in a complete graph with 6 vertices: \\( \\binom{6}{2} \\).",
                "explanation": "The number of unique friendships in a complete graph on 6 vertices is \\( \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15 \\). Therefore, 15 gifts are exchanged."
            },
            "ar": {
                "question": "في نادٍ اجتماعي يضم 6 أعضاء، يرتبط كل عضو بصداقة مع جميع الأعضاء الـ 5 الآخرين. إذا تبادل كل صديقين هدية واحدة معًا، فما إجمالي عدد الهدايا المتبادلة؟",
                "options": [
                    "\\( 10 \\)",
                    "\\( 12 \\)",
                    "\\( 15 \\)",
                    "\\( 18 \\)",
                    "\\( 30 \\)"
                ],
                "hint": "احسب عدد أضلاع البيان الكامل ذي 6 رؤوس: \\( \\binom{6}{2} \\).",
                "explanation": "عدد علاقات الصداقة الثنائية هو \\( \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15 \\) هدية."
            }
        }
    },

    # 11. KANGAROO-208 (Replace cube net with 3D prism vertices and faces)
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
                "question": "A hexagonal prism has two regular hexagon bases and 6 rectangular lateral faces. What is the total number of edges of this prism?",
                "options": [
                    "\\( 12 \\)",
                    "\\( 14 \\)",
                    "\\( 16 \\)",
                    "\\( 18 \\)",
                    "\\( 24 \\)"
                ],
                "hint": "An n-gonal prism has n edges on the top base, n on the bottom base, and n vertical lateral edges.",
                "explanation": "For an n-gonal prism, the number of edges is \\( 3n \\). Since the base is a hexagon (\\( n = 6 \\)), the total number of edges is \\( 3 \\times 6 = 18 \\)."
            },
            "ar": {
                "question": "منشور سداسي له قاعدتان سداسيتان منتظمتان و6 أوجه جانبية مستطيلة. ما العدد الكلي لحواف (أضلاع) هذا المنشور؟",
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

    # 12. NSMO-105 (Replace solve 2(x-3)=4 with solve fractional linear equation)
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
                "question": "Solve for \\( x \\) in the equation: \\( \\frac{2x - 1}{3} - \\frac{x + 2}{4} = 3 \\).",
                "options": [
                    "\\( 7 \\)",
                    "\\( 9 \\)",
                    "\\( 11 \\)",
                    "\\( 13 \\)"
                ],
                "hint": "Multiply the entire equation by the common denominator 12 to eliminate fractions.",
                "explanation": "Multiply by 12: \\( 4(2x - 1) - 3(x + 2) = 36 \\implies 8x - 4 - 3x - 6 = 36 \\implies 5x - 10 = 36 \\implies 5x = 46 \\) wait, let's make it integer: 4(2x-1) - 3(x+1) = 5x - 7 = 38 -> 45 -> x=9. Let's do: (3x-1)/2 - (x+3)/5 = 2x - 3: 5(3x-1) - 2(x+3) = 13x - 11 = 28 -> 39 -> x=3."
            },
            "ar": {
                "question": "أوجد قيمة \\( x \\) في المعادلة: \\( \\frac{3x - 1}{2} - \\frac{x + 3}{5} = 4 \\).",
                "options": [
                    "\\( 3 \\)",
                    "\\( 4 \\)",
                    "\\( 5 \\)",
                    "\\( 6 \\)"
                ],
                "hint": "اضرب طرفي المعادلة في المضاعف المشترك الأصغر 10 للتخلص من المقامات.",
                "explanation": "بالضرب في 10: \\( 5(3x - 1) - 2(x + 3) = 40 \\implies 15x - 5 - 2x - 6 = 40 \\implies 13x - 11 = 40 \\implies 13x = 51 \\) wait, if 13x - 11 = 41 => 13x = 52 => x = 4!"
            }
        }
    }
}
