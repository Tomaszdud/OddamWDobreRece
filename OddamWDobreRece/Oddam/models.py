from django.db import models
from django.contrib.auth.models import AbstractUser

LOCALIZATION_CHOICES = (('warsaw','Warszawa'),
                        ('wroclaw','Wrocław'),
                        ('poznan','Poznań'),
                        ('gdansk','Gdańsk'),)

FOR_CHOICES = (('children','children'),
                ('mothers','mothers'),
                ('homeless','homeless'),
                ('disabled','disabled'),
                ('old','old'),)

TYPE_CHOICES = (('clothes-to-use','clothes-to-use'),
                ('clothes-useless','clothes-useless'),
                ('toys','toys'),
                ('books','books'),
                ('other','other'),)


class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Institution(models.Model):
    name = models.CharField(max_length=100)
    localization = models.CharField(max_length=7,choices=LOCALIZATION_CHOICES)


class Gift(models.Model):
    type_of_thing = models.CharField(max_length=15, choices=TYPE_CHOICES)
    capacity = models.DecimalField(max_digits=3, decimal_places=2)
    localization = models.CharField(max_length=7,choices=LOCALIZATION_CHOICES)
    for_who = models.CharField(max_length=8, choices=FOR_CHOICES)
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)


class Adress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_code = models.TextField(max_length=7)
    phone_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    info = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)