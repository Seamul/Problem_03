from django  import forms

class InputDataFromUser(forms.Form):
	pipe_outside_diameter =forms.FloatField(initial=10.75)
	pipe_wall_thickness =forms.FloatField(initial=0.5)
	pipe_density =forms.FloatField(initial=490)
	corrosion_allowance=forms.FloatField(initial=0.125)
	fbe_thickness=forms.FloatField(initial=0.0118)
	fbe_Density=forms.FloatField(initial=81.16)
	installation_empty=forms.FloatField(initial=0)
	flooded=forms.FloatField(initial=64)
	hydrotest=forms.FloatField(initial=64.7)









