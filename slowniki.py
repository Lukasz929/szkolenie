#slownik: klucz-wartosc, nie pozwala na duplikaty kluczy,
#klucz musi byc niezmiennym typem danych (tekst czyli string, int i tuple)

dict={
    "brand":"Ford",
    "model":"Mondeo",
    "year":"2018"
}
print(dict)
print(type(dict))
print(dict["model"])


x = dict["model"]
#x = dict["model_auta"]

x = dict.get("model") #do x przypisanie modelu
print(x)
x = dict.get("model_auta", "brak danych") #jesli nie ma model_auta to wyrzuci brak danych
print(x)
print(dict.get("model_auta", "brak danych"))

dict["year"] = 2023 
dict["kolor"] = "czarny"
print(dict)

print(dict.keys()) #nazwy kluczy
print(dict.values()) #nazwy wartosci
print(dict.items()) #para klucz wartosc

