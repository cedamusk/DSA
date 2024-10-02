# linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i

my_list=[1,3,5,7,9,11,13,15]
result=linear_search(my_list, 7)
print(f"Element found at index:{result}")
