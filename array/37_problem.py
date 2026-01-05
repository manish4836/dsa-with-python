# Problem: Check if any prefix sum is even
# Idea:
# Prefix sum banate hue har step par check karo
# agar koi bhi prefix sum even ho to True

arr = [1, 2, 4, 4, 6]

prefix = []
running_sum = 0
result = False

for x in arr:
    running_sum += x          # prefix sum update
    prefix.append(running_sum)

    if running_sum % 2 == 0:  # check if prefix is even
        result = True
        break

print(prefix)
print(result)
