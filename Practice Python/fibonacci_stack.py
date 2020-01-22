class FibonacciStack:
    def __init__(self):
        self.items = []
        self.popping = 0
        self.fibonacci = 0

    def push(self, item):
        self.items.append(item)

    def fibo(self, x):
        while x >= 0:
            if x == 0:
                self.fibonacci = 0
                return self.fibonacci
            elif x == 1:
                self.fibonacci = 1
                return self.fibonacci
            self.fibonacci = self.fibo(x - 1) + self.fibo(x - 2)
            return self.fibonacci


    def pop(self):
        if len(self.items) <= 0:
            return False
        else:
            self.popping = self.popping + 1
            print(self.fibo(self.popping - 1) * self.items[-1])
            self.items = self.items[:-1]

    def is_empty(self):
        return (len(self.items) == 0)
