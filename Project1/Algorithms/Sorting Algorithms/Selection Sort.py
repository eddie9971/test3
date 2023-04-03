# 1. Selection Sort
# for i from 0 to n-1:
#     find the smallest number between number[i] and number[n-1]
#     swap the smallest number with numbers[i]


arr = [64, 25, 12, 22, 11]
# Traverse through all array elements


def selection_sort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list


print(selection_sort(arr))