import json
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    try:
        root = tk.Tk()
        root.withdraw()

        input_file = filedialog.askopenfilename(
            title="Select JSON File",
            filetypes=[("JSON Files", "*.json")]
        )

        if not input_file:
            print("No file selected.")
            return

        if getattr(sys, 'frozen', False):

            program_dir = os.path.dirname(sys.executable)
        else:

            program_dir = os.path.dirname(os.path.abspath(__file__))

        output_dir = os.path.join(program_dir, "converted")
        os.makedirs(output_dir, exist_ok=True)

        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, base_name + ".csv")

        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        csv_content = data.get("m_Script")
        if csv_content is None:
            messagebox.showerror("Error", "'m_Script' not found in JSON.")
            return

        with open(output_file, "w", encoding="utf-8", newline="") as f:
            f.write(csv_content)

        messagebox.showinfo("Success", f"CSV saved to:\n{output_file}")
        print(f"Success: CSV saved to '{output_file}'")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()