import json
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv
import io

def main():
    try:
        root = tk.Tk()
        root.withdraw()

        input_file = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not input_file:
            print("No file selected.")
            return

        m_name = simpledialog.askstring("Input m_Name", "Enter m_Name value:")

        if not m_name:
            messagebox.showerror("Error", "m_Name cannot be empty.")
            return

        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))

        output_dir = os.path.join(base_dir, "reconverted")
        os.makedirs(output_dir, exist_ok=True)

        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, base_name + ".json")

        formatted_lines = []
        with open(input_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                output = io.StringIO()
                writer = csv.writer(output, quoting=csv.QUOTE_ALL, lineterminator='')
                writer.writerow(row)
                formatted_lines.append(output.getvalue())

        script_content = "\r\n".join(formatted_lines) + "\r\n"

        data_to_save = {
            "m_Name": m_name,
            "m_Script": script_content
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)

        messagebox.showinfo("Success", f"JSON saved to:\n{output_file}")
        print(f"Success: JSON saved to '{output_file}'")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()