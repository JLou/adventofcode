class Node():
    def __init__(self, name='root', children=None, parent=None, isFile=False, size=0):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
        self.isFile=isFile
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        self.children.append(node)


with open('inputs/07') as f:
    lines = f.read().splitlines()

root = Node('/', None, None)
curr = root
for l in lines[1:]:
    if l == "$ cd ..":
        curr = curr.parent
    elif l.startswith("$ cd"):
        for child in curr.children:
            if child.name == l[5:]:
                curr = child
                break            
    elif l == "$ ls":
        continue
    elif l.startswith("dir"):
        node = Node(l[4:], None, curr, False, 0)
        curr.add_child(node)
    else:
        s, f = l.split(" ")
        node = Node(f, None, curr, True, int(s))
        curr.add_child(node)


smallnodes = []
nodes=[]
def compute_size(node:Node):
    if node.isFile or node.size != 0:
        return node.size
    else:
        s = sum(map(compute_size, node.children))
        node.size = s
        if s <= 100000:
            smallnodes.append(s)
        nodes.append(s)
        return s

compute_size(root)

print(sum(smallnodes))

free = 70000000 - root.size
required= 30000000 - free
print(min(i for i in nodes if i > required))
