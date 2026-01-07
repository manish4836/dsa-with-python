# Problem: Average of all subarrays of size k
# Idea:
# Sliding window ka sum maintain karke
# har step par average calculate karo

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

average = []

window_sum = sum(arr[:k])
average.append(window_sum / k)

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    average.append(window_sum / k)

print(average)
