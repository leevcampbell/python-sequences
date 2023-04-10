#!/usr/bin/env python3

def print_fibonacci(length):
    a = 0
    b = 1
    fib_list = []
    for i in range(length):
        fib_list.append(a)
        a, b = b, a + b
    print(fib_list)