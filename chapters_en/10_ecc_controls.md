# Chapter 10: Essential Controls - Practical Explanation

In the previous chapter, we explored the high-level ecosystem of Saudi Arabia’s cybersecurity landscape and the pivotal role of the National Cybersecurity Authority (NCA - *Al-Hay’ah al-Wataniyyah li-Amn al-Siybrani*). Now, we move from the "who" and "why" to the "how."

For any tech entrepreneur or international company operating in the Kingdom, the **Essential Cybersecurity Controls (ECC)** are not merely suggestions; they are the bedrock of your operational legitimacy. In 2024, the NCA updated these controls to reflect the evolving threat landscape and the rapid digital transformation of the Saudi economy under Vision 2030.

This chapter provides a practical, deep-dive explanation of the ECC 2024. We will strip away the dense regulatory language and focus on what you actually need to build, document, and maintain to ensure compliance and, more importantly, to protect your business.

---

## 1. Cybersecurity Governance (Al-Hukama al-Siybraniyyah)

Governance is the "brain" of your cybersecurity program. Without it, your technical tools are just expensive toys. In the Saudi market, the NCA places heavy emphasis on accountability at the board and executive levels.

### The Cybersecurity Strategy and Policy (Control 1-1)
You cannot simply "do" cybersecurity; you must define it. The ECC requires a documented Cybersecurity Policy.
*   **Practical Tip:** Do not download a generic template from the internet. Your policy must be tailored to your specific tech stack (e.g., if you are a SaaS company on STC Cloud, your policy should reflect cloud-native risks).
*   **Actionable Step:** Ensure your policy is approved by the CEO or the Board. In Saudi audits, an unsigned policy is treated as non-existent.

### Cybersecurity Roles and Responsibilities (Control 1-2)
The NCA requires a clear organizational structure. For startups, this doesn't mean you need a 50-person team, but you must designate a **Cybersecurity Officer** (often referred to as a CISO).
*   **The Saudi Context:** If you are a larger entity or a government contractor, there may be "Saudization" (*Nitaqat*) requirements for sensitive cybersecurity roles.
*   **Warning:** Avoid "Conflict of Interest." The person managing IT operations should not be the same person auditing cybersecurity. They are two different functions: one builds the house, the other checks the locks.

### Cybersecurity Risk Management (Control 1-3)
Risk management is about prioritizing your budget. You must conduct a formal **Cybersecurity Risk Assessment** at least once a year.
*   **Example:** A fintech app in Riyadh should prioritize "Data Leakage" and "Unauthorized Transaction" risks over "Physical Office Intrusion" if most of its staff works remotely.

---

## 2. Asset Management (Idarat al-Usul)

You cannot protect what you don't know you have. Asset management is often the weakest link for fast-growing Saudi startups that spin up cloud servers daily.

### Asset Inventory (Control 2-1)
The ECC 2024 mandates a comprehensive inventory of all hardware, software, and data assets.
*   **Practical Approach:** Use automated discovery tools. If you are using AWS (Riyadh Region) or Google Cloud (Dammam), use their native tagging and inventory services.
*   **Table: What to Track in Your Inventory**

| Asset Type | Examples | Key Detail Needed |
| :--- | :--- | :--- |
| **Hardware** | Laptops, Servers, Firewalls | Serial Number, User, Location |
| **Software** | OS, Databases, SaaS tools | Version, License Expiry |
| **Data** | Customer PII, Financial Records | Sensitivity Level (Top Secret to Public) |
| **People** | Employees, Contractors | Access Level, Nationality |

### Acceptable Use of Assets (Control 2-2)
You must define an "Acceptable Use Policy" (AUP). This tells your employees that they shouldn't use their work laptops for personal crypto mining or visiting high-risk websites. 
*   **Practical Tip:** Include the AUP in the onboarding package for every new hire in your Saudi office. Have them sign it digitally.

---

## 3. Identity and Access Management (IAM)

In the world of Saudi cybersecurity, "Identity is the new perimeter." With the rise of remote work and cloud services, controlling *who* accesses *what* is critical.

