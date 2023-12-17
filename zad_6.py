def process_lists(list1, list2):
    merged_list = list(set(list1 + list2))
    powered_list = [x**3 for x in merged_list]
    return powered_list