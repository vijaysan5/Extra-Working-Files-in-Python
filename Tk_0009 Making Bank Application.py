

import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

def submit():
    opening = f"""
    
    username : {username.get()}
    password : {password.get()}
    """

    print(opening)
    messagebox.showinfo("Information Box", "Ready to Start")

root = tk.Tk()
root.title("Bank Application")
root.geometry("300x400")

username= tk.StringVar()
password = tk.StringVar()

image = Image.open("GUI Tkinter Program/900_image PNG People logo.png").resize((80,80))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.place(x=100, y=5)

tk.Label (root, text="Username").place(x=110, y=100)
a = tk.Entry (root, textvariable=username).place(x=80, y=120)
tk.Label (root, text="Password").place(x=110, y=150)
tk.Entry (root, textvariable=password).place(x=80, y=170)
tk.Button (root, text="")
tk.Button (root, text="Submit", command=submit).place(x=120, y=320)

root.mainloop()

