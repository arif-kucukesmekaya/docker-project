FROM python:3.11-slim

WORKDIR /app

# Python bağımlılıkları
COPY requirements.txt .
# Pip install (DNS sorunları için retry mekanizması)
RUN pip install --no-cache-dir --timeout=100 -r requirements.txt

# Uygulama dosyaları
COPY . .

# Log klasörü oluştur
RUN mkdir -p logs

# Port
EXPOSE 5000

# Uygulamayı çalıştır
CMD ["python", "app.py"]

