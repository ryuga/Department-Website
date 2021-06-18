# Generated by Django 3.2.4 on 2021-06-18 12:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
                ('designation', models.CharField(max_length=30)),
                ('quote', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(blank=True, help_text='Leave empty to auto create or add custom', max_length=50, null=True)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('student_count', models.IntegerField(default=35)),
                ('language', models.CharField(default='English/Malayalam', max_length=40)),
                ('duration', models.CharField(default='3 years', max_length=15)),
                ('first_year_syllabus', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=35), blank=True, help_text='Add multiple module names separated by comma', null=True, size=None)),
                ('second_year_syllabus', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=35), blank=True, help_text='Add multiple module names separated by comma', null=True, size=None)),
                ('third_year_syllabus', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=35), blank=True, help_text='Add multiple module names separated by comma', null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, help_text='Leave empty to auto create or add custom', max_length=100, null=True)),
                ('designation', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.SlugField(blank=True, help_text='Leave empty to auto create or add custom', max_length=30, null=True, unique=True)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('live', 'Live'), ('ended', 'Ended')], default='upcoming', max_length=10)),
                ('image_url', models.URLField()),
                ('venue', models.CharField(max_length=30)),
                ('topic', models.CharField(blank=True, max_length=30, null=True)),
                ('host', models.CharField(blank=True, max_length=30, null=True)),
                ('skill_level', models.CharField(blank=True, choices=[('Open for all', 'Open for all'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=30, null=True)),
                ('description', models.TextField()),
                ('markdown_content', models.TextField(blank=True, help_text='Markdown content if any', null=True)),
                ('facebook_page_link', models.URLField(blank=True, help_text='Optional', null=True)),
                ('instagram_page_link', models.URLField(blank=True, help_text='Optional', null=True)),
                ('twitter_link', models.URLField(blank=True, help_text='Optional', null=True)),
                ('staff_in_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.faculty')),
            ],
        ),
    ]
