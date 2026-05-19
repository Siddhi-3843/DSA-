# stock price buy and Sell problem

def max_profit(prices):
    min_price = float('inf')  # start with infinity (no buy yet)
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price          # found a cheaper buy day
        elif price - min_price > max_profit:
            max_profit = price - min_price  # found a better profit

    return max_profit

# Test
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))      # 0
print(max_profit([2, 4, 1]))            # 2