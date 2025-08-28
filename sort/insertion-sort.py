def shift(arr, cur, n):
    val = arr[cur]
    idx = cur
    for i in range(cur - 1, -1, -1):
        if arr[i] <= val:
            break
        arr[i+1] = arr[i]
        idx = i
    arr[idx] = val

def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] <= arr[i]:
            continue
        shift(arr, i, n)

arr = [5, 2, 4, 3, 0]
insertion(arr)
print(arr)
