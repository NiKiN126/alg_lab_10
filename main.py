import random

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем элементы местами
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи по одному
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # меняем элементы местами
        heapify(arr, i, 0)

def generate_random_array(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

# Генерация массива и сортировка
size = 10
start_range = 1
end_range = 20
arr = generate_random_array(size, start_range, end_range)
print("Исходный массив:")
print(arr)

heap_sort(arr)
print("\nОтсортированный массив:")
print(arr)