from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from photo.models import Photo
from .serializers import PhotoSerializer

class PhotoViewSet(ViewSet):
    '''API view for Photo'''
    lookup_field = 'pk'


    def list(self, request):
        '''
            Endpoint: GET /photos
            Description: List all photos
        '''
        photos = Photo.objects.all().order_by('-uploaded_at')
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    def retrieve(self, request, pk=None):
        '''
            Endpoint: GET /photos/<pk>
            Description: Retrieve a single photo by ID
        '''
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=HTTP_200_OK)
        except Photo.DoesNotExist:
            return Response({'message': 'Photo not found'}, status=HTTP_404_NOT_FOUND)


    def create(self, request):
        '''
            Endpoint: POST /photos
            Description: Create a new photo
        '''
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        '''
            Endpoint: PUT /photos/<pk>
            Description: Update a photo by ID
        '''
        try:
            photo = Photo.objects.get(pk=pk)
            serializer = PhotoSerializer(photo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Photo.DoesNotExist:
            return Response({'message': 'Photo not found'}, status=HTTP_404_NOT_FOUND)



    def destroy(self, request, pk=None):
        '''
            Endpoint: DELETE /photos/<pk>
            Description: Delete a photo by ID
        '''
        try:
            photo = Photo.objects.get(pk=pk)
            photo.delete()
            return Response({'message': 'Photo deleted'}, status=HTTP_200_OK)
        except Photo.DoesNotExist:
            return Response({'message': 'Photo not found'}, status=HTTP_404_NOT_FOUND)
