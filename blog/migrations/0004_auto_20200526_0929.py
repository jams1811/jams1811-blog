# Generated by Django 3.0.6 on 2020-05-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200526_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='portfolio/images'),
        ),
    ]
