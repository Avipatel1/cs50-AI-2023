import nltk
# nltk.download('punkt_tab') # Uncomment this line to download the punkt tokenizer if not already downloaded
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S | VP NP | NN | PP

NP -> N
NP -> NN
NP -> N N N
NP -> Det N
NP -> Det NN
NP -> Det NN PP
NP -> Adj N
NP -> Det Adj N
NP -> Det Adj Adj N
NP -> Det Adj Adj Adj N
NP -> N PP
NP -> Det N PP
NP -> Det N PP PP
NP -> Det Adj N PP
NP -> Det Adj Adj N PP
NP -> Det Adj Adj Adj N PP
NP -> Det N Conj Det N
NP -> N Conj N
NP -> Det N Conj N
NP -> N Conj Det N
NP -> NP P NP
NP -> NP Adv


NN -> N N

VP -> V
VP -> V NP
VP -> V NP NP
VP -> V PP
VP -> V NP PP
VP -> V Adv
VP -> V V
VP -> V NP Adv
VP -> V P NP
VP -> V P Det
VP -> V Conj V

PP -> P NP

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    words = nltk.word_tokenize(sentence)
    processed = []
    for word in words:
        word_lower = word.lower()
        if any(char.isalpha() for char in word_lower):
            processed.append(word_lower)
    return processed


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []

    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            chunks.append(subtree)

    return chunks


if __name__ == "__main__":
    main()
