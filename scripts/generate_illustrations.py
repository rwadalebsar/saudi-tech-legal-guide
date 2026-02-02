#!/usr/bin/env python3
"""
Fully automated illustration generator for the Saudi Tech Legal Compass book.
AI decides what illustrations are needed and generates them.
"""

import os
import json
import base64
from pathlib import Path
from datetime import datetime

from google import genai
from google.genai import types

# Configuration
BOOK_SPEC_PATH = Path(__file__).parent.parent / "book-project-spec.md"
ILLUSTRATIONS_DIR = Path(__file__).parent.parent / "illustrations"
PLAN_FILE = ILLUSTRATIONS_DIR / "illustration_plan.json"

# Ensure output directory exists
ILLUSTRATIONS_DIR.mkdir(exist_ok=True)

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

def generate_illustration_plan(client, book_spec):
    """Use AI to analyze book and decide what illustrations are needed."""

    planning_prompt = """You are an expert book illustrator. Create exactly 20 illustrations for a book about Saudi tech regulations.

Return a JSON array with this exact structure for each item:
{"chapter": "ch01", "type": "flowchart", "title_en": "Title", "title_ar": "عنوان", "description": "What it shows", "prompt": "Image generation prompt"}

Types: diagram, flowchart, comparison_table, infographic
Chapters: ch01-ch14, appendix_a, appendix_b

Cover these topics:
1. Company types comparison (LLC vs SJS vs Single-person)
2. MISA investment license process
3. Company registration steps
4. Personal data types under PDPL
5. Consent requirements flowchart
6. Cross-border data transfer rules
7. PDPL compliance checklist visual
8. PDPL penalties overview
9. NCA cybersecurity framework
10. ECC controls hierarchy
11. Etimad government procurement process
12. Compliance certification badges
13. SDAIA AI governance structure
14. AI ethics principles
15. Data classification pyramid
16. Privacy notice components
17. Breach notification timeline
18. Government contract lifecycle
19. Saudization (Nitaqat) zones
20. Tech company legal roadmap

Return ONLY valid JSON array, no markdown, no explanation."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[planning_prompt],
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=8000,
        )
    )

    # Parse JSON from response
    response_text = response.text.strip()
    # Remove markdown code blocks if present
    if "```" in response_text:
        parts = response_text.split("```")
        for part in parts:
            if part.strip().startswith("json"):
                response_text = part.strip()[4:].strip()
                break
            elif part.strip().startswith("["):
                response_text = part.strip()
                break

    # Try to fix common JSON issues
    response_text = response_text.strip()
    if not response_text.endswith("]"):
        # Find last complete object and close array
        last_brace = response_text.rfind("}")
        if last_brace > 0:
            response_text = response_text[:last_brace+1] + "]"

    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"  Warning: JSON parse error, using fallback plan")
        # Return a minimal fallback plan
        return [
            {"chapter": "ch01", "type": "comparison_table", "title_en": "Company Types Comparison", "title_ar": "مقارنة أنواع الشركات", "description": "LLC vs SJS vs Single-person company comparison", "prompt": "Professional infographic comparing three business entity types: LLC, Simplified Joint Stock, and Single-Person Company. Clean corporate style, blue color scheme, comparison table format with icons."},
            {"chapter": "ch02", "type": "flowchart", "title_en": "Foreign Investment Process", "title_ar": "عملية الاستثمار الأجنبي", "description": "Steps to obtain MISA license", "prompt": "Professional flowchart showing foreign investment license application process in Saudi Arabia. Steps include: Application, Review, Approval, Registration. Clean corporate style."},
            {"chapter": "ch04", "type": "diagram", "title_en": "Personal Data Types", "title_ar": "أنواع البيانات الشخصية", "description": "Classification of personal vs sensitive data under PDPL", "prompt": "Professional diagram showing data classification pyramid. Top: Sensitive Data, Bottom: Personal Data. Include examples for each category. Blue and teal corporate colors."},
            {"chapter": "ch05", "type": "flowchart", "title_en": "Consent Decision Tree", "title_ar": "شجرة قرارات الموافقة", "description": "When consent is required under PDPL", "prompt": "Decision tree flowchart for determining when explicit consent is required under Saudi PDPL. Yes/No branches leading to consent required or exception applies."},
            {"chapter": "ch06", "type": "infographic", "title_en": "Cross-Border Data Transfer", "title_ar": "نقل البيانات عبر الحدود", "description": "Rules for transferring data outside Saudi Arabia", "prompt": "Infographic showing cross-border data transfer rules. World map with Saudi Arabia highlighted, arrows showing data flow, checkmarks for allowed transfers, X for prohibited."},
            {"chapter": "ch09", "type": "diagram", "title_en": "NCA Cybersecurity Framework", "title_ar": "إطار الأمن السيبراني", "description": "Overview of ECC, CCC, CSCC controls", "prompt": "Hierarchical diagram showing Saudi National Cybersecurity Authority framework. Three pillars: ECC (Essential Controls), CCC (Cloud Controls), CSCC (Critical Systems Controls)."},
            {"chapter": "ch10", "type": "infographic", "title_en": "ECC Controls Overview", "title_ar": "نظرة عامة على الضوابط الأساسية", "description": "The main domains of Essential Cybersecurity Controls", "prompt": "Professional infographic showing 8 domains of ECC controls: Governance, Asset Management, Identity Management, Application Security, Cryptography, Backup, Vulnerability Management, Incident Response."},
            {"chapter": "ch11", "type": "flowchart", "title_en": "Government Procurement Process", "title_ar": "عملية المشتريات الحكومية", "description": "Etimad platform tender process", "prompt": "Flowchart showing government tender process via Etimad platform: Registration, Tender Search, Bid Submission, Evaluation, Award, Contract. Professional government style."},
            {"chapter": "ch13", "type": "diagram", "title_en": "SDAIA AI Governance", "title_ar": "حوكمة الذكاء الاصطناعي", "description": "SDAIA role in AI regulation", "prompt": "Organizational diagram showing SDAIA structure and role in Saudi AI governance. Include National Data and AI Strategy elements."},
            {"chapter": "ch14", "type": "infographic", "title_en": "AI Ethics Principles", "title_ar": "مبادئ أخلاقيات الذكاء الاصطناعي", "description": "Saudi AI ethics principles visualization", "prompt": "Circular infographic showing 6 AI ethics principles: Fairness, Transparency, Accountability, Privacy, Security, Human Oversight. Modern tech style with icons."}
        ]

def generate_single_illustration(client, illustration_info, index):
    """Generate a single illustration using Gemini image model."""

    # Create optimized prompt for professional book illustration
    image_prompt = f"""Create a professional, clean illustration for a business/legal book.
