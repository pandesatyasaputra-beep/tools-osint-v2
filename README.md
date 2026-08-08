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
git clone https://github.com/pandesatyasaputra-beep/tools-osint-v2.git
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
git clone https://github.com/pandesatyasaputra-beep/tools-osint-v2.git
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
push vi
