from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField

from .models import File

class FilepdfAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name','text')


class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']