#!/usr/bin/env python3
"""
Build a static website from the book chapters with proper disclaimers.
"""

import os
import re
import markdown
from pathlib import Path
from datetime import datetime

# Directories
BASE_DIR = Path(__file__).parent.parent
CHAPTERS_AR = BASE_DIR / "chapters_ar"
CHAPTERS_EN = BASE_DIR / "chapters_en"
ILLUSTRATIONS = BASE_DIR / "illustrations"
WEBSITE_DIR = BASE_DIR / "website"

# Chapter order
CHAPTER_ORDER = [
    ("00_introduction", "Introduction", "المقدمة"),
    ("01_company_types", "Company Types", "أنواع الشركات"),
    ("02_foreign_investors", "Foreign Investors", "المستثمرون الأجانب"),
    ("03_founding_steps", "Founding Steps", "خطوات التأسيس"),
    ("04_pdpl_basics", "PDPL Basics", "أساسيات حماية البيانات"),
    ("05_consent", "Consent", "الموافقة"),
    ("06_cross_border", "Cross-Border Transfer", "النقل عبر الحدود"),
    ("07_pdpl_compliance", "PDPL Compliance", "الامتثال"),
    ("08_pdpl_penalties", "Penalties", "العقوبات"),
    ("09_cybersecurity_ecosystem", "Cybersecurity", "الأمن السيبراني"),
    ("10_ecc_controls", "ECC Controls", "الضوابط الأساسية"),
    ("11_government_contracts", "Government Contracts", "العقود الحكومية"),
    ("12_compliance_advantage", "Compliance Advantage", "ميزة الامتثال"),
    ("13_ai_landscape", "AI Regulations", "تنظيم الذكاء الاصطناعي"),
    ("14_ai_products", "AI Products", "منتجات الذكاء الاصطناعي"),
    ("appendix_a_checklists", "Checklists", "قوائم المراجعة"),
    ("appendix_b_templates", "Templates", "النماذج"),
    ("appendix_c_resources", "Resources", "المصادر"),
    ("appendix_d_glossary", "Glossary", "المصطلحات"),
]

DISCLAIMER_EN = """
<div class="disclaimer">
    <h3>⚠️ Important Legal Disclaimer</h3>
    <p><strong>This guide is for informational and educational purposes only.</strong></p>
    <ul>
        <li>This content does <strong>NOT</strong> constitute legal advice.</li>
        <li>Laws and regulations change frequently. Always verify current requirements with official government sources.</li>
        <li>Consult a qualified legal professional before making business decisions.</li>
        <li>The authors assume no liability for actions taken based on this information.</li>
        <li>Last updated: {date}</li>
    </ul>
    <p><strong>Official Sources:</strong></p>
    <ul>
        <li><a href="https://laws.boe.gov.sa" target="_blank">Bureau of Experts (هيئة الخبراء)</a> - Official law texts</li>
        <li><a href="https://misa.gov.sa" target="_blank">Ministry of Investment (MISA)</a></li>
        <li><a href="https://mc.gov.sa" target="_blank">Ministry of Commerce</a></li>
        <li><a href="https://sdaia.gov.sa" target="_blank">SDAIA</a> - Data Protection</li>
        <li><a href="https://nca.gov.sa" target="_blank">NCA</a> - Cybersecurity</li>
    </ul>
</div>
"""

DISCLAIMER_AR = """
<div class="disclaimer rtl">
    <h3>⚠️ إخلاء مسؤولية قانونية مهم</h3>
    <p><strong>هذا الدليل لأغراض المعلومات والتعليم فقط.</strong></p>
    <ul>
        <li>هذا المحتوى <strong>لا يُشكّل</strong> استشارة قانونية.</li>
        <li>الأنظمة واللوائح تتغير باستمرار. تحقق دائماً من المتطلبات الحالية من المصادر الحكومية الرسمية.</li>
        <li>استشر محامياً مؤهلاً قبل اتخاذ قرارات تجارية.</li>
        <li>المؤلفون لا يتحملون أي مسؤولية عن الإجراءات المتخذة بناءً على هذه المعلومات.</li>
        <li>آخر تحديث: {date}</li>
    </ul>
    <p><strong>المصادر الرسمية:</strong></p>
    <ul>
        <li><a href="https://laws.boe.gov.sa" target="_blank">هيئة الخبراء بمجلس الوزراء</a> - نصوص الأنظمة الرسمية</li>
        <li><a href="https://misa.gov.sa" target="_blank">وزارة الاستثمار</a></li>
        <li><a href="https://mc.gov.sa" target="_blank">وزارة التجارة</a></li>
        <li><a href="https://sdaia.gov.sa" target="_blank">سدايا</a> - حماية البيانات</li>
        <li><a href="https://nca.gov.sa" target="_blank">الهيئة الوطنية للأمن السيبراني</a></li>
    </ul>
</div>
"""

