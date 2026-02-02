#!/usr/bin/env python3
"""
Build styled PDF books from markdown chapters with illustrations.
Modern style: white background, green accents, dark grey text.
"""

import os
import re
import markdown
from pathlib import Path
from weasyprint import HTML, CSS

# Directories
BASE_DIR = Path(__file__).parent.parent
CHAPTERS_AR = BASE_DIR / "chapters_ar"
CHAPTERS_EN = BASE_DIR / "chapters_en"
ILLUSTRATIONS = BASE_DIR / "illustrations"
OUTPUT_DIR = BASE_DIR / "output"

# Modern color scheme
COLORS = {
    "primary": "#1B5E20",      # Dark green
    "secondary": "#4CAF50",    # Light green
    "accent": "#81C784",       # Pale green
    "text": "#333333",         # Dark grey
    "text_light": "#666666",   # Medium grey
    "background": "#FFFFFF",   # White
    "border": "#E0E0E0",       # Light grey border
    "code_bg": "#F5F5F5",      # Code background
}

# CSS Styling
CSS_STYLE = f"""
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap');

@page {{
    size: A4;
    margin: 2.5cm 2cm;
    @top-center {{
        content: string(chapter-title);
        font-size: 10pt;
        color: {COLORS['text_light']};
    }}
    @bottom-center {{
        content: counter(page);
        font-size: 10pt;
        color: {COLORS['text_light']};
    }}
}}

@page :first {{
    @top-center {{ content: none; }}
}}

* {{
    box-sizing: border-box;
}}

body {{
    font-family: 'Inter', 'Noto Sans Arabic', sans-serif;
    font-size: 11pt;
    line-height: 1.8;
    color: {COLORS['text']};
    background: {COLORS['background']};
    text-align: justify;
}}

body.rtl {{
    direction: rtl;
    text-align: right;
    font-family: 'Noto Sans Arabic', 'Inter', sans-serif;
}}

/* Cover Page */
.cover {{
    page-break-after: always;
    text-align: center;
    padding-top: 30%;
}}

.cover h1 {{
    font-size: 28pt;
    color: {COLORS['primary']};
    margin-bottom: 0.5em;
    line-height: 1.3;
}}

.cover .subtitle {{
    font-size: 16pt;
    color: {COLORS['text_light']};
    margin-bottom: 2em;
}}

.cover .author {{
    font-size: 14pt;
    color: {COLORS['text']};
    margin-top: 3em;
}}

.cover .year {{
    font-size: 12pt;
    color: {COLORS['text_light']};
    margin-top: 1em;
}}

/* Table of Contents */
.toc {{
    page-break-after: always;
}}

.toc h2 {{
    color: {COLORS['primary']};
    border-bottom: 3px solid {COLORS['secondary']};
    padding-bottom: 0.5em;
}}

.toc ul {{
    list-style: none;
    padding: 0;
}}

.toc li {{
    padding: 0.5em 0;
    border-bottom: 1px solid {COLORS['border']};
}}

.toc a {{
    color: {COLORS['text']};
    text-decoration: none;
}}

/* Headings */
h1 {{
    font-size: 24pt;
    color: {COLORS['primary']};
    margin-top: 0;
    margin-bottom: 1em;
    padding-bottom: 0.5em;
    border-bottom: 4px solid {COLORS['secondary']};
    string-set: chapter-title content();
    page-break-before: always;
}}

h1:first-of-type {{
    page-break-before: avoid;
}}

h2 {{
    font-size: 16pt;
    color: {COLORS['primary']};
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    padding-bottom: 0.3em;
    border-bottom: 2px solid {COLORS['accent']};
}}

h3 {{
    font-size: 13pt;
    color: {COLORS['text']};
    margin-top: 1.2em;
    margin-bottom: 0.6em;
    font-weight: 600;
}}

h4 {{
    font-size: 11pt;
    color: {COLORS['text_light']};
    margin-top: 1em;
    margin-bottom: 0.5em;
    font-weight: 600;
}}

/* Paragraphs */
p {{
    margin-bottom: 1em;
    orphans: 3;
    widows: 3;
}}

/* Lists */
ul, ol {{
    margin-bottom: 1em;
    padding-left: 1.5em;
}}

body.rtl ul, body.rtl ol {{
    padding-left: 0;
    padding-right: 1.5em;
}}

li {{
    margin-bottom: 0.4em;
}}

/* Tables */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    font-size: 10pt;
}}

th {{
    background: {COLORS['primary']};
    color: white;
    padding: 12px 10px;
    text-align: left;
    font-weight: 600;
}}

body.rtl th {{
    text-align: right;
}}

td {{
    padding: 10px;
    border-bottom: 1px solid {COLORS['border']};
}}

tr:nth-child(even) {{
    background: #F9F9F9;
}}

/* Blockquotes */
blockquote {{
    margin: 1.5em 0;
    padding: 1em 1.5em;
    background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
    border-left: 4px solid {COLORS['secondary']};
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: {COLORS['text']};
}}

body.rtl blockquote {{
    border-left: none;
    border-right: 4px solid {COLORS['secondary']};
    border-radius: 8px 0 0 8px;
}}

/* Code */
code {{
    font-family: 'Courier New', monospace;
    background: {COLORS['code_bg']};
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9em;
}}

pre {{
    background: {COLORS['code_bg']};
    padding: 1em;
    border-radius: 8px;
    overflow-x: auto;
    border: 1px solid {COLORS['border']};
}}

pre code {{
    background: none;
    padding: 0;
}}

/* Images/Figures */
.figure {{
    margin: 2em 0;
    text-align: center;
    page-break-inside: avoid;
}}

.figure img {{
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}

.figure-caption {{
    margin-top: 0.8em;
    font-size: 10pt;
    color: {COLORS['text_light']};
    font-style: italic;
}}

/* Tips and Warnings */
.tip, .warning, .note {{
    margin: 1.5em 0;
    padding: 1em 1.5em;
    border-radius: 8px;
    page-break-inside: avoid;
}}

.tip {{
    background: #E8F5E9;
    border-left: 4px solid {COLORS['secondary']};
}}

.warning {{
    background: #FFF3E0;
    border-left: 4px solid #FF9800;
}}

.note {{
    background: #E3F2FD;
    border-left: 4px solid #2196F3;
}}

/* Strong and emphasis */
strong {{
    color: {COLORS['primary']};
    font-weight: 600;
}}

em {{
    font-style: italic;
}}

/* Links */
a {{
    color: {COLORS['secondary']};
    text-decoration: none;
}}

/* Horizontal rule */
hr {{
    border: none;
    height: 2px;
    background: linear-gradient(90deg, {COLORS['secondary']}, transparent);
    margin: 2em 0;
}}

/* Page breaks */
.page-break {{
    page-break-after: always;
}}

/* Chapter Cover Page */
.chapter-cover {{
    page-break-before: always;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    text-align: center;
    background: linear-gradient(135deg, #E8F5E9 0%, #FFFFFF 50%, #E8F5E9 100%);
    padding: 3em;
}}

.chapter-cover .chapter-number {{
    font-size: 72pt;
    font-weight: 700;
    color: {COLORS['secondary']};
    opacity: 0.3;
    margin-bottom: 0.2em;
}}

.chapter-cover .chapter-title {{
    font-size: 28pt;
    font-weight: 700;
    color: {COLORS['primary']};
    line-height: 1.3;
    max-width: 80%;
    margin: 0 auto;
}}

.chapter-cover .chapter-subtitle {{
    font-size: 14pt;
    color: {COLORS['text_light']};
    margin-top: 1.5em;
    max-width: 70%;
}}

.chapter-cover .chapter-decoration {{
    width: 100px;
    height: 4px;
    background: linear-gradient(90deg, {COLORS['secondary']}, {COLORS['accent']});
    margin: 2em auto;
    border-radius: 2px;
}}

/* Checklist styling */
.checklist {{
    list-style: none;
    padding-left: 0;
}}

.checklist li {{
    padding-left: 1.5em;
    position: relative;
}}

.checklist li:before {{
    content: "☐";
    position: absolute;
    left: 0;
    color: {COLORS['secondary']};
}}
"""

