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
    text_to_convert.close()
    
    
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
    # take input text, look through text, 
    # separate text into tuples
    # tuples will be our key for dictionary
    # each key will need values (the words that follow previous word)
    # repeat until the end of the text
    # return the dictionary

    # loop through words to make tuple list
    # check before adding if the new tuple key already exists
    #    if key not in key_tuples
    # if it is not there, chains = {key_tuple:words[n+2]}
    # if it is there, add your third word to the value for the key_tuples
        # chains[key_tuples] = (words[n+2])
    # when you've reached the end of the index, 
    # you need to add the final word to the value
        # words[-1]
    # print(words[0])

    chains = {}

    n = 0   # n is the counter
    key_tuples = ()
    key_list = []
    chains[key_tuples] = []
    value_list = []

    words = text_string.split()
    # To set a stop point, append None to the end of our word list.
    words.append(None)

    for key in words: 
        if n != (len(words) - 2):
            key_tuples = (words[n], words[n + 1])
            value = words[n + 2]
        
        # if key_tuples not in key_list:
        #     key_list.append(key_tuples)
        
        # to create dictionary, check if tuple exists
        # if tuple exists, add to value list with the word immed following
        # if tuple doesn't exist, 
        # add tuple to key list and create new value list
            
            if key_tuples not in chains:
                chains[key_tuples] = []
                # chains[key_tuples] = [value]
                # chains[key] = value
                # dict_name[watermelon] = dict_name.get(1, i)
                # chains[key_tuples] = chains.get(key_tuples, value_list.append(value))
                #chains[key_tuples] = chains[key_tuples].append(words[n+2])
            chains[key_tuples].append(value)
            n += 1
            # if key_tuples in chains:
            #     current_value = chains[key_tuples]
            #     current_value.append(value) 
            #     chains[key_tuples] = [value]
        
        # if n == (len(words) - 2):
        #     chains[key_tuples] = chains[key_tuples].append(words[-1])
        #     chains = {key_tuples:chains[key_tuples]}
        #     break
            
        #x += 1
    #return key_list
    # print(key_list)
    # print((words[41]))
    
    # x = 0   # tuple counter
    #for key2 in key_list:

        # if x == (len(words) - 3):
        #     break
        # # x += 1

    return chains
    # print(chains)

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
