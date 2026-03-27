import sqlite3

#Spojiti na bazu
conn=sqlite3.connect('klijnet.db')

#Kreiranje kursora
c=conn.cursor()

#Query database

c.execute("SELECT * FROM  klijenti ")

#print(c.fetchone()[0])
#print(c.fetchmany(4))
#print(c.fetchall())

items=c.fetchall()
print("Ime Prezime"+"\t"+"email")
print("-----------"+"\t"+"-----")

for item in items:
    print(item[0]+" " +item [1] + "\t" +item[2])


#print("Komanda izvrsena uspjesno...")

#Potvrda naredbe
conn.commit()

#Zatvori konekciju
conn.close()