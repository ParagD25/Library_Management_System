import sqlite3
def connect_to_database():
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('create table if not exists book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER UNIQUE)')
    conn.commit()
    conn.close() 

def insert_in_database(title,author,year,isbn):
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('insert into book values (null,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close() 

def view_data():
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('select * from book')
    view=cur.fetchall()
    conn.close() 
    return view

def search_in_database(title='',author='',year='',isbn=''):
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('select * from book where title=? or author=? or year=? or isbn=?',(title,author,year,isbn))
    search=cur.fetchall()
    conn.close() 
    return search  

def update_record(id,title,author,year,isbn):
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('update book set title=?,author=?,year=?,isbn=? where id=?',(title,author,year,isbn,id))
    conn.commit()
    conn.close() 

def delect_record(id):
    conn=sqlite3.connect('lib_books.db')
    cur=conn.cursor()
    cur.execute('delete from book where id=?',(id,))
    conn.commit()
    conn.close() 


connect_to_database()
