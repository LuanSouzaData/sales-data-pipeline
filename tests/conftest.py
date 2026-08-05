import pandas as pd
import pytest


@pytest.fixture
def sample_sales_dataframe():
    """
    Sample DataFrame used across unit tests.
    """

    return pd.DataFrame(
        {
            "sale_id": [1, 2, 2, 3, 4],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-01",
                "2026-08-02",
                "2026-08-03",
            ],
            "customer_name": [
                "Ana",
                "Carlos",
                "Carlos",
                "Maria",
                None,
            ],
            "category": [
                "Books",
                "books",
                "books",
                "ELECTRONICS",
                "electronics",
            ],
            "quantity": [
                1,
                2,
                2,
                1,
                0,
            ],
            "unit_price": [
                50,
                80,
                80,
                300,
                -10,
            ],
        }
    )