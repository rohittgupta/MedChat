
from flask import Flask, render_template, jsonify, request, session
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-here"  # Required for sessions

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

chatModel = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

# Updated prompt with chat history
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Store chat history (simple in-memory - resets on restart)
chat_history = []

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    global chat_history
    msg = request.form["msg"]
    print(msg)
    
    # Include chat history in the request
    response = rag_chain.invoke({
        "input": msg,
        "chat_history": chat_history
    })
    
    # Save to history
    chat_history.append(HumanMessage(content=msg))
    chat_history.append(AIMessage(content=response["answer"]))
    
    # Keep only last 10 exchanges to avoid token limits
    if len(chat_history) > 20:
        chat_history = chat_history[-20:]
    
    print("Response:", response["answer"])
    return str(response["answer"])

@app.route("/clear", methods=["POST"])
def clear_chat():
    global chat_history
    chat_history = []
    return "Chat cleared"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)