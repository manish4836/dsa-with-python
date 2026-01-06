# Day 8 – Two Pointer
# Problem: Reverse an array
# Idea:
# Do pointers array ke dono ends par rakho,
# aur jab tak left < right ho tab tak elements swap karo.

arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
