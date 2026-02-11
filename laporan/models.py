from django.db import models
from django.utils import timezone
class LaporanLapangan(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    nama_tim = models.CharField(max_length=100, help_text="Misal: Tim Alpha")
    penerima = models.CharField(max_length=100, help_text="Misal: Pak Budi")
    alamat = models.TextField()
    jarak_km = models.DecimalField(max_digits=5, decimal_places=2)
    keterangan = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    tanggal = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nama_tim} - {self.penerima}"

# Tabel khusus untuk menangani Multiple Uploads
class FotoLaporanLapangan(models.Model):
    laporan = models.ForeignKey(LaporanLapangan, on_delete=models.CASCADE, related_name='foto_bukti')
    gambar = models.ImageField(upload_to='bukti_lapangan/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class LaporanKantor(models.Model):
    nama_staf = models.CharField(max_length=100, help_text="Misal: Andi")
    deskripsi = models.TextField(help_text="Apa yang dikerjakan")
    foto_hasil = models.ImageField(upload_to='hasil_kantor/', null=True, blank=True)
    
    # PERBAIKAN DI SINI:
    # Hapus 'auto_now_add=True', ganti dengan 'default=timezone.now'
    tanggal = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.nama_staf} - {self.tanggal.strftime('%Y-%m-%d')}"