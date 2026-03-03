import tkinter as tk
from tkinter import messagebox
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def on_closing(root):
    root.destroy()
    sys.exit(0)

def run_conversion(mode):
    try:
        if mode == "to_csv":
            import csv_logic
            csv_logic.main() 
        elif mode == "to_json":
            import json_logic
            json_logic.main()
        
        messagebox.showinfo("Success", "Conversion Task Completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def main():
    root = tk.Tk()
    root.title("Unity CSV-JSON Converter")
    root.geometry("400x250")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    try:
        img_path = resource_path("icon.png")
        icon_img = tk.PhotoImage(file=img_path)
        root.iconphoto(True, icon_img)
    except:
        pass

    tk.Label(root, text="Select Conversion Mode", font=("Arial", 14, "bold"), pady=20).pack()

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    tk.Button(
        button_frame, text="JSON to CSV", width=20, height=3, 
        bg="#4CAF50", fg="white",
        command=lambda: run_conversion("to_csv")
    ).grid(row=0, column=0, padx=10, pady=10)

    tk.Button(
        button_frame, text="CSV to JSON", width=20, height=3, 
        bg="#2196F3", fg="white",
        command=lambda: run_conversion("to_json")
    ).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Version 1.0.0", font=("Arial", 8), fg="gray").pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()