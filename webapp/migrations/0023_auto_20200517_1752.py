# Generated by Django 3.0.3 on 2020-05-17 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_auto_20200517_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merge',
            old_name='dates',
            new_name='a_date',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='time',
            new_name='a_time',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='hospital',
            new_name='hospital_name',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='age',
            new_name='p_age',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='disease',
            new_name='p_disease',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='email',
            new_name='p_email',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='gender',
            new_name='p_gender',
        ),
        migrations.RenameField(
            model_name='merge',
            old_name='ph_no',
            new_name='p_ph_no',
        ),
    ]
