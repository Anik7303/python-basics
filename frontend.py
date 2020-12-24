from tkinter import Label, Entry, StringVar, Listbox, Scrollbar, Button, END

from backend import Database

class FrontEnd(object):
    def __init__(self, window):
        self.window = window
        self.selected_item = None

        self.database = Database('database.db')
        self.window.wm_title('BookStore')

        # labels
        l_title = Label(self.window, text="Title")
        l_title.grid(row=0, column=0)

        l_author = Label(self.window, text="Author")
        l_author.grid(row=0, column=5)

        l_year = Label(self.window, text="Year")
        l_year.grid(row=1, column=0)

        l_isbn = Label(self.window, text="ISBN")
        l_isbn.grid(row=1, column=5)

        # entries
        self.txt_title = StringVar()
        self.en_title = Entry(self.window, textvariable=self.txt_title)
        self.en_title.grid(row=0, column=1)
        self.en_title.focus()

        self.txt_author = StringVar()
        self.en_author = Entry(self.window, textvariable=self.txt_author)
        self.en_author.grid(row=0, column=6)

        self.txt_year = StringVar()
        self.en_year = Entry(self.window, textvariable=self.txt_year)
        self.en_year.grid(row=1, column=1)

        self.txt_isbn = StringVar()
        self.en_isbn = Entry(self.window, textvariable=self.txt_isbn)
        self.en_isbn.grid(row=1, column=6)

        # listbox
        self.lb_books = Listbox(self.window, width=40)
        self.lb_books.grid(row=2, column=0, rowspan=7, columnspan=3)

        # scrollbar for listbox
        self.scl_vlb = Scrollbar(self.window, width=10)
        self.scl_vlb.grid(row=2, column=5, rowspan=7)

        self.lb_books.configure(yscrollcommand=self.scl_vlb.set)
        self.scl_vlb.configure(command=self.lb_books.yview)

        self.lb_books.bind('<<ListboxSelect>>', self.set_selected_item)

        # buttons
        self.btn_viewall = Button(self.window, text="View all", width=12, command=self.command_view)
        self.btn_viewall.grid(row=2, column=6, columnspan=2)

        self.btn_search = Button(self.window, text="Search", width=12, command=self.command_search)
        self.btn_search.grid(row=3, column=6, columnspan=2)

        self.btn_add = Button(self.window, text="Add entry", width=12, command=self.command_add)
        self.btn_add.grid(row=4, column=6, columnspan=2)

        self.btn_update = Button(self.window, text="Update", width=12, command=self.command_update)
        self.btn_update.grid(row=5, column=6, columnspan=2)

        self.btn_delete = Button(self.window, text="Delete", width=12, command=self.command_delete)
        self.btn_delete.grid(row=6, column=6, columnspan=2)

        self.btn_close = Button(self.window, text="Close", width=12, command=self.command_close)
        self.btn_close.grid(row=7, column=6, columnspan=2)

    def update_entries(self):
        if self.selected_item is None:
            return None

        self.en_title.delete(0, END)
        self.en_title.insert(END, self.selected_item[1])

        self.en_author.delete(0, END)
        self.en_author.insert(END, self.selected_item[2])

        self.en_year.delete(0, END)
        self.en_year.insert(END, self.selected_item[3])

        self.en_isbn.delete(0, END)
        self.en_isbn.insert(END, self.selected_item[4])


    def set_selected_item(self, event):
        index = self.lb_books.curselection()
        if len(index) > 0:
            self.selected_item = self.lb_books.get(index[0])
            self.update_entries()

    def clearList(self):
        self.lb_books.delete(0, END)

    def command_view(self):
        self.clearList()
        book_list = self.database.viewall()
        for book in book_list:
            self.lb_books.insert(END, book)

    def command_search(self):
        self.clearList()
        results = self.database.search(
            self.txt_title.get(),
            self.txt_author.get(),
            self.txt_year.get(),
            self.txt_isbn.get()
        )
        for result in results:
            self.lb_books.insert(END, result)

    def command_add(self):
        self.database.insert(
            self.txt_title.get(),
            self.txt_author.get(),
            self.txt_year.get(),
            self.txt_isbn.get()
        )
        self.command_view()

    def command_update(self):
        if self.selected_item is not None:
            self.database.update(
                self.selected_item[0],
                self.txt_title.get(),
                self.txt_author.get(),
                self.txt_year.get(),
                self.txt_isbn.get()
            )
            self.command_view()

    def command_delete(self):
        self.database.delete(self.selected_item[0])
        self.command_view()

    def command_close(self):
        self.window.destroy()
