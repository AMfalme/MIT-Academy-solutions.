# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def swap(sequence, i, j):
    sequence_list = list(sequence)
    sequence_list[i], sequence_list[j] = sequence_list[j], sequence_list[i]
    return ''.join(sequence_list)


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    sequence_len = len(sequence)
    if sequence_len == 1:
        return [sequence]
    permutations = []
    for pos, element in enumerate(sequence):

        remaining = sequence.replace(element, '')
        seq = get_permutations(remaining)
        for i, elements in enumerate(seq):
            permutation = elements + element
            permutations.append(permutation)
    return permutations


if __name__ == '__main__':
    # print(get_permutations('abc'))

    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    # delete this line and replace with your code here
