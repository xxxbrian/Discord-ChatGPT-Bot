import os, discord
from src.chatbot import ChatBot
from src.dcbot import DcBot

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = DcBot(intents=intents)

    token = os.getenv('DISCORD_TOKEN')
    email = os.getenv('OPENAI_EMAIL')
    password = os.getenv('OPENAI_PASSWORD')
    if not token or not email or not password:
        raise Exception('Missing environment variables')

    client.set_chatbot(ChatBot(email, password))
    client.run(token)