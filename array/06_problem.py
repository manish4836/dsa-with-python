arr = [1, 1, 2, 2, 3, 3, 3, 4]

i = 1
for j in range(1, len(arr)):
    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]
print("Unique count:", i)
print("Array:", arr)