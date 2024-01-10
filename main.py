from collections import Counter
from preprocessing import tfidf_vectorizer,read_file,create_ngrams,tokenize
from metrics import euclidean_distance,jaccard_similarity,dtw_distance,get_cosine_similarity


def compare_docs(doc1 : str, doc2 : str, similarity : str, n_gram = 2) -> float:

    if similarity== "cosine":
        val1,val2 = Counter(tokenize(doc1)),Counter(tokenize(doc2))
        similarity_function = get_cosine_similarity

    elif similarity == "euclidean":
        tf_idf_mat = tfidf_vectorizer([doc1,doc2])
        val1,val2 = tf_idf_mat[0],tf_idf_mat[1]
        similarity_function = euclidean_distance

    elif similarity == "jaccard":
        val1 = set(create_ngrams(doc1, n_gram))
        val2 = set(create_ngrams(doc2, n_gram))
        similarity_function = jaccard_similarity

    elif similarity == "dtw":
        val1 = create_ngrams(doc1, n_gram)
        val2 = create_ngrams(doc2, n_gram)
        similarity_function = dtw_distance

    else:
        raise ValueError("Invalid similarity")

    similarity = similarity_function(val1, val2)
    return similarity


if __name__ == "__main__":

    doc1 = read_file('sample1.txt')
    doc2 = read_file('sample2.txt')
    doc3 = read_file('sample3.txt')
    

    # Frequency counting
    # Cosine similarity 
    score = compare_docs(doc1,doc2,"cosine")
    print("Cosine score 1-2:",score)
    score = compare_docs(doc1,doc3,"cosine")
    print("Cosine score 1-3:",score)

    # TF-IDF techniques
    # Euclidean distance using TF-IDF (not so good)
    score = compare_docs(doc1,doc2,"euclidean")
    print("Euclidean score 1-2:",score)
    score = compare_docs(doc1,doc3,"euclidean")
    print("Euclidean score 1-3:",score)


    # N-grams techniques
    # Jaccard similarity
    score = compare_docs(doc1,doc2,"jaccard")
    print("Jaccard score 1-2:",score)
    score = compare_docs(doc1,doc3,"jaccard")
    print("Jaccard score 1-3:",score)

    # Dynamic Time Warping distance
    score = compare_docs(doc1,doc2,"dtw",1)
    print("DTW score 1-2:",score)
    score = compare_docs(doc1,doc3,"dtw",1)
    print("DTW score 1-3:",score)


