from datetime import datetime, date, timedelta

#aktualny czas
teraz = datetime.now()
print(f"Teraz jest {teraz}")
print("Teraz jest:", teraz, "\n")

#konkretna data
urodziny = date(1995, 10, 25)
print(f"urodziny: {urodziny}\n")

#arytmetyka dat (timdelta)
teraz = datetime.now().date()
wyniki_dat = (teraz - urodziny).days
print("dni ktore minely:", wyniki_dat, "\n")

dzisiaj = datetime.now()
za_tydzien = dzisiaj + timedelta(weeks=1)
print(f"dzien tygodnia: {dzisiaj.weekday()} \n") # poniedzialek 0, niedziela 6

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
dzien = int(tekst_CSV[3:5])
miesiac = int(tekst_CSV[0:2])
rok = int(tekst_CSV[6:10])

Data_BHP=date(rok, miesiac, dzien)
print("Data BHP:", Data_BHP + timedelta(days=270), "\n")

#obiekt -> tekst
ladna_data = teraz.strftime("%d.%m.%Y")
print(ladna_data)