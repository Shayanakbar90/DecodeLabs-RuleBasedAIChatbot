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
```

is normalized to:

```text
"what is your name"
```

---

## 💬 Example Conversation

```text
User: hello
Nova: Hello! How can I help you today?

User: what is your name
Nova: My name is Nova. I am a rule-based chatbot.

User: something unknown
Nova: I don't understand that yet. Type 'help' to see what you can ask.

User: exit
Nova: Goodbye! Thanks for chatting with me.
```

---

## ⚠️ Limitations

![Rule Based](https://img.shields.io/badge/System-Rule--Based-orange)
![Context](https://img.shields.io/badge/Context-Limited-lightgrey)

- Responds only to predefined inputs
- Does not understand broader conversation context
- Does not learn from previous interactions
- Does not use machine learning or a large language model
- Does not permanently store conversation history
- May not recognize differently worded questions

---

## 🚀 Future Improvements

- Add keyword-based intent recognition
- Support multiple phrases for each response
- Add fuzzy matching for spelling mistakes
- Expand the predefined response library
- Store conversation history in a database
- Add automated tests
- Introduce multilingual support

---

## ✅ Project Status

[![Status](https://img.shields.io/badge/Status-Completed-2ea44f)](https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot)
[![Deployment](https://img.shields.io/badge/Deployment-Live-2ea44f)](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)
[![Platform](https://img.shields.io/badge/Platform-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

The application is complete and publicly available through Streamlit Community Cloud.

### [Launch the Live Application](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)

---

## 👨‍💻 Author

### **Shayan Akbar**

**Artificial Intelligence Intern | DecodeLabs**

[![GitHub Profile](https://img.shields.io/badge/GitHub-Shayanakbar90-181717?logo=github&logoColor=white)](https://github.com/Shayanakbar90)
[![Project Repository](https://img.shields.io/badge/Repository-View_Source-0969DA?logo=github&logoColor=white)](https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot)
[![Live Application](https://img.shields.io/badge/Live_App-Open-FF4B4B?logo=streamlit&logoColor=white)](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)

This project was developed as part of the **DecodeLabs Artificial Intelligence Training Program** to demonstrate the design and deployment of a rule-based conversational application using Python and Streamlit.

---

<div align="center">

### Built with Python and Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

**⭐ Star the repository if you found the project useful.**

</div>
