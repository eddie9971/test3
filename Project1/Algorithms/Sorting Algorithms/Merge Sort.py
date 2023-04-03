# MergeSort(arr[], l,  r)
# If r > l
# Find the middle point to divide the array into two halves:
# middle m = l + (r – l)/2
# Call mergeSort for first half:
# Call mergeSort(arr, l, m)
# Call mergeSort for second half:
# Call mergeSort(arr, m + 1, r)
# Merge the two halves sorted in steps 2 and 3:
# Call merge(arr, l, m, r)

def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    
        # [2,1,3,5,4]
        # [2,1]  [3,5,4]
        # [2][1]  [3][5,4]
        #             [5][4]
        #



