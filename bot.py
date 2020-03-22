from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('TW Chat Bot')
conversa = ['Oi', 'Ola', 'Tudo bem?', 'Tudo otimo', 'Voce gosta de programar?', 'Sim, eu programo em Python']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')

# Dummy