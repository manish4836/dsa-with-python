arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for n in arr:
    if n in freq:
        freq[n] += 1
    else :
        freq[n] = 1
print(freq)