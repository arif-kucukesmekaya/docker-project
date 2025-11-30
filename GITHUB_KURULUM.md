# 🚀 GitHub'a Yükleme Rehberi

Bu dosya projenizi GitHub'a yüklemek için adım adım talimatları içerir.

## 📋 Gereksinimler

- GitHub hesabı
- Git kurulu (zaten kurulu)
- Terminal erişimi

## 🔧 Adım Adım Kurulum

### 1. GitHub'da Yeni Repository Oluştur

1. https://github.com adresine git
2. Sağ üstteki **"+"** butonuna tıkla
3. **"New repository"** seç
4. Repository adını gir (örn: `docker-project` veya `docker-uygulama-ortami`)
5. **Public** veya **Private** seç (ödev için genelde Public)
6. **"Initialize this repository with a README"** seçeneğini işaretleme (zaten README.md var)
7. **"Create repository"** butonuna tıkla

### 2. GitHub Repository URL'ini Al

Repository oluşturulduktan sonra şu şekilde bir URL göreceksin:
```
https://github.com/KULLANICI_ADI/REPOSITORY_ADI.git
```

Örnek:
```
https://github.com/arif/docker-project.git
```

### 3. Projeyi GitHub'a Yükle

Terminal'de şu komutları çalıştır:

```bash
cd /home/arif/docker-project

# GitHub repository URL'ini ekle (YUKARIDAKI URL'İ KULLAN)
git remote add origin https://github.com/KULLANICI_ADI/REPOSITORY_ADI.git

# Dosyaları GitHub'a yükle
git branch -M main
git push -u origin main
```

**ÖNEMLİ:** Yukarıdaki URL'yi kendi GitHub repository URL'inizle değiştirin!

### 4. GitHub Kullanıcı Adı ve Şifre

Eğer iki faktörlü kimlik doğrulama (2FA) kullanıyorsanız:
- Şifre yerine **Personal Access Token** kullanmanız gerekir
- Token oluşturmak için: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

## ✅ Kontrol

Yükleme başarılı olduktan sonra:
1. GitHub repository sayfanıza gidin
2. Tüm dosyaların yüklendiğini kontrol edin:
   - ✅ docker-compose.yml
   - ✅ app/ klasörü
   - ✅ myapp.service
   - ✅ README.md
   - ✅ screenshots/ klasörü
   - ✅ cron-job.sh

## 📤 Proje URL'si

Proje URL'si şu formatta olacak:
```
https://github.com/KULLANICI_ADI/REPOSITORY_ADI
```

Bu URL'yi ödev olarak gönderebilirsiniz!

## 🔄 Sonraki Güncellemeler

Eğer projede değişiklik yaparsanız:

```bash
cd /home/arif/docker-project
git add .
git commit -m "Değişiklik açıklaması"
git push
```

## ⚠️ Sorun Giderme

### "remote origin already exists" hatası
```bash
git remote remove origin
git remote add origin https://github.com/KULLANICI_ADI/REPOSITORY_ADI.git
```

### "Authentication failed" hatası
- GitHub kullanıcı adı ve şifrenizi kontrol edin
- 2FA kullanıyorsanız Personal Access Token kullanın

### "Permission denied" hatası
- Repository'nin size ait olduğundan emin olun
- URL'yi kontrol edin

