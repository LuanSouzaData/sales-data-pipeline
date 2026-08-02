from sales_pipeline.extract import extract_sales_data
from sales_pipeline.transform import transform_sales_data


def main() -> None:
    df = extract_sales_data()

    df = transform_sales_data(df)
    
    print("\nUnique categories:")
    print(df["category"].unique())

    print(df)
    
    print("\n" + "=" * 50)
    print("PIPELINE SUMMARY")
    print("=" * 50)

    print(f"Final records : {len(df)}")
    print(f"Columns       : {len(df.columns)}")

    print("\nColumns:")
    for column in df.columns:
        print(f" - {column}")


if __name__ == "__main__":
    main()
    
    