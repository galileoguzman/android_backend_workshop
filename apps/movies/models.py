from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from helpers.helper_images import make_upload_path

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=50)
	synopsis = models.TextField()
	cover = models.ImageField(upload_to=make_upload_path, default='default.jpg')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	def __str__(self):
		return '%s %s' % (self.name)

	def thumbnail(self):
		if self.cover:
			return u'<img src="%s" width=50 height=50 />' % (self.cover.url)
		else:
			return u'No image file found'
	thumbnail.short_description = 'Thumbnail image'
	thumbnail.allow_tags = True


# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Movie)
def movie_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.cover.delete(False)