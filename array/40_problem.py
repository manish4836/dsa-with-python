# Idea:
# Pehle k elements ka sum banao,
# phir window slide karke ek element minus aur ek add karo

arr = [2, 1, 5, 1, 3, 2]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)