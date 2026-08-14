from sales_pipeline.transform import transform_sales_data
import pandas as pd
from sales_pipeline.transform import (
    remove_duplicates,
    remove_invalid_quantity,
    remove_invalid_prices,
    validate_dates,
    standardize_categories,
    normalize_customer_names,
    calculate_total_price,
)


def test_remove_duplicates(sample_sales_dataframe):
    # Arrange
    df = sample_sales_dataframe

    # Act
    result = remove_duplicates(df)

    # Assert
    assert len(result) == 2


def test_remove_invalid_quantity(invalid_quantity_dataframe):
    # Arrange
    df = invalid_quantity_dataframe

    # Act
    result = remove_invalid_quantity(df)

    # Assert
    assert (result["quantity"] > 0).all()
    assert len(result) == 2
    
    
def test_remove_invalid_prices(invalid_price_dataframe):
    # Arrange
    df = invalid_price_dataframe

    # Act
    result = remove_invalid_prices(df)

    # Assert
    assert (result["unit_price"] > 0).all()
    assert len(result) == 2
    
    
def test_validate_dates(invalid_dates_dataframe):
    # Arrange
    df = invalid_dates_dataframe

    # Act
    result = validate_dates(df)

    # Assert
    assert result["date"].isna().sum() == 0
    assert len(result) == 2
    
    
def test_standardize_categories(categories_dataframe):
    # Arrange
    df = categories_dataframe

    # Act
    result = standardize_categories(df)

    # Assert
    expected = {"Books", "Electronics"}
    assert set(result["category"].unique()) == expected
    
    
def test_normalize_customer_names(customer_names_dataframe):
    # Arrange
    df = customer_names_dataframe

    # Act
    result = normalize_customer_names(df)

    # Assert
    assert result.loc[0, "customer_name"] == "Ana Silva"
    assert result.loc[1, "customer_name"] == "Carlos Souza"
    assert result.loc[2, "customer_name"] == "Unknown"
    assert result.loc[3, "customer_name"] == "Maria"
    
    
def test_calculate_total_price(total_price_dataframe):
    # Arrange
    df = total_price_dataframe

    # Act
    result = calculate_total_price(df)

    # Assert
    assert "total_price" in result.columns
    assert result.loc[0, "total_price"] == 200
    assert result.loc[1, "total_price"] == 400
    
def test_transform_sales_data():
    # Arrange
    df = pd.DataFrame(
        {
            "sale_id": [1, 2, 2, 3],
            "date": [
                "2026-08-01",
                "2026-08-01",
                "2026-08-01",
                "invalid-date",
            ],
            "customer_name": [
                " ana silva ",
                None,
                None,
                "CARLOS SOUZA",
            ],
            "category": [
                " books ",
                "electronics",
                "electronics",
                "BOOKS",
            ],
            "quantity": [2, 1, 1, 0],
            "unit_price": [100, 500, 500, 100],
        }
    )

    # Act
    result = transform_sales_data(df)

    # Assert
    assert len(result) == 2
    assert list(result["sale_id"]) == [1, 2]

    assert result.loc[0, "customer_name"] == "Ana Silva"
    assert result.loc[1, "customer_name"] == "Unknown"

    assert result.loc[0, "category"] == "Books"
    assert result.loc[1, "category"] == "Electronics"

    assert result["date"].notna().all()

    assert result.loc[0, "total_price"] == 200
    assert result.loc[1, "total_price"] == 500    