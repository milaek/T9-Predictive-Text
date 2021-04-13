# T9 Predictive Text 
 A program that reads the text content of a file as words, creates a dictionary mapping the words to their frequency, 
 creates a Trie of said words, and then uses both of the above to predict from user input numbers 
 what words they may be trying to access. The prediction provides the most common words via frequency in descending order, including words that would use the user input numbers as a prefix within the word.
 This project was written as part of Udacity's Intermediate Python Nanodegree.

 # How to Use
 This program runs in the command line using python. In command line enter the project folder directory. Then using your OS appropriate command, run t9.py using python. The program will prompt the user for input.

# Attribution
The data set originally comes from [Google's NGram project](https://storage.googleapis.com/books/ngrams/books/datasetsv3.html), 
released under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). 
Specifically, we're using the 1-grams of version 20090715.

The helper code contained in helper.py comes from Udacity's Intermediate Python Nanodegree course.
This project was completed as part of taking the paid course in April 2021.
The course cannot be accessed without a udacity account, but the homepage, syllabus, and further
information about the nanodegree can be found [here](https://www.udacity.com/course/intermediate-python-nanodegree--nd303?gclid=Cj0KCQjw38-DBhDpARIsADJ3kjnOHPk_P7SwE4D5VyVTVmOutAsa16iuYPZ8tFBf0ZzdT3UECemswV0aAkKWEALw_wcB&utm_campaign=12712700850_c&utm_keyword=%2Budacity%20%2Bpython_b&utm_medium=ads_r&utm_source=gsem_brand&utm_term=124530982990)
