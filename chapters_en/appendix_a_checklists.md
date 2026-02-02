# Appendix A: Checklists

This appendix serves as a practical toolkit for founders, CEOs, and compliance officers navigating the Saudi Arabian tech ecosystem. These checklists are designed to translate the complex regulatory requirements discussed in the preceding chapters into actionable steps. 

By following these guides, you ensure that your venture aligns with the **Vision 2030** objectives, the **New Companies Law (2023)**, the **Personal Data Protection Law (PDPL)**, and the **National Cybersecurity Authority (NCA)** standards.

---

## 1. Company Formation Checklist
Starting a tech company in Saudi Arabia has been streamlined through the **Saudi Business Center (SBC)**. Whether you are a local entrepreneur or a foreign investor via the **Ministry of Investment (MISA)**, use this checklist to ensure no step is missed.

### Phase 1: Pre-Incorporation Strategy
- [ ] **Select Legal Entity Type:** Decide between a Limited Liability Company (LLC), a Joint Stock Company (JSC), or the new **Simple Joint Stock Company (SJSC)** (Sharika Musahama Mubassata). *Tip: The SJSC is ideal for tech startups due to its flexibility in management and share classes.*
- [ ] **Reserve Trade Name:** Ensure the name complies with Ministry of Commerce (MoC) guidelines and does not infringe on existing trademarks.
- [ ] **Determine Capital Structure:** While there is often no high minimum capital for LLCs, certain MISA licenses for tech may require specific capital commitments.
- [ ] **Identify Shareholders and Managers:** Collect IDs for Saudis/GCC nationals or passports for foreign investors.

### Phase 2: Licensing and Registration
- [ ] **Obtain MISA Investment License (For Foreigners):** Apply via the MISA portal. Ensure your "ISIC" activity code matches "Information and Communication."
- [ ] **Draft Articles of Association (Aqd Al-Ta’sees):** Use the MoC standardized templates but customize clauses regarding "Drag-along/Tag-along" rights if you are an SJSC.
- [ ] **Issue Commercial Registration (Sijil Tijari - CR):** This is your company’s birth certificate.
- [ ] **Register with the Chamber of Commerce (GCCI):** Required within 30 days of CR issuance.

### Phase 3: Post-CR Mandatory Registrations
- [ ] **National Address (Shorfat):** Register your physical office location. Virtual offices are permitted for certain tech activities but check specific license requirements.
- [ ] **General Organization for Social Insurance (GOSI):** Essential for managing **Saudization (Nitaqat)** levels.
- [ ] **Zakat, Tax and Customs Authority (ZATCA):** Register for Zakat (for Saudis/GCC) or Income Tax (for foreigners) and **VAT** if your projected revenue exceeds SAR 375,000.
- [ ] **Muqeem/Qiwa Portals:** Essential for managing employee visas and labor contracts.

> **Pro-Tip:** Do not delay ZATCA registration. Failure to register for VAT within the statutory timeframe can result in heavy fines, even if you haven't started operations.

---

## 2. PDPL Compliance Checklist
The **Personal Data Protection Law (PDPL)**, overseen by the **Saudi Data and AI Authority (SDAIA)**, is mandatory for all entities processing data in the Kingdom. Use this checklist to ensure your tech product is "Privacy by Design."

### Administrative Compliance
- [ ] **Appoint a Data Protection Officer (DPO):** While not mandatory for all small businesses, it is highly recommended for tech companies processing sensitive data.
- [ ] **Create a Record of Processing Activities (RoPA):** Document what data you collect, why, where it is stored, and who has access.
- [ ] **Update Privacy Policy:** Ensure it is available in Arabic and English, clearly stating the legal basis for processing (e.g., Consent, Contractual Necessity).

### Technical and Operational Compliance
- [ ] **Implement Consent Management:** If relying on consent, ensure it is "explicit, informed, and freely given." Use checkboxes that are not pre-ticked.
- [ ] **Data Minimization Check:** Verify that your app/platform only collects the minimum data necessary for the service. (Reference: PDPL Article 11).
- [ ] **Data Localization Audit:** Ensure that personal data is processed within Saudi Arabia unless you meet the specific exemption criteria for **Cross-Border Data Transfer**.
- [ ] **Data Subject Rights (DSR) Workflow:** Create a process to handle user requests for:
    - Right to Access.
    - Right to Rectification (Correction).
    - Right to Destruction (Deletion).
- [ ] **Breach Notification Protocol:** Prepare a template to notify SDAIA within 72 hours if a data breach occurs that poses a risk to data subjects.

### Comparison: Consent vs. Legitimate Interest
| Feature | Consent (Muwafaqah) | Legitimate Interest |
| :--- | :--- | :--- |
| **Usage** | Marketing, Sensitive Data | Security, Fraud Prevention |
| **Revocability** | Can be withdrawn anytime | Harder to contest if proven |
| **Requirement** | Explicit Action (Opt-in) | Internal Assessment |

---

## 3. ECC Checklist for Small Businesses
The **Essential Cybersecurity Controls (ECC-1:2018)** issued by the **National Cybersecurity Authority (NCA)** are the gold standard. For tech SMEs, these controls are often a prerequisite for signing contracts with government entities or large corporations like Aramco or STC.

