from django.urls import path
from django.contrib.auth import views as auth_views
from dapur import views
from django.conf import settings
from django.conf.urls.static import static
#from arsip.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

#file ini untuk memaanggil url /path kalian yang akan di proses pada file views 
urlpatterns = [
#views adalah file /class
#home adalah function/method
#'' =root directory
    path('', views.tua, name='tua'),
    path('regist', views.regist, name="regist"),
    path('masuk', views.masuk, name="masuk"),
    path('keluar', views.keluar, name="keluar"),

    path('homeuser2', views.homeuser2, name="homeuser2"),


    path('homeuser1', views.homeuser1, name="homeuser1"),
# bagian surat masuk
    path('tmbhsurat', views.tmbhsurat, name="tmbhsurat"),
    path('shkotakmasuk', views.shkotakmasuk, name="shkotakmasuk"),
    path('kotakmasuk22', views.kotakmasuk22, name="kotakmasuk22"),
    path('shkotakmasuk/<int:pk>/', views.updatekotakmasuk, name="updatekotakmasuk"),
    path('delete/<int:nsurat>', views.Dkotakmasuk),
# bagian surat KELUAR 
    path('shkotakkeluar', views.shkotakkeluar, name="shkotakkeluar"),
    path('tmbhsuratkeluar', views.tmbhsuratkeluar, name="tmbhsuratkeluar"),
    path('svkotakkeluar', views.svkotakkeluar, name="svkotakkeluar"),
    path('shkotakkeluar/<int:nsurat>/', views.updatekotakkeluar, name="updatekotakkeluar"),
    path('shkotakkeluar/<int:nsurat1>', views.Deletesuratkeluar,name="Deletesuratkeluar"),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

