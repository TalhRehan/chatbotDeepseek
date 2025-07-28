This project implements a chatbot interface using Flask as the backend framework and Ollama's deepseek-r1 language model for generating responses. The application features a clean, modern UI with smooth animations for message display.

Features
Streaming Chat Interface: Real-time message exchange with animation effects
Ollama Integration: Utilizes the deepseek-r1 language model for intelligent responses
LangGraph Workflow: Implements a stateful conversation graph for message handling
Clean UI: Gradient background with responsive chat bubbles
Tag Filtering: Automatically removes <think> tags from model responses

Prerequisites
Before running the application, ensure you have the following installed:
Python 3.7+
Ollama running locally (with deepseek-r1 model downloaded)
Required Python packages (install via pip install -r requirements.txt)
Installation

Clone the repository:
git clone https://github.com/yourusername/chatbot-interface.git
cd chatbot-interface

Install the required Python packages:
pip install flask langchain-ollama langgraph
Ensure Ollama is running locally on port 11434 with the deepseek-r1 model downloaded.
Running the Application

Start the Flask development server:
python app.py
The application will be available at http://localhost:5000.

Project Structure:
├── app.py                # Flask application and chatbot logic
├── index.html            # Frontend interface
└── README.md             # This documentation file
API Endpoints
GET /: Serves the chat interface HTML page

POST /chat: Processes user messages and returns chatbot responses

Customization
You can customize the following aspects of the application:
Model: Change the Ollama model in app.py by modifying the model parameter
UI: Adjust the styling in index.html to match your preferences
Message Processing: Modify the remove_think_tags function to handle different response formatt
