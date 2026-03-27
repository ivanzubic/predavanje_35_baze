import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Kreiranje tablice
c.execute("""CREATE TABLE klijenti(
          ime DATATYPE,
          prezime DATATYPE,
          email DATATYPE
          )""")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()