arr = [1, 2, 3, 4]

prefix = []

running_sum = 0

for n in arr:
    running_sum += n
    prefix.append(running_sum)
print(prefix)