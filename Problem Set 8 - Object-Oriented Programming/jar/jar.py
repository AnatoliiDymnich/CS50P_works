"""program as a cookie jar in which to store cookies"""

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        cookie = "🍪"
        return cookie * self.size

    def deposit(self, n):
        count = self.size + n
        if count > self.capacity or n < 0:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size or n < 0:
            raise ValueError
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n < 0:
            raise ValueError
        else:
            self._size = n
