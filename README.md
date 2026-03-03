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
2. Using the Executable (.exe)Launch main.exe.To Edit: Click JSON to CSV, select your Unity JSON file. Edit the resulting CSV in the /converted folder.To Export: Click CSV to JSON, select your edited CSV, and provide the m_Name (e.g., Kaiwa_A01). The final JSON will be generated in the /reconverted folder.📦 Building the ExecutableTo bundle this project into a single standalone file with a custom icon, use PyInstaller. Run the following command in your terminal:PowerShellpython -m PyInstaller --noconsole --onefile --add-data "csv_logic.py;." --add-data "json_logic.py;." --add-data "icon.png;." --icon="icon.ico" main.py
📂 Project StructureFileDescriptionmain.pyThe primary GUI entry point, launcher logic, and process manager.csv_logic.pyLogic for extracting and cleaning m_Script data from JSON into CSV.json_logic.pyLogic for re-packaging CSV data into JSON with strict Unity quoting rules.icon.png / .icoVisual assets for the application icon and window title bar.⚠️ Technical NotesEncoding: This tool strictly uses UTF-8. If you are using Excel, always save your files as CSV UTF-8 (Comma delimited) to prevent character corruption (especially for Japanese/Kanji text).Anti-Loop Protection: The application is built using module imports instead of subprocesses. This prevents the common bug where a bundled EXE opens infinite windows when a button is clicked.Unity Compatibility: This tool is specifically designed and tested for assets extracted via UnityAssetsBundleExtractor (UABE), UABEA, or AssetStudio.📄 LicenseThis project is open-source and free to use for game development, localization, and modding purposes.
### Cara Memastikan Format Berhasil:
1. Pastikan kamu menyalin dari baris `# Unity Text Assets...` sampai paling bawah `...modding purposes.`
2. Di GitHub, klik tombol **"Edit"** pada file `README.md`.
3. Hapus semua isi yang lama, lalu **Paste** kode di atas.
4. Klik tab **"Preview"** untuk memastikan tabel, kode blok, dan judul muncul dengan benar.

Apakah ada bagian lain yang ingin ditambahkan atau diperbaiki?
