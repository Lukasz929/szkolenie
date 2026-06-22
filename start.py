#komunikacja - pol. prit
"""
kom wielolinikowy

"""

print("czesc" , "Rafal")
print("czesc" + "Rafal") # konkatenacja tekstow
print("*" * 80)

#zmienne
imię = "rafal"
print("czesc" , imię)

C = None #zmienna bez wartosci

#nazwy zastrzezone
import keyword
print (keyword.kwlist)

#definiowanie wielu zmiennych
x,y,z=2,5,8
print(x,y,z)

a = 5 #int
b = 5.99 #float
q = a + b
print(q)

#zaokragalnie
a = 16.12
b = 16.1
q = a - b
print(f"{q:.2f}")
q=round(q,2)
print(q)

print("Jestem na szkoleniu.", f"Imies: {imię}", f"wartosc to: {q}", sep=".")
print("Jestem na szkoleniu." , end=".")
print(f"Imies: {imię}" , end=".")
print(f"wartosc to: {q}")

x=5
x+=5 # x=x+5
print(x)

#typ zmiennej 
print(type(q))

print("Lista zakupow:\n\t Chleb \n\t Maslo") #nastepna linia, tab


#liczba z podloga
liczba=123455677899.7776543
print(f"Wynik:{liczba:_}")
print(f"Wynik:{liczba:_}".replace("_"," ").replace(".",","))
polska_liczba=f"{liczba:_}".replace("_"," ").replace(".",",")
print(polska_liczba)

#modifikacja zmiennej
t1 = "Ala ma kota"
t2 = t1.replace("Ala", "Zuzia").replace("kota","żółwia")
print(t2)


