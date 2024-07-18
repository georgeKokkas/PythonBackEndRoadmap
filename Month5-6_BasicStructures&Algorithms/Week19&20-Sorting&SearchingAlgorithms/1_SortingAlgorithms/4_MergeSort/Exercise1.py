# Implement Merge Sort and test it with a list of unsorted integers.

# Concept: Merge Sort is a Divide and Conquer algorithm. It divides the input 
# array into two halves, calls itself for the two halves, and then merges the two 
# sorted halves. The merge() function is used for merging two halves. 
# The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and 
# arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Test Merge Sort
arr = [12, 11, 13, 5, 6, 7]
print("Merge Sort:", merge_sort(arr))  # Output: [5, 6, 7, 11, 12, 13]
