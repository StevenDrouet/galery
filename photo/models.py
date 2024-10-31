from django.db.models import Model, UUIDField, CharField, ImageField, DateTimeField

from utils import make_uuid


class Photo(Model):
    '''Fields for Photo model'''
    id = UUIDField(primary_key=True, default=make_uuid, editable=False, unique=True)
    name = CharField(max_length=100)
    photo = ImageField(upload_to='photos/')
    uploaded_at = DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name