def compact(lst):
    lst = lst
    for x in lst:
         if x is True:
            print(x)
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """