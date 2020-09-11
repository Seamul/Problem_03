from django.shortcuts import render,HttpResponse
from .forms import InputDataFromUser
# Create your views here.
from django.shortcuts import get_object_or_404
def home(request):
	if request.method=='POST':
		input_data_form=InputDataFromUser(request.POST)
		if input_data_form.is_valid():
			cd=input_data_form.cleaned_data
		b5=cd['pipe_outside_diameter']
		b6=cd['pipe_wall_thickness']
		b7=cd['pipe_density']
		b8=cd['corrosion_allowance']
		c11=cd['fbe_thickness']
		d11=cd['fbe_Density']
		c15=cd['installation_empty']
		c16=cd['flooded']
		c17=cd['hydrotest']
		e5=-.005
		E3=(b5-2*b6)/2
		E4=e5+E3
		E5=E4+c11/2
		E6=E5*2
		E10=3.1416*(E5*E5-E4*E4)/144*d11
		E11=3.1416*E3*E3/144*c15
		E13=3.1416*E5*E5/144*c17
		dic={"E3":E3,"E4":E4,"E5":E5,"E6":E6,"E10":E10,"E11":E11,"E13":E13}
		print(dic)
		return render(request,'home/output.html',dic)
	    
	else:
		input_data_form=InputDataFromUser()
		print("get")
		

	
	return render(request,'home/home.html',{"form":input_data_form})


	# pipe_outside_diameter =forms.FloatField(initial=10.75)
	# pipe_wall_thickness =forms.FloatField(initial=0.5)
	# pipe_density =forms.FloatField(initial=490)
	# corrosion_allowance=forms.FloatField(initial=0.125)
	# fbe=forms.FloatField(initial=0.0118)
	# installation_empty=forms.FloatField(initial=0)
	# flooded=forms.FloatField(initial=64)
	# hydrotest=forms.FloatField(initial=64.7)
