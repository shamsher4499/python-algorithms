

def median_two_sort_arrays(list1:list, list2:list):
    list1.extend(list2)
    list1.sort()
    div_data = len(list1)//2
    if len(list1)%2 != 0:
        return float(list1[div_data])
    if isinstance(len(list1)/2, float):
        if len(list1) == 2:
            return float(sum(list1)/2)
    if div_data == 1:
        return float(list1[1])
    else:
        v1, v2 = list1[div_data-1], list1[div_data]
        return float((v1+v2)/2)



l1 = []
l2 = [3,4]
print(median_two_sort_arrays(l1, l2))