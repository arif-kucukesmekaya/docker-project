# Docker Uygulama Ortamı

Bu proje, Docker ve Docker Compose kullanılarak oluşturulmuş tam kapsamlı bir web uygulama ortamıdır.

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Servisler](#servisler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Servis Yönetimi](#servis-yönetimi)
- [Loglama](#loglama)
- [Cron Görevleri](#cron-görevleri)
- [Ekran Görüntüleri](#ekran-görüntüleri)

## 🎯 Proje Hakkında

Bu proje, Docker container'ları kullanarak bir web uygulaması, veritabanı ve yönetim araçlarını bir araya getiren bir ortamdır. Tüm servisler birbirleriyle haberleşir ve tek bir komutla yönetilebilir.

## 🛠 Servisler

### 1. Flask Web Uygulaması
- **Port:** 80 (Nginx üzerinden)
- **Açıklama:** Kullanıcıların isim ve mesaj girebileceği basit bir web arayüzü
- **Özellikler:**
  - Form ile mesaj gönderme
  - Tüm mesajları listeleme
  - Modern ve responsive tasarım
  - Loglama desteği

### 2. PostgreSQL Veritabanı
- **Port:** 5433 (host) → 5432 (container)
- **Not:** Host port 5433 kullanılıyor çünkü 5432 zaten kullanımda
- **Veritabanı:** mydb
- **Kullanıcı:** postgres
- **Şifre:** postgres
- **Tablo:** messages (id, name, message, created_at)

### 3. Adminer
- **Port:** 8080
- **URL:** http://localhost:8080
- **Açıklama:** Web tabanlı veritabanı yönetim arayüzü
- **Bağlantı Bilgileri:**
  - Sistem: PostgreSQL
  - Sunucu: postgres
  - Kullanıcı: postgres
  - Şifre: postgres
  - Veritabanı: mydb

### 4. Nginx
- **Port:** 80
- **Açıklama:** Reverse proxy olarak çalışır, tüm istekleri Flask uygulamasına yönlendirir

## 🚀 Kurulum

### Gereksinimler
- Docker (20.10+)
- Docker Compose (2.0+)
- Linux (systemd için)

### Adımlar

1. **Projeyi klonlayın veya indirin:**
```bash
cd /home/arif/docker-project
```

2. **Docker Compose ile servisleri başlatın:**
```bash
docker-compose up -d
```

3. **Servislerin durumunu kontrol edin:**
```bash
docker-compose ps
```

4. **Logları izleyin:**
```bash
docker-compose logs -f
```

## 💻 Kullanım

### Web Uygulaması
Tarayıcınızda şu adresi açın:
```
http://localhost
```

### Adminer (Veritabanı Yönetimi)
Tarayıcınızda şu adresi açın:
```
http://localhost:8080
```

**Bağlantı Bilgileri:**
- Sistem: PostgreSQL
- Sunucu: `postgres`
- Kullanıcı: `postgres`
- Şifre: `postgres`
- Veritabanı: `mydb`

## ⚙️ Servis Yönetimi

### Systemd ile Yönetim

1. **Servis dosyasını kopyalayın:**
```bash
sudo cp myapp.service /etc/systemd/system/
```

2. **Systemd'yi yeniden yükleyin:**
```bash
sudo systemctl daemon-reload
```

3. **Servisi etkinleştirin:**
```bash
sudo systemctl enable myapp
```

4. **Servisi başlatın:**
```bash
sudo systemctl start myapp
```

5. **Servis durumunu kontrol edin:**
```bash
sudo systemctl status myapp
```

6. **Servisi durdurun:**
```bash
sudo systemctl stop myapp
```

### Manuel Yönetim

**Servisleri başlat:**
```bash
docker-compose up -d
```

**Servisleri durdur:**
```bash
docker-compose down
```

**Servisleri yeniden başlat:**
```bash
docker-compose restart
```

**Belirli bir servisi yeniden başlat:**
```bash
docker-compose restart flask
```

## 📝 Loglama

### Flask Uygulaması Logları
Flask uygulaması logları `logs/app.log` dosyasına yazar.

**Logları izlemek için:**
```bash
tail -f logs/app.log
```

**Docker loglarını izlemek için:**
```bash
docker-compose logs -f flask
```

## ⏰ Cron Görevleri

Cron görevi, her 2 dakikada bir log dosyasını arşivler ve veritabanı yedeği alır.

### Cron Kurulumu

1. **Cron scriptini çalıştırılabilir yapın:**
```bash
chmod +x cron-job.sh
```

2. **Crontab'ı düzenleyin:**
```bash
crontab -e
```

3. **Şu satırı ekleyin:**
```bash
*/2 * * * * /home/arif/docker-project/cron-job.sh
```

Bu, her 2 dakikada bir cron-job.sh scriptini çalıştırır.

### Cron Görevi Ne Yapar?
- Log dosyasını `log_archive/` klasörüne kopyalar
- Veritabanı yedeği alır (SQL formatında)
- 30 günden eski dosyaları temizler

## 📸 Ekran Görüntüleri

Ekran görüntüleri `screenshots/` klasöründe bulunmaktadır.

### Gerekli Ekran Görüntüleri

1. **Web Uygulaması** - http://localhost
   - Ana sayfa ve form görünümü
   - Mesaj listesi görünümü

2. **Adminer** - http://localhost:8080
   - Giriş sayfası
   - Veritabanı ve messages tablosu görünümü

3. **Docker Container'ları**
   - `docker compose ps` komutunun çıktısı

Detaylı bilgi için `screenshots/README.md` dosyasına bakın.

## 🔧 Sorun Giderme

### Servisler başlamıyor
```bash
# Logları kontrol edin
docker-compose logs

# Servisleri yeniden başlatın
docker-compose down
docker-compose up -d
```

### Veritabanı bağlantı hatası
```bash
# PostgreSQL container'ının çalıştığını kontrol edin
docker-compose ps postgres

# Veritabanı loglarını kontrol edin
docker-compose logs postgres
```

### Port çakışması
Eğer 80, 8080 veya 5432 portları kullanılıyorsa, `docker-compose.yml` dosyasındaki port numaralarını değiştirin.

**Not:** PostgreSQL portu varsayılan olarak 5433'e ayarlanmıştır (5432 zaten kullanılıyorsa).

## 📊 Proje Yapısı

```
docker-project/
├── app/
│   ├── app.py              # Flask uygulaması
│   ├── templates/
│   │   └── index.html      # Web arayüzü
│   ├── requirements.txt    # Python bağımlılıkları
│   └── Dockerfile         # Flask container imajı
├── nginx/
│   └── nginx.conf         # Nginx konfigürasyonu
├── logs/                  # Log dosyaları
├── log_archive/           # Arşivlenmiş loglar
├── screenshots/          # Ekran görüntüleri
├── docker-compose.yml    # Docker Compose konfigürasyonu
├── myapp.service         # Systemd servis dosyası
├── cron-job.sh           # Cron görev scripti
└── README.md             # Bu dosya
```

## 🔐 Güvenlik Notları

- Bu proje geliştirme/öğrenme amaçlıdır
- Production ortamında şifreleri environment variable olarak kullanın
- Veritabanı şifrelerini değiştirin
- HTTPS kullanmayı düşünün

## 📝 Lisans

Bu proje eğitim amaçlıdır.

## 👤 Yazar

Docker ve Linux bilgileriyle oluşturulmuş bir uygulama ortamı projesi.

