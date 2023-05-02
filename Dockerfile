FROM python:3.9-alpine
WORKDIR /app
COPY /src .
CMD ["python", "main.py"]
