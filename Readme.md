# KaStack Conversation Intelligence System

## Overview

KaStack Conversation Intelligence System is a Retrieval-Augmented Generation (RAG) based application designed to analyze conversational datasets, detect topic transitions, generate topic checkpoints, create periodic message summaries, extract user persona information, and answer user queries using retrieved conversational context.

The system processes conversations chronologically and maintains contextual memory through topic checkpoints and message checkpoints. It combines semantic retrieval and persona extraction to provide intelligent responses grounded in conversation history.

This project was developed as part of the AI/ML Engineer Intern assessment.

---

# Problem Statement

The objective of this project is to build a conversation intelligence system capable of:

* Processing conversations chronologically.
* Detecting topic changes over time.
* Creating topic checkpoints whenever discussions shift.
* Generating summaries for each topic segment.
* Creating summaries for every 100 messages.
* Extracting user persona information from conversations.
* Building a chatbot that answers questions using retrieved conversational context and persona information.

---

# System Architecture

Conversation Dataset

↓

Message Parsing

↓

Chronological Processing

↓

Topic Detection

↓

Topic Checkpoints + Topic Summaries

↓

100 Message Checkpoints

↓

Persona Extraction

↓

Embedding Generation

↓

Similarity-Based Retrieval

↓

Conversation Intelligence Chatbot

---

# Key Features

## 1. Chronological Conversation Processing

The system processes conversations in their original chronological order.

Each conversation is parsed message-by-message to preserve context and ensure topic detection follows the natural flow of discussion.

This satisfies the requirement of processing conversation history sequentially rather than treating the entire dataset as a single block.

---

## 2. Topic Checkpoint Generation

Whenever the semantic meaning of the conversation changes significantly, a new topic checkpoint is created.

Each checkpoint contains:

* Topic ID
* Start Message Index
* End Message Index
* Topic Summary

Example:

Topic 1

Messages: 1 – 25

Summary: Discussion about moving to a new city and career plans.

Topic 2

Messages: 26 – 60

Summary: Discussion about education and future studies.

These checkpoints allow the system to maintain structured conversational memory.

---

## 3. Topic Detection Methodology

Topic detection is performed using semantic similarity between messages.

### Embedding Model

SentenceTransformer

Model Used:

all-MiniLM-L6-v2

### Detection Process

1. Convert each message into an embedding vector.
2. Compare consecutive messages using cosine similarity.
3. Detect topic shifts when similarity drops below a predefined threshold.
4. Create a new topic checkpoint whenever a topic transition is detected.

This approach allows the system to identify meaningful changes in conversation themes.

---

## 4. Topic Summarization

Each detected topic segment is summarized independently.

The summarization process creates lightweight extractive summaries without relying on external large language model APIs.

Purpose:

* Improve retrieval quality.
* Provide quick topic understanding.
* Reduce storage complexity.
* Support efficient context retrieval.

---

## 5. 100 Message Checkpoints

Apart from topic checkpoints, the system creates checkpoints every 100 messages.

These checkpoints are independent of topic boundaries and provide long-term conversational memory.

Example:

Messages 1 – 100

Messages 101 – 200

Messages 201 – 300

Each checkpoint stores:

* Start Message Number
* End Message Number
* Summary

This satisfies the requirement of creating periodic summaries throughout the conversation timeline.

---

# Persona Extraction

The system extracts user persona information directly from conversation signals.

Persona extraction is evidence-driven and avoids unsupported assumptions.

---

## Persona Categories

### Habits

Examples:

* Talks about studying
* Talks about work
* Exercise related discussions

Each habit is supported by observable conversational evidence.

---

### Personal Facts

Examples:

* Student

Facts are extracted only when explicitly mentioned within conversations.

---

### Personality Traits

Examples:

* Curious
* Goal-Oriented

Traits are derived from recurring conversational patterns and supported by evidence.

---

### Communication Style

The system analyzes:

* Average words per message
* Message length characteristics
* Communication behavior

Example:

Average Words Per Message: 11.56

Message Style: Short

---

# Retrieval-Augmented Generation (RAG)

The chatbot uses Retrieval-Augmented Generation principles rather than relying solely on predefined responses.

The retrieval pipeline ensures answers are grounded in relevant conversation history.

---

## Embedding Model

SentenceTransformer

Model:

all-MiniLM-L6-v2

---

## Retrieval Process

User Question

↓

Convert Query to Embedding

↓

Calculate Cosine Similarity

↓

Retrieve Relevant Topic Summaries

↓

Retrieve Relevant Message Checkpoints

↓

Combine Retrieved Context

↓

Generate Response

This satisfies the requirement of retrieving both topic summaries and message chunks before answering.

---

# Chatbot Functionality

The chatbot combines:

1. Persona Information
2. Topic Retrieval Results
3. Message Checkpoint Retrieval Results

Supported Questions:

* What kind of person is this user?
* What are their habits?
* How do they talk?
* Study-related questions
* Work-related questions
* General conversational queries

The chatbot responds using retrieved conversational context rather than static responses.

---

# Technologies Used

## Programming Language

Python

---

## Libraries

* Pandas
* Sentence Transformers
* Scikit-Learn
* Streamlit
* JSON

---

# Project Structure

KaStack-Conversation-Intelligence-System/

│

├── app.py

├── parser.py

├── topic_detector.py

├── summarizer.py

├── process_all.py

├── rag_utils.py

├── retriever.py

├── message_retriever.py

├── persona.py

│

├── persona.json

├── topic_checkpoints.json

├── 100_message_checkpoints.json

│

├── conversations.csv

├── requirements.txt

├── README.md

│

└── assets/

---

# How to Run

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Run the Streamlit Application

```bash
py -m streamlit run app.py
```

## Step 3: Open Browser

Streamlit will generate a local URL.

Open the URL in your browser.

---

# Evaluation Requirements Covered

✅ Chronological Conversation Processing

✅ Topic Change Detection

✅ Topic Checkpoint Creation

✅ Topic Summaries

✅ 100 Message Checkpoints

✅ User Persona Extraction

✅ Communication Style Analysis

✅ Embedding-Based Retrieval

✅ Topic Summary Retrieval

✅ Message Checkpoint Retrieval

✅ Retrieval-Augmented Chatbot

✅ End-to-End Working Application

---

# Future Improvements

Potential enhancements include:

* Advanced topic segmentation techniques
* Improved abstractive summarization
* Vector database integration
* Multi-user persona tracking
* Conversation analytics dashboard
* Enhanced retrieval ranking strategies
* Memory optimization for large-scale datasets

---

# Conclusion

The KaStack Conversation Intelligence System demonstrates a complete conversational intelligence pipeline capable of understanding long conversations, identifying topic transitions, extracting user persona information, retrieving relevant context, and answering questions through a Retrieval-Augmented Generation (RAG) framework.

The solution emphasizes explainability, lightweight architecture, chronological processing, and practical conversational memory management while avoiding heavy dependence on external LLM APIs.

The project successfully satisfies all major requirements of the assessment, including topic checkpoint generation, 100-message checkpoint creation, persona extraction, semantic retrieval, and chatbot-based interaction.
