# Problem: Longest subarray with sum <= K
# Idea:
# Window ko expand karo jab sum valid ho,
# aur shrink karo jab sum limit cross kare

arr = [2, 1, 5, 1, 3, 2]
K = 7

left = 0
window_sum = 0

max_len = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum > K:
        window_sum -= arr[left]
        left += 1

        max_len = max(max_len, right - left + 1)

print(max_len)