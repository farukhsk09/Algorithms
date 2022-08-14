#Merge sort 
# Divide until you break to single elements 
# merge using iterator and replace each by position
# Refer : https://www.geeksforgeeks.org/merge-sort/
def mergesort(arr):
    left=0
    right=len(arr)
    if len(arr)>1:
        mid = (right - left)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i =j=k=0
        while(i < len(L) and j<len(R)):
            if L[i] < R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j <len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return

values =[24,5,6,2,9,14,70]
mergesort(values)
print(values)