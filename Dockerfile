# Stage 1: Build the application
FROM python:3.11-bullseye AS build

RUN useradd -m nonroot

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app app

# Stage 2: Create the production image
FROM python:3.11-slim-bullseye

RUN useradd -m nonroot

WORKDIR /app

COPY --from=build /app .

COPY ssl.key /app/
COPY ssl.cert /app/


ENV DB_PASSWORD=changeme
ENV API_KEY=changeme

EXPOSE 80


EXPOSE 443

USER nonroot

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/app/ssl.key", "--ssl-certfile", "/app/ssl.cert"]

