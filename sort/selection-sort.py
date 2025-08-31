def shift(arr, start, n):
    smallest_idx = start

    for i in range(start + 1, n):
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i

    arr[start], arr[smallest_idx] = arr[smallest_idx], arr[start]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        shift(arr, i, n)

arr = [6, 7, 9, 4, 3, 0]
selection_sort(arr)
print(arr)

# ...
arr = [6, 7, 9, 4, 3, 0]
n = len(arr)

for i in range(n - 1):
    idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[idx]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]

print(arr)
