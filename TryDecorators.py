#!/usr/bin/python

import time
import functools


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def measuretime(func):
    """Print the runtime of the decorated function, first instance"""
    def wrapper():
        starttime = time.perf_counter()
        func()
        endtime = time.perf_counter()
        print(f"Time needed: {endtime - starttime} seconds")
    return wrapper

def sleep(func):
    def wrapper():
        time.sleep(5)
        return func()
    return wrapper

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def debugEasy(func):
    """Print the function signature and return value, 1st try"""
    def wrapper():
        print(f"Calling {func.__name__}")
    return wrapper

@timer
@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])

@measuretime
@timer
@sleep
@debug
def wakeup():
    print("Get up! Your break is over.")

@debug
def scare():
    print("Boo!")

def main():
    wastetime()
    wakeup()
    scare()

if __name__ == "__main__":
    main()