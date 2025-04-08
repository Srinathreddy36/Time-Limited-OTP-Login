# Garuda Sentinel – Time-Limited OTP Login System 🔐🛡️

A secure OTP-based authentication system designed as part of the **Garuda Sentinel** initiative – blending modern cybersecurity with inspiration from Indian mythology to protect society and individuals from digital threats.

## 🚀 Overview

This project demonstrates a secure one-time password (OTP) verification system in Python. It uses hashing with salt, a time limit for OTP expiration, and limits user attempts to ensure robust protection.

## 🧠 Features

- ✅ OTP generated with secure randomness (`secrets` module)
- 🧂 Salted and hashed using `SHA3-256`
- ⏳ OTP expires after 30 seconds
- 🔁 Max 3 attempts allowed
- 🗂️ Hashes and metadata stored securely in local file

## 🛠️ Tech Stack

- Python 3
- `hashlib` – Hashing (SHA3-256)
- `secrets` – Secure random number generator
- `time` – For OTP expiry
- Local File Storage

## 🧪 How It Works

1. User enters a strong password (min 12 characters).
2. An OTP is generated using `secrets` and shown to user.
3. OTP is hashed with a salt and stored with timestamp.
4. User has 30 seconds and 3 tries to enter the correct OTP.
5. System validates the entered OTP hash against stored hash.
6. Access is granted if correct and within limits.

## 🔐 Why It Matters

This simulation mimics real-world secure authentication systems (e.g., UPI, banking logins) and showcases how even simple OTP systems must be handled securely to prevent spoofing and scams.

## 📚 What You Learn

- Hashing with Salt
- OTP generation and validation
- Time-based security mechanisms
- Secure coding practices in Python
- File I/O for basic data storage

## 🛡️ Part of Garuda Sentinel Mission

> "Inspired by **Garuda**, the divine protector – this project guards digital gates and strengthens cybersecurity awareness."

---

## ✅ Status

🚧 Active Development | 🔒 Secure | 🎯 Portfolio-Ready

## 📌 Next Up

- Add Biometric/Backup Code authentication
- Store data in encrypted file or database
- Build GUI with PyQt or Tkinter

---

## 📎 Author

**Srinath Reddy**  
Garuda Sentinel | Cybersecurity Student & Enthusiast  
GitHub: [@Srinathreddy36](https://github.com/Srinathreddy36)



