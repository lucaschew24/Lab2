import statistics
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    inp = input()
    splt = inp.split(",")
    flt = [float(i) for i in splt]
    return flt

def calc_average(flt):
    print("calc_average")
    avg = sum(flt)/len(flt)
    print("Average: ", avg)

def find_min_max(flt):
    print("find_min_max")
    mini = min(flt)
    maxi = max(flt)
    print("Min: ", mini, ", Max: ", maxi)

def sort_temperature(flt):
    print("sort_temperature")
    sorted = flt.sort()
    print("Sorted: ", sorted)


def calc_median_temperature(flt):
    print("calc_median_temperature")
    median = statistics.median(flt)
    print("Median: ", median)

def main():
    display_main_menu()
    flt = get_user_input()
    calc_average(flt)
    find_min_max(flt)
    sort_temperature(flt)
    calc_median_temperature(flt)

main()