# Brute force method to count the number of inversions in a list
def count_inversions_brute_force(arr):
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return "Error: Array contains non-integer values, inversion count can't be performed."
    
    inversions = 0
    n = len(arr)
    
    # Compare each pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
                
    return inversions

# Divide and conquer (merge sort) method to count the number of inversions in a list
def count_inversions_divide_and_conquer(arr):
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return "Error: Array contains non-integer values, inversion count can't be performed."
    
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inversions = merge_sort(arr, left, mid)
    inversions += merge_sort(arr, mid + 1, right)
    inversions += merge_and_count(arr, left, mid, right)
    
    return inversions

def merge_and_count(arr, left, mid, right):
    # Left and right subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    inversions = 0
    
    # Merge while counting inversions
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            inversions += (mid - i + 1 - left)  # Count inversions
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
        
    return inversions

# The provided nested list (contains a mix of integers and letters for testing)
students_random_numbers = [
    [5, 2, 3, 6], ['a', 1, 5, 2], [-7, -6, -4, -1], [-6, -2, -5, -7], [2, 3, 8, 4], [5, 5, 5, 4]
]

# Initialize containers for categorization
valid_inversion_counts = []
negative_inversion_counts = []
error_messages = []

# Process each sublist for inversion counts
for index, sublist in enumerate(students_random_numbers):
    if all(isinstance(x, int) for x in sublist):  # Check if all elements are integers
        if all(x < 0 for x in sublist):  # Check if all elements are negative
            negative_inversion_counts.append((index + 1, "Inversion count can be found since course code cant be negative."))
        else:
            brute_force_count = count_inversions_brute_force(sublist)
            divide_and_conquer_count = count_inversions_divide_and_conquer(sublist[:])
            valid_inversion_counts.append((index + 1, brute_force_count, divide_and_conquer_count))
    else:
        error_messages.append((index + 1, "Error: Array contains letters instead of integer values, inversion count can't be performed."))

# Display results for valid inversion counts
print("\nCategorized Inversion Counts (Valid Entries):")
for student_index, bf_count, dc_count in valid_inversion_counts:
    print(f"Student {student_index}: Brute Force Inversion Count = {bf_count}, Divide and Conquer Inversion Count = {dc_count}")

# Display results for negative integer entries
print("\nNegative Integer Entries:")
for student_index, message in negative_inversion_counts:
    print(f"Student {student_index}: {message}")

# Display error messages for invalid entries
print("\nError Messages for Invalid Entries:")
for student_index, error in error_messages:
    print(f"Student {student_index}: {error}")
