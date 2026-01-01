arr = [10, 10, 20, 30, 30, 30]

freq = {}
for n in arr:
    freq[n] = freq.get(n, 0) + 1

max_count = 0

ans = None

for key, values in freq.items():
    if values > max_count:
        max_count = values
        ans = key

print("Most Frequent Element:",ans)