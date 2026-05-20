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