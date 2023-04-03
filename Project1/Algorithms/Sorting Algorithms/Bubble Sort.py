# Bubble Sort
# Repeat n-1 times:
#     for i from 0 to n-2:
#         If numbers [i] and numbers [i+1] out of order:
#             Swap them
#         If no swap
#         quit()
# throwing the largest number to the last index

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1, Swap if the element found is greater, than the next element
            if arr[j] > arr[j+1]: #
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Driver code to test above
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]

    print(bubbleSort(arr))