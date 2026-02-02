n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def heapify_down(arr, k, n):
    while 2 * k + 1 < n:
        L, R = 2 * k + 1, 2 * k + 2

        if L < n and arr[L] > arr[k]:
            m = L
        else:
            m = k
        if R < n and arr[R] > arr[m]:
            m = R

        if m != k:
            arr[k], arr[m] = arr[m], arr[k]
            k = m
        else:
            break

def make_heap(arr, n):
    for k in range(n - 1, -1, -1):
        heapify_down(arr, k, n)

def heap_sort(arr, n):
    for k in range(n - 1, -1, -1):
        arr[0], arr[k] = arr[k], arr[0]
        n -= 1
        heapify_down(arr, 0, n)

make_heap(arr, n)
heap_sort(arr, n)

print(*arr)

