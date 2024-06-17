from django.db import models


# Create your models here.

class Images(models.Model):
    image = models.ImageField('images/')


class Compititiveprice(models.Model):
    image = models.ImageField('images/')
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    details = models.CharField(max_length=500)

class FreshAndOrganicBeans(models.Model):
    image = models.ImageField('images/')
    name = models.CharField(max_length=40)
    details = models.CharField(max_length=300)

class Specialoffer(models.Model):
    email = models.EmailField(max_length=30)

class Bookyourtable(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    date = models.DateField(max_length=20)
    time = models.TimeField(max_length=20)
    person = models.CharField(max_length=30)

class Ourclientssay(models.Model):
    image = models.ImageField('images/')
    name = models.CharField(max_length=40)
    comments = models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)