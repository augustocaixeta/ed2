def selection_sort_descending(arr):
  n = len(arr)
  for i in range(n - 1):
    max_index = i
    for j in range(i + 1, n):
      if arr[j] > arr[max_index]:
        max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
  return arr

values = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
print("Original:", values)
print("Sorted in descending order:", selection_sort_descending(values))