# Generated by Django 4.0.3 on 2022-04-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_child_father_full_name_alter_child_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]