# Generated by Django 3.0.3 on 2020-04-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data1',
            name='fee',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='data1',
            name='password',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='data1',
            name='res_code',
            field=models.IntegerField(max_length=30),
        ),
    ]