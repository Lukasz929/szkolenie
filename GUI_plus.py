from tkinter import simpledialog
from tkinter import messagebox
from prettytable import PrettyTable
from prettytable import MARKDOWN


tabela = PrettyTable()
tabela.set_style(MARKDOWN)
tabela.field_names = ["Marka", "Rabat"]
tabela.add_row(["Opel", "15%"])
tabela.add_row(["Skoda", "18%"])
tabela.add_row(["Audi", "20%"])
tabela.add_row(["Inna", "5%"])
print(tabela)

odpowiedz = messagebox.askyesnocancel("Program", "Czy na pewno chcesz otworzyc program?")
if odpowiedz is True:
    print("wcisnieto tak")
elif odpowiedz is False:
    print("wcisnieto nie")
    exit()
else:
    print("wcisnieto anuluj")
    exit()

Cena_auta = simpledialog.askfloat("Cena pojazdu", "Podaj cene pojazdu:", minvalue=0)
rabat_opel = 0.15
rabat_skoda = 0.18
rabat_audi = 0.2
rabat_inny = 0.05
Marka = simpledialog.askstring("Marka pojazdu", "Podaj marke pojazdu: ")
Marka = Marka.capitalize()

# print(type(Cena_auta))
# if Cena_auta == "":
#     messagebox.showerror("","Nie podano ceny")
#     exit()
if Marka == "":
    messagebox.showerror("","Nie podano marki")
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
    messagebox.showinfo("CENA","Cena auta po rabacie: " + str(cena))