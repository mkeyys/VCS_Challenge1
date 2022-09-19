def search(arr,left, right, x):
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return search(arr, mid+1, right, x)
        else:
            return search(arr, left, mid-1, x )
    else:
        return -1
arr = input("Array: ").split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
num_x = int(input("x = "))
result = search(arr, 0, len(arr)-1, num_x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
