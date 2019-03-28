def deleteNode(head, position):
    new_list = SinglyLinkedList()
    if position == 0:
        head = head.next
        new_list.head = head
        return new_list

    currentnode = head
    index = 0
    while index < position - 1:
        currentnode = currentnode.next
        index += 1
    node_delete = currentnode.next
    currentnode.next = node_delete.next
    new_list.head = head
    return new_list


class SinglyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, value):
        newNode = SinglyLinkedListNode(value)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def print_list(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
        print('First list')

        llist1.print_list()

        position = int(input())

        llist1 = deleteNode(llist1.head, position)
        llist1.print_list()
