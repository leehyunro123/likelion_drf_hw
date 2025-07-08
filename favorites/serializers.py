from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)
    
    songs = serializers.SerializerMethodField(read_only =True)
    
    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs, many = True)
        return serializers.data
    
    class Meta:
        model = Singers
        fields = '__all__'
        
class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source='singer.name', read_only=True)
    
    class Meta:
        model = Songs
        fields = ['id', 'singer', 'singer_name', 'title', 'release', 'content']
        read_only_fields = ['singer']