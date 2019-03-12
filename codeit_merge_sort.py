def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i < len(list1):
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

    if j < len(list2):
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

    return merged_list

def merge_sort(my_list):
    # Base Case
    if len(my_list) <= 1:
        return my_list

    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    return merge(merge_sort(left), merge_sort(right))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)
