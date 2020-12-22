import psycopg2

def create_connection():
    """
    create a database connection to SQLite database

    :return: Connnection object or None
    """
    conn = None
    try:
        conn = psycopg2.connect(
            database='store',
            user='postgres',
            password='anikmohammad',
            host='localhost',
            port='5432'
        )
    except Exception as e:
        print(e)
    
    return conn

def create_store_table(conn):
    """
    Create store table in SQLite database

    :param conn: Connection object
    """
    sql_string = """
    CREATE TABLE IF NOT EXISTS store (
        _id SERIAL PRIMARY KEY,
        item TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    """
    try:
        cur = conn.cursor()
        cur.execute(sql_string)
        conn.commit()
    except Exception as e:
        print(e)

def insert(conn, item, quantity, price):

    sql_string = """
    INSERT INTO store (item, quantity, price)
    VALUES (%s, %s, %s)
    """

    try:    
        cur = conn.cursor()
        cur.execute(sql_string, [item, quantity, price])
        conn.commit()
    except Exception as e:
        print(e)

def view(conn):
    
    sql_string = 'SELECT * FROM store'
    try:
        cur = conn.cursor()
        cur.execute(sql_string)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e)
    
    return None

def delete(conn, id):
    
    sql_string = "DELETE FROM store WHERE _id = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql_string, [id])
        conn.commit()
    except Exception as e:
        print(e)

def update(conn, id, item=None, quantity=None, price=None):

    sql_string = "UPDATE store SET"
    count = 0
    values = []

    if item is not None:
        sql_string = sql_string + " item = %s"
        values.append(item)
        count = count + 1
    if quantity is not None:
        if count > 0:
            sql_string = sql_string + ","
        sql_string = sql_string + " quantity = %s"
        values.append(quantity)
        count = count + 1
    if price is not None:
        if count > 0:
            sql_string = sql_string + ","
        sql_string = sql_string + " price = %s"
        values.append(price)
    
    sql_string = sql_string + " WHERE _id = %s"
    values.append(id)

    try:
        cur = conn.cursor()
        cur.execute(sql_string, values)
        conn.commit()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection()

    if conn is not None:
        create_store_table(conn)
        # insert(conn, 'item 1', 4, 10)
        # insert(conn, 'item 2', 8, 3)
        # delete(conn, 4)
        # update(conn, 3, quantity=5, price=11.8)
        print(view(conn))
        conn.close()
