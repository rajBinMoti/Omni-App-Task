DNA = "AAAAACCCCCAAAAACCCCCCCCCAAAAAGGGTTT"


def find_sequences():
    '''
    >>> DNA # sample doctest 1
    'AAAAACCCCCAAAAACCCCCCCCCAAAAAGGGTTT'
    >>> len(DNA)    # sample doctest 2
    35
    >>> result = find_sequences(DNA) # actual doctest 1
    >>> len(result)
    2
    >>> result
    ["AAAAACCCCC","CCCCCAAAAA"]
    '''
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
