import discord


class DcBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chatbot = None

    def set_chatbot(self, chatbot):
        self.chatbot = chatbot

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.chatbot.set_dcbot_id(self.user.id)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if isinstance(message.channel, discord.DMChannel):
            # handle DM
            await self.chatbot.handle_dm(message)
        elif isinstance(message.channel, discord.TextChannel) and (
            (self.user.mention in message.content) or
            (message.reference
             and message.reference.resolved.author == self.user)):
            # handle Channel
            await self.chatbot.handle_channel(message)
        else:
            pass