'''
Dev: Brayan S.
Script description: Configure SQLite3 data base
'''

#Import engine database package
import sqlite3

#Create database connection (Database name)
conn = sqlite3.connect('market.db')

#Creating cursor object by connection => nos permite ejecutar comandos o peraciones sql
cur = conn.cursor()

#Create users table
users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        firstname TEXT NOT NULL, 
        lastname TEXT NOT NULL,
        ident_number TEXT UNIQUE NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        );
'''
#Excecute SQL  (Query)
cur.execute(users_table)

#Save changes in database => Push in database
conn.commit()

#print("::: Database market created successfully! :::")

#Close connection
#conn.close()