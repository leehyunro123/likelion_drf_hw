from django.shortcuts import render

# Create your views here.
from rest_framework import response
from rest_framework.decorators import api_view
from .models import Songs, Singers
from .serializers import SongSerializer, SingerSerializer

from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongSerializer(songs, many=True)
        return response.Response(data=serializer.data)

    if request.method == 'POST':
        singer_name = request.data.get('singer')
        singer = get_object_or_404(Singers, name=singer_name)
        
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(singer=singer)
            return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.errors, status=400)

@api_view(['GET', 'POST'])
def singer_list(request):
    if request.method == 'GET':
        singers = Singers.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return response.Response(data=serializer.data)

    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return response.Response(data=serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def singer_detail(request, singer_id):
    singer = get_object_or_404(Singers, id=singer_id)
    
    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return response.Response(data=serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SingerSerializer(singer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data)
        return response.Response(data=serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        singer_id = singer.id
        singer.delete()
        return response.Response(data={'id': singer_id, 'message': '가수가 성공적으로 삭제되었습니다.'})
