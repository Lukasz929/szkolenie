from tkinter import simpledialog

Cena_auta = simpledialog.askfloat("Cena pojazdu", "Podaj cene pojazdu:", minvalue=0)
rabat_opel = 0.15
rabat_skoda = 0.18
rabat_audi = 0.2
rabat_inny = 0.05
Marka = simpledialog.askstring("Marka pojazdu", "Podaj marke pojazdu: ")
Marka = Marka.capitalize()
# print(type(Cena_auta))
if Cena_auta == "":
    print("Nie podano ceny")
    exit()
elif Marka == "":
    print("Nie podano marki")
else:
    if Marka == "Opel":
        rabat = rabat_opel
    elif Marka == "Skoda":
        rabat = rabat_skoda
    elif Marka == "Audi":
        rabat = rabat_audi
    else:
        rabat = rabat_inny

    cena = int(Cena_auta) * (1 - rabat)
    print("Cena auta po rabacie:", cena)