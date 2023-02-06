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

    def print_list(self):
        temp = self.head
        while (temp):
            print("(", temp.bas,"-", temp.son, ")", end=" ")
            temp = temp.next
        print()

    def release_memory(self, addr, size):

        if self.head == None:
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
    
    def allocate_with_addr(self, addr, size):
        
        if None == self.head:
            print("Silinecek adres yok")
            return
        
        last = self.head
        prev = self.head
        while(last != None):
            if addr+size < last.bas:
                return
            elif addr >= last.bas and addr+size <= last.son:
                if addr == last.bas and addr+size == last.son:
                    if prev == last:
                        #prev = last.next
                        self.head = last.next
                        return
                    else:
                        prev.next = last.next
                        return
                elif addr > last.bas and addr+size < last.son:
                    new_node = Node(addr+size, last.son)
                    last.son = addr
                    new_node.next = last.next
                    last.next = new_node
                    return
                elif addr == last.bas and addr+size < last.son:
                    last.bas = addr + size
                    return
                elif addr > last.bas and addr+size == last.son:
                    last.son = addr
                    return
                else:
                    return
            else:
                prev = last
                last = last.next
    
   
    def allocate_with_size(self, size):
        prev = self.head
        last = self.head
        fit = self.head

        while(last):
            if((last.son - last.bas) == size):
                if(prev == last):
                    self.head = last.next
                    return
                else:
                    prev.next = last.next
                    return
            elif((last.son - last.bas) < (fit.son - fit.bas)):
                fit = last
            last = last.next   

        fit.bas += size                

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.release_memory(900, 5)
    llist.release_memory(912, 2)
    llist.release_memory(906, 2)
    llist.release_memory(914, 1)
    llist.release_memory(890, 5)
    llist.print_list()
    llist.allocate_with_addr(890, 5)
    llist.print_list()
    llist.allocate_with_addr(901, 2)
    llist.print_list()
    llist.allocate_with_addr(912, 3)
    llist.print_list()
    llist.release_memory(912, 5)
    llist.print_list()
    llist.allocate_with_size(1)
    llist.print_list()
    llist.allocate_with_size(1)
    llist.print_list()


    print()
