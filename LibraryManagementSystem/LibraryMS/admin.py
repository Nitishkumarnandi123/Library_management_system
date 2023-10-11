from django.contrib import admin
from .models import Course, Semester, Author, Book

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Author)
admin.site.register(Book)