# Chapter order
CHAPTER_ORDER = [
    "00_introduction",
    "01_company_types",
    "02_foreign_investors",
    "03_founding_steps",
    "04_pdpl_basics",
    "05_consent",
    "06_cross_border",
    "07_pdpl_compliance",
    "08_pdpl_penalties",
    "09_cybersecurity_ecosystem",
    "10_ecc_controls",
    "11_government_contracts",
    "12_compliance_advantage",
    "13_ai_landscape",
    "14_ai_products",
    "appendix_a_checklists",
    "appendix_b_templates",
    "appendix_c_resources",
    "appendix_d_glossary",
]

# Illustration mapping (chapter_id -> list of illustration files)
def get_illustrations_for_chapter(chapter_id):
    """Get illustration paths for a chapter."""
    illustrations = []

    # Map chapter IDs to illustration directories
    chapter_mapping = {
        "01_company_types": "ch01",
        "02_foreign_investors": "ch01",  # MISA is in ch01
        "03_founding_steps": "ch01",
        "04_pdpl_basics": "ch02",
        "05_consent": "ch02",
        "06_cross_border": "ch03",
        "07_pdpl_compliance": "ch03",
        "08_pdpl_penalties": "ch04",
        "09_cybersecurity_ecosystem": "ch05",
        "10_ecc_controls": "ch05",
        "11_government_contracts": "ch06",
        "12_compliance_advantage": "ch07",
        "13_ai_landscape": "ch08",
        "14_ai_products": "ch08",
    }

    if chapter_id in chapter_mapping:
        ch_dir = ILLUSTRATIONS / chapter_mapping[chapter_id]
        if ch_dir.exists():
            illustrations = sorted(ch_dir.glob("*.jpg")) + sorted(ch_dir.glob("*.png"))

    return illustrations