CSS_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Tajawal:wght@400;500;700&family=JetBrains+Mono&display=swap');

:root {
    --primary: #0F766E;
    --primary-dark: #134E4A;
    --primary-light: #14B8A6;
    --secondary: #0EA5E9;
    --accent: #F59E0B;
    --text: #1E293B;
    --text-light: #64748B;
    --text-muted: #94A3B8;
    --bg: #FFFFFF;
    --bg-alt: #F8FAFC;
    --bg-card: #FFFFFF;
    --border: #E2E8F0;
    --shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
    --radius: 12px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 16px;
    line-height: 1.75;
    color: var(--text);
    background: var(--bg-alt);
    -webkit-font-smoothing: antialiased;
}

.rtl {
    direction: rtl;
    text-align: right;
    font-family: 'Tajawal', -apple-system, sans-serif;
}

.container {
    max-width: 860px;
    margin: 0 auto;
    padding: 2.5rem;
}

/* Header */
header {
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 50%, var(--primary-light) 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

header h1 {
    font-size: 2.75rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
    position: relative;
    letter-spacing: -0.02em;
}

header p {
    opacity: 0.9;
    font-size: 1.25rem;
    font-weight: 400;
    position: relative;
}

/* Navigation */
nav {
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    padding: 0.75rem 1rem;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--shadow);
}

nav ul {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    gap: 0.375rem;
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto;
}

nav a {
    display: block;
    padding: 0.5rem 0.875rem;
    color: var(--text-light);
    text-decoration: none;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

nav a:hover {
    background: var(--bg-alt);
    color: var(--primary);
}

nav a.active {
    background: var(--primary);
    color: white;
}

/* Disclaimer */
.disclaimer {
    background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
    border: 1px solid #F59E0B;
    border-radius: var(--radius);
    padding: 1.5rem 2rem;
    margin: 2rem 0;
    box-shadow: var(--shadow);
}

.disclaimer h3 {
    color: #B45309;
    margin-bottom: 1rem;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.disclaimer ul {
    margin: 1rem 0 1rem 1.25rem;
    color: #92400E;
}

.disclaimer.rtl ul {
    margin: 1rem 1.25rem 1rem 0;
}

.disclaimer li {
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
}

.disclaimer a {
    color: var(--primary);
    font-weight: 500;
    text-decoration: underline;
    text-underline-offset: 2px;
}

.disclaimer a:hover {
    color: var(--primary-dark);
}

/* Content Card */
.content {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: var(--shadow-lg);
    border: 1px solid var(--border);
}

.content h1 {
    color: var(--primary-dark);
    font-size: 2.25rem;
    font-weight: 700;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 3px solid var(--primary-light);
    letter-spacing: -0.02em;
}

.content h2 {
    color: var(--primary);
    font-size: 1.5rem;
    font-weight: 600;
    margin: 2.5rem 0 1.25rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border);
}

.content h3 {
    color: var(--text);
    font-size: 1.2rem;
    font-weight: 600;
    margin: 2rem 0 1rem;
}

.content p {
    margin-bottom: 1.25rem;
    color: var(--text);
}

.content ul, .content ol {
    margin: 1.25rem 0 1.25rem 1.5rem;
}

.rtl .content ul, .rtl .content ol {
    margin: 1.25rem 1.5rem 1.25rem 0;
}

.content li {
    margin-bottom: 0.625rem;
    color: var(--text);
}

.content li::marker {
    color: var(--primary);
}

/* Tables */
.content table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 2rem 0;
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
}

.content th {
    background: linear-gradient(135deg, var(--primary-dark), var(--primary));
    color: white;
    padding: 1rem 1.25rem;
    text-align: left;
    font-weight: 600;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.rtl .content th {
    text-align: right;
}

.content td {
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--border);
    background: var(--bg);
}

