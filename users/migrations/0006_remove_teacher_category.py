# Generated by Django 4.1 on 2023-01-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_teacher_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='category',
        ),
    ]
