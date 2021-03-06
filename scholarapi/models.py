from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name="Course Name")

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=250, verbose_name="College Name")
    place = models.CharField(max_length=250, verbose_name="Location")
    address = models.CharField(max_length=350, verbose_name="Address")
    affiliated_university = models.CharField(
        max_length=200, verbose_name="Affiliated University", default='')
    courses = models.ManyToManyField(
        Course, default="", verbose_name="Available Courses")
    college_image = models.FileField(
        upload_to="colleges/", null=True, verbose_name="College Image")
    fee_brochure = models.FileField(
        upload_to="fees/", null=True, verbose_name="Fees Brochure")

    def __str__(self):
        return self.name


class Applicant(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="First Name")
    last_name = models.CharField(max_length=250, verbose_name="Last Name")
    phone = models.IntegerField(default=0)
    email = models.EmailField(
        max_length=250, unique=True, blank=True, null=True)
    college = models.ForeignKey(
        College, null=True, on_delete=models.SET_NULL, verbose_name="College Name")
    course = models.ForeignKey(
        Course, null=True, on_delete=models.SET_NULL, verbose_name="Course Name")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Carousel(models.Model):
    carousel_image = models.FileField(
        upload_to="carousels/", null=True, verbose_name="Carousel Image")
    carousel_heading = models.CharField(max_length=500, verbose_name="Heading")
    carousel_description = models.CharField(
        max_length=500, verbose_name="Description")
