# 🔐 Secure Coding Review Report – CodeAlpha Task 3

## 🎯 Project Name
CodeAlpha_SecureCodingReview

---

## 👤 Intern Information
- Name: Bereket
- Role: Web Developer Trainee @ ASTU
- Domain: Cybersecurity Internship (CodeAlpha)

---

## 📝 Overview

This report summarizes the secure coding audit performed on a simple JavaScript-based login application. The purpose was to identify potential security flaws, evaluate their impact, and suggest remediation strategies to improve code hygiene and protect users against attacks such as XSS, brute force, and credential leaks.

---

## 📂 Scope of Audit

- Frontend Technology: HTML, CSS, JavaScript
- Focus Areas: Authentication logic, input handling, rate limiting, password policies, HTTPS enforcement

---

## ⚠️ Vulnerabilities & Recommended Fixes

| No. | Vulnerability               | Risk                          | Recommendation                             |
|-----|-----------------------------|-------------------------------|--------------------------------------------|
| 1   | Hardcoded credentials       | Credential leaks              | Move auth logic to server; hash passwords  |
| 2   | No input sanitization       | XSS injection                 | Use DOMPurify or escape HTML input       |
| 3   | No rate limiting            | Brute-force login attempts    | Add cooldown or lockout after N failures   |
| 4   | Insecure HTTP access        | Man-in-the-middle attacks     | Enforce HTTPS and add HSTS headers         |
| 5   | Weak password validation    | Vulnerable to poor passwords  | Require strong regex-based password check  |

---

## 🧪 Code Review Highlight

Before (Vulnerable Code):
```js
if (username === "admin" && password === "1234") {
  alert("Login successful!");
}