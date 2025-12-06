import sqlite3

BRANCHES = [
    "🍔 Chilonzor filiali",
    "🍕 Yunusobod filiali",
    "🌭 Sergeli filiali",
    "🍟 Mirzo Ulug'bek filiali",
    "🥤 Yakkasaroy filiali",
    "🍗 Olmazor filiali"
]


conn = sqlite3.Connection('fastfood.db')
cur = conn.cursor()


create_table_category = """
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""
create_table_product = """
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    price REAL NOT NULL,
    image_url TEXT,
    FOREIGN KEY (category_id) REFERENCES category (id)
);  
"""
create_table_user = """
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL UNIQUE,
    full_name TEXT,
    language TEXT DEFAULT 'uz'
);
"""

def create_tables():
    cur.execute(create_table_category)
    cur.execute(create_table_product)
    cur.execute(create_table_user)
    conn.commit()
    

def insert_category(name: str):
    cur.execute("INSERT INTO category (name) VALUES (?)", (name,))
    conn.commit()
    
    
def insert_product(name: str, category_id: int, price: float, image_url: str):
    cur.execute(
        "INSERT INTO product (name, category_id, price, image_url) VALUES (?, ?, ?, ?)",
        (name, category_id, price, image_url)
    )
    conn.commit()
    
def get_all_categories():
    cur.execute("SELECT * FROM category")
    return cur.fetchall()


def get_products_by_category(category_id: int):
    cur.execute("SELECT * FROM product WHERE category_id = ?", (category_id,))
    return cur.fetchall()


# get_product(product_id), delete_category(nomi), delete_product(nomi)