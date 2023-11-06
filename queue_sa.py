# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3, Part 3
# Due Date: 11/6/2023
# Description: Queue ADT implementation using Static Array from A2 for storage


# Note: Changing any part of the pre-implemented methods (besides adding  #
#       default parameters) will cause the Gradescope tests to fail.      #


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class.
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty, False otherwise.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def print_underlying_sa(self) -> None:
        """
        Print underlying StaticArray. Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(self._sa)

    def _increment(self, index: int) -> int:
        """
        Move index to next position.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # ---------------------------------------------------------------------- #

    def enqueue(self, value: object) -> None: #passes the prescribed test
        """
            Add a new value to the end of the queue.
            Implemented with O(1) amortized runtime complexity using a circular buffer.
        """
        if self._current_size == self._sa.length():
            # If the buffer is full, double its size
            self._resize(self._current_size * 2)

        # Calculate the next position (circular buffer)
        next_back = self._increment(self._back)

        # Add the new value to the back of the queue
        self._sa[next_back] = value
        self._back = next_back

        self._current_size += 1

        # ... (other methods)

    def _resize(self, new_size: int) -> None:
        """
        Resize the circular buffer to a new size.
        Implemented with O(n) complexity.
        """
        new_buffer = StaticArray(new_size)

        # Copy elements to the new buffer
        for i in range(self._current_size):
            new_buffer[i] = self._sa[(self._front + i) % self._sa.length()]

        self._sa = new_buffer
        self._front = 0
        self._back = self._current_size - 1

    def dequeue(self) -> object: #passes the prescribed test
        """
                Remove and return the value at the beginning of the queue.
                Implemented with O(1) runtime complexity.
                """
        if self.is_empty():
            raise QueueException("Queue is empty")

        # Get the value at the front of the queue
        front_value = self._sa[self._front]

        # Update the front position (circular buffer)
        self._front = self._increment(self._front)
        self._current_size -= 1

        if self._current_size <= self._sa.length() // 4 and self._current_size > 4:
            # If the buffer is less than 25% full, shrink it to half its size
            self._resize(self._sa.length() // 2)

        return front_value

    def front(self) -> object: #passes the prescribed test
        """
            Return the value of the front element of the queue without removing it.
            Implemented with O(1) runtime complexity.
        """
        if self.is_empty():
            raise QueueException("Queue is empty")

        return self._sa[self._front]

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        pass
