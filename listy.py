mieszanka = ["Ania", 5, True]
print(mieszanka[1]) 
print(mieszanka[-1], "\n") #mozna tez indeksy ujemne wtedy idziemy w lewo

print(len(mieszanka), "\n") #dlugosc listy

lista = [7, 13, 17]
print("Suma=", sum(lista))
print("Max=", max(lista), "\n")

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
podzielony_tekst = tekst_CSV.split()
print("list:", podzielony_tekst)

podzielony_tekst.append( [10000, 15000] )
print("append:",podzielony_tekst)

podzielony_tekst.extend( [10000, 15000] )
print("extend:", podzielony_tekst)
