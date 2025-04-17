# Generated by Django 5.2 on 2025-04-16 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('age', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
                ('street_name', models.CharField(blank=True, max_length=500)),
                ('resident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helloworld.person')),
            ],
        ),
    ]
