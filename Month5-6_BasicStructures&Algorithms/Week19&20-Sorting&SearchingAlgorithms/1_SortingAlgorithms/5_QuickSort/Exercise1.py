# Implement Quick Sort and test it with a list of unsorted integers.

# Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot 
# and partitions the given array around the picked pivot. There are many 
# different versions of quicksort that pick pivot in different ways:

    # 1) Always pick the first element as a pivot.
    # 2) Always pick the last element as a pivot (implemented here).
    # 3) Pick a random element as a pivot.
    # 4) Pick the median as the pivot.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) - 1]  # Choosing the last element as pivot
        left = [x for x in arr[:-1] if x <= pivot]  # All elements less than or equal to pivot
        right = [x for x in arr[:-1] if x > pivot]  # All elements greater than pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

# Test Quick Sort
arr = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quick_sort(arr))  # Output: [1, 5, 7, 8, 9, 10]
