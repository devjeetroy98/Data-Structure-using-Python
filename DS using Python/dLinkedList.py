class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None

    def showList(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def findEnvironment(self, sdata):
        flag=0
        temp = self.head
        while(temp):
            if(temp.data == sdata):
                print("Before Element: ", temp.prev.data)
                print("After Element: ", temp.next.data)
                flag=1
                break
            else:
                temp = temp.next
        if(flag==0):
            print("Element doesn't exist in Doubly Linked List")

if __name__ == "__main__":
    n = int(input("How many nodes wanna create? "))
    mynodeVal = list(map(int, input().split()))
    nodesList = list()
    for i in mynodeVal:
        nodename = "node"+ str(i)
        nodename = Node(i)
        nodesList.append(nodename)

    myList = DoubleLinkedList()
    myList.head = nodesList[0]

    for i in range(len(nodesList)):
        try:
            nodesList[i].prev = nodesList[i-1]
            nodesList[i].next = nodesList[i+1]
        except:
            continue
    
    while(True):
        print("\n1. Print List\n2. Find Environment\n3. Exit")
        choice = int(input())
        if(choice == 1):
            myList.showList()
        elif(choice == 2):
            elem = int(input("Search Value: "))
            myList.findEnvironment(elem)
        elif(choice == 3):
            break
        else:
            print("Enter correct choice!")