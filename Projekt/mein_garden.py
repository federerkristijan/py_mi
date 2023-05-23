import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from database import *


root = tk.Tk()
root.geometry("700x500")
root.title("Garden Tracker")
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
style.map("Treeview", background=[("selected", "#347083")])

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set, selectmode="extended")
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.tag_configure("oddrow", background="white")
        table.tag_configure("evenrow", background="lightblue")
        table.pack(expand=tk.YES, fill=tk.BOTH)

data = [[]]
with sqlite3.connect('mein_garden.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plants")
    data = (row for row in cursor.fetchall())


table = Table(root, headings=("plant", "start", "end", "days left", "notes"), rows=data)
table.pack(expand=tk.YES, fill=tk.BOTH, side=LEFT)
root.mainloop()
