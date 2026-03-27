import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Redoslijed

#c.execute("SELECT rowid, * FROM klijenti ORDER BY rowid DESC ")
#c.execute("SELECT rowid, * FROM klijenti ORDER BY rowid ASC ")
#c.execute("SELECT rowid, * FROM klijenti ORDER BY prezime")
#c.execute("SELECT rowid, * FROM klijenti ORDER BY ime")

#AND/OR
#c.execute("SELECT rowid, * FROM klijenti WHERE prezime LIKE 'Krun%' OR rowid=1 ")

#Limits

c.execute("SELECT rowid, * FROM klijenti ORDER BY rowid LIMIT 3")

items=c.fetchall()

for item in items:
    print(item)

#print("Komanda izvrsena uspjesno...")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()