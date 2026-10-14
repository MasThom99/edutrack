# EduTrack 🎓
### Student Academic & Skill Portfolio Tracker

EduTrack adalah aplikasi mobile berbasis **Flutter** yang dibangun untuk memvisualisasikan direktori profil mahasiswa sekaligus merinci rekam jejak sertifikasi keahlian, prestasi, dan portofolio kompetensi dalam struktur relasi data bertingkat (**One-to-Many**).

Proyek ini dikembangkan sebagai pemenuhan **Latihan Praktikum & Pretest Pertemuan 1 - Pemrograman Mobile Lanjut**, Universitas Amikom Purwokerto.

---

## 👨‍🎓 Identitas Mahasiswa

* **Nama Lengkap**: Ikhwan Nur Rizki Fathama
* **NIM**: 24SA11A023
* **Program Studi**: Informatika
* **Fakultas**: Ilmu Komputer
* **Perguruan Tinggi**: Universitas Amikom Purwokerto
* **Dosen Pengampu**: Nandang Hermanto, M.Kom.

---

## ✨ Fitur Utama

1. **Direktori Mahasiswa (Layar 1 - `StudentListScreen`)**:
   - Menampilkan daftar kartu mahasiswa dalam *scrollable list* (`ListView.builder`).
   - Informasi kartu: Foto profil (*NetworkImage* melingkar), Nama Lengkap, NIM, Program Studi, dan chip indikator total sertifikasi.
   - Desain berbasis **Material 3 Academic Modern** (Deep Indigo `#1E3A8A` & Soft Slate `#F8FAFC`).

2. **Detail Profil & Portofolio Kredensial (Layar 2 - `StudentDetailScreen`)**:
   - **Header Profil**: Banner gradient elegan, foto avatar profil berdimensi besar, NIM, jurusan, surel, dan chip status verifikasi.
   - **Rekam Jejak 1-to-N**: Menampilkan riwayat **5+ item sertifikasi kompetensi** per mahasiswa.
   - Rincian item sertifikasi: Nama keahlian, lembaga kredensial (Dicoding, AWS, Google, Cisco, BNSP, dsb.), tahun perolehan, dan **Badge Grade** berwarna *Emerald Green* (`#059669`).

3. **Navigasi Cerdas & Efisien**:
   - Menerapkan *Object Parameter Passing* via `Navigator.push` yang meneruskan seluruh instance objek `Student` tanpa perlu query pencarian ulang ID di layar tujuan.
   - Dukungan tombol kembali (*Back button*) pada AppBar yang mempertahankan posisi gulir daftar utama.

---

## 🏗️ Struktur Proyek (Modular Architecture)

```
lib/
├── models/
│   ├── certification_model.dart    // Blueprint entitas relasi Certification
│   └── student_model.dart          // Blueprint entitas utama Student (menampung List<Certification>)
├── data/
│   └── dummy_data.dart             // Kumpulan data statis mahasiswa & sertifikasi relasi 1-to-N
├── screens/
│   ├── student_list_screen.dart    // Layar 1: Daftar kartu mahasiswa
│   └── student_detail_screen.dart  // Layar 2: Detail profil & portofolio sertifikasi
└── main.dart                       // Konfigurasi tema Material 3 dan entry point aplikasi
```

---

## 🚀 Panduan Menjalankan Aplikasi

Pastikan Anda telah menginstal **Flutter SDK** (versi 3.19 ke atas direkomendasikan).

1. **Clone repositori**:
   ```bash
   git clone <url-repo-anda>
   cd edutrack
   ```

2. **Unduh dependencies**:
   ```bash
   flutter pub get
   ```

3. **Verifikasi kode**:
   ```bash
   flutter analyze
   ```

4. **Jalankan aplikasi**:
   - Melalui Web Server:
     ```bash
     flutter run -d web-server --web-port=8080 --web-hostname=localhost
     ```
     Lalu buka browser di `http://localhost:8080`.
   - Melalui Chrome:
     ```bash
     flutter run -d chrome
     ```
   - Melalui Windows Desktop (jika toolchain terpasang):
     ```bash
     flutter run -d windows
     ```

---

## 📄 Dokumen Laporan & Presentasi

Dalam repositori ini juga disertakan:
* **Laporan Praktikum Lengkap (`.docx`)**: `Laporan_Praktikum_Pertemuan_1_Ikhwan_Nur_Rizki_Fathama.docx`
* **Naskah & Panduan Video Presentasi 5 Menit (`.pdf`)**: `EduTrack_Panduan_Presentasi_Tugas.pdf`
