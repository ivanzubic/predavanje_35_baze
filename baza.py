import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Kreiraj prvi jednostruki zapis
c.execute("INSERT INTO klijenti VALUES('Vito', 'Vitajic', 'vitoo@gmail.com')")

print("Komanda izvrsena uspjesno...")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()