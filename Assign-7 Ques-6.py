def remove_duplicates(nums):
    return list(set(nums))

def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

# Get input from the user
input_str = input("Enter the numbers separated by commas: ")
input_array = [int(num) for num in input_str.split(",")]

# Remove duplicates
unique_array = remove_duplicates(input_array)
print("Unique array:", unique_array)

# Sort using selection sort
selection_sorted = selection_sort(unique_array)
print("Selection sorted array:", selection_sorted)

# Sort using bubble sort
bubble_sorted = bubble_sort(unique_array)
print("Bubble sorted array:", bubble_sorted)
