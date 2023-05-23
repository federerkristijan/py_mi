from tkinter import *


# python 3.11.2

root = Tk()
root.title('Menu')
root.geometry("400x400")

table_menu = Menu(root)
root.config(menu=table_menu)

# New command
def new():
    pass

# Open command
def open():
    pass

# Save command
def save():
    pass

# Cut command
def cut():
    pass

# Copy command
def copy():
    pass

# Find command
def find():
    pass

# edit command
def edit():
    pass

# File menu button
file_menu = Menu(table_menu)
table_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu button
edit_menu = Menu(table_menu)
table_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Find", command=find)
edit_menu.add_command(label="Find", command=edit)

root.mainloop()
