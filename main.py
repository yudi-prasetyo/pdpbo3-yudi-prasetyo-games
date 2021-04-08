from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from PIL import Image
from PIL.ImageTk import PhotoImage
from games import *

games_list = []

# Root
root = Tk()
root.title("Praktikum DPBO Python")

# Left part of windows
left_frame = LabelFrame(root, padx=10, pady=10)
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Form Pane
form_frame = Frame(left_frame, padx=10, pady=10)
form_frame.pack(padx=10, pady=10)

# Input 1 field
lbl_nama = Label(form_frame ,text = "Nama Game").grid(row = 0,column = 0, sticky=W)
input_nama = Entry(form_frame)
input_nama.grid(row = 0,column = 1, padx=10, pady=10, sticky=W)

# Input 2 field
lbl_dev = Label(form_frame ,text = "Nama Developer").grid(row = 1,column = 0, sticky=W)
input_dev = Entry(form_frame)
input_dev.grid(row = 1,column = 1, padx=10, pady=10, sticky=W)

# Dropdown field
lbl_thn_rilis = Label(form_frame ,text = "Tahun Rilis").grid(row = 2,column = 0, sticky=W)
list_thn_rilis = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011]
selected_thn_rilis = StringVar(root)
selected_thn_rilis.set(list_thn_rilis[0])
input_thn_rilis = Combobox(form_frame, textvariable=selected_thn_rilis, values=list_thn_rilis)
input_thn_rilis.grid(row = 2, column = 1, padx=10, pady=10, sticky=W)

# Checkbox field
lbl_platform = Label(form_frame ,text = "Platform").grid(row = 3, column = 0, sticky=W)
v = [StringVar(root), StringVar(root), StringVar(root), StringVar(root)]
checkbox_frame = Frame(form_frame)
checkbox_frame.grid(padx=10, pady=10, row=3, column=1, sticky=W)
input_platform_0 = Checkbutton(checkbox_frame, text = "Microsoft Windows", variable=v[0], onvalue="Microsoft Windows")
input_platform_0.grid(row = 0, column = 0)
input_platform_1 = Checkbutton(checkbox_frame, text = "PlayStation 5", variable=v[1], onvalue="PlayStation 5")
input_platform_1.grid(row = 0, column = 1)
input_platform_2 = Checkbutton(checkbox_frame, text = "Xbox Series X", variable=v[2], onvalue="Xbox Series X")
input_platform_2.grid(row = 0, column = 2)
input_platform_3 = Checkbutton(checkbox_frame, text = "Nintendo Switch", variable=v[3], onvalue="Nintendo Switch")
input_platform_3.grid(row = 0, column = 3)

# Radio button field
lbl_mode = Label(form_frame ,text = "Mode").grid(row = 4, column = 0, sticky=W)
selected_mode = StringVar(root)
radio_frame = Frame(form_frame)
radio_frame.grid(padx=10, pady=10, row=4, column=1, sticky=W)
input_mode_0 = Radiobutton(radio_frame, text="Single-player", variable=selected_mode, value="Single-player")
input_mode_0.grid(row = 0, column = 0)
input_mode_1 = Radiobutton(radio_frame, text="Multi-player", variable=selected_mode, value="Multi-player")
input_mode_1.grid(row = 0, column = 1)

# Upload image field
# Open file dialog and get the filename

def upload_image():
    global image_filename
    image_filename =  filedialog.askopenfilename(title ='Open')

image_filename = ""
btn_image = Button(form_frame, text="UPLOAD IMAGE", command=lambda : upload_image(), width=50)
btn_image.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

# Submit button
# Action when submit button is pressed
def submit():
    global image_filename
    selected_platform = []
    for i in v:
        if i.get() != '0' and i.get() != '':
            selected_platform.append(i.get())

    if input_nama.get() and input_dev.get() and input_thn_rilis.get() and selected_platform and selected_mode.get():
        game = Games(input_nama.get(), input_dev.get(), input_thn_rilis.get(), selected_platform, selected_mode.get(), image_filename)
        games_list.append(game)
        messagebox.showinfo("Information", "Data berhasil ditambahkan")
    else:
        messagebox.showwarning("Warning", "Harap isi semua data")
    image_filename = ""

btn_submit = Button(form_frame, text="SUBMIT", command=submit, width=50)
btn_submit.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

