import pandas as pd

from sales_pipeline.transform import remove_duplicates


def test_remove_duplicates():

    df = pd.DataFrame(
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
            "quantity": [1, 2, 2],
            "unit_price": [50, 80, 80],
        }
    )

    result = remove_duplicates(df)

    assert len(result) == 2