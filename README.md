# Discord ChatGPT Bot

[![Base Docker Image CI](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/base-image.yml/badge.svg)](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/base-image.yml) [![Docker Image CI](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/xxxbrian/Discord-ChatGPT-Bot/actions/workflows/docker-image.yml)

A **Discord bot** based on **ChatGPT** with support for opening multiple different conversation sessions in channels and DM, each Channel and DM having a separate contextual conversation.

#### Usage:

**In channel:**

`@bot !start` Start a conversation

`@bot [message]`Ask a question

`@bot !end`Ending the conversation

**In DM:**

`!start` Start a conversation

`[message]`Ask a question

`!end`Ending the conversation

#### Install:

**With git clone:**

```bash
# Install dependencies
pip install discord.py
pip install chatgptpy --upgrade

# Set environment variables
export DISCORD_TOKEN="YOUR_TOKEN"
export OPENAI_EMAIL="YOUR_EMAIL"
export OPENAI_PASSWORD="YOUR_PASSWORD"

# Run
python run.py
```

**With docker:**

```bash
docker run -d --name=Discoed-ChatGPT-Bot --restart=unless-stopped \
-e DISCORD_TOKEN="YOUR_TOKEN" \
-e OPENAI_EMAIL="YOUR_EMAIL" \
-e OPENAI_PASSWORD="YOUR_PASSWORD" \
xxxbrian/discord_chatgpt_bot:latest
```