# Day 4 – Array
# Problem: Check if array is strictly increasing
# Idea: Compare current element with previous one using loop

arr = [1, 2, 3, 4]

is_increasing = True

for n in range(1, len(arr)):
    if arr[n] <= arr[n-1]:
        is_increasing = False 
        break 
print(is_increasing)