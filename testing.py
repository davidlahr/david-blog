def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


# add_15 = create_adder(15)
#
# print(add_15(10))
#
# greet(shout)
# greet(whisper)


def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")

    return inner1



def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()