def create_cover_html(lang):
    """Create cover page HTML."""
    if lang == "ar":
        return f"""
        <div class="cover">
            <h1>البوصلة القانونية لشركات التقنية في السعودية</h1>
            <p class="subtitle">دليلك العملي للأنظمة والامتثال</p>
            <p class="author">د. عبدالله</p>
            <p class="year">٢٠٢٦</p>
        </div>
        """
    else:
        return f"""
        <div class="cover">
            <h1>The Legal Compass for Tech Companies in Saudi Arabia</h1>
            <p class="subtitle">Your Practical Guide to Regulations and Compliance</p>
            <p class="author">Dr. Abdullah</p>
            <p class="year">2026</p>
        </div>
        """


def create_toc_html(chapters_content, lang):
    """Create table of contents."""
    toc_title = "المحتويات" if lang == "ar" else "Table of Contents"

    toc_html = f'<div class="toc"><h2>{toc_title}</h2><ul>'

    for chapter_id, content in chapters_content:
        # Extract first heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
            toc_html += f'<li>{title}</li>'

    toc_html += '</ul></div>'
    return toc_html


def get_chapter_number(chapter_id):
    """Extract chapter number from chapter ID."""
    if chapter_id.startswith("00"):
        return ""
    elif chapter_id.startswith("appendix"):
        letter = chapter_id.split("_")[1].upper()
        return letter
    else:
        num = chapter_id.split("_")[0]
        return str(int(num))


def get_chapter_subtitle(chapter_id, lang):
    """Get subtitle/description for chapter cover."""
    subtitles = {
        "00_introduction": ("مقدمة الكتاب", "Book Introduction"),
        "01_company_types": ("نظام الشركات السعودي", "Saudi Companies Law"),
        "02_foreign_investors": ("الاستثمار الأجنبي", "Foreign Investment"),
        "03_founding_steps": ("خطوات عملية", "Practical Steps"),
        "04_pdpl_basics": ("نظام حماية البيانات الشخصية", "Personal Data Protection Law"),
        "05_consent": ("الموافقة والحقوق", "Consent and Rights"),
        "06_cross_border": ("نقل البيانات الدولي", "International Data Transfer"),
        "07_pdpl_compliance": ("الامتثال العملي", "Practical Compliance"),
        "08_pdpl_penalties": ("المخاطر والعقوبات", "Risks and Penalties"),
        "09_cybersecurity_ecosystem": ("الهيئة الوطنية للأمن السيبراني", "National Cybersecurity Authority"),
        "10_ecc_controls": ("الضوابط الأساسية", "Essential Controls"),
        "11_government_contracts": ("منصة اعتماد", "Etimad Platform"),
        "12_compliance_advantage": ("الميزة التنافسية", "Competitive Advantage"),
        "13_ai_landscape": ("سدايا والذكاء الاصطناعي", "SDAIA and AI"),
        "14_ai_products": ("بناء منتجات متوافقة", "Building Compliant Products"),
        "appendix_a_checklists": ("قوائم المراجعة", "Checklists"),
        "appendix_b_templates": ("النماذج الجاهزة", "Ready Templates"),
        "appendix_c_resources": ("المصادر والروابط", "Resources and Links"),
        "appendix_d_glossary": ("المصطلحات", "Glossary"),
    }

    if chapter_id in subtitles:
        return subtitles[chapter_id][0] if lang == "ar" else subtitles[chapter_id][1]
    return ""


