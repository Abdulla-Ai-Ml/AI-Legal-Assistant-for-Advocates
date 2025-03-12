# AI Legal Adviser

## Overview
AI Legal Adviser is an advanced AI-powered legal assistant designed to help advocates and legal professionals quickly access relevant Indian legal information. This project leverages natural language processing (NLP) and deep learning to provide legal insights based on user queries in English or Hindi. The assistant retrieves relevant legal documents, understands the user's query, and generates contextually accurate responses.

## Features
- **Legal Document Retrieval**: Uses FAISS for efficient searching and retrieval of relevant legal documents.
- **AI-Powered Responses**: Utilizes Groq's Llama-based model to generate legal responses.
- **Multi-Language Support**: Supports queries in both English and Hindi.
- **Voice Input**: Converts speech to text for hands-free interaction.
- **Context Awareness**: Maintains conversation history using LangChain's memory module.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building an interactive web-based UI.
- **Transformers (Hugging Face)**: Loads and processes the InLegalBERT model for legal text embedding.
- **FAISS (Facebook AI Similarity Search)**: Enables fast and accurate searching of legal documents.
- **LangChain**: Manages conversation history and integrates AI models.
- **Groq API**: Generates AI-based legal responses.
- **SpeechRecognition**: Provides speech-to-text functionality.
- **LangDetect**: Identifies the language of user queries.

## How It Works
### 1. Load Legal Documents and Create Embeddings
- Predefined Indian legal texts are embedded using the InLegalBERT model.
- FAISS indexes these embeddings to enable quick retrieval.

### 2. Process User Queries
- Users can type their legal queries in English or Hindi.
- Alternatively, they can use voice input, which gets converted to text.

### 3. Retrieve Relevant Legal Documents
- The system searches for relevant legal texts using FAISS.
- The most relevant legal excerpts are retrieved for context.

### 4. Generate AI-Based Legal Advice
- Language detection is performed to determine whether the query is in English or Hindi.
- A dynamic prompt is created using LangChain, including the query and retrieved legal context.
- Groq's AI model generates a legal response based on the prompt.

### 5. Display the Response
- The chatbot displays the AI-generated response along with relevant legal documents.
- Users can view more details through an expandable section.

- ![image1](https://github.com/user-attachments/assets/00c7ce6f-7817-4ff9-96d0-2f9894a5c9df)
- ![image2](https://github.com/user-attachments/assets/e7b5a213-5edd-4810-a666-0ebeaa560d82)
![image3](https://github.com/user-attachments/assets/2678b3df-d49b-4cc9-aea9-3b0e639878c0)
![image4](https://github.com/user-attachments/assets/c76faa3c-57c2-4035-8108-fbcb7e45f5a6)





## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pip

### Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Abdulla-Ai-Ml/AI-Legal-Assistant-for-Advocates.git]
  cd AI-Legal-Assistant-for-Advocates
   
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the Groq API key:
   Replace `GROQ_API_KEY` in the script with your own API key.

4. Run the application:
   ```bash
   streamlit run ai-legal-assistant.py
   ```

## Future Improvements
- Expand the legal database with more documents.
- Integrate additional AI models for better legal interpretations.
- Improve multi-language support with additional Indian languages.
- Enhance the UI with a more intuitive design.


