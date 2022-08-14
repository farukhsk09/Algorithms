#Explanation :
# quick sort depends on Divide and Conquer - Pick a Pivot and all less than should be in 
# left side array and high should be in right side array
# Partition method - pick the spot for the pivot , and rearrange lesser and greater elements
# Refer : https://www.geeksforgeeks.org/quick-sort/
#take a array , start and end index as input and return a sorted array
def quicksort(arr, low , high,order):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr,low,pi-1,order)
        quicksort(arr,pi+1,high,order)
    if order == "ASC":
        return
    else:
        arr.reverse()
        return
def partition(arr , low , high):
    pivot = arr[high]
    # always pick the left most position for pivot
    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            # Swap lesser element to left side of i
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    # pivot goes to its rightful place
    temp=arr[i+1]
    arr[i+1]=pivot
    arr[high]=temp
    return i+1


values =[24,5,6,2,9,14,70]
quicksort(values,0,6,"ASC")
print(values)
quicksort(values,0,6,"DESC")
print(values)