FROM python:3.11-slim

WORKDIR /app

# Python bağımlılıkları
COPY requirements.txt .

# DNS sorununu çözmek için pip install öncesi DNS ayarları
# Build sırasında host network kullanılıyorsa bu gerekli değil ama yine de ekliyoruz
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf.backup && \
    echo "nameserver 8.8.4.4" >> /etc/resolv.conf.backup || true

# Pip install (DNS sorunları için retry mekanizması ve index-url)
RUN pip install --no-cache-dir --timeout=100 \
    --index-url https://pypi.org/simple \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

# Uygulama dosyaları
COPY . .

# Log klasörü oluştur
RUN mkdir -p logs

# Port
EXPOSE 5000

# Uygulamayı çalıştır
CMD ["python", "app.py"]

