import re
import math
from collections import Counter

def read_file(path: str) -> str:
    """Open file and read all text"""
    with open(path, 'r') as f:
        text = f.read() 
    return text


def tokenize(text: str) -> list[str]:
    """Change string into list of words without spaces and special chars"""
    result = re.findall(r'\b\w+\b', text.lower())
    return result


def create_ngrams(text: str, n: int) -> list[tuple[str]]:
    """Creates n-grams from given text after tokenizing"""
    words = tokenize(text)
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]


def calculate_tf(word: str, document: str) -> float:
    # Calculate term frequency. Helper for TF-IDF vectorizer
    words = tokenize(document)
    word_count = Counter(words)
    return word_count[word] / len(words)

def calculate_idf(word: str, documents: list[str]) -> float:
    # Calculate inverse document frequency. Helper for TF-IDF vectorizer
    document_count = sum(1 for doc in documents if word in tokenize(doc))
    return math.log(len(documents) / (document_count + 1))


def tfidf_vectorizer(documents: list[str]) -> list[list[float]]:
    """Calculate TF-TDF matrix from list of document strings and return it"""
    unique_words = set(word for doc in documents for word in tokenize(doc))
    tfidf_matrix = []

    for doc in documents:
        tfidf_vector = []
        for word in unique_words:
            tf = calculate_tf(word, doc)
            idf = calculate_idf(word, documents)
            tfidf_vector.append(tf * idf)
        tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix









