"""Here also, how the data array is entered isn't specified
So, I assumed time series data are entered with spaces"""


"""a = input().split()
for k in range(len(a)):
    a[k] = int(a[k])"""
a = [2,3,4,5,6,7,2,3,3,4,2,3,4,5,6,7,2,3,3,4]

f = int(input())
n = int(input())

samples = (f/60)*n
sampleSize = n/samples
sampleSize = int(sampleSize)
final = []
avg = 0

#This loop is faulty. Didn't have enough time to figure it out.
for i in range(1, n+1, sampleSize):
    for i in range(i-1, i+sampleSize-1):
        avg += a[i]
    avg = avg/sampleSize
    final.append(avg)

print(final)
    
    



