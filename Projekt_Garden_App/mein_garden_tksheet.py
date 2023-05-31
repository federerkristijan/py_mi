# https://pypi.org/project/tksheet/

from tksheet import Sheet
# import tkinter as tk
from tkinter import *
from database import *
from tkinter import filedialog

# python 3.11.2


# defining table
#table_menu = Menu()

# create a database or connect to one
conn = sqlite3.connect('mein_garden.db')
# create cursor
c = conn.cursor()

with sqlite3.connect('mein_garden.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM plants")

class table(Tk):

    def __init__(self):
        Tk.__init__(self)
        # configuring columns and rows
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        # config table
        #self.config(menu=table_menu)
        # filedialog
        # self.filename = filedialog.askopenfile()

        self.sheet_table = Sheet(
            self,
            data= [(row for row in cursor.fetchall())],
            height=500,
            width=800)
        self.sheet_table.enable_bindings((
            "single_select",
            "drag_select",
            "column_drag_and_drop",
            "column_select",
            "row_select",
            "column_width_resize",
            "double_click_column_resize",
            "rc_insert_column",
            "rc_delete_column",
            "rc_insert_row",
            "rc_delete_row",
            "row_width_resize",
            "copy",
            "cut",
            "paste",
            "delete",
            "undo",
            "edit_cell"
        ))
        self.sheet_table.grid(row=0, column=0, sticky="nswe")
        # self.sheet_table.highlight_cells(row= 5, column= 5, bg= "#ed4337", fg="white")
        # self.sheet_table.highlight_cells(row= 5, column= 1, bg= "#ed4337", fg="white")
        # self.sheet_table.highlight_cells(row= 5, bg= "#ed4337", fg="white", canvas = "row_index")
        # self.sheet_table.highlight_cells(column= 0, bg= "#ed4337", fg="white", canvas= "header")
        list = ["plant", "start", "end", "days left", "notes"]
        self.sheet_table.headers((f" {c}" for c in list))
        # with sqlite3.connect('mein_garden.db') as connection:
        #     cursor = connection.cursor()
        #     cursor.execute("SELECT * FROM plants")
        #     self.data = (row for row in cursor.fetchall())

        """
        # # File menu button
        file_menu = Menu(table_menu)
        table_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=new_file) # -> neue Tabelle erstellen
        file_menu.add_command(label="Open", command=open)
        file_menu.add_command(label="Save", command=save)
        file_menu.add_command(label="Exit", command=self.destroy)

        # Edit menu button
        edit_menu = Menu(table_menu)
        table_menu.add_cascade(label="Edit", menu=edit_menu)
        # edit_menu.add_command(label="Cut", command=cut)
        # edit_menu.add_command(label="Copy", command=copy)
        # edit_menu.add_command(label="Find", command=find)
        edit_menu.add_command(label="Edit", command=edit)
        """

app = table()
app.title('Mein garden')
app.mainloop()
