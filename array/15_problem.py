arr = [3, 1, -4, 2]

prefix = []

running_sum = 0

for x in arr:
    running_sum += x
    prefix.append(running_sum)
print(prefix)