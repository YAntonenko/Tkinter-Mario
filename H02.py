#Yuna Antonenko 04.02.2025

import tkinter as tk
import ctypes
from PIL import Image, ImageTk


def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    p = 50
    pilt = pilt.crop((0+p, 0+p, laius+p, korgus+p))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def main():

    aken = tk.Tk()
    aken.title("Yuna ülesanded")
    aken.geometry("400x400")
    aken.resizable(True, False)

    #pilt
    label = tk.Label(aken, text="Chuck Norris", font=("Arial", 16, "bold"), fg="blue").pack()
    kuva_pilt(aken, "norris.jpg", 200, 200)
   
    #text
    lorem = "Lorem ipsum dolor sit amet,consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12), fg="black")
    tekst.insert(tk.INSERT, lorem)
    tekst.pack()


    aken.mainloop()

if __name__ == "__main__":
    main()