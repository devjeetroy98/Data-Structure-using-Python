def binarySearch(array,l,r, value):
    if(l<=r):
        mid = (l+r)//2
        if(array[mid]==value):
            return mid
        elif(value<array[mid]):
            return binarySearch(array,l, mid-1,value)
        elif(value>array[mid]):
            return binarySearch(array,mid+1,r,value)
        else:
            pass

if __name__ =="__main__":

    n = int(input("Enter the no of elements: "))

    array = list(map(int, input().split()))

    searchKey = int(input("Enter seachable element: "))
    array.sort()

    print("Sorted: ",array)
    idx = binarySearch(array, 0, n-1, searchKey)
    if(idx):
        print("Position: ",idx+1)
    else:
        print("Element doesn't exist in the array!")

