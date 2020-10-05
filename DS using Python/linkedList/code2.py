

# TODO : Find if loop exist in Linked List

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def showList(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def hasLoop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return 1

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n3

    ll = LinkedList()
    
    ll.head = n1

    if(ll.hasLoop()):
        print("Contains a loop!")
    else:
        print("Don't have any loop!")