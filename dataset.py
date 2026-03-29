import csv
import random


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

    # randomize the order of the data to avoid best/worst case scenarios
    random.shuffle(data)
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
