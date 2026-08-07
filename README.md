<div align="center">

# 🤖 Nova — Rule-Based AI Chatbot

### A deterministic conversational chatbot built with Python and Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Project Status](https://img.shields.io/badge/Status-Completed-2EA44F)]()
[![DecodeLabs](https://img.shields.io/badge/DecodeLabs-AI%20Internship-6C63FF)]()

[🚀 Launch Live Chatbot](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/) •
[💻 View Source Code](https://github.com/Shayanakbar90/DecodeLabs-RuleBasedAIChatbot)

</div>

---

## Overview

**Nova** is a rule-based conversational chatbot developed as part of the **DecodeLabs Artificial Intelligence Industrial Training Program**.

The project demonstrates how conversational behaviour can be created through explicit rules, deterministic response mapping, input normalization, fallback handling, and continuous interaction.

Unlike machine-learning or large-language-model chatbots, Nova does not generate answers probabilistically. It compares normalized user input against a predefined knowledge base and returns the response associated with the matching rule.

A Streamlit interface provides an accessible web-based chat experience, while the core chatbot can also be executed directly from the command line.

---

## Live Application

The deployed application can be accessed here:

### [Open Nova Rule-Based AI Chatbot](https://decodelabs-rulebasedaichatbot-bpelv2npnxfmvtqegtv6ui.streamlit.app/)

The web interface allows users to:

- Enter messages through an interactive chat box
- View the complete conversation history
- Test predefined questions
- Receive fallback responses for unsupported input
- End or restart a conversation
- Explore example prompts from the sidebar

---

## Project Objectives

The primary objectives of this project were to:

- Understand the fundamentals of rule-based conversational systems
- Apply Python control flow to user–system interaction
- Organize predefined responses using dictionaries
- Normalize user input before rule matching
- Handle unsupported or empty messages safely
- Maintain a continuous conversation loop
- Separate the chatbot logic from the user interface
- Deploy the completed application as an accessible web app

---

## Key Features

### Deterministic Response Engine

Each recognized user message maps to a predefined response. The same input therefore produces the same output consistently.

### Input Normalization

User input is converted to lowercase, trimmed, and cleaned of unnecessary whitespace before matching.

For example:

```text
"   WHAT IS YOUR NAME   "
