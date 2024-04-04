from django.db import models

class Location(models.Model):
    coordinates = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    class Meta:
        indexes = [models.Index(fields=["address"])]
        ordering = ["address"]
    
class Family(models.Model):
    title = models.CharField(max_length=255)
    no_of_members = models.IntegerField(default=1)
    total_family_income = models.IntegerField()
    duration_of_residence = models.IntegerField(help_text="no of days")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=["title"])]

class Citizenship(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        indexes = [models.Index(fields=["title"])]

class EducationalAttainment(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        indexes = [models.Index(fields=["title"])]

class EmployementStatus(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        indexes = [models.Index(fields=["title"])]
    
class MaritalStatus(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        indexes = [models.Index(fields=["title"])]

class Member(models.Model):
    name = models.CharField(max_length=255, )
    age = models.IntegerField()
    contact_no = models.CharField(max_length=11)
    income  = models.DecimalField(max_digits=10 ,decimal_places=2)
    birthdate = models.DateField()
    birth_place = models.CharField(max_length=255)
    marital_status = models.OneToOneField(MaritalStatus, on_delete=models.CASCADE)
    citizenship = models.OneToOneField(Citizenship, on_delete=models.CASCADE)
    educational_attainment = models.OneToOneField(EducationalAttainment, on_delete=models.CASCADE)
    employement_status = models.OneToOneField(EmployementStatus, on_delete=models.CASCADE)
    family = models.ManyToManyField(Family)

    class Meta:
        indexes = [models.Index(fields=["name"])]
        ordering = ["name"]