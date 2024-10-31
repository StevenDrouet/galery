from django.contrib.admin import register, ModelAdmin
from .models import Photo

@register(Photo)
class PhotoAdmin(ModelAdmin):
    '''Photo admin'''
    model = Photo
    list_display = ('name', 'uploaded_at')
    search_fields = ('name',)
