arr = [3, 1, 4, 2, 5]

prefix = []

running_sum = 0

for x in arr:
    running_sum += x
    prefix.append(running_sum)

print(prefix)

new_list = []
for r in range(1, len(prefix)):
    new_list.append(prefix[r] - prefix[0])

print(new_list)