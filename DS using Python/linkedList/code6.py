
# TODO : Swap any two nodes

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

    def findNodeAndPrev(self, data):
        curr = self.head
        prev = None
        while(curr):
            if(curr.data == data):
                return [curr, prev]
            prev = curr
            curr = curr.next

    def swapNodes(self, data1, data2):
        p1, prev1 = self.findNodeAndPrev(data1)
        p2, prev2 = self.findNodeAndPrev(data2)
        if( p1 and p2 and prev1 and prev2):
            adr = p2.next
            prev1.next = p2
            p2.next = p1.next
            prev2.next = p1
            p1.next = adr

        # ! For handling,if one data is head of linkedlist
        
        elif(p1 and p2 and prev2):
            adr = p2.next
            p2.next = p1.next
            prev2.next = p1
            p1.next = adr
            self.head = p2
        else:
            pass       

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(15)
    n3 = Node(12)
    n4 = Node(18)
    n5 = Node(16)
    n6 = Node(20)
    n7 = Node(14)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    ll = LinkedList()
    
    ll.head = n1

    print("Before Swapping:")
    ll.showList()
    ll.swapNodes(12,14)
    print("After Swapping:")
    ll.showList()