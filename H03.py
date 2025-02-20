#Yuna Antonenko 04.02.2025
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")


    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  
        kuintressimäär = float(sisestus2.get())/12/100
        makste_arv = int(sisestus3.get())*12

        igakuine_makse = laenusumma * kuintressimäär / (1 - (1 + kuintressimäär)** - makste_arv)

        vastus = tk.Label(aken, text=f"Esimene sisestus: {laenusumma}, Teine sisestus: {makste_arv}")        
        vastus.pack()

    label = tk.Label(aken, text="Laenusumma (€): ").pack(pady=(10, 0))
    sisestus1 = tk.Entry(aken).pack()

   
    label = tk.Label(aken, text="Aastane interssimäär (%): ").pack(pady=(10, 0))
    sisestus2 = tk.Entry(aken).pack()

    label = tk.Label(aken, text="laenuperiood (aastates): ").pack(pady=(10, 0))
    sisestus3  = tk.Entry(aken).pack()

    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()
