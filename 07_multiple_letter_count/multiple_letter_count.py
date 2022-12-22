def multiple_letter_count(phrase):
    dict = {}
    for i in phrase:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        return dict
     
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """