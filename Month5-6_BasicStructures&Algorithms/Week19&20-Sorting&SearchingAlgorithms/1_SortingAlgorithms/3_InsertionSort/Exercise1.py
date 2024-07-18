# Implement Insertion Sort and test it with a list of unsorted integers.

# Concept: Insertion Sort builds the final sorted array one item at a time. 
# It is much less efficient on large lists than more advanced algorithms such as 
# quicksort, heapsort, or merge sort. However, insertion sort provides several 
# advantages: simple implementation, efficient for (quite) small data sets, 
# and stable (does not change the relative order of elements with equal keys).

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test Insertion Sort
arr = [12, 11, 13, 5, 6]
print("Insertion Sort:", insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]
