# 📊 Sistem Monitoring & Laporan Lapangan (Django)

Aplikasi berbasis web untuk memantau aktivitas tim lapangan dan staf kantor secara real-time. Dilengkapi dengan dashboard eksekutif, visualisasi data, dan fitur ekspor laporan otomatis.

## 🚀 Fitur Utama

### 1. Dashboard Eksekutif
* **Visualisasi Data:** 6 Grafik interaktif (Harian, Jam Sibuk, Performa Staf) menggunakan Chart.js.
* **KPI Cards:** Ringkasan statistik performa secara visual.
* **Filter Canggih:** Filter data berdasarkan rentang tanggal yang dinamis.

### 2. Manajemen Laporan
* **Laporan Lapangan:** Input data pengiriman, jarak tempuh, lokasi, dan **Multiple Upload** bukti foto.
* **Aktivitas Kantor:** Log aktivitas harian staf internal.
* **Validasi Status:** Status Submitted, Approved, dan Rejected.

### 3. Fitur Ekspor Canggih (Report Generation)
* **📄 Export PDF:** Menghasilkan dokumen PDF siap cetak. Foto bukti dilampirkan secara otomatis pada halaman lampiran terpisah agar rapi.
* **📊 Export Excel:** Menghasilkan file `.xlsx` dimana **foto bukti tertanam langsung (embedded)** di dalam sel Excel, bukan sekadar link.

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python, Django 5.x
* **Frontend:** HTML5, Tailwind CSS (CDN), JavaScript
* **Database:** SQLite (Default) / PostgreSQL (Ready)
* **Libraries:**
    * `Chart.js` (Visualisasi Grafik)
    * `jspdf` & `jspdf-autotable` (PDF Generation)
    * `ExcelJS` & `FileSaver` (Excel Generation with Images)

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

## 📷 Screenshot

*(Anda bisa menambahkan screenshot aplikasi di sini nanti)*

---
Dibuat dengan ❤️ menggunakan Django.