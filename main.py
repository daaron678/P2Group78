import time

import dataset
import terminal
import sort

if __name__ == "__main__":
    columns = [
        column
        for column in dataset.get_column_names()
        if not column.startswith("race:")
    ]
    selection = terminal.select_from_list(
        columns, "Which column would you like to sort?"
    )
    data = dataset.load_data(selection)

    # note that each column is represented as a string. (ex. "2" instead of 2)

    # in dataset, certain ages are represented as floats which is not needed. We will change the data type to int.
    if selection in ("age"):
        # cannot map string representing float to int, so first map as float
        data = list(map(float, data))
        data = list(map(int, data))

    # the following columns take data as floats represented as strings
    if selection in ("bmi", "hbA1c_level"):
        pass

    print("Sorting using Quick Sort...")
    start_time = time.perf_counter()
    sort.quick_sort(data, 0, len(data) -1)
    end_time = time.perf_counter()

    qs_time = end_time - start_time
    print(f"Quick Sort completed in {qs_time:.6f} seconds.\n")

    print("\n\nSorting using Merge Sort...")
    start_time = time.perf_counter()
    # pass in array, left index, right index
    sort.merge_sort(data, 0, len(data) -1)
    end_time = time.perf_counter()

    ms_time = end_time - start_time

    print(f"Merge Sort completed in {ms_time:.6f} seconds.\n")


    if ms_time < qs_time:
        print("Merge Sort was faster.")
    else:
        print("Quick Sort was faster.")

    print("\n")
