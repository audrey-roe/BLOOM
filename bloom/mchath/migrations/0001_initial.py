# Generated by Django 4.1.1 on 2022-09-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caregiver_name', models.CharField(max_length=200)),
                ('child_age', models.PositiveIntegerField()),
                ('child_name', models.CharField(max_length=200)),
                ('relation_to_child', models.CharField(max_length=200)),
                ('caregiver_email', models.EmailField(max_length=50)),
                ('caregiver_phone', models.BigIntegerField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
