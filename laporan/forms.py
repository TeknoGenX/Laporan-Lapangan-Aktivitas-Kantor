from django import forms
from .models import LaporanLapangan, LaporanKantor

class LaporanLapanganForm(forms.ModelForm):
    # Definisi field biasa (JANGAN pasang attrs={'multiple': True} di sini)
    foto_bukti = forms.FileField(
        widget=forms.FileInput(), 
        label="Bukti Foto (Bisa pilih banyak)",
        required=False
    )
    class Meta:
        model = LaporanLapangan
        fields = ['nama_tim', 'penerima', 'alamat', 'jarak_km', 'tanggal', 'keterangan']
        widgets = {
            'keterangan': forms.Textarea(attrs={'rows': 3}),
            # TAMBAHKAN format='%Y-%m-%dT%H:%M' DI SINI
            'tanggal': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M' 
            ),
        }

    class Meta:
        model = LaporanLapangan
        fields = ['nama_tim', 'penerima', 'alamat', 'jarak_km', 'tanggal', 'keterangan']
        widgets = {
            'keterangan': forms.Textarea(attrs={'rows': 3}),
            'alamat': forms.Textarea(attrs={'rows': 3}),
            'tanggal': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # KITA SUNTIKKAN ATRIBUT 'MULTIPLE' DI SINI
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tambahkan atribut HTML 'multiple' secara manual agar tidak kena blokir validasi Django
        self.fields['foto_bukti'].widget.attrs.update({'multiple': True})


class LaporanKantorForm(forms.ModelForm):
    class Meta:
        model = LaporanKantor
        fields = ['nama_staf', 'deskripsi', 'foto_hasil', 'tanggal']
        widgets = {
            'deskripsi': forms.Textarea(attrs={'rows': 3}),
            # TAMBAHKAN format DI SINI JUGA
            'tanggal': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }