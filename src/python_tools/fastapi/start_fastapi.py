import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="/path/to/ssl.key",
        ssl_certfile="/path/to/ssl.cert",
    )
