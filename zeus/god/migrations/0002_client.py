# Generated by Django 2.2.7 on 2019-11-27 20:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('god', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('checkInTime', models.DateTimeField(auto_now_add=True)),
                ('checkOutTime', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
