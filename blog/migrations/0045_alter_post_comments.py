# Generated by Django 4.0.3 on 2022-04-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
