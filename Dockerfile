FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "bot.py"]
