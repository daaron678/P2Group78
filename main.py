import dataset
import terminal
import sort

if __name__ == "__main__":
    selection = terminal.select_from_list(
        dataset.get_column_names(), "Which column would you like to sort?"
    )
    data = dataset.load_data(selection)

    print(f"\nSorting the '{selection}' column...")

    print("\nSorting using sorted()...\n")
    ms_time = sort.check_native_fn(data)
    print(
        f"sorted() succeeded in {ms_time:.6f} seconds..\n"
    )

    print("\nSorting using Merge Sort...\n")
    is_correct, expected, actual, ms_time = sort.check_sort_fn(sort.merge_sort, data)
    print(
        f"Merge Sort { 'succeeded' if is_correct else 'failed' } in {ms_time:.6f} seconds.\n"
    )
    print(f"Expected: {expected[:10]} ... {expected[-10:]}")
    print(f"Actual:   {actual[:10]} ... {actual[-10:]}")

    print('\nSorting using "Quick" Sort...\n')
    is_correct, expected, actual, qs_time = sort.check_sort_fn(sort.quick_sort, data)
    print(
        f"Quick Sort { 'succeeded' if is_correct else 'failed' } in {qs_time:.6f} seconds.\n"
    )
    print(f"Expected: {expected[:10]} ... {expected[-10:]}")
    print(f"Actual:   {actual[:10]} ... {actual[-10:]}")

    print("\n\n")
    if ms_time < qs_time:
        print("Merge Sort was faster.")
    else:
        print("Quick Sort was faster.")

    print("\n")
