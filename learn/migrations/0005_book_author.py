# Generated by Django 3.0.6 on 2020-06-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20200529_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
