from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
import convertBase

root = Tk()
root.geometry(f"{600}x{350}")
root.title("Numerical Base Converter")

def calculate():
    global calculation
    converted = convertBase.convert(number.get(), baseTo.get(), baseFrom.get())
    try:calculation.pack_forget()
    except Exception:pass
    calculation = Label(root, text = converted, bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
    calculation.pack(anchor = "center", fill = X)
    

bases = [str(i) for i in range(1, 67)]
ttk.Style().configure("style1.TCombobox", foreground="blue", background="black")

baseTo = StringVar()
number = StringVar()
baseFrom = StringVar()

frame1 = Frame(root)
frame1.pack(anchor = "center", pady = 10)
Label(frame1, text = "Enter number: ").pack(side = LEFT)
Entry(frame1, width = 30, font = "ms-sans 20", insertbackground = "white", bg = "black", fg = "yellow", textvariable = number).pack(side = RIGHT)

frame2 = Frame(root)
frame2.pack(anchor = "center", pady = 10)
Label(frame2, text = "Base From:").pack(side = LEFT)
baseFrom = ttk.Combobox(frame2,  width = 40, height = 20, textvariable = baseFrom, values = bases, style = "style1.TCombobox", font = "ms-sans 15")
baseFrom.pack(side = RIGHT)

frame3 = Frame(root)
frame3.pack(anchor = "center", pady = 10)
Label(frame3, text = "Base To:     ").pack(side = LEFT)
baseTo = ttk.Combobox(frame3,  width = 40, height = 20, textvariable = baseTo, values = bases, style = "style1.TCombobox", font = "ms-sans 15")
baseTo.pack(side = RIGHT)

CalculateButton = Button(root, text = "calculate", bg = "black", fg = "yellow", font = "ms-sans 30", command = calculate)
CalculateButton.pack(fill = X, anchor = "center")

calculation = Label(root, text = "calculated", bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
calculation.pack(anchor = "center", fill = X)

root.mainloop()
