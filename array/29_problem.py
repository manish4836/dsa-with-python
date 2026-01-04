# Problem: Range Sum Query
# Idea: Use prefix sum to calculate range sum in O(1)

arr = [1, 2, 3, 4, 5]
l = 1
r = 3

prefix = []

running_sum = 0
for n in arr:
    running_sum += n
    prefix.append(running_sum)

print(prefix)

if l == 0:   #arr[0] se r tak ka sum chahiye
    ans = prefix[r]
else:
    ans = prefix[r] - prefix[l - 1]   #prefix[3] me arr[0] se arr[3] tak ka sum hota hai,isliye arr[1] se arr[3] ka sum nikalne ke liye prefix[0] minus karte hain

print(ans)