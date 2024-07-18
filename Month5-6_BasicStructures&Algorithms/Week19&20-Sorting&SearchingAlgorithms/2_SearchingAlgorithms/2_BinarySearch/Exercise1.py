# Implement Binary Search and test it with a sorted list of integers and a target value.

# Concept: Binary Search is a more efficient search algorithm but requires the 
# list to be sorted. It works by repeatedly dividing the search interval in half.
# If the value of the target is less than the middle element, it narrows 
# the interval to the lower half. Otherwise, it narrows it to the upper half. 
# The process continues until the value is found or the interval is empty.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the element is found
        elif arr[mid] < target:
            left = mid + 1  # Move the left pointer to mid + 1
        else:
            right = mid - 1  # Move the right pointer to mid - 1
    return -1  # Return -1 if the element is not found

# Test Binary Search
arr = [2, 3, 4, 10, 40]
target = 10
print("Binary Search:", binary_search(arr, target))  # Output: 3
