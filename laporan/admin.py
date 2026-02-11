from django.contrib import admin
from .models import LaporanLapangan, FotoLaporanLapangan, LaporanKantor

class FotoInline(admin.TabularInline):
    model = FotoLaporanLapangan
    extra = 1

@admin.register(LaporanLapangan)
class LaporanLapanganAdmin(admin.ModelAdmin):
    inlines = [FotoInline] # Memungkinkan upload banyak foto di satu halaman admin
    list_display = ('nama_tim', 'penerima', 'status', 'tanggal')
    list_filter = ('status', 'tanggal')

@admin.register(LaporanKantor)
class LaporanKantorAdmin(admin.ModelAdmin):
    list_display = ('nama_staf', 'tanggal')