
# ! K’th Smallest/Largest Element in Unsorted Array


# TODO: Sort the array and return element at (k-1) index

def findKLargest(arr, k):
    arr.sort()
    return arr[k-1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = int(input())
    ans = findKLargest(arr, n)
    print(ans)