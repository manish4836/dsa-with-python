#Problem: To transfer all zeros end of list
#Idea:if the current element is not equal to zero then shif to  slow position 
# and change index number by +1


arr = [0, 1, 0, 3, 12]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print(arr)