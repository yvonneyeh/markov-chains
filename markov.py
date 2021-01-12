"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open the file and assign that a name
    # Read the file as an entire string
    # split out the white space

    text_to_convert = open(file_path)
    text_string = text_to_convert.read()
    
    
    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # take input text, look through text, 
    # separate text into tuples
    # tuples will be our key for dictionary
    # each key will need values (the words that follow previous word)
    # repeat until the end of the text
    # return the dictionary
     

    split_text = text_string.split()
    # print(split_text)
    # print(type(split_text))
    n = 0   # n is our counter
    x = 2
    key_tuples = ()
    key_list = []
    for key in split_text:
        key_tuples = (split_text[n], split_text[n+1])
        # print(key)
        # print(len(split_text))
        
        # print(key_list)
        key_list.append(key_tuples)
        
        # to create dictionary, check if tuple exists
        # if tuple exists, add to value list with the word immed following
        # if tuple doesn't exist, 
            # add tuple to key list and create new value list
        
        if n == (len(split_text) - 3):
            continue
            chains.get(key_tuples, split_text[n+2])  
        print(chains)   
    
        if n == (len(split_text) - 2):
            break
        n += 1
        x += 1
    #return key_list
    print(key_list)
    # print((split_text[41]))
    
    x = 0   # tuple counter
    #for key2 in key_list:
    #    chains[key2] = chains.get(key_tuples, split_text[x+2])
        # print(chains)

        # if x == (len(split_text) - 3):
        #     break
        # # x += 1

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
