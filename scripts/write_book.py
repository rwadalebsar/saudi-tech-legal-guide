#!/usr/bin/env python3
"""
Fully automated book writer for the Saudi Tech Legal Compass.
AI writes each chapter in both Arabic and English.
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime

from google import genai
from google.genai import types

# Configuration
BOOK_SPEC_PATH = Path(__file__).parent.parent / "book-project-spec.md"
CHAPTERS_DIR_AR = Path(__file__).parent.parent / "chapters_ar"
CHAPTERS_DIR_EN = Path(__file__).parent.parent / "chapters_en"

# Book structure with target word counts
BOOK_STRUCTURE = [
    {
        "id": "00_introduction",
        "title_ar": "المقدمة",
        "title_en": "Introduction",
        "pages": "10-15",
        "word_target": 3000,
        "sections_ar": [
            "لماذا هذا الكتاب الآن؟",
            "كيف تقرأ هذا الكتاب",
            "خريطة الأنظمة السعودية المتعلقة بالتقنية",
            "قصة واقعية: شركة خسرت عقداً حكومياً بسبب جهلها بالأنظمة"
        ],
        "sections_en": [
            "Why This Book Now?",
            "How to Read This Book",
            "Map of Saudi Tech-Related Regulations",
            "Real Story: A Company That Lost a Government Contract Due to Regulatory Ignorance"
        ]
    },
    {
        "id": "01_company_types",
        "title_ar": "الفصل الأول: أنواع الشركات - أيها تناسبك؟",
        "title_en": "Chapter 1: Company Types - Which Suits You?",
        "pages": "15-20",
        "word_target": 5000,
        "sections_ar": [
            "الشركة ذات المسؤولية المحدودة (LLC)",
            "الشركة المساهمة المبسطة (SJS)",
            "شركة الشخص الواحد",
            "جدول مقارنة شامل"
        ],
        "sections_en": [
            "Limited Liability Company (LLC)",
            "Simplified Joint Stock Company (SJS)",
            "Single-Person Company",
            "Comprehensive Comparison Table"
        ],
        "reference": "Saudi Companies Law 2023 / نظام الشركات السعودي الجديد (٢٠٢٣)"
    },
    {
        "id": "02_foreign_investors",
        "title_ar": "الفصل الثاني: الأجانب والسوق السعودي",
        "title_en": "Chapter 2: Foreign Investors and the Saudi Market",
        "pages": "15-20",
        "word_target": 5000,
        "sections_ar": [
            "الملكية الأجنبية ١٠٠٪ - متى تُسمح؟",
            "أنواع رخص الاستثمار (MISA)",
            "متطلبات التوطين (نطاقات)",
            "الشريك المحلي: متى تحتاجه ومتى لا تحتاجه؟",
            "دراسة حالة: شركة أجنبية تدخل السوق السعودي"
        ],
        "sections_en": [
            "100% Foreign Ownership - When Is It Allowed?",
            "Types of Investment Licenses (MISA)",
            "Saudization Requirements (Nitaqat)",
            "Local Partner: When Do You Need One?",
            "Case Study: A Foreign Company Entering the Saudi Market"
        ],
        "reference": "Foreign Investment Law and Ministry of Investment"
    },
    {
        "id": "03_founding_steps",
        "title_ar": "الفصل الثالث: خطوات التأسيس العملية",
        "title_en": "Chapter 3: Practical Founding Steps",
        "pages": "10-15",
        "word_target": 4000,
        "sections_ar": [
            "المنصات الإلكترونية المطلوبة",
            "المستندات المطلوبة (قائمة مراجعة)",
            "التكاليف المتوقعة",
            "الجدول الزمني الواقعي",
            "الأخطاء الشائعة وكيفية تجنبها"
        ],
        "sections_en": [
            "Required Electronic Platforms",
            "Required Documents (Checklist)",
            "Expected Costs",
            "Realistic Timeline",
            "Common Mistakes and How to Avoid Them"
        ],
        "reference": "Ministry of Commerce and Saudi Business Center"
    },
    {
        "id": "04_pdpl_basics",
        "title_ar": "الفصل الرابع: فهم نظام حماية البيانات الشخصية - الأساسيات",
        "title_en": "Chapter 4: Understanding PDPL - The Basics",
        "pages": "12-15",
        "word_target": 4500,
        "sections_ar": [
            "ما هي البيانات الشخصية؟ (تعريف عملي مع أمثلة)",
            "ما هي البيانات الحساسة؟ (القائمة الكاملة)",
            "من هي جهة التحكم؟",
            "الفرق بين المعالجة، النقل، الإفصاح، النشر",
            "على من يُطبق النظام؟ (النطاق الجغرافي)"
        ],
        "sections_en": [
            "What Is Personal Data? (Practical Definition with Examples)",
            "What Is Sensitive Data? (Complete List)",
            "Who Is a Data Controller?",
            "Difference Between Processing, Transfer, Disclosure, and Publication",
            "Who Does the Law Apply To? (Geographical Scope)"
        ],
        "reference": "Personal Data Protection Law (PDPL) and Executive Regulations"
    },
    {
        "id": "05_consent",
        "title_ar": "الفصل الخامس: الموافقة والمسوغات القانونية",
        "title_en": "Chapter 5: Consent and Legal Bases",
        "pages": "12-15",
        "word_target": 4500,
        "sections_ar": [
            "متى تحتاج موافقة صريحة؟",
            "الحالات التي لا تحتاج فيها موافقة (٧ استثناءات)",
            "كيف تصيغ إشعار الخصوصية؟",
            "نموذج إشعار خصوصية لتطبيق تقني",
            "حقوق صاحب البيانات (الوصول، التصحيح، الحذف)"
        ],
        "sections_en": [
            "When Do You Need Explicit Consent?",
            "Cases Where Consent Is Not Required (7 Exceptions)",
            "How to Draft a Privacy Notice",
            "Privacy Notice Template for a Tech Application",
            "Data Subject Rights (Access, Rectification, Deletion)"
        ],
        "reference": "PDPL Articles 5-10"
    },
    {
        "id": "06_cross_border",
        "title_ar": "الفصل السادس: نقل البيانات خارج المملكة",
        "title_en": "Chapter 6: Cross-Border Data Transfer",
        "pages": "12-15",
        "word_target": 4500,
        "sections_ar": [
            "القاعدة الأساسية: الحظر",
            "الاستثناءات المسموحة (١٠ حالات)",
            "الضمانات المطلوبة للنقل",
            "الدول ذات الحماية الكافية",
            "حالة عملية: شركة SaaS تستخدم AWS",
            "الحلول: On-premise vs Cloud المحلي"
        ],
        "sections_en": [
            "The Default Rule: Prohibition",
            "Permitted Exceptions (10 Cases)",
            "Required Safeguards for Transfer",
            "Countries with Adequate Protection",
            "Practical Case: A SaaS Company Using AWS",
            "Solutions: On-Premise vs Local Cloud"
        ],
        "reference": "PDPL Article 29"
    },
    {
        "id": "07_pdpl_compliance",
        "title_ar": "الفصل السابع: الامتثال العملي لشركات التقنية",
        "title_en": "Chapter 7: Practical PDPL Compliance for Tech Companies",
        "pages": "12-15",
        "word_target": 4500,
        "sections_ar": [
            "تقييم أثر حماية البيانات (DPIA)",
            "تعيين مسؤول حماية البيانات - متى يجب؟",
            "التسجيل في بوابة سدايا",
            "إجراءات الإبلاغ عن الانتهاكات",
            "قائمة مراجعة الامتثال الكاملة"
        ],
        "sections_en": [
            "Data Protection Impact Assessment (DPIA)",
            "Appointing a Data Protection Officer - When Required?",
            "Registration on SDAIA Portal",
            "Breach Notification Procedures",
            "Complete Compliance Checklist"
        ],
        "reference": "PDPL Executive Regulations"
    },
    {
        "id": "08_pdpl_penalties",
        "title_ar": "الفصل الثامن: العقوبات والمخاطر",
        "title_en": "Chapter 8: Penalties and Risks",
        "pages": "8-10",
        "word_target": 3000,
        "sections_ar": [
            "العقوبات المالية (حتى ٥ ملايين ريال)",
            "العقوبات الجنائية (حتى سنتين سجن)",
            "الضرر السمعي",
            "كيف تتجنب المخالفات؟"
        ],
        "sections_en": [
            "Financial Penalties (Up to 5 Million SAR)",
            "Criminal Penalties (Up to 2 Years Imprisonment)",
            "Reputational Damage",
            "How to Avoid Violations"
        ],
        "reference": "PDPL Chapter 6"
    },
    {
        "id": "09_cybersecurity_ecosystem",
        "title_ar": "الفصل التاسع: فهم منظومة الأمن السيبراني السعودية",
        "title_en": "Chapter 9: Understanding the Saudi Cybersecurity Ecosystem",
        "pages": "10-12",
        "word_target": 4000,
        "sections_ar": [
            "الهيئة الوطنية للأمن السيبراني (NCA) - من هي؟",
            "خريطة الضوابط والمعايير (ECC, CCC, CSCC)",
            "من يجب عليه الالتزام؟",
            "العلاقة بين ECC و PDPL"
        ],
        "sections_en": [
            "The National Cybersecurity Authority (NCA) - Who Are They?",
            "Map of Controls and Standards (ECC, CCC, CSCC)",
            "Who Must Comply?",
            "The Relationship Between ECC and PDPL"
        ],
        "reference": "Essential Cybersecurity Controls (ECC) - NCA"
    },
    {
        "id": "10_ecc_controls",
        "title_ar": "الفصل العاشر: الضوابط الأساسية - شرح عملي",
        "title_en": "Chapter 10: Essential Controls - Practical Explanation",
        "pages": "15-18",
        "word_target": 5500,
        "sections_ar": [
            "حوكمة الأمن السيبراني",
            "إدارة الأصول",
            "إدارة الهويات والصلاحيات",
            "حماية التطبيقات",
            "إدارة التشفير",
            "النسخ الاحتياطي والتعافي",
            "إدارة الثغرات",
            "الاستجابة للحوادث",
            "قائمة مراجعة ECC المبسطة"
        ],
        "sections_en": [
            "Cybersecurity Governance",
            "Asset Management",
            "Identity and Access Management",
            "Application Protection",
            "Cryptography Management",
            "Backup and Recovery",
            "Vulnerability Management",
            "Incident Response",
            "Simplified ECC Checklist"
        ],
        "reference": "ECC 2024 - NCA"
    },
    {
        "id": "11_government_contracts",
        "title_ar": "الفصل الحادي عشر: الفوز بالعقود الحكومية",
        "title_en": "Chapter 11: Winning Government Contracts",
        "pages": "15-18",
        "word_target": 5500,
        "sections_ar": [
            "منصة اعتماد (Etimad) - كيف تعمل؟",
            "أنواع المنافسات",
            "المتطلبات الفنية الشائعة",
            "كيف تقرأ كراسة الشروط؟",
            "تسعير خدمات التقنية للحكومة",
            "الأخطاء القاتلة في العروض",
            "دراسة حالة: عرض فائز لمشروع AI حكومي"
        ],
        "sections_en": [
            "Etimad Platform - How Does It Work?",
            "Types of Competitions",
            "Common Technical Requirements",
            "How to Read Tender Documents",
            "Pricing Tech Services for Government",
            "Fatal Mistakes in Proposals",
            "Case Study: A Winning AI Government Project Proposal"
        ],
        "reference": "Government Tenders and Procurement Law and Etimad Platform"
    },
    {
        "id": "12_compliance_advantage",
        "title_ar": "الفصل الثاني عشر: تحويل الامتثال إلى ميزة تنافسية",
        "title_en": "Chapter 12: Turning Compliance into Competitive Advantage",
        "pages": "8-10",
        "word_target": 3000,
        "sections_ar": [
            "شهادات الامتثال المعترف بها",
            "كيف تسوّق امتثالك؟",
            "بناء الثقة مع العملاء الحكوميين",
            "الامتثال كخدمة (Compliance as a Service)"
        ],
        "sections_en": [
            "Recognized Compliance Certifications",
            "How to Market Your Compliance",
            "Building Trust with Government Clients",
            "Compliance as a Service"
        ],
        "reference": "Best Practices in the Saudi Market"
    },
    {
        "id": "13_ai_landscape",
        "title_ar": "الفصل الثالث عشر: المشهد التنظيمي للذكاء الاصطناعي",
        "title_en": "Chapter 13: The AI Regulatory Landscape",
        "pages": "10-12",
        "word_target": 4000,
        "sections_ar": [
            "سدايا: من هي وماذا تفعل؟",
            "الاستراتيجية الوطنية للبيانات والذكاء الاصطناعي",
            "مبادئ أخلاقيات الذكاء الاصطناعي",
            "متطلبات الشفافية والمساءلة"
        ],
        "sections_en": [
            "SDAIA: Who Are They and What Do They Do?",
            "National Data and AI Strategy",
            "AI Ethics Principles",
            "Transparency and Accountability Requirements"
        ],
        "reference": "AI Ethics Principles - SDAIA"
    },
    {
        "id": "14_ai_products",
        "title_ar": "الفصل الرابع عشر: بناء منتجات AI متوافقة",
        "title_en": "Chapter 14: Building Compliant AI Products",
        "pages": "10-12",
        "word_target": 4000,
        "sections_ar": [
            "التحيز الخوارزمي - كيف تتجنبه؟",
            "قابلية التفسير (Explainability)",
            "حوكمة نماذج الـ LLM",
            "استخدام البيانات السعودية في التدريب",
            "دراسة حالة: Chatbot حكومي متوافق"
        ],
        "sections_en": [
            "Algorithmic Bias - How to Avoid It",
            "Explainability",
            "LLM Governance",
            "Using Saudi Data for Training",
            "Case Study: A Compliant Government Chatbot"
        ],
        "reference": "AI Ethics Principles - SDAIA"
    },
    {
        "id": "appendix_a_checklists",
        "title_ar": "ملحق أ: قوائم المراجعة",
        "title_en": "Appendix A: Checklists",
        "pages": "8-10",
        "word_target": 2500,
        "sections_ar": [
            "قائمة مراجعة تأسيس الشركة",
            "قائمة مراجعة الامتثال لـ PDPL",
            "قائمة مراجعة ECC للشركات الصغيرة",
            "قائمة مراجعة التقدم لمنافسة حكومية"
        ],
        "sections_en": [
            "Company Formation Checklist",
            "PDPL Compliance Checklist",
            "ECC Checklist for Small Businesses",
            "Government Tender Submission Checklist"
        ]
    },
    {
        "id": "appendix_b_templates",
        "title_ar": "ملحق ب: النماذج الجاهزة",
        "title_en": "Appendix B: Ready Templates",
        "pages": "10-12",
        "word_target": 3500,
        "sections_ar": [
            "نموذج إشعار الخصوصية (عربي/إنجليزي)",
            "نموذج سياسة حماية البيانات الداخلية",
            "نموذج اتفاقية معالجة البيانات (DPA)",
            "نموذج تقييم أثر حماية البيانات (DPIA)",
            "نموذج الإبلاغ عن انتهاك بيانات"
        ],
        "sections_en": [
            "Privacy Notice Template (Arabic/English)",
            "Internal Data Protection Policy Template",
            "Data Processing Agreement (DPA) Template",
            "Data Protection Impact Assessment (DPIA) Template",
            "Data Breach Notification Template"
        ]
    },
    {
        "id": "appendix_c_resources",
        "title_ar": "ملحق ج: الروابط والمصادر",
        "title_en": "Appendix C: Links and Resources",
        "pages": "5-6",
        "word_target": 1500,
        "sections_ar": [
            "روابط جميع الأنظمة واللوائح",
            "المنصات الحكومية الرسمية",
            "جهات الاتصال المهمة",
            "مصادر للتعلم المستمر"
        ],
        "sections_en": [
            "Links to All Laws and Regulations",
            "Official Government Platforms",
            "Important Contacts",
            "Resources for Continuous Learning"
        ]
    },
    {
        "id": "appendix_d_glossary",
        "title_ar": "ملحق د: المصطلحات",
        "title_en": "Appendix D: Glossary",
        "pages": "5-6",
        "word_target": 2000,
        "sections_ar": [
            "قاموس المصطلحات القانونية والتقنية (عربي-إنجليزي)",
            "الاختصارات الشائعة"
        ],
        "sections_en": [
            "Legal and Technical Terms Dictionary (Arabic-English)",
            "Common Abbreviations"
        ]
    }
]


def get_client():
    """Initialize Gemini client with API key from environment."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    return genai.Client(api_key=api_key)


