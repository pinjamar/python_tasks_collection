import sqlite3

create_table_query = '''CREATE TABLE IF NOT EXISTS Users (
                        ime TEXT,
                        prezime TEXT, 
                        pin TEXT,
                        aktivan BOOLEAN)'''

insert_into_query = '''INSERT INTO Users (ime, prezime, pin, aktivan
                       VALUES (?,?,?)'''

select_by_pin = '''SELECT * FROM Users WHERE pin=?'''

update_by_pin = '''UPDATE Users
                   SET ime=?,
                       prezime=?,
                       pin=?
                    WHERE pin=?'''

try:
    conn = sqlite3.connect('SmartKey.db')

    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()

    users = [('Filip', 'Skendrovic', '9999'),
             ('Admin', 'Admin', '0000'),
             ('Ivan', 'Gracanin', '1234'),
             ('Ivan', 'Ljaljic', '4321'),
             ('Kresimir', 'Sarac', '4567'),
             ('Iva', 'Zlomislic', '4444'),
             ('Pero', 'Peric', '2222'),
             ]

    for user in users:
        cursor.execute(insert_into_query, user)

    conn.commit()

    # cursor.execute(select_by_pin, ("9999",))
    # record = cursor.fetchone()

    # cursor.execute(update_by_pin, ('Filip', 'Skendrovic', '8888', users[0][2]))
    # conn.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Dogodila se greška")

finally:
    if conn:
        conn.close()
