import requests

# Lista przykładowych książek
books = [
    {
        "title": "Wiedźmin: Ostatnie życzenie",
        "author": "Andrzej Sapkowski",
        "year": 1993,
        "isbn": "9788370542104"
    },
    {
        "title": "Hobbit, czyli tam i z powrotem",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "isbn": "9780007118359"
    },
    {
        "title": "Harry Potter i Kamień Filozoficzny",
        "author": "J.K. Rowling",
        "year": 1997,
        "isbn": "9788380087480"
    },
    {
        "title": "Mistrz i Małgorzata",
        "author": "Michaił Bułhakow",
        "year": 1967,
        "isbn": "9780141180144"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "isbn": "9780451524935"
    }
]

# URL API
url = 'http://127.0.0.1:5000/books'

# Dodawanie książek do API
for book in books:
    response = requests.post(url, json=book)
    if response.status_code == 201:
        print(f'Książka dodana: {book["title"]}')
    else:
        print(f'Błąd przy dodawaniu książki: {book["title"]}, Status Code: {response.status_code}')
