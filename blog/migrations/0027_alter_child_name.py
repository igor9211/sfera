# Generated by Django 4.0.3 on 2022-04-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_child_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]