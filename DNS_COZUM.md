# 🔧 DNS Sorunu Çözümü

Eğer Docker build sırasında DNS hatası alıyorsanız, şu çözümleri deneyin:

## Çözüm 1: Docker Daemon DNS Ayarları (Önerilen)

```bash
# Docker daemon DNS ayarlarını düzenle
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json > /dev/null <<EOF
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
EOF

# Docker'ı yeniden başlat
sudo systemctl restart docker
```

## Çözüm 2: WSL2 DNS Ayarları

```bash
# WSL2 DNS ayarlarını düzelt
sudo bash -c 'cat > /etc/resolv.conf <<EOF
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF'

# Kalıcı yapmak için
sudo bash -c 'cat > /etc/wsl.conf <<EOF
[network]
generateResolvConf = false
EOF'
```

## Çözüm 3: Build Sırasında Host Network Kullan

`docker-compose.yml` dosyasında zaten `network: host` eklendi. Eğer hala sorun varsa:

```bash
# Manuel build
cd /home/arif/docker-project
docker build --network=host -t myapp-flask ./app
```

## Çözüm 4: Manuel Paket İndirme (Son Çare)

Eğer hiçbiri işe yaramazsa, paketleri manuel indirip kopyalayabilirsiniz:

```bash
# Yerel makinede paketleri indir
pip download -d ./packages Flask psycopg2-binary

# Dockerfile'ı güncelle (pip install yerine local packages kullan)
```

## Mevcut Durum

Projede şu ayarlar yapıldı:
- ✅ `docker-compose.yml`: `network: host` build ayarı eklendi
- ✅ `Dockerfile`: pip install için trusted-host ve index-url eklendi
- ✅ DNS ayarları container runtime için eklendi

## Test

DNS sorununu test etmek için:

```bash
# Docker build test
cd /home/arif/docker-project
docker compose build flask

# Eğer başarılı olursa
docker compose up -d
```

## Not

DNS sorunu genellikle WSL2'de görülür. Yukarıdaki çözümlerden birini uyguladıktan sonra projeyi tekrar build edin.