Style: Modern, minimalist, professional infographic style suitable for print.
Colors: Use a professional color palette with blues, teals, and accent colors.
Text: Include clear labels in English (Arabic text will be added later).
Layout: Clean, well-organized, easy to understand at a glance.

Illustration request:
{illustration_info['prompt']}

Title: {illustration_info['title_en']}
Type: {illustration_info['type']}

Important: This is for a professional book about Saudi Arabian tech regulations. Keep it clean, corporate, and informative."""

    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[image_prompt],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT']
            )
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                return part.inline_data.data, part.inline_data.mime_type

        return None, None

    except Exception as e:
        print(f"  Error generating illustration: {e}")
        return None, None

def save_illustration(image_data, mime_type, illustration_info, index):
    """Save the generated illustration to disk."""

    # Determine file extension
    ext = "png" if "png" in mime_type else "jpg"

    # Create chapter directory
    chapter = illustration_info.get("chapter", "misc")
    chapter_dir = ILLUSTRATIONS_DIR / chapter
    chapter_dir.mkdir(exist_ok=True)

    # Generate filename
    safe_title = illustration_info['title_en'].lower().replace(" ", "_")[:30]
    filename = f"{index:02d}_{safe_title}.{ext}"
    filepath = chapter_dir / filename

    # Save image
    with open(filepath, "wb") as f:
        f.write(image_data)

    return filepath

def main():
    """Main automation flow."""
    print("=" * 60)
    print("Saudi Tech Legal Compass - Illustration Generator")
    print("=" * 60)

    client = get_client()
    book_spec = read_book_spec()

    # Step 1: Check for existing plan or generate new one
    if PLAN_FILE.exists():
        print("\nFound existing illustration plan. Loading...")
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            plan = json.load(f)
        print(f"Loaded plan with {len(plan)} illustrations")
    else:
        print("\nStep 1: AI is analyzing the book and planning illustrations...")
        plan = generate_illustration_plan(client, book_spec)

        # Save the plan
        with open(PLAN_FILE, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        print(f"Created plan with {len(plan)} illustrations")
        print(f"Plan saved to: {PLAN_FILE}")

    # Step 2: Generate illustrations
    print(f"\nStep 2: Generating {len(plan)} illustrations...")
    print("-" * 40)

    results = []
    for i, illustration in enumerate(plan, 1):
        print(f"\n[{i}/{len(plan)}] {illustration['title_en']}")
        print(f"  Type: {illustration['type']}")
        print(f"  Chapter: {illustration.get('chapter', 'N/A')}")

        # Check if already generated
        chapter = illustration.get("chapter", "misc")
        safe_title = illustration['title_en'].lower().replace(" ", "_")[:30]
        existing = list((ILLUSTRATIONS_DIR / chapter).glob(f"*{safe_title}*")) if (ILLUSTRATIONS_DIR / chapter).exists() else []

        if existing:
            print(f"  Skipping (already exists): {existing[0].name}")
            results.append({"status": "skipped", "path": str(existing[0])})
            continue

        print("  Generating...")
        image_data, mime_type = generate_single_illustration(client, illustration, i)

        if image_data:
            filepath = save_illustration(image_data, mime_type, illustration, i)
            print(f"  Saved: {filepath}")
            results.append({"status": "success", "path": str(filepath)})
        else:
            print("  Failed to generate")
            results.append({"status": "failed", "illustration": illustration['title_en']})

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    success = sum(1 for r in results if r['status'] == 'success')
    skipped = sum(1 for r in results if r['status'] == 'skipped')
    failed = sum(1 for r in results if r['status'] == 'failed')
    print(f"Generated: {success}")
    print(f"Skipped (existing): {skipped}")
    print(f"Failed: {failed}")
    print(f"\nIllustrations saved to: {ILLUSTRATIONS_DIR}")

if __name__ == "__main__":
    main()
