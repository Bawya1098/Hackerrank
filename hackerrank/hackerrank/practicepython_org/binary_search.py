from math import ceil


def find_midindex(search_list):
    length = len(search_list)
    low_index = 0
    high_index = length
    mid_index = ceil((low_index + high_index) / 2)
    return mid_index


def finding_element(search_list):
    print("enter element to be searched:")
    search_element = int(input())
    sorted_list = sorted(search_list)
    mid_index = find_midindex(sorted_list)
    mid_value = sorted_list[mid_index] - 1
    if search_element == mid_value:
        print("search_element is at index:", mid_index)
    elif search_element < mid_value:
        for elements in range(0, sorted_list[mid_index]):
            if search_element == sorted_list[elements]:
                print("search_element is at position:", elements)
    elif search_element > mid_value and search_element in sorted_list:
        for elements in range(sorted_list[mid_index], len(sorted_list)):
            if search_element == sorted_list[elements]:
                print("search_element is at position:", elements)
    else:
        print("Element not  Present")


finding_element([1, 2, 9, 3, 4, 5, 6, 7, 8])
