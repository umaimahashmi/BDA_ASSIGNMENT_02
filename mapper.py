#!/usr/bin/env python3

import sys
import math
from collections import defaultdict

def calculate_tf(document):
    term_frequency_dict = defaultdict(int)
    terms = document.lower().split()
    for term in terms:
        term_frequency_dict[term] += 1
    return term_frequency_dict

def calculate_idf(documents):
    total_documents = len(documents)
    document_frequency = defaultdict(int)
    for document in documents:
        terms = set(document.lower().split())
        for term in terms:
            document_frequency[term] += 1

    idf_scores = {}
    for term, freq in document_frequency.items():
        idf = math.log(total_documents / (1 + freq))
        idf_scores[term] = round(idf, 2)  # Round IDF to two decimal places
    return idf_scores

def main():
    documents = []
    for line in sys.stdin:
        _, text = line.strip().split(",", 1)  # Split line into ID and TEXT, discard ID
        documents.append(text)

    # Calculate TF scores for each document
    tf_scores = {i: calculate_tf(doc) for i, doc in enumerate(documents, 1)}

    # Calculate IDF scores
    idf_scores = calculate_idf(documents)

    # Output TF-IDF scores to stdout
    for doc_id, tf in tf_scores.items():
        tf_idf_scores = {term: tf_value * idf_scores[term] for term, tf_value in tf.items()}
        tf_idf_string = ",".join(f"{term}:{tf_idf}" for term, tf_idf in tf_idf_scores.items())
        print(f"{doc_id}\t{tf_idf_string}")

if __name__ == "__main__":
    main()

