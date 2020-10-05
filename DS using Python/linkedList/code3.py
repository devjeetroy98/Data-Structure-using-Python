

# TODO : Find if linkedlist is Palindrome

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

    def isPalindrome(self):
        temp = self.head
        datas = list()
        while(temp):
            datas.append(temp.data)
            temp = temp.next
        
        if(datas == datas[::-1]):
            return True
        else:
            return False

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(3)
    n6 = Node(2)
    n7 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    ll = LinkedList()
    
    ll.head = n1

    if(ll.isPalindrome()):
        print("This is a palindromic linked list.")
    else:
        print("This is not a palindromic linked list.")