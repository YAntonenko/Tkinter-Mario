# Yuna Antonenko 18.02.2025

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

import tkinter as tk

aken = tk.Tk()
aken = ttk.Window(themename="darkly")
aken.geometry("500x500")
aken.title("Pitsa tellimisvorm")

#1

label = tk.Label(aken, text="Kasutaja ID:").pack()
tk.Entry(aken).pack()

#2
def show_selection():
    # print("Hind: ", selected_color.get())
    # print(var1)
    # print(selected_option.get())
    if selected_option.get()=="Kuller":
        trans = 3
    else:
        trans = 0
    summa = selected_option.get() + var1.get() + float(var2.get()) + var3.get() + trans
    messagebox.showinfo("Su pitsa summa: ", str(summa)+"€")

selected_color = tk.IntVar(value=5)


label = tk.Label(aken, text="Vali suurus (hind): ").pack()

radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

var1 = tk.IntVar(value=0)
var2 = tk.IntVar(value=0)
var3 = tk.IntVar(value=0)

#Checkbox
label = tk.Label(aken, text="Vali lisandid (hind): ").pack()


checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue="1.5", offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()


#fdghrn
label = tk.Label(aken, text="Vali kättetoimetamine (hind):").pack()


# Dropdown 
valikud = ["Kuller (+3€)", "Kohapeal", "Kuller (+3€)"]
selected_option = tk.StringVar()
selected_option.set("Vali üksus")

dropdown = ttk.OptionMenu(aken, selected_option, *valikud,  bootstyle="info")
dropdown.pack()  

btn_confirm = ttk.Button(aken, text="Arvuta hind", command=show_selection, bootstyle="danger")
btn_confirm.pack(pady=20)
aken.mainloop()








