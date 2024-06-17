# Generated by Django 4.0.6 on 2023-04-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookyourtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('date', models.DateField(max_length=20)),
                ('time', models.TimeField(max_length=20)),
                ('person', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Compititiveprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='images/')),
                ('price', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FreshAndOrganicBeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='images/')),
                ('name', models.CharField(max_length=40)),
                ('details', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ourclientssay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='images/')),
                ('name', models.CharField(max_length=40)),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specialoffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]