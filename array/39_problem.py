# Day 8 – Two Pointer
# Problem: Check if pair with given sum exists
# Idea:
# Do pointers start aur end se move karte hain
# Sum ke comparison ke hisaab se pointer adjust hota hai

arr = [1, 2, 3, 4, 6]
target = 6

start = 0
end = len(arr) - 1

result = False

while start < end:
    curr_sum = arr[start] + arr[end]

    if curr_sum == target:
        result = True
        break
    elif curr_sum < target:
        start += 1
    else:
        end -= 1

print(result)
