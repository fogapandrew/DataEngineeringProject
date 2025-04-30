import requests
from bs4 import BeautifulSoup
import json
import time 
#from MyApp.utils import *


class religiousBookExtractor:
    
    def __init__(self) -> str:
        
        self.apiurl = "https://openlibrary.org/search.json?q=religion"
        self.weburl = "https://www.goodreads.com/shelf/show/christian-info"
        self.headers =  {
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
                   }
        
        
    
    def fetch_religious_books_method_one(self) -> list:
        
        religious_books= requests.get(self.apiurl)
        if religious_books.status_code != 200:
            raise Exception(f"failed to fetch from api : {religious_books.status_code}")
        books_elements = religious_books.json()
        return books_elements
       
       
    def fetch_religious_books_method_two(self) -> list:
        
        religious_books_list = requests.get(url=self.weburl, headers=self.headers)
        if religious_books_list.status_code != 200:
            raise Exception(f"failed to fetch from webpage : {religious_books_list.status_code}")
        
        religious_books_html = BeautifulSoup(religious_books_list.content, "html.parser")
        religious_books_html = religious_books_html.find("div", class_ = "leftContainer")
        religious_books_html = religious_books_html.find_all("div", class_ = "elementList")
        
        return religious_books_html


class harrypoterbookextractor :

    def __init__(self) -> str:
        self.api_key = 'AIzaSyDzG4PL_TUH_TV1pVvkkLDiMu5vO_N9iAo' 
        self.query = "harry potter"
        self.max_results = 40
        self.total_books_needed = 100
        self.bookapiurl = " "

    def fetchstephenbooks(self) -> list:

        for start in range(0, self.total_books_needed, self.max_results):
            self.bookapiurl = f"https://www.googleapis.com/books/v1/volumes?q={self.query}&startIndex={start}&maxResults={self.max_results}&key={self.api_key}"
            response = requests.get(self.bookapiurl)

        if response.status_code != 200:
            print(f"failed to fetch from api : {response.status_code}")
        else:
            data = response.text
            books = json.loads(data)

        return books    
    

class readanybookextractor:
    def __init__(self):
        self.bookapiurl = "https://www.readanybook.online/"

    def fetchreadanybook(self):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(self.bookapiurl)
                if response.status_code == 436:
                    raise requests.exceptions.RequestException(f"Custom status code 436 received from {self.bookapiurl}")
                response.raise_for_status()
                soup = BeautifulSoup(response.text, features="html.parser")
                return soup
            except requests.exceptions.RequestException as e:
                print(f"Error fetching books from ReadAnyBook: {e}")
                if attempt < max_retries - 1:
                    print("Retrying...")
                    time.sleep(2)  # Wait for 2 seconds before retrying
                else:
                    print("Max retries reached. Returning empty list.")
                    return BeautifulSoup("", features="html.parser")

