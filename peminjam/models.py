from django.db import models

class Peminjam(models.Model):
    nama = models.CharField(max_length=250, unique=True, db_index=True)
    deskripsi = models.CharField(max_length=1000, blank=True)

    FAKULTAS = 'Fakultas'
    UKA = 'UKA'
    UKM = 'UKM'
    PILIHAN_TIPE_PEMINJAM = (
        (FAKULTAS, 'Fakultas'),
        (UKA, 'UKA'),
        (UKM, 'UKM'),
    )

    tipe = models.CharField(max_length=50, choices=PILIHAN_TIPE_PEMINJAM, default=UKM)

    def __str__(self):
        return self.nama + '-' + self.tipe
