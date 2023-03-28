phrase = "The rain in spain stays mainly in the plain."


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    non_duplicated_letters = {}
    for letter in phrase:
        if letter == ' ':
            continue
        if letter not in non_duplicated_letters:
            non_duplicated_letters[letter] = 1
        else:
            non_duplicated_letters[letter] += 1

    largest_value = 0
    for value in non_duplicated_letters.values():
        if value > largest_value:
            largest_value = value
    print(largest_value)

    most_frequent_letters = []
    for key, value1 in non_duplicated_letters.items():
        if value1 == largest_value:
            most_frequent_letters.append(key)
    return sorted(most_frequent_letters)

    # return non_duplicated_letters


print(top_chars(phrase))