from pychatgpt import Chat


class ChatThread():

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.threads = {}
        # initialize the ChatGPT API
        Chat(email, password)

    def chat_start(self, id: str) -> str:
        if id in self.threads:
            return '**Conversation already started.**'
        self.threads[id] = Chat(self.email, self.password)
        return '**Conversation started.**'

    def chat_end(self, id: str) -> str:
        if id not in self.threads:
            return '**Conversation not started.**'
        self.threads.pop(id)
        return '**Conversation ended. I have forgotten everything.**'

    def handle(self, id: str, message) -> list[str]:
        if id not in self.threads:
            return [
                '**Use `/start` to start a conversation\nUse `/end` to end the conversation.\n\nI will forget everything after the conversation ends.**'
            ]
        try:
            # response, conversation_id, previous_convo_id
            response, _, _ = self.threads[id].ask(message)
            resp_chunks = self._split_message(response)
        except Exception as e:
            print(e)
            resp_chunks = ['*Wabibabu, wabibabu, wabibabu...*']
        finally:
            return resp_chunks

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
