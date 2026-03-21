# see "Sorting" lecture slides, slide 90
# helper function to merge together the subarrays
# in python both arrays and lists are mutable objects. In our implementation the dataset is passed in as a list.
# see "Sorting" lecture slides, slide 90
def merge(arr:list, left:int, mid:int, right:int):
    n1 = mid - left + 1
    n2 = right - mid
    # lists are mutable and we don't specify the container's size
    X, Y = [], []
    [X.append(arr[left + i]) for i in range(n1)]
    [Y.append(arr[mid + 1 + j]) for j in range(n2)]
    # merge the arrays X and Y into arr
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1
    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        arr[k] = X[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = Y[j]
        j += 1
        k += 1

# algorithm from sorting review slides and lecture slides (slide 89) 
# merge sort takes in a one-dimensional array and returns the sorted one-dimension array
def merge_sort(arr, left, right):
   if left < right:
        # python does not automatically recognize left and right as integers. We need to round down the expression. Example: if mid is 1.5,
        # in merge_sort implemented in C++ this would give a mid value of 1.
        # so cast as an int: https://stackoverflow.com/questions/17141979/round-a-floating-point-number-down-to-the-nearest-integer
        mid = left + int((right - left) / 2) 
        # divide arr into subarrays
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # merge the sorted subarrays
        arr = merge(arr, left, mid, right)

def partition(arr, low, high) -> int:
    pivot = arr[low]
    up, down = low, high
    while up < down:
        for j in range(up, high):
            if arr[up] > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if arr[down] < pivot:
                break
            down -= 1
        if up < down:
            # equivalent to C++ swap()
            t = arr[up]
            arr[up] = arr[down]
            arr[down] = t   
    t = arr[low]
    arr[low] = arr[down]
    arr[down] = t
    return down

def quick_sort(arr:list, low:int, high:int):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)