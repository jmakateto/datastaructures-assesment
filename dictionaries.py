
import re
from collections import defaultdict

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    words = sentence.split()
    frequency = defaultdict(int)

    for word in words:
        frequency[word] += 1

    return dict(frequency)
