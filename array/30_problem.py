# Day 6 – Array
# Problem: Range Sum Queries
# Idea:
# 1. Prefix sum banate hain jisme prefix[i] = arr[0] se arr[i] tak ka sum hota hai
# 2. Har query (l, r) ke liye:
#    - Agar l == 0 ho, to directly prefix[r] answer hota hai
#    - Agar l > 0 ho, to prefix[r] me se prefix[l-1] minus karte hain
#      taaki left ka extra sum hata sakein

arr = [2, 4, 6, 8, 10]

queries = [
    (0, 2),
    (1, 3),
    (2, 4)
]

# Step 1: Build prefix sum array
prefix = []
running_sum = 0

for n in arr:
    running_sum += n
    prefix.append(running_sum)

print(prefix)   # [2, 6, 12, 20, 30]

# Step 2: Answer each query using prefix sum
new_list = []

for l, r in queries:
    if l == 0:
        # If range starts from index 0, no extra left part to remove
        ans = prefix[r]
    else:
        # Remove sum of elements from index 0 to l-1
        ans = prefix[r] - prefix[l - 1]

    new_list.append(ans)

print(new_list)   # [12, 18, 24]
