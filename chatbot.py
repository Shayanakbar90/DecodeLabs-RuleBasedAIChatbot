"""Rule-Based AI Chatbot
DecodeLabs Artificial Intelligence - Project 1
"""

BOT_NAME = "Nova"

EXIT_COMMANDS = {
    "bye",
    "exit",
    "quit",
    "goodbye",
}

FALLBACK_RESPONSE = (
    "I don't understand that yet. Type 'help' to see what you can ask."
)

RESPONSES = {
    "hello": "Hello! How can I help you today?",

    "hi": "Hi there! What would you like to talk about?",

    "hey": "Hey! Nice to meet you.",

    "how are you":
        "I'm running perfectly, thanks for asking. How are you?",

    "what is your name":
        f"My name is {BOT_NAME}. I'm a rule-based chatbot.",

    "who are you":
        f"I'm {BOT_NAME}, a chatbot powered by predefined rules.",

    "what can you do":
        "I can respond to greetings, introduce myself, explain this "
        "project, answer predefined questions, and end the conversation.",

    "what is artificial intelligence":
        "Artificial intelligence is the field of building systems that "
        "perform tasks that normally require human intelligence.",

    "what is a rule based chatbot":
        "A rule-based chatbot matches a user's input with predefined "
        "rules and returns the response linked to the matching rule.",

    "tell me about this project":
        "This project demonstrates input sanitization, control flow, "
        "dictionary lookup, fallback handling, and a continuous loop.",

    "help":
        "Try: hello, how are you, what is your name, what can you do, "
        "what is artificial intelligence, what is a rule based chatbot, "
        "tell me about this project, thanks, or exit.",

    "thanks":
        "You're welcome!",

    "thank you":
        "You're welcome. I'm glad I could help.",
}


def normalize_input(raw_input):
    """Convert input to lowercase and remove unnecessary spaces."""
    return " ".join(raw_input.lower().strip().split())


def get_response(raw_input):
    """Generate a response for the given user input."""

    clean_input = normalize_input(raw_input)

    if not clean_input:
        return "Please type a message so I can respond.", False

    if clean_input in EXIT_COMMANDS:
        return "Goodbye! Thanks for chatting with me.", True

    response = RESPONSES.get(
        clean_input,
        FALLBACK_RESPONSE
    )

    return response, False


def run_chatbot():
    """Run the chatbot continuously until the user exits."""

    print("=" * 55)
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}, your rule-based AI chatbot.")
    print(f"{BOT_NAME}: Type 'help' for options or 'exit' to stop.")
    print("=" * 55)

    while True:

        user_input = input("You: ")

        response, should_exit = get_response(user_input)

        print(f"{BOT_NAME}: {response}")

        if should_exit:
            break


if __name__ == "__main__":
    run_chatbot()
