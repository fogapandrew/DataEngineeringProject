import re
from PIL import Image
import random
from io import BytesIO
import requests


class religiousBooksTransformer:
    
    def __init__(self) -> None:
        pass
          
    def books_and_their_attributes_from_api(self, books_elements, max_books: int = 5):
        
        list_of_books_and_their_attributes = []
        for book, doc in enumerate(books_elements['docs']):
            if book >= max_books:
                break
            title = str(doc["title"])
            author = str(doc["author_name"][0])
            score = float(doc["ratings_average"])
            cover_id = doc["cover_i"]
            
            if cover_id:
                book_cover_url = str(f'http://covers.openlibrary.org/b/id/{cover_id}-L.jpg')
            else:
                book_cover_url = 'No Cover Available'
            
            list_of_books_and_their_attributes.append([title, author, score, book_cover_url])
            
        return list_of_books_and_their_attributes
    
    
    def books_and_their_attributes_from_webpage(self, religious_books_html):
        
        religious_books=[]
        for attributes in religious_books_html:
            image_tag = attributes.find("img")
            title = image_tag.attrs["alt"]
            book_cover_url = image_tag.attrs["src"]
                    
        author_tag = attributes.find("a", class_="authorName")
        author = author_tag.text
        rating_tag = attributes.find("span", class_="greyText smallText").text
        pattern = r'avg rating\s+([0-9.]+)'
        match = re.search(pattern, rating_tag, re.IGNORECASE)  
        score = float(match.group(1)) if match else None           # get the first number after the pattern

        religious_books.append([title, author, score, book_cover_url])

        return religious_books
    


class harrypoterbooktransformer:
    def __init__(self) -> None:
        pass    

    def get_all_harryporterbook(self , harrypotterextrated):

        all_harry_books = []
        for book in harrypotterextrated:
            image = Image.open(requests.get(book["cover"], stream=True).raw)
            
            all_harry_books.append([book["number"] , book["title"], book["releaseDate"] , book["description"], image])

        return all_harry_books
        

class readanybooktransformer:

    def __init__(self) -> None:
        pass

    def get_all_readanybook(self , readanybookextrated):

        book_entries = readanybookextrated.find_all('a', class_='link')

        all_authors = []
        all_ratings = []
        book_images = [] 
        book_titles = []
        
        all_readany_books = []  

        for entry in book_entries:
            title = entry.get('title')  
            img_tag = entry.find('img')  
            img_src = img_tag.get('data-src') if img_tag else None  
            book_images.append(str(img_src))
            book_titles.append(str(title))   


        
        author_entries = readanybookextrated.find_all('span', class_='list')

        for author_data in author_entries:
            author_tag = author_data.find('a')
            author = author_tag.get('title')
            author.split(' ', 1)
            all_authors.append(str(author.split(' ', 1)[1]))

        book_ratings = readanybookextrated.find_all('div', class_='preview-rate')

        for b_ratings in book_ratings:
            ratings = b_ratings.find('b')
            book_rating = ratings.text
            all_ratings.append(float(book_rating))

        min_len = min(len(book_images), len(book_titles), len(all_authors), len(book_ratings))

        # Truncate each list to the minimum length
        book_image = book_images[:min_len]
        book_title = book_titles[:min_len]
        all_author = all_authors[:min_len]
        all_rating = all_ratings[:min_len]

        all_readany_books.append([book_title, all_author, all_rating , book_image])

    

        return all_readany_books