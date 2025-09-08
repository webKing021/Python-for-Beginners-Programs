def merge_sort(arr):
    # If the list has 1 or 0 items, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # Add any leftover numbers
    result.extend(left or right)
    return result


# Example
numbers = [5, 2, 9, 1, 6, 3]
print("Before:", numbers)
print("After: ", merge_sort(numbers))
