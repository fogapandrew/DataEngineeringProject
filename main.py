from src.extraction import *
from src.transformation import *
from src.utils import *
from src.load import *


def main():
    
    """_summary_
    """
    
    # data extraction------------
    books_from_api = religiousBookExtractor().fetch_religious_books_method_one()
    books_from_webpage = religiousBookExtractor().fetch_religious_books_method_two()
    
    
    # data trandormation----------
    api_books = religiousBooksTransformer().books_and_their_attributes_from_api(books_from_api)
    webscrape_books = religiousBooksTransformer().books_and_their_attributes_from_webpage(books_from_webpage)
    
    
    # load------------------------
    combined_christian_books = api_books + webscrape_books
    
    database_path = "books.db"    # creating database books    
    data = load_the_database(database_path).store_books_in_db(combined_christian_books)

    
if __name__== "__main__":
    main()