# Simple RAG Demo for Class 10 Students

A **Retrieval-Augmented Generation (RAG)** demonstration built with basic Python to help Class 10 students understand the core concepts of information retrieval and answer generation.

## What is RAG?

RAG stands for "Retrieval-Augmented Generation" and consists of two main steps:

1. **RETRIEVAL**: Find the most relevant text chunks for a question
2. **GENERATION**: Write an answer using those chunks with proper source citations

## How it Works

This implementation uses:
- **Word-count vectors** (bag-of-words model)
- **Cosine similarity** for document ranking
- **Simple rule-based answer generation**

## Features

- ✅ No external AI packages required - pure Python implementation
- ✅ Educational focus with detailed comments
- ✅ Sample documents covering basic science topics
- ✅ Interactive question-answering interface
- ✅ Source citation and similarity scoring
- ✅ Example questions file for testing and learning
- ✅ Step-by-step educational explanations

## Sample Topics Covered

- Solar System Basics
- Photosynthesis
- Basic Electricity
- Gravity and Orbits

## How to Run

1. Make sure you have Python 3.x installed
2. Clone this repository:
   ```bash
   git clone https://github.com/PrakashP-SRE/student-rag-tutorial.git
   cd student-rag-tutorial
   ```
3. Run the main program:
   ```bash
   python RAG_10thstd.py
   ```
4. Or try the example questions:
   ```bash
   python example_questions.py
   ```
5. Enter your question when prompted

## Example Usage

```
Ask your question (e.g., 'Why do planets orbit the Sun?'): How does photosynthesis work?

Answer:
Here's a helpful explanation based on what I found:

- Photosynthesis happens in the chloroplasts of plant cells
- Plants use sunlight, carbon dioxide, and water to make glucose and oxygen

Why these lines? Because they are most similar to your question using word-matching math (cosine similarity).

Sources:
• Photosynthesis Explained (score=0.85)
```

## Educational Goals

This project demonstrates:
- Text preprocessing and tokenization
- Vector space models in information retrieval
- Similarity measurement using cosine similarity
- Basic natural language processing concepts
- Source attribution and citation

## Project Files

- `RAG_10thstd.py` - Main RAG implementation with detailed comments
- `example_questions.py` - Example questions and interactive demo
- `README.md` - This documentation
- `requirements.txt` - Python dependencies (currently none needed)
- `LICENSE` - MIT license for open source use

## Try These Questions

- "Why do planets orbit the Sun?"
- "How does photosynthesis work?"
- "What is electric current?"
- "Tell me about gravity"

## License

This project is open source and available under the MIT License.
