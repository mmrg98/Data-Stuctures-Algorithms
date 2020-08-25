class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, node):
        if len(self.children) <2:
            self.children.append(node)
            print("added a %s to %s" % (node.data,self.data))
        else:
            print("child is an orphan")

    def remove_child(self, node):
        self.children = [child for child in self.children if child is not node]
    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.data)
            nodes += current_node.children
    def get_child(self,data):
        for child in self.children:
            if child.data==data:
                return child
        return None
    
root=TreeNode("family")
inp=input("enter child full name (done if finished): ")
while inp!="done":
    current_node=root
    names = inp.split()[::-1]
    first=names.pop()
    last=names.pop(0)
    
    if current_node.data==last:
        if names:
            for name in names:
                child= current_node.get_child(name)
                if child:
                    current_node=child
                elif root.get_child(child):
                    new_node=TreeNode(name)
                    current_node.add_child(new_node)
                    current_node=new_node
                else:
                    print("parent does not exist")
                    break
        current_node.add_child(TreeNode(first))

    inp=input("enter child full name (done if finished): ")
    

root.traverse()
        

