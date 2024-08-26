class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class SinglyLL:

    def __init__(self):
        self.length = 0
        self.head = None

    # insert from first
    def insert_from_head(self, value):
        # create a new node
        # assign the new_node.next = self.head

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert_from_trail(self, value):
        # create a new node
        # traverse and point head to the last node
        # head.next - new_node

        new_node = Node(value)
        if self.length == 0:
            # No nodes present
            self.head = new_node
            self.length += 1
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next

            curr.next = new_node
            self.length += 1

    def delete_from_head(self):
        if self.length == 0:
            print("Nothing to delete")
        else:
            new_first_node = self.head.next
            if not new_first_node:
                self.length += 1
                self.head = None
                print("Deleted the only Node.")
            else:
                self.head = None
                self.head = new_first_node
            self.length += 1

    def delete_from_tail(self):
        if self.length == 0:
            print("Nothing to delete")
        else:
            new_first_node = self.head.next
            if not new_first_node:
                self.length += 1
                self.head = None
                print("Deleted the only Node.")
            else:
                curr = self.head
                while curr.next.next != None:
                    curr = curr.next
                curr.next = None
            self.length -= 1

    def insert_from_middle(self, value, index):
        curr = self.head
        cnt = 1
        while curr != None:
            cnt += 1
            if cnt == index:
                new_node = Node(value)
                next_node = curr.next
                curr.next = new_node
                new_node.next = next_node
            else:
                curr = curr.next

    def insert_from_middle(self, value, index):
        curr = self.head
        cnt = 1
        while curr != None:
            cnt += 1
            if cnt == index:
                new_node = Node(value)
                next_node = curr.next
                curr.next = new_node
                new_node.next = next_node
            else:
                curr = curr.next

    def delete_from_middle(self, value, index):
        curr = self.head
        cnt = 1
        while curr != None:
            cnt += 1
            if cnt == index:
                new_node = Node(value)
                next_node = curr.next
                curr.next = new_node
                new_node.next = next_node
            else:
                curr = curr.next

    def __str__(self):
        # data1, add_data2, data2, add_data3, data3, None
        # head.data, head.next
        curr = self.head
        res, cnt = '',  0
        while curr != None:
            cnt += 1
            res += curr.data + "->"
            curr = curr.next
        print(f'length of the SLL {cnt}')
        return res

sll = SinglyLL()
sll.insert_from_trail('data-1')
sll.insert_from_trail('data-2')
sll.insert_from_trail('data-3')
sll.insert_from_trail('data-4')
# sll.insert_from_trail('data-5')
# sll.delete_from_tail()
sll.insert_from_middle('middle-data', 3)

# sll.delete_from_head()

print(sll)