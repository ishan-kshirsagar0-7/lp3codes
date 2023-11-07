import random

# This function takes the last element as pivot, places
# the pivot element at its correct position in sorted array,
# and places all smaller to left of pivot and all greater elements to right of pivot
def partition_deterministic(arr, low, high):
    pivot = arr[high]  # pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The main function that implements QuickSort
def quick_sort_deterministic(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition_deterministic(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)

# This function is same as above but chooses pivot randomly
def partition_randomized(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]  # Swap with high
    return partition_deterministic(arr, low, high)

# The main function to do QuickSort using randomized partition
def quick_sort_randomized(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition_randomized(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)

# Driver code to test the above functions
if __name__ == "__main__":
    arr1 = [10, 7, 8, 9, 1, 5]
    arr2 = arr1.copy()  # Copy the array to keep the same inputs for both sorts

    n = len(arr1)
    
    print("Original array:", arr1)
    quick_sort_deterministic(arr1, 0, n - 1)
    print("Sorted array with deterministic quick sort:", arr1)

    quick_sort_randomized(arr2, 0, n - 1)
    print("Sorted array with randomized quick sort:", arr2)
