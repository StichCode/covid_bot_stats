FROM python:3.8.6-slim

ENV TOKEN=1252959267:AAHJeV3NwVbUGou4AYdf8u8OI-qFC6mGnJ4

RUN apt-get update && apt-get install -y gcc python3-dev python3-
COPY . .
RUN pip3 install --no-cache-dir -I -r requirments.txt

CMD ["python3", "main.py"]
