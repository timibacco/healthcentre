from django.db import models
# Create your models here.

class defualtInfo(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('others', 'others'),
    )    
    MARITAL_STATUS = (
        ('single', 'SINGLE'),
        ('married', 'MARRIED'),
    )
    TITLE_STATUS = (
        ('mr', 'Mr'),
        ('miss', 'Miss'),
        ('mrs', 'Mrs'),
        ('dr', 'Dr')
    )
    CLASS = (
        ('undergraduate','Undergraduate'),
        ('graduate', 'Graduate'),
    )
    KINS = (
        ('cousin', 'Cousin'),
        ('spouse', 'Spouse'),
        ('parent','Parent'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('guardian', 'Guardian')
    )
    first_name = models.CharField(max_length= 150)
    last_name = models.CharField(max_length= 150)
    regNo = models.CharField(max_length= 25)
    HRegNo = models.CharField(max_length =25)
    sex = models.CharField(max_length= 3, choices= SEX_CHOICES, default='others')
    Age = models.IntegerField(max_length =15)
    mobileNo = models.IntegerField(max_length= 11)
    birthDate = models.DateTimeField()
    maritalStatus = models.CharField(max_length = 8, choices = MARITAL_STATUS, default= 'single')
    tribe = models.CharField(max_length = 20)
    stateOfOrigin = models.CharField( max_length = 29)
    nationality = models.CharField(max_length= 150)
    religion = models.CharField(max_length= 100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length= 100)
    kinName = models.CharField(max_length= 150)
    kinAddress = models.CharField(max_length = 500)
    kinMobile = models.IntegerField(max_length= 11)
    regStatus = models.BooleanField(default = False)
    def __str__(self):  
        return self.first_name + " " + self.last_name  

class privyInfo(models.Model):
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    )
    GENOTYPES = (
        ('AA', 'AA'),
        ('AC', 'AC'),
        ('AS', 'AS'),
        ('CC', 'CC'),
        ('SC', 'SC'),
        ('SS', 'SS'),
    )
    bloodGroup = models.CharField(max_length = 3,choices = BLOOD_GROUP)
    genotype = models.TextField(max_length= 2, choices= GENOTYPES)
    weight = models.DecimalField(max_length = 6)
    height = models.DecimalField(max_length = 6)
    allergies = models.BooleanField(default= False)
    disability = models.BooleanField(default =False)

