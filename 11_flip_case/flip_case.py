def flip_case(phrase, to_swap): 
    x = to_swap.swapcase()
    for x in phrase:
        return phrase
# I would need to loop through the string and swapcase()the char that == to_swap. return the phrase.

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
