# Generated by Django 3.1.3 on 2020-11-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]