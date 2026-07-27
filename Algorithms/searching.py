def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    arr = [11, 22, 25, 34, 64, 90]
    print(f"Array: {arr}")
    target = 25
    print(f"Linear search ({target}): index {linear_search(arr, target)}")
    print(f"Binary search ({target}): index {binary_search(arr, target)}")
    print(f"Binary recursive ({target}): index {binary_search_recursive(arr, target, 0, len(arr)-1)}")
