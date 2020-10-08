# Generated by Django 3.1.1 on 2020-10-08 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town_name', models.JSONField(null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('date_started', models.DateTimeField()),
                ('date_finished', models.DateTimeField()),
                ('is_completed', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lighttown.town')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=300)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lighttown.house')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]