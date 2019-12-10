from src.definition import nodeLinkedList
from src.definition import get_description, add_to_list, reverse_link_list
def test_linklist_node():
    v1 = nodeLinkedList('Sonal')
    assert  1==1


def test_linkedList_node_with_next_node():
    v1 = nodeLinkedList('Sonal')
    v2 = nodeLinkedList('Nayak', v1)
    print(v2.print_node())
    assert 1==1


def test_get_description_with2():
    v1 = nodeLinkedList('Sonal')
    v2 = nodeLinkedList('Nayak', v1)
    description = get_description(v2)
    assert 'Nayak Sonal null' == description


def test_get_description_with3():
    v1 = nodeLinkedList('3')
    v2 = nodeLinkedList('2', v1)
    v3 = nodeLinkedList('1', v2)
    description = get_description(v3)
    assert '1 2 3 null' ==  description


def test_add_and_get_description_with2():
    v1 = nodeLinkedList('World')
    v2 = nodeLinkedList('Hello', v1)
    add_to_list(v2, '!')
    description = get_description(v2)
    # print(description)
    assert 'Hello World ! null' == description


def test_reverse_order():
    v1 = nodeLinkedList('red')
    v2 = nodeLinkedList('are', v1)
    v3 = nodeLinkedList('roses', v2)
    earlier_description = get_description(v3)
    # print(earlier_description)
    reversed_description = get_description(reverse_link_list(v3))
    # print(reversed_description)
    assert earlier_description == 'roses are red null'
    assert reversed_description == 'red are roses null'
