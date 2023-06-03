
FROM python:3.10-bullseye

ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update \
    && apt-get install -y curl chromium  \
    build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 \
    libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info  chromium-driver \
    fonts-noto-color-emoji

RUN mkdir -p -m 775 /app && chown $USER_UID:$USER_GID /app
WORKDIR /app

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME

COPY --chown=$USER_UID:$USER_GID . .

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV PUPPETEER_EXECUTABLE_PATH /usr/bin/chromium

RUN pip install  -e .
EXPOSE 8080

RUN chmod +x /app/entrypoint.sh

CMD ["bash"]

