import os
import discord
from discord.ext import commands
from chatbot import ChatThread

token = os.getenv('DISCORD_TOKEN')
email = os.getenv('OPENAI_EMAIL')
password = os.getenv('OPENAI_PASSWORD')
if not token or not email or not password:
    raise Exception('Missing environment variables')

chat = ChatThread(email, password)

intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.watching,
                            name="ChatGPT is BEST!")
mybot = commands.Bot(command_prefix="!", intents=intents, activity=activity)


@mybot.event
async def on_ready():
    await mybot.tree.sync()
    print(f'{mybot.user} has connected to Discord!')


@mybot.event
async def on_message(message):
    pass


@mybot.tree.command(name="start", description="Start the chat with bot.")
async def start(interaction: discord.Interaction):
    resp = chat.chat_start(id=interaction.user.id)
    await interaction.response.send_message(resp)


@mybot.tree.command(name="end", description="End the chat with bot.")
async def end(interaction: discord.Interaction):
    resp = chat.chat_end(id=interaction.user.id)
    await interaction.response.send_message(resp)


@mybot.tree.command(name="chat", description="Ask Bot to help you.")
async def ask(interaction: discord.Interaction, *, message: str):
    await interaction.response.defer(thinking=True)
    resp_chuncks = chat.handle(id=interaction.user.id, message=message)
    for chunk in resp_chuncks:
        await interaction.followup.send(chunk)


mybot.run(token)