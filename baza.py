import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Kreiraj mnogo zapisa
zapisi=[
    ('Viktor', 'Viktoric','viktor@yahoo.com'),
    ('Ivan', 'Ivanic', 'ivan@hotmail.com'),
    ('Hugo', 'Ivanic', 'hugo@hr.hr')
]
c.executemany("INSERT INTO klijenti VALUES (?,?,?)",zapisi)

print("Komanda izvrsena uspjesno...")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()