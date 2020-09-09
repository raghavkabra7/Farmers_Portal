from django.db import models
from django.contrib.auth.models import User
from django_matplotlib import MatplotlibFigureField


# Create your models here.

# Create your models here.


class districs(models.Model):
    name  = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class states(models.Model):
    name  = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name

class User_detail(models.Model):
    usr = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    dis = models.ForeignKey(districs,on_delete = models.CASCADE,null=True)
    states1 = models.ForeignKey(states, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=10, null=True)
    aadhar = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=12, null=True)
    language = models.CharField(max_length=12, null=True)
    size = models.CharField(max_length=12, null=True)

    id_proof = models.CharField(max_length=100, null=True)
    photo = models.FileField( null=True)
    def __str__(self):
        return self.name


class districs_notes(models.Model):
    dis = models.ForeignKey(districs, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class states_notes(models.Model):
    states1 = models.ForeignKey(states, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')


class pest(models.Model):
    pest_name = models.CharField(max_length=100, null=True)
    photo = models.FileField(null=True)
    short_disc = models.TextField(null=True)
    long_disc = models.TextField(null=True)
    demage = models.TextField(blank=True, null=True)
    Preventing = models.TextField(blank=True, null=True)
    Tips = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pest_name


class Pestsolution(models.Model):
    pest_name = models.ForeignKey(pest, on_delete=models.CASCADE, null=True)
    photo1 = models.FileField(blank=True, null=True)
    madecine = models.TextField(blank=True, null=True)


class Crop(models.Model):
    crop_name = models.CharField(max_length=100, null=True)
    photo = models.FileField(null=True)
    short_disc = models.TextField(null=True)
    long_disc = models.TextField(null=True)

    def __str__(self):
        return self.crop_name


class Cropsolution(models.Model):
    crop_name = models.ForeignKey(Crop, on_delete=models.CASCADE, null=True)
    photo = models.FileField(blank = True,null=True)
    photo_dec = models.TextField(blank = True,null=True)

class Soil_detail(models.Model):
    soil = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    Ph =   models.CharField(max_length=10, null=True)
    cn = models.CharField(max_length=10, null=True)
    phos = models.CharField(max_length=10, null=True)
    pot = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name