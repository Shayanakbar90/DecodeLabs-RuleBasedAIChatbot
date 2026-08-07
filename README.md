<div align="center">

Nova — Rule-Based AI Chatbot

A simple rule-based chatbot built with Python and Streamlit.

Live Demo ·Source Code

</div>

About the Project

Nova is a rule-based chatbot developed as part of the DecodeLabs Artificial Intelligence training program. It responds to predefined user inputs through a structured set of rules.

The project demonstrates basic chatbot development concepts, including input normalization, response matching, fallback handling, session-based chat history, and web deployment with Streamlit.

Unlike generative AI systems, Nova does not create new responses or use a trained language model. It returns predefined responses based on recognized user messages.

Features

Predefined rule-based responses

Input normalization

Fallback response for unsupported messages

Exit-command handling

Streamlit chat interface

Session-based conversation history

Command-line version

Live deployment

Technologies Used

Technology

Purpose

Python

Core chatbot logic

Streamlit

Web interface

GitHub

Source-code hosting

Streamlit Community Cloud

Application deployment

Project Structure

DecodeLabs-RuleBasedAIChatbot/
├── app.py
├── chatbot.py
├── requirements.txt
├── chatbot-demo.png
├── chatbot-demo-2.png
├── README.md
└── .gitignore

How It Works

The user enters a message.

The chatbot converts the input to lowercase and removes extra spaces.

It checks whether the message is an exit command.

It searches for the message in the predefined response dictionary.

It returns the matching response or a fallback message.

A simplified version of the response logic is:

clean_input = normalize_input(user_input)

if clean_input in EXIT_COMMANDS:
    return exit_response, True

return RESPONSES.get(clean_input, FALLBACK_RESPONSE), False

Supported Inputs

The chatbot can respond to messages such as:

hello

hi

how are you

what is your name

what can you do

what is artificial intelligence

what is a rule based chatbot

tell me about this project

help

thanks

bye

exit

Messages outside the predefined rule set receive a fallback response.

Live Application

Open the deployed application:

Launch Nova Rule-Based AI Chatbot

Installation

1. Clone the repository

git clone https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot.git
cd DecodeLabs-RuleBasedAIChatbot

2. Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate

macOS or Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

Run the Project

Streamlit web application

streamlit run app.py

Command-line application

python chatbot.py

Example Conversation

User: hello
Nova: Hello! How can I help you today?

User: what is your name
Nova: My name is Nova. I am a rule-based chatbot.

User: something unknown
Nova: I don't understand that yet. Type 'help' to see what you can ask.

User: exit
Nova: Goodbye! Thanks for chatting with me.

Limitations

Responds only to predefined inputs

Does not understand context or semantic meaning

Does not learn from conversations

Does not use machine learning or an external AI API

Does not permanently store chat history

Possible Improvements

Add keyword-based intent matching

Support multiple phrases for the same intent

Add fuzzy matching for spelling mistakes

Expand the response set

Add persistent conversation storage

Add automated tests

Author

Shayan Akbar

Developed as part of the DecodeLabs Artificial Intelligence training program.

GitHub: Shayanakbar90

Repository: DecodeLabs-RuleBasedAIChatbot

Live App: Nova Chatbot
