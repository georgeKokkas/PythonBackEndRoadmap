# Implement a dynamic programming solution for the subset sum problem.

def subset_sum(arr, target):
    n = len(arr)
    # Create a 2D array to store the results
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  # Base case: a sum of 0 can always be made with an empty subset

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

# Test Subset Sum
arr = [3, 34, 4, 12, 5, 2]
target = 9
print("Is there a subset with sum 9?", subset_sum(arr, target))  # Output: True
