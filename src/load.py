import sqlite3

class load_the_database:
    def __init__(self, db_path):
        self.db_path = db_path

    def store_books_in_db(self, books):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                score REAL,
                cover_url TEXT
            )
        ''')
        
        for book in books:
            if isinstance(book[0], list):
                # Handle nested lists
                for i in range(len(book[0])):
                    cursor.execute('''
                        INSERT INTO books (title, author, score, cover_url) VALUES (?, ?, ?, ?)
                    ''', (book[0][i], book[1][i], book[2][i], book[3][i]))
            else:
                cursor.execute('''
                    INSERT INTO books (title, author, score, cover_url) VALUES (?, ?, ?, ?)
                ''', (book[0], book[1], book[2], book[3]))
        
        conn.commit()
        conn.close()

    def read_books_from_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        
        conn.close()
        return books