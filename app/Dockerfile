FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf.backup && \
    echo "nameserver 8.8.4.4" >> /etc/resolv.conf.backup || true

RUN pip install --no-cache-dir --timeout=100 \
    --index-url https://pypi.org/simple \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

COPY . .

RUN mkdir -p logs

EXPOSE 5000

CMD ["python", "app.py"]

