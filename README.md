# 🔑 Password Generator & Strength Analyzer

A robust command-line interface (CLI) password creation utility engineered in Python. It generates high-entropy, unpredictable character strings using modern cryptographic randomness.

---

## 🛠️ Features

- **Cryptographically Secure:** Leverages Python's `secrets` module instead of `random` for defense against predictability.
- **Customizable Character Pools:** Toggle lowercase letters, uppercase letters, numeric digits, and special symbols independently.
- **Entropy Evaluation Engine:** Calculates theoretical security performance based on Shannon entropy math parameters (\(L \times \log_2(R)\)).
- **Bulk Output Generation:** Quickly creates multiple unique variations in a single operation loop.

---

## 📁 Repository Structure

```text
password-generator-tool/
├── .gitignore
├── README.md
└── password generator/
    └── Password generator.py
```

---

## 🚀 Quick Start

### 1️⃣ Prerequisites
Make sure you have [Python 3.x](https://python.org) installed on your machine.

### 2️⃣ Clone & Setup
```bash
# Clone the repository
git clone https://github.com

# Navigate into the project folder
cd password-generator-tool
```

### 3️⃣ Run the Application
```bash
python "password generator/Password generator.py"
```

---

## 📝 License
This project is open-source and available under the **MIT License**.

