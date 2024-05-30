from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = sqlite3.connect('library.db')
    return conn

@app.route('/books', methods=['GET'])
def get_books():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    
    book_list = []
    for book in books:
        book_list.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "year": book[3],
            "isbn": book[4]
        })
    return jsonify(book_list)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id=?", (id,))
    book = cursor.fetchone()
    conn.close()
    
    if book:
        return jsonify({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "year": book[3],
            "isbn": book[4]
        })
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    title = new_book["title"]
    author = new_book["author"]
    year = new_book["year"]
    isbn = new_book["isbn"]
    
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                   (title, author, year, isbn))
    conn.commit()
    conn.close()
    
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.get_json()
    title = updated_book["title"]
    author = updated_book["author"]
    year = updated_book["year"]
    isbn = updated_book["isbn"]
    
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, id))
    conn.commit()
    conn.close()
    
    return jsonify(updated_book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
