# Generated by Django 4.0.3 on 2022-04-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_child_date_of_birth_alter_child_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='phone_1',
        ),
        migrations.RemoveField(
            model_name='child',
            name='phone_2',
        ),
        migrations.AlterField(
            model_name='child',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='child',
            name='father_full_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='child',
            name='mother_full_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
