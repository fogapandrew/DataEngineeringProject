import re

class religiousBooksTransformer:
    
    def __init__(self) -> None:
        pass
          
    def books_and_their_attributes_from_api(self, books_elements, max_books: int = 5):
        
        list_of_books_and_their_attributes = []
        for book, doc in enumerate(books_elements['docs']):
            if book >= max_books:
                break
            title = doc["title"]
            author = doc["author_name"][0]
            score = doc["ratings_average"]
            cover_id = doc["cover_i"]
            
            if cover_id:
                book_cover_url = f'http://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
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