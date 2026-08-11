import pandas as pd
import pytest

from sales_pipeline.load import load_sales_data


def test_load_sales_data(sqlite_connection):
    # Arrange
    df = pd.DataFrame(
        {
            "sale_id": [1, 2],
            "date": pd.to_datetime(
                ["2026-08-01", "2026-08-02"]
            ),
            "customer_name": [
                "Ana",
                "Carlos",
            ],
            "category": [
                "Books",
                "Electronics",
            ],
            "quantity": [
                2,
                1,
            ],
            "unit_price": [
                100,
                500,
            ],
            "total_price": [
                200,
                500,
            ],
        }
    )

    # Act
    load_sales_data(sqlite_connection, df)

    # Assert
    cursor = sqlite_connection.cursor()

    cursor.execute(
        """
        SELECT
            sale_id,
            customer_name,
            category,
            quantity,
            unit_price,
            total_price
        FROM sales
        ORDER BY sale_id
        """
    )

    result = cursor.fetchall()

    assert len(result) == 2

    assert result[0] == (
        1,
        "Ana",
        "Books",
        2,
        100.0,
        200.0,
    )

    assert result[1] == (
        2,
        "Carlos",
        "Electronics",
        1,
        500.0,
        500.0,
    )


def test_load_sales_data_updates_existing_sale(sqlite_connection):
    # Arrange
    first_df = pd.DataFrame(
        {
            "sale_id": [1],
            "date": pd.to_datetime(["2026-08-01"]),
            "customer_name": ["Ana"],
            "category": ["Books"],
            "quantity": [2],
            "unit_price": [100],
            "total_price": [200],
        }
    )

    updated_df = pd.DataFrame(
        {
            "sale_id": [1],
            "date": pd.to_datetime(["2026-08-02"]),
            "customer_name": ["Ana Silva"],
            "category": ["Electronics"],
            "quantity": [3],
            "unit_price": [500],
            "total_price": [1500],
        }
    )

    # Act
    load_sales_data(sqlite_connection, first_df)
    load_sales_data(sqlite_connection, updated_df)

    # Assert
    cursor = sqlite_connection.cursor()

    cursor.execute(
        """
        SELECT
            sale_id,
            date,
            customer_name,
            category,
            quantity,
            unit_price,
            total_price
        FROM sales
        WHERE sale_id = 1
        """
    )

    result = cursor.fetchone()

    assert result == (
        1,
        "2026-08-02",
        "Ana Silva",
        "Electronics",
        3,
        500.0,
        1500.0,
    )


def test_load_sales_data_rolls_back_on_error(sqlite_connection):
    # Arrange
    valid_df = pd.DataFrame(
        {
            "sale_id": [1],
            "date": pd.to_datetime(["2026-08-01"]),
            "customer_name": ["Ana"],
            "category": ["Books"],
            "quantity": [2],
            "unit_price": [100],
            "total_price": [200],
        }
    )

    invalid_df = pd.DataFrame(
        {
            "sale_id": [2],
            "date": pd.to_datetime(["2026-08-02"]),
            "customer_name": [None],
            "category": ["Books"],
            "quantity": [1],
            "unit_price": [100],
            "total_price": [100],
        }
    )

    # Act
    load_sales_data(sqlite_connection, valid_df)

    with pytest.raises(Exception):
        load_sales_data(sqlite_connection, invalid_df)

    # Assert
    cursor = sqlite_connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM sales"
    )

    result = cursor.fetchone()[0]

    assert result == 1