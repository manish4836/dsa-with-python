arr = [7, 2, 5, 1, 6]

queries = [
    (0, 4),   # full array
    (0, 0),   # single element (start)
    (4, 4),   # single element (end)
    (1, 3),   # middle range
    (2, 2)    # single element (middle)
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
        new_list.append(prefix[r] - prefix[l-1])

print(new_list)