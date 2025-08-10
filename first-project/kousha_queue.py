class Queue:
    def __init__(self):
        self.queue = []
        front = 0
        rear = -1
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0] if len(self.queue) != 0 else raise Exception ("Array is Empty!!!")
    
    def display(self):
        print(self.queue)