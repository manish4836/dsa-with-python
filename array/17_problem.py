arr = [1,2,3,2,1]

start = 0
end = len(arr) - 1

while start < end :
    if arr[start] != arr[end]:
        print(False)
    start = start + 1
    end = end - 1

print(True)