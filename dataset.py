import csv

def load_data(column_name):
    data = []
    with open("diabetes_dataset.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row[column_name])
    return data
