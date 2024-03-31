#!/usr/bin/env python3

import sys
from collections import defaultdict

def main():
    tf_idf_scores = defaultdict(dict)

    for line in sys.stdin:
        doc_id, tf_idf_string = line.strip().split("\t")
        tf_idf_pairs = tf_idf_string.split(",")
        for pair in tf_idf_pairs:
            term, tf_idf = pair.split(":")
            tf_idf_scores[doc_id][term] = float(tf_idf)

    # Calculate relevance for each document
    query_text = "spanish west florida"
    query_terms = query_text.lower().split()
    query_tf_idf = {term: 1.0 for term in query_terms}  # Assuming TF=1 for each term in the query

    relevance_results = {}
    for doc_id, doc_tf_idf in tf_idf_scores.items():
        relevance_score = sum(query_tf_idf[term] * doc_tf_idf.get(term, 0.0) for term in query_terms)
        relevance_results[doc_id] = relevance_score

    # Sort and print relevance results
    sorted_relevance = sorted(relevance_results.items(), key=lambda x: x[1], reverse=True)
    for doc_id, score in sorted_relevance:
        print(f"doc {doc_id}: {score}")

if __name__ == "__main__":
    main()

