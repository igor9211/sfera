# Generated by Django 4.0.3 on 2022-04-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_rename_lastname_child_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
