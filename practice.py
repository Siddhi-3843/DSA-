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