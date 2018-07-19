# This is a stack
class Stack:
    top = 0
    maximum_size = 5
    # this sets up the stack
    def __init__(self, list):
        self.stack = []
    #this removes an item from the stack
    def pop(self):
        self.stack.pop()
        top = len(self.stack)
    #this adds an item to the stack
    def push(self,data):
        self.stack.append(data)
        top =len(self.stack)
    #this displays the stack
    def listContents(self):
        print(self.stack)
    #this see if the stack is full   
    def isFull(self):
        if self.top == self.maximum_size:
            print("Stack is full")
            return True
    #This see if the stack is empty    
    def isEmpty(self):
        if self.top == 0:
            print("Stack is empty")
            return True 




