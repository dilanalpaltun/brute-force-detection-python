# Python Brute Force Detection System 🔐

This project is a simple Python-based authentication system designed to detect
failed login attempts and brute force attacks.  
It logs security events and integrates with **Wazuh SIEM** for security monitoring.

---

## 🚀 Features
- Secure password hashing (SHA-256)
- Failed login attempt logging
- Temporary account lock after multiple failed attempts
- Brute force attack detection
- Security event logging to file
- Wazuh SIEM rule integration

---

## 🛠️ Technologies Used

- Python 3
- hashlib
- time
- Wazuh SIEM

---

## 📂 Project Structure

python-bruteforce-detection/
│
├── auth_system.py
├── auth_security.log
├── wazuh_rules.xml
└── README.md
