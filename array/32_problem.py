## Idea:
# Prefix sum se range sum nikaalna


arr = [3, 1, 4, 2, 5, 6]

queries = [
    (0, 0),
    (0, 3),
    (2, 4),
    (3, 5)
]
prefix = []

running_sum = 0
for x in arr:
    running_sum += x
    prefix.append(running_sum)

print(prefix)

new_list = []
for l, r in queries:
    if l == 0:
        new_list.append(prefix[r])
    else:
        new_list.append(prefix[r] - prefix[l - 1])
print(new_list)