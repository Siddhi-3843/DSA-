# plus one
arr = [1, 2, 3]
n = len(arr)
carry = True          # assume we need to add 1

for i in range(n-1, -1, -1):
    if carry:
        arr[i] += 1
        if arr[i] < 10:
            carry = False    # no more carry needed
        else:
            arr[i] = 0       # carry continues

if carry:                    # only if still remaining
    arr.insert(0, 1)

print(arr)


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
