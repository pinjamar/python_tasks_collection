import sqlite3

# imat ćemo tablicu obligations koja će imati 4 stupca: user (TEXT), start (DATETIME), end (DATETIME), task (TEXT)! 

# Obligations Queries
# Create Obligations Table
create_obligations_query = """CREATE TABLE IF NOT EXISTS Obligations (
                                user TEXT,
                                start DATETIME,
                                end DATETIME, 
                                task TEXT
                            )"""
# Insert into Obligations
insert_into_obligations_query = """INSERT INTO Obligations (user, start, end, task)
                                   VALUES (?, ?, ?, ?)"""

# Select Obligations By User 
select_obligations_by_username = """SELECT * FROM Obligations WHERE user=?"""

# conn = sqlite3.connect('MySmartHome.db')
# cursor = conn.cursor()

# cursor.execute(create_obligations_query)
# conn.commit()

# obligations = [('Antonio', '2023-08-31 09:00:00', '2023-08-31 10:00:00', 'Jutarnji trening'), 
#                ('Antonio', '2023-08-31 13:00:00', '2023-08-31 14:00:00', 'Ručak')]

# for obligation in obligations:
#     cursor.execute(insert_into_obligations_query, obligation)
    
# conn.commit()
# cursor.close()
# conn.close()


