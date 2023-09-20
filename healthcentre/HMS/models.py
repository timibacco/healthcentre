from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from HMS.enums import sexChoices, maritalStatus, Kind, Kins, titleStatus, Genotypes, bloodGroup
# Create your models here.




class HealthProfile(models.Model):
    
        


    #is_active = models.BooleanField( default = True)
    #date = models.DateTimeField( default = datetime.datetime)
    healthcentre_No= models.CharField(max_length= 12 , blank= True, null= True )
    bloodGroup = models.CharField(max_length =7, choices = bloodGroup,default = bloodGroup.UNKNOWN)
    genotype = models.CharField(max_length= 7, choices= Genotypes, default = Genotypes.UNKNOWN )

    weight = models.DecimalField(max_digits= 5, decimal_places= 2, null=True)
    height = models.DecimalField(max_digits= 3, decimal_places= 2, null=True)
    allergies = models.BooleanField(default= False)
    disability = models.BooleanField(default =False)
    
    def __str__(self):
        return self.healthcentre_No
    



class Patient(models.Model):
   
   
    

    first_name = models.CharField(max_length= 150)
    last_name = models.CharField(max_length= 150)
    matric_No = models.CharField(max_length= 25,unique = True)
    healthcentre_No = models.CharField(max_length =25, unique = True)
    sex = models.CharField(max_length = 6, choices= sexChoices, 
                            default = sexChoices.OTHERS)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    age = models.IntegerField()
    mobileNo = models.CharField(max_length=20, unique = True)
    health_profile = models.OneToOneField(HealthProfile, on_delete=models.CASCADE, blank=True, null=True,related_name= 'medical_info')
    birthDate = models.DateTimeField()
    maritalStatus = models.CharField( max_length = 1, choices = maritalStatus,
                                         default= maritalStatus.SINGLE)

    kind = models.CharField( max_length = 7, choices = Kind,
                                 default = Kind.UNKNOWN)
    tribe = models.CharField(max_length = 20)
    stateOfOrigin = models.CharField( max_length = 29)
    nationality = models.CharField(max_length= 150)
    religion = models.CharField(max_length= 100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length= 100)
    kinName = models.CharField(max_length= 150)
    kinAddress = models.CharField(max_length = 500)
    kin_relationship = models.CharField(max_length = 8,choices = Kins, default = Kins.BROTHER)
   
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