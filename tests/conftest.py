import sqlite3

import pandas as pd
import pytest


@pytest.fixture
def sample_sales_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 2],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-01",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Carlos",
            ],
            "category": [
                "Books",
                "Books",
                "Books",
            ],
            "quantity": [
                1,
                2,
                2,
            ],
            "unit_price": [
                100,
                150,
                150,
            ],
        }
    )


@pytest.fixture
def invalid_quantity_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 3, 4],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-02",
                "2026-08-02",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Maria",
                "Lucas",
            ],
            "category": [
                "Books",
                "Books",
                "Books",
                "Books",
            ],
            "quantity": [
                1,
                0,
                -2,
                3,
            ],
            "unit_price": [
                100,
                150,
                200,
                250,
            ],
        }
    )
    
    
@pytest.fixture
def invalid_price_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 3, 4],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-02",
                "2026-08-02",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Maria",
                "Lucas",
            ],
            "category": [
                "Books",
                "Books",
                "Books",
                "Books",
            ],
            "quantity": [
                1,
                2,
                1,
                3,
            ],
            "unit_price": [
                100,
                0,
                -50,
                250,
            ],
        }
    )
    
    
@pytest.fixture
def invalid_dates_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 3, 4, 5],
            "date": [
                "2026-08-01",
                "2026-08-32",
                "abc",
                None,
                "2026-08-05",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Maria",
                "Lucas",
                "Fernanda",
            ],
            "category": [
                "Books",
                "Books",
                "Books",
                "Books",
                "Books",
            ],
            "quantity": [
                1,
                2,
                1,
                3,
                2,
            ],
            "unit_price": [
                100,
                150,
                200,
                250,
                300,
            ],
        }
    )
    
    
@pytest.fixture
def categories_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 3, 4],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-02",
                "2026-08-02",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Maria",
                "Lucas",
            ],
            "category": [
                " books ",
                "BOOKS",
                "electronics",
                " ELECTRONICS ",
            ],
            "quantity": [1, 2, 3, 4],
            "unit_price": [100, 150, 200, 250],
        }
    )
    
    
@pytest.fixture
def customer_names_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2, 3, 4],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-02",
                "2026-08-02",
            ],
            "customer_name": [
                " ana silva ",
                "CARLOS SOUZA",
                None,
                "mArIa",
            ],
            "category": [
                "Books",
                "Books",
                "Books",
                "Books",
            ],
            "quantity": [1, 2, 3, 4],
            "unit_price": [100, 150, 200, 250],
        }
    )
    
    
@pytest.fixture
def total_price_dataframe():
    return pd.DataFrame(
        {
            "sale_id": [1, 2],
            "date": [
                "2026-08-01",
                "2026-08-02",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
            ],
            "category": [
                "Books",
                "Books",
            ],
            "quantity": [
                2,
                5,
            ],
            "unit_price": [
                100,
                80,
            ],
        }
    )
    
    
@pytest.fixture
def sqlite_connection():
        connection = sqlite3.connect(":memory:")

        connection.execute(
        """
        CREATE TABLE sales (
            sale_id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL
        )
        """
    )

        yield connection

        connection.close()