from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
from games import *

games_list = []

# Root
root = Tk()
root.title("Praktikum DPBO Python")

# Left part of windows
left_pane = PanedWindow(root)
left_pane.pack(fill=BOTH, expand=1)

# Form Pane
form_pane = PanedWindow(left_pane)

# Input 1 field
lbl_nama = Label(form_pane ,text = "Nama Game").grid(row = 0,column = 0)
input_nama = Entry(form_pane)
input_nama.grid(row = 0,column = 1)

# Input 2 field
lbl_dev = Label(form_pane ,text = "Nama Developer").grid(row = 1,column = 0)
input_dev = Entry(form_pane)
input_dev.grid(row = 1,column = 1)

# Dropdown field
lbl_thn_rilis = Label(form_pane ,text = "Tahun Rilis").grid(row = 2,column = 0)
list_thn_rilis = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]
selected_thn_rilis = StringVar(root)
selected_thn_rilis.set(list_thn_rilis[0])
input_thn_rilis = Combobox(form_pane, textvariable=selected_thn_rilis, values=list_thn_rilis)
input_thn_rilis.grid(row = 2, column = 1)

# Checkbox field
lbl_platform = Label(form_pane ,text = "Platform").grid(row = 3, column = 0)
v = [StringVar(root), StringVar(root), StringVar(root), StringVar(root)]
input_platform_0 = Checkbutton(form_pane, text = "Microsoft Windows", variable=v[0], onvalue="Microsoft Windows")
input_platform_0.grid(row = 3, column = 1)
input_platform_1 = Checkbutton(form_pane, text = "PlayStation 5", variable=v[1], onvalue="PlayStation 5")
input_platform_1.grid(row = 3, column = 2)
input_platform_2 = Checkbutton(form_pane, text = "Xbox Series X", variable=v[2], onvalue="Xbox Series X")
input_platform_2.grid(row = 3, column = 3)
input_platform_3 = Checkbutton(form_pane, text = "Nintendo Switch", variable=v[3], onvalue="Nintendo Switch")
input_platform_3.grid(row = 3, column = 4)

# Radio button field
lbl_mode = Label(form_pane ,text = "Mode").grid(row = 4, column = 0)
selected_mode = StringVar(root)
input_mode_0 = Radiobutton(form_pane, text="Single-player", variable=selected_mode, value="Single-player")
input_mode_0.grid(row = 4, column = 1)
input_mode_1 = Radiobutton(form_pane, text="Multi-player", variable=selected_mode, value="Multi-player")
input_mode_1.grid(row = 4, column = 2)

# Upload image field
# Open file dialog and get the filename
def upload_image():
    image_filename = filedialog.askopenfilename(title ='Open')
    img = Image.open(image_filename)
    # resize the image and apply a high-quality down sampling filter
    # img = img.resize((250, 250), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
   
    # create a label
    panel = Label(form_pane, image = img, text="IMAGEEEE")
    panel.grid(row = 9, column=0)

btn_image = Button(form_pane, text="Upload Image", command=upload_image)
btn_image.grid(row=5, column=0)

# Action when submit button is pressed
def submit():
    selected_platform = []
    for i in v:
        if i.get() != '0' and i.get() != '':
            selected_platform.append(i.get())
    game = Games(input_nama.get(), input_dev.get(), input_thn_rilis.get(), selected_platform, selected_mode.get())
    games_list.append(game)

# Displaying games list
def show_games():
    index = 0
    for i in games_list:
        print("=================Games " + str(index + 1) + " =========")
        print(i.get_nama())
        print(i.get_nama_dev())
        print(i.get_thn_rilis())
        print(i.get_platform())
        print(i.get_mode())
        index += 1

# Displaying games list
def delete_games():
    games_list.clear()

# Submit button
btn_submit = Button(form_pane, text="Submit", command=submit)
btn_submit.grid(row=6, column=0)

# Display games list button
btn_display = Button(form_pane, text="See All Games", command=show_games)
btn_display.grid(row=7, column=0)

# Delete button
btn_delete = Button(form_pane, text="Delete All Games", command=delete_games)
btn_delete.grid(row=8, column=0)

# Add form pane to left pane
left_pane.add(form_pane)

right_pane = PanedWindow(left_pane)
left_pane.add(right_pane)

top = Label(right_pane, text="top pane")
right_pane.add(top)

mainloop()