FROM xxxbrian/discord_chatgpt_bot:base-image
# FROM python

COPY . /root
WORKDIR /root

RUN pip install -r requirements.txt

CMD ["python", "src/dcbot.py"]
