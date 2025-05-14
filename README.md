
# 😊 Aplikasi sederhana Deteksi Senyum

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.7.0-green.svg)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.23.5-yellow.svg)](https://numpy.org/)

Aplikasi deteksi senyum secara real-time menggunakan computer vision dengan OpenCV dan Haar Cascades.



## 📋 Deskripsi

Aplikasi ini menggunakan webcam Anda untuk mendeteksi wajah dan senyum secara real-time. Aplikasi akan secara otomatis mengunduh classifier Haar Cascade yang diperlukan jika belum ada di komputer Anda. Ketika senyum terdeteksi, senyum akan ditandai dengan kotak merah dan dilabeli "Smile Detected!".

Fitur:
- Deteksi wajah dan senyum secara real-time
- Penghitung FPS untuk memantau performa
- Opsi untuk menyimpan tangkapan layar
- Mengaktifkan/menonaktifkan deteksi wajah dan senyum

## 👨‍💻 Tim Pengembang

Projek ini dikembangkan sebagai bagian dari mata kuliah Computer Vision oleh:

| Nama                           | NIM           |
|--------------------------------|---------------|
| BILLY JUAN VALENTINO AMBARURA  |220211060063   | 
| TRI GIANTO SALENDAH            |220211060029   |
| NATALIO MICHAEL TUMUAHI        |220211060042   | 

Dosen Pengampu: Muhammad D. Putro, S.T, M.Eng


## 🔧 Persyaratan

```
numpy==1.23.5
opencv-python==4.7.0.72
matplotlib==3.7.1
```

## 🚀 Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/natalio123/deteksi_smile_haarcascade.git
   cd deteksi_smile_haarcascade
   ```

2. Buat dan aktifkan virtual environment (opsional tapi direkomendasikan):
   ```bash
   python -m venv venv
   
   # Pada Windows
   venv\Scripts\activate
   
   # Pada macOS/Linux
   source venv/bin/activate
   ```

3. Instal semua persyaratan:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Penggunaan

Jalankan aplikasi:
```bash
python main.py
```

### Kontrol Keyboard:
- `q` - Keluar dari aplikasi
- `s` - Simpan frame saat ini sebagai gambar
- `f` - Aktifkan/nonaktifkan deteksi wajah (peringatan: menonaktifkan deteksi wajah juga akan menonaktifkan deteksi senyum)
- `m` - Aktifkan/nonaktifkan deteksi senyum

## 🔍 Cara Kerja

1. Aplikasi menggunakan classifier Haar Cascade untuk deteksi wajah dan senyum
2. Pertama, wajah dideteksi dalam setiap frame
3. Untuk setiap wajah yang terdeteksi, Region of Interest (ROI) didefinisikan
4. Dalam setiap ROI wajah, detektor senyum mencari pola senyum
5. Ketika senyum terdeteksi, senyum ditandai dengan kotak merah

## 🧠 Detail Teknis

Aplikasi ini menggunakan:
- OpenCV untuk computer vision dan akses webcam
- NumPy untuk operasi numerik
- Classifier Haar Cascade untuk deteksi objek
- Matplotlib (tersedia tetapi tidak digunakan secara aktif dalam skrip utama)

### File Haar Cascade:
- `haarcascade_frontalface_default.xml` - Untuk deteksi wajah
- `haarcascade_smile.xml` - Untuk deteksi senyum

File-file ini secara otomatis diunduh pada saat pertama kali aplikasi dijalankan jika belum ada.

## ⚠️ Pemecahan Masalah

Jika Anda mengalami masalah:

1. **Akses webcam gagal**: 
   - Pastikan webcam Anda terhubung dan tidak digunakan oleh aplikasi lain
   - Coba ubah indeks kamera di kode (`cv2.VideoCapture(0)`)

2. **Unduhan file cascade gagal**:
   - Periksa koneksi internet Anda
   - Unduh file secara manual dari repositori GitHub OpenCV dan letakkan di direktori `haarcascades`

3. **Masalah kualitas deteksi**:
   - Sesuaikan kondisi pencahayaan
   - Modifikasi parameter `scaleFactor`, `minNeighbors`, dan `minSize` dalam fungsi deteksi

## 🤝 Kontribusi

Kontribusi sangat diterima! Jangan ragu untuk mengirimkan Pull Request.

