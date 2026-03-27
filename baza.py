import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Query database

c.execute("SELECT * FROM  klijenti WHERE prezime LIKE 'Vi%'")
c.execute("SELECT * FROM  klijenti WHERE email LIKE '%gmail.com'")


items=c.fetchall()


for item in items:
    print(item)


#print("Komanda izvrsena uspjesno...")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()