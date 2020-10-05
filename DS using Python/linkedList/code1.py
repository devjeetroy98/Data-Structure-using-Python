

# TODO : Make basic functions in Linked List

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

    def findIndex(self, idx):
        if idx < 0:
            return None
        temp = self.head
        counter = 0
        while(temp):
            temp = temp.next
            counter +=1
            if(counter == idx):
                return temp
        return None

    def findValue(self, val):
        temp = self.head
        counter = 0
        while(temp):
            if(temp.data == val):
                return counter
            temp = temp.next
            counter +=1
        return -1

    def lenOfLinkedList(self):
        temp = self.head
        counter = 0
        while(temp):
            temp = temp.next 
            counter += 1
        return counter

    def insertNew(self, data, index):
        curr = self.findIndex(index)
        try:
            pastVal = curr.data 
            currNext = curr.next
            curr.data = data
            n = Node(pastVal)
            curr.next = n
            n.next = currNext
        except:
            pass

    def deleteByIndex(self, index):
        curr = self.findIndex(index-1)
        curr.next = curr.next.next

    def deleteByValue(self, value):
        pos = self.findValue(value)
        curr = self.findIndex(pos-1)
        try:
            curr.next = curr.next.next
        except:
            pass

if __name__ == "__main__":
    mynodeVal = list(map(int, input().split()))

    nodesList = list()
    for i in mynodeVal:
        nodename = Node(i)
        nodesList.append(nodename)

    myList = LinkedList()
    myList.head = nodesList[0]

    for i in range(len(nodesList)):
        try:
            nodesList[i].next = nodesList[i+1]
        except:
            pass

    myList.showList()
    print(myList.lenOfLinkedList())
    myList.deleteByValue(30)
    myList.showList()
    print(myList.lenOfLinkedList())