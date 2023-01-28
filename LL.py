
class Node:

    # Function to initialise the node object
    def __init__(self, bas, son):
        self.bas = bas
        self.son = son
        self.next = None


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def add_to_end(self, addr, size):

        if self.head is None:
            new_node = Node(addr, addr+size)
            self.head = new_node
            return

        last = self.head
        if last.bas > addr+size :
            new_node = Node(addr, addr+size)
            new_node.next = self.head
            self.head = new_node
        elif last.next is None:
            new_node = Node(addr, addr+size)
            new_node.next = None
            last.next = new_node

        else:
            while (last.next.next):
                if  addr >= last.son and addr+size <=last.next.bas:
                    if addr != last.son and addr+size != last.next.bas:
                        new_node = Node(addr, addr+size)
                        new_node.next = last.next
                        last.next = new_node
                    elif addr is last.son and addr+size is last.next.bas:
                        last.son = last.next.son
                        last.next = last.next.next
                    elif addr is last.son and addr+size is not last.next.bas:
                        last.son = addr+size
                    else:
                        last.next.bas = addr+size
                else:
                    last = last.next  
            if addr is last.next.son:
                last.next.son = addr+size
            else:
                new_node = Node(addr, addr+size)
                last.next.next = new_node




    def printList(self):
        temp = self.head
        while (temp):
            print("(", temp.bas,"-", temp.son, ")", end=" ")
            temp = temp.next

    
    def deleteNode(self, position):
        temp = self.head
        prev = self.head
        
        for i in range(0, position):
            if i == 0 and position == 1:
                self.head = temp.next
            else:
                if i == position -1 and temp is not None:
                    prev.next = temp.next
                else:
                    prev = temp
                    if prev is None:
                        break
                    temp = temp.next

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.add_to_end(900, 5)
    llist.add_to_end(908, 2)
    llist.add_to_end
    llist.printList()
    print()
