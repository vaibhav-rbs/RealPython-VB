from django.db import models

# Create your models here.

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.TextField()

def __str__(self):
	return "{0}/{1}/{2}/{3}\n".format(self.id, self.created_at,self.title,self.content)