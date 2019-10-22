import sqlite3

def connect():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("Create Table if not exists books(id integer Primary key, title text, author text, year int, isbn int)")
    con.commit()
    con.close()

def insert(title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?, ?, ?, ?)",(title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books where title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id, title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
    con.commit()
    con.close()

connect()
