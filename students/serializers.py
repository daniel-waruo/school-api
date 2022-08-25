import base64
import uuid

from django.core.files import File
from django.core.files.base import ContentFile
from rest_framework import serializers

from root.utils import SerializerImageCharField
from students.models import Student, Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """Enter Images as Base 64 and save to Bucket"""
    profile_photo = SerializerImageCharField()

    class Meta:
        model = Student
        fields = '__all__'

    def save(self, **kwargs):
        # save image
        profile_photo = self.validated_data["profile_photo"]
        student_name = self.validated_data["first_name"]
        # convert Base 64 to a savable image
        image_format, image_string = profile_photo.split(';base64,')
        ext = image_format.split('/')[-1]
        # save image and a unique UUID field
        data = ContentFile(base64.b64decode(image_string))
        file_name = f"{student_name}_{str(uuid.uuid4())}." + ext
        profile_photo = File(file=data, name=file_name)
        # replace file field with an Image instance
        self.validated_data["profile_photo"] = profile_photo
        return super().save(**kwargs)
