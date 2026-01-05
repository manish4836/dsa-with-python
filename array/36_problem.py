# Problem: Count subarrays starting from index 0 with sum = K
# Idea:
# Har prefix sum ek subarray hai jo index 0 se start hota hai,
# isliye check karte hain prefix == K

arr = [2, 3, 1, 4, 2]
K = 6

running_sum = 0
count = 0

for x in arr:
    running_sum += x     # prefix sum
    if running_sum == K:
        count += 1

print(count)
