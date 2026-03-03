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



---

### 2. Using the Executable (.exe)
1. Launch `main.exe`.
2. **To Edit:** Click **JSON to CSV**, select your Unity JSON file. Edit the resulting CSV in the `/converted` folder.
3. **To Export:** Click **CSV to JSON**, select your edited CSV, and provide the `m_Name` (e.g., Kaiwa_A01). The final JSON will be generated in the `/reconverted` folder.

### 📦 Building the Executable
To bundle this project into a single standalone file with a custom icon, use **PyInstaller**. Run the following command in your terminal:
```bash
python -m PyInstaller --noconsole --onefile --add-data "csv_logic.py;." --add-data "json_logic.py;." --add-data "icon.png;." --icon="icon.ico" main.py
```



---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **`main.py`** | The primary GUI entry point, launcher logic, and process manager. |
| **`csv_logic.py`** | Logic for extracting and cleaning `m_Script` data from JSON into CSV. |
| **`json_logic.py`** | Logic for re-packaging CSV data into JSON with strict Unity quoting rules. |
| **`icon.png` / `.ico`** | Visual assets for the application icon and window title bar. |



---

## ⚠️ Technical Notes

* **Encoding:** This tool strictly uses **UTF-8**. If you are using Excel, always save your files as **CSV UTF-8 (Comma delimited)** to prevent character corruption, especially for Japanese/Kanji text.
* **Anti-Loop Protection:** The application is built using module imports instead of subprocesses. This prevents the common bug where a bundled EXE opens infinite windows when a button is clicked.
* **Unity Compatibility:** This tool is specifically designed and tested for assets extracted via *UnityAssetsBundleExtractor (UABE)*, *UABEA*, or *AssetStudio*.



---

## 📄 License

This project is open-source and free to use for game development, localization, and modding purposes.
