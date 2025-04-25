import sys

sys.path.append('../Year2')

from Lessons import adts

x = adts.binaryTree(33)
x.addNode(50)
x.addNode(12)
x.addNode(14)

def print_yay(x):
    if x == None:
        return
    print_yay(x.left)
    print_yay(x.right)
    print(x.data)

print_yay(x)