# Buy and sell stock (multiple transactions allowed)    prices = [7, 1, 5, 3, 6, 4]
prices = [7, 1, 5, 3, 6, 4]
profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:  # if current price is higher than previous
        profit += prices[i] - prices[i-1]  # add the profit from this transaction   
        

print(profit)


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