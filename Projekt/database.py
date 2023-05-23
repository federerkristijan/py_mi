from tkinter import *
# from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('My first Python sqlite3 Database')
root.geometry('400x550')

# def connect():
#     # create a database or connect to one
#     conn = sqlite3.connect('mein_garden.db')
#     # create cursor
#     c = conn.cursor()

# create a database or connect to one
conn = sqlite3.connect('mein_garden.db')
# create cursor
c = conn.cursor()

# create table
# c.execute("""CREATE TABLE plants (
#     name text,
#     start_date integer,
#     end_date integer,
#     days_left integer,
#     notes text
# )""")

# def new_file():
#     c.execute("""CREATE TABLE plants (
#      name text,
#      start_date integer,
#      end_date integer,
#      days_left integer,
#      notes text)""")
#     file_new_frame.pack(fill="both", expand=1)

def submit():
    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()

    # insert into table via python dict
    c.execute("INSERT INTO plants VALUES (:p_name, :s_date, :e_date, :d_left, :notes)",
              {
                  'p_name': p_name.get(),
                  's_date': s_date.get(),
                  'e_date': e_date.get(),
                  'd_left': d_left.get(),
                  'notes': notes.get()
              })

    # clear the text boxes
    p_name.delete(0, END)
    s_date.delete(0, END)
    e_date.delete(0, END)
    d_left.delete(0, END)
    notes.delete(0, END)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

def query(): # open/show

    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()

    # query the database
    # oid - objectID unique parameter key
    c.execute('SELECT *, oid FROM plants')
    # fetches all the records
    # fetchone (1st one), also fetchmany(n) (fetches n records)
    records = c.fetchall()

    # loop through results
    print_records = ''
    for record in records:
        print_records += str(record[5]) + '. ' + str(record[0]) + 's: ' + str(record[3]) + ' days left' + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

def delete():
    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from plants WHERE oid= " + delete_box.get())

def save():
    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()

    # delete_box == 'Select ID'
    record_id = delete_box.get()

    c.execute("""UPDATE plants SET
            name = :name,
            start_date = :start,
            end_date = :end,
            days_left = :left,
            notes = :notes

            WHERE oid = :oid""",
            {
                'name': p_name_editor.get(),
                'start': s_date_editor.get(),
                'end': e_date_editor.get(),
                'left': d_left_editor.get(),
                'notes': notes_editor.get(),
                'oid': record_id
            })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    editor.destroy()

def edit():
    global editor

    editor = Tk()
    editor.title('Editor')
    editor.geometry('400x280')

    # create a database or connect to one
    conn = sqlite3.connect('mein_garden.db')
    # create cursor
    c = conn.cursor()

    # selecting the id from delete_box aka select ID
    record_id = delete_box.get()
    # query the database
    c.execute('SELECT * FROM plants WHERE oid = ' + record_id)
    # fetches all the records
    records = c.fetchall()

    # global vars
    global p_name_editor
    global s_date_editor
    global e_date_editor
    global d_left_editor
    global notes_editor

    # text boxes
    p_name_editor = Entry(editor, width=30)
    p_name_editor.grid(row=0, column=1, padx=(0, 30), pady=(10, 5))
    s_date_editor = Entry(editor, width=30)
    s_date_editor.grid(row=1, column=1, padx=(0, 30), pady=(5, 5))
    e_date_editor = Entry(editor, width=30)
    e_date_editor.grid(row=2, column=1, padx=(0, 30), pady=(5, 5))
    d_left_editor = Entry(editor, width=30)
    d_left_editor.grid(row=3, column=1, padx=(0, 30), pady=(5, 5))
    notes_editor = Entry(editor, width=30)
    notes_editor.grid(row=4, column=1, padx=(0, 30), pady=(5, 5))

    # text box labels
    p_name_label = Label(editor, text="Plant Name")
    p_name_label.grid(row=0, column=0, pady=(10, 0))
    s_date_label = Label(editor, text="Start Date")
    s_date_label.grid(row=1, column=0)
    e_date_label = Label(editor, text="End Date")
    e_date_label.grid(row=2, column=0)
    d_left_label = Label(editor, text="Days left")
    d_left_label.grid(row=3, column=0)
    notes_label = Label(editor, text="Notes")
    notes_label.grid(row=4, column=0)

    # loop through results
    for record in records:
        p_name_editor.insert(0, record[0])
        s_date_editor.insert(0, record[1])
        e_date_editor.insert(0, record[2])
        d_left_editor.insert(0, record[3])
        notes_editor.insert(0, record[4])

    # create an update button
    save_btn = Button(editor, text="Save changes", command=save)
    save_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=99)
    save_file_frame.pack(fill="x")

# text boxes
p_name = Entry(root, width=30)
p_name.grid(row=0, column=1, padx=(0, 30), pady=(10, 5))
s_date = Entry(root, width=30)
s_date.grid(row=1, column=1, padx=(0, 30), pady=(5, 5))
e_date = Entry(root, width=30)
e_date.grid(row=2, column=1, padx=(0, 30), pady=(5, 5))
d_left = Entry(root, width=30)
d_left.grid(row=3, column=1, padx=(0, 30), pady=(5, 5))
notes = Entry(root, width=30)
notes.grid(row=4, column=1, padx=(0, 30), pady=(5, 5))
# Select ID
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, padx=(0, 30), pady=(5, 5))

# text box labels
p_name_label = Label(root, text="Plant Name")
p_name_label.grid(row=0, column=0, pady=(10, 0))
s_date_label = Label(root, text="Start Date")
s_date_label.grid(row=1, column=0)
e_date_label = Label(root, text="End Date")
e_date_label.grid(row=2, column=0)
d_left_label = Label(root, text="Days left")
d_left_label.grid(row=3, column=0)
notes_label = Label(root, text="Notes")
notes_label.grid(row=4, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=8, column=0, padx=(10, 10), pady=5)

# create submit button
submit_btn = Button(root, text="Add record to the database", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

# query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# delete button
delete_btn = Button(root, text="Delete a record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# update button & editor window
edit_btn = Button(root, text="Edit a record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Frames
# file_new_frame = Frame(root, width=300, height=300)
save_file_frame = Frame(root, width=300, height=300)

root.mainloop()
