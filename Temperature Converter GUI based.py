import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            result.set("Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

tk.Label(root, text="Select Unit:").pack(pady=5)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.pack(pady=5)
combo_unit.current(0)

tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Arial', 12), justify="center").pack(pady=10)

root.mainloop()
