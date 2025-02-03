import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height<= 0:
            messagebox.showerror("Hata,Lütfen pozitif sayılar giriniz.")
            return
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Zayıf"
        elif 18.5 <= bmi < 24.9:
            category = "Normal kilolu"
        elif 25<= bmi <29.9:
            category = "Fazla kilolu"
        else:
            category = "Obez"

        result_label.config(text= f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Hata, Lütfen sadece sayı giriniz.")


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

tk.Label(window, text="Kilo (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Boy (m):").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()


