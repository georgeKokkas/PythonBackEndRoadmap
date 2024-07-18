# Implement Bubble Sort and test it with a list of unsorted integers.

# Concept: Bubble Sort repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order. 
# The pass through the list is repeated until the list is sorted.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
