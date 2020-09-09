def linearSearch(array, searchKey):
    for i in array:
        if(i==searchKey):
            return array.index(i)

if __name__ =="__main__":

    n = int(input("Enter the no of elements: "))
    array = list(map(int, input().split()))
    searchKey = int(input("Enter seachable element: "))

    idx = linearSearch(array, searchKey)

    if(idx):
        print("Position: ",idx+1)
    else:
        print("Element doesn't exist in the array!")

        