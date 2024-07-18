# Given an amount and a set of coin denominations, find the minimum number of 
# coins needed to make the amount.

# Concept: Greedy algorithms build up a solution piece by piece, always choosing 
# the next piece that offers the most immediate benefit. They do not always produce 
# the optimal solution, but they are easy to implement and often yield good results.

def min_coins(coins, amount):
    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    count = 0  # Initialize the count of coins
    for coin in coins:
        # While the coin can be used (coin value is less than or equal to the remaining amount)
        while amount >= coin:
            amount -= coin  # Reduce the amount by the coin value
            count += 1  # Increase the count of coins used
    
    # Return the total count of coins used
    return count if amount == 0 else -1  # Return -1 if the amount cannot be made with the given coins

# Test Minimum Number of Coins
coins = [1, 5, 10, 25]
amount = 30
print("Minimum number of coins needed:", min_coins(coins, amount))  # Output: 2 (25 + 5)
