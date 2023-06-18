def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_greater = []
        items_lower = []
        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

print(f"List entered by the user {marks}")
print(f"List after sorting is: {quick_sort(marks)}")
