import sqlite3

class Database(object):
    def __init__(self, db_name):
        sql_string = """
        CREATE TABLE IF NOT EXISTS books(
            _id INTEGER PRIMARY KEY,
            title CHAR(100) NOT NULL,
            author CHAR(40) NOT NULL,
            year INTEGER NOT NULL,
            isbn CHAR(30) NOT NULL
        )
        """
        try:
            self.conn = sqlite3.connect(db_name)
            self.cur = self.conn.cursor()
            self.cur.execute(sql_string)
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def drop_table(self, table_name):
        sql_string = "DROP TABLE ?"
        try:
            self.cur.execute(sql_string, [table_name])
            self.conn.commit()
        except Exception as e:
            print(e)

    def insert(self, title, author, year, isbn):
        sql_string = """
        INSERT INTO books (title, author, year, isbn)
        VALUES (?, ?, ?, ?)
        """
        try:
            self.cur.execute(sql_string, [title, author, year, isbn])
            self.conn.commit()
        except Exception as e:
            print(e)

    def search(self, title = "", author = "", year = "", isbn = ""):
        sql_string = """
        SELECT * FROM books WHERE
            title = ? OR
            author = ? OR
            year = ? OR
            isbn = ?
        """
        try:
            self.cur.execute(sql_string, [title, author, year, isbn])
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def view(self, id):
        sql_string = "SELECT * FROM books WHERE _id = ?"
        try:
            self.cur.execute(sql_string, [id], True)
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def viewall(self, ):
        sql_string = "SELECT * FROM books"
        try:
            self.cur.execute(sql_string)
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def delete(self, id):
        sql_string = "DELETE FROM books WHERE _id = ?"
        try:
            self.cur.execute(sql_string, [id])
            self.conn.commit()
        except Exception as e:
            print(e)

    def update(self, id, title = None, author = None, year = None, isbn = None):
        sql_string = """
        UPDATE books
        SET
            title = ?,
            author = ?,
            year = ?,
            isbn = ?
        WHERE _id = ?
        """
        try:
            self.cur.execute(sql_string, [title, author, year, isbn, id])
            self.conn.commit()
        except Exception as e:
            print(e)

    def __del__(self):
        self.conn.close()

