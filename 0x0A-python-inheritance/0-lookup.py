#!/usr/bin/python3
'''
a function that returns the list of available attributes
and methods of an object
'''


def lookup(obj):
    '''
    a function that returns the list of available
    attributes and methods of an object

    Attribute:
        obj: object

    Returns: list of object
    '''
    return (dir(obj))

