# 🚨 CodeAlpha Task 4: Network Intrusion Detection System

## 🔒 Domain
Cybersecurity Internship — CodeAlpha

## 👨‍💻 Intern Details
- Name: Bereket
- Role: Web Developer Trainee @ ASTU

---

## 📝 Project Summary

This project demonstrates the setup and configuration of a Network Intrusion Detection System (NIDS) using Snort, a powerful open-source tool for real-time traffic analysis and packet logging. The goal was to detect suspicious network activity and generate alerts based on predefined rules.

---

## ⚙️ Tool Used
- IDS: Snort
- OS: Ubuntu Linux
- Interface: eth0 (example)
- Alert Mode: Console-based

---

## 📑 Steps Performed
1. Installed Snort via package manager.
2. Configured snort.conf and custom local.rules.
3. Ran Snort to monitor real-time traffic.
4. Triggered demo alerts with custom rules.
5. Captured screenshots of alert output.

---

## 🧪 Sample Rule
```snort
alert tcp any any -> any 80 (msg:"Suspicious HTTP traffic detected"; sid:1000001;)