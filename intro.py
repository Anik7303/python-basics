from tkinter import Tk, Button, Entry, Text, StringVar, END

window = Tk()

def show_text():
    text = tx_el.get()
    if text != '':
        try:
            miles = float(text) * 1.667
            txt1.insert(END, miles)
        except FloatingPointError:
            print('FloatingPointError occured')
        except ValueError:
            print('ValueError occured')
        except:
            print('Error occured')

btn1 = Button(window, text="Execute", command=show_text)
#btn1.pack()
btn1.grid(row=0, column=0)

tx_el = StringVar()
in_el = Entry(window, textvariable=tx_el)
in_el.grid(row=0, column=1)

txt1 = Text(window, height=1, width=50)
txt1.grid(row=1, column=0, columnspan=2)

window.mainloop()