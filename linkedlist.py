# Linear Data strucute, replacement for Array
# coll of nodes
# data & address
# Linked list, address will not be in continous form, or its not a contiguous memory
# first node Head will always point to null
# in list the write operation will have O(n) time complexity, but in LL the time complexity is O(1) which is constant time
# List allocates double memory, so most of the memory remains unutilised

# Diff array & LL is seating in theatre

# data1, add_data2 ---> data2, add_data3 ---> data3, null


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# data1 = Node('data1')
# data2 = Node('data2')
# data3 = Node('data3')

# data1.next = data2  # assign the ADDRESS OF SECOND NODE TO node 1's next variable
# data2.next = data3  # assign the address of third node to next varibale of node 2

# print(data1)
# print(data2)
# print(data3)


class LinkedList():

    # first it will be Empty linked list
    # no of nodes 0
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def insert_head(self, value):
        new_node = Node(value)  # create new Node
        new_node.next = self.head   # assign the address of the head to next varibale of node
        self.head = new_node    # assign the new node to head making new node as head node
        self.length += 1    # increment the node count

    def insert_tail(self, value):
        # create a new node
        # point self.head to the last node of the LL
        # assign address of new Node to the next variable of self.head
        # assign the head to the new node
        # increment the node count
        curr = self.head
        while curr.next != None:    # if i have to stop at last node, if i have to point to last but one, then its curr.next.next
            curr = curr.next

        new_node = Node(value)
        new_node.next = None
        curr.next = new_node
        self.length += 1    # increment the node count

    def __str__(self):
        # head will be pointing to first node in LL
        curr = self.head
        res = ''
        while curr != None:     # if i have to stop at very last, this will point to address that last node it pointing to
            res = str(res) + "->" + curr.data
            curr = curr.next
        return res

    def insert_middle(self, value, insert_value):
        # find the head, next to which the element has to be inserted
        # find the head + 1 element, previous to which the element has to be inserted
        # define new_node
        # head.next = new_node
        # new_node.next = previous_node
        new_node = Node(value)

        curr = self.head
        cnt = 1
        while curr.next != None:
            cnt += 1
            if cnt == insert_value:
                next_node = curr.next
                curr.next = new_node
                new_node.next = next_node
            else:
                curr = curr.next

ll = LinkedList()

ll.insert_head('data4')
ll.insert_head('data3')
ll.insert_head('data2')
ll.insert_head('data1')
ll.insert_tail('data5')
ll.insert_tail('data6')


insert_index = 3
insert_value = 'data_middle'
ll.insert_middle(insert_value, insert_index)

print(ll)