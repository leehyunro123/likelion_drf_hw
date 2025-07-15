from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Singers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    debut = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)


class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singers, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100)
    release = models.TextField()
    content = models.TextField()
