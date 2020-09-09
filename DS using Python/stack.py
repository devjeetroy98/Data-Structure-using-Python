class Stack:

    stack=list()

    def __init__(self, arr):        
        self.stack.extend(arr)

    def push(self,elem):
        self.stack.append(elem)

    def pop(self):
        deletedElem = self.stack.pop()
        return deletedElem

    def display(self):
        for i in self.stack:
            print(i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter the no of elements: "));
    print("Enter elements: ")
    elements = list(map(int, input().split()))

    myStack = Stack(elements)

    while(True):
        print("\n1. Push item into Stack\n2. Pop item from Stack\n3. Display the stack\n4. Exit")
        choice = int(input("Enter your choice: "));
        if(choice == 1):
            elem = int(input("Enter element to be inserted: "))
            myStack.push(elem)
        elif(choice == 2):
            elem = myStack.pop()
            print("Deleted Element: ",elem);
        elif(choice == 3):
            myStack.display()
        elif(choice == 4):
            break;
        else:
            print("Enter correct choice!!")
