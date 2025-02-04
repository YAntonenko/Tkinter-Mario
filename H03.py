#Yuna Antonenko 04.02.2025
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")


    def kuva_sisestus():
        tekst1 = sisestus1.get()  
        tekst2 = sisestus2.get()  
        tekst3 = sisestus3.get() 
        vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}")        
        vastus.pack()

    label = tk.Label(aken, text="Laenusumma (€): ").pack()
    sisestus1 = tk.Entry(aken).pack()

   
    label = tk.Label(aken, text="Aastane interssimäär (%): ").pack()
    sisestus2 = tk.Entry(aken).pack()

    label = tk.Label(aken, text="laenuperiood (aastates): ").pack()
    sisestus3  = tk.Entry(aken).pack()

    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()
