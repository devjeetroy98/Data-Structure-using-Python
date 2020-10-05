
# ! Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’

# TODO : arr[i] = j then make arr[j] = i

def reIndex(arr, n):
    result = list([0] * n)

    for i in range(n):
        newIdx = arr[i]
        result[newIdx] = i

    return result

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    ans = reIndex(arr, len(arr))
    print(ans)