FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
WORKDIR fastapi-application

CMD ["python", "main.py"]