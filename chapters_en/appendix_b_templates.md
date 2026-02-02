# Appendix B: Ready Templates

This appendix provides a comprehensive toolkit of templates designed specifically for tech companies operating in the Kingdom of Saudi Arabia (KSA). These documents are drafted to align with the **Personal Data Protection Law (PDPL)** issued by Royal Decree No. (M/19) and its **Implementing Regulations**, as overseen by the **Saudi Data and AI Authority (SDAIA)**.

While these templates provide a robust starting point, remember that "copy-pasting" is not compliance. You must customize these documents to reflect your specific data flows, tech stack, and business model.

---

## 1. Privacy Notice Template (Bilingual: English/Arabic)

Under **Article 13** of the PDPL, you must provide a Privacy Notice (*إشعار الخصوصية*) to data subjects before or at the time of collecting their data. For tech companies, this is usually hosted on your website or within your app.

### Practical Tip: The "Layered" Approach
Don't overwhelm users with a 20-page document on the first screen. Use a "Layered Notice":
1.  **Layer 1:** A summary "Pop-up" or "Privacy Dashboard" highlighting the most critical info (What we collect and why).
2.  **Layer 2:** The full Privacy Notice (Template below).

#### Template: Privacy Notice

| Section / البند | English Description | (باللغة العربية) الوصف |
| :--- | :--- | :--- |
| **1. Introduction** | This notice explains how [Company Name] collects and processes your personal data in KSA. | يوضح هذا الإشعار كيف تقوم [اسم الشركة] بجمع ومعالجة بياناتك الشخصية في المملكة. |
| **2. Data We Collect** | We collect: Name, Email, Phone, National ID (*Huwiyah*), and Usage Data. | نجمع: الاسم، البريد الإلكتروني، رقم الجوال، الهوية الوطنية، وبيانات الاستخدام. |
| **3. Purpose** | We process data to provide services, verify identity via *Nafath*, and improve our App. | نعالج البيانات لتقديم الخدمات، والتحقق من الهوية عبر "نفاذ"، وتحسين التطبيق. |
| **4. Legal Basis** | We rely on [Consent / Performance of Contract / Legitimate Interest]. | نعتمد على [الموافقة / تنفيذ العقد / المصلحة المشروعة]. |
| **5. Data Sharing** | We share data with [List Partners, e.g., Cloud Providers] within KSA. | نشارك البيانات مع [قائمة الشركاء] داخل المملكة العربية السعودية. |
| **6. Your Rights** | You have the right to access, correct, and destroy your data. | لديك الحق في الوصول إلى بياناتك، وتصحيحها، وإتلافها. |

**Full Text Draft:**

> **Privacy Notice for [App/Company Name]**
>
> **1. Identity of the Controller:** [Insert Legal Entity Name], CR No. [Insert Number], Address: [Insert Saudi Office Address].
> **2. Collection of Data:** We collect information you provide directly (e.g., during registration) and automatically (e.g., IP address).
> **3. Purpose of Processing:** In accordance with PDPL principles, we only collect data necessary to:
> *   Authenticate users via the National Single Sign-On (*Nafath*).
> *   Process payments through local gateways.
> *   Comply with Saudi regulatory requirements (e.g., CITC/CST regulations).
> **4. Data Retention:** We store your data for [X years] as per the statutory requirements of the [Relevant Saudi Authority, e.g., SAMA].
> **5. Security:** We implement technical and organizational measures as per the National Cybersecurity Authority (NCA) standards.
> **6. Contact:** For any data requests, contact our Data Protection Officer (DPO) at [Email Address].

---

## 2. Internal Data Protection Policy Template

This is a "living" document for your employees. It tells your developers, marketers, and HR staff how they are allowed to handle data. Under **Article 30** of the Implementing Regulations, organizations must establish internal policies to ensure compliance.

### Practical Example: The "Developer Rule"
A common mistake in Saudi startups is developers using "Live Production Data" to test new features. Your internal policy should explicitly forbid this, requiring "Anonymized Data" (*بيانات مجهولة المصدر*) for testing environments.

