def binary_search(arr, target):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

        print(mid, left, right)

    return -1

arr = [2, 10, 12, 16, 19, 21, 23, 24, 28, 31]
target = 28

print(binary_search(arr, target))
