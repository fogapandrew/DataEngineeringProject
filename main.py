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



    HARRY_POTTER_BOOKS_LIST = harrypoterbookextractor().fetchstephenbooks()   # API data  
    READY_ANY_BOOKS_LIST = readanybookextractor().fetchreadanybook()   # web data


    # data trandormation----------
    api_books = religiousBooksTransformer().books_and_their_attributes_from_api(books_from_api)
    webscrape_books = religiousBooksTransformer().books_and_their_attributes_from_webpage(books_from_webpage)


    api_harrypotter_books = harrypoterbooktransformer().get_all_harryporterbook(HARRY_POTTER_BOOKS_LIST)
    webscrape_readany_books = readanybooktransformer().get_all_readanybook(READY_ANY_BOOKS_LIST)
    


    # load------------------------
    combined_christian_books = api_books + webscrape_books + webscrape_readany_books

    database_path = "books.db"    
    
    
    # creating database books    
    data = load_the_database(database_path).store_books_in_db(combined_christian_books)

     # Read and print the contents of the database
    books_in_db = load_the_database(database_path).read_books_from_db()

    
    print(books_in_db)
if __name__== "__main__":
    main()