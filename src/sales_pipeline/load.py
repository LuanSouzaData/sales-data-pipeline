import sqlite3

import pandas as pd

from sales_pipeline.logger import setup_logger

logger = setup_logger()

# ==========================
# SQL Statements
# ==========================

INSERT_SALES_SQL = """
INSERT INTO sales (
    sale_id,
    date,
    customer_name,
    category,
    quantity,
    unit_price,
    total_price
)
VALUES (?, ?, ?, ?, ?, ?, ?)

ON CONFLICT(sale_id)
DO UPDATE SET
    date = excluded.date,
    customer_name = excluded.customer_name,
    category = excluded.category,
    quantity = excluded.quantity,
    unit_price = excluded.unit_price,
    total_price = excluded.total_price;
"""


def dataframe_to_records(df: pd.DataFrame) -> list[tuple]:
    """
    Convert a DataFrame into a list of tuples
    ready for SQLite insertion.
    """

    dataframe = df.copy()

    dataframe["date"] = dataframe["date"].dt.strftime("%Y-%m-%d")

    records = list(
        dataframe.itertuples(
            index=False,
            name=None
        )
    )

    return records


def load_sales_data(
    connection: sqlite3.Connection,
    df: pd.DataFrame
) -> None:
    """
    Load transformed sales data into SQLite.
    """

    cursor = connection.cursor()

    records = dataframe_to_records(df)

    logger.info(
        f"Loading {len(records)} record(s) into SQLite..."
    )

    try:

        cursor.executemany(
            INSERT_SALES_SQL,
            records
        )

        connection.commit()

        logger.info(
            f"{len(records)} record(s) loaded successfully."
        )

    except sqlite3.Error:

        connection.rollback()

        logger.exception(
            "Failed to load records into SQLite."
        )

        raise

    finally:

        cursor.close()