.content tr:last-child td {
    border-bottom: none;
}

.content tr:nth-child(even) td {
    background: var(--bg-alt);
}

.content tr:hover td {
    background: #F0FDFA;
}

/* Blockquotes */
.content blockquote {
    background: linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%);
    border-left: 4px solid var(--primary);
    padding: 1.5rem 2rem;
    margin: 2rem 0;
    border-radius: 0 var(--radius) var(--radius) 0;
    font-style: italic;
    color: var(--primary-dark);
}

.rtl .content blockquote {
    border-left: none;
    border-right: 4px solid var(--primary);
    border-radius: var(--radius) 0 0 var(--radius);
}

/* Code */
.content code {
    background: #F1F5F9;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    font-size: 0.875em;
    font-family: 'JetBrains Mono', monospace;
    color: var(--primary-dark);
}

.content pre {
    background: #1E293B;
    color: #E2E8F0;
    padding: 1.5rem;
    border-radius: var(--radius);
    overflow-x: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.875rem;
    line-height: 1.6;
}

.content pre code {
    background: none;
    padding: 0;
    color: inherit;
}

.content img {
    max-width: 100%;
    border-radius: var(--radius);
    margin: 1.5rem 0;
    box-shadow: var(--shadow-lg);
}

.content strong {
    color: var(--text);
    font-weight: 600;
}

.content a {
    color: var(--primary);
    text-decoration: underline;
    text-underline-offset: 3px;
    text-decoration-thickness: 1px;
    transition: all 0.2s;
}

.content a:hover {
    color: var(--primary-dark);
    text-decoration-thickness: 2px;
}

/* Language switcher */
.lang-switch {
    text-align: center;
    padding: 1rem;
    background: linear-gradient(180deg, var(--bg) 0%, var(--bg-alt) 100%);
}

.lang-switch a {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.625rem 1.5rem;
    margin: 0 0.375rem;
    background: var(--primary);
    color: white;
    text-decoration: none;
    border-radius: 9999px;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    box-shadow: var(--shadow);
}

