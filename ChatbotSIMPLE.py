def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, so I don't have feelings, but thank you for asking!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

print("Welcome to the Simple Chatbot!")
print("You can start chatting. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(simple_chatbot(user_input))
        break
    else:
        print("Bot:", simple_chatbot(user_input))
