import sqlite3

db = sqlite3.connect('storage.db')

db.execute("""CREATE TABLE IF NOT EXISTS storage
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name TEXT NOT NULL,
    Quantity INT NOT NULL,
    Price INT NOT NULL
    )""")


def Redigesana():

    izvele = input('1 - Pievienosana | 2 - Datu Mainisana:  ')

    if izvele == '1':
        while True:
            name = input('Ievadiet Preces Nosaukumu: ')
            if name.isdigit() == False:
                if name.strip() == '':
                    print('Ievadiet Atkartoti Preces Nosaukumu!')
                    continue
                else:
                    break
            else:
                print('Ievadiet Atkartoti Preces Nosaukumu!')
                continue

        while True:
            quantity = input('Ievadiet Preces Daudzumu: ')
            if quantity.isdigit():
                break
            else:
                print('Ievadiet Atkartoti Preces Daudzumu!')
                continue

        while True:
            price = input('Ievadiet Preces Cenu: ')
            if price.isdigit():
                break
            else:
                print('Ievadiet Atkartoti Preces Cenu!')
                continue

        # print(name,quantity,price)

        db.execute("""INSERT INTO storage
            (Name, Quantity, Price)
            VALUES (:Name,:Quantity,:Price)
        """,{'Name':name,'Quantity':quantity,'Price':price})

        db.commit()

    elif izvele == '2':
        data = db.execute("""SELECT * FROM storage""")
        for i in data:
            print('ID:',i[0],'|','Name:',i[1],'|','Quantity:',i[2],'|','Price:',i[3])
        while True:
            id = input('Ievadiet ID Precei, Kuras Datus Gribat Mainit: ')
            if id.isdigit():
                if int(id) <= i[0]:
                    break
                else:
                    print('Ievadiet Preces ID Velreiz!')
                    continue                   
            else:
                print('Ievadiet Preces ID Velreiz!')
                continue

        print('Izvelaties Ko Jus Gribat Mainit?')
        while True:
            editing1 = input('1 - Vards | 2 - Daudzums | 3 - Cena: ')
            

Redigesana()