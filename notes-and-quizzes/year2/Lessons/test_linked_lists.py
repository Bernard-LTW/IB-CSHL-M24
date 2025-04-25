from adts import Node

my_list = Node("Alice")
print(my_list)

bob_node = Node("Bob")
my_list.addNode(bob_node)
print(my_list)

amy_node = Node("Amy")
carl_node = Node("Carl")
test_7 = Node("halo")

my_list.next.addNode(carl_node)
my_list.addNode(amy_node)
my_list.next.next.addNode(test_7)
print(my_list)
