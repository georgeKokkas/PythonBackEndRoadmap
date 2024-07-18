# Implement a dynamic programming solution for the longest common subsequence problem.

# Concept: Dynamic Programming (DP) is an optimization technique that solves 
# problems by breaking them down into simpler sub-problems and storing the 
# results of these sub-problems to avoid redundant computations.

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    # Create a 2D array to store the lengths of longest common subsequence
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Test Longest Common Subsequence
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS:", longest_common_subsequence(X, Y))  # Output: 4
