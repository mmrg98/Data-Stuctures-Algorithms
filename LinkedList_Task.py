from datetime import datetime
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
  
    def get_data(self):
        return self.data
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, data=None):
        self.head_node = Node(data)
    
    def get_head_node(self):
        return self.head_node
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    def get_data(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_data() != None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    def remove_node(self, data):

        current_node = self.get_head_node()
        if current_node.get_data() == data:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_data() == data:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
n1=Node([0,"I was born"])
n2=Node([4,"I attended KG"])
n3=Node([7,"I attended school"])
LinkedList1=LinkedList()
LinkedList1.head_node=n1
n1.set_next_node(n2)
n2.set_next_node(n3)
age=int(input("Enter your age: "))
temp = LinkedList1.get_head_node()
while temp.get_data()[0]<age: 
    cur_age=temp.get_data()[0]+1
    if temp.next_node != None and temp.get_next_node().get_data()[0] ==cur_age:
        temp = temp.next_node        
    else:
        print(" type a highlight about your %d year: "% cur_age)
        n=n1=Node([cur_age,input("")],temp.get_next_node())
        temp.set_next_node(n)
        temp = n
print(LinkedList1.get_data())


