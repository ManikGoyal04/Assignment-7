def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Get input from the user
input_str = input("Enter the numbers separated by commas: ")
input_array = [int(num) for num in input_str.split(",")]

# Sort the input array
sorted_array = sorted(input_array)
print("Sorted array:", sorted_array)

# Ask user for the element to search
search_element = int(input("Enter the element to search: "))

# Perform binary search
search_result = binary_search(sorted_array, search_element)

if search_result == -1:
    print("Element not found in the array.")
else:
    print("Element found at index:", search_result)

    # Count the occurrences of the element
    occurrence_count = count_occurrences(sorted_array, search_element)
    print("Number of occurrences of element", search_element, "is:", occurrence_count)

