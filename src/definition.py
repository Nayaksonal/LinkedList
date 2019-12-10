
class nodeLinkedList:

    def __init__(self, value, nextnode=None):
        self.data = value
        self.next_node: nodeLinkedList = nextnode if nextnode is not None else  None
        # print(f'data : {self.data}')

    def print_node(self):
       print(f'data with me {self.data}')


def get_description(node: nodeLinkedList):
    if node.next_node is not None:
        return f'{node.data} {get_description(node.next_node)}'
    else:
        return f'{node.data} null'


def add_to_list(node: nodeLinkedList, value: str):

    if node.next_node is None:
       new_node = nodeLinkedList(value)
       node.next_node = new_node
    else:
        return add_to_list(node.next_node, value)


def reverse_link_list(node):
    cur_node = node
    while cur_node is not None:
        old_next_node = cur_node.next_node
        if cur_node == node:
           cur_node.next_node = None
        else:
            cur_node.next_node = old_curr

        old_curr = cur_node
        cur_node = old_next_node
    return old_curr
