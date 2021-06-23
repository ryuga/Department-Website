# Generated by Django 3.2.4 on 2021-06-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_gallery_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='tags',
            field=models.ManyToManyField(null=True, to='web.Tag'),
        ),
    ]
