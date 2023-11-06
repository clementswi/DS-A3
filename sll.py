# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 1, Singly-Linked list implementation
# Due Date: 11/6/23
# Description: Singly-Linked list implementation, based on SLNode class.


from SLNode import SLNode


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None: #passes the prescribed test
        """
                Add a new node with the given value at the beginning of the list.
                This method has O(1) runtime complexity.
                """
        new_node = SLNode(value)  # Create a new node with the provided value

        # Make the new node point to the current first node (after the sentinel)
        new_node.next = self._head.next

        # Update the sentinel's reference to the new node, making it the new first node
        self._head.next = new_node




    def insert_back(self, value: object) -> None: #passes the prescribed test
        """
            Add a new node with the given value at the end of the list.
            This method has O(N) runtime complexity.
        """
        new_node = SLNode(value)  # Create a new node with the provided value

        # If the list is empty, simply make the new node the first node
        if self.is_empty():
            self._head.next = new_node
        else:
            # Find the current last node
            current = self._head.next
            while current.next is not None:
                current = current.next

            # Add the new node after the current last node
            current.next = new_node

    def insert_at_index(self, index: int, value: object) -> None: #passes the prescribed test
        """
                Insert a new node with the given value at the specified index position in the linked list.
                Index 0 refers to the beginning of the list (right after the front sentinel).
                If the provided index is invalid, the method raises a custom “SLLException”.
                This method has O(N) runtime complexity.
                """
        if index < 0 or index > self.length():
            raise SLLException("Invalid index")

        new_node = SLNode(value)  # Create a new node with the provided value

        current = self._head
        for _ in range(index):
            current = current.next  # Traverse to the node just before the desired index

        new_node.next = current.next  # Connect the new node to the next node
        current.next = new_node  # Connect the previous node to the new node

    def remove_at_index(self, index: int) -> None: #passes the prescribed test
        """
            Remove the node at the specified index position from the linked list.
            Index 0 refers to the beginning of the list (right after the front sentinel).
            If the provided index is invalid, the method raises a custom “SLLException”.
            This method has O(N) runtime complexity.
        """
        if index < 0 or index >= self.length():
            raise SLLException("Invalid index")

        current = self._head
        for _ in range(index):
            current = current.next  # Traverse to the node just before the desired index

        # Remove the node at the specified index by updating the 'next' reference of the previous node
        current.next = current.next.next

    def remove(self, value: object) -> bool: #passes both prescribed tests
        """
            Remove the first node that matches the provided value from the linked list.
            Returns True if a node was removed, and False otherwise.
            This method has O(N) runtime complexity.
        """
        current = self._head

        while current.next is not None:
            if current.next.value == value:
                # Found a node with the matching value, remove it
                current.next = current.next.next
                return True

            current = current.next

        return False  # The value was not found in the list

    def count(self, value: object) -> int: #passes the prescribed test
        """
            Count the number of elements in the list that match the provided value.
            Returns the count of matching elements.
            This method has O(N) runtime complexity.
        """
        count = 0
        current = self._head.next  # Start from the first node

        while current is not None:
            if current.value == value:
                count += 1
            current = current.next  # Move to the next node

        return count

    def find(self, value: object) -> bool: #passes the prescribed test
        """
            Check whether the provided value exists in the linked list.
            Returns True if the value is found, and False otherwise.
            This method has O(N) runtime complexity.
        """
        current = self._head.next  # Start from the first node

        while current is not None:
            if current.value == value:
                return True  # Found the value

            current = current.next  # Move to the next node

        return False  # The value was not found in the list

    def slice(self, start_index: int, size: int) -> "LinkedList": #passes the prescribed tests
        """
                Create and return a new LinkedList containing nodes from the original list, starting
                at the specified start_index and up to the requested size.
                If the provided start index is invalid, or if there are not enough nodes between the
                start index and the end of the list to make a slice of the requested size, this method
                raises a custom “SLLException”.
                The runtime complexity of this implementation is O(N).
                """
        if start_index < 0 or start_index >= self.length():
            raise SLLException("Invalid start index")

        current = self._head.next  # Start from the first node
        for _ in range(start_index):
            if current is None:
                raise SLLException("Invalid start index")
            current = current.next  # Traverse to the specified start_index

        new_list = LinkedList()  # Create a new linked list to hold the slice
        new_list._head = SLNode(None)  # Initialize the new list's sentinel node

        slice_size = 0  # Counter to keep track of the number of nodes added to the slice
        slice_current = new_list._head  # Pointer to the last node in the new list

        while current is not None and slice_size < size:
            # Copy the value of the current node to the new list
            slice_current.next = SLNode(current.value)
            slice_current = slice_current.next

            current = current.next  # Move to the next node
            slice_size += 1

        if slice_size < size:
            raise SLLException("Not enough nodes to create the requested slice")

        return new_list
