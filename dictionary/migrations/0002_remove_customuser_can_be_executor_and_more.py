# Generated by Django 5.0.4 on 2024-04-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='can_be_executor',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar'),
        ),
    ]
