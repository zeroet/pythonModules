import sys


def string_to_int(Str):
    try:
        temp = int(Str)
        if type(temp) == int:
            return temp
    except:
        print("AssertionError: argument is not an integer")
        exit()


def odd_even_zero(num):
    if num == 0:
        print("I'm Zero")
    elif num % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


arg = sys.argv

if len(arg) == 1:
    quit()
elif len(arg) > 2:
    print("AssertionError: more than one argument are provided")
    exit(0)
num = string_to_int(arg[1])
odd_even_zero(num)