def read_book_spec():
    """Read the book specification file."""
    with open(BOOK_SPEC_PATH, "r", encoding="utf-8") as f:
        return f.read()


def get_progress_file(lang):
    """Get progress file path for language."""
    chapters_dir = CHAPTERS_DIR_AR if lang == "ar" else CHAPTERS_DIR_EN
    return chapters_dir / "progress.json"


def load_progress(lang):
    """Load progress from file."""
    progress_file = get_progress_file(lang)
    if progress_file.exists():
        with open(progress_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "in_progress": None}


def save_progress(lang, progress):
    """Save progress to file."""
    progress_file = get_progress_file(lang)
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def write_chapter_arabic(client, chapter_info, book_spec, previous_chapters_summary=""):
    """Generate a single chapter in Arabic using AI."""

    sections_list = "\n".join([f"- {s}" for s in chapter_info['sections_ar']])
    reference = chapter_info.get('reference', 'المصادر الرسمية السعودية')

    prompt = f"""أنت مؤلف كتاب متخصص في الأنظمة السعودية للشركات التقنية. اكتب الفصل التالي بالعربية الفصحى بأسلوب عملي ومهني.

## معلومات الفصل
- العنوان: {chapter_info['title_ar']}
- عدد الكلمات المستهدف: {chapter_info['word_target']} كلمة
- المرجع الأساسي: {reference}

## الأقسام المطلوبة
{sections_list}

## إرشادات الكتابة
1. اكتب بالعربية الفصحى مع استخدام المصطلحات الإنجليزية التقنية عند الضرورة
2. استخدم أسلوباً عملياً مباشراً يخاطب رواد الأعمال والمطورين
3. أضف أمثلة عملية من واقع السوق السعودي
4. استخدم القوائم والجداول عند الحاجة
5. اجعل المحتوى قابلاً للتطبيق مباشرة
6. تجنب اللغة القانونية المعقدة - بسّط المفاهيم
7. أضف نصائح عملية وتحذيرات من الأخطاء الشائعة
8. اذكر المواد القانونية المحددة عند الإشارة للأنظمة

## سياق الكتاب
هذا الكتاب بعنوان "البوصلة القانونية لشركات التقنية في السعودية" يستهدف:
- رواد الأعمال السعوديين في قطاع التقنية
- الشركات الأجنبية الراغبة في دخول السوق السعودي
- المبرمجين ومديري المشاريع
- المستثمرين في قطاع التقنية

{f"## ملخص الفصول السابقة{chr(10)}{previous_chapters_summary}" if previous_chapters_summary else ""}

## التنسيق
- استخدم Markdown للتنسيق
- ابدأ بالعنوان الرئيسي (#)
- استخدم العناوين الفرعية (## و ###)
- أضف قوائم مرقمة ونقطية
- استخدم الجداول للمقارنات
- أضف اقتباسات للنصوص القانونية المهمة (>)

اكتب الفصل كاملاً الآن:
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=16000,
        )
    )

    return response.text


def write_chapter_english(client, chapter_info, book_spec, previous_chapters_summary=""):
    """Generate a single chapter in English using AI."""

    sections_list = "\n".join([f"- {s}" for s in chapter_info['sections_en']])
    reference = chapter_info.get('reference', 'Official Saudi Sources')

    prompt = f"""You are an expert author specializing in Saudi regulations for tech companies. Write the following chapter in clear, professional English with a practical approach.

