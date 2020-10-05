

# TODO : Delete duplicates from an unsorted linked list

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

    def deleteDuplicates(self,n):
        temp = self.head
        fast = temp.next
        dataset = list()
        dataset.append(temp.data)
        while(fast):
            if fast.data not in dataset:
                dataset.append(fast.data)
                temp.next = fast
                fast = fast.next
                temp = temp.next
            else:
                fast = fast.next
        temp.next = None

        

if __name__ == "__main__":
    n1 = Node(4)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(4)
    n5 = Node(3)
    n6 = Node(4)
    n7 = Node(2)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    ll = LinkedList()
    
    ll.head = n1

    print("Created List:")
    ll.showList()
    print("After deleting duplicates:")
    ll.deleteDuplicates(7)
    ll.showList()