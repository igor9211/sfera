from django.db import models
from django.utils import timezone
from django.urls import reverse


class Events(models.Model):
    STATUS = (('draft', 'Draft'), ('published', 'Published'))
    id = models.BigAutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    information = models.TextField()
    # slug = models.SlugField(max_length=250, unique_for_date='publish', auto_created=True)
    date_of_event = models.DateField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery:gallery_detail', args=[self.id, self.name])


def upload_gallery_image(instance, filename):
    return f"media/{instance.event.name}/gallery/{filename}"


class Gallery(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='image')

