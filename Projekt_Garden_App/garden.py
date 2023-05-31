import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

root = tk.Tk()
root.geometry("700x500")
root.title("Garden Tracker")
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
style.map("Treeview", background=[("selected", "#347083")])

# # create a database or connect to one
# conn = sqlite3.connect('mein_garden.db')
# # create cursor
# c = conn.cursor()

# # create table
# c.execute("""CREATE TABLE plants (
#     name text,
#     start_date integer,
#     end_date integer,
#     days_left integer,
#     notes text
# )""")

class Table(tk.Toplevel):
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

class SubmitWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.title('Enter your data')

       # labels and entry boxes
        tk.Label(self, text='Plant name:').grid(row=0, column=0, padx=5, pady=5)
        self.p_name_entry = tk.Entry(self)
        self.p_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text='Start date:').grid(row=1, column=0, padx=5, pady=5)
        self.s_date_entry = tk.Entry(self)
        self.s_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text='End date:').grid(row=2, column=0, padx=5, pady=5)
        self.e_date_entry = tk.Entry(self)
        self.e_date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text='Days left:').grid(row=3, column=0, padx=5, pady=5)
        self.d_left_entry = tk.Entry(self)
        self.d_left_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text='Notes:').grid(row=4, column=0, padx=5, pady=5)
        self.notes_entry = tk.Entry(self)
        self.notes_entry.grid(row=4, column=1, padx=5, pady=5)

        # submit and cancel buttons
        tk.Button(self, text='Submit', command=self.submit).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self, text='Cancel', command=self.destroy).grid(row=5, column=1, padx=5, pady=5)

    def submit(self):
        # get the values from the entry boxes
        p_name = self.p_name_entry.get()
        s_date = self.s_date_entry.get()
        e_date = self.e_date_entry.get()
        d_left = self.d_left_entry.get()
        notes = self.notes_entry.get()

        # create a database or connect to one
        conn = sqlite3.connect('mein_garden.db')
        # create cursor
        c = conn.cursor()

        # insert into table via python dict
        c.execute("INSERT INTO plants VALUES (:p_name, :s_date, :e_date, :d_left, :notes)",
                {
                    'p_name': p_name,
                    's_date': s_date,
                    'e_date': e_date,
                    'd_left': d_left,
                    'notes': notes
                })

        # clear the text boxes
        self.p_name_entry.delete(0, END)
        self.s_date_entry.delete(0, END)
        self.e_date_entry.delete(0, END)
        self.d_left_entry.delete(0, END)
        self.notes_entry.delete(0, END)

        # commit changes
        conn.commit()
        # close connection
        conn.close()

        # destroy the window
        self.destroy()

table = Table(root, headings=("plant", "start", "end", "days left", "notes"), rows=data)
# table.pack(expand=tk.YES, fill=tk.BOTH, side=LEFT)
root.mainloop()
