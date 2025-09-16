From python:3.11.9-alpine

WORKDIR /app

RUN apk add --no-cache build-base libffi-dev

COPY ./App/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "/app/main.py"]
