#!/usr/bin/python

import time

def measuretime(func):
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
    def wrapper():
        print(f"Calling {func.__name__}")
    return wrapper

@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])

@measuretime
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