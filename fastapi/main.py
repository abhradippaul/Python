from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

BOOKS = [
    Book(1, "Title One", "Author One", "Description One", 5),
    Book(2, "Title Two", "Author Two", "Description Two", 4),
    Book(3, "Title Three", "Author Three", "Description Three", 3),
    Book(4, "Title Four", "Author Four", "Description Four", 5),
    Book(5, "Title Five", "Author Five", "Description Five", 4),
    Book(6, "Title Six", "Author Six", "Description Six", 3)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/books/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)

@app.get("/books/{dynamic_param}")
async def get_book(dynamic_param=""):
    for book in BOOKS:
        if book["title"].casefold() == dynamic_param.casefold():
            return {"Book": book}
    return {"Book": None}

@app.put("/books/{dynamic_param}")
async def update_book(updated_book, dynamic_param=""):
    for book in BOOKS:
        if book["title"].casefold() == dynamic_param.casefold():
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            book["category"] = updated_book["category"]
            print(BOOKS)
            return {"Updated Book": book}
    return {"Book": None}
