import random

class collection:
    def __init__(self, items = []):
        self.items = items
        self.location = 0

    def addItem(self, item):
        self.items.append(item)

    def isEmpty(self) -> bool:
        return bool(self.items)

    def hasNext(self) -> bool:
        return self.location < len(self.items)

    def getNext(self):
        if self.hasNext():
            self.location += 1
            return self.items[self.location - 1]
        else:
            return None

    def resetNext(self):
        self.location = 0
        return

    def removeNext(self):
        if self.hasNext():
            self.items.pop(self.location)
        else:
            return None

    def removeLast(self):
        self.items.pop()
        return

    def addFirst(self, item):
        self.items.insert(0, item)
        return

    def NUKEMODE(self):
        self.items.clear()
        return

    def randomize(self):
        random.shuffle(self.items)
        return



class queue:
    def __init__(self, data = []):
        self.data = data

    def enqueue(self, item):
        self.data.append(item)
        return

    def dequeue(self):
        item = self.data[0]
        self.data = self.data[1:len(self.data)]
        return item

    def isEmpty(self):
        return bool(len(self.data)==0)

    def __repr__(self):
        return f"<Queue> {self.data}"


class stack:
    def __init__(self, data = []):
        self.data = data

    def push(self, item):
        self.data.append(item)
        return

    def pop(self):
        item = self.data[len(self.data)-1]
        self.data = self.data[0:len(self.data)-1]
        return item

    def isEmpty(self):
        return bool(self.data)

    def __repr__(self):
        return f"<Stack> {self.data}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        out = f"Node[{self.data}]"
        temp = self.next
        while temp:
            out += f"->Node[{temp.data}]"
            temp = temp.next
        return out

    def addNode(self, node):
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node
        else:
            self.next = node

class binaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = binaryTree(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = binaryTree(data)

    def __repr__(self):
        return f"{self.data}"

    def __str__(self):
        return f"{self.data}"

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
