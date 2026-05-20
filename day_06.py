# Remove duplicates from sorted array
arr = [1, 1, 1, 1, 2]
j = 0
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:     # different from last unique
        j += 1
        arr[j] = arr[i] # place it at next position
print(j+1)
print(arr[:j+1])