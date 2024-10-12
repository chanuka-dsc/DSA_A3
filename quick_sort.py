from Data_Structures.DoublyLinkedList import DoublyLinkedList
from Data_Structures.Nodes.DLLNode import DLLNode

arr = [2, 5, 1, 3, 7, 6, 9, 8, 10, 4]

lst = DoublyLinkedList()
lst.append_array(arr)


def quick_sort(lst: DoublyLinkedList, start: int, end: int):
    if end > start:
        i = _partition(lst, start, end)
        quick_sort(lst, start, i - 1)
        quick_sort(lst, i + 1, end)


def _partition(lst: DoublyLinkedList, start: int, end: int):
    pivot = lst._get_node_by_i(end)
    i = start
    j = end - 1

    while i < j:
        while i < end and lst._get_node_by_i(i).val < pivot.val:
            i += 1
        while j > start and lst._get_node_by_i(j).val > pivot.val:
            j -= 1

        if i < j:
            i_node = lst._get_node_by_i(i)
            j_node = lst._get_node_by_i(j)
            i_node.val, j_node.val = j_node.val, i_node.val

    i_node = lst._get_node_by_i(i)
    if i_node.val > pivot.val:
        i_node.val, pivot.val = pivot.val, i_node.val

    return i


quick_sort(lst, 1, 10)
lst.print_lst()
