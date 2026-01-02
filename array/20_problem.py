# Day 4 – Array
# Problem: Check if target sum eliments are present or not
# Idea: Two pointers use karo.
# Left pointer start se, right pointer end se.
# Dono ka sum target se compare karo.
# Sum chhota ho to left badhao, bada ho to right ghatao.

arr = [1, 2, 3, 4, 6]
target = 6

start = 0
end = len(arr) - 1

result = False
while start < end :
    sum = arr[start] + arr[end]
    
    if sum == target:
        result = True
        break
    elif sum < target:
        start += 1
    else:
        end -= 1

print(result)