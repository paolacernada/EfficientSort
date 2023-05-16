# Author: Paola Cernada
# GitHub username: paolacernada
# Description: A program that graphs the time it takes to execute
#              a bubble and insertion sort on numerous random
#              lists of increasing element length by 1,000 at
#              a time, using the random module and decorators.

import time
import random
from matplotlib import pyplot
from functools import wraps


def sort_timer(fn):
    """
    sort_timer is a decorator function that counts the number of
    seconds it takes the decorated function to run.
    """

    def wrapper(func):
        """
        Decorator wrapper function to sort_timer.
        """
        start_time = time.perf_counter()
        fn(func)
        end_time = time.perf_counter()
        result = end_time - start_time
        return result

    print(wrapper)

@sort_timer
def bubble_sort(a_list):
    """
    bubble_sort is a method that sorts the array in ascending order.
    """
    for number in range(len(a_list) - 1):

        for index in range(len(a_list) - 1 - number):

            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
    """
    insertion_sort is a method that sorts the array in ascending order.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1

        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1

        a_list[pos + 1] = value

def compare_sorts(decorated_func_1, decorated_func_2):
    """
    compare_sorts is a method which takes as inputs two decorated sort
    functions. It will then build a list of 1000 integers at random
    and then duplicate that list.
    """
    size_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    x_coordinates = []
    y_coordinates_1 = []
    y_coordinates_2 = []

    for val in size_list:
        numbers_list = [random.randint(1, val) for _ in range(val)]
        copy_list = numbers_list.copy()

        time_1 = decorated_func_1(numbers_list)
        time_2 = decorated_func_2(copy_list)

        x_coordinates.append(val)
        y_coordinates_1.append(time_1)
        y_coordinates_2.append(time_2)

    pyplot.plot(x_coordinates, y_coordinates_1, "ro--", linewidth=2, label="Bubble Sort")
    pyplot.plot(x_coordinates, y_coordinates_2, "go--", linewidth=2, label="Insertion Sort")
    pyplot.xlabel("X - Coordinate")
    pyplot.ylabel("Y - Coordinate")
    pyplot.legend(loc="upper center")
    pyplot.show()

# include a line that calls your compare_sorts() function to generate the graph.
compare_sorts(bubble_sort, insertion_sort)
