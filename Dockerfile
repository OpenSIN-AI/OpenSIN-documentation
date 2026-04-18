FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git curl ca-certificates && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    curl -fL -o opencode.tar.gz "https://github.com/anomalyco/opencode/releases/download/v1.4.3/opencode-linux-x64.tar.gz"; \
    tar -xzf opencode.tar.gz -C /usr/local/bin opencode; \
    rm -f opencode.tar.gz; \
    chmod +x /usr/local/bin/opencode; \
    opencode --version

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod +x /app/start.sh
RUN mkdir -p /workspace

EXPOSE 7860
ENV HF_SPACE=true PORT=7860
ENTRYPOINT ["/app/start.sh"]

