from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.




class HealthProfile(models.Model):
    class BloodGroup(models.TextChoices):
        A_PLUS =     'A+', 'A+'
        A_MINUS =    'A-', 'A-'
        B_PLUS =     'B+', 'B+'
        B_MINUS =     'B-', 'B-'
        O_PLUS =     'O+', 'O+'
        O_MINUS =    'O-', 'O-'
        AB_PLUS =    'AB+', 'AB+'
        AB_MINUS  =    'AB-', 'AB-'
        UNKNOWN = 'Unknown', 'UNKNOWN'
        
    class Genotypes(models.TextChoices):
        AA =   'AA', 'AA'
        AC =   'AC', 'AC'
        AS =   'AS', 'AS'
        CC =   'CC', 'CC'
        SC =    'SC', 'SC'
        SS =     'SS', 'SS'
        UNKNOWN = 'Unknown', 'UNKNOWN'

    #is_active = models.BooleanField( default = True)
    #date = models.DateTimeField( default = datetime.datetime)
    healthcentre_No= models.CharField(max_length= 12 , blank= True, null= True )
    bloodGroup = models.CharField(max_length =7, choices = BloodGroup.choices,default = BloodGroup.UNKNOWN)
    genotype = models.CharField(max_length= 7, choices= Genotypes.choices, default = Genotypes.UNKNOWN )

    weight = models.DecimalField(max_digits= 5, decimal_places= 2, null=True)
    height = models.DecimalField(max_digits= 3, decimal_places= 2, null=True)
    allergies = models.BooleanField(default= False)
    disability = models.BooleanField(default =False)
    
    def __str__(self):
        return self.healthcentre_No
    



class Patient(models.Model):
    class SexChoices(models.TextChoices):
        MALE =   'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHERS = 'Others', 'others'
            
    class MaritalStatus(models.TextChoices):
        SINGLE =     'S', 'SINGLE'
        MARRIED =    'M', 'MARRIED'
        
    class TitleStatus(models.TextChoices):
        MR = 'mr', 'Mr'
        MISS = 'miss', 'Miss'
        MRS = 'mrs', 'Mrs'
        DR =  'dr', 'Dr'
    
    class Kins(models.TextChoices):
        COUSIN = 'cousin', 'Cousin'
        SPOUSE =  'spouse', 'Spouse'
        PARENT = 'parent','Parent'
        SISTER = 'sister', 'Sister'
        BROTHER = 'brother', 'Brother'
        GUARDIAN = 'guardian', 'Guardian'
        
    class Kind(models.TextChoices):

        UNDERGRADUATE = 'UG','Undergraduate'
        GRADUATE =   'GR', 'Graduate'
        ACADEMIC= 'AC','Academic Staff'
        NON_ACADEMIC = 'NA','Non-academic Staff'
        VISITOR = 'VR', 'Visitor'
        UNKNOWN = 'Unknown', 'Unknown'
    

    first_name = models.CharField(max_length= 150)
    last_name = models.CharField(max_length= 150)
    matric_No = models.CharField(max_length= 25,unique = True)
    healthcentre_No = models.CharField(max_length =25, unique = True)
    sex = models.CharField(max_length = 6, choices= SexChoices.choices, 
                            default=SexChoices.OTHERS)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    Age = models.IntegerField()
    mobileNo = models.CharField(max_length=20, unique = True)
    health_profile = models.OneToOneField(HealthProfile, on_delete=models.CASCADE, blank=True, null=True,related_name= 'medical_info')
    birthDate = models.DateTimeField()
    maritalStatus = models.CharField( max_length = 1, choices = MaritalStatus.choices,
                                         default= MaritalStatus.SINGLE)

    kind = models.CharField( max_length = 7, choices = Kind.choices,
                                 default = Kind.UNKNOWN)
    tribe = models.CharField(max_length = 20)
    stateOfOrigin = models.CharField( max_length = 29)
    nationality = models.CharField(max_length= 150)
    religion = models.CharField(max_length= 100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length= 100)
    kinName = models.CharField(max_length= 150)
    kinAddress = models.CharField(max_length = 500)
    kin_relationship = models.CharField(max_length = 8,choices = Kins.choices, default = Kins.BROTHER)
   
    kinMobile = models.CharField(max_length= 20)
    regStatus = models.BooleanField(default = False)
    def __str__(self):  
        return self.first_name + self.last_name 

   

@receiver(post_save, sender=Patient)
def generate_health_profile_healthcentre_No(sender, instance, created, **kwargs):
    if created:
        if not instance.health_profile:
            health_profile = HealthProfile.objects.create(medical_info=instance, healthcentre_No=instance.healthcentre_No) 
            instance.health_profile = health_profile
            instance.save()