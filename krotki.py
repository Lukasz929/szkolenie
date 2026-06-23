#krotka (tuple) - niezmienna lista 
krotka = (7, 13, 17)
#krotka[1] = 2  nie mozna modyfikowac
print(krotka, "\n")

jeden_element=(5,) #jeden element musi byc przecinek
print(type(jeden_element))

print(krotka.count(13), "\n")

krotka_1 = (1, 2, 3)
krotka_2 = (4, 5, 6)
wynik = krotka_1 + krotka_2
print(wynik)
print(5 in wynik) #czy element jest w zbiorze

#przeksztalcanie na liste 
lista = list(krotka)
lista[0] = "nowy"
krotka=tuple(lista)
print(krotka)
print(type(krotka))