### User Access Management (Control 3-1)
The core principle here is **Least Privilege** (*Mabda' al-Salahiyyat al-Duqqa*). Users should only have the access necessary for their job—nothing more.
*   **Common Mistake:** Giving "Admin" rights to every developer. In an NCA audit, this is a major red flag.
*   **Practical Step:** Implement a formal "Joiners, Movers, Leavers" process. When an employee leaves your company, their access must be revoked immediately (ideally within 4 hours).

### Multi-Factor Authentication (MFA)
Under ECC 2024, MFA is no longer optional for administrative access or remote access.
*   **Saudi Context:** If your application integrates with government services, you might need to interface with **Nafath** (the National Single Sign-On). For internal systems, using apps like Microsoft Authenticator or hardware keys (YubiKeys) is highly recommended.

### Privileged Access Management (PAM)
Privileged accounts (those with power to delete databases or change security settings) require extra scrutiny.
*   **Actionable Tip:** Use a "Jump Server" or a PAM solution to record what admins do. If a database is deleted at 2:00 AM on a Friday (the Saudi weekend), you need a log of exactly who did it.

---

## 4. Application Protection (Himayat al-Tatbiqat)

For tech companies, your code is your most valuable asset—and your biggest vulnerability.

### Secure Software Development Life Cycle (S-SDLC)
The NCA requires that security be baked into the development process, not bolted on at the end.
*   **Practical Tip for Developers:** Use the **OWASP Top 10** as your checklist.
*   **Separation of Environments:** You must have separate environments for Development (*Tatwir*), Testing (*Ikhtibar*), and Production (*Intaj*). Production data should **never** be used in the development environment.

### API Security
Since many Saudi tech companies are built on APIs (Application Programming Interfaces)—especially in the Open Banking and Logistics sectors—securing these endpoints is vital.
*   **Warning:** Unprotected APIs are the leading cause of data breaches in the region. Ensure all APIs require authentication and use rate-limiting to prevent DDoS attacks.

---

## 5. Cryptography Management (Al-Tashfir)

Cryptography is the art of scrambling data so that even if it is stolen, it is useless to the thief.

### Encryption Standards (Control 5-1)
The NCA specifies that you must use "strong and industry-recognized" encryption algorithms.
*   **Practical Tip:** Avoid "rolling your own crypto." Use AES-256 for data at rest and TLS 1.2 or 1.3 for data in transit. 
*   **Key Management:** How you store the "keys" to the encryption is more important than the encryption itself. Do not store encryption keys in the same database as the encrypted data. Use a Key Management Service (KMS).

### Data Residency and Encryption
Under the Saudi PDPL (Personal Data Protection Law), certain sensitive data must remain within the Kingdom. When this data is stored in the cloud, it must be encrypted using keys that you—the company—control, not just the cloud provider.

---

## 6. Backup and Recovery (Al-Nuskh al-Ihtiyati wa al-Isti'adah)

In Saudi Arabia, ransomware attacks are a significant threat. Your backup is your last line of defense.

### The 3-2-1 Rule
A practical standard to meet ECC requirements:
1.  **3 Copies of Data:** The original and two backups.
2.  **2 Different Media:** e.g., Cloud storage and a local NAS.
3.  **1 Offsite Copy:** For a Saudi company, this means a backup in a different geographic region (e.g., if your main server is in Riyadh, keep a backup in Jeddah or a different cloud zone).

### Testing the Restore (Control 6-2)
A backup that hasn't been tested is not a backup.
*   **Practical Tip:** Conduct a "Restoration Drill" every six months. Document the results. An auditor will ask: "When was the last time you successfully restored your database?" You need a dated log to prove it.

---

## 7. Vulnerability Management (Idarat al-Thughrat)

Hackers look for the easiest way in—usually an unpatched server or an old version of a plugin.

### Vulnerability Scanning
You should run automated scans on your network and applications regularly.
*   **Critical/High Vulnerabilities:** The ECC expects you to patch "Critical" vulnerabilities within a very short window (often 48-72 hours after a patch is released).

### Penetration Testing (Ikhtibar al-Ikhtiraq)
Once a year (or after any major update), hire a third-party cybersecurity firm to try and "hack" your systems.
*   **Practical Tip:** Ensure the firm you hire is authorized to operate in Saudi Arabia. The report they provide will be a key document for your compliance file.

---

## 8. Incident Response (Al-Istijabah lil-Hawadith)

It is not a matter of *if* you will be attacked, but *when*. The NCA requires you to be ready.

### Incident Response Plan (IRP)
You need a written plan that answers:
*   Who is in the "War Room"?
*   How do we isolate the infected servers?
*   When do we notify the NCA or the SDAIA (Saudi Data and AI Authority)?

### Reporting Requirements
Under Saudi regulations, major cybersecurity incidents must be reported to the NCA’s **Saudi Information Technology Center (SIRC)** within specific timeframes. 
*   **Warning:** Failing to report a significant breach can lead to heavy fines under the PDPL and ECC frameworks.

---

## 9. Simplified ECC Checklist for Tech Startups

To make this actionable, use the following checklist to evaluate your current status.

| Control Area | Action Item | Status (Done/Pending) |
| :--- | :--- | :--- |
| **Governance** | Do we have a signed Cybersecurity Policy? | |
| **Governance** | Is there a designated Cybersecurity Officer? | |
| **Assets** | Is our Asset Inventory updated this month? | |
| **Access** | Is MFA enabled for all staff emails and cloud consoles? | |
| **Access** | Have we removed access for all former employees? | |
| **App Security** | Are Dev, Test, and Prod environments separated? | |
| **Data** | Is customer PII encrypted at rest? | |
| **Backup** | Did we test a backup restoration in the last 6 months? | |
| **Vulnerability** | Are all "Critical" patches applied to our servers? | |
| **Incident** | Do we have the contact info for the NCA reporting portal? | |

---

## Practical Tips and Common Mistakes

### Mistake 1: "We are on the Cloud, so security is their problem."
This is a dangerous misconception. This is called the **Shared Responsibility Model**. The cloud provider (AWS, Google, STC Cloud) secures the "physical" data center. You are responsible for securing the data, the code, and the user access *inside* that cloud.

### Mistake 2: Treating ECC as a "One-Time Project."
Cybersecurity is a continuous cycle. An auditor will look for "evidence of operation." This means they don't just want to see your policy; they want to see the logs showing you followed that policy every day for the last year.

### Practical Tip: The "Evidence Folder"
Start a digital folder today. Every time you do a vulnerability scan, every time you train an employee on security, and every time you test a backup, save the report/screenshot in this folder. When the NCA or a major Saudi client (like Aramco or STC) asks for proof of security, you will be ready in minutes.

### The Saudi "Trust Factor"
In the Saudi market, cybersecurity is a competitive advantage. Large Saudi enterprises and government entities are extremely risk-averse. If you can prove—through ECC compliance—that your startup is secure, you will win contracts much faster than a competitor who treats security as an afterthought.

## Conclusion
The ECC 2024 is your roadmap to building a resilient tech company in the Kingdom. While the requirements may seem daunting, they are aligned with global best practices. By focusing on governance first, securing your identities, and maintaining a rigorous backup and patching schedule, you satisfy not just the regulators, but also your investors and customers.

In the next chapter, we will look at the specific technical standards for **Cloud Computing Compliance**, which builds upon these essential controls for companies hosted in the cloud.