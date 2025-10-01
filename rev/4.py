def insertion_sort_count(arr):
  n = len(arr)
  copy_count = 0
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      copy_count += 1
      j -= 1
    arr[j + 1] = key
  return arr, copy_count

values = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
sorted_arr, total_copies = insertion_sort_count(values)
print("Sorted arr:", sorted_arr)
print("Total copies within while loop:", total_copies)