# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant_registrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Registrar', max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('hostel', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Computer Center', max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('department', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Gymkhana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Gymkhana', max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('department', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Library', max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Stud_Faculty_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Stud_Lab_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('roll_no', models.IntegerField(default=0)),
                ('hostel', models.CharField(blank=True, max_length=250)),
                ('department', models.CharField(blank=True, max_length=250)),
                ('caretaker_approval', models.BooleanField(default=False)),
                ('warden_approval', models.BooleanField(default=False)),
                ('HOD_approval', models.BooleanField(default=False)),
                ('assistant_registrar_approval', models.BooleanField(default=False)),
                ('CC_approval', models.BooleanField(default=False)),
                ('library_approval', models.BooleanField(default=False)),
                ('faculty_approval', models.ManyToManyField(through='main.Stud_Faculty_Status', to='main.Faculty')),
                ('lab_approval', models.ManyToManyField(through='main.Stud_Lab_Status', to='main.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('webmail', models.CharField(blank=True, max_length=250, unique=True)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('hostel', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='stud_lab_status',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
        migrations.AddField(
            model_name='stud_faculty_status',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
    ]
