# Implement Selection Sort and test it with a list of unsorted integers.

# Concept: Selection Sort divides the input list into two parts: the sublist of 
# items already sorted, which is built up from left to right at the front (left)
# of the list, and the sublist of items remaining to be sorted that occupy 
# the rest of the list. Initially, the sorted sublist is empty, and the unsorted 
# sublist is the entire input list. The algorithm proceeds by finding the smallest 
# (or largest, depending on sorting order) element from the unsorted sublist, 
# swapping it with the leftmost unsorted element, and moving the sublist 
# boundaries one element to the right.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test Selection Sort
arr = [64, 25, 12, 22, 11]
print("Selection Sort:", selection_sort(arr))  # Output: [11, 12, 22, 25, 64]
