# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 4
# Due Date: 11/6/23
# Description: Implementing a stack ADT with a singly linked list as storage

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None: #passes the prescribed test
        """
            Add a new element to the top of the stack.
        """
        new_node = SLNode(value)  # Create a new node with the given value
        new_node.next = self._head  # Set the new node's next reference to the current head
        self._head = new_node  # Update the head to the new node

    def pop(self) -> object: #passes the prescribed test
        """
            Remove the top element from the stack and return its value.
            If the stack is empty, raise a custom "StackException".
        """
        if self.is_empty():
            raise StackException("Stack is empty")

        popped_value = self._head.value  # Get the value of the top node
        self._head = self._head.next  # Update the head to the next node

        return popped_value

    def top(self) -> object:
        """
            Return the value of the top element of the stack without removing it.
            If the stack is empty, raise a custom "StackException".
        """
        if self.is_empty():
            raise StackException("Stack is empty")

        return self._head.value  # Return the value of the top node
