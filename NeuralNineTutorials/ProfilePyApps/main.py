#basic examples and functions
# to profile speed of different functions within a program
# for graphical table
# pip3 install tuna

# nav to file and run without importing the cprofile package
# python3 -m cProfile file.py
#if importing cprofile package and pstats
#import cProfile
#import pstats

import time

def add(x, y):
    #not good
    resulting_sum = 0
    resulting_sum += x
    resulting_sum += y
    return resulting_sum

def fact(n):
    result = 1
    for i in range(1, n +1):
        result *= i
    return result

def do_stuff():
    result = []
    for x in range(100000):
        result.append(x ** 2)
    return result
    # list comprehension is alot faster
    #return [x ** 2 for x in range(100000)]

def waste_time():
    time.sleep(5)
    print("Hello")


if __name__ == "__main__":
    print(add(100, 5000))
    print(fact(70000))
    print(do_stuff())
    # callin multiple times can give you average per call
#   print(do_stuff())
#   print(do_stuff())
    waste_time()

    #only with importing cprofile package
#   with cProfile.Profile() as profile:
#       print(add(100, 5000))
#       print(fact(70000))
#       print(do_stuff())
#       waste_time()

#   results = pstats.Stats(profile)
#   results.sort_stats(pstats.SortKey.TIME)
#   results.print_stats()
    
#    for tuna graphical table
#   results.dump_stats("results.prof")
#   nav to that file and run
#   tuna results.prof