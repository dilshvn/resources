"""How the array 'a' is entered isn't specified
So, I assumed integers are entered with spaces"""

#To create the array 'a'
a = input().split()
for k in range(len(a)):
    a[k] = int(a[k])

#To get the length of array 'a'
len = int(input())

max_ = a[0]
secMax = a[0]

for i in range(len):
    if a[i] > max_:
        secMax = max_
        max_ = a[i]
    elif a[i] > secMax and a[i] != max_:
        secMax = a[i]
        
#prints the maximum integer
print(max_)

#prints the second maximum integer
print(secMax)

