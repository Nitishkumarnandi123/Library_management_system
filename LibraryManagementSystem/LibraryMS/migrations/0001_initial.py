# Generated by Django 4.2.4 on 2023-09-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryMS.author')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryMS.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryMS.semester')),
            ],
        ),
    ]