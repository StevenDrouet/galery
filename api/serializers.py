from rest_framework.serializers import CharField, ModelSerializer, ImageField

from photo.models import Photo

class PhotoSerializer(ModelSerializer):
    '''Serializer for Photo data'''
    name = CharField(required=True, max_length=100, min_length=1)
    photo = ImageField(required=True)  

    class Meta:
        model = Photo
        fields = ['name', 'photo']