#Given a sorted integer list of n elements and a target value, 
#write a function that searches for a target. 
#If the target exists, return the index; otherwise, return -1

n = [1, 2, 3, 4, 5, 6, 7]
target = 3

if target in n:
    result = target
else:
    result = -1

print(result)
