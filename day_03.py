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
