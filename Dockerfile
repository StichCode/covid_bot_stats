FROM python:3.8.6-slim

ENV LOGURU_LEVEL=INFO

COPY . .
RUN pip3 install --no-cache-dir -I -r requirements.txt

CMD ["python3", "main.py"]
