import statistics
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    inp = input()
    splt = inp.split(",")
    flt = float(splt)
    return(flt)

def calc_average(flt):
    print("calc_average")
    avg = sum(flt)/len(flt)
    print("Average: ", avg)

def find_min_max(flt):
    print("find_min_max")
    min = min(flt)
    max = max(flt)
    print("Min: ", min, ", Max: ", max)

def sort_temperature(flt):
    print("sort_temperature")
    sorted = flt.sort()
    print("Sorted: ", sorted)


def calc_median_temperature(flt):
    print("calc_median_temperature")
    median = statistics.median(flt)
    print("Median: ", median)