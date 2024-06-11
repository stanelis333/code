

import sqlite3

conn = sqlite3.connect("paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/paskaitos1.db")
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS paskaitos (pavadinimas text, destytojas text, trukme integer) """)
conn.commit()

# c.execute(" INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80), ('Java', 'Tomas', 80) ")
# conn.commit()

c.execute("SELECT * FROM paskaitos WHERE trukme > 50")
print(c.fetchall())

c.execute("UPDATE paskaitos SET pavadinimas = 'Python programavimas' WHERE destytojas = 'Donatas' ")
conn.commit()

c.execute("DELETE from paskaitos WHERE pavadinimas = 'Java' ")
conn.commit()

c.execute("SELECT * FROM paskaitos")
print(c.fetchall())


conn.close()

