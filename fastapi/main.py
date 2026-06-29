from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

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
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [
    Book(1, "Title One", "Author One", "science", 4),
    Book(2, "Title Two", "Author Two", "science", 5),
    Book(3, "Title Three", "Author Three", "history", 3),
    Book(4, "Title Four", "Author Four", "math", 4),
    Book(5, "Title Five", "Author Five", "history", 5),
    Book(6, "Title Six", "Author Two", "science", 2),
]

@app.get("/books")
async def read_all_books():
    return BOOKS
        
@app.get("/books/")
async def read_book(book_category: str, book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get("category").casefold() == book_category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book")
async def update_book(new_book=Body()):
    for book,i in BOOKS:
        if new_book.casefold() == book.get("title").casefold():
            BOOKS[i] = new_book
            return new_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title):
    for i in range(len(BOOKS)):
        if book_title.casefold() == BOOKS[i].get("title").casefold():
            removed_book = BOOKS.pop(i)
            return removed_book

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        
@app.get("/books/{book_title}/")
async def read_book(book_title: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return