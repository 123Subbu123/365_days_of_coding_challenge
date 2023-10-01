## 56.The longest subarray with a sum equal to a given target value
def longest_subarray_with_sum(arr, target_sum):
    # Create a dictionary to store the cumulative sum and its index
    sum_indices = {}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        # If the current_sum equals the target_sum, update max_length
        if current_sum == target_sum:
            max_length = i + 1

        # If the current_sum - target_sum is in the dictionary, update max_length
        if current_sum - target_sum in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum - target_sum])

        # If the current_sum is not in the dictionary, add it with its index
        if current_sum not in sum_indices:
            sum_indices[current_sum] = i

    return max_length

# Example usage:
arr = [1, -1, 5, -2, 3]
target_sum = 3
result = longest_subarray_with_sum(arr, target_sum)
print("Length of longest subarray with sum", target_sum, "is:", result)
