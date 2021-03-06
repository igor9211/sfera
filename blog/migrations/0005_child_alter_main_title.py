# Generated by Django 4.0.3 on 2022-04-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_main_alter_post_managers_remove_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('mother_full_name', models.CharField(max_length=40)),
                ('father_full_name', models.CharField(max_length=40)),
                ('phone_1', models.IntegerField()),
                ('phone_2', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('information', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='main',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
