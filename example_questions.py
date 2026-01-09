#!/usr/bin/env python3
"""
Example Questions for RAG Tutorial
==================================

This file contains example questions that work well with the RAG system
and demonstrates how to test the system with different types of queries.

Run this file to see the RAG system in action with predefined examples,
then try your own questions in the interactive demo.
"""

import sys
import os

# Add the current directory to Python path to import RAG_10thstd
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from RAG_10thstd import rag_answer

def run_examples():
    """Run a series of example questions to demonstrate the RAG system."""
    
    print("🚀 RAG Tutorial - Example Questions")
    print("=" * 50)
    print("This demo shows how the RAG system works with different types of questions.")
    print("Watch how it retrieves relevant information and generates answers!\n")
    
    # List of example questions with expected topics
    example_questions = [
        {
            "question": "Why do planets orbit the Sun?",
            "topic": "Gravity and Orbits",
            "explanation": "Tests understanding of gravitational forces"
        },
        {
            "question": "How does photosynthesis work in plants?",
            "topic": "Photosynthesis",
            "explanation": "Tests biological process knowledge"
        },
        {
            "question": "What is electric current?",
            "topic": "Basic Electricity", 
            "explanation": "Tests physics concepts about electricity"
        },
        {
            "question": "Tell me about the solar system",
            "topic": "Solar System",
            "explanation": "Tests general astronomy knowledge"
        },
        {
            "question": "What is Ohm's Law?",
            "topic": "Basic Electricity",
            "explanation": "Tests specific physics formulas"
        },
        {
            "question": "How do moons orbit planets?",
            "topic": "Gravity and Orbits",
            "explanation": "Tests orbital mechanics understanding"
        }
    ]
    
    for i, example in enumerate(example_questions, 1):
        print(f"📝 Example {i}: {example['topic']}")
        print("-" * 50)
        print(f"Question: {example['question']}")
        print(f"Focus: {example['explanation']}")
        print(f"\n🤖 RAG System Answer:")
        
        try:
            # Get answer from RAG system
            answer = rag_answer(example['question'], k=2)
            print(answer)
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure RAG_10thstd.py is in the same directory!")
        
        print("\n" + "="*70 + "\n")
        
        # Add a pause for readability
        input("Press Enter to continue to the next example...")

def interactive_demo():
    """Run an interactive demo where users can ask their own questions."""
    
    print("🎯 Interactive RAG Demo")
    print("=" * 40)
    print("Now it's your turn! Ask questions about:")
    print("📡 Solar System and planets")  
    print("🌱 Photosynthesis in plants")
    print("⚡ Basic electricity concepts")
    print("🌍 Gravity and orbits")
    print("\n💡 Tips:")
    print("- Use keywords that might appear in science textbooks")
    print("- Ask about concepts, not specific facts")
    print("- Try variations of the example questions")
    print("\nType 'quit', 'exit', or 'q' to finish\n")
    
    question_count = 0
    
    while True:
        user_question = input("🤔 Your question: ").strip()
        
        if user_question.lower() in ['quit', 'exit', 'q']:
            print(f"\n🎉 Thanks for trying the RAG tutorial!")
            print(f"You asked {question_count} questions. Great job exploring! 👋")
            break
            
        if not user_question:
            print("Please ask a question or type 'quit' to exit.")
            continue
        
        if user_question.endswith('?') == False:
            user_question += '?'  # Add question mark if missing
            
        question_count += 1
        print(f"\n🤖 RAG System Processing...")
        print("-" * 50)
        
        try:
            answer = rag_answer(user_question, k=2)
            print(answer)
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Make sure RAG_10thstd.py is in the same directory!")
        
        print("\n" + "-"*50)

def show_system_info():
    """Show information about how the RAG system works."""
    
    print("ℹ️  How This RAG System Works")
    print("=" * 40)
    print("1. 📝 PREPROCESSING: Your question is cleaned and tokenized")
    print("2. 🔍 VECTORIZATION: Words are converted to numerical vectors")
    print("3. 📊 SIMILARITY: Cosine similarity finds relevant documents") 
    print("4. 🎯 RETRIEVAL: Top matching documents are selected")
    print("5. ✍️  GENERATION: Answer is created using retrieved content")
    print("6. 📚 CITATION: Sources are provided with similarity scores")
    print("\nThis demonstrates the core concepts used in modern search engines!")
    print("-" * 60)

if __name__ == "__main__":
    print("🌟 Welcome to the Student RAG Tutorial! 🌟\n")
    
    # Show system information
    show_system_info()
    
    print("\nChoose what you'd like to do:")
    print("1️⃣  Run example questions (recommended first)")
    print("2️⃣  Jump to interactive demo")
    print("3️⃣  Both (examples first, then interactive)")
    
    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            print("\n🚀 Starting with example questions...\n")
            run_examples()
            break
        elif choice == "2": 
            print("\n🎯 Starting interactive demo...\n")
            interactive_demo()
            break
        elif choice == "3":
            print("\n🚀 Starting with examples, then interactive demo...\n")
            run_examples()
            print("\n" + "="*70)
            print("Now let's try the interactive demo!")
            print("="*70 + "\n")
            interactive_demo()
            break
        else:
            print("Please enter 1, 2, or 3")
