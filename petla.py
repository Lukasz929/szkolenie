cars = ["audi", "bmw", "skoda", "kia"]
for cokolwiek in cars:
    print("Pojazd: ", cokolwiek)


ile_razy = len(cars)
for element in range(ile_razy):
    print(f"pobiera element: {element} tablicy o wartosci: {cars[element]}")

# for ile, car in enumerate(cars, start=0):
#     print("Pojazd nr = ", ile, end=" ")
#     print("to: ", car)

print("*" * 80)
garaz = {
    "Toyota" : "Corolla",
    "Mazda"  : "CX-5",
    "BMW"    : "M3",
    "Tesla"  : "Model S"
}
#items- klucz i wartosc, keys - klucze, valuse - wartosci
for marka, model in garaz.items():
    print(f"Marka: {marka} | Model: {model}") 

auta_szczegoly ={
    "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000},
    "KR67890": {"marka": "BMW", "rok": 2018, "przebieg": 120000}
}
print("*" * 80)
for rejestracja, dane in auta_szczegoly.items():
    print(f"Auto o nr {rejestracja}")
    #odwolujemy sie do wewnetrznego slownika "dane"
    marka = dane["marka"]
    rok = dane["rok"]
    przebieg = dane["przebieg"]

    print(f" -> {marka} z roku {rok} ma przebieg: {przebieg}")

print("\n")
print("*" * 80)
