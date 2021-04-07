from tkinter import *
from tkinter.ttk import *

# Root
root = Tk()
root.title("Praktikum DPBO Python")

# Left part of windows
left_pane = PanedWindow(root)
left_pane.pack(fill=BOTH, expand=1)

# Form Pane
form_pane = PanedWindow(left_pane)

# Input 1 field
a = Label(form_pane ,text = "Input 1").grid(row = 0,column = 0)
a1 = Entry(form_pane).grid(row = 0,column = 1)

# Input 2 field
b = Label(form_pane ,text = "Input 2").grid(row = 1,column = 0)
b1 = Entry(form_pane).grid(row = 1,column = 1)

# Dropdown field
c = Label(form_pane ,text = "Dropdown").grid(row = 2,column = 0)
dropdown_set = (1, 2, 3, 4, 5)
dropdown_selected = StringVar(root)
dropdown_selected.set(dropdown_set[0])
dropdown = Combobox(form_pane, textvariable=dropdown_selected, values=dropdown_set).grid(row = 2, column = 1)

# Checkbox field
d = Label(form_pane ,text = "Checkbox Field").grid(row = 3, column = 0)
d0 = Checkbutton(form_pane, text = "1").grid(row = 3, column = 1)
d1 = Checkbutton(form_pane, text = "2").grid(row = 3, column = 2)
d2 = Checkbutton(form_pane, text = "3").grid(row = 3, column = 3)

# Radio Button field
e = Label(form_pane ,text = "Radio Button Field").grid(row = 4, column = 0)
radio_selected = StringVar(root)
e0 = Radiobutton(form_pane, text="1", variable=radio_selected, value=1).grid(row = 4, column = 1)
e1 = Radiobutton(form_pane, text="2", variable=radio_selected, value=2).grid(row = 4, column = 2)
e2 = Radiobutton(form_pane, text="3", variable=radio_selected, value=3).grid(row = 4, column = 3)

# Add form pane to left pane
left_pane.add(form_pane)

right_pane = PanedWindow(left_pane)
left_pane.add(right_pane)

top = Label(right_pane, text="top pane")
right_pane.add(top)

mainloop()