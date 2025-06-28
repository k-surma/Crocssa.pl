# ────── Python + Flask + Socket.IO (dev) ──────
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1. zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. kod źródłowy
COPY . .

EXPOSE 5000
# 3. tryb deweloperski – hot-reload
CMD ["flask", "--app", "run", "run", "--host", "0.0.0.0", "--reload"]
