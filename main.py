import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import os

# Path lokasi file XML - pastikan path ini benar
cascade_dir = "haarcascades"  # direktori untuk menyimpan file XML

# Buat direktori jika belum ada
if not os.path.exists(cascade_dir):
    os.makedirs(cascade_dir)

# Download file XML yang diperlukan untuk deteksi wajah dan senyum
face_cascade_path = os.path.join(cascade_dir, "haarcascade_frontalface_default.xml")
smile_cascade_path = os.path.join(cascade_dir, "haarcascade_smile.xml")

# Download file jika belum ada
if not os.path.exists(face_cascade_path):
    print("Downloading face cascade file...")
    import urllib.request
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml",
        face_cascade_path
    )

if not os.path.exists(smile_cascade_path):
    print("Downloading smile cascade file...")
    import urllib.request
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_smile.xml",
        smile_cascade_path
    )

# Verifikasi file telah didownload
print(f"Face cascade file exists: {os.path.exists(face_cascade_path)}")
print(f"Smile cascade file exists: {os.path.exists(smile_cascade_path)}")

# Inisialisasi cascade classifiers dengan path lengkap
face_cascade = cv2.CascadeClassifier(face_cascade_path)
smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

# Verifikasi classifier berhasil dimuat
if face_cascade.empty():
    print("ERROR: Gagal memuat face cascade classifier!")
else:
    print("Face cascade classifier berhasil dimuat.")

if smile_cascade.empty():
    print("ERROR: Gagal memuat smile cascade classifier!")
else:
    print("Smile cascade classifier berhasil dimuat.")

# Inisialisasi webcam
cap = cv2.VideoCapture(0)  # 0 untuk webcam default

# Periksa apakah webcam berhasil diinisialisasi
if not cap.isOpened():
    print("Error: Tidak dapat membuka webcam.")
    exit()

# Variabel untuk menghitung FPS
prev_frame_time = 0
new_frame_time = 0

# Tombol shortcut
print("Tekan 'q' untuk keluar")
print("Tekan 's' untuk menyimpan gambar")
print("Tekan 'f' untuk toggle deteksi wajah")
print("Tekan 'm' untuk toggle deteksi senyum")

# Flag untuk mengaktifkan/menonaktifkan deteksi
detect_face = True  # Kita tetap perlu mendeteksi wajah untuk mencari ROI senyum
detect_smile = True

# Main loop untuk real-time video
while True:
    # Membaca frame dari webcam
    ret, frame = cap.read()
    
    # Jika frame tidak berhasil dibaca, keluar dari loop
    if not ret:
        print("Error: Tidak dapat membaca frame.")
        break
    
    # Menghitung FPS
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    
    # Konversi frame ke grayscale untuk deteksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah (dibutuhkan untuk mencari region senyum)
    if detect_face and not face_cascade.empty():
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        for (x, y, w, h) in faces:
            # Gambar kotak di sekitar wajah (dibuat transparan/tidak terlihat)
            # Kita hanya menandai wajah dengan titik kecil di sudut kiri atas untuk referensi
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
            
            # Region of interest untuk wajah
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
            # Deteksi senyum dalam region wajah
            if detect_smile and not smile_cascade.empty():
                smiles = smile_cascade.detectMultiScale(
                    roi_gray,
                    scaleFactor=1.8,
                    minNeighbors=20,
                    minSize=(25, 25)
                )
                for (sx, sy, sw, sh) in smiles:
                    # Gambar kotak merah di sekitar senyum
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
                    
                    # Tambahkan teks "Smile Detected" di bawah kotak senyum
                    smile_y = y + sy + sh + 20
                    if smile_y < frame.shape[0]:  # Pastikan teks tidak keluar dari frame
                        cv2.putText(frame, "Smile Detected!", (x + sx, smile_y), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Tampilkan informasi FPS
    cv2.putText(frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Tampilkan informasi deteksi
    status_text = f"Smile Detection: {'ON' if detect_smile else 'OFF'}"
    cv2.putText(frame, status_text, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Tampilkan frame
    cv2.imshow('Smile Detection', frame)
    
    # Tunggu input keyboard
    key = cv2.waitKey(1) & 0xFF
    
    # Tekan 'q' untuk keluar
    if key == ord('q'):
        break
    # Tekan 's' untuk menyimpan gambar
    elif key == ord('s'):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite(f'smile_detection_{timestamp}.jpg', frame)
        print(f"Gambar disimpan sebagai smile_detection_{timestamp}.jpg")
    # Toggle deteksi wajah dengan 'f'
    elif key == ord('f'):
        detect_face = not detect_face
        if not detect_face:
            print("PERHATIAN: Menonaktifkan deteksi wajah akan menghentikan deteksi senyum")
    # Toggle deteksi senyum dengan 'm'
    elif key == ord('m'):
        detect_smile = not detect_smile

# Lepaskan webcam dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()