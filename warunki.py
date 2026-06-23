pensja = 12000
wczasy = "morze"

if pensja < 5000 and wczasy == "mazury":
    print("nie za wiele na wczasy") 
# \ podzial wiersza na dodatkowa linie, ew nawiasy po elif ()
elif (pensja < 8000 and \
    (wczasy == "mazury"
     or wczasy == "morze")):
    komunikat = "moze ta byc"  #5000 - 7999
elif pensja < 13000 and pensja >= 8000:
    komunikat = "super"
else:  # opcjonalne
    komunikat = "moze byc"
# CTRL + / - Comment/uncomment

print(komunikat)