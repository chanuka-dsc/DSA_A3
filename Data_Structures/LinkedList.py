from Data_Structures.Nodes.LLNode import LLNode


class LinkedList:

    def __init__(self) -> None:
        self.lst = None
        self.cnt = 0

    # Add a value: x to the end of the list
    def append(self, x: int) -> None:
        # if list is empty
        if self.lst is None:
            self.lst = LLNode(x)
            # if list has elements
        else:
            tmp = self.lst
            while tmp.nxt is not None:
                tmp = tmp.nxt
            tmp.nxt = LLNode(x)
        self.cnt += 1

    # Add a value:- x to a specific index:- p within the list
    def add_value(self, x: int, p: int) -> None:
        # Invalid index to add to list
        if p <= 0 or (p - 1) > self.cnt:
            return

        # When list is empty --> L=<>, p=1 :<X>
        if self.lst is None and p == 1:
            self.lst = LLNode(x)
            self.cnt += 1
            return

        # When head is changed
        if p == 1:
            n_node = LLNode(x)
            n_node.nxt = self.lst
            self.lst = n_node
            self.cnt += 1
            return

        # When list is not empty
        tmp = self.lst
        for _ in range(p - 2):
            tmp = tmp.nxt

        # Add the new element
        n_node = LLNode(x)
        n_node.nxt = tmp.nxt
        tmp.nxt = n_node

        # Increment count
        self.cnt += 1

    def append_array(self, arr):
        for element in arr:
            self.append(element)

    # Remove a node at a given index
    def remove(self, p: int) -> None:
        # Invalid index to remove from list
        if p <= 0 or p > self.cnt:
            return

        # If head is removed
        if p == 1:
            self.lst = self.lst.nxt
            self.cnt -= 1
            return

        tmp = self.lst
        for _ in range(p - 2):
            tmp = tmp.nxt

        tmp.nxt = tmp.nxt.nxt
        self.cnt -= 1

    # Find a value:- x and return its index:- p if exists, else -1
    def search(self, x: int) -> int:
        tmp = self.lst
        i = 1

        # traverse the list to find the element
        while tmp:
            if tmp.val == x:
                return i
            tmp = tmp.nxt
            i += 1

        return -1

    # Return the value of index p in the list
    def _return(self, p: int) -> LLNode:
        # Invalid index to retrieve from list
        if p <= 0 or p > self.cnt:
            return

        tmp = self.lst
        for _ in range(p - 1):
            tmp = tmp.nxt

        return tmp

    # Check if the list is empty
    def empty(self) -> bool:
        return self.lst is None

    # Get the current length of the list
    def __len__(self) -> int:
        return self.cnt

    # Will delete the first instance of a value: x in the list
    def delete(self, x: int) -> None:
        # empty list edge case
        if self.empty():
            return

        tmp = self.lst
        # case where head is changed
        if tmp.val == x:
            self.lst = tmp.nxt
            self.cnt -= 1
            return

            # need to keep track of the previous node to break the link
        prev = None
        found = False

        # traverse the list to find the element
        while not found:
            if tmp.val == x:
                found = True
                break
            prev = tmp
            tmp = tmp.nxt

            # case where the list has reach it's end and the element was not found
            if tmp is None:
                break

        if found:
            prev.nxt = tmp.nxt
            self.cnt -= 1
