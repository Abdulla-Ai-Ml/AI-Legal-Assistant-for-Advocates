🚀 Introducing AI Legal Adviser: Your AI-Powered Legal Assistant for Indian Law ⚖️
I’m thrilled to share my latest project: AI Legal Adviser, a cutting-edge AI-powered tool designed to assist advocates and individuals with legal queries related to Indian law. This project combines advanced AI technologies, natural language processing (NLP), and a user-friendly interface to make legal information more accessible and actionable.

Whether you’re an advocate looking for quick legal references or someone seeking clarity on Indian law, this tool is here to help—in both English and Hindi!

✨ Key Features
Multilingual Support:

Handles queries in both English and Hindi, making it accessible to a wider audience.

Voice Input:

Speak your query instead of typing! The tool uses speech recognition to convert your voice into text, supporting both English and Hindi.

Contextual Legal Advice:

Generates accurate and context-aware responses using Groq’s advanced language models combined with InLegalBERT embeddings.

Efficient Document Retrieval:

Uses FAISS (Facebook AI Similarity Search) to quickly retrieve the most relevant legal documents from a curated database.

User-Friendly Interface:

Built with Streamlit, the interface is simple, intuitive, and easy to navigate.

🛠️ How It Works
User Input:

Users can either type or speak their legal query. The tool detects the language (English or Hindi) automatically.

Legal Document Search:

The query is processed using InLegalBERT, a legal-specific NLP model, to generate embeddings. These embeddings are then used to search a database of legal texts using FAISS.

Response Generation:

The retrieved legal documents are passed to Groq’s language model (LLama-3.3-70b) to generate a contextual and accurate response.

Display Results:

The response is displayed in the chat interface, along with the relevant legal documents for reference.

🔧 Technologies Used
Natural Language Processing (NLP):

InLegalBERT: A legal-specific variant of BERT for generating embeddings of legal texts.

Machine Learning:

PyTorch: For handling model inference and tensor operations.

Vector Search:

FAISS: For efficient and fast retrieval of relevant legal documents.

Conversational AI:

LangChain: For managing prompt templates and conversational memory.

Speech Recognition:

SpeechRecognition Library: For converting speech to text.

Advanced Language Models:

Groq API: For generating high-quality, context-aware responses.

Web Interface:

Streamlit: For building a simple and interactive web app.

💡 Why This Matters
The AI Legal Adviser is more than just a tool—it’s a step toward democratizing access to legal information. By leveraging AI, this project aims to:

Empower advocates with quick and accurate legal references.

Help individuals understand complex legal concepts in a simple and accessible way.

Bridge the gap between technology and law, making legal knowledge available to everyone.
