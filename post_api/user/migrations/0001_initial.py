# Generated by Django 3.1 on 2020-12-21 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('suite', models.IntegerField()),
                ('city', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
            ],
        ),
    ]
