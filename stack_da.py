# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, part 2
# Due Date: 11/6/23
# Description: Stack implemented using the dynamic array from A2 as underlying storage

from dynamic_array import *

class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None: #passes the prescribed test
        """
            Add a new element to the top of the stack.
            It must be implemented with O(1) amortized runtime complexity.
        """
        self._da.append(value)  # Use the append method of DynamicArray
    def pop(self) -> object: #passes the prescribed test
        """
                Remove the top element from the stack and return its value.
                If the stack is empty, the method raises a custom “StackException”.
                It must be implemented with O(1) amortized runtime complexity.
                """
        if self.is_empty():
            raise StackException("Stack is empty")

        # Get the top element
        top_index = self._da.length() - 1
        top_element = self._da.get_at_index(top_index)

        # Remove the top element
        self._da.remove_at_index(top_index)

        return top_element


    def top(self) -> object: #passes the prescribed test
        """
                Return the value of the top element of the stack without removing it.
                If the stack is empty, the method raises a custom “StackException”.
                It must be implemented with O(1) runtime complexity.
                """
        if self.is_empty():
            raise StackException("Stack is empty")

        # Get the top element
        top_index = self._da.length() - 1
        top_element = self._da.get_at_index(top_index)

        return top_element
