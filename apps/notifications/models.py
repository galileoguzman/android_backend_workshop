from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Notification(models.Model):
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=140)
	destination = models.TextField()
	single_notification = models.BooleanField(default=True)
	api_key = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.title
