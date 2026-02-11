# 📊 Sistem Monitoring & Laporan Lapangan (Django)

Aplikasi berbasis web untuk memantau aktivitas tim lapangan dan staf kantor secara real-time. Dilengkapi dengan dashboard eksekutif, visualisasi data, CRUD (Create, Read, Update, Delete), dan fitur ekspor laporan otomatis.

## 🚀 Fitur Utama

### 1. Dashboard Eksekutif
* **Visualisasi Data:** 6 Grafik interaktif (Harian, Jam Sibuk, Performa Staf, Status) menggunakan Chart.js.
* **KPI Cards:** Ringkasan statistik performa secara visual.
* **Filter Canggih:** Filter seluruh data dan grafik berdasarkan rentang tanggal yang dinamis.

### 2. Manajemen Laporan (CRUD Lengkap)
* **Laporan Lapangan:** Input data pengiriman, jarak tempuh, lokasi, dan **Multiple Upload** bukti foto.
* **Aktivitas Kantor:** Log aktivitas harian staf internal.
* **Edit & Hapus:** Fitur koreksi data (Edit) dan penghapusan data (Delete) langsung dari dashboard.
* **Validasi Status:** Status Submitted, Approved, dan Rejected.

### 3. Fitur Ekspor Canggih (Report Generation)
* **📄 Export PDF:** Menghasilkan dokumen PDF siap cetak. Foto bukti dilampirkan secara otomatis pada halaman lampiran terpisah agar rapi.
* **📊 Export Excel:** Menghasilkan file `.xlsx` dimana **foto bukti tertanam langsung (embedded)** di dalam sel Excel, bukan sekadar link.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python, Django 5.x
* **Frontend:** HTML5, Tailwind CSS (CDN), JavaScript (Modern UI)
* **Database:** SQLite (Default) / PostgreSQL (Ready)
* **Libraries:**
    * `Chart.js` (Visualisasi Grafik)
    * `jspdf` & `jspdf-autotable` (PDF Generation)
    * `ExcelJS` & `FileSaver` (Excel Generation with Images)

---

## 📦 Cara Install & Menjalankan (Localhost)

Ikuti langkah ini untuk menjalankan proyek di komputer Anda:

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/USERNAME_ANDA/proyek-monitoring.git](https://github.com/USERNAME_ANDA/proyek-monitoring.git)
    cd proyek-monitoring
    ```

2.  **Buat Virtual Environment**
    ```bash
    python -m venv venv
    
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Migrasi Database**
    ```bash
    python manage.py migrate
    ```

5.  **Buat Superuser (Untuk akses admin)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```

7.  **Akses Aplikasi**
    * Dashboard: `http://127.0.0.1:8000/`
    * Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📖 Panduan Penggunaan Aplikasi

Berikut adalah langkah-langkah menggunakan fitur utama aplikasi:

### 1. Membuat Laporan Baru
1.  Di halaman Dashboard, klik tombol **"➕ Input Baru"** di pojok kanan atas.
2.  Pilih Tab yang sesuai:
    * **Laporan Lapangan:** Untuk tim logistik/lapangan. Isi Nama Tim, Penerima, Jarak, Keterangan, dan **Upload Foto Bukti** (bisa pilih banyak foto sekaligus).
    * **Aktivitas Kantor:** Untuk staf internal. Isi Nama Staf, Deskripsi Pekerjaan, dan Foto Hasil (opsional).
3.  Klik tombol **Kirim Laporan**. Data akan otomatis masuk ke Dashboard.

### 2. Mengelola Data (Edit & Hapus)
Setiap kartu laporan di Dashboard memiliki tombol aksi di bagian bawah:
* **Edit (✏️):** Klik ikon pensil untuk mengubah data yang salah atau menambah foto.
* **Hapus (🗑️):** Klik ikon sampah untuk menghapus laporan (akan muncul konfirmasi pop-up agar aman).

### 3. Filter Data & Grafik
1.  Gunakan kolom **Tanggal Mulai** dan **Tanggal Akhir** di bagian atas Dashboard.
2.  Klik tombol **Filter**.
3.  Semua grafik statistik, PDF, dan Excel akan menyesuaikan data berdasarkan rentang tanggal yang dipilih.

### 4. Export Laporan
* **Export PDF:** Klik tombol **📄 PDF**. Sistem akan memproses gambar dan menghasilkan laporan siap cetak dengan halaman lampiran foto.
* **Export Excel:** Klik tombol **📊 Excel**. Sistem akan mendownload file `.xlsx` dengan gambar fisik yang tertanam di dalam sel tabel.

### 5. Mengubah Status Laporan (Admin)
1.  Masuk ke halaman Admin (`/admin`).
2.  Pilih menu **Laporan Lapangan**.
3.  Pilih laporan dan ubah statusnya menjadi **Approved** atau **Rejected**.
4.  Perubahan status akan terlihat di Dashboard (Badge warna Hijau/Merah).

---

## 📷 Screenshot

*(Anda bisa menambahkan screenshot aplikasi di sini nanti)*

---
Dibuat dengan ❤️ menggunakan Django.
