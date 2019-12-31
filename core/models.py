from django.db import models


class Facebook(models.Model):
	post_id = models.CharField(max_length=100)
	post = models.TextField()

