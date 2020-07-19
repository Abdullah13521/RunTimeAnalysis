import time
import random
from algorithms_file import bubble_sort, quicksort, merge_sort, selection_sort, insertion_sort

def create_random_list(size, max_val):
    """ Creates a random list of integers """
    return [random.randint(1,max_val) for num in range(size)]

def analyze_func(algorithm, arr):
    """ Analyzes the function runtime of a sorting algorithm """
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    seconds = round(end_time - start_time, 5)
    print("{}     -> Elapsed time: {}".format(algorithm.__name__.capitalize(), seconds))

size = int(input("What size list do you want? "))
max = int(input("What max value do you want? "))
num_runs = int(input("How many runs do you want? "))

# Loop for each run
for num in range(num_runs):
    print("Run: {}".format(num+1))
    l = create_random_list(size, max)

    # It's better to comment those lines out when analyzing large lists 
    analyze_func(bubble_sort, l.copy())
    analyze_func(selection_sort, l.copy())
    analyze_func(insertion_sort, l.copy())

    analyze_func(quicksort, l)
    analyze_func(merge_sort, l)
    analyze_func(sorted, l)
    print("-" * 40)
