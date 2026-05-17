# wave array
arr = [3, 6, 5, 10, 7, 20]
n = len(arr)

for i in range(0, n, 2):    # even indexes only
    
    if i > 0 and arr[i] < arr[i-1]:     
        arr[i], arr[i-1] = arr[i-1], arr[i]
    
    if i < n-1 and arr[i] < arr[i+1]:    
        arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)



# move all zeros to end
arr = [0, 1, 0, 3, 12]
j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)      
