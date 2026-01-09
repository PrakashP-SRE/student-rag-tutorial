# Student RAG Tutorial

A **Retrieval-Augmented Generation (RAG)** educational project designed to help students understand the fundamentals of information retrieval and answer generation using basic Python.

## 🎯 What is RAG?

RAG stands for "Retrieval-Augmented Generation" and consists of two main steps:

1. **RETRIEVAL**: Find the most relevant text chunks for a question using similarity matching
2. **GENERATION**: Create an answer using those chunks with proper source citations

## 🔧 How it Works

This implementation demonstrates:
- **Text preprocessing** and tokenization
- **Bag-of-words** vector representation
- **Cosine similarity** for document ranking
- **Simple rule-based** answer generation
- **Source attribution** and citation

## ✨ Features

- ✅ No external AI packages required - pure Python implementation
- ✅ Educational focus with step-by-step comments
- ✅ Interactive question-answering interface
- ✅ Example questions for testing and learning
- ✅ Source citation with similarity scores
- ✅ Sample documents covering basic science topics

## 📚 Sample Topics Covered

- **Solar System**: Planets, moons, asteroids, and basic astronomy
- **Photosynthesis**: How plants convert sunlight to energy
- **Basic Electricity**: Current, voltage, resistance, and Ohm's Law
- **Gravity and Orbits**: How gravitational forces work in space

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PrakashP-SRE/student-rag-tutorial.git
   cd student-rag-tutorial
   ```

2. **Run the main program:**
   ```bash
   python RAG_10thstd.py
   ```

3. **Try the example questions:**
   ```bash
   python example_questions.py
   ```

4. **Enter your question when prompted**

## 🎮 Example Usage

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

## 📁 Project Structure

```
student-rag-tutorial/
├── RAG_10thstd.py          # Main RAG implementation with detailed comments
├── example_questions.py    # Example questions and interactive demo
├── README.md              # This documentation
├── requirements.txt       # Python dependencies (currently none needed)
├── LICENSE               # MIT license for open source use
└── .gitignore           # Git ignore rules
```

## 🧪 Try These Questions

- "Why do planets orbit the Sun?"
- "How does photosynthesis work in plants?"
- "What is electric current made of?"
- "Tell me about the solar system"
- "What is Ohm's Law in electricity?"
- "How do satellites stay in orbit?"

## 🎓 Educational Goals

This project demonstrates fundamental concepts in:

- **Information Retrieval**: How search engines find relevant documents
- **Vector Space Models**: Mathematical representation of text
- **Similarity Measurement**: Comparing documents using cosine similarity
- **Text Processing**: Cleaning and preparing text for analysis
- **Source Attribution**: Citing where information comes from

Perfect for students learning about:
- Natural Language Processing basics
- Search algorithms
- Text mining concepts
- Python programming
- Mathematical concepts in computer science

## 🛠️ Technical Details

### Text Preprocessing
- Converts text to lowercase
- Removes punctuation and numbers
- Tokenizes into individual words

### Vectorization
- Uses bag-of-words model
- Counts word frequencies
- Creates sparse vector representations

### Similarity Calculation
- Implements cosine similarity formula
- Measures angle between document vectors
- Returns scores from 0 (no similarity) to 1 (identical)

### Answer Generation
- Extracts relevant sentences from top documents
- Provides source citations with similarity scores
- Explains reasoning behind answer selection

## 🤝 Contributing

This is an educational project! Feel free to:
- Add more sample documents
- Improve the answer generation logic
- Add new example questions
- Enhance the user interface
- Create visualizations of the similarity calculations

## 📄 License

This project is open source and available under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

Created for educational purposes to help students understand the basics of RAG systems and information retrieval. Perfect for classroom demonstrations and learning exercises.

---

**Happy Learning! 🚀📚**
