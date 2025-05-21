from django.db import models


class Karyawan(models.Model):
    pilihan_pendidikan = [
        ("SMA", "SMA"),
        ("S1", "S1"),
        ("S2", "S2")
    ]

    pilihan_jabatan = [
        ("Anggota Security", "Anggota Security"),
        ("Danru Security", "Danru Security"),
        ("Chief Security", "Chief Security"),
        ("Staff Operasional", "Staff Operasional"),
        ("Direktur", "Direktur"),
        ("Direktur Keuangan", "Direktur Keuangan"),
        ("Manager Operasional", "Manager Operasional"),
        ("HRD", "HRD")]

    pilihan_sertifikat = [
        ("Gada Pratama", "Gada Pratama"),
        ("Gada Madya", "Gada Madya"),
        ("Gada Utama", "Gada Utama")
    ]

    pilihan_jk = [
        ("Laki-laki", "Laki-laki"),
        ("Perempuan", "Perempuan")
    ]

    pilihan_status = [
        ("TK/0", "TK/0"),
        ("TK/1", "TK/1"),
        ("TK/2", "TK/2"),
        ("K/0", "K/0"),
        ("K/1", "K/1"),
        ("K/2", "K/2")
    ]

    id = models.CharField(max_length=11, unique=True, primary_key=True)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=20, choices=pilihan_jabatan)
    lokasi = models.CharField(max_length=40)
    nik = models.CharField(max_length=16, unique=True)
    pendidikan = models.CharField(max_length=100, choices=pilihan_pendidikan)
    tanggal_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=100)
    kelamin = models.CharField(max_length=15, choices=pilihan_jk)
    status = models.CharField(max_length=5, choices=pilihan_status)
    nomor_kk = models.CharField(max_length=16)
    alamat_ktp = models.CharField(max_length=100)
    alamat_tinggal = models.CharField(max_length=100)
    ibu = models.CharField(max_length=40)
    nohp = models.CharField(max_length=13)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama
