FROM python:3.8.6-slim

ENV TOKEN=1252959267:AAHJeV3NwVbUGou4AYdf8u8OI-qFC6mGnJ4
ENV LOGURU_LEVEL=INFO

RUN apt-get update -y && apt-get install -y gcc python3 python3-pip python3-dev
COPY . .
RUN pip3 install --no-cache-dir -I -r requirements.txt

CMD ["python3", "main.py"]
