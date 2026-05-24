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