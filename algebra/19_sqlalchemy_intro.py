import sqlalchemy as db

# from sqlalchemy import Metadata, Table, select 

# Za spajanje na bazu koristimo "engine"
db_engine = db.create_engine('sqlite:///TvrtkaDb.db')

# Imamo engine, sad se spajamo na bazu
db_connection = db_engine.connect()

# Za dohvat METADATA podataka
db_metadata = db.MetaData()

# Dohvatimo podatke o tabeli s djelatnicima Employees
employees = db.Table('Employees', db_metadata, autoload_with=db_engine)

# Sada kad imamo detalje o tablici možemo dohvatiti podatke iz nje
# SELECT * FROM Employees

sql_select_upit = db.select(employees)

# Kreirat ćemo objekt koji ćemo koristiti kao posrednika (proxy) za pristup podacima
result_proxy = db_connection.execute(sql_select_upit)

# Kreirat ćemo varijablu za listu redaka pročitanih iz baze
result = result_proxy.fetchall()

for res in result:
    print(res)