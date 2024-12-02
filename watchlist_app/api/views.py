from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import WatchList, StreamPlatform


class StreamPlatformListAV(APIView):
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
        
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#@api_view(['GET', 'POST'])
#def movie_list(request):
#    if request.method == 'GET':
#        movies = WatchList.objects.all()
#        serializer = WatchListSerializer(movies, many=True)
#        return Response(serializer.data)
#    
#    if request.method == 'POST':
#        serializer = WatchListSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def movie_details(request, pk):
#    if request.method == 'GET':
#        try:
#            movie = WatchList.objects.get(pk=pk)
#        except WatchList.DoesNotExist:
#            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#        
#        serializer = WatchListSerializer(movie)
#        return Response(serializer.data)
#    
#    if request.method == 'PUT':
#        movie = WatchList.objects.get(pk=pk)
#        serializer = WatchListSerializer(movie, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#        
#    if request.method == 'DELETE':
#        movie = WatchList.objects.get(pk=pk)
#        movie.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)