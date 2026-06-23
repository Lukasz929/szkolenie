from tkinter import simpledialog
from tkinter import messagebox
from prettytable import PrettyTable
from prettytable import MARKDOWN

# 1. wersja
firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
Kurs_akcji_wczoraj = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
Kurs_akcji_dzis    = [16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11]
komunikat_final = ""

ile_razy = len(Kurs_akcji_dzis)
Roznica = []
Info = []
for akcja in range(ile_razy):
    wartosc = Kurs_akcji_dzis[akcja] - Kurs_akcji_wczoraj[akcja]
    Roznica.append(f"{wartosc:.2f}")
    if wartosc > 0:
        Info.append("wzrosl")
    else:
        Info.append("spadl")
    #komunikaty
    komunikat = f"Firma: {firmy[akcja]}, kurs akcji {Info[akcja]} o {Roznica[akcja]}"
    komunikat_final += komunikat + "\n"


print(Roznica, Info)

tabela = PrettyTable()
tabela.field_names = ["Firma", "Kurs wczoraj", "Kurs dzisiaj", "Roznica", "Informacja"]

for i in range(ile_razy):
    tabela.add_row([firmy[i], Kurs_akcji_wczoraj[i], Kurs_akcji_dzis[i], Roznica[i], Info[i]])

print(tabela)

messagebox.showinfo("Informacja", komunikat_final)