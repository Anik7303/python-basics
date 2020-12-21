from tkinter import Tk, Label, StringVar, Entry, Button, Text, END, FIRST

def show_values():
    value = float(input_txt.get())

    grams = value * 1000.0
    pounds = value * 2.20462
    ounces = value * 35.274

    # txt_gm.delete('1.0', END)
    # txt_gm.insert(END, grams)

    txt_gm.replace('1.0', END, grams)
    txt_pound.replace('1.0', END, pounds)
    txt_ounce.replace('1.0', END, ounces)

window = Tk()

label1 = Label(window, text="KG")
label1.grid(row=0, column=0)

input_txt = StringVar()
input_el = Entry(window, textvariable=input_txt)
input_el.grid(row=0, column=1)

btn_convert = Button(window, text="Convert", command=show_values)
btn_convert.grid(row=0, column=2)

txt_gm = Text(window, width=30, height=1)
txt_gm.grid(row=1, column=0)

txt_pound = Text(window, width=30, height=1)
txt_pound.grid(row=1, column=1)

txt_ounce = Text(window, width=30, height=1)
txt_ounce.grid(row=1, column=2)

window.mainloop()