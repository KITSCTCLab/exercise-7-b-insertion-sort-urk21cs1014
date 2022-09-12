from typing import List

def insertionSort(array) -> List[int]:
  size = len(array)
  for index in range(1, size):
    curr_ind = index
    while curr_ind > 0 and array[curr_ind - 1] > array[curr_ind]:
      array[curr_ind - 1], array[curr_ind] = array[curr_ind], array[curr_ind - 1]
      curr_ind -= 1
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
