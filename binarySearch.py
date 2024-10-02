def binary_search(data, target):
    left=0
    right=len(data)-1

    while left<=right:
        mid=(left+right)//2
        if data[mid]==target:
            return mid
        elif data[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

data=[2,5, 8, 12, 16, 23, 38]
target=16
result=binary_search(data, target)

if result !=1:
    print("Element found at index", result)
else:
    print("Element not found in the list")