str = list(input())
len = int(input())
i = int(input())
n = int(input())
final = ""

for j in range(len):
    if j >= i and j < (i+n):
        final += ""
    else:
        final += str[j]

print(final)
