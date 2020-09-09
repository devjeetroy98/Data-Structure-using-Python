class Queue:

    queue=list()

    def __init__(self, arr):        
        self.queue.extend(arr)

    def push(self,elem):
        self.queue.append(elem)

    def pop(self):
        deletedElem = self.queue.pop(0)
        return deletedElem

    def display(self):
        for i in self.queue:
            print(i, end=" ")

if __name__ == "__main__":
    n = int(input("Enter the no of elements: "));
    print("Enter elements: ")
    elements = list(map(int, input().split()))

    myQueue = Queue(elements)

    while(True):
        print("\n1. Push item into Queue\n2. Delete item from Queue\n3. Display the Queue\n4. Exit")
        choice = int(input("Enter your choice: "));
        if(choice == 1):
            elem = int(input("Enter element to be inserted: "))
            myQueue.push(elem)
        elif(choice == 2):
            elem = myQueue.pop()
            print("Deleted Element: ",elem);
        elif(choice == 3):
            myQueue.display()
        elif(choice == 4):
            break;
        else:
            print("Enter correct choice!!")