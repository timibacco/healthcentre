from django.db import models
# Create your models here.

class Patient(models.Model):
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
    
    KINS = (
        ('cousin', 'Cousin'),
        ('spouse', 'Spouse'),
        ('parent','Parent'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('guardian', 'Guardian')
    )
    CLASS = [
        ('Student',(
        ('Undergraduate','Undergraduate'),
        ('Graduate', 'Graduate')
        )
    ),
        ('Staff', (
        ('academic staff','Academic Staff'),
        ( 'non-academic staff','Non-academic Staff')
        )
    ),
        ('visitor', 'Visitor'),
        ('unknown', 'Unknown')
    
    ]

    first_name = models.CharField(max_length= 150)
    last_name = models.CharField(max_length= 150)
    regNo = models.CharField(max_length= 25,unique = True)
    HRNo = models.CharField(max_length =25, unique = True)
    sex = models.CharField(max_length= 6, choices= SEX_CHOICES, default='others')
    Age = models.IntegerField()
    mobileNo = models.CharField(max_length=20, unique = True)
    birthDate = models.DateTimeField()
    maritalStatus = models.CharField(max_length = 8, choices = MARITAL_STATUS, default= 'single')
    kind = models.CharField(max_length = 19, choices = CLASS, default = 'unknown')
    tribe = models.CharField(max_length = 20)
    stateOfOrigin = models.CharField( max_length = 29)
    nationality = models.CharField(max_length= 150)
    religion = models.CharField(max_length= 100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length= 100)
    kinName = models.CharField(max_length= 150)
    kinAddress = models.CharField(max_length = 500)
    kinMobile = models.CharField(max_length= 20)
    regStatus = models.BooleanField(default = False)
    def __str__(self):  
        return self.HRNo 

class HealthProfile(models.Model):
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bloodGroup = models.CharField(max_length = 3,choices = BLOOD_GROUP)
    genotype = models.TextField(max_length= 2, choices= GENOTYPES)
    weight = models.DecimalField(max_digits= 5, decimal_places= 2)
    height = models.DecimalField(max_digits= 3, decimal_places= 2)
    allergies = models.BooleanField(default= False)
    disability = models.BooleanField(default =False)
    
    def __str__(self):
        return f"Health Profile of {self.patient.HRNo}"

