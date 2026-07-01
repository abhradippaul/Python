from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID not needed", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Abhradip Paul",
                "description": "A new description of a book",
                "rating": 5,
                "published_date" : 2029
            }
        }
    }

BOOKS = [
    Book(1, "Title One", "Author One", "Description One", 5, 2013),
    Book(2, "Title Two", "Author Two", "Description Two", 4, 2030),
    Book(3, "Title Three", "Author Three", "Description Three", 3, 2029),
    Book(4, "Title Four", "Author Four", "Description Four", 5, 2028),
    Book(5, "Title Five", "Author Five", "Description Five", 4, 2027),
    Book(6, "Title Six", "Author Six", "Description Six", 3, 2026)
]

def find_book_id(book: Book):
    if len(BOOKS):
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/publish", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int):
    for book in BOOKS:
        if book.rating == rating:
            return {"Book": book}
    return {"Book": None}

@app.put("/books/update_book", status_code=status.HTTP_200_OK)
async def update_book(updated_book: BookRequest):
    book_changed = False
    for book in BOOKS:
        if book.id == update_book.id:
            book = updated_book
            book_changed = True
            return {"Updated Book": book}
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return {"Book": book}
    raise HTTPException(status_code=404, detail="Item not found")