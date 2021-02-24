from django.shortcuts import render
from .models import Sinau, Video
from .serializers import SinauSerializer, VideoSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sinau import serializers

# Create your views here.
@api_view(["POST"])
def add_sinau(request):
    name = request.data["name"]
    tipe = request.data["tipe"]
    sin = Sinau(name=name, tipe=tipe)
    sin.save()
    return Response(SinauSerializer(sin).data)

@api_view(["GET"])
def sinaus(request):
    sin = Sinau.objects.all()
    serializer = SinauSerializer(sin, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_video(request, id):
    width = ""
    height = ""
    thumbnail = ""
    duration = ""
    file = ""
    if "width" in request.data:
        width = request.data["width"]
    if "height" in request.data:
        height = request.data["height"]
    if "thumbnail" in request.data:
        thumbnail = request.data["thumbnail"]
    if "duration" in request.data:
        duration = request.data["duration"]
    if "file" in request.data:
        file = request.data["file"]
    sin = Sinau.objects.get(id=id)
    vid = Video(sinau=sin, width=width, height=height, thumbnail=thumbnail, duration=duration, file=file)
    vid.save()
    return Response(VideoSerializer(vid).data)


@api_view(["GET"])
def videos(request):
    vid = Video.objects.all()
    serializer = VideoSerializer(vid, many=True)
    return Response(serializer)
