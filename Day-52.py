## 59.program finds the two numbers in an array that have the smallest absolute difference between them
def find_smallest_absolute_difference(arr):
    if len(arr) < 2:
        return None

    arr.sort()  # Sort the array in ascending order
    min_abs_diff = float('inf')  # Initialize with a large value
    result = []

    for i in range(len(arr) - 1):
        abs_diff = abs(arr[i] - arr[i + 1])

        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
            result = [arr[i], arr[i + 1]]

    return result

# Example usage:
input_array = [4, 2, 1, 3, 5, 6]
result = find_smallest_absolute_difference(input_array)
if result:
    print(f"The two numbers with the smallest absolute difference are {result[0]} and {result[1]}")
else:
    print("The array has less than two elements.")
