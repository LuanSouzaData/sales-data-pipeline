CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    total_price REAL NOT NULL
);