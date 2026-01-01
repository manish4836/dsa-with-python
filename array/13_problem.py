arr = [1, 2, 3, 4, 5]

is_increasing = True

for n in range(1, len(arr)):
    if arr[n] <= arr[n-1]:    # <= → chhota ya barabar, current value pahle vale se badi hai check karna.
        is_increasing = False
        break
print(is_increasing)