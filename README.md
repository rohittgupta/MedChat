# MedChat - Medical AI Chatbot

A comprehensive medical chatbot application powered by LLMs, RAG (Retrieval-Augmented Generation), and vector embeddings. This application provides accurate medical information and answers to health-related queries using Groq's Llama-3.1-8b and Pinecone vector database.

## Overview

MedChat is an intelligent chatbot that combines:
- **Large Language Models**: Groq's Llama-3.1-8b for fast, accurate responses
- **Retrieval-Augmented Generation (RAG)**: To ground responses in medical documents
- **Vector Embeddings**: Sentence Transformers for semantic search
- **Vector Database**: Pinecone for efficient similarity search
- **Web Interface**: Flask-based UI for easy interaction
- **Conversation Memory**: Maintains chat history for contextual conversations

## Features

- 🤖 **AI-Powered Medical Responses**: Uses Groq's Llama-3.1-8b for intelligent answer generation
- 📚 **Document-Based Search**: Retrieves relevant medical information from indexed documents
- 🔍 **Semantic Search**: Uses embeddings for intelligent document similarity matching
- 💬 **Conversational Interface**: User-friendly chat interface with conversation history
- 🏥 **Medical Context**: Grounded responses using medical literature and documents
- ⚡ **Fast Response Times**: Powered by Groq's inference API

## Tech Stack

### Backend
- **Flask 3.1.1**: Web framework
- **LangChain 0.3.26**: LLM orchestration and RAG implementation
- **Pinecone**: Vector database for semantic search
- **Groq API**: Language model (Llama-3.1-8b)

### LLM & Integration
- **LangChain-Groq**: Groq API integration for LangChain
- **LangChain-Pinecone 0.2.8**: Pinecone vector store integration

### Embeddings & NLP
- **Sentence Transformers 4.1.0**: Generate semantic embeddings (all-MiniLM-L6-v2)
- **LangChain Community 0.3.26**: Extended LangChain utilities
- **PyPDF 5.6.1**: PDF document processing

### Utilities
- **Python-dotenv 1.1.0**: Environment configuration management

### Frontend
- **HTML/CSS**: Responsive web interface

## Project Structure

```
MedChat/
├── app.py                 # Main Flask application
├── setup.py               # Package setup configuration
├── requirements.txt       # Python dependencies
├── store_index.py         # Vector index creation & management
├── template.sh            # Shell script template
├── README.md              # Project documentation
├── data/                  # Medical documents and data files
├── src/                   # Source code modules
│   ├── __init__.py
│   ├── helper.py          # Helper functions (embeddings, etc.)
│   ├── prompt.py          # System prompts and templates
│   └── __pycache__/
├── static/                # Static files
│   └── style.css          # Styling
├── templates/             # HTML templates
│   └── chat.html          # Chat interface
└── medical_chatbot.egg-info/  # Package metadata
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Groq API key (free tier available at https://console.groq.com)
- Pinecone API key (free tier available at https://www.pinecone.io)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd MedChat
   ```

2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   ```

5. **Prepare Vector Index**
   
   Run the index creation script to embed your medical documents:
   ```bash
   python store_index.py
   ```

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000` (or the configured port).

### Key Components

#### app.py
- Initializes Flask application
- Loads environment variables
- Configures embeddings and vector store
- Sets up RAG chain with retrieval and QA
- Handles API endpoints

#### src/helper.py
- Functions for downloading and managing embeddings
- Hugging Face model integration

#### src/prompt.py
- System prompts for the medical chatbot
- Prompt templates for consistent responses

#### store_index.py
- Creates and manages Pinecone vector indexes
- Processes and embeds medical documents

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Chat interface homepage |
| POST | `/ask` | Submit medical queries |
| GET | `/api/health` | Health check endpoint |

## How It Works

1. **Document Ingestion**: Medical documents are processed and split into chunks
2. **Embedding**: Each chunk is embedded using Sentence Transformers (all-MiniLM-L6-v2)
3. **Vector Storage**: Embeddings are stored in Pinecone for fast retrieval
4. **Query Processing**: User queries are embedded and compared against stored vectors
5. **Retrieval**: Most relevant documents are retrieved based on similarity
6. **Generation**: Groq's Llama-3.1-8b generates contextually accurate responses using retrieved documents
7. **Conversation Memory**: Chat history is maintained for coherent multi-turn conversations

## Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (for Llama-3.1-8b model)
- `PINECONE_API_KEY`: Your Pinecone API key
- Other Flask and application-specific configurations

### Pinecone Index

- **Index Name**: `medical-chatbot`
- **Search Type**: Similarity search
- **Top K Results**: 3 documents per query
- **Embedding Model**: Sentence Transformers (all-MiniLM-L6-v2, 384 dimensions)

## Requirements

See `requirements.txt` for complete dependencies:
- langchain==0.3.26
- flask==3.1.1
- sentence-transformers==4.1.0
- pypdf==5.6.1
- python-dotenv==1.1.0
- langchain-pinecone==0.2.8
- langchain-groq
- langchain-community==0.3.26

## Development

### Project Author
- **Name**: Boktiar Ahmed Bappy
- **Email**: entbappy73@gmail.com

### Version
- Current Version: 0.1.0

## Notes

- Ensure your medical documents are properly formatted before indexing
- The chatbot retrieves information from indexed documents for accuracy
- Responses are generated based on the most relevant retrieved documents
- Regular updates to the document index improve response quality

## License

This project is provided as-is for educational and medical information purposes.

## Disclaimer

⚠️ **Important**: This chatbot provides general medical information and should not be used as a substitute for professional medical advice. Always consult with qualified healthcare professionals for medical diagnosis, treatment, and advice.