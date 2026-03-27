import random
import time


def check_sort_fn(sort_fn: callable, data: list):
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
    sort_fn(data, 0, len(data) - 1)
    end_time = time.perf_counter()
    return data == expected, expected, data, end_time - start_time

def check_native_fn(data: list):
    """Run Python's native sorted() function and measure time.
    Args: 
        data: List to sort
    Returns:
        - elapsed_seconds (float): runtime in seconds.
    """
    start_time = time.perf_counter()
    sorted(data)
    end_time = time.perf_counter()
    return end_time - start_time

def merge(arr: list, left: int, mid: int, right: int) -> None:
    X = arr[left : mid + 1]
    Y = arr[mid + 1 : right + 1]
    i = j = 0
    k = left
    while i < len(X) and j < len(Y):
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1
    while i < len(X):
        arr[k] = X[i]
        i += 1
        k += 1
    while j < len(Y):
        arr[k] = Y[j]
        j += 1
        k += 1


def merge_sort(arr: list, left: int, right: int) -> None:
    """In-place merge sort.

    Sorts the subarray `arr[left:right+1]` in-place using merge sort.

    Args:

        arr: Mutable sequence to sort in-place.
        left: Inclusive left index of the subarray to sort.
        right: Inclusive right index of the subarray to sort.

    Returns:
        None
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low: int, high: int):
    """In-place optimized quicksort.

    Uses a randomized pivot and always recurses on the smaller partition
    while iterating on the larger partition to limit recursion depth.

    Args:
        arr: Mutable sequence to sort in-place.
        low: Inclusive left index of the subarray to sort.
        high: Inclusive right index of the subarray to sort.

    Returns:
        None
    """
    while low < high:
        # pick random pivot and move it to end
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        p = partition(arr, low, high)

        # sizes of left and right partitions
        left_size = p - 1 - low
        right_size = high - (p + 1)

        # recurse on smaller partition first
        if left_size < right_size:
            if low < p - 1:
                quick_sort(arr, low, p - 1)
            low = p + 1
        else:
            if p + 1 < high:
                quick_sort(arr, p + 1, high)
            high = p - 1
