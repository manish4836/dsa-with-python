# Day 10 – Sliding Window (Variable Size)
# Problem: Longest subarray with sum <= K
# Idea:
# Window ko expand karo jab sum valid ho,
# aur shrink karo jab sum limit cross kare

arr = [2, 1, 5, 1, 3, 2]
K = 7

left = 0
window_sum = 0

min_len = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= K:
        min_len = min(min_len,right - left + 1)
        window_sum -= arr[left]
        left += 1

# Agar koi valid subarray nahi mila
if min_len == float('inf'):
    print(0)
else:
    print(min_len)

