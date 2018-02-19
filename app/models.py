from django.db import models

# Create your models here.
class NoteBook(models.Model):
	title = models.CharField(max_length=1337)
	

class Note(models.Model):
	title = models.CharField(max_length=1337)
	body = models.TextField()
	notebook= models.ForeignKey(NoteBook, on_delete = models.CASCADE, null=True)
