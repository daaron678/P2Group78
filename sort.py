import random
import time


def check_sort_fn(sort_fn: callable, data: list) -> tuple[bool, list, list, float]:
    """Run a sorting function, verify correctness, and measure time.

    The provided `sort_fn` must sort `data` in-place and accept the
    signature `sort_fn(data, 0, len(data)-1)`.

    Args:
        sort_fn: Callable that sorts `data` in-place.
        data: List to sort (modified in-place).

    Returns:
        A tuple `(is_correct, expected, actual, elapsed_seconds)` where:
            - is_correct (bool): True if `actual == expected`.
            - expected (list): reference-sorted list (using `sorted()`).
            - actual (list): the list after calling `sort_fn`.
            - elapsed_seconds (float): runtime in seconds.
    """
    expected = sorted(data)
    start_time = time.perf_counter()
    sort_fn(data)
    end_time = time.perf_counter()
    return data == expected, expected, data, end_time - start_time


def merge(arr: list, left: int, mid: int, right: int) -> None:
    # create temporary arrays for the left and right halves
    X = arr[left : mid + 1]
    Y = arr[mid + 1 : right + 1]
    i = j = 0
    k = left

    # set up pointers for X and Y and compare the smallest elements of each half to copy back into the original array
    while i < len(X) and j < len(Y):
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1

    # once one half is fully copied, copy the remaining elements of the other half (if any)
    while i < len(X):
        arr[k] = X[i]
        i += 1
        k += 1
    while j < len(Y):
        arr[k] = Y[j]
        j += 1
        k += 1


def merge_sort(arr: list, left: int = 0, right: int = None) -> None:
    """In-place merge sort.

    Sorts the subarray `arr[left:right+1]` in-place using merge sort.

    Args:

        arr: Mutable sequence to sort in-place.
        left: Inclusive left index of the subarray to sort.
        right: Inclusive right index of the subarray to sort.

    Returns:
        None
    """
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2  # find the middle
        merge_sort(arr, left, mid)  # call left half
        merge_sort(arr, mid + 1, right)  # call right half
        merge(arr, left, mid, right)  # merge the sorted halves


def partition(arr: list, low: int, high: int) -> int:
    # Hoare partition scheme using the first element as the pivot and two pointers that move towards each other
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # move the left pointer right
        i += 1
        while arr[i] < pivot:
            i += 1

        # move the right pointer left
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # if pointers meet, return the division point
        if i >= j:
            return j

        # swap elements at the pointers
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list, low: int = 0, high: int = None):
    """In-place quicksort.

    Uses a randomized pivot and always recurses on the smaller partition
    while iterating on the larger partition to limit recursion depth.

    Args:
        arr: Mutable sequence to sort in-place.
        low: Inclusive left index of the subarray to sort.
        high: Inclusive right index of the subarray to sort.

    Returns:
        None
    """
    if high is None:
        high = len(arr) - 1

    while low < high:
        # select a random pivot and move it to the front
        pivot_idx = random.randint(low, high)
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]

        p = partition(arr, low, high)

        left_size = p - low + 1
        right_size = high - p

        # recurse on the smaller partition to minimize calls and loop to process the larger partition
        if left_size < right_size:
            quick_sort(arr, low, p)
            low = p + 1  # loops to do right side
        else:
            quick_sort(arr, p + 1, high)
            high = p  # loops to do left side


def native_sort(arr: list) -> None:
    """Sort using Python's built-in sorted() function.

    This is not truly in-place since sorted() returns a new list, but we
    copy the sorted result back into the original list to allow for
    consistent timing and comparison.

    Args:
        arr: List to sort (modified in-place).
    """
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]
