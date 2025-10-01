def bubble_sort_string(s):
  arr = list(s)
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return "".join(arr)

text = "algorithm"
result = bubble_sort_string(text)
print("Original:", text)
print("Sorted:", result)