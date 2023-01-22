# Generated by Django 3.2.5 on 2021-11-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=20)),
                ('lname', models.TextField(max_length=20)),
                ('emai', models.EmailField(max_length=254)),
                ('passw', models.TextField(max_length=300)),
                ('city', models.CharField(default='Not provided', max_length=20)),
                ('number', models.IntegerField(default='00000')),
            ],
        ),
        migrations.CreateModel(
            name='Donator_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emai', models.EmailField(default=1, max_length=254, null=True)),
                ('for_class', models.CharField(max_length=10)),
                ('subjects', models.TextField(default='Not provided', max_length=50, null=True)),
                ('number_of_books', models.CharField(max_length=10)),
                ('edition', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]