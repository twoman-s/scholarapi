from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name="Course Name")
    semesters = models.CharField(max_length=250)
    fees = models.IntegerField(default=0, verbose_name="Course Fee")
    # fee_brochure = models.FileField()
    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=250, verbose_name="College Name")
    place = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=350)
    email = models.EmailField(max_length=250, unique=True, blank=True, null=True)
    courses = models.ManyToManyField(Course, default="")

    def __str__(self):
        return self.name


class Applicant(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="First Name")
    last_name = models.CharField(max_length=250, verbose_name="Last Name")
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=250, unique=True, blank=True, null=True)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL, verbose_name="College Name")
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name="Course Name")

    def __str__(self):
        return self.first_name + " " + self.last_name
