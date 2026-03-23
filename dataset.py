import csv
import pandas as pd

def load_data(column_name, csv_path="diabetes_dataset.csv"):
    """Load all values from a single column in the CSV file.

    Args:
        column_name: The name of the column to load values from.
        csv_path: Optional path to the CSV file.

    Returns:
        A list of values for the requested column.
    """
    data = []
    with open(csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw = row[column_name]

            # weed out empty/null values
            if raw is None:
                data.append(None)
                continue
            value = raw.strip()
            if value == "":
                data.append(None)
                continue

            # try to convert to numeric type if possible, otherwise keep as string
            try:
                f = float(value)
                if f.is_integer():
                    data.append(int(f))
                else:
                    data.append(f)
            except ValueError:
                data.append(value)
    return data

def load_data_cat(column_name, csv_path="diabetes_dataset.csv"):
    """Load all values from a single categorical column in the CSV file.
    This function coverts the categorical column of data into numeric 
    representation for a faster execution time using the sorting algorithms.

    Returns:
        A list of values for the requested column
        A list of numeric values representing categories in the column,
        A dictionary mapping numeric codes (keys) to string representation of category (vals).
    """
    data = load_data(column_name, csv_path)
    # sorting by categories of strings is computationally expensive for quick_sort (3 minutes for gender)
    data_cat = pd.Categorical(data)
    codes = list(map(int, data_cat.codes))
    codes_map = {}
    for index, cat in enumerate(data_cat.categories):
        codes_map[index] = cat
    return data, codes, codes_map



def get_column_names(csv_path="diabetes_dataset.csv"):
    """Return the list of column names from the CSV file header.

    Args:
        csv_path: Optional path to the CSV file.

    Returns:
        A list of column names (strings) in the file.
    """
    with open(csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return reader.fieldnames or []
