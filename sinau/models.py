from django.db import models
from django.db.models import indexes
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.fields import NOT_PROVIDED
from video_encoding.fields import VideoField, ImageField
from video_encoding.models import Format

# Create your models here.
class Sinau(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    tipe = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# https://www.youtube.com/watch?v=m6chqKlhpPo
# https://github.com/escaped/django-video-encoding
class Video(models.Model):
    sinau = models.ForeignKey(Sinau, on_delete=models.DO_NOTHING, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    thumbnail = ImageField(blank=True)
    duration = models.FloatField(editable=False, null=True)
    file = VideoField(width_field='width', height_field='height',
                        duration_field='duration')
    format_set = GenericRelation(Format)
    created_at = models.DateTimeField(auto_now=True)