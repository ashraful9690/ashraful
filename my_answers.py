#!/usr/bin/python

"""
Here is the comment part. Please carefully read this part before your homework.
1. General knowledge,
    1-1. Codes have comments like this block. In such block, your code are invalid. 
        And commented parts are used to describe/explain the code.
    1-2. If your words starts and ends with three ", the whole block is commented.
    1-3. If your words following after #, this line is commented.
2. Homework description,
    2-1. The following codes are partially done. You need to fill the line(s) to make it
        complete. Please DO NOT delete the spaces before the variable I created for you.
        And DO NOT change the vairable name.
    2-2. What you are expected to do has shown in the comments. Please read carfully.
3. In the tests, you have the test samples released. These are partial tests. But you can
   use this to test your basic logics. Or just add print to test in this file.
"""


def numbersAndStrings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Write square root of 9 without using math module
    x = 9 ** (1/2)

    # Assign a string "CUNY" to a variable y
    y = print("CUNY")

    # Repeat variable y 3 times using *
    z = print(y * 3)

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = (y + " is good")

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = (m + " is awesome")

    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "CUNY is awesome"

    # Split variable n on a delimiter 'space' into a list of substrings
    p = (',')

    # Get all the items except the first of the third substring
    r = n[0:3]

    # We have a 3 x 3 matrix
    A = [[1, 4, 5], [6, 10, 11], [12, 17, 38]]

    # Collect the items in the last column of matrix A using list comprehension
    c = Print [A(2)]

    # Collect only the even items of the right diagonal of matrix A using list comprehension
    # What is right diagonal? items in right diagonal of A is [5, 10, 12]. Start from right top
    # to left bottom.
    d = print [A[2][0],[1][1],[0][0]] 

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "CUNY" using list comprehension.
    o = print ('C','U','N','Y')

    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f = dict(fruit='apple', quantity=4, color='green')

    # Get the item in dictionary f that the key "fruit" maps to
    a = f('fruit')

    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity'] = f['quantity'] + 1

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    amazing_grace = {
        'name': {
            'first_name': "Grace",
            'last_name': "Hopper"},
        'jobs': ["scientist", "engineer"],
        'age': 85
    }

    # Add "programmer" to the list of jobs Grace has
    amazing_grace['jobs'].append('programmer)

    # Get the third job Grace has that you recently added
    p = amazing_grace['jobs'](2)

    # Get the sorted keys of amazing_grace in alphabetically ascending order
    k = list(amazong_grace.keys())
    k.shor()

    return a, f, p, k


numbersAndStrings()
lists()
dictionaries()
