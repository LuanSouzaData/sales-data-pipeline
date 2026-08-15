import pandas as pd

from sales_pipeline.logger import setup_logger

logger = setup_logger()


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicated sales based on the sale_id column.
    """
    df = df.copy()
    original_rows = len(df)

    df = df.drop_duplicates(subset=["sale_id"])

    removed_rows = original_rows - len(df)

    logger.info("Removed %s duplicated record(s).", removed_rows)

    return df

def remove_invalid_quantity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove records with quantity less than or equal to zero.
    """
    df = df.copy()
    original_rows = len(df)

    df = df[df["quantity"] > 0]

    removed_rows = original_rows - len(df)

    logger.info(
        "Removed %s record(s) with invalid quantity.",
        removed_rows,
    )

    return df

def remove_invalid_prices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove records with unit_price less than or equal to zero.
    """
    df = df.copy()
    original_rows = len(df)

    df = df[df["unit_price"] > 0]

    removed_rows = original_rows - len(df)

    logger.info(
        "Removed %s record(s) with invalid price.",
        removed_rows,
    )

    return df

def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all implemented data quality rules.
    """
    
    df = remove_duplicates(df)
    df = remove_invalid_quantity(df)
    df = remove_invalid_prices(df)
    df = validate_dates(df)
    df = standardize_categories(df)
    df = normalize_customer_names(df)
    df = calculate_total_price(df)
    
    logger.info(
        "Transformation completed. %s record(s) remaining.",
        len(df),
    )
    return df

def validate_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and convert the date column.
    Invalid dates are removed.
    """
    df = df.copy()
    original_rows = len(df)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce",
    )

    df = df.dropna(subset=["date"])

    removed_rows = original_rows - len(df)

    logger.info(
        "Removed %s record(s) with invalid dates.",
        removed_rows,
    )

    return df

def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize category names.
    """

    df = df.copy()

    df["category"] = (
        df["category"]
        .str.strip()
        .str.lower()
    )

    category_mapping = {
        "electronics": "Electronics",
        "eletronicos": "Electronics",
        "books": "Books",
    }

    df["category"] = df["category"].replace(category_mapping)

    logger.info("Categories standardized successfully.")

    return df

def normalize_customer_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize customer names by removing extra spaces.
    """

    df = df.copy()

    original_nulls = df["customer_name"].isna().sum()

    df["customer_name"] = (
        df["customer_name"]
        .fillna("Unknown")
        .str.strip()
        .str.title()
    )

    logger.info(
        "Normalized customer names. Missing names filled: %s.",
        original_nulls,
    )

    return df

def calculate_total_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the total price for each sale.
    """

    df = df.copy()

    df["total_price"] = (
        df["quantity"] * df["unit_price"]
    )

    logger.info(
        "Transformation completed. %s record(s) remaining.",
        len(df),
    )

    return df