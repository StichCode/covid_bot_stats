FROM python:3.9.1-slim

ENV LOGURU_LEVEL=INFO

COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -I -r requirements.txt

COPY . .
CMD ["python3", "main.py"]
