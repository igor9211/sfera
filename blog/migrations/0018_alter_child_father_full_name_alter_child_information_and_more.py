# Generated by Django 4.0.3 on 2022-04-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_child_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='father_full_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='child',
            name='information',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='mother_full_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='child',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
    ]