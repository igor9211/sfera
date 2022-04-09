from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'), )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    comments = models.TextField(null=True, blank=True)
    objects = models.Manager() #menadzer domyslny
    published = PublishedManager()  # Menadżer niestandardowy
    # tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[
            self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug
        ])


class Main(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title


def upload_gallery_image(instance, filename):
    return f"media/{instance}/gallery/{filename}"


class Child(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    id_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    mother_full_name = models.CharField(max_length=40, null=True, blank=True)
    father_full_name = models.CharField(max_length=40, null=True, blank=True)
    # phone_1 = PhoneNumberField(null=False, blank=False)
    # phone_2 = PhoneNumberField(blank=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to=upload_gallery_image, null=True, blank=True)
    information = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id_name)




