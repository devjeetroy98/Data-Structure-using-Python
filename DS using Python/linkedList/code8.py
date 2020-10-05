
# ! TODO : Find intersection point of 2 linked list

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

    def returnLength(self):
        temp = self.head
        counter = 0
        while(temp):
            counter += 1
            temp = temp.next
        
        return counter

    def findIntersectionPoint(self, temp2):
        p1,p2 = self.head, temp2.head
        n1 = self.returnLength()
        n2 = temp2.returnLength()
        count = 0
        d = abs(n1-n2)

        # ! Travel the extra length of the longer linkedlist
        if n1 > n2:
            for i in range(d):
                p1 = p1.next
        else:
            for i in range(d):
                p2 = p2.next

        # ! Now length of both the linkedlist are same
        while(p1.next != p2.next):
            count += 1
            p1 = p1.next
            p2 = p2.next

        # ! Store the next of current node and go to the next node.
        # ! We will return the data and address of the same node.
        adr = p1.next
        p1 = p1.next
        return [p1.data, adr]

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

    m1 = Node(11)
    m2 = Node(17)
    m1.next = m2
    m2.next = n5
    ll2 = LinkedList()
    ll2.head = m1

    print("First Linked List:")
    ll1.showList()
    print("Second Linked List:")
    ll2.showList()
    print("The intersection point is:")
    ans = ll1.findIntersectionPoint(ll2)
    print("Value:",ans[0])
    print("Address:",ans[1])