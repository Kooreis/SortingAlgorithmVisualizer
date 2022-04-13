```python
import time
import random

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print_array(arr)
        print()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print_array(arr)
    print()

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print_array(arr)
    print()

def main():
    size = 10
    arr = [random.randint(1, 100) for _ in range(size)]
    print("Original array:")
    print_array(arr)
    print("\nBubble sort:")
    bubble_sort(arr.copy())
    print("Insertion sort:")
    insertion_sort(arr.copy())
    print("Selection sort:")
    selection_sort(arr.copy())

if __name__ == "__main__":
    main()
```