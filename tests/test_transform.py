from sales_pipeline.transform import remove_duplicates


def test_remove_duplicates(sample_sales_dataframe):

    result = remove_duplicates(sample_sales_dataframe)

    assert len(result) == 4