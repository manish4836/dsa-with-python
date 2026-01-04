arr = [5, 3, 8, 2, 6, 4]
l = 2
r = 5

prefix = []

running_sum = 0
for x in arr:
    running_sum += x
    prefix.append(running_sum)

print(prefix)
 
if l == 0:
    ans = prefix[r]

else:
    ans = prefix[r] - prefix[l - 1]

print(ans)