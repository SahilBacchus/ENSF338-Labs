# Exercise 1.1
def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    # create temporary arrays
    # slice arr from index low to mid inclusively
    left = arr[low: mid + 1]
    # slice arr from index mid + 1 to high inclusively
    right = arr[mid + 1: high + 1]

    # declare and instantiate indices to traverse temp arrays
    # left arr index
    i = 0
    # right arr index
    j = 0
    # merged arr index
    k = low

    # loop through left and right temps simultaneously
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # copies remaining elements after one of the halves is exhausted
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
