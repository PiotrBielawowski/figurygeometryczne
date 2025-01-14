import tkinter as tk
from tkinter import messagebox

def wybierz_figure(figura):
    wynik.delete(1.0, tk.END)
    wynik.insert(tk.END, f"Wybrano figurę: {figura}\n")

    if figura == "Kwadrat":
        a.config(state="normal")
        b.config(state="disabled")
        c.config(state="disabled")
        h.config(state="disabled")
        r.config(state="disabled")
    elif figura == "Prostokąt":
        a.config(state="normal")
        b.config(state="normal")
        c.config(state="disabled")
        h.config(state="disabled")
        r.config(state="disabled")
    elif figura == "Trójkąt":
        a.config(state="normal")
        b.config(state="normal")
        c.config(state="normal")
        h.config(state="normal")
        r.config(state="disabled")
    elif figura == "Koło":
        a.config(state="disabled")
        b.config(state="disabled")
        c.config(state="disabled")
        h.config(state="disabled")
        r.config(state="normal")

    wybrana_figura.set(figura)

def oblicz():
    figura = wybrana_figura.get()
    if figura == "":
        messagebox.showerror("Błąd", "Nie wybrano żadnej figury")
        return

    try:
        wartosc_a = float(a.get()) if a.get() else 0
        wartosc_b = float(b.get()) if b.get() else 0
        wartosc_c = float(c.get()) if c.get() else 0
        wartosc_h = float(h.get()) if h.get() else 0
        wartosc_r = float(r.get()) if r.get() else 0
    except ValueError:
        messagebox.showerror("Błąd", "Podano nieprawidłowe dane")
        return

    if figura == "Kwadrat":
        pole = wartosc_a ** 2
        obwod = 4 * wartosc_a
    elif figura == "Prostokąt":
        pole = wartosc_a * wartosc_b
        obwod = 2 * (wartosc_a + wartosc_b)
    elif figura == "Trójkąt":
        pole = 0.5 * wartosc_a * wartosc_h
        obwod = wartosc_a + wartosc_b + wartosc_c
    elif figura == "Koło":
        pole = 3.14 * wartosc_r ** 2
        obwod = 2 * 3.14 * wartosc_r

    wynik.delete(1.0, tk.END)
    wynik.insert(tk.END, f"Pole: {pole}\n")
    wynik.insert(tk.END, f"Obwód: {obwod}\n")

okno = tk.Tk()
okno.geometry("1920x1080")
okno.title("Obliczanie figur geometrycznych")

wybrana_figura = tk.StringVar(value="")

etykieta_naglowek = tk.Label(okno, text="Wybierz figurę", font=("Arial", 24))
etykieta_naglowek.pack(pady=20)

ramka_przyciski = tk.Frame(okno)
ramka_przyciski.pack(pady=20)

btn_kwadrat = tk.Button(ramka_przyciski, text="Kwadrat", font=("Arial", 16), command=lambda: wybierz_figure("Kwadrat"))
btn_kwadrat.grid(row=0, column=0, padx=10, pady=10)

btn_prostokat = tk.Button(ramka_przyciski, text="Prostokąt", font=("Arial", 16), command=lambda: wybierz_figure("Prostokąt"))
btn_prostokat.grid(row=0, column=1, padx=10, pady=10)

btn_trojkat = tk.Button(ramka_przyciski, text="Trójkąt", font=("Arial", 16), command=lambda: wybierz_figure("Trójkąt"))
btn_trojkat.grid(row=0, column=2, padx=10, pady=10)

btn_kolo = tk.Button(ramka_przyciski, text="Koło", font=("Arial", 16), command=lambda: wybierz_figure("Koło"))
btn_kolo.grid(row=0, column=3, padx=10, pady=10)

ramka_dane = tk.Frame(okno)
ramka_dane.pack(pady=20)

etykieta_a = tk.Label(ramka_dane, text="a:", font=("Arial", 14))
etykieta_a.grid(row=0, column=0, padx=5, pady=5)
a = tk.Entry(ramka_dane, font=("Arial", 14))
a.grid(row=0, column=1, padx=5, pady=5)

etykieta_b = tk.Label(ramka_dane, text="b:", font=("Arial", 14))
etykieta_b.grid(row=1, column=0, padx=5, pady=5)
b = tk.Entry(ramka_dane, font=("Arial", 14))
b.grid(row=1, column=1, padx=5, pady=5)

etykieta_c = tk.Label(ramka_dane, text="c:", font=("Arial", 14))
etykieta_c.grid(row=2, column=0, padx=5, pady=5)
c = tk.Entry(ramka_dane, font=("Arial", 14))
c.grid(row=2, column=1, padx=5, pady=5)

etykieta_h = tk.Label(ramka_dane, text="h:", font=("Arial", 14))
etykieta_h.grid(row=3, column=0, padx=5, pady=5)
h = tk.Entry(ramka_dane, font=("Arial", 14))
h.grid(row=3, column=1, padx=5, pady=5)

etykieta_r = tk.Label(ramka_dane, text="r:", font=("Arial", 14))
etykieta_r.grid(row=4, column=0, padx=5, pady=5)
r = tk.Entry(ramka_dane, font=("Arial", 14))
r.grid(row=4, column=1, padx=5, pady=5)

btn_oblicz = tk.Button(okno, text="Oblicz", font=("Arial", 16), command=oblicz)
btn_oblicz.pack(pady=20)

wynik = tk.Text(okno, font=("Arial", 14), height=10, width=40)
wynik.pack(pady=20)

okno.mainloop()
