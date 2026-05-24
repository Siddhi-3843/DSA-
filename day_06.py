arr = [1, 2, 3]
n = len(arr)
total = 0

for i in range(n):
    total += arr[i] * (i + 1) * (n - i)

print(total)


# sum of all subarrays
arr = [1, 2, 3]
total = 0

for i in range(len(arr)):
    curr_sum = 0
    for j in range(i, len(arr)):
        curr_sum += arr[j]
        total += curr_sum

print(total)



# Find missing ranges

arr = [0, 1, 3, 50, 75]
lower, upper = 0, 99
result = []

# add boundaries
nums = [lower-1] + arr + [upper+1]

for i in range(1, len(nums)):
    gap = nums[i] - nums[i-1]
    if gap == 2:
        result.append(str((nums[i-1]+1)))          # single missing
    elif gap > 2:
         result.append(str(nums[i-1] + 1) + "->" + str(nums[i] - 1))  # range missing

print(result)



# alternate positive and negatives
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

neg = [x for x in arr if x < 0]
pos = [x for x in arr if x >= 0]

result = []
i, j = 0, 0

# alternate neg and pos
while i < len(neg) and j < len(pos):
    result.append(neg[i])   # add negative
    result.append(pos[j])   # add positive
    i += 1
    j += 1

# append remaining
result += neg[i:]
result += pos[j:]


print(result)

# Reverse array in group
arr = [1, 2, 3, 4, 5]
k = 3
n = len(arr)

i = 0
while i < n:
    left = i
    right = min(i + k - 1, n - 1)  # handles last group
    
    while left < right:
        arr[left], arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    
    i +=k   # jump to next group

print(arr)


# Remove duplicates from sorted array
arr = [1, 1, 1, 1, 2]
j = 0
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:     # different from last unique
        j += 1
        arr[j] = arr[i] # place it at next position
print(j+1)
print(arr[:j+1])