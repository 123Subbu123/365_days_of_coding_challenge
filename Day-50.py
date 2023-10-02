## 57.Longest Increasing Subsequence
def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(arr)
print("Length of the Longest Increasing Subsequence is:", result)
