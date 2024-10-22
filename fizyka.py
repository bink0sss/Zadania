import tkinter as tk
from tkinter import messagebox

# Funkcja do obliczania sił reakcji w podporach
def oblicz_sily():
    try:
        masa = float(masa_entry.get())
        dlugosc_belki = float(dlugosc_belki_entry.get())
        a = float(odleglosc_a_entry.get())
        b = float(odleglosc_b_entry.get())
        grawitacja = float(grawitacja_entry.get())

        if a + b > dlugosc_belki:
            raise ValueError("Odległości podpór są większe niż długość belki!")


        # Siła grawitacji (ciężar belki)
        ciezar_belki = masa * grawitacja
        
        # Moment względem podpor
        Rb = (ciezar_belki * (dlugosc_belki / 2 - a)) / (dlugosc_belki - b - a)  # Siła reakcji w podporze B
        Ra = ciezar_belki - Rb  # Siła reakcji w podporze A

        # Wyświetlenie wyników w nowym oknie
        messagebox.showinfo("Wynik", f"Siła w podporze A: {Ra:.2f} N\nSiła w podporze B: {Rb:.2f} N")

    except ValueError as e:
        messagebox.showerror("Błąd", f"Wprowadź poprawne dane!\n{e}")

# Funkcja walidująca - blokuje znaki niebędące cyframi lub kropką dziesiętną oraz blokuje znak minus
def waliduj_wejscie(tekst, poprzedni_tekst):
    # Zezwalamy na pusty ciąg, liczby dodatnie i kropkę dziesiętną
    if tekst == "":
        return True
    # Sprawdzamy, czy tekst zawiera tylko cyfry i maksymalnie jedną kropkę dziesiętną
    if tekst.replace('.', '', 1).isdigit():
        # Sprawdzamy, czy nie ma więcej niż jednej kropki dziesiętnej
        if tekst.count('.') <= 1:
            return True
    # Jeśli nie spełnia warunków, wracamy do poprzedniego poprawnego tekstu
    return False

# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Obliczanie sił w podporach belki")

# Rejestracja funkcji walidującej
reg = root.register(waliduj_wejscie)

# Etykiety i pola do wprowadzania danych z walidacją
tk.Label(root, text="Masa belki (kg):").grid(row=0, column=0)
masa_entry = tk.Entry(root, validate="key", validatecommand=(reg, '%P', '%s'))  # Walidacja liczb dodatnich
masa_entry.grid(row=0, column=1)

tk.Label(root, text="Długość belki (m):").grid(row=1, column=0)
dlugosc_belki_entry = tk.Entry(root, validate="key", validatecommand=(reg, '%P', '%s'))  # Walidacja liczb dodatnich
dlugosc_belki_entry.grid(row=1, column=1)

tk.Label(root, text="Odległość podpory A od końca belki (m):").grid(row=2, column=0)
odleglosc_a_entry = tk.Entry(root, validate="key", validatecommand=(reg, '%P', '%s'))  # Walidacja liczb dodatnich
odleglosc_a_entry.grid(row=2, column=1)

tk.Label(root, text="Odległość podpory B od końca belki (m):").grid(row=3, column=0)
odleglosc_b_entry = tk.Entry(root, validate="key", validatecommand=(reg, '%P', '%s'))  # Walidacja liczb dodatnich
odleglosc_b_entry.grid(row=3, column=1)

tk.Label(root, text="Siła grawitacji (m/s²):").grid(row=4, column=0)
grawitacja_entry = tk.Entry(root, validate="key", validatecommand=(reg, '%P', '%s'))  # Walidacja liczb dodatnich
grawitacja_entry.grid(row=4, column=1)
grawitacja_entry.insert(0, "9.81")  # Domyślna wartość siły grawitacji

# Przycisk do obliczania sił
oblicz_button = tk.Button(root, text="Oblicz siły", command=oblicz_sily)
oblicz_button.grid(row=5, columnspan=2)

# Uruchomienie aplikacji
root.mainloop()
