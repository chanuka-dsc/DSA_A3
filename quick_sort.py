from Data_Structures.DoublyLinkedList import DoublyLinkedList

arr = [2, 5, 1, 3, 7, 6, 9, 8, 10, 4]

lst = DoublyLinkedList()
lst.append_array(arr)


# quick sort algorithm that sorted the elements in an ascending order
def quick_sort(lst: DoublyLinkedList, start: int, end: int):
    if end > start:
        i = _partition(lst, start, end)
        quick_sort(lst, start, i - 1)
        quick_sort(lst, i + 1, end)


# broke the logic down separately to make it easier to debug
def _partition(lst: DoublyLinkedList, start: int, end: int):
    pivot = lst._get_node_by_i(end)
    i = start
    j = end - 1  # because the end is the pivot

    while i < j:
        while i <= j and lst._get_node_by_i(i).val < pivot.val:
            i += 1
        while i <= j and lst._get_node_by_i(j).val > pivot.val:
            j -= 1

        if i <= j:
            i_node = lst._get_node_by_i(i)
            j_node = lst._get_node_by_i(j)
            i_node.val, j_node.val = j_node.val, i_node.val

    i_node = lst._get_node_by_i(i)
    if i_node.val > pivot.val:
        i_node.val, pivot.val = pivot.val, i_node.val

    return i


print("\n\n Test 1 : random list\n\n")

quick_sort(lst, 1, 10)
lst.print_lst()

print("\n\n Test 2 : list in descending order\n\n")
arr_2 = [6, 5, 4, 3, 2, 1, 0]
lst_2 = DoublyLinkedList()
lst_2.append_array(arr_2)

quick_sort(lst_2, 1, 7)
lst_2.print_lst()

print("\n\n Test 3 : All non positive and with two instance of the same value\n\n")
arr_3 = [-2, -99, -15, 0, -12, -12, -1]
lst_3 = DoublyLinkedList()
lst_3.append_array(arr_3)

quick_sort(lst_3, 1, 7)
lst_3.print_lst()

"""
    Here I tried to follow the algorithm given in the slides but, I was not able to get some cases to work properly.
    Afterwards I found this in the python book page 559 which had a different approach and
    here the difference was instead of switching for each instance between the two sides it finds two larger and smaller values
    the switch the two. Then when the two pointers pass each other we know that we have gone through all the elements. 
    Then we just have to move the pivot to the correct position. 
"""
