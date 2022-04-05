import sqlite3

def Edit():

 while True:
    nosaukums = input('ievadiet preces nosaukumu')
    if nosaukums.strip() == "" and nosaukums.isdigit() == True:
        print("ievadiet velreiz")
    else:
        break

while True:
    daudzums = input('ievadiet preces daudzumu ')
    if daudzums.strip() == "" and daudzums.isdigit() == True:
        print("ievadiet velreiz")
    else:
        break

while True:
    cena = input('ievadiet preces cenu')
    if len(cena) <0 and len(cena) >100 (cena).isdigit() == False:
        continue
    else:
        break

Edit()

