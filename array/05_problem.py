arr = [12, 35, 1, 10, 34, 1]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest and num >second_largest:
        second_largest = num

print(f"Second Largest: {second_largest}")