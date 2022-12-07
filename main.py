import os
import discord
from pychatgpt import Chat


class ChatBot():

    def __init__(self, email, password, proxies: str or dict = None):
        self.email = email
        self.password = password
        self.proxies = proxies
        self.threads = {}
        self.dcbot_id = None

    def set_dcbot_id(self, id):
        self.dcbot_id = id

    @staticmethod
    def _split_message(message, size=1800) -> list:
        # split message into chunks of size, ensure each chunk ends with a full sentence
        chunks = []
        end_of_sentence = ['.', '!', '?', '\n']
        while len(message) > size:
            chunk = message[:size]
            if chunk[-1] not in end_of_sentence and len(chunk) == size:
                for c in end_of_sentence:
                    shift = chunk.rfind(c)
                    if shift != -1:
                        break

                shift = chunk.rfind(' ') if shift == -1 else shift
                if shift != -1:
                    chunk = chunk[:shift + 1]
            chunks.append(chunk)
            message = message[len(chunk):]
        chunks.append(message)
        return chunks

    async def handle_dm(self, message):
        if message.author not in self.threads:
            if message.content != '!start':
                await message.channel.send(
                    '**Send `!start` to start a conversation\nSend `!end` to end the conversation.\n\nI will forget everything after the conversation ends.**'
                )
                return
            self.threads[message.author] = Chat(self.email,
                                                self.password,
                                                proxies=self.proxies)
            await message.channel.send('**Conversation started.**')
            return
        if message.content == '!end':
            self.threads.pop(message.author)
            await message.channel.send(
                '**Conversation ended. I have forgotten everything.**')
            return
        try:
            response = self.threads[message.author].ask(message.content)
            responses = self._split_message(response)
        except Exception as e:
            print(e)
            responses = ['**Something went wrong. Try again later.**']
        finally:
            for response in responses:
                await message.channel.send(response, reference=message)

    async def handle_channel(self, message):
        atmessage = f"<@{self.dcbot_id}>"
        if message.channel.id not in self.threads:
            if message.content.strip(atmessage).strip() != '!start':
                await message.channel.send(
                    '**@Me and send `!start` to start a conversation\n@Me and send `!end` to end the conversation.\n\nI will forget everything after the conversation ends.**',
                    reference=message)
                return
            self.threads[message.channel.id] = Chat(self.email,
                                                    self.password,
                                                    proxies=self.proxies)
            await message.channel.send('**Conversation started.**',
                                       reference=message)
            return
        if message.content.strip(atmessage).strip() == '!end':
            self.threads.pop(message.channel.id)
            await message.channel.send(
                '**Conversation ended. I have forgotten everything.**',
                reference=message)
            return
        try:
            response = self.threads[message.channel.id].ask(message.content)
            responses = self._split_message(response)
        except Exception as e:
            print(e)
            responses = ['Something went wrong. Try again later.']
        finally:
            for response in responses:
                await message.channel.send(response, reference=message)


class MyClient(discord.Client):

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


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    token = os.getenv('DISCORD_TOKEN')
    email = os.getenv('OPENAI_EMAIL')
    password = os.getenv('OPENAI_PASSWORD')
    if not token or not email or not password:
        raise Exception('Missing environment variables')

    client.set_chatbot(ChatBot(email, password))
    client.run(token)
