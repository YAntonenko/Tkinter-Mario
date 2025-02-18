# Yuna Antonenko 11.02.2025


import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps
import os

selected_files = []

def open_directory():
    directory = filedialog.askdirectory()
    dir_label.config(text="Valitud kaust: {directory}")
    kausta_sissu =os.listdir(directory)
    for fail in kausta_sissu:
        file_name, file_extension = os.path.splitext(fail)
        if file_extension == "jpg" or file_extension == ".jped":
            text_field.insert(tk.END, fail + "\n")
            selected_files.append(os.path.join(directory, fail))

    print(selected_files)



def save_directory():
    save_directory = filedialog.askdirectory()
    for file in selected_files:
        img = Image.open(file)
        img = img.resize((200, 200))
        filename = os.path.basename(file)
        img.save(os.path.join(save_directory, filename))
    print("Pildid on salvedtatud.")



aken = tk.Tk()
aken.geometry("450x400")
aken.title("Pildi suuruse muutmine")

label = tk.Label(aken, text="Pildi suurus 200x200", font=("Arial", 16))
label.pack(pady=10)

inputtxt = tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

open_button = tk.Button(aken, text="Vali failid", command=open_directory)
open_button.pack(pady=10)

save_button = tk.Button(aken, text="salvesta pildid", command=save_directory)
save_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)


aken.mainloop()
















