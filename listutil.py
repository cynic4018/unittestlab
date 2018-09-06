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

    # newlist=[]
    # for c in list:
    #     if c not in newlist:
    #         newlist.append(c)
    #
    # return len(newlist)