# helper function to merge together the subarrays
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    X, Y = [], []
    [X.append(arr[left + i]) for i in range(n1)]
    [Y.append(arr[mid + 1 + j]) for j in range(n2)]
    # merge the arrays X and Y into arr
    i, j, k = 0, 0, left
    while i < n1 & j < n2:
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

def merge_sort(arr, left, right):
   if left < right:
        mid = left + round((right - left) / 2) # python does not automatically recognize end and start as integers
        # divide arr into subarrays
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # merge the sorted subarrays
        merge(arr, left, mid, right)

def quick_sort(arr):
    pass