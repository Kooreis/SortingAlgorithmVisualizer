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