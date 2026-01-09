
# simple_rag.py
# --------------------------------------------
# A VERY SIMPLE RAG DEMO FOR CLASS 10 STUDENTS
# --------------------------------------------
# RAG means "Retrieval-Augmented Generation".
# 1) RETRIEVAL: Find the most relevant text chunks for a question.
# 2) GENERATION: Write an answer using those chunks (with sources).
#
# This program uses only basic Python (no external AI packages).
# It shows the core idea with word-count vectors and cosine similarity.

import re
import math
from collections import Counter
from typing import List, Tuple

# -----------------------------
# 0) SMALL "LIBRARY" OF DOCUMENTS
# -----------------------------
# Imagine these are textbook notes or help articles.
DOCUMENTS = [
    {
        "title": "Solar System Basics",
        "text": """The Solar System has the Sun at the center. 
        Planets like Mercury, Venus, Earth, and Mars are inner rocky planets. 
        Jupiter and Saturn are gas giants. Uranus and Neptune are ice giants. 
        Moons orbit many planets. Asteroids and comets also belong to the Solar System."""
    },
    {
        "title": "Photosynthesis Explained",
        "text": """Photosynthesis happens in the chloroplasts of plant cells. 
        Plants use sunlight, carbon dioxide, and water to make glucose and oxygen. 
        Chlorophyll captures light energy. This process is vital for life on Earth."""
    },
    {
        "title": "Basic Electricity",
        "text": """Electric current is the flow of electrons through a conductor. 
        Voltage is the push that drives electrons. Resistance opposes current flow. 
        Ohm's Law connects them: V = I × R. Batteries provide a voltage difference."""
    },
    {
        "title": "Gravity and Orbits",
        "text": """Gravity is a force that pulls objects together. 
        The Sun's gravity keeps planets in orbit. Faster sideways speed plus gravity 
        creates circular or elliptical paths. Satellites orbit Earth using the same idea."""
    }
]

# ----------------------------------
# 1) TEXT PREPROCESSING (KEEP IT SIMPLE)
# ----------------------------------
def clean(text: str) -> List[str]:
    """
    Convert text to a list of lowercase words.
    - Remove punctuation
    - Split by spaces
    - Keep only alphabetic tokens (no numbers for simplicity)
    """
    text = text.lower()
    # Replace non-letters with spaces
    text = re.sub(r"[^a-z]", " ", text)
    # Split and remove empty strings
    tokens = [t for t in text.split() if t]
    print("Flow 3-clean")
    print(tokens)
    return tokens

# -----------------------------------
# 2) MAKE A "BAG-OF-WORDS" VECTOR
# -----------------------------------
def vectorize(tokens: List[str]) -> Counter:
    """
    Count how many times each word appears.
    This is called a 'bag-of-words' model.
    Example: ["sun", "gravity", "sun"] -> {"sun": 2, "gravity": 1}
    """
    print("Flow 3-Vectorize")
    return Counter(tokens)

# -----------------------------------
# 3) COSINE SIMILARITY (MATH PART)
# -----------------------------------
def cosine_similarity(v1: Counter, v2: Counter) -> float:
    """
    Measure how similar two word-count vectors are.
    Cosine similarity = dot(v1, v2) / (|v1| * |v2|)
    Values range from 0 (not similar) to 1 (very similar).
    """
    print("Flow 4-Cosine Similarity")
    # Dot product: sum over common words of count1 * count2
    dot = sum(v1[w] * v2[w] for w in v1.keys() & v2.keys())
    print("dot:", dot)
    # Magnitudes: sqrt(sum of counts^2)
    mag1 = math.sqrt(sum(c * c for c in v1.values()))
    mag2 = math.sqrt(sum(c * c for c in v2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)

# -------------------------------------------------------
# 4) RETRIEVE: RANK DOCUMENTS BY SIMILARITY TO THE QUESTION
# -------------------------------------------------------
def retrieve_top_k(question: str, k: int = 2) -> List[Tuple[float, dict]]:
    """
    Return the top-k most similar documents to the question.
    Each item is (similarity_score, document_dict).
    """
    print("Flow 2-retrieve_top_k")
    print("Flow 2-question")
    q_vec = vectorize(clean(question))
    print("Flow 4-retrieve_top_k")
    scored = []
    for doc in DOCUMENTS:
        print("Flow 4-document")
        d_vec = vectorize(clean(doc["text"]))
        score = cosine_similarity(q_vec, d_vec)
        scored.append((score, doc))
    # Sort by score descending
    scored.sort(key=lambda x: x[0], reverse=True)
    # Pick top k
    return scored[:k]

# -------------------------------------------------------
# 5) GENERATE: BUILD A FRIENDLY ANSWER USING RETRIEVED DOCS
# -------------------------------------------------------
def generate_answer(question: str, top_docs: List[Tuple[float, dict]]) -> str:
    """
    Create an answer by:
    - Taking helpful lines from the best documents
    - Adding a short explanation
    - Citing sources (document titles)
    NOTE: This is a simple 'rule-based' generator, not a real LLM.
    """
    # Collect sentences from top docs
    sentences = []
    sources = []
    for score, doc in top_docs:
        print("Flow 5-generate_answer")
        # Save source title for citation
        sources.append(f"{doc['title']} (score={score:.2f})")
        # Choose 1-2 informative sentences from each doc
        raw_sentences = [s.strip() for s in doc["text"].split(".") if s.strip()]
        # Heuristic: keep short, clear lines
        pick = raw_sentences[:2]
        sentences.extend(pick)

    # A simple "generated" answer:
    answer = []
    answer.append("Here’s a helpful explanation based on what I found:\n")
    # Join selected sentences
    answer.append(" - " + "\n - ".join(sentences))
    answer.append("\n\nWhy these lines? Because they are most similar to your question using word-matching math (cosine similarity).")
    answer.append("\n\nSources:\n" + "\n".join(f" • {src}" for src in sources))
    return "".join(answer)

# -----------------------------------
# 6) MAIN: ASK A QUESTION, GET AN ANSWER
# -----------------------------------
def rag_answer(question: str, k: int = 2) -> str:
    """
    Full RAG pipeline:
    1) Retrieve top-k relevant documents.
    2) Generate a clear, short answer using those documents.
    """
    print("Flow 1-rag_answer")
    top_docs = retrieve_top_k(question, k=k)
    print("Flow 5-rag_answer")
    print(top_docs)
    # If nothing matches well, be honest:
    if all(score == 0.0 for score, _ in top_docs):
        return "I couldn't find helpful information for that question in my small library. Try rephrasing or add more documents."
    return generate_answer(question, top_docs)

# -----------------
# 7) TRY IT OUT!
# -----------------
if __name__ == "__main__":
    print("=== SIMPLE RAG DEMO ===")
    user_question = input("Ask your question (e.g., 'Why do planets orbit the Sun?'): ")
    print("\nAnswer:\n")
    print("Flow Start")
    print(rag_answer(user_question, k=2))
    print("Flow End")
    print("\n(Tip: Try questions about 'gravity', 'solar system', 'photosynthesis', or 'electricity'.)")