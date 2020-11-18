def sort(target_list):
    for i in range(len(target_list) - 1):
        for j in range(i + 1, len(target_list)):
            if target_list[i] < target_list[j]:
                target_list[i], target_list[j] = target_list[j], target_list[i]
    # return target_list


list01 = [342, 45, 65, 7, 8, 98, 9, 34]
sort(list01)
print(list01)
