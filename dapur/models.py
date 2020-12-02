from django.db import models

# Create your models here.

#class Students(models.Model):
 #   nama = models.CharField(max_length=100)
  #  psw = models.CharField(max_length=100)
   # email = models.EmailField(blank = True)
   # picture = models.ImageField()
  
#class Meta:
 #   db_table = "dapur_students" 

class Surats(models.Model):
  CATEGORY = (
            ('Biasa', 'Biasa'),
            ('Segera', 'Segera'),
            ('Mendesak','Mendesak'),
            )
  KLASFIK = (
            ('Kilat', 'Kilat'),
            ('Express', 'Express'),
            ('Biasa','Biasa'),
            )

  nomor_surat =  models.CharField(max_length=100)
  tanggal_surat = models.DateField()
  kategori = models.CharField(max_length=50, null=False, choices=CATEGORY)
  klasifikasi = models.CharField(max_length=50, null=False, choices=KLASFIK)
  pengirim = models.CharField(max_length=100)
  perihal = models.TextField(default = 'DataFlair Django tutorials')
  attachment = models.FileField(upload_to='filesimpan/attachments/')

  def __str__(self):
      return self.nomor_surat

class TSuratKeluar(models.Model):
  CATEGORY = (
            ('Biasa', 'Biasa'),
            ('Segera', 'Segera'),
            ('Mendesak','Mendesak'),
            )
  KLASFIK = (
            ('Umum', 'Umum'),
            ('Khusus', 'Khusus'),
            ('Kilat','Kilat'),
            )

  Nomor_surat =  models.CharField(max_length=100)
  Tanggal_surat = models.DateField()
  Kategori = models.CharField(max_length=50, null=False, choices=CATEGORY)
  Klasifikasi = models.CharField(max_length=50, null=False, choices=KLASFIK)
  Tujuan = models.CharField(max_length=100)
  Tembusan = models.CharField(max_length=100)
  Perihal = models.TextField(default = 'Default ')
  Attachment = models.FileField(upload_to='filekeluar/attachments/')

  def __str__(self):
      return self.Nomor_surat


