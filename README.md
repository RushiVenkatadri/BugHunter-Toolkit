# 🛡️ BugHunter Toolkit

> A modular Python reconnaissance toolkit for bug bounty hunters and web security researchers.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-v1.0.0-success)

---

## ✨ Features

- Domain validation
- IP resolution
- HTTP/HTTPS detection
- Security header analysis
- robots.txt discovery
- sitemap.xml discovery
- Markdown report generation
- Organized workspace creation
- Installable CLI (`bughunter`)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/RushiVenkatadri/BugHunter-Toolkit.git

cd BugHunter-Toolkit
```

Create a virtual environment:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install:

```bash
pip install -e .
```

---

## 🚀 Usage

Scan a target:

```bash
bughunter scan nasa.gov
```

---

## 📂 Project Structure

```text
BugHunter-Toolkit/

src/
└── bughunter/
    ├── cli.py
    ├── engine.py
    ├── banner.py
    ├── config.py
    └── modules/
```

---

## 📄 Generated Workspace

```text
results/

example.com/

├── report.md
├── logs.txt
└── raw/
    ├── robots.txt
    └── sitemap.xml
```

---

## 🛠 Current Capabilities

- Domain validation
- DNS resolution
- Website detection
- HTTP response collection
- Security header analysis
- robots.txt collection
- sitemap.xml collection
- Markdown reporting

---

## 🗺 Roadmap

### v1.1

- security.txt support
- JSON reports
- DNS record enumeration
- SSL certificate inspection

### v1.2

- Technology detection
- HTTP method enumeration
- Better reporting

### v2.0

- Plugin system
- Third-party tool integrations
- HTML dashboard

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rushi Venkatadri**

- GitHub: https://github.com/RushiVenkatadri
- LinkedIn: https://www.linkedin.com/in/rushi-venkatadri
