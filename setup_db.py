import sqlite3
import os

# Ensure the instance folder exists to store the SQLite database file
if not os.path.exists('instance'):
    # Create the instance folder if it doesn't exist
    os.makedirs('instance')

# Define the path to the SQLite database file loocated in the instance folder
db_path = os.path.join('instance', 'board_games.sqlite')

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)

# Read the SQL schema from the schema.sql file and execute it to create the necessary tables in the database
with open('app/schema.sql') as f:
    conn.executescript(f.read())

print("Database initialized successfully in:", db_path)
conn.close()