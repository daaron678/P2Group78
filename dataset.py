import csv


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
            data.append(row[column_name])
    return data


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
