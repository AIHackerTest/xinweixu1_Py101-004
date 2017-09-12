#Ex 41 - Learning to speak Object-Oriented

#class - tell python to make a new type of thing;
#object - two meanings, the most basic type of thing,
#         and any instance of some thing;
#instance - what you get when you tell python to create a class
#def - how you define a function inside a class
#self - inside the function in a class, self is a variable
#       for the instance/object being processed
#inheritance - the concept that one class can inherit traits
#              from another class
#composition - the concept that a class can be composed of other
#              classes as parts, much like how a car has wheels
#attribute - a property classes have that are from composition
#            and are usually variables
#is-a - a phrase to say that sth inherits from another
#       like "salmon" is-a "fish"
#has-a - a phrase to say that sth is composed of other things
#       like a "salmon" has-a "mouth"

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
       "class %%%(%%%):":
           "Make a class named %%% that is-a %%%.",
       "class %%%(object): \n\tdef __init__(self, ***)":
           "class %%% has-a __init__ that takes self and *** parameters.",
       "class %%%(object):\n\tdef ***(self, @@@)":
           "class %%% has-a fucntion *** that takes self and @@@ parameters.",
               "*** = %%%()":
          "Set *** to an instance of class %%%.",
               "***.*** (@@@)":
           "From *** get the *** function, call it with params self, @@@.",
               "***.*** = '***'":
           "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website:
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    #strip each element of word and turn in into a string

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
             random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # this is how you duplicate a list or string
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print (question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print ("\nBye")
