import os
import json
import requests
import sqlite3
from PIL import Image
from io import BytesIO

# constants ir toot directory

root_directory = os.path.dirname(os.path.abspath(__file__))


# Ensure the directory is writable and exists
if not os.path.exists(root_directory):
    os.makedirs(root_directory)
    
suggested_books_file = os.path.join(root_directory, "suggestedbooks.json")


class load_save_and_suggest_next_books:
    
    def __init__(self)-> None:
        pass
    

    def load_suggested_books(self):
        """
        method to load suggested books from file
        """
        try:
            with open(suggested_books_file , 'r') as file:
                return set(json.load(file))
        except (FileNotFoundError,json.JSONDecodeError):
            return set()
    

    def save_suggested_books(self, suggested_books):
        """
        Function to save suggested books to file

        Args:
            suggested_books (_type_): _description_
        """
        with open(suggested_books_file, 'w') as file:
            json.dump(list(suggested_books), file)
        
        

    def suggest_next_book(self, books: list)-> dict:
    
        """
        suggest the next book with the highest score that hasn't been suggested yet
    
        """ 
        
        # Load suggested books from file
        suggested_books = self.load_suggested_books()
        
        # Filter out already suggested books
        unsuggested_books = [book for book in books if book[0] not in suggested_books]
    
        if not unsuggested_books:
            print("No more books to suggest")
            return None
    
    
        suggested_book = max(unsuggested_books, key=lambda x: x[2])
    
    
        # Unpack the book attributes
        title, author, score, book_cover_url = suggested_book
    
        print("We suggest you read the following book next:")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"score: {score}")
        print(f"ISBN (): {book_cover_url}")
         #print(f"Cover URL: {webbrowser.open(cover_url)}")
    
         
        # Add the book to the suggested_books set
        suggested_books.add(title)
    
          # Save the updated set to the file
        self.save_suggested_books(suggested_books)
    

        return suggested_book



def display_image_from_url(image_url):
    """
    Display an image directly from its URL.
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.show()  # Opens the image in the default image viewer
        else:
            print("Image could not be loaded.")
    except Exception as e:
        print(f"Error fetching image: {e}")


class retrieve_book_from_database:
    
    def __init__(self, database_path: str):
        self.database_path = database_path

    def fetch_and_display_books(self):
        """
        Retrieve books from the database and display their details along with the cover image.

        :param database_path: Path to the SQLite database.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        # Query to fetch all books
        cursor.execute('SELECT title, author, score, cover_url FROM books')
        books = cursor.fetchall()

        # Process and display data
        for title, author, score, cover_url in books:
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Score: {score}")
            print(f"Cover URL: {cover_url}")

            # Display the cover image if available
            if cover_url != "No Cover Available":
                display_image_from_url(cover_url)
            else:
                print("No cover image available.\n")

        # Close the database connection
        conn.close()
