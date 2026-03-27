import sqlite3

def prikaz_sve():
    #Spojiti na bazu
    conn=sqlite3.connect('klijnet.db')

    c=conn.cursor()
    
    c.execute("SELECT rowid, * FROM  klijenti ")
    items=c.fetchall()
    print("Ime Prezime"+"\t"+"email")
    print("-----------"+"\t"+"-----")

    for item in items:
        print(item)

    conn.commit()

    conn.close()
def dodaj_jedan(ime,prezime,email):
    conn=sqlite3.connect('klijnet.db')

    c=conn.cursor()
    
    c.execute("INSERT INTO klijenti VALUES(?,?,?)",(ime,prezime,email))

    print("Komanda izvrsena uspjesno...")
    
    conn.commit()

    conn.close()
def obrisi(id):
    conn=sqlite3.connect('klijnet.db')

    c=conn.cursor()

    c.execute("DELETE from klijenti WHERE rowid=(?)",id)

    conn.commit()
    conn.close()