def create_chapter_cover(title, chapter_id, lang):
    """Create a cover page for a chapter."""
    chapter_num = get_chapter_number(chapter_id)
    subtitle = get_chapter_subtitle(chapter_id, lang)

    # Display number or letter
    if chapter_num:
        if chapter_num.isalpha():
            display_num = chapter_num  # Appendix letter
        else:
            display_num = chapter_num if lang == "en" else chapter_num  # Could convert to Arabic numerals
    else:
        display_num = ""

    return f'''
    <div class="chapter-cover">
        <div class="chapter-number">{display_num}</div>
        <div class="chapter-decoration"></div>
        <h1 class="chapter-title">{title}</h1>
        <p class="chapter-subtitle">{subtitle}</p>
    </div>
    '''


def process_markdown(content, chapter_id, lang):
    """Convert markdown to HTML and add illustrations."""

    # Extract title from first heading
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Chapter"

    # Remove the first heading from content (we'll use it in cover)
    content = re.sub(r'^#\s+.+$', '', content, count=1, flags=re.MULTILINE)

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    html = md.convert(content)

    # Create chapter cover + content
    chapter_cover = create_chapter_cover(title, chapter_id, lang)

    # Add illustrations at the end of the chapter
    illustrations = get_illustrations_for_chapter(chapter_id)
    if illustrations:
        for img_path in illustrations[:2]:  # Max 2 images per chapter
            img_name = img_path.stem.replace("_", " ").title()
            html += f'''
            <div class="figure">
                <img src="file://{img_path}" alt="{img_name}">
                <p class="figure-caption">{img_name}</p>
            </div>
            '''

    return chapter_cover + f'<div class="chapter-content">{html}</div>'


def build_book(lang):
    """Build PDF book for a language."""

    chapters_dir = CHAPTERS_AR if lang == "ar" else CHAPTERS_EN
    output_file = OUTPUT_DIR / f"book_{lang}.pdf"

    print(f"\nBuilding {'Arabic' if lang == 'ar' else 'English'} PDF...")

    # Collect all chapter content
    chapters_content = []
    for chapter_id in CHAPTER_ORDER:
        chapter_file = chapters_dir / f"{chapter_id}.md"
        if chapter_file.exists():
            content = chapter_file.read_text(encoding='utf-8')
            chapters_content.append((chapter_id, content))
            print(f"  Added: {chapter_id}")

    # Build HTML document
    rtl_class = ' class="rtl"' if lang == "ar" else ''

    html_parts = [
        f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"></head>',
        f'<body{rtl_class}>',
        create_cover_html(lang),
        create_toc_html(chapters_content, lang),
    ]

    # Add chapters
    for chapter_id, content in chapters_content:
        chapter_html = process_markdown(content, chapter_id, lang)
        html_parts.append(f'<div class="chapter">{chapter_html}</div>')

    html_parts.append('</body></html>')

    full_html = '\n'.join(html_parts)

    # Save HTML for debugging
    html_file = OUTPUT_DIR / f"book_{lang}.html"
    html_file.write_text(full_html, encoding='utf-8')
    print(f"  HTML saved: {html_file}")

    # Generate PDF
    print(f"  Generating PDF...")
    HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(
        output_file,
        stylesheets=[CSS(string=CSS_STYLE)]
    )

    print(f"  PDF saved: {output_file}")
    return output_file


def main():
    """Build both Arabic and English PDFs."""

    print("=" * 60)
    print("Saudi Tech Legal Compass - PDF Builder")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Build both versions
    ar_pdf = build_book("ar")
    en_pdf = build_book("en")

    print("\n" + "=" * 60)
    print("PDF GENERATION COMPLETE")
    print("=" * 60)
    print(f"\nArabic PDF: {ar_pdf}")
    print(f"English PDF: {en_pdf}")

    # Show file sizes
    ar_size = ar_pdf.stat().st_size / (1024 * 1024)
    en_size = en_pdf.stat().st_size / (1024 * 1024)
    print(f"\nArabic: {ar_size:.1f} MB")
    print(f"English: {en_size:.1f} MB")


if __name__ == "__main__":
    main()
