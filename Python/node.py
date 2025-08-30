class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(244)
node2 = Node(3)
node3 = Node(11)
node4 = Node(45)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

#TRAVERSE A LINKED LIST
def TranverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=' -> ')
        currentNode=currentNode.next
    print("null")


TranverseAndPrint(node2)

#FIND THE LOWEST VALUE IN A LINKED LIST
def findLowestValue(head):
    minValue = head.data # Assume the head as the min value
    currentNode = head.next # Start checking from the next node

    while currentNode:      # While there are still nodes to check
        if currentNode.data < minValue:
            minValue = currentNode.data      # Update minValue if a smaller value is found
        currentNode = currentNode.next   # Move to the next node
    return minValue     # Return the lowest value found

print("the min value in the linked list is", findLowestValue(node1))