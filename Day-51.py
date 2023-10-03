## 58.Longest Subarray with Sum K
def longest_subarray_with_sum(arr, target_sum):
    prefix_sum = {}  # Dictionary to store the prefix sum and its corresponding index
    max_length = 0  # Maximum length of the subarray with sum equal to target_sum
    current_sum = 0  # Current prefix sum

    for i, num in enumerate(arr):
        current_sum += num

        # If the current sum is equal to the target sum, update the max_length
        if current_sum == target_sum:
            max_length = i + 1

        # If the current sum - target_sum is in the prefix_sum dictionary, update max_length
        if current_sum - target_sum in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - target_sum])

        # Store the current sum and its index in the prefix_sum dictionary
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_length

# Example usage:
arr = [1, -1, 5, -2, 3]
target_sum = 3
result = longest_subarray_with_sum(arr, target_sum)
print("Length of Longest Subarray with Sum", target_sum, "is", result)
