#blueprints for database what tables to use and colums and how to connect them
from django.db import models

# Create your models here.  
class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length = 250)
	genre = models.CharField(max_length = 100)
	album_logo = models.CharField(max_length = 1000)

	def __str__ (self):
		return self.album_title



class song(models.Model):
	album = models.ForeignKey(Album,on_delete = models.CASCADE)
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length = 250)
