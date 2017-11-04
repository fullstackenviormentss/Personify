import ronald_brain.util.preprocessor as preprocessor
import ronald_brain.util.constants as constants
from ronald_brain.util.preprocessor import Ngram
from ronald_brain.models.markov_chain import *

from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

def favourite_english_words():
    pp = preprocessor.Preprocessor("/home/rory/projects/ronald/data/trump-tweets.csv")
    words = pp.words_only()
    count = Counter(words)
    labels, values = zip(*count.items())

    word_dict = {"word" : labels, "count": values}
    df = pd.DataFrame(word_dict)

    df = df.loc[df['count'] > 250]

    sns_plot = sns.factorplot(x='word', y='count', data=df, kind='bar', aspect=2)
    sns_plot.savefig("graphs/histograms/english_word_count.png")

    # plt.show()


def words_after_word(target_word):
    pp = preprocessor.Preprocessor("/home/rory/projects/ronald/data/trump-tweets.csv", "/home/rory/projects/ronald/data/trump-speeches.txt")
    words = [t for t in pp.combined_tokens if t not in USELESS_PUNCTUATION + FRONT_PUNCTUATION]

    grams = pp.build_n_grams(words, 5)

    target_bigrams = [t for t in grams if t[0] == target_word]

    target_follow = [' '.join(t[1:]) for t in target_bigrams]

    count = Counter(target_follow)
    labels, values = zip(*count.items())

    word_dict = {"word": labels, "count": values}
    df = pd.DataFrame(word_dict).sort_values('count', ascending=False)

    df = df.head(7)

    sns_plot = sns.factorplot(x='word', y='count', data=df, kind='bar', aspect=2)
    # sns_plot.savefig("graphs/histograms/english_word_count.png")

    plt.show()


# favourite_english_words()
words_after_word("trump")


