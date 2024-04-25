fix_list = []
def call_data(list_data):
    for item in list_data:
        if isinstance(item, list):
            call_data(item)
        else:
            fix_list.append(item)


call_data([1, 2, [3, 4, [5, 6]], 7, 8, [9, 10]])
print(fix_list)