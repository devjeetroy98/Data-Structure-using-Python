
# ! Rearrange an array in order – 
# ! smallest, largest, 2nd smallest, 2nd largest, and so on

# TODO: Sort the array and use 2 pointers algorithm

def patternArray(arr, n):
    arr.sort()
    res = list()

    # * Using 2 pointers algorithm
    i = 0
    j = n-1
    while(i < j):
        res.extend([arr[i], arr[j]])
        i += 1
        j -= 1
    
    if(n % 2 != 0):
        res.append(arr[n//2])

    return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = patternArray(arr, len(arr))
    print(result)