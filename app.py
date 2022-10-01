from cProfile import run
import tkinter
import customtkinter as ct
import os
from tkinter import ANCHOR, CENTER, filedialog, Text

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")

app = ct.CTk()
app.geometry("400x300")
app.title("App Runner 2")
apps = []

def addExecutable():
    filename= filedialog.askopenfilename(initialdir="/", title="Select Executable", filetypes=(("Executables","*exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tkinter.Label(app, text='apps')
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

openExecutable = ct.CTkButton(app, text="Open Executable", command=addExecutable)
openExecutable.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

runAll = ct.CTkButton(app, text="Run All")
runAll.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()
