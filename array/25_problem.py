#Problem: Check the arr is strictly decreasing or not
#Idea: assme arr is strictly decreasing
#  apply loop on arr
# check currunt element is not big of the previous elements

arr = [9, 7, 5, 3]

is_decreasing = True

for i in range(1, len(arr)):
    if arr[i] >= arr[i - 1]:
        is_decreasing = False
        break

print(is_decreasing)