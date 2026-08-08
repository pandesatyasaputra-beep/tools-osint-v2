# 🔍 OSINT TOOL

Open Source Intelligence (OSINT) Tool yang berjalan di **Kali Linux** dan **Termux (Android)**.

## ✨ Fitur

| No | Modul | Deskripsi |
|----|-------|-----------|
| 1 | 📱 Phone Lookup | Informasi nomor telepon (negara, operator, timezone) |
| 2 | 🌐 IP Lookup | Geolokasi & informasi alamat IP |
| 3 | 🌍 Domain/Whois | Informasi domain (registrar, tanggal, name server) |
| 4 | 👤 Username Search | Cari username di 30+ platform media sosial |
| 5 | 📧 Email Recon | Validasi email & cek domain |
| 6 | 🔎 DNS Enumeration | Enumerasi subdomain dari suatu domain |
| 7 | 🚪 Port Scanner | Scan port umum pada target |

## 📥 Instalasi

### Kali Linux
```bash
git clone <repo-url>
cd osint-tool
chmod +x install.sh
./install.sh
```

Atau instal manual:
```bash
sudo apt update && sudo apt install python3 python3-pip
pip install requests phonenumbers colorama whois termcolor
```

### Termux (Android)
```bash
pkg update && pkg install python git
git clone <repo-url>
cd osint-tool
chmod +x install.sh
./install.sh
```

## 🚀 Cara Menjalankan

```bash
python osint_tool.py
```

## 📖 Panduan Penggunaan

1. Setelah menjalankan, akan muncul menu utama dengan 7 modul
2. Pilih nomor modul yang diinginkan [1-7]
3. Ikuti petunjuk input yang diberikan
4. Tekan Enter untuk kembali ke menu

### Contoh Penggunaan

**Phone Lookup:**
```
Masukkan nomor dengan kode negara: +628123456789
```

**IP Lookup:**
```
Masukkan IP: 8.8.8.8
Atau ketik 'me' untuk melihat IP sendiri
```

**Username Search:**
```
Masukkan username: john_doe
```

## ⚖️ Disclaimer

> ⚠️ **PENTING**: Tool ini dibuat untuk tujuan **edukasi** dan **pengujian yang sah** saja.
> - Gunakan hanya untuk target yang Anda miliki atau memiliki izin resmi
> - Dilarang menggunakan untuk aktivitas ilegal
> - Penggunaan yang salah menjadi tanggung jawab pengguna sepenuhnya

## 🛠️ Dependencies

- Python 3.x
- requests
- phonenumbers
- colorama
- whois
- termcolor

## 📝 Catatan

- Beberapa modul (seperti email breach check) membutuhkan API key dari layanan pihak ketiga
- Username search membutuhkan koneksi internet
- DNS Enumeration dan port scanner membutuhkan hak akses yang sesuai
- Pastikan koneksi internet stabil untuk hasil terbaik

## 📄 Lisensi

Tool ini untuk penggunaan edukasi. Gunakan dengan bijak dan bertanggung jawab.

---

## ☁️ Cara Upload ke GitHub

### Metode 1: Upload Manual (Tanpa Git)

Cara paling mudah, tanpa perlu install `git`:

1. Buka **[github.com](https://github.com)** dan login
2. Klik tombol **"+"** di pojok kanan atas → **"New repository"**
3. Beri nama repository, misal: `osint-tool`
4. Klik **"Create repository"**
5. Klik link **"uploading an existing file"**
6. **Drag & drop** file berikut ke halaman tersebut:
   - `osint_tool.py`
   - `install.sh`
   - `upload_github.sh`
   - `README.md`
   - `.gitignore`
7. Klik **"Commit changes"**

### Metode 2: Menggunakan Script Upload

**Windows** (`.bat`):
```bash
upload_github.bat
```

**Kali Linux / Termux** (`.sh`):
```bash
chmod +x upload_github.sh
./upload_github.sh
```

**Langkah-langkah yang dilakukan script:**
1. Check apakah `git` sudah terinstall
2. Inisialisasi repository (`git init`)
3. Add semua file (`git add .`)
4. Commit dengan pesan (`git commit`)
5. Tambahkan remote URL GitHub
6. Push ke GitHub (`git push`)

### Metode 3: Git Manual

```bash
# 1. Install git (jika belum)
# Kali:   sudo apt install git
# Termux: pkg install git

# 2. Inisialisasi
git init

# 3. Tambahkan file
git add .

# 4. Commit
git commit -m "Initial commit of OSINT Tool"

# 5. Buat repo di GitHub (https://github.com/new)
git remote add origin https://github.com/USERNAME/osint-tool.git

# 6. Push
git branch -M main
git push -u origin main
```

> 💡 **Catatan**: GitHub sekarang memerlukan **Personal Access Token** (bukan password) untuk push via CLI. Buat token di: `https://github.com/settings/tokens`
