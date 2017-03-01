from django import forms
from models import Movie



# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------

class MovieForm(forms.ModelForm):
	name = forms.CharField(label="Movie name")
	synopsis = forms.CharField(label="Movie description")
	
	class Meta:
		model = Movie
		fields = ('name', 'synopsis', 'cover', )

