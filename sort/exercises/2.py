def find_insert_position(arr, value):
    n = len(arr)
    for i in range(n):
        if arr[i] > value:
            return i
    return n

def insert_in_order(arr, value):
    arr.append(None)

    pos = find_insert_position(arr, value)
    n = len(arr) - 1

    for i in range(n, pos, -1):
        arr[i] = arr[i-1]

    arr[pos] = value

arr = [1, 2, 4, 5]
insert_in_order(arr, 3)
print(arr)