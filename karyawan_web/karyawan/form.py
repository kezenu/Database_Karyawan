from django import forms
from .models import Karyawan


class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = [
            "id",
            "nama",
            "jabatan",
            "lokasi",
            "nik",
            "pendidikan",
            "tanggal_lahir",
            "tempat_lahir",
            "kelamin",
            "status",
            "nomor_kk",
            "alamat_ktp",
            "alamat_tinggal",
            "ibu",
            "nohp",
            "email",
        ]
        widget = {
            "tanggal_lahir": forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tanggal_lahir'].input_formats = ['%Y-%m-%d']
