# 🛡️ SysAuditDump - Windows Auditing Tool

A modular Python-based auditing tool for checking local system weaknesses on Windows machines. Useful for system administrators, cybersecurity students, and CEH learners.

---

## 📦 Modules Included

- 🔍 `user_audit.py`: Local user account enumeration
- 🔐 `password_policy_check.py`: Weak password policies
- 🔒 `auto_login_check.py`: Checks for registry-based autologin
- 📂 `smb_share_enum.py`: Public/shared folders via SMB
- 🧪 `hash_dump.py`: Dumps password hashes from SAM (admin only)
- 📝 `report_generator.py`: Runs all modules and generates final report

---

## ⚠️ Note

- Designed for lab/testing environments
- Requires **Python 3** and **admin privileges** for some modules
- Outputs saved in `report/audit_report.txt`

---

## 📸 Screenshot
![Screenshot 2025-07-05 021637](https://github.com/user-attachments/assets/d4efce91-3447-4923-a9d9-a789e2732391)



---

## 👨‍💻 Author

Made by [Kuldeep](https://github.com/404Nexus) — Cybersecurity Enthusiast & CEH Learner 🔐

