import sqlite3

NAME = 'ads.db'

def create_table():
    conn = sqlite3.connect(NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            address TEXT,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_data(ad_data):
    conn = sqlite3.connect(NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ads (title, price, address, description)
        VALUES (?, ?, ?, ?)
    ''', (ad_data['title'], ad_data['price'], ad_data['address'], ad_data['description']))

    conn.commit()
    conn.close()
