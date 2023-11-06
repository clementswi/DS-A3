# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 5
# Due Date: 11/6/23
# Description: Implementing a queue ADT with a singly linked list as storage


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
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
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None: #passes the prescribed test
        """
            Add a new value to the end of the queue.
        """
        new_node = SLNode(value)  # Create a new node with the given value

        if self.is_empty():
            self._head = new_node  # If the queue is empty, set both head and tail to the new node
            self._tail = new_node
        else:
            self._tail.next = new_node  # Set the current tail's next reference to the new node
            self._tail = new_node  # Update the tail to the new node

    def dequeue(self) -> object: #passes the prescribed test
        """
            Remove and return the value from the beginning of the queue.
            If the queue is empty, raise a custom "QueueException".
        """
        if self.is_empty():
            raise QueueException("Queue is empty")

        dequeued_value = self._head.value  # Get the value of the current head node
        self._head = self._head.next  # Update the head to the next node

        if self._head is None:
            # If the queue becomes empty after dequeue, also update the tail to None
            self._tail = None

        return dequeued_value

    def front(self) -> object: #passes the prescribed test
        """
            Return the value of the front element of the queue without removing it.
            If the queue is empty, raise a custom "QueueException".
        """
        if self.is_empty():
            raise QueueException("Queue is empty")

        return self._head.value  # Return the value of the current head node
