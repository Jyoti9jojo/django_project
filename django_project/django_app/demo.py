# def decorator(view_function):
#     def wrapper():
#         2+2 == 5
#         return view_function()
#     return wrapper

from random import random
import time
import math
 
def calculate_time(func):
     
    def inner1(*args, **kwargs):
        print("inside inner1 function")
        print("inside inner1 askdfjhsidfhf")

        begin = time.time()
         
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1

@calculate_time
def power_of(num):
    print(num)
 
@calculate_time
def factorial(num):
    print("inside factorial start")

    print(math.factorial(num))
    print("inside factorial end")
 
factorial(10)