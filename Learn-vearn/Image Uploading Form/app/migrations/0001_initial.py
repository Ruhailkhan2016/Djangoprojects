# Generated by Django 4.0.5 on 2022-07-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagename', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]