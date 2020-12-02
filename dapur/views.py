from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
# Panggil model dan form
from dapur.forms import SuratMasuk, FSuratKeluar
from dapur.models import Surats, TSuratKeluar
from dapur.decorators import unauthenticated_user, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

def tua(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    #print(request.user)
    #'name' adalah variabel untuk dictonary
    return render(request, "homepage.html", {'name' : 'Harada'})


def berhasil(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    
    #'name' adalah variabel untuk dictonary
    return render(request, "aksi.html")

@login_required(login_url='masuk')
@admin_only
def homeuser1(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    
    #'name' adalah variabel untuk dictonary
    return render(request, "userbagum/homeuser.html")


@login_required(login_url='masuk')
def shkotakmasuk(request):
	upload = Surats.objects.all()
	return render(request, 'userbagum/kotakmasuk/kotakmasuk.html', {'upload_form': upload})


def tmbhsurat(request):
	return render(request, 'userbagum/kotakmasuk/tmbhkotak.html')


def kotakmasuk22(request):
	
    if request.method == 'POST':  
        form = SuratMasuk(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shkotakmasuk')
    else:
        form = SuratMasuk()
    return render(request, 'userbagum/kotakmasuk/kotakmasuk.html')


def updatekotakmasuk(request, pk):

	order = Surats.objects.get(nomor_surat=pk)
	usm = SuratMasuk(instance=order)

	if request.method == 'POST':
		usm = SuratMasuk(request.POST, instance=order)
		if usm.is_valid():
			usm.save()
			return redirect('shkotakmasuk')

	return render(request, 'userbagum/kotakmasuk/UKotakMasuk.html',  {'update_data1':usm})


def Dkotakmasuk(request, nsurat):
	nsurat = int(nsurat)
	try:
		book_sel = Surats.objects.get(id = nsurat)
	except Surats.DoesNotExist:
		return redirect('homeuser1')
	book_sel.delete()
	return redirect('shkotakmasuk')


@login_required(login_url='masuk')
def shkotakkeluar(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    tmplsuratkeluar = TSuratKeluar.objects.all()
    #'name' adalah variabel untuk dictonary
    return render(request, "userbagum/kotakkeluar/kotakkeluar.html", {'tmpldata': tmplsuratkeluar})


def tmbhsuratkeluar(request):
	return render(request, 'userbagum/kotakkeluar/tmbh_data_keluar.html')

def svkotakkeluar(request):
	
    if request.method == 'POST':  
        form = FSuratKeluar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shkotakkeluar')
    else:
        form = FSuratKeluar()
    return render(request, 'userbagum/kotakkeluar/kotakkeluar.html')

def updatekotakkeluar(request, nsurat):

	order = TSuratKeluar.objects.get(Nomor_surat=nsurat)
	usk = FSuratKeluar(instance=order)

	if request.method == 'POST':
		usk = FSuratKeluar(request.POST, instance=order)
		if usk.is_valid():
			usk.save()
			return redirect('svkotakkeluar')

	return render(request, 'userbagum/kotakkeluar/UKotakKeluar.html', {'ubahdata':usk})

def Deletesuratkeluar(request, nsurat1):
	nsurat1 = int(nsurat1)
	try:
		book_sel = TSuratKeluar.objects.get(id = nsurat1)
	except TSuratKeluar.DoesNotExist:
		return redirect('homeuser1')
	book_sel.delete()
	return redirect('shkotakkeluar')



@login_required(login_url='masuk')
def homeuser2(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    
    #'name' adalah variabel untuk dictonary
    return render(request, "analis/homepage.html")


	

@unauthenticated_user
def regist(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
	if request.method == 'POST':	
		firstname = request.POST['fn']
		lastname = request.POST['ln']
		username = request.POST['nama']
		password = request.POST['psw']
		email	 = request.POST['email']
		if User.objects.filter(username=username).exists():
			messages.info (request,'username taken')
			return redirect('regist')

		elif User.objects.filter(email=email).exists():
			messages.info (request,'email taken')
			return redirect('regist')
			

		else:
			varuser2 = User.objects.create_user(first_name=firstname, last_name=lastname,  username=username, password=password, email=email)
			varuser2.save()
			print ('user created')
			return redirect('tua')

	else:
		return render(request, 'daftar.html')


#LOGIN CODE
@unauthenticated_user
def masuk(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
	if request.method == 'POST':	
		username = request.POST['nama']
		password = request.POST['psw']

		varuser = auth.authenticate(username=username,password=password)

		if varuser is not None:
			auth.login(request, varuser)
			return redirect('homeuser1')
		else:
			messages.info(request,'invalid credentials')
			return redirect('masuk')
		#'name' adalah variabel untuk dictonary
	else:
		return render(request, 'login.html')


def keluar(request):
	auth.logout(request)
	return redirect('masuk')