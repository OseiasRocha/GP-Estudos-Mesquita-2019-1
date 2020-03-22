from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Ola', 'Tudo bem?', 'Tudo otimo', 'Voce gosta de programar?', 'Sim, eu programo em Python']

bot = ListTrainer(chatbot)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')

# Dummy