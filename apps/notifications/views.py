from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Notification
from forms import NotificationForm
from helpers import send_notification
# Create your views here.
@login_required()
def notification_new(request):
	if request.method == "POST":
		form = NotificationForm(request.POST, request.FILES)
		if form.is_valid():
			notification = form.save(commit=False)
			try:
				if send_notification(notification.title, notification.body, notification.single_notification, notification.api_key):
					notification.firebase_response = 'success'
				else:
					notification.firebase_response = 'error'
			except Exception, e:
				print e

			return redirect('home')
	else:
		form = NotificationForm()
	return render(request, 'notification_edit.html', {
		'form': form,
	})