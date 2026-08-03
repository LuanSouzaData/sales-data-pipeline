from pathlib import Path
import sqlite3

from sales_pipeline.config import DATABASE_PATH, SCHEMA_PATH
from sales_pipeline.logger import setup_logger

logger = setup_logger()


def create_connection() -> sqlite3.Connection:
    """
    Create a connection to the SQLite database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    logger.info("Connected to SQLite database.")

    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    """
    Create database tables using the SQL schema file.
    """

    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        schema = schema_file.read()

    connection.executescript(schema)
    connection.commit()

    logger.info("Database initialized successfully.")


def close_connection(connection: sqlite3.Connection) -> None:
    """
    Close the SQLite database connection.
    """

    connection.close()

    logger.info("SQLite connection closed.")