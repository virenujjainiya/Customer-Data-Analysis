# Generated by Django 3.2.3 on 2021-06-06 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csvs')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
