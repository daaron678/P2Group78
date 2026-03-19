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

    print("\n\nSorting using Merge Sort...")
    start_time = time.perf_counter()
    sort.merge_sort(data.copy())
    end_time = time.perf_counter()

    ms_time = end_time - start_time

    print(f"Merge Sort completed in {ms_time:.6f} seconds.\n")

    print("Sorting using Quick Sort...")
    start_time = time.perf_counter()
    sort.quick_sort(data.copy())
    end_time = time.perf_counter()

    qs_time = end_time - start_time
    print(f"Quick Sort completed in {qs_time:.6f} seconds.\n")

    if ms_time < qs_time:
        print("Merge Sort was faster.")
    else:
        print("Quick Sort was faster.")

    print("\n")
