from django.db import models

# Create your models here.
class Course(models.Model):
    cname = models.CharField(max_length=20)

    def __str__(self):
        return self.cname


class Semester(models.Model):
    sname = models.CharField(max_length=30)

    def __str__(self):
        return self.sname


class Author(models.Model):
    autname = models.CharField(max_length=30)

    def __str__(self):
        return self.autname


class Book(models.Model):
    bname = models.CharField(max_length=30)
    auther = models.ForeignKey(Author,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.bname









