from queue import Queue


class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x):
        self.q.put(x)
        for _ in range(self.q.qsize() - 1): self.q.put(self.q.get())

    def pop(self):
        return self.q.get()

    def top(self):
        r = self.q.get()
        self.q.put(r)
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        return r

    def empty(self):
        return not self.q.qsize()