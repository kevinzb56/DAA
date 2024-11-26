# Brute force method to count the number of inversions in a list
def count_inversions_brute_force(arr):
    inversions = 0
    n = len(arr)
    
    # Compare each pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
                
    return inversions

# Example usage
arr = [8, 4, 2, 1]

# Count inversions using brute force
brute_force_inversions = count_inversions_brute_force(arr)
print(f"Brute Force Inversions: {brute_force_inversions}")
