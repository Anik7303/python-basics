from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar, Button, END

import backend

selected_item = None

def update_entries():
    if selected_item is None:
        return None

    en_title.delete(0, END)
    en_title.insert(END, selected_item[1])
    en_author.delete(0, END)
    en_author.insert(END, selected_item[2])
    en_year.delete(0, END)
    en_year.insert(END, selected_item[3])
    en_isbn.delete(0, END)
    en_isbn.insert(END, selected_item[4])

def set_selected_item(event):
    index = lb_books.curselection()
    global selected_item
    if len(index) > 0:
        selected_item = lb_books.get(index[0])
        update_entries()

def clearList():
    lb_books.delete(0, END)

def command_view():
    clearList()
    book_list = backend.viewall()
    for book in book_list:
        lb_books.insert(END, book)

def command_search():
    clearList()
    results = backend.search(txt_title.get(), txt_author.get(), txt_year.get(), txt_isbn.get())
    for result in results:
        lb_books.insert(END, result)

def command_add():
    backend.insert(txt_title.get(), txt_author.get(), txt_year.get(), txt_isbn.get())
    command_view()

def command_update():
    if selected_item is not None:
        backend.update(
            selected_item[0],
            txt_title.get(),
            txt_author.get(),
            txt_year.get(),
            txt_isbn.get()
        )
        command_view()

def command_delete():
    backend.delete(selected_item[0])
    command_view()

def command_close():
    window.destroy()

window = Tk()
window.wm_title('BookStore')

# labels
l_title = Label(window, text="Title")
l_title.grid(row=0, column=0)

l_author = Label(window, text="Author")
l_author.grid(row=0, column=5)

l_year = Label(window, text="Year")
l_year.grid(row=1, column=0)

l_isbn = Label(window, text="ISBN")
l_isbn.grid(row=1, column=5)

# entries
txt_title = StringVar()
en_title = Entry(window, textvariable=txt_title)
en_title.grid(row=0, column=1)
en_title.focus()

txt_author = StringVar()
en_author = Entry(window, textvariable=txt_author)
en_author.grid(row=0, column=6)

txt_year = StringVar()
en_year = Entry(window, textvariable=txt_year)
en_year.grid(row=1, column=1)

txt_isbn = StringVar()
en_isbn = Entry(window, textvariable=txt_isbn)
en_isbn.grid(row=1, column=6)

# listbox
lb_books = Listbox(window, width=40)
lb_books.grid(row=2, column=0, rowspan=7, columnspan=3)

# scrollbar for listbox
scl_vlb = Scrollbar(window, width=10)
scl_vlb.grid(row=2, column=5, rowspan=7)

lb_books.configure(yscrollcommand=scl_vlb.set)
scl_vlb.configure(command=lb_books.yview)

lb_books.bind('<<ListboxSelect>>', set_selected_item)

# buttons
btn_viewall = Button(window, text="View all", width=12, command=command_view)
btn_viewall.grid(row=2, column=6, columnspan=2)

btn_search = Button(window, text="Search", width=12, command=command_search)
btn_search.grid(row=3, column=6, columnspan=2)

btn_add = Button(window, text="Add entry", width=12, command=command_add)
btn_add.grid(row=4, column=6, columnspan=2)

btn_update = Button(window, text="Update", width=12, command=command_update)
btn_update.grid(row=5, column=6, columnspan=2)

btn_delete = Button(window, text="Delete", width=12, command=command_delete)
btn_delete.grid(row=6, column=6, columnspan=2)

btn_close = Button(window, text="Close", width=12, command=command_close)
btn_close.grid(row=7, column=6, columnspan=2)

window.mainloop()

if __name__ == "__main__":
    backend.create_table()
