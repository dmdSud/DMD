from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

class Cources(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=500)
    logo_link=models.CharField(max_length=500)
    reco=models.BooleanField(default=True)
    use=models.TextField(default="use")
    cource_book=models.TextField()
