
# ! Minimum swaps required to bring all elements less
# ! than or equal to k together

# TODO : 1. Count the elements <= k => count
# TODO : 2. Take a subarray of size "count", and find elements
# TODO : greater than k in that window, => "mink"
# TODO : 3. Minimum "mink" will be the answer

def findSwap(arr, k):
    n = len(arr)
    counter = 0
    bad = 0
    for i in arr:
        if i <= k:
            counter+=1
    
    try:
        j = 0
        minx = 0
        ans1 = 9999
        for i in range(n):
            temp = arr[j:j+counter]
            for it in temp:
                if it > k:
                    minx += 1
            ans1 = min([ans1, minx])
    except:
        pass

    arr = arr[::-1]

    try:
        j = 0
        minx = 0
        ans2 = 9999
        for i in range(n):
            temp = arr[j:j+counter]
            for it in temp:
                if it > k:
                    minx += 1
            ans2 = min([ans2, minx])
    except:
        pass

    return min([ans1,ans2])

if __name__ == "__main__":
    myList = list(map(int,input().split()))
    k = int(input())
    ans = findSwap(myList,k)
    print(ans)