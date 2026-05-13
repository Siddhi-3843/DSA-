#Find Largest and second largest number of array 
a=[5, 4, 3, 2, 1]
largest= a[0]
second =float('-inf')
for num in a :
    if num>largest :
        second = largest
        largest = num
    elif num > second and num!= largest:
        second=num

print(largest)
print(second)