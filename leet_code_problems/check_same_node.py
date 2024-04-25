

def check_graph_code(list1, list2):
    """
    Function to check if the two graphs are same or not
    """
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


print(check_graph_code([1, None, 3], [1, None, 4]))