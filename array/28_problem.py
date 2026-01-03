# Problem: Maximum Difference
# Idea: Track minimum so far and max difference

arr = [2, 3, 10, 6, 4, 8, 1]

min_so_far = arr[0]

maxi_diff = 0

for n in range(1, len(arr)):
    if arr[n] - min_so_far > maxi_diff:
        maxi_diff = arr[n] - min_so_far

    if arr[n] < min_so_far:
        min_so_far = arr[n]

print(maxi_diff)