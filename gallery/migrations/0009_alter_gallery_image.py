# Generated by Django 4.0.3 on 2022-04-04 18:35

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_alter_events_date_of_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to=gallery.models.upload_gallery_image),
        ),
    ]