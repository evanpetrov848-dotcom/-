import tkinter as tk
from tkinter import messagebox

# وظيفة الزر عند الضغط عليه
def calculate():
    try:
        amount = float(entry.get())
        result = amount * 550  # السعر
        messagebox.showinfo("النتيجة", f"المبلغ بالعملة المحلية: {result} SDG")
    except:
        messagebox.showerror("خطأ", "الرجاء إدخال رقم صحيح")

# إنشاء النافذة
root = tk.Tk()
root.title("USDT Exchange")
root.geometry("300x200")

# إضافة نص وصندوق إدخال وزر
tk.Label(root, text="أدخل كمية USDT:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="احسب السعر", command=calculate)
btn.pack(pady=20)

root.mainloop()
