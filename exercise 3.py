def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    for _ in range(len(list1) + len(list2)):
        if i < len(list1) and (j > len(list2) or list1[i] <= list2[j]):
           merged_list.append(list1[i])
           i+=1
        else:
           merged_list.append(list2[j])
           j+=1

    return merged_list

list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(merge_sorted_lists(list1, list2))
