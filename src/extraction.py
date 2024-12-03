import re
import requests
from io import BytesIO  
from PIL import Image
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
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




    