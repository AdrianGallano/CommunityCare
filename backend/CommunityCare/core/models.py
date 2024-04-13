from django.db import models

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Non-binary", "Non-binary"),
    ("Other", "Other"),
    ("Prefer not to say", "Prefer not to say"),
)

class Location(models.Model):
    coordinates = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.address

    class Meta:
        indexes = [models.Index(fields=["address"])]
        ordering = ["address"]

    
    
class Family(models.Model):
    title = models.CharField(max_length=255)
    no_of_members = models.IntegerField(default=1)
    total_family_income = models.IntegerField()
    duration_of_residence = models.IntegerField(help_text="no of days")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]

class Citizenship(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]

class EducationalAttainment(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]

class EmploymentStatus(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]
    
class MaritalStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=["title"])]



class Member(models.Model):
    name = models.CharField(max_length=255, )
    age = models.IntegerField()
    contact_no = models.CharField(max_length=20)
    income  = models.DecimalField(max_digits=10 ,decimal_places=2)
    gender = models.CharField(max_length=30, null=True, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    birth_place = models.CharField(max_length=255)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE)
    educational_attainment = models.ForeignKey(EducationalAttainment, on_delete=models.CASCADE)
    employment_status = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE)
    family = models.ManyToManyField(Family)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=["name"])]
        ordering = ["name"]