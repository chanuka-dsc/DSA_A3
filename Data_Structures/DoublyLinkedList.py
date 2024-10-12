from Data_Structures.Nodes.DLLNode import DLLNode


class DoublyLinkedList:

    def __init__(self) -> None:
        self.lst = None
        self.cnt = 0

    # Add a value: x to the end of the list
    def append(self, x: int) -> None:
        # if list is empty
        if self.lst is None:
            self.lst = DLLNode(x)
            self.cnt += 1

        else:
            tmp = self.lst
            # loop until the tail
            while tmp.nxt:
                tmp = tmp.nxt
            # add new node
            n_node = DLLNode(x)
            n_node.prv = tmp
            tmp.nxt = n_node

            self.cnt += 1

    def append_array(self, arr):
        for element in arr:
            self.append(element)

    # Check if the list is empty
    def empty(self) -> bool:
        return self.lst is None

    # Returns the length of the list
    def __len__(self):
        return self.cnt

    # Method print each elements of the list with it's links
    def print_lst(self):
        tmp = self.lst
        while tmp:
            print(
                str(tmp.prv.val if tmp.prv is not None else None)
                + " <- prev "
                + str(tmp.val)
                + " nxt-> "
                + str(tmp.nxt.val if tmp.nxt is not None else None)
            )
            tmp = tmp.nxt

    # Insert a value: x to an index: p in the list
    def add_value(self, x: int, p: int) -> None:

        # Insert value to head when list is empty
        if self.empty():
            self.lst = DLLNode(x)
            self.cnt += 1
            return

        # Insert value to head when list is not empty
        if p == 1:
            n_node = DLLNode(x)
            n_node.nxt = self.lst
            self.lst.prv = n_node
            self.lst = n_node
            self.cnt += 1
            return

        # This search takes O(n)
        node = (
            self._get_node_by_i(p) if p != self.cnt + 1 else self._get_node_by_i(p - 1)
        )  # if we are adding to the tail the we need to get the current tail which is (p - 1)

        # Guard clause for invalid indexes
        if node is None:
            return

        # Initialize new node
        n_node = DLLNode(x)

        # The actual insertion takes O(1)
        # If element is added to the tail
        if node.nxt is None:
            node.nxt = n_node
            n_node.prv = node
            self.cnt += 1

        # If element is added to the middle
        else:
            node.prv.nxt = n_node
            n_node.prv = node.prv
            n_node.nxt = node
            node.prv = n_node
            self.cnt += 1

    # Remove an element at index: p in the list
    def remove(self, p: int) -> None:
        # can't remove from an empty list
        if self.empty():
            return

        # Remove Head
        if p == 1:
            self.lst = self.lst.nxt
            self.lst.prv = None
            self.cnt -= 1
            return

        # This search takes O(n)
        node = self._get_node_by_i(p)

        # Guard clause for invalid indexes
        if node is None:
            return

        # The actual removal takes O(1)
        # If tail is removed
        if node.nxt is None:
            node.prv.nxt = None
            node.prv = None
            self.cnt -= 1
        # If element from middle is removed
        else:
            node.prv.nxt = node.nxt
            node.nxt.prv = node.prv
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

    # Return the node at index p in the list
    def _return(self, p: int) -> DLLNode:
        # Invalid index to retrieve from list
        if p <= 0 or p > self.cnt:
            return

        tmp = self.lst
        for _ in range(p - 1):
            tmp = tmp.nxt

        return tmp

    # Reverses a the list
    def reverse(self) -> None:

        # No point in reversing an empty or one itemed list
        if self.cnt < 2:
            return

        tmp = self.lst
        # loop to reverse the links
        while tmp:
            nxt = tmp.nxt
            tmp.nxt = tmp.prv
            tmp.prv = nxt

            # if the list is at its end
            if nxt is None:
                self.lst = tmp
                return

            tmp = tmp.prv

    # Rotate a list by r: indexes forward where list item i becomes (i+r) mod n (n  = number of list items)
    def rotate(self, r: int) -> None:
        # r must be at least 1 to rotate, and if r = n no ration takes place
        if r < 1 or r == self.cnt:
            return

        # In case r lager than n
        if r > self.cnt:
            r = r % self.cnt

        tmp = self.lst

        # Find the new Head
        for _ in range(r):
            tmp = tmp.nxt

        # Splice the list at new head
        tmp.prv.nxt = None
        tmp.prv = None

        # Keeping a reference to the new head
        n_head = tmp

        # Rind the end
        while tmp.nxt:
            tmp = tmp.nxt

        # Re-join the two splices
        tmp.nxt = self.lst
        self.lst.prv = tmp

        # Set new head
        self.lst = n_head

    # Will delete the first instance of a value: x in the list
    def delete(self, x: int) -> None:
        # empty list edge case
        if self.empty():
            return

        tmp = self.lst
        # case where head is changed
        if tmp.val == x:
            self.lst = tmp.nxt
            self.lst.prv = None
            self.cnt -= 1
            return

        # No need to keep track of the previous node to break the link as the node already has it
        found = False

        # traverse the list to find the element
        while not found:
            if tmp.val == x:
                found = True
                break

            tmp = tmp.nxt

            # case where the list has reach it's end and the element was not found
            if tmp is None:
                break

            # break the link and join the next element
        if found:
            tmp.prv.nxt = tmp.nxt
            # if it is not the tail we can update the next elements previous
            if tmp.nxt is not None:
                tmp.nxt.prv = tmp.prv
            self.cnt -= 1

    # Returns a reference to the node at index:p
    def _get_node_by_i(self, p: int) -> DLLNode:
        # Invalid index for list
        if p <= 0 or p > self.cnt:
            return

        tmp = self.lst
        for _ in range(p - 1):
            tmp = tmp.nxt

        return tmp