right_frame = LabelFrame(root, padx=10, pady=10, borderwidth=0, highlightthickness=0)
right_frame.grid(row=0, column=1, padx=10, pady=10)

# Application Name
app_name = Label(right_frame, text="My Games", font=("Arial", 25)).grid(row=0, column=0, padx=10, pady=10)

# Application description
desc = "Menampilkan list games milik pribadi"
app_desc = Label(right_frame, text=desc, font=("Arial", 17)).grid(row=1, column=0, padx=10, pady=10)

# Display games list button
# Displaying games list
def show_games():
    top = Toplevel()
    top.title("Daftar Games")

    if games_list:
        for i in games_list:
            game_frame = Frame(top, padx=10, pady=10)
            game_frame.pack(padx=10, pady=10, anchor=W)

            nama = Label(game_frame, text="Nama\t\t:   " + i.get_nama()).grid(row=0, column=1, sticky=W)
            dev = Label(game_frame, text="Nama Developer\t:   " + i.get_nama_dev()).grid(row=1, column=1, sticky=W)
            tahun_rilis = Label(game_frame, text="Tahun Rilis\t:   " + i.get_thn_rilis()).grid(row=2, column=1, sticky=W)
            str_platform = ', '.join(i.get_platform())
            platform = Label(game_frame, text="Platform\t\t:   " + str_platform).grid(row=3, column=1, sticky=W)
            mode = Label(game_frame, text="Mode\t\t:   " + i.get_mode()).grid(row=4, column=1, sticky=W)

            pict = ""
            if i.get_pict():
                pict = i.get_pict()
            else:
                # if the data did not have picture
                pict = "default.png"

            # Load image
            img = Image.open(pict)
            # Resize image
            img = img.resize((100, 100), Image.ANTIALIAS)

            img = PhotoImage(img)
            panel = Label(game_frame, image = img)
            panel.image = img
            panel.grid(row = 0, column=0, rowspan=4, padx=10, pady=10)
    else:
        frame = Frame(top, padx=10, pady=10)
        frame.pack(padx=10, pady=10, anchor=W)

        str = Label(frame, text="Data masih kosong").grid(row=0, column=0, sticky=W)

btn_display = Button(right_frame, text="LIHAT SEMUA GAMES", command=show_games, width=20)
btn_display.grid(row=2, column=0, padx=10, pady=10)

# Delete button
# Deleting games list
def delete_games():
    exit = messagebox.askquestion ('Hapus Data','Yakin untuk hapus semua data?', icon='warning')
    if exit == 'yes':
        messagebox.showinfo('Berhasil', 'Data berhasil dihapus')
        games_list.clear()
    else:
        messagebox.showinfo('Kembali', 'Anda akan kembali ke aplikasi')
    
btn_delete = Button(right_frame, text="HAPUS SEMUA GAMES", command=delete_games, width=20)
btn_delete.grid(row=3, column=0, padx=10, pady=10)

# About application
def about():
    top = Toplevel()
    top.title("Daftar Games")

    about_frame = LabelFrame(top, padx=10, pady=10)
    about_frame.pack(padx=10, pady=10, anchor=W)

    lbl_about_1 = Label(about_frame, text="Nama Aplikasi\t:\tMy Games").grid(row=0, column=0, sticky=W)
    lbl_about_2 = Label(about_frame, text="Deskripsi Aplikasi\t:\tMenampilkan list games milik pribadi").grid(row=1, column=0, sticky=W)
    lbl_about_3 = Label(about_frame, text="Nama Pembuat\t:\tYudi Prasetyo").grid(row=2, column=0, sticky=W)
    lbl_about_4 = Label(about_frame, text="NIM Pembuat\t:\t1905348").grid(row=3, column=0, sticky=W)
    
btn_about = Button(right_frame, text="TENTANG APLIKASI", command=about, width=20)
btn_about.grid(row=4, column=0, padx=10, pady=10)

# Exit button
# Deleting games list
def exit_apps():
    exit = messagebox.askquestion ('Keluar Aplikasi','Yakin untuk keluar?', icon='warning')
    if exit == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Kembali', 'Anda akan kembali ke aplikasi')
    
btn_exit = Button(right_frame, text="KELUAR", command=exit_apps, width=20)
btn_exit.grid(row=5, column=0, padx=10, pady=10)

mainloop()