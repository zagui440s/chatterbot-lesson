from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("My ChatBot")

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

list_trainer = ListTrainer(chatbot)
list_trainer.train([
    "Hi, how are you?",
    "I'm good, thank you!",
    "What is your name?",
    "I am a chatbot.",
    "What can you do?",
    "I can chat with you!"
])
# Function to chat with the bot
def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

chat()