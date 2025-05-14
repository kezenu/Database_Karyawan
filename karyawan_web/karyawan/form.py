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
            "tempat_lahir",
            "kelamin",
            "status",
            "nomor_kk",
            "alamat_ktp",
            "alamat_tinggal",
            "ibu_kandung",
            "nohp",
            "email",
        ]