## Chapter Information
- Title: {chapter_info['title_en']}
- Target word count: {chapter_info['word_target']} words
- Primary reference: {reference}

## Required Sections
{sections_list}

## Writing Guidelines
1. Write in clear, professional English accessible to international readers
2. Use a practical, direct style addressing entrepreneurs and developers
3. Add practical examples from the Saudi market context
4. Use lists and tables where appropriate
5. Make content immediately actionable
6. Avoid complex legal jargon - simplify concepts
7. Add practical tips and warnings about common mistakes
8. Reference specific legal articles when citing regulations
9. Include Arabic terms in parentheses where relevant (e.g., "Saudization (Nitaqat)")

## Book Context
This book titled "The Legal Compass for Tech Companies in Saudi Arabia" targets:
- Saudi tech entrepreneurs
- Foreign companies wanting to enter the Saudi market
- Developers and project managers
- Tech sector investors

{f"## Summary of Previous Chapters{chr(10)}{previous_chapters_summary}" if previous_chapters_summary else ""}

## Formatting
- Use Markdown formatting
- Start with main heading (#)
- Use subheadings (## and ###)
- Add numbered and bulleted lists
- Use tables for comparisons
- Add blockquotes for important legal texts (>)

Write the complete chapter now:
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=16000,
        )
    )

    return response.text


