# Generated by Django 4.0.3 on 2022-04-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_child_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
