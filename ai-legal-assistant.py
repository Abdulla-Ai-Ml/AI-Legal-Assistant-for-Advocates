import streamlit as st
from transformers import AutoTokenizer, AutoModel
import torch
import faiss
import numpy as np
import os
from langdetect import detect
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from groq import Groq
import speech_recognition as sr  # For speech-to-text

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Initialize Groq client
GROQ_API_KEY = "enter your key"  # Replace with your Groq API key
groq_client = Groq(api_key=GROQ_API_KEY)

# Load InLegalBERT from Hugging Face
LEGAL_MODEL = "law-ai/InLegalBERT"
tokenizer = AutoTokenizer.from_pretrained(LEGAL_MODEL)
model = AutoModel.from_pretrained(LEGAL_MODEL)

# Load Legal Documents (Example Data)
legal_texts = [
    "Article 21 of the Indian Constitution guarantees the right to life and personal liberty.",
    "IPC Section 302 deals with punishment for murder, which is death or life imprisonment.",
    "The Consumer Protection Act, 2019 provides remedies to consumers against unfair trade practices.",
    "The Right to Information Act, 2005 empowers citizens to seek information from public authorities.",
    "The Indian Evidence Act, 1872 governs the admissibility of evidence in Indian courts."
]

# Embed Legal Documents using InLegalBERT
def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy()

legal_embeddings = np.vstack([embed_text(text) for text in legal_texts])

# Create FAISS Index for Searching Legal Texts
index = faiss.IndexFlatL2(legal_embeddings.shape[1])
index.add(legal_embeddings)

# Search Legal Documents
def search_legal_documents(query, k=3):
    query_embedding = embed_text(query)
    D, I = index.search(query_embedding, k=k)
    return [legal_texts[i] for i in I[0]]

# Initialize LangChain Memory
memory = ConversationBufferMemory()

# Define Prompt Templates
english_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
    You are an expert legal assistant for advocates. Answer the user's query based on Indian law and the provided legal context.
    User Query: {query}
    Legal Context: {context}
    """
)

hindi_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
    आप भारतीय कानून के विशेषज्ञ हैं। उपयोगकर्ता के प्रश्न का उत्तर दें और प्रदान किए गए कानूनी संदर्भ के आधार पर हिंदी में उत्तर दें।
    उपयोगकर्ता प्रश्न: {query}
    कानूनी संदर्भ: {context}
    उत्तर हिंदी में दें।
    """
)

# Function to generate response using Groq
def generate_groq_response(prompt):
    try:
        response = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",  # Replace with the actual Groq model name
            max_tokens=1024,
            temperature=1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response at the moment."

# Function to convert speech to text with pause detection
def speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2.0  # Set pause threshold to 2 seconds
    with sr.Microphone() as source:
        st.write("Listening... Speak now. Pause for 2 seconds to stop.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="en-IN")  # Supports Hindi and English
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            st.error("Sorry, there was an issue with the speech recognition service.")
            return None

# Streamlit UI
st.set_page_config(page_title="AI Legal Assistant", page_icon="⚖️", layout="centered")
st.title("⚖️ AI Legal Assistant for Advocates")
st.write("Welcome to the AI Legal Assistant! Ask me anything related to Indian law in English or Hindi.")

# Add a button for voice input
if st.button("🎤 Use Voice Input"):
    query = speech_to_text()
else:
    query = st.chat_input("Ask a legal question in English or Hindi...")

if query:
    # Detect language of the query
    try:
        language = detect(query)
    except:
        language = "en"  # Default to English if detection fails

    # Step 1: Search for relevant legal documents
    legal_context = search_legal_documents(query)
    
    # Step 2: Generate a response using Groq
    if language == "hi":
        prompt = hindi_prompt.format(query=query, context="\n".join(legal_context))
    else:
        prompt = english_prompt.format(query=query, context="\n".join(legal_context))
    
    response = generate_groq_response(prompt)
    
    # Display chat history
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        st.write(response)
    
    # Display relevant legal documents
    with st.expander("Relevant Legal Documents"):
        for doc in legal_context:
            st.write(doc)
