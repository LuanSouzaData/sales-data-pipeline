import pandas as pd
import pytest

from sales_pipeline.extract import extract_sales_data


def test_extract_sales_data(monkeypatch, tmp_path):
    # Arrange
    first_csv = tmp_path / "sales_01.csv"
    second_csv = tmp_path / "sales_02.csv"

    first_csv.write_text(
        """sale_id,date,customer_name,category,quantity,unit_price
1,2026-08-01,Ana,Books,2,100
2,2026-08-01,Carlos,Books,1,150
"""
    )

    second_csv.write_text(
        """sale_id,date,customer_name,category,quantity,unit_price
3,2026-08-02,Maria,Electronics,1,500
"""
    )

    monkeypatch.setattr(
        "sales_pipeline.extract.RAW_DATA_DIR",
        tmp_path,
    )

    # Act
    result = extract_sales_data()

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
    assert list(result["sale_id"]) == [1, 2, 3]


def test_extract_sales_data_without_csv(monkeypatch, tmp_path):
    # Arrange
    monkeypatch.setattr(
        "sales_pipeline.extract.RAW_DATA_DIR",
        tmp_path,
    )

    # Act / Assert
    with pytest.raises(FileNotFoundError):
        extract_sales_data()
