from Data_Structures.LinkedList import LinkedList

arr = [2, 45, -2, 0, 3, 13, 20, 99]


ll = LinkedList()
ll.append_array(arr)


def selection_sort(ll: LinkedList):
    tmp = ll.lst
    while tmp is not None:
        current_min = tmp  # current minimum
        comp = tmp.nxt  # What we are going to compare with
        while comp is not None:
            if current_min.val > comp.val:  # Check if minimum condition holds
                current_min = comp  # set reference to new minimum
            comp = comp.nxt

        if tmp.val > current_min.val:  # Check if minimum condition holds for lst
            # here we can just exchange values instead of whole nodes as there is nothing unique to a node which  relates to  its value
            old_min = tmp.val
            tmp.val = current_min.val
            current_min.val = old_min

        tmp = tmp.nxt


selection_sort(ll)
print(ll.lst)