#### Template: Internal Data Protection Policy

**1. Purpose**
This policy defines the requirements for protecting Personal Data at [Company Name] to ensure compliance with the Saudi PDPL.

**2. Scope**
Applies to all employees, contractors, and third-party consultants.

**3. Data Minimization (*الحد من البيانات*)**
*   Employees shall only collect the minimum amount of data necessary for their specific task.
*   "Just in case" data collection is strictly prohibited.

**4. Access Control**
*   Access to sensitive data (e.g., Health data or Bio-metric data) is restricted based on the "Principle of Least Privilege."
*   Multi-Factor Authentication (MFA) is mandatory for all internal systems accessing user databases.

**5. Training**
*   All staff must undergo PDPL awareness training annually.
*   New developers must be trained on "Privacy by Design" (*الخصوصية بالتصميم*).

**6. Data Retention and Disposal**
*   Data must be deleted once the purpose for collection expires.
*   Physical documents must be shredded; digital data must be "wiped" using approved software.

> **Warning:** Failure to have an internal policy can be seen by SDAIA as a sign of "negligence," which can increase the severity of fines under **Article 35** of the PDPL.

---

## 3. Data Processing Agreement (DPA) Template

If your tech company is a B2B SaaS provider, your clients (the "Controllers") will require you (the "Processor") to sign a DPA. Alternatively, if you outsource your cloud hosting to a provider like *STC Cloud* or *Oracle Saudi Arabia*, you need a DPA with them.

**Legal Reference:** **Article 16** of the PDPL states that a Controller must choose a Processor that provides sufficient guarantees to protect data.

#### Template: Data Processing Agreement

**Between:**
1.  **[Controller Name]** (The Client)
2.  **[Processor Name]** (The Tech Provider/You)

**1. Subject Matter**
The Processor shall process personal data only on the documented instructions of the Controller.

**2. Obligations of the Processor:**
*   **Confidentiality:** Ensure all personnel processing data are bound by non-disclosure agreements (NDAs).
*   **Sub-processors:** The Processor shall not engage another sub-processor (e.g., a third-party API) without prior written authorization from the Controller.
*   **Security:** Implement measures equivalent to the ECC-1:2018 (Essential Cybersecurity Controls).
*   **Audit Rights:** Allow the Controller or a Saudi-certified auditor to inspect the Processor’s facilities.

**3. Data Transfers**
The Processor shall not transfer personal data outside of Saudi Arabia unless such transfer complies with the **Cross-Border Data Transfer Regulations** (Chapter 6 of this book).

**4. Breach Notification**
The Processor must notify the Controller within [e.g., 24 hours] of becoming aware of any data breach.

---

## 4. Data Protection Impact Assessment (DPIA) Template

A DPIA (*تقييم الأثر على حماية البيانات*) is mandatory under **Article 27** of the Implementing Regulations if your processing involves "High Risk." This includes large-scale processing of sensitive data, automated decision-making (AI), or monitoring of public areas.

### Practical Context: AI Startups
If you are building an AI tool that analyzes user behavior to provide credit scoring in the Saudi market, a DPIA is **not optional**. It is a prerequisite for launching.

#### Template: DPIA Form

| Section | Questions to Answer |
| :--- | :--- |
| **Project Description** | What is the new tech feature? (e.g., AI-driven facial recognition for check-ins). |
| **Necessity & Proportionality** | Is there a less intrusive way to achieve the goal? Why do you need this specific data? |
| **Risk Assessment** | What is the risk to the user if this data is leaked? (High/Medium/Low). |
| **Mitigation Measures** | How will we reduce risk? (e.g., Encryption, Tokenization, Local Hosting). |
| **SDAIA Consultation** | Does this risk remain "High" even after mitigation? If yes, you must consult SDAIA. |

**DPIA Workflow for Developers:**
1.  **Map the Flow:** Use a flowchart to show where data enters the app, where it is stored (e.g., Riyadh Region AWS), and who sees it.
2.  **Identify Vulnerabilities:** Is the API encrypted? Is the database behind a firewall?
3.  **Sign-off:** The CEO or the DPO must sign the DPIA before the "Push to Production."

