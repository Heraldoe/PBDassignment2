# Generated by Django 4.1 on 2022-09-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemwatchlist',
            name='rating',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='itemwatchlist',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
    ]
