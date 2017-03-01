from django import forms
from models import Notification



# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------

class NotificationForm(forms.ModelForm):
	title = forms.CharField(label="Notification title")
	body = forms.CharField(label="Notification body")
	api_key = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea emojy'}), label="Firebase API_KEY")
	destination = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea emojy'}), label="Notification target")
	
	class Meta:
		model = Notification
		fields = ('title', 'body', 'api_key', 'destination', 'single_notification',)

