"""Replacement of remaining legacy duplicates with unique ideas."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "kangaroo": {
        "KANGAROO-132": {
            "id": "KANGAROO-132", "track": "kangaroo", "level": "Cadet", "topic": "Sequences", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "A geometric sequence begins with \( b_1 = 3 \) and has common ratio \( r = 2 \). What is the sum of its first \( 6 \) terms?",
                    "options": ["\( 189 \)", "\( 186 \)", "\( 192 \)", "\( 195 \)", "\( 177 \)"],
                    "hint": "Use the finite geometric series formula \( S_n = \frac{b_1(r^n - 1)}{r - 1} \).",
                    "explanation": "\( S_6 = 3 \cdot \frac{2^6 - 1}{2 - 1} = 3(64 - 1) = 3 \times 63 = 189 \)."
                },
                "ar": {
                    "question": "متتالية هندسية حدها الأول \( b_1 = 3 \) وأساسها \( r = 2 \). ما مجموع أول \( 6 \) حدود منها؟",
                    "options": ["\( 189 \)", "\( 186 \)", "\( 192 \)", "\( 195 \)", "\( 177 \)"],
                    "hint": "استخدم صيغة مجموع المتسلسلة الهندسية \( S_n = \frac{b_1(r^n - 1)}{r - 1} \).",
                    "explanation": "\( S_6 = 3 \cdot \frac{2^6 - 1}{2 - 1} = 3(64 - 1) = 3 \times 63 = 189 \)."
                }
            },
            "correct_index": 0
        },
        "KANG-JUN-002-R364": {
            "id": "KANG-JUN-002-R364", "track": "kangaroo", "level": "Junior", "topic": "Algebra", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "If \( x - \frac{1}{x} = 4 \), what is the value of \( x^2 + \frac{1}{x^2} \)?",
                    "options": ["\( 14 \)", "\( 16 \)", "\( 18 \)", "\( 20 \)", "\( 22 \)"],
                    "hint": "Square both sides of \( (x - 1/x) = 4 \) and expand.",
                    "explanation": "\( (x - 1/x)^2 = x^2 - 2 + 1/x^2 = 16 \implies x^2 + 1/x^2 = 16 + 2 = 18 \)."
                },
                "ar": {
                    "question": "إذا كان \( x - \frac{1}{x} = 4 \)، فما قيمة \( x^2 + \frac{1}{x^2} \)؟",
                    "options": ["\( 14 \)", "\( 16 \)", "\( 18 \)", "\( 20 \)", "\( 22 \)"],
                    "hint": "ربّع طرفي المعادلة \( (x - 1/x) = 4 \) وفك القوس.",
                    "explanation": "\( (x - 1/x)^2 = x^2 - 2 + 1/x^2 = 16 \implies x^2 + 1/x^2 = 16 + 2 = 18 \)."
                }
            },
            "correct_index": 2
        },
        "KANGAROO-162": {
            "id": "KANGAROO-162", "track": "kangaroo", "level": "Cadet", "topic": "Logic", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "In a club of \( 45 \) members, \( 28 \) speak English, \( 22 \) speak French, and \( 7 \) speak neither language. How many members speak both English and French?",
                    "options": ["\( 10 \)", "\( 12 \)", "\( 14 \)", "\( 16 \)", "\( 18 \)"],
                    "hint": "First determine how many members speak at least one of the two languages.",
                    "explanation": "Members speaking at least one language: \( 45 - 7 = 38 \). By inclusion-exclusion: \( 28 + 22 - 38 = 12 \)."
                },
                "ar": {
                    "question": "في نادٍ يضم \( 45 \) عضوًا، يتحدث \( 28 \) الإنجليزية، و\( 22 \) الفرنسية، و\( 7 \) لا يتحدثون أيًا منهما. كم عضوًا يتحدث اللغتين معًا؟",
                    "options": ["\( 10 \)", "\( 12 \)", "\( 14 \)", "\( 16 \)", "\( 18 \)"],
                    "hint": "احسب أولاً عدد الأعضاء الذين يتحدثون لغة واحدة على الأقل.",
                    "explanation": "الذين يتحدثون لغة واحدة على الأقل: \( 45 - 7 = 38 \). بمبدأ الشمول والاستبعاد: \( 28 + 22 - 38 = 12 \)."
                }
            },
            "correct_index": 1
        },
        "KANG-ECO-152": {
            "id": "KANG-ECO-152", "track": "kangaroo", "level": "Ecolier", "topic": "Geometry", "type": "MCQ", "difficulty": "easy",
            "content": {
                "en": {
                    "question": "How many vertices (corners) does a regular pentagon have?",
                    "options": ["\( 3 \)", "\( 4 \)", "\( 5 \)", "\( 6 \)", "\( 8 \)"],
                    "hint": "Count the number of angles or sides of a pentagon.",
                    "explanation": "A pentagon has \( 5 \) sides and \( 5 \) vertices."
                },
                "ar": {
                    "question": "كم رأسًا (زاوية) للمضلع الخماسي المنتظم؟",
                    "options": ["\( 3 \)", "\( 4 \)", "\( 5 \)", "\( 6 \)", "\( 8 \)"],
                    "hint": "عد أضلاع أو زوايا الشكل الخماسي.",
                    "explanation": "الشكل الخماسي له \( 5 \) أضلاع و\( 5 \) رؤوس."
                }
            },
            "correct_index": 2
        },
        "KAN-JUN-15": {
            "id": "KAN-JUN-15", "track": "kangaroo", "level": "Junior", "topic": "Spatial Reasoning", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "A solid rectangular block measuring \( 3 \times 4 \times 5 \) is painted blue on all \( 6 \) faces and then sliced into \( 1 \times 1 \times 1 \) unit cubes. How many unit cubes have no paint on any face?",
                    "options": ["\( 0 \)", "\( 4 \)", "\( 6 \)", "\( 8 \)", "\( 12 \)"],
                    "hint": "The unpainted cubes form an inner rectangular block with dimensions reduced by \( 2 \) along each axis.",
                    "explanation": "Inner dimensions are \( (3-2) \times (4-2) \times (5-2) = 1 \times 2 \times 3 = 6 \) unpainted cubes."
                },
                "ar": {
                    "question": "قالب خشبي مستطيل أبعاده \( 3 \times 4 \times 5 \) طلي باللون الأزرق على جميع أوجهه الستة، ثم قُطع إلى مكعبات وحدة \( 1 \times 1 \times 1 \). كم مكعبًا لم يُطلَ أي من أوجهه؟",
                    "options": ["\( 0 \)", "\( 4 \)", "\( 6 \)", "\( 8 \)", "\( 12 \)"],
                    "hint": "المكعبات غير المطلية تشكل متوازي مستطيلات داخلي أبعاده تنقص بمقدار \( 2 \) في كل بُعد.",
                    "explanation": "الأبعاد الداخلية: \( (3-2) \times (4-2) \times (5-2) = 1 \times 2 \times 3 = 6 \) مكعبات."
                }
            },
            "correct_index": 2
        },
        "KAN-JUN-08": {
            "id": "KAN-JUN-08", "track": "kangaroo", "level": "Junior", "topic": "Set Theory", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "In a class of \( 40 \) students, \( 24 \) take Physics, \( 18 \) take Chemistry, and \( 8 \) take neither course. How many students take both Physics and Chemistry?",
                    "options": ["\( 6 \)", "\( 8 \)", "\( 10 \)", "\( 12 \)", "\( 14 \)"],
                    "hint": "Use \( |A \cup B| = |A| + |B| - |A \cap B| \).",
                    "explanation": "Students taking at least one: \( 40 - 8 = 32 \). Both: \( 24 + 18 - 32 = 10 \)."
                },
                "ar": {
                    "question": "في صف يضم \( 40 \) طالبًا، يدرس \( 24 \) الفيزياء، و\( 18 \) الكيمياء، و\( 8 \) لا يدرسون أيًا منهما. كم طالبًا يدرس المادتين معًا؟",
                    "options": ["\( 6 \)", "\( 8 \)", "\( 10 \)", "\( 12 \)", "\( 14 \)"],
                    "hint": "استخدم \( |A \cup B| = |A| + |B| - |A \cap B| \).",
                    "explanation": "الذين يدرسون مادة واحدة على الأقل: \( 40 - 8 = 32 \). كلاهما: \( 24 + 18 - 32 = 10 \)."
                }
            },
            "correct_index": 2
        },
        "KANGAROO-157": {
            "id": "KANGAROO-157", "track": "kangaroo", "level": "Cadet", "topic": "Statistics", "type": "MCQ", "difficulty": "easy",
            "content": {
                "en": {
                    "question": "The five numbers \( 4, 7, x, 12, 15 \) are listed in strictly increasing order. If their median is \( 9 \), what is the value of \( x \)?",
                    "options": ["\( 8 \)", "\( 9 \)", "\( 10 \)", "\( 11 \)", "\( 12 \)"],
                    "hint": "For an odd number of ordered values, the median is the central entry.",
                    "explanation": "The list has \( 5 \) elements in order, so the 3rd element is the median: \( x = 9 \)."
                },
                "ar": {
                    "question": "الأعداد الخمسة \( 4, 7, x, 12, 15 \) مرتبة تصاعديًا. إذا كان وسيطها هو \( 9 \)، فما قيمة \( x \)؟",
                    "options": ["\( 8 \)", "\( 9 \)", "\( 10 \)", "\( 11 \)", "\( 12 \)"],
                    "hint": "لعدد فردي من القيم المرتبة، الوسيط هو القيمة الوسطى تمامًا.",
                    "explanation": "القائمة مرتبة وبها \( 5 \) عناصر، لذا العنصر الثالث هو الوسيط: \( x = 9 \)."
                }
            },
            "correct_index": 1
        },
        "KANGAROO-119": {
            "id": "KANGAROO-119", "track": "kangaroo", "level": "Cadet", "topic": "Probability", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "Two standard fair six-sided dice are rolled simultaneously. What is the probability that the product of the two numbers rolled is odd?",
                    "options": ["\( \frac{1}{6} \)", "\( \frac{1}{4} \)", "\( \frac{1}{3} \)", "\( \frac{1}{2} \)", "\( \frac{3}{4} \)"],
                    "hint": "The product of two integers is odd if and only if both numbers are odd.",
                    "explanation": "Each die has \( 3 \) odd outcomes out of \( 6 \). Probability = \( \frac{3}{6} \times \frac{3}{6} = \frac{1}{4} \)."
                },
                "ar": {
                    "question": "أُلقي نردان منتظمان ذوا ستة أوجه معًا. ما احتمال أن يكون حاصل ضرب العددين الظاهرين عددًا فرديًا؟",
                    "options": ["\( \frac{1}{6} \)", "\( \frac{1}{4} \)", "\( \frac{1}{3} \)", "\( \frac{1}{2} \)", "\( \frac{3}{4} \)"],
                    "hint": "يكون حاصل ضرب عددين فرديًا إذا وفقط إذا كان كلا العددين فرديين.",
                    "explanation": "كل نرد له \( 3 \) أعداد فردية من \( 6 \). الاحتمال = \( \frac{3}{6} \times \frac{3}{6} = \frac{1}{4} \)."
                }
            },
            "correct_index": 1
        },
        "KANGAROO-167": {
            "id": "KANGAROO-167", "track": "kangaroo", "level": "Cadet", "topic": "Spatial Reasoning", "type": "MCQ", "difficulty": "easy",
            "content": {
                "en": {
                    "question": "A prism has a base shaped as a regular hexagon. How many total edges does this hexagonal prism have?",
                    "options": ["\( 12 \)", "\( 14 \)", "\( 16 \)", "\( 18 \)", "\( 24 \)"],
                    "hint": "Count the edges of the top base, bottom base, and the vertical connecting edges.",
                    "explanation": "The prism has \( 6 \) bottom edges, \( 6 \) top edges, and \( 6 \) vertical edges: \( 6 + 6 + 6 = 18 \) edges."
                },
                "ar": {
                    "question": "منشور قاعدته مضلع سداسي منتظم. كم عدد الحواف (الأضلاع) الكلية لهذا المنشور السداسي؟",
                    "options": ["\( 12 \)", "\( 14 \)", "\( 16 \)", "\( 18 \)", "\( 24 \)"],
                    "hint": "عد حواف القاعدة السفلية، والعلوية، والحواف الجانبية الواصلة بينهما.",
                    "explanation": "للمنشور \( 6 \) حواف سفلية و\( 6 \) علوية و\( 6 \) جانبية: \( 6 + 6 + 6 = 18 \) حافة."
                }
            },
            "correct_index": 3
        }
    },
    "nafes": {
        "NAFES-105": {
            "id": "NAFES-105", "track": "nafes", "level": "Grade 3", "topic": "Measurement", "type": "MCQ", "difficulty": "easy",
            "content": {
                "en": {
                    "question": "A train departed at \( 7:30 \text{ AM} \) and arrived at its destination at \( 11:15 \text{ AM} \) on the same morning. What was the total travel time?",
                    "options": ["\( 3 \text{ hours } 15 \text{ minutes} \)", "\( 3 \text{ hours } 30 \text{ minutes} \)", "\( 3 \text{ hours } 45 \text{ minutes} \)", "\( 4 \text{ hours } 15 \text{ minutes} \)"],
                    "hint": "Count the full hours from 7:30 to 10:30, then add the remaining minutes to 11:15.",
                    "explanation": "From 7:30 to 10:30 is 3 hours. From 10:30 to 11:15 is 45 minutes. Total = 3 hours and 45 minutes."
                },
                "ar": {
                    "question": "غادر قطار المحطة الساعة \( 7:30 \text{ صباحًا} \) ووصل إلى وجهته الساعة \( 11:15 \text{ صباحًا} \) في نفس اليوم. ما المدة الزمنية المستغرقة في الرحلة؟",
                    "options": ["\( 3 \text{ ساعات و } 15 \text{ دقيقة} \)", "\( 3 \text{ ساعات و } 30 \text{ دقيقة} \)", "\( 3 \text{ ساعات و } 45 \text{ دقيقة} \)", "\( 4 \text{ ساعات و } 15 \text{ دقيقة} \)"],
                    "hint": "احسب الساعات الكاملة من 7:30 إلى 10:30 ثم أضف الدقائق المتبقية حتى 11:15.",
                    "explanation": "من 7:30 إلى 10:30 ثلاث ساعات، ومن 10:30 إلى 11:15 هناك 45 دقيقة. إذن المجموع 3 ساعات و45 دقيقة."
                }
            },
            "correct_index": 2
        },
        "NAFES-258": {
            "id": "NAFES-258", "track": "nafes", "level": "Grade 9", "topic": "Probability", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "A bag contains \( 4 \) red marbles, \( 5 \) white marbles, and \( 6 \) black marbles. If one marble is drawn uniformly at random, what is the probability that it is NOT red?",
                    "options": ["\( \frac{4}{15} \)", "\( \frac{1}{3} \)", "\( \frac{11}{15} \)", "\( \frac{7}{15} \)"],
                    "hint": "The number of non-red marbles is white + black.",
                    "explanation": "Total marbles = \( 4 + 5 + 6 = 15 \). Non-red marbles = \( 5 + 6 = 11 \). Probability = \( \frac{11}{15} \)."
                },
                "ar": {
                    "question": "كيس يحتوي على \( 4 \) كرات حمراء، و\( 5 \) كرات بيضاء، و\( 6 \) كرات سوداء. إذا سُحبت كرة واحدة عشوائيًا، فما احتمال ألا تكون حمراء؟",
                    "options": ["\( \frac{4}{15} \)", "\( \frac{1}{3} \)", "\( \frac{11}{15} \)", "\( \frac{7}{15} \)"],
                    "hint": "عدد الكرات غير الحمراء هو مجموع الكرات البيضاء والسوداء.",
                    "explanation": "إجمالي الكرات = \( 4 + 5 + 6 = 15 \). الكرات غير الحمراء = \( 5 + 6 = 11 \). الاحتمال = \( \frac{11}{15} \)."
                }
            },
            "correct_index": 2
        },
        "NAFES-178": {
            "id": "NAFES-178", "track": "nafes", "level": "Grade 9", "topic": "Algebra", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "Solve the linear inequality for \( x \): \( 4x - 5 > 2x + 9 \).",
                    "options": ["\( x > 7 \)", "\( x < 7 \)", "\( x > 2 \)", "\( x < 2 \)"],
                    "hint": "Subtract \( 2x \) from both sides and add \( 5 \).",
                    "explanation": "\( 4x - 2x > 9 + 5 \implies 2x > 14 \implies x > 7 \)."
                },
                "ar": {
                    "question": "حل المتباينة الخطية الآتية: \( 4x - 5 > 2x + 9 \).",
                    "options": ["\( x > 7 \)", "\( x < 7 \)", "\( x > 2 \)", "\( x < 2 \)"],
                    "hint": "اطرح \( 2x \) من الطرفين واجمع \( 5 \).",
                    "explanation": "\( 4x - 2x > 9 + 5 \implies 2x > 14 \implies x > 7 \)."
                }
            },
            "correct_index": 0
        },
        "NAFES-244": {
            "id": "NAFES-244", "track": "nafes", "level": "Grade 3", "topic": "Fractions", "type": "MCQ", "difficulty": "easy",
            "content": {
                "en": {
                    "question": "A chocolate bar is divided into \( 8 \) equal pieces. Omar ate \( 3 \) of the pieces. What fraction of the chocolate bar did Omar eat?",
                    "options": ["\( \frac{1}{8} \)", "\( \frac{3}{8} \)", "\( \frac{5}{8} \)", "\( \frac{7}{8} \)"],
                    "hint": "The denominator represents the total equal pieces, and the numerator represents the pieces eaten.",
                    "explanation": "Omar ate \( 3 \) out of \( 8 \) equal pieces, so the fraction is \( \frac{3}{8} \)."
                },
                "ar": {
                    "question": "لوح شوكولاتة مقسم إلى \( 8 \) قطع متساوية. أكل عمر \( 3 \) قطع منها. ما الكسر الذي يمثل الجزء الذي أكله عمر؟",
                    "options": ["\( \frac{1}{8} \)", "\( \frac{3}{8} \)", "\( \frac{5}{8} \)", "\( \frac{7}{8} \)"],
                    "hint": "المقام يمثل إجمالي القطع المتساوية، والبسط يمثل القطع المأكولة.",
                    "explanation": "أكل عمر \( 3 \) من أصل \( 8 \) قطع متساوية، إذن الكسر هو \( \frac{3}{8} \)."
                }
            },
            "correct_index": 1
        },
        "NAFES-3564-22d4": {
            "id": "NAFES-3564-22d4", "track": "nafes", "level": "Grade 9", "topic": "Algebra", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "Solve the linear equation for \( x \): \( 5(x - 2) = 3x + 8 \).",
                    "options": ["\( 7 \)", "\( 8 \)", "\( 9 \)", "\( 10 \)"],
                    "hint": "Distribute \( 5 \) into the parenthesis first.",
                    "explanation": "\( 5x - 10 = 3x + 8 \implies 2x = 18 \implies x = 9 \)."
                },
                "ar": {
                    "question": "حل المعادلة الخطية الآتية: \( 5(x - 2) = 3x + 8 \).",
                    "options": ["\( 7 \)", "\( 8 \)", "\( 9 \)", "\( 10 \)"],
                    "hint": "قم بفك القوس بضرب \( 5 \) أولاً.",
                    "explanation": "\( 5x - 10 = 3x + 8 \implies 2x = 18 \implies x = 9 \)."
                }
            },
            "correct_index": 2
        },
        "NAFES-6155-daf3": {
            "id": "NAFES-6155-daf3", "track": "nafes", "level": "Grade 9", "topic": "Fractions", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "If \( \frac{2}{5} \) of a certain number is \( 30 \), what is \( \frac{3}{5} \) of that number?",
                    "options": ["\( 35 \)", "\( 40 \)", "\( 45 \)", "\( 50 \)"],
                    "hint": "If \( 2 \) fifths equal \( 30 \), then \( 1 \) fifth equals \( 15 \).",
                    "explanation": "\( \frac{1}{5} \) of the number is \( 30 \div 2 = 15 \). Therefore, \( \frac{3}{5} \) is \( 3 \times 15 = 45 \)."
                },
                "ar": {
                    "question": "إذا كان \( \frac{2}{5} \) من عدد ما يساوي \( 30 \)، فما قيمة \( \frac{3}{5} \) من ذلك العدد؟",
                    "options": ["\( 35 \)", "\( 40 \)", "\( 45 \)", "\( 50 \)"],
                    "hint": "إذا كان خمسا العدد يساويان \( 30 \)، فإن خمس العدد يساوي \( 15 \).",
                    "explanation": "خمس العدد هو \( 30 \div 2 = 15 \)، إذن ثلاثة أخماسه تساوي \( 3 \times 15 = 45 \)."
                }
            },
            "correct_index": 2
        },
        "NAFES-9-228": {
            "id": "NAFES-9-228", "track": "nafes", "level": "Grade 9", "topic": "Sequences", "type": "MCQ", "difficulty": "medium",
            "content": {
                "en": {
                    "question": "In a geometric sequence with positive terms, the first term is \( a_1 = 5 \) and the fourth term is \( a_4 = 40 \). What is the common ratio \( r \)?",
                    "options": ["\( 2 \)", "\( 3 \)", "\( 4 \)", "\( 8 \)"],
                    "hint": "Use the formula \( a_n = a_1 \cdot r^{n-1} \).",
                    "explanation": "\( a_4 = a_1 \cdot r^3 \implies 40 = 5 r^3 \implies r^3 = 8 \implies r = 2 \)."
                },
                "ar": {
                    "question": "في متتالية هندسية حدودها موجبة، الحد الأول \( a_1 = 5 \) والحد الرابع \( a_4 = 40 \). ما قيمة أساس المتتالية \( r \)؟",
                    "options": ["\( 2 \)", "\( 3 \)", "\( 4 \)", "\( 8 \)"],
                    "hint": "استخدم صيغة الحد العام للمتتالية الهندسية \( a_n = a_1 \cdot r^{n-1} \).",
                    "explanation": "\( a_4 = a_1 \cdot r^3 \implies 40 = 5 r^3 \implies r^3 = 8 \implies r = 2 \)."
                }
            },
            "correct_index": 0
        }
    },
    "nsmo": {
        "NSMO-P3-045": {
            "id": "NSMO-P3-045", "track": "nsmo", "level": "Phase 3: Senior National Olympiad (Grades 10-12)", "topic": "Diophantine Equations", "type": "MCQ", "difficulty": "hard",
            "content": {
                "en": {
                    "question": "Find the number of pairs of positive integers \( (x, y) \) satisfying the equation \( x^2 - 4y^2 = 45 \).",
                    "options": ["\( 1 \)", "\( 2 \)", "\( 3 \)", "\( 4 \)"],
                    "hint": "Factor the left-hand side as a difference of squares: \( (x - 2y)(x + 2y) = 45 \).",
                    "explanation": "Since \( x, y > 0 \), \( x + 2y > x - 2y > 0 \). Their difference is \( (x+2y)-(x-2y) = 4y \), a positive multiple of \( 4 \). Factoring \( 45 \): (1, 45) gives \( 4y = 44 \implies y=11, x=23 \); (3, 15) gives \( 4y = 12 \implies y=3, x=9 \); (5, 9) gives \( 4y = 4 \implies y=1, x=7 \). All \( 3 \) pairs are positive integers."
                },
                "ar": {
                    "question": "أوجد عدد أزواج الأعداد الصحيحة الموجبة \( (x, y) \) التي تحقق المعادلة \( x^2 - 4y^2 = 45 \).",
                    "options": ["\( 1 \)", "\( 2 \)", "\( 3 \)", "\( 4 \)"],
                    "hint": "حلل الطرف الأيسر كفرق بين مربعين: \( (x - 2y)(x + 2y) = 45 \).",
                    "explanation": "بما أن \( x, y > 0 \)، فإن \( x + 2y > x - 2y > 0 \). فرقهما هو \( 4y \) وهو مضاعف موجب لـ \( 4 \). قواسم 45: (1, 45) تعطي \( y=11, x=23 \)؛ و(3, 15) تعطي \( y=3, x=9 \)؛ و(5, 9) تعطي \( y=1, x=7 \). جميع الأزواج الـ \( 3 \) أعداد صحيحة موجبة."
                }
            },
            "correct_index": 2
        }
    },
    "jee": {
        "JEE-140": {
            "id": "JEE-140", "track": "jee", "level": "Grade 12", "topic": "Continuity and Differentiability", "type": "MCQ", "difficulty": "hard",
            "content": {
                "en": {
                    "question": "Let \( f(x) = |x^2 - 4| + |x^3 - 8| \) for all \( x \in \mathbb{R} \). Find the total number of points at which \( f(x) \) is not differentiable.",
                    "options": ["\( 1 \)", "\( 2 \)", "\( 4 \)", "\( 5 \)"],
                    "hint": "Check points where the expressions inside the absolute values change sign: \( x = 2 \) and \( x = -2 \).",
                    "explanation": "At \( x = 2 \), the right derivative is \( 4 + 12 = 16 \) while the left derivative is \( -4 - 12 = -16 \ne 16 \), so \( f \) is non-differentiable at \( x = 2 \). At \( x = -2 \), \( x^2 - 4 \) has a non-zero slope while \( |x^3 - 8| \) is smooth and negative (\( -16 \)), yielding corner at \( x = -2 \). Hence \( f \) is non-differentiable at exactly \( 2 \) points."
                },
                "ar": {
                    "question": "لتكن \( f(x) = |x^2 - 4| + |x^3 - 8| \) لكل \( x \in \mathbb{R} \). أوجد العدد الكلي للنقاط التي تكون عندها \( f(x) \) غير قابلة للاشتقاق.",
                    "options": ["\( 1 \)", "\( 2 \)", "\( 4 \)", "\( 5 \)"],
                    "hint": "افحص النقاط التي تغير فيها المقادير داخل القيمة المطلقة إشارتها: \( x = 2 \) و\( x = -2 \).",
                    "explanation": "عند \( x = 2 \)، المشتقة من اليمين 16 ومن اليسار -16، فتكون غير قابلة للاشتقاق. وعند \( x = -2 \)، المقدار الأول غير قابل للاشتقاق بينما الثاني قابل للاشتقاق وقيمته سالبة، فيكون المجموع غير قابل للاشتقاق. إذن عدد النقاط هو \( 2 \)."
                }
            },
            "correct_index": 1
        }
    }
}

def apply_replacements():
    for track, reps in REPLACEMENTS.items():
        p = ROOT / "data" / f"{track}.json"
        bank = json.loads(p.read_text())
        b_map = {q["id"]: q for q in bank}
        count = 0
        for qid, new_q in reps.items():
            if qid in b_map:
                idx = bank.index(b_map[qid])
                bank[idx] = new_q
                count += 1
            else:
                print(f"WARNING: {qid} not found in {track}!")
        p.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n")
        print(f"[{track}] Applied {count}/{len(reps)} replacements.")

if __name__ == "__main__":
    apply_replacements()
