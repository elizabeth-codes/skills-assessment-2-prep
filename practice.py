"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example:

        >>> no_dupes = without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

        >>> isinstance(no_dupes, list)
        True

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    The function should return a variable of type list:
        >>> type(without_duplicates([111111, 2, 33333, 2]))
        <class 'list'>
    """

    return []


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a set of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should return a set:

        >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
        >>> isinstance(unique_common_items, set)
        True

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once:

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types:

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    return set()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    return []


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

    return []


#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    """ Print sorted list of pairs where the pairs are sorted."""
    # NOTE: This is used only for documentation tests. You can ignore it.

    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()

################
#Dictionaries
################

# Why are dictionaries necessary? Why not use a list?
#you can use a key value pair in dictionaries, and you can make sure that each key is unique using dictionaries unlike lists. lookup time is fast.

# How is the lookup time in a dictionary different from that of a list?
#lookup time in a dictionary is faster because you're looking for something specific rather than rifling through all the cards until you match the term and the query

# How do you create an empty dictionary? How do you create a dictionary with initial content?
# animals = {} for an empty dictionary
#     animals = {'goat': 6, 'pony': 1, 'duck': 14} for a populated dictionary

# How do you add a new key/value pair to a dictionary? How do you update the value of a key in a dictionary?
#using the example above:
#animals['rabbit'] = 2 for net new
#animals['pony'] = 2 for updating pony's value to 2.
#so they're basically the same; just for one the key is already in the dictionary and for the other, it is not.

# How do you remove a key/value pair from a dictionary?
# del animals['rabbit']

# How do you look up the value for a given key in a dictionary?
# animals['duck'] when animals in the dictionary name and duck is the key name. it will return 14 where 14 is the value.

# How do you iterate over a dictionary?
# if you want to get keys
# # for animal in animals:
# #     print(animal)
# if you want to get values
# for animal in animals:
#     print(animals[animal])

# Print keys?
#see above
# Print values?
#see above
# Print keys and values?
# animals.items()
# or
# for animal, number in animals.items():
#     print(f'{animal}: {number}')

# What is a KeyError? When does one occur?
# attemptin to index into a dictionary with a nonexistant key results in a keyerror

# Dictionary methods to know:

# .get()
#return the value for a key if the key is in the dictionary.
#if the key is not in the dictionary: returns default.
#if a default is not specified, it returns None so that a KeyError is not raised.
# #animals.get('porcupine',0)
# returns 0 because there were not porcupines in the dictionary

# .values()
#returns the values in a dictionary
#e.g. animals.values() could return dict_values([6,1,14]) if those are the values in the dictionary

# .items()
#as we discussed about 20 lines up from here, it will return the key value pairs in a dictionary.

# How do you access a dictionary within a dictionary?
# animals['pony']['bites'] if pony is the key in animals and bites is akey within pony.

# When should you use a dictionary?
#for key uniqueness, for ease of searching by term, for counting

################
# Python Tools
################

# What are some characteristics of Python as compared to other programming languages?
#it is strongly-typed, dynamic and high leve.
#strongly-typed: the value doesn't change. Dynamic: able to create new data and occupy more memory as the program runs rather than compiling
#high level: allows us to abstract and use English-like syntax.

# What are .pyc files? What is their purpose?
#some file that forms when python is compiled?? I don't really understand what their purpose is. just so that you don't have to compile again if its already compiled?

# What’s the difference between the commands python3 mygame.py and python3 -i mygame.py?
#python3 just runs it in the terminal as per usual and prints/returns any results as prescribed by the program after running it
#-i opens up interactive mode so it runs python and your code and returns you to th epython console, with all functions still defined and all variables still in memory

# Built-in Python functions to know:

# dir()
#show me the methods and attributes of this object.

# help()
#show me documentation about how to use this object.

# Why does code style matter?
#>Well styled code is easier to read, has fewer bugs and helps you do better on interviews.

# Key points of Python style to know
#They are listed below.

# Tabs vs. Spaces
#spaces are preferred, usually 4, don't mix n match.

# Line length and how to break lines for readability
#lines should be no more than 79 characters. you can always add line breaks in braces, brackets, parentheses

# Where to put whitespace
#around operators, divide paragraphs, put 2 blank lines between functions.

# Variable name style
#should use snake case, should be verby, should tell what something is for; use plural nouns for collections, singular nouns for everything else
#Use singular version of collections' names in for-loops (for fruit in fruits:)

# Docstrings and comments
#Docstrings: use """triple quotes""". shouldn't run more than one line; tell you when and why to use a function, written for users of the function
#Comments tell you how it works on the inside and are for maintainers of your function

# What is sys.argv? What happens if you print it out?
#I don't really understand tbh. something about command line arguments. you can pass them in and then user more files rather than just hard coding one.

################
# Markov Chains
################

# In the context of Markov chains, what is a bigram? What’s an n-gram?
#bigram - two word phrases (In this case, the keys to our dictionary. over line breaks as well as in a single line.)
#n-gram: sequence of n words; constructed from text and can be thought of as  links in a chain

# How could you use dictionaries to structure a bigram markov chain implementation?
#create a dictionary in which the key is bigrams from the actual text and the values are the words that come after each bigram.
#Choose a random bigram to start.
#choose a random key to continue. now look at the final bigram, treat that as a key and choose a value to extend the line. repeat.

################
# Shell
################

# VS Code shortcuts to know and use:

# CTRL-/ to comment/uncomment

# CTRL-] and CTRL-[ to indent/dedent (or tab and shift + tab)

# Shell shortcuts and commands to know and use:

# Tab completion

# Up arrow/Down arrow to navigate history

# CTRL-A to go to beginning of line

# CTRL-E to go to end of line

# CTRL-D to delete moving forward

# head <some file name>

# cat <some file name>

# tail <some file name>

# wc <some file name>

# sort <some file name>

# grep <term> <some file name>

# Using * to file name glob

# env

# echo $PATH

# which python

# export SOME_VARIABLE='some value'

# What is STDIN? How do you capture it using Python?

# What is STDOUT? How do you push to it using Python?

# What is STDERR?

# How do you redirect the output of one shell command to a file?

# How do you redirect the output of one shell command and append it to a file?

# How do you redirect the content of a file as input to an interactive Python script?

# How do you redirect the output of one shell command to the input of another?

# What is the shell environment?

# What is the $PATH environment variable? What role does it play on the command line?

# How can you access the shell environment in Python?

# How do you set environment variables using a .sh file?

################
# Python Projects
################

# What is a Python module?

# What is a namespace?

# What are the 3 ways to import something in Python?

# Why is from some_module import * not a good practice?

# When should you import a whole library versus only one function, class, etc.?

# What does if __name__ == "__main__" ask? When should you include this check at the bottom of your file?

# Where are the three places that you can import things from?

# What is pip?

# What is a virtual environment? How is that different than a virtual machine?

# Why are virtual environments necessary?

# How do you create a virtual environment? How do you activate it?

# What command can you use to view the currently installed Python libraries?

# What should you name the file that has the list of a Python project’s dependencies?

################
# Classes
################

# How are classes different than dictionaries in terms of structure, flexibility, and data storage?

# What is the relationship between a class and an instance?

# What is instantiation?

# What are attributes? How do you define an attribute at the class level (to be shared by all instances)? How do you set a new attribute on an instance? How can you update the value of an attribute on an instance?

# What is a method? How do you define a method on a class? How do you call a method?

# What are the key differences between functions and methods?

# What is initialization? How is it different than instantiation?

# What is __init__? When does it get called?

# What is encapsulation? What is abstraction? What is polymorphism?

# What is inheritance? When is it appropriate for one class to inherit attributes and/or methods from another?

# What are the various ways in which a child class can modify methods and attributes from a parent class?

# What is super()?

# What’s an example of violating polymorphism? What’s an example of enforcing polymorphism?

# When overriding parent methods, what is the only method that is normal to require different arguments than the parent method?

# What is an abstract class? What makes it different than a typical class?

# When there are methods that don’t directly map to an existing hierarchy, how can you continue to pursue encapsulation? (i.e. avoid copying the same method on several classes)
