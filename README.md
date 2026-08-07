<div align="center">

# 🤖 Nova — Rule-Based AI Chatbot

### A deterministic conversational chatbot developed with Python and Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Completed-2EA44F)]()
[![Deployment](https://img.shields.io/badge/Deployment-Live-success)](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)

[🚀 Launch Live Application](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/) •
[💻 View Source Code](https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot)

</div>

---

## Overview

**Nova** is a rule-based conversational chatbot developed as part of the **DecodeLabs Artificial Intelligence Industrial Training Program**.

The project demonstrates how a chatbot can process user input, match it against predefined conversational rules, and return consistent responses through a structured decision-making system.

Unlike machine-learning or generative AI chatbots, Nova does not generate responses using a trained model or external API. Instead, it uses deterministic Python logic, predefined response mappings, input normalization, exit-command detection, and fallback handling.

The chatbot includes both:

- A web-based interface developed with Streamlit
- A command-line interface developed with Python

This modular structure separates the chatbot engine from the presentation layer, making the application easier to understand, test, maintain, and extend.

---

## Live Application

The deployed chatbot is available through Streamlit Community Cloud.

### [Open Nova Rule-Based AI Chatbot](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)

The live application allows users to:

- Send messages through an interactive chat interface
- View the complete conversation during the active session
- Test predefined questions and commands
- Receive controlled fallback responses
- End a conversation using exit commands
- Restart the conversation using the sidebar
- Review example questions supported by the chatbot

---

## Project Objectives

The main objectives of this project were to:

- Understand the fundamental architecture of rule-based chatbots
- Build a deterministic conversational response system
- Store predefined responses using Python dictionaries
- Normalize user input before rule matching
- Handle empty and unsupported messages safely
- Detect commands that end the conversation
- Develop a continuous command-line conversation loop
- Create a browser-based chatbot interface with Streamlit
- Separate application logic from interface logic
- Deploy the completed project as a publicly accessible web application

---

## Key Features

### Deterministic Response Engine

Nova uses predefined rules to generate responses. The same recognized input always produces the same output.

This makes the chatbot:

- Predictable
- Transparent
- Easy to test
- Easy to control
- Suitable for structured conversations

### Input Normalization

Before attempting to match a user message, the chatbot cleans the input by:

- Converting text to lowercase
- Removing leading spaces
- Removing trailing spaces
- Reducing unnecessary whitespace

For example:

```text
"   WHAT IS YOUR NAME   "
Predefined Response Mapping

Recognized messages are matched against a dictionary containing predefined input-response pairs.

A simplified example is shown below:

responses = {
    "hello": "Hello! How can I help you today?",
    "what is your name": "My name is Nova.",
    "help": "Here are some questions you can ask..."
}
Fallback Response

When the chatbot receives a message that does not match any predefined rule, it returns a controlled fallback response.

I don't understand that yet. Type 'help' to see what you can ask.

This prevents the application from crashing or returning an empty response.

Exit Command Recognition

Nova recognizes several commands for ending the conversation, including:

bye
exit
quit
goodbye
Interactive Web Interface

The Streamlit application provides:

Chat-style message display
User and assistant message separation
Persistent conversation history during the active session
Chat input field
Example questions
New conversation control
Command-Line Interface

The chatbot can also be executed directly inside a terminal without launching the Streamlit application.

Modular Architecture

The project separates:

Core chatbot logic
User-interface logic
Dependency configuration
Documentation

This separation improves maintainability and code organization.

How the Chatbot Works

Nova follows a structured input-processing-response workflow.

┌────────────────────────┐
│ User enters a message  │
└────────────┬───────────┘
             │
             ▼
┌─────────────────────────────┐
│ Normalize the user input    │
│                             │
│ • Convert to lowercase      │
│ • Remove extra whitespace   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Check whether input is empty│
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Check for an exit command   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Search predefined responses │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ Return matched response     │
│ or fallback response        │
└─────────────────────────────┘

The central response logic can be represented as:

clean_input = normalize_input(user_input)

if clean_input in EXIT_COMMANDS:
    return exit_response, True

response = RESPONSES.get(clean_input, FALLBACK_RESPONSE)

return response, False
System Architecture

The project uses a simple modular architecture.

┌─────────────────────────────────┐
│       Streamlit Web Interface   │
│              app.py             │
│                                 │
│ • Chat input                    │
│ • Message rendering             │
│ • Session history               │
│ • Example prompts               │
│ • Conversation reset            │
└────────────────┬────────────────┘
                 │
                 │ Calls chatbot engine
                 ▼
┌─────────────────────────────────┐
│       Chatbot Response Engine   │
│           chatbot.py            │
│                                 │
│ • Input normalization           │
│ • Rule matching                 │
│ • Exit-command detection        │
│ • Fallback handling             │
│ • Command-line interaction      │
└─────────────────────────────────┘
Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Interactive web application
Python dictionaries	Storage of chatbot rules and responses
Session State	Temporary conversation-history management
Git	Version control
GitHub	Source-code hosting
Streamlit Community Cloud	Live web deployment
Project Structure
DecodeLabs-RuleBasedAIChatbot/
│
├── app.py
│   └── Streamlit web interface
│
├── chatbot.py
│   └── Core chatbot engine and command-line application
│
├── requirements.txt
│   └── Python dependency list
│
├── chatbot-demo.png
│   └── Project demonstration image
│
├── chatbot-demo-2.png
│   └── Additional demonstration image
│
├── README.md
│   └── Complete project documentation
│
└── .gitignore
    └── Files excluded from version control
Application Preview
Streamlit Chat Interface

Additional Project Demonstration

For a stronger portfolio presentation, replace these images with updated screenshots of the deployed Streamlit interface.

Supported Inputs

Nova currently recognizes predefined messages such as:

User Input	Chatbot Behaviour
hello	Returns a greeting
hi	Starts a friendly conversation
hey	Responds with an informal greeting
how are you	Returns a conversational response
what is your name	Introduces the chatbot
who are you	Explains Nova's identity
what can you do	Describes the chatbot's capabilities
what is artificial intelligence	Provides a basic explanation of AI
what is a rule based chatbot	Explains rule-based chatbot systems
tell me about this project	Describes the project
help	Displays available questions
thanks	Returns an acknowledgement
bye	Ends the conversation
exit	Ends the conversation
quit	Ends the conversation

Messages outside the predefined rule set receive the fallback response:

I don't understand that yet. Type 'help' to see what you can ask.
Example Conversation
Nova: Hello! I'm Nova, your rule-based AI chatbot.
Nova: Type 'help' for available questions or 'exit' to stop.

You: hello

Nova: Hello! How can I help you today?

You: what is your name

Nova: My name is Nova. I'm a rule-based chatbot.

You: what can you do

Nova: I can respond to greetings, introduce myself, explain this
project, answer predefined questions, and end the conversation.

You: explain something unknown

Nova: I don't understand that yet. Type 'help' to see what you can ask.

You: exit

Nova: Goodbye! Thanks for chatting with me.
Installation and Local Setup
Prerequisites

Before running the application locally, ensure that the following software is installed:

Python 3.10 or later
pip
Git
1. Clone the Repository
git clone https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot.git
2. Open the Project Directory
cd DecodeLabs-RuleBasedAIChatbot
3. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
macOS or Linux
python3 -m venv venv
source venv/bin/activate
4. Install the Required Dependencies
pip install -r requirements.txt
Running the Application
Run the Streamlit Web Application
streamlit run app.py

Streamlit will normally display a local URL similar to:

http://localhost:8501

Open that URL in your browser.

Run the Command-Line Application
python chatbot.py

On some systems, use:

python3 chatbot.py

The chatbot will continue accepting messages until the user enters an exit command.

Core Concepts Demonstrated

This project demonstrates the practical application of:

Rule-based artificial intelligence
Deterministic decision-making
Input normalization
Input validation
Dictionary-based response mapping
Conditional statements
Python functions
Continuous loops
Fallback handling
Exit-command processing
Modular application structure
Session-state management
Conversational interface development
Cloud application deployment
Rule-Based Chatbot vs Generative Chatbot
Rule-Based Chatbot	Generative Chatbot
Uses predefined rules	Uses trained language models
Produces predictable responses	Produces context-dependent responses
Does not require model training	Usually requires a model or external API
Easy to inspect and control	More difficult to interpret
Suitable for structured tasks	Suitable for open-ended conversations
Cannot answer outside its rule set	Can respond to a wider range of questions
Low computational requirements	Higher computational requirements
Simple to test	More complex to test

Nova is intentionally rule-based because the objective of the project is to demonstrate foundational chatbot logic rather than machine-learning model development.

Testing Checklist

The application can be tested using the following cases:

 Recognized greeting returns the correct response
 Uppercase input is converted to lowercase
 Extra spaces are removed
 Empty input is handled safely
 Unknown input returns a fallback response
 Exit commands end the conversation
 Streamlit displays user messages
 Streamlit displays chatbot responses
 Conversation history remains visible during the session
 New-chat control resets the conversation
 Command-line application runs independently
 Application is deployed successfully
Current Limitations

The current version has several intentional limitations:

It only recognizes predefined inputs
It cannot understand semantic meaning
It cannot reliably recognize paraphrased questions
It does not learn from previous conversations
It does not use machine learning
It does not use a large language model
It does not use an external AI API
It does not permanently store conversation history
It supports text-based interaction only
It cannot generate original responses

These limitations are consistent with the educational purpose of a rule-based chatbot.

Future Improvements

Possible future enhancements include:

Keyword-based intent detection
Multiple acceptable phrases for each intent
Fuzzy string matching
Typing-error recognition
Regular-expression-based rules
Expanded conversational categories
Persistent conversation storage
Database integration
User authentication
Administrative response management
Voice-input support
Text-to-speech output
Sentiment-aware responses
Natural language processing integration
Machine-learning-based intent classification
Automated unit testing
Analytics for chatbot usage
Multilingual support
Learning Outcomes

Through this project, the following skills were developed:

Designing a structured conversational system
Organizing predefined rules and responses
Processing and validating user input
Developing reusable Python functions
Separating business logic from interface logic
Managing user interaction through Streamlit
Maintaining session-based conversation history
Deploying a Python web application
Writing professional technical documentation
Managing source code with Git and GitHub
Project Status

Completed and deployed successfully.

The project includes:

A functional Python chatbot engine
A command-line interface
A Streamlit web interface
Session-based chat history
Controlled fallback handling
Live cloud deployment
Complete project documentation
Author
Shayan Akbar

Developed as part of the DecodeLabs Artificial Intelligence Industrial Training Program.

GitHub Profile: Shayanakbar90
Project Repository: DecodeLabs-RuleBasedAIChatbot
Live Application: Nova Rule-Based AI Chatbot
Acknowledgement

This project was completed as part of the DecodeLabs Artificial Intelligence training program to strengthen practical understanding of Python programming, rule-based systems, conversational application design, web-interface development, and cloud deployment.

<div align="center">
⭐ Support the Project

If you found this project useful, consider giving the repository a star.

Built with Python, Streamlit, and deterministic conversational logic.

</div> ```
Author
Shayan Akbar

Developed as part of the DecodeLabs Artificial Intelligence Industrial Training Program.

GitHub Profile: Shayanakbar90
Project Repository: DecodeLabs-RuleBasedAIChatbot
Live Application: Nova Rule-Based AI Chatbot
Acknowledgement

This project was completed as part of the DecodeLabs Artificial Intelligence training program to strengthen practical understanding of Python programming, rule-based systems, conversational application design, web-interface development, and cloud deployment.

<div align="center">
