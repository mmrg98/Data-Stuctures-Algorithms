class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node 
    def set_next_node(self, next_node):
        self.next_node = next_node   
    def get_next_node(self):
        return self.next_node   
    def get_data(self):
        return self.data
class Queue:
     def __init__(self, limit=None):
        self.front_node = None
        self.back_node = None
        self.length = 0
        self.limit = limit
     def is_full(self):
        return self.length == self.limit if self.limit else False
     def is_empty(self):
        return self.length == 0  
     def get_length(self):
        return self.length
     def peek(self):
        if not self.is_empty():
            return self.front_node.get_data()
     def enqueue(self, data):
        if not self.is_full():
            if data> 12:
                d=[]
                while data>12:
                    t=12
                    data=data-t
                    d.append(t)
                d.append(data)
                for i in d:
                    new_node = Node(i)
                    if self.is_empty():
                        self.front_node = new_node
                        self.back_node = new_node
                    else:
                        self.back_node.set_next_node(new_node)
                        self.back_node = new_node
                    self.length += 1
                    

            else:
                new_node = Node(data)
                if self.is_empty():
                    self.front_node = new_node
                    self.back_node = new_node
                else:
                    self.back_node.set_next_node(new_node)
                    self.back_node = new_node
                self.length += 1
     def dequeue(self):
        if not self.is_empty():
            removed_node = self.front_node
            if self.get_length() == 1:
                self.front_node = None
                self.back_node = None
            else:
                self.front_node = removed_node.get_next_node()
            self.length -= 1
            return removed_node.get_data()
def waitingTime(queue):
    q1=Queue()
    t=queue
    waiting=0
    if not t.is_empty():
        while not t.is_empty():
            waiting=waiting +(t.peek()*30)
            q1.enqueue(t.dequeue())
        print("waiting time is: %d seconds"% waiting)    
    else:      
        print("waiting time is: %d seconds"% waiting)
    while not q1.is_empty():    
            queue.enqueue(q1.dequeue())
qu=Queue()
waitingTime(qu)
qu.enqueue(24)
waitingTime(qu)
print(qu.dequeue())
waitingTime(qu)
#qu.enqueue(5)
#qu.enqueue(8)
#qu.enqueue(12)
#print(qu.dequeue())
#waitingTime(qu)
#qu.enqueue(15)
#waitingTime(qu)
