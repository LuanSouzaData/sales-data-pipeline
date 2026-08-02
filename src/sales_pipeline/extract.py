from pathlib import Path

import pandas as pd

from sales_pipeline.config import RAW_DATA_DIR
from sales_pipeline.logger import setup_logger

logger = setup_logger()


def extract_sales_data() -> pd.DataFrame:
    """
    Reads all CSV files from the raw data directory
    and returns a single DataFrame.
    """

    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_DATA_DIR}"
        )

    logger.info("Found %s CSV file(s).", len(csv_files))

    dataframes = []

    for file in csv_files:
        logger.info("Reading file: %s", file.name)

        df = pd.read_csv(file)

        dataframes.append(df)

    final_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    logger.info(
        "Total records loaded: %s",
        len(final_df)
    )

    return final_df