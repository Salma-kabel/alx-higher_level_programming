#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """invert == operator"""
    def __eq__(self, value):
        return super().__ne__(value)

    """invert != operator"""
    def __ne__(self, value):
        return super().__eq__(value)
