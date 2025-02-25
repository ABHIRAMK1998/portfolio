# Generated by Django 4.2.11 on 2024-05-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='certifications',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_showcase',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='work_experience',
            field=models.TextField(blank=True),
        ),
    ]
