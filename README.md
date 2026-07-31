# Rule-Based AI Chatbot

This project was developed as part of my DecodeLabs Artificial Intelligence Industrial Training.

The goal of the project is to build a simple rule-based chatbot in Python that responds to predefined user inputs using deterministic logic. The chatbot does not use machine learning or a large language model. Instead, it follows explicit rules so that each recognized input produces a predictable response.

## Project Objective

The project focuses on the foundations of conversational logic and control flow.

The chatbot can:

- Accept user input
- Normalize text using lowercase conversion and whitespace removal
- Respond to predefined greetings and questions
- Recognize exit commands
- Return a fallback response for unknown input
- Continue running until the user chooses to end the conversation

## Project Screenshot

[View Chatbot Screenshot 1](./chatbot-demo-1.png)

[View Chatbot Screenshot 2](./chatbot-demo-2.png)

## How It Works

The chatbot follows a simple input-process-output flow:

1. The user enters a message.
2. The input is cleaned using `lower()` and `strip()`.
3. The program checks whether the input is an exit command.
4. Known inputs are matched with predefined responses.
5. Unknown inputs receive a fallback response.
6. The chatbot continues running inside a `while` loop until the user exits.

## Concepts Used

- Python control flow
- Conditional logic
- `while` loops
- Dictionaries
- Dictionary `.get()` lookup
- Input normalization
- Functions
- Fallback handling
- Deterministic response logic

## Example Inputs

You can try messages such as:

- `hello`
- `hi`
- `how are you`
- `what is your name`
- `what can you do`
- `help`
- `thanks`
- `bye`
- `exit`
- `quit`

## Project Structure

```text
.
├── chatbot.py
├── chatbot-demo.png
├── README.md
└── .gitignore
```

## Run the Project

Make sure Python is installed on your computer.

Run the chatbot with:

```bash
python chatbot.py
```

If needed, use:

```bash
python3 chatbot.py
```

The chatbot will continue accepting input until you enter an exit command such as `bye`, `exit`, `quit`, or `goodbye`.

## Project Status

Completed and tested successfully.

## Author

**Shayan Akbar**

Developed as part of the DecodeLabs Artificial Intelligence Industrial Training Program.
