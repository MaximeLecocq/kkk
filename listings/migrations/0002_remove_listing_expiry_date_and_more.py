# Generated by Django 5.0.6 on 2024-08-18 10:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='listing',
            name='expiry_date_beverages',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='expiry_date_canned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='expiry_date_dry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='categories',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]