def insertion_sort_descending(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

values = [5, 2, 9, 1, 7]
print("Original:", values)
print("Sorted (descending):", insertion_sort_descending(values))