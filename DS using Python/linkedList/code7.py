
# TODO : Finding intersection of 2 sorted linkedlist

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
    
    def findIntersection(self,temp2):
        i,j = self.head,temp2.head
        ll3 = LinkedList()
        ll3.head = None
        pointer = None

        while(i and j):
            if(i.data == j.data):
                n = Node(i.data)
                if(ll3.head == None):
                    # ! Assign head to starting node
                    ll3.head = n
                    pointer = n
                    # ! Move both to next
                    i = i.next
                    j = j.next
                else:
                    # ! Add new node in the linkedlist
                    pointer.next = n
                    pointer = pointer.next
                    # ! Move both to next
                    i = i.next
                    j = j.next

            # ! Increment the smaller data pointer
            elif(i.data < j.data):
                i = i.next
            else:
                j = j.next
        
        return ll3.head

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(6)
    n6 = Node(7)
    n7 = Node(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None
    ll1 = LinkedList()    
    ll1.head = n1

    m1 = Node(2)
    m2 = Node(4)
    m3 = Node(6)
    m4 = Node(8)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = None
    ll2 = LinkedList()
    ll2.head = m1

    ll1.showList()
    ll2.showList()
    print("The intersection nodes are:")
    ans = ll1.findIntersection(ll2)
    while(ans):
        print(ans.data, end = " ")
        ans = ans.next

    