# rotate an array by k times optimal solution


# rotate an array by k times
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
for i in range(k):
    last = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last 
print(arr)


# third largest element 
arr = [5, 5, 5]
largest =float('-inf')
second =float('-inf')
third =float('-inf')
for num in arr:
    if num > largest:
        
        third=second
        second=largest
        largest =num
    elif num>second and num!=largest:
        third =second
        second=num
    elif num>third and num!=largest and num!=second:
        third=num
print("Third largest :",third) 

if third == float('-inf'):
    print("Third largest does not exist")
else:
    print("Third largest:", third)