---

## 5. Data Breach Notification Template

If a breach occurs, the clock starts ticking. Under the PDPL, you must notify SDAIA within **72 hours** if the breach poses a risk to data subjects.

### Pro-Tip: The "Incident Response Playbook"
Don't wait for a hack to write this. Keep this template in a "Break Glass in Case of Emergency" folder.

#### Template: Notification to SDAIA

**To:** Saudi Data and AI Authority (SDAIA)
**Subject:** Formal Notification of Personal Data Breach

**1. General Information**
*   **Entity Name:** [Legal Entity Name]
*   **Contact Person:** [DPO Name and Mobile Number]
*   **Date/Time of Discovery:** [YYYY-MM-DD / HH:MM]

**2. Nature of the Breach**
*   **Type:** (e.g., Unauthorized access, Accidental loss, Ransomware).
*   **Categories of Data:** (e.g., Customer names, IBANs, National ID numbers).
*   **Number of Data Subjects Affected:** [Approximate Number].

**3. Likely Consequences**
*   Describe potential harm (e.g., Identity theft, financial loss, or reputational damage to users).

**4. Measures Taken/Proposed**
*   [e.g., We have isolated the affected server, reset all user passwords, and notified the National Cybersecurity Center (NCSC)].

**5. Notification to Users**
*   Have users been notified? [Yes/No]. If no, provide the planned timeline.

---

## Summary Table: Which Template to Use When?

| Scenario | Required Template | Legal Reference |
| :--- | :--- | :--- |
| Launching a new Mobile App | **Privacy Notice** | PDPL Art. 13 |
| Hiring new employees | **Internal Data Protection Policy** | PDPL Art. 30 |
| Signing a SaaS contract with a client | **Data Processing Agreement (DPA)** | PDPL Art. 16 |
| Launching an AI feature using bio-metrics | **DPIA Template** | PDPL Art. 27 |
| Discovering a database leak | **Breach Notification Template** | PDPL Art. 20 |

---

## Practical Tips and Common Mistakes

### ❌ Common Mistakes
1.  **Using GDPR Templates verbatim:** While the PDPL is similar to GDPR, there are unique Saudi requirements regarding **National ID (*Huwiyah*)** handling and specific **Cross-Border Transfer** rules. A European template will not mention SDAIA or the Saudi National Cybersecurity Authority (NCA).
2.  **Ignoring the Arabic Version:** For B2C apps in Saudi Arabia, your Privacy Notice **must** be available in Arabic. In a dispute, the Saudi courts will prioritize the Arabic text.
3.  **Vague Retention Periods:** Avoid saying "we keep data as long as needed." Specify a time frame (e.g., "10 years as per Saudi Companies Law" or "5 years as per SAMA requirements").

### ✅ Actionable Tips for Entrepreneurs
*   **Automate Consent:** Use "Consent Management Platforms" (CMPs) that are configured for the Saudi PDPL. This ensures you have a timestamped record of every user’s "I Agree" (*أوافق*).
*   **Appoint a Point of Contact:** Even if you aren't legally required to have a formal "Data Protection Officer" (DPO), designate one person in your tech team to be the "Privacy Lead."
*   **Keep a Record of Processing Activities (RoPA):** This is a simple spreadsheet listing every category of data you hold, where it's stored, and who has access. It is the first thing SDAIA will ask for during an audit.

---

## Final Reminder
These templates are tools to help you navigate the "Legal Compass." Use them to build trust with your Saudi customers and investors. In the modern Saudi economy, **Data is the New Oil**, and protecting it is not just a legal obligation—it is a competitive advantage.

> **Legal Disclaimer:** These templates are for informational purposes only and do not constitute legal advice. Regulations in Saudi Arabia are subject to updates by SDAIA and other regulatory bodies. Always consult with a Saudi-qualified legal counsel before finalizing your legal documents.