# swapping using two pointers 
a=[]
left = 0
right =len(a)-1

while left<right:
    a[left],a[right]=a[right],a[left]
    left +=1
    right -=1
print(a)




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