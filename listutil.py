def count_unique(list):
    """Count the number of distinct elements in a list.

   The list can contain any kind of elements, including duplicates and nulls in any order.

   (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

   :param list:  list of elements to find distinct elements of
   :return: the number of distinct elements in list

   Examples:
   >>> count_unique(['a','b','b','b','a','c','c'])
   3
   >>> count_unique(['a','a','a','a'])
   1
   >>> count_unique([ ])
   0
   """
    if list == None:
        return None
    if len(list) == 0:
        return 0
    compare = list[0]
    count = 1
    list.sort()
    for i in list:
        if 0 != i and compare != i:
            count += 1
            compare = i

    return count

def binary_search(list, element):
    """Search the element in list that already sorted by using binary search.

       :param list:  list of elements to find elements of
              element: element in list that want to find
       :return: the index  of elements that want to find from list,
                if not, return 'Not found'

       Examples:
       >>> binary_search([1, 2, 3, 4, 5, 6, 7], 1)
       0
       >>> binary_search([1, 2, 3, 4, 5, 6], 6)
       5
       >>> binary_search([1, 2, 3, 4, 5, 6], 7)
       'Not found'
       >>> binary_search([], 4)
       'List is empty'
       """

    if element == None:
        raise TypeError('Search element must not be none')
    if len(list) == 0:
        return 'List is empty'

    list.sort()
    leftside = 0
    rightside = len(list)-1
    while leftside <= rightside:
        middle = int(((leftside+rightside)/2))
        if list[middle] == element:
            return middle
        elif element < list[middle]:
            rightside = middle-1
        else:
            leftside = middle+1

    return 'Not found'

