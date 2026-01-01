arr = [7, 3, 9, 1, 2, 5]

min_num = arr[0]
second_min = arr[0]

for n in arr:
    if n < min_num:
        second_min = min_num
        min_num = n 

    elif n < second_min and n != min_num:
        second_min = n
print(second_min)