def generate_chapter_summary(client, chapter_content, lang):
    """Generate a brief summary of a chapter for context in subsequent chapters."""

    if lang == "ar":
        prompt = f"""اكتب ملخصاً مختصراً (٣-٥ جمل) لهذا الفصل بالعربية:

{chapter_content[:3000]}...

الملخص:"""
    else:
        prompt = f"""Write a brief summary (3-5 sentences) of this chapter in English:

{chapter_content[:3000]}...

Summary:"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=500,
        )
    )

    return response.text


def write_book_in_language(client, book_spec, lang):
    """Write the entire book in a specific language."""

    lang_name = "Arabic" if lang == "ar" else "English"
    chapters_dir = CHAPTERS_DIR_AR if lang == "ar" else CHAPTERS_DIR_EN
    chapters_dir.mkdir(exist_ok=True)

    progress = load_progress(lang)

    print(f"\n{'='*60}")
    print(f"Writing {lang_name} Version")
    print(f"{'='*60}")
    print(f"Total chapters: {len(BOOK_STRUCTURE)}")
    print(f"Completed: {len(progress['completed'])}")
    print("-" * 40)

    # Build summary of previous chapters
    summaries = []
    for chapter_id in progress['completed']:
        summary_file = chapters_dir / f"{chapter_id}_summary.txt"
        if summary_file.exists():
            with open(summary_file, "r", encoding="utf-8") as f:
                summaries.append(f.read())

    previous_summary = "\n\n".join(summaries) if summaries else ""

    # Process each chapter
    for chapter in BOOK_STRUCTURE:
        chapter_id = chapter['id']
        chapter_file = chapters_dir / f"{chapter_id}.md"
        title = chapter['title_ar'] if lang == "ar" else chapter['title_en']

        # Skip completed chapters
        if chapter_id in progress['completed']:
            print(f"\n[✓] {title} - already completed")
            continue

        print(f"\n[...] Writing: {title}")
        print(f"     Target: {chapter['word_target']} words")

        # Mark as in progress
        progress['in_progress'] = chapter_id
        save_progress(lang, progress)

        try:
            # Generate chapter
            if lang == "ar":
                content = write_chapter_arabic(client, chapter, book_spec, previous_summary)
            else:
                content = write_chapter_english(client, chapter, book_spec, previous_summary)

            # Save chapter
            with open(chapter_file, "w", encoding="utf-8") as f:
                f.write(content)

            # Generate and save summary for context
            summary = generate_chapter_summary(client, content, lang)
            summary_file = chapters_dir / f"{chapter_id}_summary.txt"
            with open(summary_file, "w", encoding="utf-8") as f:
                f.write(f"## {title}\n{summary}")

            # Update summaries for next chapter
            previous_summary += f"\n\n## {title}\n{summary}"

            # Mark as completed
            progress['completed'].append(chapter_id)
            progress['in_progress'] = None
            save_progress(lang, progress)

            # Count words
            word_count = len(content.split())
            print(f"[✓] Completed: {chapter_file.name} ({word_count} words)")

        except Exception as e:
            print(f"[✗] Error writing chapter: {e}")
            progress['in_progress'] = None
            save_progress(lang, progress)
            raise

    return progress


def main():
    """Main automation flow."""
    parser = argparse.ArgumentParser(description="Write the Saudi Tech Legal Compass book")
    parser.add_argument("--lang", choices=["ar", "en", "both"], default="both",
                        help="Language to write: ar (Arabic), en (English), or both (default)")
    args = parser.parse_args()

    print("=" * 60)
    print("Saudi Tech Legal Compass - Book Writer")
    print("البوصلة القانونية لشركات التقنية في السعودية")
    print("=" * 60)

    client = get_client()
    book_spec = read_book_spec()

    languages = []
    if args.lang in ["ar", "both"]:
        languages.append("ar")
    if args.lang in ["en", "both"]:
        languages.append("en")

    results = {}
    for lang in languages:
        results[lang] = write_book_in_language(client, book_spec, lang)

    # Final summary
    print("\n" + "=" * 60)
    print("BOOK WRITING COMPLETE")
    print("=" * 60)

    for lang in languages:
        lang_name = "Arabic" if lang == "ar" else "English"
        chapters_dir = CHAPTERS_DIR_AR if lang == "ar" else CHAPTERS_DIR_EN
        progress = results[lang]

        print(f"\n{lang_name}:")
        print(f"  Chapters written: {len(progress['completed'])}/{len(BOOK_STRUCTURE)}")
        print(f"  Output directory: {chapters_dir}")

        # Calculate total words
        total_words = 0
        for chapter in BOOK_STRUCTURE:
            chapter_file = chapters_dir / f"{chapter['id']}.md"
            if chapter_file.exists():
                with open(chapter_file, "r", encoding="utf-8") as f:
                    total_words += len(f.read().split())

        print(f"  Total words: ~{total_words:,}")


if __name__ == "__main__":
    main()
