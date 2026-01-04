# Idea:
# Prefix sum se har query ka range sum nikaala,
# aur check kiya kaunsa sum X se bada hai.

arr = [1, 2, 3, 4, 5]

queries = [
    (0, 2),
    (1, 3),
    (2, 4)
]

X = 7

prefix = []

running_sum = 0

for x in arr:
    running_sum += x
    prefix.append(running_sum)

print(prefix)


count = 0
new_list = []
for l, r in queries:
    if l == 0:
        sum = (prefix[r])

    else:
        sum = (prefix[r] - prefix[l-1])

    new_list.append(sum)

    if sum > X:
        count += 1

print(new_list)
print(count)