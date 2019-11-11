from django.db import models

class Cat(models.Model):
	image = models.ImageField(upload_to='images/')
	text = models.CharField(max_length=300)
	