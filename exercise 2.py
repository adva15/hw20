def Remove_duplicates(list_r):
    duplicates = []
    for i in range(len(list_r)):
        for _ in range(i + 1,len(list_r)):
            if list_r[i] == list_r[_] and list_r[i] not in duplicates:
                duplicates.append(list_r[i])
    return duplicates

print(Remove_duplicates([1, 1, 2, 3, 4, 4, 4]))


