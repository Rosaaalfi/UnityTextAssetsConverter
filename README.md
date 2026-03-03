# Unity Text Assets Converter (JSON ↔ CSV)

A simple GUI-based tool designed to help developers and modders convert **Unity Text Assets** (JSON format) to **CSV** and vice versa. This tool ensures that the data structure remains identical to the Unity standard, specifically handling the complex quoting required by the Unity engine.



---

## ✨ Key Features

* **Two-Way Conversion:** Seamlessly convert JSON to CSV for easy editing in Excel/Google Sheets, and re-convert back to JSON for Unity integration.
* **Unity-Standard Quoting:** Automatically wraps every column in double quotes (`QUOTE_ALL`), ensuring compatibility with Unity's internal CSV parser (as seen in `m_Script` fields).
* **Smart Directory Management:** Automatically detects if it's running as a script or an EXE to create `converted/` and `reconverted/` folders in the correct application directory.
* **Intuitive GUI:** A clean, two-button interface built with Tkinter for maximum ease of use.
* **Standalone Portability:** Optimized to be bundled into a single `.exe` file that runs without needing a Python installation on the target machine.



---

## 🚀 Getting Started

### 1. Running from Source (Python)
If you prefer running the script directly, ensure you have Python 3.10+ installed:
```bash
python main.py
```
