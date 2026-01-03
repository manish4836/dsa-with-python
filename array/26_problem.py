#Problem: Check total number of zeros
#idea:apply loop on arr and check condition 


arr = [0, 1, 0, 3, 0, 5]

count = 0 

for x in arr:
    if x == 0:
        count += 1

print("Total zoro:",count)