.lang-switch a:hover {
    background: var(--primary-dark);
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

/* Footer */
footer {
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    color: #CBD5E1;
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 0;
}

footer p {
    margin-bottom: 0.75rem;
    font-size: 0.95rem;
}

footer a {
    color: var(--primary-light);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

footer a:hover {
    color: white;
}

/* Responsive */
@media (max-width: 768px) {
    header {
        padding: 3rem 1.5rem;
    }

    header h1 {
        font-size: 2rem;
    }

    nav ul {
        gap: 0.25rem;
    }

    nav a {
        padding: 0.375rem 0.625rem;
        font-size: 0.75rem;
    }

    .container {
        padding: 1.25rem;
    }

    .content {
        padding: 1.5rem;
        border-radius: 8px;
    }

    .content h1 {
        font-size: 1.75rem;
    }

    .content h2 {
        font-size: 1.25rem;
    }

    .disclaimer {
        padding: 1.25rem;
    }
}

/* Print styles */
@media print {
    nav, .lang-switch, .disclaimer {
        display: none;
    }

    .content {
        box-shadow: none;
        border: none;
    }
}
"""

def create_nav_html(chapters, current_id, lang):
    """Create navigation HTML."""
    nav = '<nav><ul>'
    for ch_id, title_en, title_ar in chapters:
        title = title_ar if lang == "ar" else title_en
        active = ' class="active"' if ch_id == current_id else ''
        nav += f'<li><a href="{ch_id}.html"{active}>{title}</a></li>'
    nav += '</ul></nav>'
    return nav

def process_chapter(content):
    """Convert markdown to HTML."""
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    return md.convert(content)

def create_page(chapter_id, content, lang, chapters):
    """Create a full HTML page."""

    title_en = "Saudi Tech Legal Guide"
    title_ar = "الدليل القانوني للتقنية في السعودية"
    subtitle_en = "A practical guide to regulations for tech companies"
    subtitle_ar = "دليل عملي للأنظمة لشركات التقنية"

    title = title_ar if lang == "ar" else title_en
    subtitle = subtitle_ar if lang == "ar" else subtitle_en
    rtl_class = ' class="rtl"' if lang == "ar" else ''
    other_lang = "en" if lang == "ar" else "ar"
    other_lang_name = "English" if lang == "ar" else "العربية"

    date = datetime.now().strftime("%Y-%m-%d")
    disclaimer = DISCLAIMER_AR.format(date=date) if lang == "ar" else DISCLAIMER_EN.format(date=date)

    nav = create_nav_html(chapters, chapter_id, lang)

    return f"""<!DOCTYPE html>
<html lang="{lang}"{rtl_class}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{CSS_STYLE}</style>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </header>

    <div class="lang-switch">
        <a href="../{other_lang}/{chapter_id}.html">{other_lang_name}</a>
    </div>

    {nav}

    <main class="container">
        {disclaimer}

        <div class="content">
            {content}
        </div>

        {disclaimer}
    </main>

    <footer>
        <p>⚠️ This is an informational guide, not legal advice. Always consult official sources.</p>
        <p>هذا دليل معلوماتي وليس استشارة قانونية. راجع دائماً المصادر الرسمية.</p>
        <p style="margin-top: 1rem;">
            <a href="https://laws.boe.gov.sa">هيئة الخبراء</a> |
            <a href="https://misa.gov.sa">MISA</a> |
            <a href="https://sdaia.gov.sa">SDAIA</a> |
            <a href="https://nca.gov.sa">NCA</a>
        </p>
    </footer>
</body>
</html>
"""

def build_website():
    """Build the complete website."""

    print("=" * 60)
    print("Building Website with Disclaimers")
    print("=" * 60)

    # Create directories
    (WEBSITE_DIR / "ar").mkdir(parents=True, exist_ok=True)
    (WEBSITE_DIR / "en").mkdir(parents=True, exist_ok=True)

    for lang in ["ar", "en"]:
        print(f"\nBuilding {lang.upper()} pages...")
        chapters_dir = CHAPTERS_AR if lang == "ar" else CHAPTERS_EN
        output_dir = WEBSITE_DIR / lang

        for ch_id, title_en, title_ar in CHAPTER_ORDER:
            chapter_file = chapters_dir / f"{ch_id}.md"
            if chapter_file.exists():
                content = chapter_file.read_text(encoding='utf-8')
                html_content = process_chapter(content)

                page = create_page(ch_id, html_content, lang, CHAPTER_ORDER)

                output_file = output_dir / f"{ch_id}.html"
                output_file.write_text(page, encoding='utf-8')
                print(f"  Created: {output_file.name}")

        # Create index redirect
        index_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url={lang}/00_introduction.html">
</head>
<body>
    <p>Redirecting to <a href="{lang}/00_introduction.html">guide</a>...</p>
</body>
</html>
"""

    # Main index
    main_index = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saudi Tech Legal Guide | الدليل القانوني للتقنية</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #1B5E20, #4CAF50);
        }
        .container {
            text-align: center;
            background: white;
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 { color: #1B5E20; margin-bottom: 0.5rem; }
        h2 { color: #666; font-weight: normal; margin-bottom: 2rem; }
        .buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        a {
            display: inline-block;
            padding: 1rem 2rem;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 1.2rem;
            transition: transform 0.2s, background 0.2s;
        }
        a:hover { background: #1B5E20; transform: translateY(-2px); }
        .disclaimer {
            margin-top: 2rem;
            padding: 1rem;
            background: #FFF3E0;
            border-radius: 8px;
            font-size: 0.9rem;
            color: #E65100;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Saudi Tech Legal Guide</h1>
        <h2>الدليل القانوني للتقنية في السعودية</h2>

        <div class="buttons">
            <a href="en/00_introduction.html">English Guide</a>
            <a href="ar/00_introduction.html">الدليل بالعربية</a>
        </div>

        <div class="disclaimer">
            ⚠️ This guide is for informational purposes only and does not constitute legal advice.<br>
            هذا الدليل لأغراض المعلومات فقط ولا يشكل استشارة قانونية.
        </div>
    </div>
</body>
</html>
"""

    (WEBSITE_DIR / "index.html").write_text(main_index, encoding='utf-8')

    print("\n" + "=" * 60)
    print("WEBSITE BUILD COMPLETE")
    print("=" * 60)
    print(f"\nOutput: {WEBSITE_DIR}")
    print(f"Open: {WEBSITE_DIR}/index.html")
    print("\nTo serve locally:")
    print(f"  cd {WEBSITE_DIR} && python -m http.server 8000")

if __name__ == "__main__":
    build_website()
