# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **book writing project** (not a software codebase) for "البوصلة القانونية لشركات التقنية في السعودية" (The Legal Compass for Tech Companies in Saudi Arabia).

The book is a practical guide covering:
- Saudi company formation (Companies Law 2023)
- Personal Data Protection Law (PDPL)
- Cybersecurity controls (ECC/NCA)
- Government contracts and Etimad platform
- AI regulations and SDAIA guidelines

## Book Structure

### Introduction (10-15 pages)
- Why this book now, how to read it, map of Saudi tech regulations, real case study

### Part 1: Founding Your Tech Company (40-50 pages)
Based on Saudi Companies Law 2023

- **Chapter 1:** Company types comparison (LLC, Simplified Joint Stock SJS, Single-person company)
- **Chapter 2:** Foreign investors and Saudi market (100% foreign ownership, MISA licenses, Nitaqat requirements, local partner needs)
- **Chapter 3:** Practical founding steps (platforms, documents, costs, timeline, common mistakes)

### Part 2: Personal Data Protection - PDPL (50-60 pages)
Based on PDPL and its Executive Regulations

- **Chapter 4:** PDPL basics (personal data definition, sensitive data, data controller, processing vs transfer vs disclosure)
- **Chapter 5:** Consent and legal bases (explicit consent requirements, 7 exceptions, privacy notice templates)
- **Chapter 6:** Cross-border data transfer (default prohibition, 10 allowed exceptions, adequate protection countries, AWS/cloud case study)
- **Chapter 7:** Practical compliance (DPIA, DPO appointment, SDAIA registration, breach reporting, full checklist)
- **Chapter 8:** Penalties and risks (up to 5M SAR fines, up to 2 years imprisonment, reputational damage)

### Part 3: Cybersecurity and Government Contracts (40-50 pages)
Based on NCA's Essential Cybersecurity Controls (ECC)

- **Chapter 9:** Saudi cybersecurity ecosystem (NCA role, ECC/CCC/CSCC controls map, who must comply, ECC-PDPL relationship)
- **Chapter 10:** Essential controls explained (governance, asset management, identity/access, app protection, encryption, backup, vulnerability management, incident response)
- **Chapter 11:** Winning government contracts (Etimad platform, competition types, reading tender documents, pricing, fatal proposal mistakes, winning AI project case study)
- **Chapter 12:** Compliance as competitive advantage (recognized certifications, marketing compliance, building government trust)

### Part 4: SDAIA and Artificial Intelligence (20-30 pages)
Based on SDAIA's AI Ethics Principles

- **Chapter 13:** AI regulatory landscape (SDAIA role, National Data & AI Strategy, ethics principles, transparency requirements)
- **Chapter 14:** Building compliant AI products (algorithmic bias avoidance, explainability, LLM governance, using Saudi data for training, compliant government chatbot case study)

### Appendices (30-40 pages)
- **Appendix A:** Checklists (company founding, PDPL compliance, ECC for SMEs, government tender submission)
- **Appendix B:** Ready templates (privacy notice AR/EN, internal data policy, DPA, DPIA, breach report)
- **Appendix C:** Links and resources (all regulations, government platforms, contacts)
- **Appendix D:** Glossary (Arabic-English legal/technical terms)
- **Appendix E:** Post-publication updates (how to follow updates, electronic supplement link)

## Commands

```bash
# Setup
cp .env.example .env          # Then add your GEMINI_API_KEY
pip install -r requirements.txt

# Write both Arabic and English versions (default)
python scripts/write_book.py

# Write only Arabic version
python scripts/write_book.py --lang ar

# Write only English version
python scripts/write_book.py --lang en

# Generate all illustrations (fully automated)
python scripts/generate_illustrations.py

# Build styled PDFs (white, green, dark grey theme)
python scripts/build_pdf.py
```

### Book Writer (`write_book.py`)
- AI writes all 14 chapters + 4 appendices
- **Two versions**: Arabic (`chapters_ar/`) and English (`chapters_en/`)
- Each chapter uses context from previous chapters for continuity
- Progress saved separately per language (resumable if interrupted)
- Target: ~60,000 words per language (~120,000 total)

### Illustration Generator (`generate_illustrations.py`)
- AI analyzes book spec and plans 20-30 illustrations
- Plan saved to `illustrations/illustration_plan.json`
- Images generated using Gemini and saved by chapter

To restart from scratch, delete `chapters_ar/progress.json`, `chapters_en/progress.json`, or `illustrations/illustration_plan.json`.

## Repository Structure

- `book-project-spec.md` - Book specification (Arabic)
- `scripts/write_book.py` - Automated book writer (AR + EN)
- `scripts/generate_illustrations.py` - Automated illustration generator
- `chapters_ar/` - Arabic chapters (Markdown)
- `chapters_en/` - English chapters (Markdown)
- `illustrations/` - Generated illustrations by chapter
- `requirements.txt` - Python dependencies

## Key Information

**Target audience:** Saudi tech entrepreneurs, foreign companies entering Saudi market, developers working with government entities, investors, and students.

**Language:** Arabic with English technical terms. The book targets 200-250 pages (50,000-60,000 words).

**Illustrations:** 20-30 diagrams and charts, created using Gemini API with model `gemini-3-pro-image-preview`.

**Primary references:**
- PDPL: https://sdaia.gov.sa
- Companies Law: https://mc.gov.sa
- NCA Cybersecurity Controls: https://nca.gov.sa
- Investment: https://misa.gov.sa
- Government Procurement: https://etimad.sa
