from django import forms
from dapur.models import Surats
from dapur.models import TSuratKeluar


#class StudentForm(forms.ModelForm):
 #   class Meta:
  #      model = Students
   #     fields = "__all__"


#DataFlair
class SuratMasuk(forms.ModelForm):

	class Meta:
		model = Surats
		fields = "__all__"

class FSuratKeluar(forms.ModelForm):

	class Meta:
		model = TSuratKeluar
		fields = "__all__"
		
		