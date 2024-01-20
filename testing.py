import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def run_tests():
    small_data = [random.randint(0, 1000) for _ in range(1000)]
    large_data = [random.randint(0, 10000) for _ in range(10000)]

    merge_small_time = timeit.timeit(lambda: merge_sort(small_data.copy()), number=10)
    merge_large_time = timeit.timeit(lambda: merge_sort(large_data.copy()), number=10)

    insertion_small_time = timeit.timeit(lambda: insertion_sort(small_data.copy()), number=10)
    insertion_large_time = timeit.timeit(lambda: insertion_sort(large_data.copy()), number=10)

    sort_small_time = timeit.timeit(lambda: small_data.sort(), number=10)
    sort_large_time = timeit.timeit(lambda: large_data.sort(), number=10)

    sorted_small_time = timeit.timeit(lambda: sorted(small_data.copy()), number=10)
    sorted_large_time = timeit.timeit(lambda: sorted(large_data.copy()), number=10)

    print("| Algorithm | Small Data Time | Large Data Time |")
    print("|------------|------------------|------------------|")
    print(f"| Merge Sort | {merge_small_time:.6f} | {merge_large_time:.6f} |")
    print(f"| Insertion Sort | {insertion_small_time:.6f} | {insertion_large_time:.6f} |")
    print(f"| List Sort | {sort_small_time:.6f} | {sort_large_time:.6f} |")
    print(f"| Sorted (Timsort) | {sorted_small_time:.6f} | {sorted_large_time:.6f} |")

if __name__ == "__main__":
    run_tests()