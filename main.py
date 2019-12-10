from src.definition import nodeLinkedList, get_description, reverse_link_list


def main():
    v1 = nodeLinkedList('a')
    v2 = nodeLinkedList('b', v1)
    v3 = nodeLinkedList('c', v2)
    print(f'Print linked list before reverse : {get_description(v3)}')
    print(f'Print linked list after reverse : {get_description(reverse_link_list(v3))}')



if __name__ =='__main__':
    main()
