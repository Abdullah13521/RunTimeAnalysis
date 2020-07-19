def quicksort(arr):
    """ An implementation of the quick sort algorithm """
    if len(arr) < 2:
        return arr
    else:
        smaller = []
        equal = []
        greater = []
        pivot = arr[-1]

        for n in range(len(arr)-1):
            if arr[n] > pivot:
                greater.append(arr[n])
            elif arr[n] < pivot:
                smaller.append(arr[n])
            else:
                equal.append(arr[n])
    return quicksort(smaller), equal, quicksort(greater)

def bubble_sort(arr):
    """ An implementation of the bubble sort algorithm """
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    return arr

def merge_sort(arr):
    """ An implementation of the merge sort algorithm """
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1, l2)

def merge_sorted(arr1, arr2):
    """ Helper function for the merge sort algorithm """
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i = i + 1
        else:
            sorted_arr.append(arr2[j])
            j = j + 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i = i + 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j = j + 1

    return sorted_arr

def selection_sort(arr):
    """ An implementation of the selection sort algorithm """
    for n in range(len(arr) - 1):
        for i in range(n, len(arr)):
            if arr[n] > arr[i]:
                arr[n], arr[i] = arr[i], arr[n]
    return arr

def insertion_sort(arr):
    """ An implementation of the insertion sort algorithm """
    key = 1
    while key < len(arr):
        for n in range(key):
            if arr[key] < arr[n]:
                arr[key], arr[n] = arr[n], arr[key]
        key = key + 1
    return arr
