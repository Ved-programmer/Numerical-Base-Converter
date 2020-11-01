from tkinter import Tk, Label, Frame, X, StringVar, LEFT, Entry, RIGHT, Button
from tkinter import ttk
import convertBase

root = Tk()
root.maxsize(610, 355)
root.minsize(590, 345)
root.geometry(f"{600}x{350}")
root.title("Numerical Base Converter")


bases = [str(i) for i in range(1, 65)]
ttk.Style().configure("style1.TCombobox", foreground="blue", background="black")

def createDropBox(textVariable, textToDisplay):
    frame2 = Frame(root)
    frame2.pack(anchor = "center", pady = 10)
    Label(frame2, text = textToDisplay).pack(side = LEFT)
    baseFrom = ttk.Combobox(frame2,  width = 40, height = 20, textvariable = textVariable, values = bases, style = "style1.TCombobox", font = "ms-sans 15")
    baseFrom.pack(side = RIGHT)
        

def calculate():
    global calculation
    converted = convertBase.convert(number.get(), baseFrom.get(), baseTo.get())
    try:calculation.pack_forget()
    except Exception:pass
    calculation = Label(root, text = converted, bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
    calculation.pack(anchor = "center", fill = X)
    

baseFrom = StringVar();baseTo = StringVar();number = StringVar()

frame1 = Frame(root)
frame1.pack(anchor = "center", pady = 10)
Label(frame1, text = "Enter number: ").pack(side = LEFT)
Entry(frame1, width = 30, font = "ms-sans 20", insertbackground = "white", bg = "black", fg = "yellow", textvariable = number).pack(side = RIGHT)

createDropBox(baseFrom, "Base From:")
createDropBox(baseTo, "Base To:     ")


CalculateButton = Button(root, text = "calculate", bg = "black", fg = "yellow", font = "ms-sans 30", command = calculate)
CalculateButton.pack(fill = X, anchor = "center")

calculation = Label(root, text = "calculated", bg = "dark blue", fg = "white", pady = 57, font = "ms-sans 20")
calculation.pack(anchor = "center", fill = X)


root.mainloop()
