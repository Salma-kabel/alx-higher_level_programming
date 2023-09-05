#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass():
    """prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    """Initialize a class"""
    def __init__(self):
        pass
