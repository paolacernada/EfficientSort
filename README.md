# Sorting-Algorithm-Comparison

In this personal project, I'll be exploring the efficiency of sorting algorithms by comparing their execution times. To accomplish this, I'll be utilizing the Python time and random modules, as well as the matplotlib package.

# Setup

To begin, make sure you have the following dependencies installed:

    * matplotlib package
    
 Next, import the necessary modules and functions:
 
    import time
    import random
    from matplotlib import pyplot as plt

# Timing Decorator

In order to measure the execution time of the sorting algorithms, I'll create a decorator function called sort_timer. This decorator will time the decorated function and return the elapsed time in seconds.

    def sort_timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            return elapsed_time
        return wrapper
        
# Sorting Algorithms

Now, let's implement the bubble sort and insertion sort algorithms. We'll decorate these functions with the sort_timer decorator to measure their execution times.

    @sort_timer
    def bubble_sort(lst):
        # Bubble sort implementation
        # ...

    @sort_timer
    def insertion_sort(lst):
        # Insertion sort implementation
        # ...
        
 
# Comparing Sorts
 
To compare the sorting algorithms, I'll write a function called compare_sorts. This function will generate a list of 1000 random numbers and make a separate copy of it. Then, it will measure the time taken by each algorithm to sort their respective copies. This process will be repeated for list sizes ranging from 2000 to 10000, incrementing by 1000. Finally, I'll plot a graph to visualize the timing data.

    def compare_sorts(bubble_sort_func, insertion_sort_func):
        list_sizes = range(1000, 11000, 1000)
        bubble_sort_times = []
        insertion_sort_times = []

        for size in list_sizes:
            lst = [random.randint(1, 10000) for _ in range(size)]
            lst_copy = list(lst)

            bubble_sort_time = bubble_sort_func(lst_copy)
            insertion_sort_time = insertion_sort_func(lst_copy)

            bubble_sort_times.append(bubble_sort_time)
            insertion_sort_times.append(insertion_sort_time)

        plt.plot(list_sizes, bubble_sort_times, 'ro--', linewidth=2, label='Bubble Sort')
        plt.plot(list_sizes, insertion_sort_times, 'go--', linewidth=2, label='Insertion Sort')
        plt.xlabel("Number of Elements")
        plt.ylabel("Time (seconds)")
        plt.legend(loc='upper left')
        plt.show()
    
# Running the Comparison

To execute the comparison between the sorting algorithms, call the compare_sorts function with the decorated sorting functions as arguments.

    compare_sorts(bubble_sort, insertion_sort)

This will generate a graph that showcases the execution times of both bubble sort and insertion sort for different list sizes.

