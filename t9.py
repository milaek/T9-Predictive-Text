"""
Main Codeblock 
"""

# Imports
import helper

# Global Constants
DATA_FILE = 'ngrams-nk.txt'


# Functions
def parse_content(content):
    """
    Parses content from a string into a dict for use by other functions

    PARAMETERS
    ----
    content : str
        single string of word/frequency pairs seperated by \n between pairs and ' ' between word and freq

    RETURNS
    ----
    Dictionary
        Dict with word/frequency pairs.
    """

    data_dict = dict()

    for pair in content.split('\n'):
        # split one more time so that word and freq are seperate items
        pair = pair.split()
        data_dict[pair[0]] = pair[1]

    return data_dict

def make_tree(data_dict):
    tree = dict()

    for word in data_dict.keys:
        current_node = tree
        for char in word:
            if char == "a" or char == "b" or char == "c":
                num = 2
            elif char == "d" or char == "e" or char == "f":
                num = 3
            elif char == "g" or char == "h" or char == "i":
                num = 4
            elif char == "j" or char == "k" or char == "l":
                num = 5
            elif char == "m" or char == "n" or char == "o":
                num = 6
            elif char == "p" or char == "q" or char == "r" or char == "s":
                num = 7
            elif char == "t" or char == "u" or char == "v":
                num = 8
            else:
                num = 9
            
            if char not in current_node:
                current_node[char] = dict()
            current_node = current_node[char]
        current_node[word] =  data_dict[word]


    return tree

def predict(tree, numbers):
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename=DATA_FILE)

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
