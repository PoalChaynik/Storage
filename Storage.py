import sqlite3

db = sqlite3.connect('storage.db')

db.execute("""CREATE TABLE IF NOT EXISTS storage
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name TEXT NOT NULL,
    Quantity INT NOT NULL,
    Price INT NOT NULL
    )""")

print('"PROJECT - NOLIKTAVA" GATAVA DARBAM!\n')
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
        print()
        for i in data:
            print('ID:',i[0],'|','Nosaukums:',i[1],'|','Daudzums:',i[2],'|','Cena:',i[3])
        print()
        while True:
            id = input('Ievadiet ID Precei, Kuras Datus Gribat Mainit | 0 - Atcelt: ')
            if id.isdigit():
                if id == '0':
                    return
                elif int(id) <= i[0]:
                    break
                else:
                    print('Ievadiet Preces ID Velreiz!')
                    continue                   
            else:
                print('Ievadiet Preces ID Velreiz!')
                continue
        if id != '0':
            print('Izvelaties Ko Jus Gribat Mainit?')
        while True:
            if id == '0':
                return
            editing1 = input('1 - Nosaukums | 2 - Daudzums | 3 - Cena: ')
            if editing1.isdigit() and int(editing1) <= 3:
                break
            else:
                print('Velreiz Izvelaties Ko Jus Gribat Mainit!')
                continue

        newName = 'Ievadiet Jaunu Preces Nosaukumu: '
        newQuantity = 'Ievadiet Jaunu Preces Daudzumu: '
        newPrice = 'Ievadiet Jaunu Preces Cenu: '

        if editing1 == '1':
            while True:
                newData = input(newName)
                if newData.isdigit() == False:
                    if newData.strip() == '':
                        print('Ievadiet Atkartoti Preces Nosaukumu!')
                        continue
                    else:
                        break
                else:
                    print('Ievadiet Atkartoti Preces Nosaukumu!')
                    continue

            newData = (newData,id)
            db.execute("""UPDATE storage SET Name=? WHERE ID=?""", newData)
            db.commit()

        elif editing1 == '2':
            while True:
                newData = input(newQuantity)
                if newData.isdigit():
                    break
                else:
                    print('Ievadiet Atkartoti Preces Daudzumu!')
                    continue

            newData = (newData,id)
            db.execute("""UPDATE storage SET Quantity=? WHERE ID=?""", newData)
            db.commit()
        elif editing1 == '3':
            while True:
                newData = input(newPrice)
                if newData.isdigit():
                    break
                else:
                    print('Ievadiet Atkartoti Preces Cenu!')
                    continue
            newData = (newData,id)
            db.execute("""UPDATE storage SET Price=? WHERE ID=?""", newData)
            db.commit()

def Searching():
    while True:
        print('Izvelaties Meklesanas Veidu!')
        veids = input('1 - Pec ID | 2 - Pec Nosaukuma | 3 - Paradit Visus Datus: ')
        if veids == '2':
            while True:
                Name1 = input('Ievadiet Preces Nosaukumu: ')
                print()
                visiDati = db.execute("SELECT * FROM storage")
                for i in visiDati:
                    if i[1] == Name1:
                        print('ID:',i[0],'|','Nosaukums:',i[1],'|','Daudzums:',i[2],'|','Cena:',i[3])
                        print()
                        return
                    else:
                        continue           
        if veids == '1':
            while True:
                id1 = input('Ievadiet Preces ID: ')
                print()
                visiDati = db.execute("SELECT * FROM storage")
                for i in visiDati:
                    if i[0] == int(id1):
                        print('ID:',i[0],'|','Nosaukums:',i[1],'|','Daudzums:',i[2],'|','Cena:',i[3])
                        print()
                        return
                    else:
                        continue
                
        if veids == '3':
            visiDati = db.execute("SELECT * FROM storage")
            print()
            for i in visiDati:
                print('ID:',i[0],'|','Nosaukums:',i[1],'|','Daudzums:',i[2],'|','Cena:',i[3])    
        print()   
        break





while True:
    menu = input("MENU| 1 - Meklesana | 2 - Redigesana | 3 - Iziet: ")
    if menu == '2':
        Redigesana()
    elif menu == '1':
        Searching()
    elif menu == '3':
        db.close()
        exit()
    else:
        print('Ievadiet Izveles Variantu Velreiz!')
        continue