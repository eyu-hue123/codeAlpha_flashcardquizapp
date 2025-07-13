# 🔐 CodeAlpha Task 3: Secure Coding Review

## 📌 Internship Domain
Cybersecurity — CodeAlpha Internship Program

## 👨‍💻 Intern Info
- Name: Bereket
- Role: Web Developer Trainee @ ASTU
- Tech Stack Used: HTML, CSS, JavaScript

---

## 🧾 Project Overview

This project presents a secure coding audit of a JavaScript-based login interface. It identifies several vulnerabilities commonly found in beginner code and outlines fixes and best practices to improve the app’s security. The focus was on frontend issues like hardcoded credentials, missing input validation, weak password rules, and improper authentication handling.

---

## 🔍 Audit Highlights

### Vulnerabilities Found
- Hardcoded credentials
- No input sanitization (XSS risk)
- No rate limiting on login attempts
- Insecure HTTP access
- Weak password validation

### Fixes Implemented
- Regex-based password strength checks
- Valid username format
- Simulated secure login using fetch()
- Promoted backend authentication

