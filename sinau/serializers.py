from django.db.models import fields
from rest_framework import serializers
from .models import Sinau, Video
from sinau import models

class SinauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinau
        fields = ("name", "tipe")

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("sinau", "width", "height", "thumbnail", "duration", "file", "format_set")

        