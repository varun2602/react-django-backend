# Generated by Django 5.0.3 on 2024-04-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('teacher', 'Teacher')], max_length=20, null=True),
        ),
    ]
