import random
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

class Stack:
    def __init__(self, limit=1000):
        self.top_node = None
        self.size = 0
        self.limit = limit
    def push(self, value):
        if not self.is_full():
            item = Node(value)
            item.set_next_node(self.top_node)
            self.top_node = item
            self.size += 1
        else:
            print("Nothing to see here, move along.")
    
    def pop(self):
        if not self.is_empty():
            popped = self.top_node
            self.top_node = popped.get_next_node()
            self.size -= 1
            return popped.get_data()
        else:
            print("WOW! Easy there buddy, it's a full house.")
  
    def peek(self):
        if not self.is_empty():
	        return self.top_node.get_data()
        else:
            print("Nothing to see here, move along.")
     
    
    def is_full(self):
        return self.size == self.limit
    
    def is_empty(self):
        return self.size == 0
cards = Stack(20)
created_cards=[]
while not(cards.is_full()):
    nums=random.randint(1,9)
    colors=random.choice(["Red","Blue", "Green", "Yellow"])
    if [colors,nums] not in created_cards:
        cards.push([colors,nums])
        created_cards.append([colors,nums])    
player1=[]
player2=[]
for i in range(1,6):
    player1.append(cards.pop())
    player2.append(cards.pop()) 
print("player 1 cards")
for i in range(len(player1)):
    print("%s- %s-%s" %(i+1 ,player1[i][0],player1[i][1]))
print("player 2 cards")
for i in range(len(player1)):
    print("%s- %s-%s" %(i+1 ,player2[i][0],player2[i][1]))
print("First card in deck: %s-%s"%(cards.peek()[0],cards.peek()[1]))



while not (cards.is_empty()):
    print(cards.pop())
