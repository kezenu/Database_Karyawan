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
            "ibu",
            "nohp",
            "email",
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
