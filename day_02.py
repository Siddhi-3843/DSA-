# Kadane's algorithm
arr = [-3, -1, -4, -2]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    if current_sum > max_sum:
        max_sum = current_sum

print("Maximum subarray sum:", max_sum)

print("...................................")

arr = [3, 1, 4, 1, 5]
n = len(arr)

# Step 1 - create empty prefix array of same size
prefix = [0] * n
print("Empty prefix:", prefix)  # [0, 0, 0, 0, 0]

# Step 2 - fill first position manually
prefix[0] = arr[0]
print("After index 0:", prefix)  # [3, 0, 0, 0, 0]

# Step 3 - fill rest using the pattern
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
    print(f"After index {i}:", prefix)

print("Final prefix:", prefix)