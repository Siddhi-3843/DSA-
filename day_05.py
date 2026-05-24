#missing and repeating values in an array of size n containing numbers from 1 to n

arr = arr = [1, 1]
n = len(arr)
freq = [0] * (n+1)   # index 0 unused

for num in arr:
    freq[num] += 1

missing = repeating = 0
for i in range(1, n+1):
    if freq[i] == 0:
        missing = i
    elif freq[i] == 2:
        repeating = i

print("Missing:", missing)
print("Repeating:", repeating)


#Array Leaders in an array

arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
leaders = []
max_right = arr[n-1]
leaders.append(max_right)

for i in range(n-2, -1, -1):
    if arr[i] > max_right:
        leaders.append(arr[i])
        max_right = arr[i]

leaders.reverse()
print(leaders)

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