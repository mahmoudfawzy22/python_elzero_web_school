import sqlite3


db = sqlite3.connect("elzero.db")

cursor = db.cursor()

# cursor.execute("insert into Users values('1', 'Ahmed', '20/10/1980', 'a@elzero.org')")
# cursor.execute("insert into Users values('2', 'Sayed', '20/10/1990', 's@elzero.org')")
# cursor.execute("insert into Users values('3', 'Gamal', '05/10/1991', 'g@elzero.org')")
# cursor.execute("insert into Users values('4', 'Mahmoud', '24/4/2005', 'm@elzero.org')")
# cursor.execute("insert into Users values('5', 'Sameh', '08/10/2000', 'sa@elzero.org')")

cursor.execute("select * from Users")

Users = cursor.fetchall()

cursor.execute("select * from Users where id=?", ('5'))

print(cursor.fetchone())

id_user = input("Enter The Number of the user : ")

cursor.execute("select * from Users where id=?", (id_user,))

user = cursor.fetchone()

if user:
    cursor.execute(f"delete from Users where id = {id_user}")

    db.commit()

    print(f"User with ID {id_user} deleted successfully.")

else:
    print(f"User whit ID {id_user} not found")


db.commit()

db.close()