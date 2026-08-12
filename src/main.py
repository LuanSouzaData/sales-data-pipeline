from sales_pipeline.database import (
    create_connection,
    initialize_database,
    close_connection,
)

from sales_pipeline.extract import extract_sales_data
from sales_pipeline.transform import transform_sales_data
from sales_pipeline.load import load_sales_data


def main():
    connection = create_connection()

    try:
        initialize_database(connection)

        df = extract_sales_data()

        df = transform_sales_data(df)

        load_sales_data(connection, df)

        print(df)

        print("\n" + "=" * 50)
        print("PIPELINE SUMMARY")
        print("=" * 50)

        print(f"Final records : {len(df)}")
        print(f"Columns       : {len(df.columns)}")

        print("\nColumns:")
        for column in df.columns:
            print(f" - {column}")

    finally:
        close_connection(connection)


if __name__ == "__main__":
    main()