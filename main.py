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
    is_correct, expected, actual, native_time = sort.check_sort_fn(sort.native_sort, data)
    print(
        f"sorted() { 'succeeded' if is_correct else 'failed' } in {native_time:.6f} seconds.\n"
    )
    print(f"Expected: {expected[:10]} ... {expected[-10:]}")
    print(f"Actual:   {actual[:10]} ... {actual[-10:]}")

    print("\nSorting using Merge Sort...\n")
    is_correct, expected, actual, merge_time = sort.check_sort_fn(sort.merge_sort, data)
    print(
        f"Merge Sort { 'succeeded' if is_correct else 'failed' } in {merge_time:.6f} seconds.\n"
    )
    print(f"Expected: {expected[:10]} ... {expected[-10:]}")
    print(f"Actual:   {actual[:10]} ... {actual[-10:]}")

    print('\nSorting using "Quick" Sort...\n')
    is_correct, expected, actual, quick_time = sort.check_sort_fn(sort.quick_sort, data)
    print(
        f"Quick Sort { 'succeeded' if is_correct else 'failed' } in {quick_time:.6f} seconds.\n"
    )
    print(f"Expected: {expected[:10]} ... {expected[-10:]}")
    print(f"Actual:   {actual[:10]} ... {actual[-10:]}")

    print("\n\n")
    if native_time < merge_time and native_time < quick_time:
        print("sorted() was the fastest!")
    elif merge_time < native_time and merge_time < quick_time:
        print("Merge Sort was the fastest!")
    elif quick_time < native_time and quick_time < merge_time:
        print("Quick Sort was the fastest!")

    print("\n")
