DNA = "AAAAACCCCCAAAAACCCCCCCCCAAAAAGGGTTT"


def find_sequences(match_length=10):
    '''
    >>> DNA # sample doctest 1
    'AAAAACCCCCAAAAACCCCCCCCCAAAAAGGGTTT'
    >>> len(DNA)    # sample doctest 2
    35
    >>> result = find_sequences(match_length=10) # actual doctest 1
    >>> len(result)
    2
    >>> result
    ['AAAAACCCCC', 'CCCCCAAAAA']
    '''

    result = []
    if len(DNA) <= match_length:
        return result
    slices = {}
    for i in range(0, len(DNA)-match_length+1):
        temp = DNA[i:i+match_length]
        if temp in list(slices.keys()):
            slices[temp] += 1
        else:
            slices[temp] = 1
    result = [x for x in slices if slices[x] > 1]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
