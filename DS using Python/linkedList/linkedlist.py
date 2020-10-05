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

