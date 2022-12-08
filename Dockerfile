FROM python

COPY . /root
WORKDIR /root

RUN pip install discord.py
RUN pip install chatgptpy --upgrade

CMD ["python", "run.py"]
