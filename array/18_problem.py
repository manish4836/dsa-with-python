arr = [1,2,3,4,6]
target = 6

left = 0 
right = len(arr) - 1

found = False 

while left < right:
    sum = arr[left] + arr[right]

    if sum == target:
        found = True
        break
    elif sum < target:
        left += 1
    else:
        right -= 1

print(found) 