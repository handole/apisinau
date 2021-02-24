from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rq import enqueue
from typing import Type
from .models import Video

from . import tasks
from .models import Video


@receiver(post_save, sender=Video)
def create_thumbnail(sender, instance, **kwargs):
    enqueue(tasks.create_thumbnail, instance.pk)

@receiver(signals.encoding_finished, sender=Video)
def mark_as_finished(sender:Type[Video], instance: Video) -> None:
    """
    Mark video as "convertion has been finished".
    """
    video.processed = True
    video.save(update_fields=['processed'])