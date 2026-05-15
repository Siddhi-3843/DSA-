arr = [-10, -20, -5, -15]

first = float('-inf')
second = float('-inf')
third = float('-inf')

for num in arr:

    if num > first:

        third = second
        second = first
        first = num

    elif num > second and num != first:

        third = second
        second = num

    elif num > third and num != second and num != first:

        third = num

print("Third Largest:", third)
print(".....................................   ")

arr = [3,1,4,1,5]
n = len(arr)
prefix=[0]*n
print("Empty prefix :", prefix)
prefix[0]=arr[0]
print ("After index 0 :", prefix)

for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
    print(f" After index{i}:",prefix)
print("final prefix :",prefix)     
L=int(input("Enter value of L:"))
R=int(input("Enter value of R:")) 
if L==0:
    result=prefix[R]
else:
    result = prefix[R]- prefix[L-1]    
print(result)    