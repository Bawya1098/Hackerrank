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


def compare_lists(llist1, llist2):
    while llist1 is not None and llist2 is not None and llist1.data == llist2.data:
        llist1 = llist1.next
        llist2 = llist2.next
    if llist1 is None and llist2 is None:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        print('First list')

        llist1.print_list()

        print('Second list')

        llist2.print_list()

        result = compare_lists(llist1.head, llist2.head)

        print('Result')
        print(result)

        # fptr.write(str(int(result)) + '\n')

    # fptr.close()
