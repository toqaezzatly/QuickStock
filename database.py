import sqlite3

DATABASE = 'quick_stock.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Return rows as dictionaries
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR UNIQUE NOT NULL,
                password VARCHAR NOT NULL
            )
        """)
        conn.execute("""
             CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
    print("Database initialized")


# Database Operations for Products
def db_get_all_products():
    with get_db_connection() as conn:
        rows = conn.execute('SELECT * FROM products').fetchall()
    return [dict(row) for row in rows]

def db_get_product(product_id):
  with get_db_connection() as conn:
    row = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    return dict(row) if row else None

def db_add_product(name, price, quantity):
    with get_db_connection() as conn:
        conn.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
        conn.commit()

def db_update_product(product_id, name, price, quantity):
    with get_db_connection() as conn:
        conn.execute('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?', (name, price, quantity, product_id))
        conn.commit()

def db_delete_product(product_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()

# Database Operations for Users
def db_create_user(username, password):
    with get_db_connection() as conn:
        try:
          conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
          conn.commit()
          return True
        except sqlite3.IntegrityError:
          return False
def db_get_user(username):
    with get_db_connection() as conn:
      row = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
      return dict(row) if row else None

# Initialize the database when app starts
init_db()