from django.db import models

# Create your models here.

# create table
class parkinsons(models.Model):
   
    avgfq = models.CharField(max_length=50,default='1')
    maxfq = models.CharField(max_length=50,default='1')
    minfq = models.CharField(max_length=50,default='1')
    varfq1 = models.CharField(max_length=50,default='1')
    varfq2 = models.CharField(max_length=50,default='1')
    varfq3 = models.CharField(max_length=50,default='1')
    varfq4 = models.CharField(max_length=50,default='1')
    varfq5 = models.CharField(max_length=50,default='1')
    amplitude1 = models.CharField(max_length=50,default='1')
    amplitude2 = models.CharField(max_length=50,default='1')
    amplitude3 = models.CharField(max_length=50,default='1')
    amplitude4 = models.CharField(max_length=50,default='1')
    amplitude5 = models.CharField(max_length=50,default='1')
    amplitude6 = models.CharField(max_length=50,default='1')
    noise1 = models.CharField(max_length=50,default='1')
    noise2 = models.CharField(max_length=50,default='1')
    complexity1 = models.CharField(max_length=50,default='1')
    scalling = models.CharField(max_length=50,default='1')
    nonlinearfq1 = models.CharField(max_length=50,default='1')
    nonlinearfq2 = models.CharField(max_length=50,default='1')
    complexity2 = models.CharField(max_length=50,default='1')
    nonlinearfq3 = models.CharField(max_length=50,default='1')
    result = models.CharField(max_length=50,default='1')