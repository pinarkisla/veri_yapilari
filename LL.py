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

        if self.head == None:
            print("pk ")
            new_node = Node(addr, addr+size)
            self.head = new_node
            return

        else:    
            last = self.head
            while (last != None):
                if(last.next == None):
                    if last.bas > addr+size:
                        new_node = Node(addr, addr+size)
                        new_node.next = self.head
                        self.head = new_node
                        return
                    elif last.bas == addr+size:
                        last.bas = addr
                        return
                    elif last.son == addr:
                        last.son = addr+size
                        return
                    elif last.son < addr:
                        new_node = Node(addr, addr+size)
                        last.next = new_node
                        return
                elif last.bas > addr+size:
                    new_node = Node(addr, addr+size)
                    new_node.next = self.head
                    self.head = new_node
                    return
                elif last.bas == addr+size:
                    last.bas = addr
                    return
                elif  addr >= last.son and addr+size <=last.next.bas:
                    if addr != last.son and addr+size != last.next.bas:
                        new_node = Node(addr, addr+size)
                        new_node.next = last.next
                        last.next = new_node
                        return
                    elif addr == last.son and addr+size == last.next.bas:

                        last.son = last.next.son
                        last.next = last.next.next
                        return
                    elif (addr == last.son and addr+size != last.next.bas):
                        last.son = addr+size
                        return
                    elif addr != last.son and addr+size == last.next.bas:
                        last.next.bas = addr
                        return
                    else:
                        print("Araya eleman eklemede hata")
                        return
                else:
                    last = last.next

    def printList(self):
        temp = self.head
        while (temp):
            print("(", temp.bas,"-", temp.son, ")", end=" ")
            temp = temp.next
        print()
    
    def delete_node(self, position):
        temp = self.head
        prev = self.head
        
        for i in range(0, position):
            if i == 0 and position == 1:
                self.head = temp.next
            else:
                if i == position -1 and temp != None:
                    prev.next = temp.next
                else:
                    prev = temp
                    if prev == None:
                        break
                    temp = temp.next

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.add_to_end(900, 5)
    llist.add_to_end(912, 2)
    llist.add_to_end(906, 2)
    llist.add_to_end(914, 1)
    llist.add_to_end(890, 5)
    llist.printList()
    llist.delete_node(3)
    llist.printList()
    print()
