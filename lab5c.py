#!/usr/bin/env python3
# Author ID: Jhanlyn Brita Dannuy - jdannuy

def add(number1, number2):
    try:
        # Attempt to convert both inputs to integers
        number1 = int(number1)
        number2 = int(number2)
        return number1 + number2
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))  # should print 15
    print(add('10', 5))  # should print 15
    print(add('abc', 5))  # should print error message
    print(read_file('seneca2.txt'))  # should print lines from the file
    print(read_file('file10000.txt'))  # should print error message
import lab5c

lab5c.add(10, 5)
lab5c.add('10', 5)
lab5c.add('abc', 5)
lab5c.read_file('seneca2.txt')
lab5c.read_file('file10000.txt')
