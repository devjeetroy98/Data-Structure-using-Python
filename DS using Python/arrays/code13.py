
# ! K-th Largest Sum Contiguous Subarray

# TODO : Generate the contiguous subarray and return (k-1) index element


def findKLargest(arr, k):
    i = 0
    n = len(arr)
    result = list()
    while( i < n):
        result.append(arr[i])
        diff = 0
        for j in range(i+1,n):
            diff += arr[j]
            result.append(arr[i] + diff)
        i += 1

    result.sort(reverse = True)
    return result[k-1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    ans = findKLargest(arr, k)
    print(ans)