class Jar():
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("capacity must be non-negative integer")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value > self.capacity:
            raise ValueError("Cookie jar’s capacity exceded")
        elif value < 0:
            raise ValueError("Not enouhg cookies")
        self._size = value

# chaba_jar = Jar(5)
# chaba_jar.deposit(3)
# print(chaba_jar)
# chaba_jar.deposit(2)
# print(chaba_jar)

# chaba_jar.withdraw(6)
# print(chaba_jar)



