import sqlite3

# class load_the_database:
    
#     def __init__(self, database_path: str) -> str:
#         self.database_path = database_path

#     def store_books_in_db(self, books: list):
#         """
#         Store books and their attributes in an SQLite database.

#         :param database_path: Path to the SQLite database.
#         :param books: List of books and their attributes to store.
#         """
#         # Connect to the SQLite database (or create it)
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()

#         # Create a table if it doesn't exist
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS books (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 title TEXT,
#                 author TEXT,
#                 score REAL,
#                 cover_url TEXT
#             )
#         ''')
        

#         # Insert book data into the database
#         for book in books:
#             title, author, score, book_cover_url = book
#             cursor.execute('''
#                 INSERT INTO books (title, author, score, cover_url)
#                 VALUES (?, ?, ?, ?)
#             ''', (title, author, score, book_cover_url))

#         # Commit changes and close the connection
#         conn.commit()
#         conn.close()


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