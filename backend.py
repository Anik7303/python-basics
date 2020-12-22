import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except Exception as e:
        print(e)
    return conn

def execute_sql(sql_string, variables=[], single=False):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(sql_string, variables)
        result = None
        if single:
            result = cur.fetchone()
        else:
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
    except Exception as e:
        print(e)

def create_table():

    sql_string = """
    CREATE TABLE IF NOT EXISTS books(
        _id INTEGER PRIMARY KEY,
        title CHAR(100) NOT NULL,
        author CHAR(40) NOT NULL,
        year INTEGER NOT NULL,
        isbn CHAR(30) NOT NULL
    )
    """
    return execute_sql(sql_string)

def drop_table():

    sql_string = "DROP TABLE books"
    return execute_sql(sql_string)

def insert(title, author, year, isbn):

    sql_string = """
    INSERT INTO books (title, author, year, isbn)
    VALUES (?, ?, ?, ?)
    """
    return execute_sql(sql_string, [title, author, year, isbn])

def search(title = "", author = "", year = "", isbn = ""):

    sql_string = """
    SELECT * FROM books WHERE
        title = ? OR
        author = ? OR
        year = ? OR
        isbn = ?
    """
    return execute_sql(sql_string, [title, author, year, isbn])

def view(id):

    sql_string = "SELECT * FROM books WHERE _id = ?"
    return execute_sql(sql_string, [id], True)

def viewall():
    
    sql_string = "SELECT * FROM books"
    return execute_sql(sql_string)

def delete(id):

    sql_string = "DELETE FROM books WHERE _id = ?"
    return execute_sql(sql_string, [id])

def update(id, title = None, author = None, year = None, isbn = None):

    sql_string = """
    UPDATE books
    SET
        title = ?,
        author = ?,
        year = ?,
        isbn = ?
    WHERE _id = ?
    """
    return execute_sql(sql_string, [title, author, year, isbn, id])

if __name__ == '__main__':
    # conn = create_connection()
    # create_table()
    # insert('title 4', 'author 2', 1999, '2344623')
    # delete(5)
    # print(view(4))
    # update(3, author="author 2", year=2003)
    print(viewall())
    # drop_table()
    # conn.close()
