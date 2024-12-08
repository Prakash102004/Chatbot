import re
import random

# Define the chatbot's response database
responses = {
    "greetings": [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! How's everything going?"
    ],
    "farewells": [
        "Goodbye! Have a wonderful day!",
        "See you later! Take care!",
        "Bye! Looking forward to our next chat."
    ],
    "weather": [
        "The weather is great! How about where you are?",
        "It looks sunny today! Perfect for a walk.",
        "Stay prepared! Weather can be unpredictable."
    ],
    "feeling": [
        "I'm doing great, thank you! How about you?",
        "I'm just a bot, but I'm happy to chat with you!",
        "Feeling fantastic! Let's talk more."
    ],
    "help": [
        "I'm here to assist you! What do you need?",
        "How can I help you today?",
        "Feel free to ask me anything!"
    ],
    "default": [
        "I'm not sure I understand. Could you clarify?",
        "Can you explain that in another way?",
        "I'm here to help, but I need more information."
    ]
}

# Pattern matching for intents
patterns = {
    "greetings": re.compile(r'\b(hello|hi|hey|greetings)\b', re.IGNORECASE),
    "farewells": re.compile(r'\b(bye|goodbye|see you|farewell)\b', re.IGNORECASE),
    "weather": re.compile(r'\b(weather|rain|sunny|forecast)\b', re.IGNORECASE),
    "feeling": re.compile(r'\b(how are you|how do you feel|feeling)\b', re.IGNORECASE),
    "help": re.compile(r'\b(help|assist|support)\b', re.IGNORECASE)
}

def match_intent(user_input):
    """
    Identify the user's intent based on predefined patterns.
    """
    for intent, pattern in patterns.items():
        if pattern.search(user_input):
            return intent
    return "default"

def generate_response(user_input):
    """
    Generate a response based on the user's input and matched intent.
    """
    intent = match_intent(user_input)
    return random.choice(responses[intent])

def chatbot():
    """
    Main function for the chatbot.
    """
    print("Chatbot: Hello! I'm here to chat with you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
