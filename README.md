# Discord ChatGPT Bot

[![Base Docker Image CI](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/base-image.yml/badge.svg)](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/base-image.yml) [![Docker Image CI](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/docker-image.yml)

A **Discord bot** based on **ChatGPT** with support for opening multiple different conversation sessions in channels and DM, each Channel and DM having a separate contextual conversation.



#### Usage:

**Slash Commands:**

- `/start`: Start a new conversation thread, each thread is a separate conversation.
- `/chat` `[message]`: Chat the bot with `[message]`, remembers what user said earlier in the conversation.
- `/end`: End the conversation thread, the bot will forget what user said earlier in the conversation.



#### Install:

**With git clone:**

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DISCORD_TOKEN="YOUR_TOKEN"
export OPENAI_EMAIL="YOUR_EMAIL"
export OPENAI_PASSWORD="YOUR_PASSWORD"

# Run
python src/dcbot.py
```

**With docker:**

```bash
docker run -d --name=Discord-ChatGPT-Bot --restart=unless-stopped \
-e DISCORD_TOKEN="YOUR_TOKEN" \
-e OPENAI_EMAIL="YOUR_EMAIL" \
-e OPENAI_PASSWORD="YOUR_PASSWORD" \
xxxbrian/discord_chatgpt_bot:latest
```



#### Dependencies:

- [OpenAI](https://chat.openai.com/)
- [rawandahmad698/PyChatGPT](https://github.com/rawandahmad698/PyChatGPT)
- [Rapptz/discord.py](https://github.com/Rapptz/discord.py)



#### TODO:

- [x] Slash command
- [ ] Support retry
- [ ] Display mode

