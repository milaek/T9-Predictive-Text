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
        String of word/frequency pairs seperated by \n between pairs and ' ' between word and freq

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
    """
    Makes a trie using the t9 numerical values of the characters in the dict of words passed in

    PARAMETERS:
    ----
    data_dict : dictionary
        Dictionary of words and their associated frequency values

    RETURNS:
    ----
    Dictionary
        Nested dictionary taking the form of a Trie, using t9 numerical values instead of alphabetic characters

    """

    tree = dict()

    for word in data_dict.keys():
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
            
            if num not in current_node:
                current_node[num] = dict()
            current_node = current_node[num]
        current_node[word] = data_dict[word]

    return tree


def predict(tree, numbers):
    """
    Gives a list of predictions as to the desired text in order of frequency based on the t9 input. Will assume that the given number could be a prefix.

    PARAMETERS:
    ----
    tree : dictionary
        Nested dictionary taking the form of a trie using t9 numbers 

    numbers : str
        String of digits that represent a t9 input

    RETURNS:
    ----
    List:
        A sorted list of tuples containing the predicted words and their associated frequencies

    """
    current_node = tree
    for num in numbers:
        if int(num) in current_node:
            current_node = current_node[int(num)]
            print(num)
        else:
            return None
    output = predict_recursive(current_node)
    sorted_output = sorted(output, key=lambda item: item[1])
    return sorted_output

def predict_recursive(current_node):
    """
    Helper function to recurse though lower branches of the trie and find more potential words

    PARAMETERS:
    ----
    current_node : dictionary
        A dictionary to search for words or further nested dictionaries

    RETURNS:
    ----
    List
        A list of tuples containing potential words and their associated frequencies.  
    """
    output = list()
    for key in current_node.keys():
        if isinstance(key, str):
            output.append((key, current_node[key]))
        else:
            predicted_longer = predict_recursive(current_node[key])
            for item in predicted_longer:
                output.append(item)
    return output


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
