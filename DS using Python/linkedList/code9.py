
# ! TODO : Reverse a linked list

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
    
    def reverseLinkedList(self):
        temp = self.head
        curr = self.head
        prev = curr

        # ! Special treatment for head
        curr = curr.next
        prev.next = None

        while(curr):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp

        self.head = temp

if __name__ == "__main__":
    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(6)
    n4 = Node(8)
    n5 = Node(9)
    n6 = Node(1)
    n7 = Node(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None
    ll1 = LinkedList()    
    ll1.head = n1

    print("The Linked List is:")
    ll1.showList()

    ll1.reverseLinkedList()

    print("The reversed Linked List is:")
    ll1.showList()