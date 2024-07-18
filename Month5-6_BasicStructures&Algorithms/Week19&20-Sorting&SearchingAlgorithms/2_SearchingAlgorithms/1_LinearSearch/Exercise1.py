# Implement Linear Search and test it with a list of integers and a target value.

# Concept: Linear Search is the simplest search algorithm. It checks each element
# of the list until the target value is found or the list ends.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Test Linear Search
arr = [2, 3, 4, 10, 40]
target = 10
print("Linear Search:", linear_search(arr, target))  # Output: 3
