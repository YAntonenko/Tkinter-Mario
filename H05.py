#Yuna Antonenko 06.02.2025


import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")


    def kuva_sisestus():
        tekst1 = sisestus1.get()  
        tekst2 = sisestus2.get()  
        vastus = tk.Label(aken, text=f"Igakuine makse: {text1}")        
        vastus.pack()

    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="x")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5, fill="x")
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5, fill="x")

    label1 = tk.Label(frame, text="Laenusumma (€): ").pack(side="left")
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(side="left", fill="x", expand="True")
   
    label2 = tk.Label(frame2, text="Aastane interssimäär (%): ").pack(side="left")
    sisestus1 = tk.Entry(frame2)
    sisestus1.pack(side="left", fill="x", expand="True")

    label3 = tk.Label(frame3, text="laenuperiood (aastates): ").pack(side="left")
    sisestus3 = tk.Entry(frame3)
    sisestus3.pack(side="left", fill="x", expand="True")

    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()