### Category 1: Cybersecurity Governance
- [ ] **Cybersecurity Policy:** Draft a formal document signed by the CEO/Founder outlining the company’s commitment to security.
- [ ] **Roles and Responsibilities:** Formally assign cybersecurity oversight to a specific team member.
- [ ] **Risk Management:** Conduct an annual cybersecurity risk assessment.

### Category 2: Cybersecurity Defense
- [ ] **Asset Management:** Maintain an inventory of all hardware and software used in the company.
- [ ] **Identity and Access Management (IAM):**
    - [ ] Implement Multi-Factor Authentication (MFA) for all remote access.
    - [ ] Use the "Principle of Least Privilege" (employees only access what they need).
- [ ] **Data Protection:** Ensure data "at rest" and "in transit" is encrypted using AES-256 or equivalent standards.
- [ ] **Vulnerability Management:** Perform regular software updates and patch management.

### Category 3: Cybersecurity Resilience
- [ ] **Backup Management:** Maintain encrypted, off-site (or cloud-based within KSA) backups.
- [ ] **Incident Response Plan:** A written guide on what to do during a DDoS attack or ransomware incident.

### Common Pitfalls in ECC Compliance
*   **Shadow IT:** Employees using unauthorized SaaS tools to store company data.
*   **Weak Password Policies:** Failing to enforce complex passwords and periodic changes.
*   **Ignoring Physical Security:** Leaving server rooms unlocked or laptops unencrypted in public spaces.

---

## 4. Government Tender Submission Checklist
The **Government Tenders and Procurement Law** and the **Etimad** portal have democratized access to government contracts. However, the requirements are rigid.

### Phase 1: Portal Readiness
- [ ] **Etimad Registration:** Ensure your company profile is active and your subscription is paid.
- [ ] **Classification (Tasneef):** For larger projects, ensure you have the required "Contractor Classification" for IT and Technology services.
- [ ] **Local Content Certificate:** Obtain a certificate from the **Local Content and Government Procurement Authority (LCGPA)**. This gives you a price preference in many tenders.

### Phase 2: Technical Proposal
- [ ] **Compliance Matrix:** Create a table showing how your solution meets every single technical requirement in the RFP (Request for Proposal).
- [ ] **Saudization Certificate:** A valid certificate from the Ministry of Human Resources and Social Development (MHRSD) is mandatory.
- [ ] **Cybersecurity Compliance:** Proof that your product meets NCA standards (ECC or CCC).

### Phase 3: Financial Proposal
- [ ] **Bid Bond (Daman Banki):** Usually 1% to 2% of the tender value. Ensure the bank guarantee is from a Saudi-licensed bank and is valid for the required duration (often 90-120 days).
- [ ] **Bill of Quantities (BoQ):** Fill out the pricing template exactly as requested. Do not change the format.
- [ ] **Zakat and Tax Certificates:** Ensure your certificates are valid and "Clearance" (Ikhla’ Tarf) is obtained.

### Summary of Mandatory Documents for Tenders
| Document Name | Arabic Term | Why it's needed |
| :--- | :--- | :--- |
| Commercial Registration | Sijil Tijari | Proof of legal existence |
| GOSI Certificate | Shahadat GOSI | Proof of labor law compliance |
| Zakat Certificate | Shahadat Zakat | Proof of tax compliance |
| Saudization Certificate | Shahadat Nitaqat | Proof of hiring locals |
| Chamber of Commerce | Al-Ghurfa Al-Tijariya | Validation of signatures |

---

## 5. Practical Tips and Action Plan

### The "First 90 Days" Checklist for Tech Founders
1.  **Day 1-30:** Focus on Legal Incorporation. Get your CR and MISA license. Open a local bank account (this can take time, so start early).
2.  **Day 31-60:** Focus on Talent and Infrastructure. Register on Qiwa, hire your core team, and set up your local cloud hosting (e.g., Oracle, Google Cloud, or Alibaba Cloud in KSA).
3.  **Day 61-90:** Focus on Compliance. Conduct your first PDPL audit and ensure your ECC controls are in place before your first major B2B sales pitch.

### Common Mistakes to Avoid
*   **Using Foreign Templates:** Never use a US or UK Privacy Policy for a Saudi company. The PDPL has specific requirements regarding "Sensitive Data" and "Credit Data" that Western templates miss.
*   **Ignoring "Local Content":** Even if your tech is superior, you may lose a government tender if your Local Content score is zero. Hire Saudis, use local suppliers, and keep your spend within the Kingdom.
*   **Delayed Saudization:** The **Nitaqat** system is automated. If your ratio drops, your ability to issue or renew visas will be instantly blocked in the **Qiwa** portal.

### Useful Legal References
*   **New Companies Law:** Royal Decree No. M/132.
*   **PDPL:** Royal Decree No. M/19, as amended by M/148.
*   **Government Procurement Law:** Royal Decree No. M/128.
*   **ECC-1:2018:** Issued by the National Cybersecurity Authority.

---

## Conclusion
Compliance in Saudi Arabia is no longer a "check-the-box" exercise; it is a fundamental part of the business strategy. By utilizing these checklists, tech companies can move from a state of regulatory risk to a state of competitive advantage. 

The Saudi market rewards those who demonstrate commitment to the local regulatory environment. Whether it is through protecting user data via the PDPL or contributing to the national economy through Local Content, your compliance is your ticket to long-term success in the Middle East's largest tech frontier.